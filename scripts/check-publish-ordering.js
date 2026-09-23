#!/usr/bin/env node
// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.

// Refuses to let an older deploy publish over a newer one.
//
// WHAT THE PUBLISH ACTUALLY IS
//
// scripts/sync-and-test-bucket.sh builds a fresh, per-run S3 origin bucket and writes
// ./origin-bucket-metadata.json naming it. infrastructure/index.ts reads that file at
// program load and feeds `.bucket` into the CloudFront distribution's origin. So
// `pulumi up` on www-production IS the publish step: it swings the live origin to
// whichever bucket the local metadata file happens to name. The program reads ONLY
// `.bucket` -- the `timestamp` and `commit` the sync script also writes are ignored --
// and nothing anywhere compares the incoming build against what is already live.
//
// Deploys are serialized by scripts/await-in-progress.js, but only probabilistically:
// it waits on runs with a LOWER run id and gives up after 45 minutes. An older run that
// outlives that cap -- or that was invisible to the turnstile, or that retries a `[409]
// Conflict` and succeeds late -- reaches `pulumi up` after a newer run has already
// published, and the live origin flips backwards. The site then serves older content
// until the next push or one of the three daily scheduled rebuilds, with every run
// reporting green. .github/workflows/post-deployment-health-check.yml runs only on
// success and checks liveness, never which commit is live, so nothing detects it.
//
// This script closes that hole at the only moment it can be closed: immediately before
// `pulumi up`, after the race has resolved.
//
// WHAT IT COMPARES, AND WHY THAT AND NOT SOMETHING ELSE
//
// The ordering key is the GitHub Actions run id, carried in the metadata file
// (scripts/common.sh's publish_run_id). Run ids are assigned by GitHub, strictly
// increasing per repository, and immune to runner clock skew. They are also precisely
// the ordering await-in-progress.js already promises ("a run only ever waits for runs
// with a LOWER id"), so this enforces at publish time the invariant the turnstile tries
// to arrange at queue time. Enforcing the same invariant twice, at two different points,
// is the whole idea: the turnstile can fail open, this cannot.
//
// Wall-clock `timestamp` is deliberately NOT the gate. It is written when the sync
// finishes, not when the publish happens, so a slow early run can carry a LATER
// timestamp than a fast later one and sail through a naive "reject older timestamp"
// check -- while two runners a few seconds out of sync can fail one that should pass.
// It is used only as a warn-only secondary signal when run ids are unavailable.
//
// Commit ancestry (`git merge-base --is-ancestor`) is the most semantically correct
// answer and is also rejected as the gate: testing-build-and-deploy.yml checks out at
// the default depth of 1, so the history isn't there; staging deploys dispatch that
// workflow at arbitrary PR branch refs, where "is an ancestor of master" is false for
// entirely healthy deploys; and force-pushes break it. See the PR that introduced this
// file for the full weighing.
//
// SOURCE OF TRUTH FOR "WHAT IS LIVE"
//
// Two reads, each answering the half it is actually authoritative for:
//
//   1. WHICH bucket is live: the stack's own `originS3BucketName` output. This is
//      written by the same `pulumi up` that swings the origin, so it cannot disagree
//      with the distribution short of someone editing state by hand.
//   2. WHAT is in it: metadata.json read directly from that bucket over S3. The sync
//      script uploads a copy of the same metadata into every bucket it builds, so the
//      bucket describes itself. Reading the bucket rather than trusting a second record
//      means the answer stays correct even after a manual pin, and it is uncached.
//
// https://www.pulumi.com/metadata.json serves the same document and is NOT used, though
// not for the obvious reason: that path has its own zero-TTL cache behavior in
// infrastructure/index.ts, so it isn't edge-cached. The problem is one layer down.
// Swinging the origin is a CloudFront DISTRIBUTION CONFIG change, and those take 15-20
// minutes to propagate globally (see BUILD-AND-DEPLOY.md). For that whole window the
// public endpoint can still answer from the previous origin -- and that window is
// exactly the one this check runs in, since the race it detects is two deploys minutes
// apart. Of the three candidate sources of truth, the public URL is the only one that
// is systematically stale precisely when it is being asked.
//
// WHAT THIS DOES NOT CATCH
//
// A newer run whose `pulumi up` is still IN FLIGHT hasn't written its outputs yet, so
// this reads the pre-race state and allows. That case is already handled, loudly, by the
// Pulumi stack lock: the second update dies on `[409] Conflict: Another update is
// currently in progress`. This check covers the case the lock cannot -- a newer run that
// has already finished.
//
// SCOPE
//
// Only stacks with a shared, ordered publish stream are checked, and they are checked
// differently (see MODES_BY_STACK). PR previews never run `pulumi up` at all
// (ci-pull-request.sh runs `pulumi preview`), and dev stacks have a single owner and no
// ordering to violate, so both skip entirely.
//
// FAILING OPEN, AND WHY THAT IS SAFE HERE
//
// Every unknown resolves to "allow, and say so": no prior deploy, a live bucket that has
// been cleaned up, metadata that is missing or unparseable, a metadata file with no run
// id (which is what every bucket built before this landed looks like). A guard on the
// deploy path must not be able to deadlock a first deploy or a recovery.
//
// The one thing that is NOT allowed to fail open is not knowing which stack we are
// about to publish to: that would silently disable the check, and a guard that never
// fires is worse than no guard because it manufactures confidence. That exits 2.

