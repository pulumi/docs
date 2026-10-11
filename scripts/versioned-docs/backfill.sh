#!/usr/bin/env bash
#
# backfill.sh — drive a full versioned-docs back-catalog backfill for one environment.
#
# For each tool it dispatches that tool's doc-gen workflow once per historical version
# (publish_only, so no latest-docs PR), waits for the archives to land in the bucket, then
# reconciles the manifest ONCE with rebuild-manifest.sh (race-proof — see BUG note there), and
# verifies. This is the "queue up the back library" runbook step; it is the same process that
# built the testing catalog, parameterized by --env.
#
# WHAT TO BACKFILL is read from a source manifest (default: the testing site). Each tool's
# versions.json already carries label + liveRoot + the exact archived version list, so this
# script derives the whole spec from it — the only hardcoded thing is tool -> workflow.
#
# AUTH / where each phase runs:
#   * dispatch  — `gh workflow run` (publishes via the workflow's OIDC role; needs gh auth)
#   * resolve   — `pulumi stack output` for the target bucket + distribution (needs pulumi auth)
#   * wait/verify/reconcile — local `aws`/`curl` (needs admin AWS creds for the target account)
# Pin AWS_PROFILE to the TARGET env's admin profile before running.
#
# Usage:
#   scripts/versioned-docs/backfill.sh --env testing [--dry-run]
#   scripts/versioned-docs/backfill.sh --env production --yes
#   scripts/versioned-docs/backfill.sh --env production --tools "pulumi-cli nodejs" --reconcile-only
#
# Flags:
#   --env testing|production     (required) target environment
#   --source-base URL            where to read the spec manifests (default https://www.pulumi-test.io)
#   --tools "a b c"              subset of tool ids (default: all 10)
#   --ref REF                    git ref to dispatch workflows from (default: current branch)
#   --latest TOOL=vX.Y.Z         override the "latest" (live) version for a tool's manifest (repeatable)
#   --stagger SECONDS            delay between dispatches (default 10)
#   --wait-timeout SECONDS       max time to wait for archives to land (default 3600)
#   --skip-existing / --no-skip-existing  skip versions already in the target bucket (default: skip)
#   --dry-run                    print the plan; dispatch/reconcile nothing
#   --dispatch-only              dispatch + wait, skip reconcile/verify
#   --reconcile-only             skip dispatch + wait, just rebuild-manifest + verify
#   --yes                        required to actually dispatch/reconcile against production
#
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# The one thing not derivable from a manifest: which workflow generates each tool.
declare -A WORKFLOW=(
  [pulumi-cli]=pulumi-cli-docs.yml
  [nodejs]=pulumi-sdk-typescript-docs.yml
  [python]=pulumi-sdk-python-docs.yml
  [dotnet]=pulumi-sdk-dotnet-docs.yml
  [java]=pulumi-sdk-java-docs.yml
  [nodejs-policy]=pulumi-policy-sdk-typescript-docs.yml
  [python-policy]=pulumi-policy-sdk-python-docs.yml
  [nodejs-esc-sdk]=pulumi-esc-sdk-typescript-docs.yml
  [python-esc-sdk]=pulumi-esc-sdk-python-docs.yml
  [dotnet-esc-sdk]=pulumi-esc-sdk-dotnet-docs.yml
)
ALL_TOOLS="pulumi-cli nodejs python dotnet java nodejs-policy python-policy nodejs-esc-sdk python-esc-sdk dotnet-esc-sdk"

# Source repo per tool — used by --versions-from tags to enumerate the REAL release history
# (one archive per major.minor, deepest first). label/liveRoot/latest still come from the
# source manifest; only the version LIST is repo-derived in tags mode.
declare -A REPO=(
  [pulumi-cli]=pulumi/pulumi
  [nodejs]=pulumi/pulumi
  [python]=pulumi/pulumi
  [dotnet]=pulumi/pulumi-dotnet
  [java]=pulumi/pulumi-java
  [nodejs-policy]=pulumi/pulumi-policy
  [python-policy]=pulumi/pulumi-policy
  [nodejs-esc-sdk]=pulumi/esc-sdk
  [python-esc-sdk]=pulumi/esc-sdk
  [dotnet-esc-sdk]=pulumi/esc-sdk
)

