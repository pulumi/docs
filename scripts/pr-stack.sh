#!/bin/bash
#
# Manage the per-PR copy of the www.pulumi.com stack that an infra PR deploys to.
#
# A PR that changes the deploy itself (the paths under `staging_evidence:` in
# .github/review-routing.yml) gets its own full stack, www-pr-<n>, served at
# https://pr-<n>.<PR_STACK_DOMAIN_SUFFIX>. testing-build-and-deploy.yml runs `make
# ci_push` against it, which is the same path production takes. pulumi-test.io
# (www-testing) only ever takes master, so it stays a faithful mirror of production.
#
# Usage:
#
#   ./scripts/pr-stack.sh name <pr>        # Print the stack name (pulumi/www-pr-<pr>).
#   ./scripts/pr-stack.sh domain <pr>      # Print the site's domain.
#   ./scripts/pr-stack.sh configure <pr>   # Create the stack if needed and write its config.
#   ./scripts/pr-stack.sh destroy <pr>     # Tear the stack down, and remove it once empty.
#   ./scripts/pr-stack.sh closed           # Print the PR numbers of stacks whose PR is closed.
#
# Environment (repository variables, passed in by the workflows):
#
#   PR_STACK_DOMAIN_SUFFIX     Required for configure. The site is pr-<n>.<suffix>.
#   PR_STACK_CERTIFICATE_ARN   Required for configure. A us-east-1 ACM certificate that
#                              covers *.<suffix>.
#   PR_STACK_HOSTED_ZONE       Optional. The Route 53 zone the record goes in. Defaults to
#                              the suffix.
#   PR_STACK_TEMPLATE          Optional. The stack whose config is copied. Defaults to
#                              pulumi/www-testing.
#
# The stack's config file is never committed. `configure` rebuilds it from the template
# on every run, so a fresh checkout (every CI job) can always deploy or destroy it, and
# a key added to the testing stack reaches PR stacks without anyone remembering to.

set -o errexit -o pipefail

cd "$(dirname "${BASH_SOURCE}")/.."

readonly ORG="pulumi"
readonly STACK_PREFIX="www-pr-"

usage() {
    echo "usage: $0 { name <pr> | domain <pr> | configure <pr> | destroy <pr> | closed }" >&2
    exit 2
}

require_pr_number() {
    if [[ ! "${1:-}" =~ ^[0-9]+$ ]]; then
        echo "error: expected a PR number, got '${1:-}'" >&2
        exit 2
    fi
}

stack_name() {
    echo "${ORG}/${STACK_PREFIX}$1"
}

domain() {
    if [ -z "${PR_STACK_DOMAIN_SUFFIX:-}" ]; then
        echo "error: PR_STACK_DOMAIN_SUFFIX is not set. Set the repository variable to the domain PR stacks live under." >&2
        exit 1
    fi
    echo "pr-$1.${PR_STACK_DOMAIN_SUFFIX}"
}

stack_exists() {
    pulumi -C infrastructure stack ls --json 2>/dev/null \
        | jq -e --arg name "${STACK_PREFIX}$1" 'any(.[]; .name == $name or (.name | endswith("/" + $name)))' > /dev/null
}

configure() {
    local pr="$1" stack site template
    stack="$(stack_name "$pr")"
    site="$(domain "$pr")"
    template="${PR_STACK_TEMPLATE:-${ORG}/www-testing}"

    if [ -z "${PR_STACK_CERTIFICATE_ARN:-}" ]; then
        echo "error: PR_STACK_CERTIFICATE_ARN is not set. Set the repository variable to a us-east-1 ACM certificate for *.${PR_STACK_DOMAIN_SUFFIX}." >&2
        exit 1
    fi

    pulumi -C infrastructure stack select --create "$stack"

    # Start from exactly what the testing stack has, then override what has to differ.
    rm -f "infrastructure/Pulumi.${STACK_PREFIX}${pr}.yaml"
    pulumi -C infrastructure config cp --stack "$template" --dest "$stack"

    local -a set=(
        "websiteDomain=${site}"
        "certificateArn=${PR_STACK_CERTIFICATE_ARN}"
        "hostedZone=${PR_STACK_HOSTED_ZONE:-${PR_STACK_DOMAIN_SUFFIX}}"
        # The zone is shared, so the record is pr-<n> inside it, not the zone's apex.
        "setRootRecord=false"
        # Bucket names are global; the testing stack's would collide.
        "websiteLogsBucketName=${site//./-}-logs"
        "makeFallbackBucket=false"
        # Account-level resources that belong to the long-lived stacks only.
        "enableWaf=false"
        "enableDataWarehouseAccess=false"
    )
    for kv in "${set[@]}"; do
        pulumi -C infrastructure config set --stack "$stack" "${kv%%=*}" "${kv#*=}"
    done

    for key in cdnLogDeliverySourceName supportRedirectDomain marketingPortalStack originBucketNameOverride redirectDomain; do
        pulumi -C infrastructure config rm --stack "$stack" "$key" 2> /dev/null || true
    done

    echo "Configured ${stack} for https://${site}"
}

destroy() {
    local pr="$1" stack remaining
    stack="$(stack_name "$pr")"

    if ! stack_exists "$pr"; then
        echo "No stack ${stack}; nothing to destroy."
        return 0
    fi

    configure "$pr"

    # The program protects the distribution, the DNS record, and the logs bucket so a
    # long-lived stack can't lose them by accident. A PR stack is meant to go away.
    pulumi -C infrastructure state unprotect --stack "$stack" --all --yes

    # AWS won't delete a Lambda@Edge function until it has cleared the replicas, which
    # can take hours after the distribution is gone. Keep going past that and leave the
    # stack in place; pr-stack-sweep.yml retries until it's empty.
    pulumi -C infrastructure destroy --stack "$stack" --yes --skip-preview --continue-on-error || true

    remaining="$(pulumi -C infrastructure stack export --stack "$stack" \
        | jq '[.deployment.resources // [] | .[] | select(.type != "pulumi:pulumi:Stack" and (.type | startswith("pulumi:providers:") | not))] | length')"
    if [ "$remaining" -gt 0 ]; then
        echo "::warning::${stack} still has ${remaining} resource(s), most likely Lambda@Edge functions AWS hasn't released yet. pr-stack-sweep.yml will retry."
        return 0
    fi

    pulumi -C infrastructure stack rm --stack "$stack" --yes
    echo "Removed ${stack}."
}

# PR numbers of www-pr-* stacks whose PR is no longer open. Needs GH_TOKEN and GITHUB_REPOSITORY.
closed() {
    local pr state
    pulumi -C infrastructure stack ls --json \
        | jq -r --arg p "$STACK_PREFIX" '.[].name | split("/") | last | select(startswith($p)) | ltrimstr($p)' \
        | while read -r pr; do
            [[ "$pr" =~ ^[0-9]+$ ]] || continue
            state="$(gh api "repos/${GITHUB_REPOSITORY}/pulls/${pr}" --jq .state 2> /dev/null || echo unknown)"
            if [ "$state" == "closed" ]; then
                echo "$pr"
            fi
        done
}

case "${1:-}" in
    name)      require_pr_number "${2:-}"; stack_name "$2" ;;
    domain)    require_pr_number "${2:-}"; domain "$2" ;;
    configure) require_pr_number "${2:-}"; configure "$2" ;;
    destroy)   require_pr_number "${2:-}"; destroy "$2" ;;
    closed)    closed ;;
    *)         usage ;;
esac