const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const repoRoot = path.join(__dirname, "..");

// The default location of the metadata file sync-and-test-bucket.sh writes. Mirrors
// origin_bucket_metadata_filepath() in scripts/common.sh. The real path comes from the
// stack's own `pathToOriginBucketMetadata` config wherever that can be read, so that
// this inspects exactly the file infrastructure/index.ts is about to consume; this is
// only the fallback for when it can't be.
const defaultMetadataFile = path.join(repoRoot, "origin-bucket-metadata.json");

// How each stack is treated. A stack that isn't listed here is skipped.
//
//   enforce  Abort the deploy. www-production is the live docs site: a silent
//            flip backwards is served to everyone, and it persists until the next
//            push or scheduled rebuild -- up to ~15 hours across the overnight gap
//            between the 4:23pm and 7:17am slots in build-and-deploy.yml.
//
//            Aborting is cheap here in a way that is worth stating plainly, because
//            "abort" usually means "somebody has to fix something at 2am" and this
//            one doesn't: when this check fires, the content that SHOULD be live
//            already is -- a newer run published it. The losing run has nothing to
//            contribute. Whoever reads the red build reads the message, confirms
//            the newer run is the live one, and closes the tab. That is why the
//            message below names the winning run and says so in as many words.
//
//   warn     Log and continue. www-testing is a scratch environment whose deploys
//            deliberately are not ordered: staging-deploy.yml dispatches
//            testing-build-and-deploy.yml at PR branch refs, and "next merge to
//            master resets pulumi-test.io" is documented behavior, not a bug. The
//            blast radius is one reviewer's preview. Failing those deploys would
//            make /deploy-staging flaky for a reason the PR author cannot act on,
//            so testing gets the signal without the gate.
const MODES_BY_STACK = {
    "www-production": "enforce",
    "www-testing": "warn",
};

const VALID_MODES = ["enforce", "warn", "skip"];

// Exit codes. 1 is reserved for "this publish would go backwards" so a caller can tell
// a real regression from a broken check.
const EXIT_OK = 0;
const EXIT_REGRESSION = 1;
const EXIT_BROKEN = 2;

// Environment variables that turn the check off, both documented in the failure message.
const OVERRIDE_VAR = "ALLOW_OUT_OF_ORDER_PUBLISH";
const MODE_VAR = "PUBLISH_ORDERING_MODE";

// GitHub renders an unchecked `type: boolean` workflow_dispatch input as the STRING
// "false", so presence is not enough -- it has to be parsed. Everything not recognizably
// affirmative is off.
function isTruthy(value) {
    return /^(1|true|yes|on)$/i.test(String(value == null ? "" : value).trim());
}

// Coerces a run id from JSON (which may hold a number or a string, depending on who
// wrote the file) to a non-negative integer, or null if it isn't one. A run id that
// can't be parsed is treated as absent rather than as zero: "unknown" must never sort
// below a real run and reject a healthy deploy.
function toRunId(value) {
    if (typeof value === "number") {
        return Number.isSafeInteger(value) && value >= 0 ? value : null;
    }
    if (typeof value === "string" && /^[0-9]+$/.test(value.trim())) {
        const parsed = Number(value.trim());
        return Number.isSafeInteger(parsed) ? parsed : null;
    }
    return null;
}

function toTimestamp(value) {
    const parsed = typeof value === "string" ? Number(value.trim()) : value;
    return typeof parsed === "number" && Number.isFinite(parsed) ? parsed : null;
}