ENV=""; SOURCE_BASE="https://www.pulumi-test.io"; TOOLS=""; REF=""
STAGGER=10; WAIT_TIMEOUT=3600; SKIP_EXISTING=true
VERSIONS_FROM="tags"; MIN_VERSION=""; MAX_MINORS=""
DRY_RUN=false; DISPATCH=true; RECONCILE=true; YES=false
declare -A LATEST_OVERRIDE=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --env)             ENV="$2"; shift 2;;
    --source-base)     SOURCE_BASE="${2%/}"; shift 2;;
    --tools)           TOOLS="$2"; shift 2;;
    --ref)             REF="$2"; shift 2;;
    --latest)          LATEST_OVERRIDE["${2%%=*}"]="${2#*=}"; shift 2;;
    --stagger)         STAGGER="$2"; shift 2;;
    --wait-timeout)    WAIT_TIMEOUT="$2"; shift 2;;
    --versions-from)   VERSIONS_FROM="$2"; shift 2;;
    --min-version)     MIN_VERSION="$2"; shift 2;;
    --max-minors)      MAX_MINORS="$2"; shift 2;;
    --skip-existing)   SKIP_EXISTING=true; shift;;
    --no-skip-existing) SKIP_EXISTING=false; shift;;
    --dry-run)         DRY_RUN=true; shift;;
    --dispatch-only)   RECONCILE=false; shift;;
    --reconcile-only)  DISPATCH=false; shift;;
    --yes)             YES=true; shift;;
    *) echo "backfill: unknown arg: $1" >&2; exit 2;;
  esac
done

[[ "$ENV" == "testing" || "$ENV" == "production" ]] || { echo "backfill: --env testing|production required" >&2; exit 2; }
[[ -n "$TOOLS" ]] || TOOLS="$ALL_TOOLS"
[[ -n "$REF" ]] || REF="$(git rev-parse --abbrev-ref HEAD)"

case "$ENV" in
  testing)    STORAGE_STACK="pulumi/pulumi-docs-versioned/testing";    WWW_STACK="pulumi/www.pulumi.com/www-testing";    SITE="https://www.pulumi-test.io";;
  production) STORAGE_STACK="pulumi/pulumi-docs-versioned/production"; WWW_STACK="pulumi/www.pulumi.com/www-production"; SITE="https://www.pulumi.com";;
esac

log()  { printf '\033[1;34m[backfill]\033[0m %s\n' "$*"; }
warn() { printf '\033[1;33m[backfill] WARN\033[0m %s\n' "$*" >&2; }
die()  { printf '\033[1;31m[backfill] ERROR\033[0m %s\n' "$*" >&2; exit 1; }

# One version per major.minor (highest patch) from a repo's release tags, NEWEST first.
# Skips pre-releases and prefixed tags (only plain vX.Y.Z). Floors at $MIN_VERSION and caps to
# the newest $MAX_MINORS if set. This is the "currently-supported, down to the minor" list;
# how far back it reaches is the operator's floor call (older tags that the current doc-gen
# toolchain can't build just fail the run and get skipped — see the wait phase).
list_minor_versions() { # $1=owner/repo
  git ls-remote --tags "https://github.com/$1" 2>/dev/null \
    | grep -oE 'refs/tags/v[0-9]+\.[0-9]+\.[0-9]+$' | sed 's#refs/tags/##' \
    | MIN="$MIN_VERSION" CAP="$MAX_MINORS" python3 -c '
import os,sys
def tup(s): return tuple(int(x) for x in s.lstrip("v").split("."))
mn = tup(os.environ["MIN"]) if os.environ.get("MIN") else None
cap = int(os.environ["CAP"]) if os.environ.get("CAP") else None
top={}
for line in sys.stdin:
    v=line.strip()
    try: p=tup(v)
    except ValueError: continue
    key=(p[0],p[1])
    if key not in top or p[2]>top[key][2]: top[key]=p
rows=[top[k] for k in sorted(top, reverse=True)]
if mn: rows=[p for p in rows if p>=mn]
if cap: rows=rows[:cap]
print(" ".join("v%d.%d.%d"%p for p in rows))'
}

# 1. Resolve the target bucket + distribution from the IaC that owns them (never hardcoded).
log "Resolving target from stack outputs ($ENV)…"
BUCKET="$(pulumi stack output bucketNameOutput --stack "$STORAGE_STACK" 2>/dev/null || true)"
DIST="$(pulumi stack output cloudFrontDistributionId --stack "$WWW_STACK" 2>/dev/null || true)"
[[ -n "$BUCKET" ]] || die "storage stack '$STORAGE_STACK' has no bucketNameOutput — versioned docs are not stood up for '$ENV'. Run 'pulumi up infrastructure/versioned-docs/$ENV' first."
[[ -n "$DIST" ]] || warn "could not read cloudFrontDistributionId from '$WWW_STACK'; reconcile will skip its invalidation (bounded by the 300s manifest TTL)."
log "  bucket=$BUCKET  distribution=${DIST:-<none>}  site=$SITE  ref=$REF"

