#!/bin/bash
#
# Run Pulumi to update the stack targeted by the given branch.

set -o errexit -o pipefail
cd "$(dirname "${BASH_SOURCE}")/.."

if [ -z ${1:-} ]; then
    echo "Usage: $0 [ preview | update ]"
    exit 1
fi

source ./scripts/common.sh

export PULUMI_ACTION=${1}

# Run a Pulumi command, retrying it only if it failed because another update holds
# the stack lock:
#
#     error: [409] Conflict: Another update is currently in progress.
#
# The service returns that before touching any resource, so there is nothing
# half-applied to reason about -- a later attempt simply re-plans against current
# state. That is why this is safe to retry and a general-purpose retry around
# `pulumi up` would not be.
#
# Only the lock conflict is retried. Any other failure returns immediately, so a
# genuine error still fails fast instead of burning several minutes of backoff
# before anyone sees it.
#
# scripts/await-in-progress.js tries to avoid the collision upstream, but it gives
# up after 45 minutes and proceeds regardless, and every run of a merge train
# reaches that cap at once -- on 2026-09-21 three runs did, and all three took a
# 409 within 40 seconds of each other. This is the backstop for that, and for a
# lock held from outside Actions entirely (scripts/laptop-deploy.sh, or a console
# operation). The backoff below tolerates roughly 7.5 minutes of contention.
retry_on_stack_lock() {
    # Overridable so the behavior can be exercised without a 7-minute test.
    local max_attempts=${PULUMI_LOCK_MAX_ATTEMPTS:-5}
    local delay=${PULUMI_LOCK_RETRY_DELAY:-30}
    local attempt=1
    local log status

    # Failures are handled explicitly below, so errexit has to be off for the loop.
    # Save whether the caller had it and restore that exact state before returning --
    # switching it on unconditionally would silently change the caller's semantics.
    local restore_errexit=0
    case $- in *e*) restore_errexit=1; set +o errexit ;; esac

    log="$(mktemp)"

    while true; do
        # tee so the command still streams into the job log live; PIPESTATUS[0]
        # because pipefail would otherwise report tee's status, not the command's.
        "$@" 2>&1 | tee "${log}"
        status=${PIPESTATUS[0]}

        # Succeeded, or failed for some reason other than the lock. Done either way.
        if [ "${status}" -eq 0 ] || ! grep -q "Another update is currently in progress" "${log}"; then
            break
        fi

        if [ "${attempt}" -ge "${max_attempts}" ]; then
            echo "Stack still locked after ${max_attempts} attempts; giving up." >&2
            break
        fi

        echo "Stack is locked by another update; retrying in ${delay}s (attempt $((attempt + 1))/${max_attempts})."
        sleep "${delay}"
        attempt=$((attempt + 1))
        delay=$((delay * 2))
    done

    rm -f "${log}"
    if [ "${restore_errexit}" -eq 1 ]; then
        set -o errexit
    fi
    return "${status}"
}

case ${PULUMI_ACTION} in
    preview)
        pulumi -C infrastructure preview
        ;;
    update)
        # `pulumi up` on this program IS the publish step: it swings the live CloudFront
        # origin to whichever bucket ./origin-bucket-metadata.json names. Refuse to do
        # that if a newer run has already published, which the queueing in
        # await-in-progress.js makes unlikely but cannot prevent.
        #
        # This has to run immediately before the update and nowhere else, because the
        # race it detects only resolves at publish time. If a retry loop is ever wrapped
        # around the `pulumi up` below -- e.g. to survive a `[409] Conflict` -- this call
        # belongs INSIDE it: the run that won the conflict is exactly the newer run this
        # check exists to avoid overwriting. It is cheap and idempotent, so re-running it
        # per attempt costs nothing.
        node ./scripts/check-publish-ordering.js

        # Given how frequently we update the CloudFront distribution, and how easy it can
        # be for our checkpointed CloudFront Etag to fall out of sync with what's current,
        # we refresh the distribution on every update.
        retry_on_stack_lock pulumi -C infrastructure refresh -t "${CDN_PULUMI_URN}" --yes

        retry_on_stack_lock pulumi -C infrastructure up --yes

        # Invalidate CloudFront cache after deploy so updated content is served immediately.
        # Only invalidate HTML and non-fingerprinted paths. Fingerprinted assets (css, js,
        # images under /fingerprinted/) use content-hash URLs and don't need invalidation.
        #
        # Each section is listed twice, as "/x/" and "/x/*": the glob matches everything
        # below /x/ but not /x/ itself, which left every section landing page
        # uninvalidated.
        DISTRIBUTION_ID=$(pulumi -C infrastructure stack output cloudFrontDistributionId 2>/dev/null || true)
        if [ -n "${DISTRIBUTION_ID}" ]; then
            echo "Invalidating CloudFront cache for distribution ${DISTRIBUTION_ID}..."
            if aws cloudfront create-invalidation \
                --distribution-id "${DISTRIBUTION_ID}" \
                --paths \
                    "/docs/" "/docs/*" \
                    "/registry/" "/registry/*" \
                    "/blog/" "/blog/*" \
                    "/tutorials/" "/tutorials/*" \
                    "/learn/" "/learn/*" \
                    "/dev/" "/dev/*" \
                    "/guides/" "/guides/*" \
                    "/product/" "/product/*" \
                    "/pricing/" "/pricing/*" \
                    "/contact/" "/contact/*" \
                    "/index.html" "/"; then
                echo "CloudFront cache invalidation submitted successfully."
            else
                echo "WARNING: CloudFront cache invalidation failed. Content will refresh within 30 minutes."
            fi
        fi
        ;;
    *)
        echo "Unknown action '${PULUMI_ACTION}'"
        exit 1
        ;;
esac