// Normalizes a parsed metadata document into the fields this check reasons about.
// Anything missing comes back null rather than undefined, so the comparison below has
// exactly one shape to handle.
function normalizeMetadata(doc) {
    if (doc === null || typeof doc !== "object" || Array.isArray(doc)) {
        return null;
    }
    return {
        bucket: typeof doc.bucket === "string" && doc.bucket !== "" ? doc.bucket : null,
        commit: typeof doc.commit === "string" && doc.commit !== "" ? doc.commit : null,
        runId: toRunId(doc.runId),
        runAttempt: toRunId(doc.runAttempt),
        timestamp: toTimestamp(doc.timestamp),
    };
}

function describe(metadata) {
    if (!metadata) {
        return "<unknown>";
    }
    const parts = [metadata.bucket || "<no bucket>"];
    if (metadata.commit) {
        parts.push(`commit ${metadata.commit.slice(0, 8)}`);
    }
    if (metadata.runId !== null) {
        const attempt = metadata.runAttempt !== null && metadata.runAttempt > 1
            ? ` attempt ${metadata.runAttempt}`
            : "";
        parts.push(`run ${metadata.runId}${attempt}`);
    } else {
        parts.push("no run id");
    }
    return parts.join(", ");
}

// The whole decision, as a pure function, so it can be tested without a shell, an AWS
// account, or a Pulumi backend. `live` is null when nothing is published yet or when the
// live state could not be read.
//
// Returns { regression, reason, warnings }.
function decidePublish(incoming, live) {
    const warnings = [];

    if (!live) {
        return {
            regression: false,
            reason: "nothing is published on this stack yet, or the live state could not be read",
            warnings,
        };
    }

    // Re-publishing the bucket that is already the origin is a no-op as far as ordering
    // goes, whatever the run ids say.
    if (incoming.bucket && live.bucket && incoming.bucket === live.bucket) {
        return {
            regression: false,
            reason: `${incoming.bucket} is already the live origin`,
            warnings,
        };
    }

    // Same commit, different bucket: a scheduled rebuild with no intervening push, or a
    // re-run. The content is identical, so this cannot be a regression regardless of
    // which run built it, and checking it before the run ids keeps a whole class of
    // false positives off the table cheaply.
    if (incoming.commit && live.commit && incoming.commit === live.commit) {
        return {
            regression: false,
            reason: `same commit as the live origin (${incoming.commit.slice(0, 8)})`,
            warnings,
        };
    }

    if (incoming.runId === null || live.runId === null) {
        const which = incoming.runId === null ? "this build" : "the live origin";
        warnings.push(
            `${which} carries no run id, so publish order cannot be checked. Every bucket ` +
            `built before scripts/common.sh started recording one looks like this, and the ` +
            `next deploy will have it on both sides.`,
        );

        // Wall clock is not trustworthy enough to fail a build on (see the header), but
        // it is worth saying out loud when it disagrees, because during the rollout
        // window it is the only signal there is.
        if (incoming.timestamp !== null && live.timestamp !== null && incoming.timestamp < live.timestamp) {
            const behindMinutes = Math.round((live.timestamp - incoming.timestamp) / 60000);
            warnings.push(
                `This build was synced ${behindMinutes}m BEFORE the live origin was. That is ` +
                `what an out-of-order publish looks like, but runner clock skew looks the same, ` +
                `so this is a warning and not a failure. Check ${describe(live)} against ` +
                `${describe(incoming)} if the site looks stale afterwards.`,
            );
        }

        return {
            regression: false,
            reason: "run ids are not comparable",
            warnings,
        };
    }

    if (incoming.runId > live.runId) {
        return {
            regression: false,
            reason: `run ${incoming.runId} is newer than the live run ${live.runId}`,
            warnings,
        };
    }

    // Equal run ids mean the same run publishing again -- a re-run of a deploy that
    // already published, or a retried `pulumi up` within one run. Its content is the
    // content that run built, so letting it through cannot move the site backwards.
    if (incoming.runId === live.runId) {
        return {
            regression: false,
            reason: `same run (${incoming.runId}) as the live origin`,
            warnings,
        };
    }

    return {
        regression: true,
        reason:
            `run ${incoming.runId} would publish over run ${live.runId}, which is newer and ` +
            `already live`,
        warnings,
    };
}