if [[ "$ENV" == "production" && "$DRY_RUN" == "false" && "$YES" != "true" ]]; then
  die "refusing to act on PRODUCTION without --yes (this dispatches real publishes and rewrites the prod manifest). Re-run with --dry-run to preview, or --yes to proceed."
fi

# 2. Read the spec (label, liveRoot, latest, archived versions) per tool from the source manifest.
declare -A LABEL LIVEROOT LATEST ARCHIVES
for tool in $TOOLS; do
  [[ -n "${WORKFLOW[$tool]:-}" ]] || die "unknown tool '$tool' (no workflow mapping)"
  mj="$(curl -fsS "$SOURCE_BASE/docs/versioned/$tool/versions.json" 2>/dev/null || true)"
  [[ -n "$mj" ]] || die "could not read source manifest for '$tool' at $SOURCE_BASE/docs/versioned/$tool/versions.json"
  # Extract label, liveRoot, latest (live) version - tab-delimited so multi-word labels survive.
  IFS=$'\t' read -r _lbl _lr _lat < <(printf '%s' "$mj" | python3 -c 'import json,sys
m=json.load(sys.stdin)
lat=next((v["version"] for v in m["versions"] if v.get("latest")), "")
print("\t".join([m["label"], m["liveRoot"], lat]))')
  LABEL[$tool]="$_lbl"; LIVEROOT[$tool]="$_lr"; LATEST[$tool]="$_lat"
  [[ -n "${LATEST_OVERRIDE[$tool]:-}" ]] && LATEST[$tool]="${LATEST_OVERRIDE[$tool]}"

  if [[ "$VERSIONS_FROM" == "tags" ]]; then
    # Deep: every major.minor from the source repo's real release history that is strictly OLDER
    # than the live 'latest' (so we never archive the live minor or anything newer than it).
    deep="$(list_minor_versions "${REPO[$tool]}")"
    [[ -n "$deep" ]] || die "no tags enumerated for '$tool' from ${REPO[$tool]} (check network / repo name / --min-version)"
    ARCHIVES[$tool]="$(LATEST="${LATEST[$tool]}" python3 -c '
import os,sys
def mm(s): p=s.lstrip("v").split("."); return (int(p[0]),int(p[1]))
lat=mm(os.environ["LATEST"])
print(" ".join(v for v in sys.argv[1:] if mm(v) < lat))' $deep)"
  elif [[ "$VERSIONS_FROM" == "manifest" ]]; then
    # Shallow: mirror whatever the source manifest already lists (e.g. clone the testing catalog).
    ARCHIVES[$tool]="$(printf '%s' "$mj" | python3 -c 'import json,sys; m=json.load(sys.stdin); print(" ".join(v["version"] for v in m["versions"] if not v.get("latest")))')"
  else
    die "--versions-from must be 'tags' or 'manifest' (got '$VERSIONS_FROM')"
  fi
done

# 3. Print the plan.
log "Backfill plan for env=$ENV (source spec: $SOURCE_BASE):"
total=0
for tool in $TOOLS; do
  cnt=$(wc -w <<<"${ARCHIVES[$tool]}")
  total=$((total+cnt))
  printf '  %-16s latest=%-10s archives(%d): %s\n' "$tool" "${LATEST[$tool]}" "$cnt" "${ARCHIVES[$tool]}"
done
log "  $total archive versions across $(wc -w <<<"$TOOLS") tools; workflows dispatched from ref '$REF'."
warn "Confirm each 'latest' above matches the live docs version in $ENV — it becomes the manifest's latest→liveRoot entry. Override with --latest TOOL=vX.Y.Z."

if [[ "$DRY_RUN" == "true" ]]; then
  log "DRY RUN — no dispatch, no reconcile. Re-run without --dry-run to execute."
  exit 0
fi

archive_exists() { aws s3api head-object --bucket "$BUCKET" --key "docs/versioned/$1/$2/index.html" >/dev/null 2>&1; }

# 4. Dispatch phase.
declare -A EXPECT   # "tool/version" -> 1 for everything we expect to land
if [[ "$DISPATCH" == "true" ]]; then
  DISPATCH_START_ISO="$(date -u +%Y-%m-%dT%H:%M:%SZ)"   # marks our runs for the drain-wait below
  log "Dispatching workflows (stagger ${STAGGER}s, skip-existing=$SKIP_EXISTING)…"
  for tool in $TOOLS; do
    for v in ${ARCHIVES[$tool]}; do
      EXPECT["$tool/$v"]=1
      if [[ "$SKIP_EXISTING" == "true" ]] && archive_exists "$tool" "$v"; then
        log "  skip $tool $v (already in bucket)"; continue
      fi
      log "  dispatch ${WORKFLOW[$tool]}  version=${v#v}  target_env=$ENV  publish_only=true"
      gh workflow run "${WORKFLOW[$tool]}" --ref "$REF" \
        -f version="${v#v}" -f target_env="$ENV" -f publish_only=true \
        || warn "dispatch failed for $tool $v (continuing)"
      sleep "$STAGGER"
    done
  done

  # 5. Wait phase — poll the BUCKET, not `gh run` (its status is unreliable). Best-effort:
  # some old toolchains fail to build and never land; we wait up to the timeout, then proceed
  # and let rebuild-manifest reflect whatever actually published.
  log "Waiting for archives to land (timeout ${WAIT_TIMEOUT}s; polling the bucket)…"
  deadline=$(( $(date +%s) + WAIT_TIMEOUT ))
  while :; do
    missing=0; miss_list=""
    for key in "${!EXPECT[@]}"; do
      archive_exists "${key%/*}" "${key#*/}" || { missing=$((missing+1)); miss_list+=" $key"; }
    done
    [[ "$missing" -eq 0 ]] && { log "  all ${#EXPECT[@]} archives present."; break; }
    [[ "$(date +%s)" -ge "$deadline" ]] && { warn "timeout with $missing not yet landed (may be build failures — skipped, not fixed):$miss_list"; break; }
    log "  $missing/${#EXPECT[@]} still pending; re-checking in 30s…"
    sleep 30
  done

  # 5b. Wait for the dispatched workflow RUNS to reach a terminal state before reconciling.
  # publish-version.sh writes versions.json as its LAST step, but the archive index.html polled
  # above is synced BEFORE that write — so reconciling the moment archives appear can be clobbered
  # by a trailing manifest write (observed once: the latest->liveRoot pointer got dropped). Waiting
  # for the runs to finish makes rebuild-manifest the guaranteed last writer. No live-site impact:
  # this only defers the single final manifest reconcile.
  log "Waiting for dispatched workflow runs to finish before reconcile…"
  declare -A WF_SEEN=(); for tool in $TOOLS; do WF_SEEN["${WORKFLOW[$tool]}"]=1; done
  drain_deadline=$(( $(date +%s) + WAIT_TIMEOUT ))
  while :; do
    active=0
    for wf in "${!WF_SEEN[@]}"; do
      n=$(gh run list --workflow "$wf" --limit 300 --json status,createdAt \
            --jq "[.[] | select(.createdAt >= \"$DISPATCH_START_ISO\" and .status != \"completed\")] | length" \
            2>/dev/null || echo 0)
      active=$((active + n))
    done
    [[ "$active" -eq 0 ]] && { log "  all dispatched runs terminal."; break; }
    [[ "$(date +%s)" -ge "$drain_deadline" ]] && { warn "timeout with $active run(s) still active; reconciling anyway (re-run --reconcile-only once they finish if the manifest looks short)."; break; }
    log "  $active dispatched run(s) still active; re-checking in 30s…"
    sleep 30
  done
fi

# 6. Reconcile phase — one race-proof manifest rebuild per tool from the bucket listing.
if [[ "$RECONCILE" == "true" ]]; then
  log "Reconciling manifests (rebuild-manifest.sh per tool)…"
  for tool in $TOOLS; do
    log "  rebuild $tool (latest=${LATEST[$tool]})"
    "$SCRIPT_DIR/rebuild-manifest.sh" --tool "$tool" --bucket "$BUCKET" \
      --live-root "${LIVEROOT[$tool]}" --label "${LABEL[$tool]}" \
      --latest-version "${LATEST[$tool]}" ${DIST:+--distribution-id "$DIST"}
  done

  # 7. Verify phase — manifest reachable with the expected version count + a sample archive 200s.
  log "Verifying via $SITE…"
  for tool in $TOOLS; do
    n=$(curl -fsS "$SITE/docs/versioned/$tool/versions.json" 2>/dev/null | grep -oc '"version"' || echo 0)
    sample="$(printf '%s' "${ARCHIVES[$tool]}" | awk '{print $1}')"
    code="n/a"
    [[ -n "$sample" ]] && code="$(curl -fsS -o /dev/null -w '%{http_code}' "$SITE/docs/versioned/$tool/$sample/" 2>/dev/null || echo ERR)"
    printf '  %-16s manifest versions=%-3s  sample %s -> %s\n' "$tool" "$n" "${sample:-none}" "$code"
  done
fi

log "Done ($ENV)."