// Resolves the mode for a stack. An explicit PUBLISH_ORDERING_MODE wins, so a one-off
// deploy can be run in warn mode without editing this table.
function resolveMode(stackName, env) {
    const override = (env[MODE_VAR] || "").trim();
    if (override !== "") {
        return override;
    }
    // `pulumi stack --show-name` prints the bare stack name today, but PULUMI_STACK_NAME
    // is org-qualified ("pulumi/www-production"). Match on the last segment so a CLI that
    // starts qualifying the name can't quietly turn production into "skip".
    const bare = String(stackName).split("/").pop();
    return MODES_BY_STACK[bare] || "skip";
}

// --- the impure half ------------------------------------------------------------

function realExec(command, args) {
    try {
        const stdout = execFileSync(command, args, {
            encoding: "utf8",
            stdio: ["ignore", "pipe", "pipe"],
        });
        return { status: 0, stdout };
    } catch (error) {
        return { status: typeof error.status === "number" ? error.status : 1, stdout: "" };
    }
}

const realDeps = {
    exec: realExec,
    readFile: (file) => fs.readFileSync(file, "utf8"),
    fileExists: (file) => fs.existsSync(file),
    env: process.env,
    log: (message) => console.log(message),
};

function pulumi(deps, args) {
    const result = deps.exec("pulumi", ["-C", path.join(repoRoot, "infrastructure"), ...args]);
    return result.status === 0 ? result.stdout.trim() : null;
}

// Reads metadata.json straight out of an S3 bucket. Returns null for anything that goes
// wrong -- the bucket having been cleaned up, the object never having been written, a
// transient S3 error -- because none of those are evidence of a regression.
function readLiveMetadata(deps, bucket, region) {
    const args = ["s3", "cp", `s3://${bucket}/metadata.json`, "-"];
    if (region) {
        args.push("--region", region);
    }
    const result = deps.exec("aws", args);
    if (result.status !== 0 || result.stdout.trim() === "") {
        return { metadata: null, error: `could not read s3://${bucket}/metadata.json` };
    }
    try {
        return { metadata: normalizeMetadata(JSON.parse(result.stdout)), error: null };
    } catch (error) {
        return { metadata: null, error: `s3://${bucket}/metadata.json is not parseable JSON` };
    }
}

function main(deps = realDeps) {
    const log = deps.log;
    const say = (message) => log(`publish-ordering: ${message}`);
    const warn = (message) => log(`::warning::publish-ordering: ${message}`);

    // Which stack is about to be published to. This is the one lookup that is not
    // allowed to fail quietly: defaulting an unknown stack to "skip" would turn a
    // broken Pulumi CLI into a silently disabled guard.
    const stackName = pulumi(deps, ["stack", "--show-name"]);
    if (!stackName) {
        log(
            "publish-ordering: could not determine the current stack (`pulumi stack --show-name` " +
            "failed). Refusing to guess: a skipped check reads exactly like a passing one. Fix " +
            `the Pulumi login/stack selection, or set ${MODE_VAR}=skip to bypass this deliberately.`,
        );
        return EXIT_BROKEN;
    }

    const mode = resolveMode(stackName, deps.env);
    if (!VALID_MODES.includes(mode)) {
        log(
            `publish-ordering: unknown ${MODE_VAR} '${mode}' (expected one of ${VALID_MODES.join(", ")}).`,
        );
        return EXIT_BROKEN;
    }

    if (mode === "skip") {
        say(`stack '${stackName}' has no shared publish ordering to protect. Skipping.`);
        return EXIT_OK;
    }

    if (isTruthy(deps.env[OVERRIDE_VAR])) {
        warn(
            `${OVERRIDE_VAR} is set, so the publish-ordering check is disabled for this run. ` +
            `This is the rollback escape hatch; it is doing what it says.`,
        );
        return EXIT_OK;
    }

    // A pinned origin means someone has already taken manual control of what is served,
    // and infrastructure/index.ts ignores the metadata file entirely in that case. There
    // is nothing here to order.
    const override = pulumi(deps, ["config", "get", "originBucketNameOverride"]);
    if (override) {
        warn(
            `originBucketNameOverride is pinned to '${override}', so the metadata file is not ` +
            `what gets published. Skipping the ordering check.`,
        );
        return EXIT_OK;
    }

    // Inspect exactly the file the Pulumi program will read. The config value is
    // relative to infrastructure/, which is where the program runs from.
    const configuredPath = pulumi(deps, ["config", "get", "pathToOriginBucketMetadata"]);
    const metadataFile = configuredPath
        ? path.resolve(repoRoot, "infrastructure", configuredPath)
        : defaultMetadataFile;

    if (!deps.fileExists(metadataFile)) {
        say(
            `no metadata file at ${metadataFile}; there is no incoming bucket to check. ` +
            `Leaving the outcome to the Pulumi program.`,
        );
        return EXIT_OK;
    }

    let incoming;
    try {
        incoming = normalizeMetadata(JSON.parse(deps.readFile(metadataFile)));
    } catch (error) {
        incoming = null;
    }
    if (!incoming || !incoming.bucket) {
        warn(
            `${metadataFile} is missing or unparseable, so there is nothing to compare. ` +
            `Leaving the outcome to the Pulumi program.`,
        );
        return EXIT_OK;
    }

    const liveBucket = pulumi(deps, ["stack", "output", "originS3BucketName"]);
    if (!liveBucket) {
        say(
            `the ${stackName} stack has no originS3BucketName output yet (first deploy, or a ` +
            `stack that has never completed an update). Allowing ${describe(incoming)}.`,
        );
        return EXIT_OK;
    }

    const region = pulumi(deps, ["config", "get", "aws:region"]);
    const { metadata: live, error: liveError } = liveBucket === incoming.bucket
        ? { metadata: { ...incoming }, error: null }
        : readLiveMetadata(deps, liveBucket, region);

    if (!live) {
        warn(
            `${liveError}. The live origin is ${liveBucket}, but its metadata could not be read, ` +
            `so publish order cannot be checked. Allowing ${describe(incoming)}.`,
        );
        return EXIT_OK;
    }

    // The bucket the stack says is live is authoritative over whatever the bucket's own
    // copy of the metadata claims, in the (unreachable-in-practice) case they disagree.
    live.bucket = liveBucket;

    const decision = decidePublish(incoming, live);
    for (const warning of decision.warnings) {
        warn(warning);
    }

    if (!decision.regression) {
        say(`OK -- ${decision.reason}.`);
        say(`  incoming: ${describe(incoming)}`);
        say(`  live:     ${describe(live)}`);
        return EXIT_OK;
    }

    const explanation = [
        "",
        "=================================================================",
        "  This deploy would move the live site BACKWARDS. Stopping.",
        "=================================================================",
        "",
        `  incoming: ${describe(incoming)}`,
        `  live:     ${describe(live)}`,
        "",
        `  ${decision.reason}.`,
        "",
        "  Nothing is broken and nothing needs fixing right now. A newer run",
        "  already published, so the site is serving the content it should be.",
        "  This run raced it, lost, and is being stopped before it can undo the",
        "  result. Confirm the live origin above looks right and you are done.",
        "",
        "  If you MEANT to publish this older build -- a deliberate rollback --",
        "  don't re-run this run: a re-run keeps its old run id and will be",
        "  stopped again. Instead:",
        "",
        `    1. Dispatch a NEW "Build and deploy" run (workflow_dispatch) at the`,
        "       ref you want live. A new run has a newer run id, so it publishes",
        "       normally. Check its \"Publish even if a newer deploy already",
        "       published\" input only if another run may publish while it waits.",
        `    2. Deploying from a laptop: set ${OVERRIDE_VAR}=true.`,
        "",
        "  Note that the ordinary rollback -- `git revert` and push -- does not",
        "  need either one: a revert is a new commit in a new run, so it is",
        "  newer by this check's reckoning and publishes normally.",
        "",
        "  See scripts/check-publish-ordering.js for the full mechanism.",
        "",
    ].join("\n");

    if (mode === "warn") {
        warn(
            `${decision.reason}. Not failing the deploy: ${stackName} is a shared scratch ` +
            `environment whose deploys are deliberately unordered. Incoming ${describe(incoming)}; ` +
            `live ${describe(live)}.`,
        );
        return EXIT_OK;
    }

    log(explanation);
    log(
        `::error::publish-ordering: refusing to publish ${describe(incoming)} over the newer, ` +
        `already-live ${describe(live)}. See the deploy log for how to override.`,
    );
    return EXIT_REGRESSION;
}

if (require.main === module) {
    process.exit(main());
}

module.exports = {
    decidePublish,
    normalizeMetadata,
    resolveMode,
    isTruthy,
    toRunId,
    main,
    MODES_BY_STACK,
    OVERRIDE_VAR,
    MODE_VAR,
    EXIT_OK,
    EXIT_REGRESSION,
    EXIT_BROKEN,
};
