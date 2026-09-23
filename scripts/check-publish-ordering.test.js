// Unit tests for the publish-ordering guard (scripts/check-publish-ordering.js) and for
// the metadata document it reads (render_origin_bucket_metadata and friends in
// scripts/common.sh).
//
// Three layers, deliberately:
//
//   1. decidePublish() -- the comparison itself, as a pure function.
//   2. main() with injected deps -- the wiring: stack scoping, the escape hatches, and
//      every way the live state can be unavailable.
//   3. One end-to-end run of the real script as a subprocess, with fake `pulumi` and
//      `aws` binaries on PATH, asserting it actually exits 1 and says so. A guard that
//      can't be shown to fire is worse than no guard, and layers 1 and 2 both stub out
//      the part that does the firing.
//
// Layer 3 follows scripts/deploy-bucket-naming.test.js: no network, no AWS, no Pulumi
// backend.

const { test } = require("node:test");
const assert = require("node:assert/strict");
const { execFileSync } = require("node:child_process");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");

const guard = require("./check-publish-ordering.js");
const {
    decidePublish,
    normalizeMetadata,
    resolveMode,
    isTruthy,
    toRunId,
    main,
    OVERRIDE_VAR,
    MODE_VAR,
    EXIT_OK,
    EXIT_REGRESSION,
    EXIT_BROKEN,
} = guard;

const COMMON_SH = path.join(__dirname, "common.sh");
const GUARD_JS = path.join(__dirname, "check-publish-ordering.js");

// A metadata document as sync-and-test-bucket.sh writes it.
function metadata(overrides = {}) {
    return normalizeMetadata({
        timestamp: 1_700_000_000_000,
        commit: "aaaaaaaabbbbbbbbccccccccddddddddeeeeeeee",
        runId: 100,
        runAttempt: 1,
        bucket: "www-production-pulumi-docs-origin-push-aaaaaaaa-abc",
        url: "http://example.invalid",
        ...overrides,
    });
}

// ---------------------------------------------------------------------------
// Layer 1: the comparison.
// ---------------------------------------------------------------------------

test("decidePublish allows a newer run over an older live one", () => {
    const decision = decidePublish(
        metadata({ runId: 101, bucket: "bucket-101", commit: "c".repeat(40) }),
        metadata({ runId: 100, bucket: "bucket-100" }),
    );
    assert.equal(decision.regression, false);
    assert.match(decision.reason, /run 101 is newer than the live run 100/);
});

test("decidePublish BLOCKS an older run over a newer live one", () => {
    const decision = decidePublish(
        metadata({ runId: 100, bucket: "bucket-100", commit: "c".repeat(40) }),
        metadata({ runId: 101, bucket: "bucket-101", commit: "d".repeat(40) }),
    );
    assert.equal(decision.regression, true);
    assert.match(decision.reason, /run 100 would publish over run 101/);
});

test("decidePublish allows the bucket that is already live", () => {
    const decision = decidePublish(
        metadata({ runId: 100, bucket: "same-bucket" }),
        metadata({ runId: 101, bucket: "same-bucket" }),
    );
    assert.equal(decision.regression, false);
    assert.match(decision.reason, /already the live origin/);
});

test("decidePublish allows a lower run id at the same commit", () => {
    // A scheduled rebuild with no intervening push, or a re-run: different bucket
    // (the name carries a per-run uniquifier), identical content.
    const decision = decidePublish(
        metadata({ runId: 100, bucket: "bucket-100", commit: "e".repeat(40) }),
        metadata({ runId: 101, bucket: "bucket-101", commit: "e".repeat(40) }),
    );
    assert.equal(decision.regression, false);
    assert.match(decision.reason, /same commit/);
});

test("decidePublish allows the same run publishing again", () => {
    const decision = decidePublish(
        metadata({ runId: 100, runAttempt: 2, bucket: "bucket-100-2", commit: "f".repeat(40) }),
        metadata({ runId: 100, runAttempt: 1, bucket: "bucket-100-1", commit: "0".repeat(40) }),
    );
    assert.equal(decision.regression, false);
    assert.match(decision.reason, /same run \(100\)/);
});

test("decidePublish allows when nothing is live", () => {
    const decision = decidePublish(metadata(), null);
    assert.equal(decision.regression, false);
    assert.match(decision.reason, /nothing is published/);
});

test("decidePublish never blocks on a missing run id, but warns", () => {
    const decision = decidePublish(
        metadata({ runId: null, bucket: "bucket-a", commit: "1".repeat(40) }),
        metadata({ runId: 101, bucket: "bucket-b", commit: "2".repeat(40) }),
    );
    assert.equal(decision.regression, false);
    assert.equal(decision.warnings.length, 1);
    assert.match(decision.warnings[0], /carries no run id/);
});

test("decidePublish warns about an older timestamp when run ids are unavailable", () => {
    // Wall clock is a hint, never a gate: runner clock skew is indistinguishable from a
    // genuine out-of-order publish, so this must not fail the build.
    const decision = decidePublish(
        metadata({ runId: null, timestamp: 1_700_000_000_000, bucket: "a", commit: "1".repeat(40) }),
        metadata({ runId: null, timestamp: 1_700_000_600_000, bucket: "b", commit: "2".repeat(40) }),
    );
    assert.equal(decision.regression, false);
    assert.equal(decision.warnings.length, 2);
    assert.match(decision.warnings[1], /synced 10m BEFORE the live origin/);
});

test("toRunId treats unusable values as absent rather than as zero", () => {
    assert.equal(toRunId(42), 42);
    assert.equal(toRunId("42"), 42);
    assert.equal(toRunId(null), null);
    assert.equal(toRunId(undefined), null);
    assert.equal(toRunId("not-a-number"), null);
    assert.equal(toRunId(-1), null);
    assert.equal(toRunId(1.5), null);
});

test("normalizeMetadata rejects documents that aren't objects", () => {
    assert.equal(normalizeMetadata(null), null);
    assert.equal(normalizeMetadata("string"), null);
    assert.equal(normalizeMetadata([1, 2]), null);
});

test("isTruthy treats GitHub's unchecked-boolean string as off", () => {
    assert.equal(isTruthy("false"), false);
    assert.equal(isTruthy(""), false);
    assert.equal(isTruthy(undefined), false);
    assert.equal(isTruthy("true"), true);
    assert.equal(isTruthy("TRUE"), true);
    assert.equal(isTruthy("1"), true);
    assert.equal(isTruthy("yes"), true);
});

test("resolveMode scopes enforcement to the stacks with a shared publish stream", () => {
    assert.equal(resolveMode("www-production", {}), "enforce");
    assert.equal(resolveMode("www-testing", {}), "warn");
    assert.equal(resolveMode("staging", {}), "skip");
    assert.equal(resolveMode("christian", {}), "skip");
    // Guards against the stack-name mismatch already latent in
    // sync-and-test-bucket.sh, which compares against "production" while the stack
    // is actually named "www-production".
    assert.equal(resolveMode("production", {}), "skip");
    assert.equal(resolveMode("www-production", { [MODE_VAR]: "warn" }), "warn");
});

test("resolveMode matches an org-qualified stack name on its last segment", () => {
    assert.equal(resolveMode("pulumi/www-production", {}), "enforce");
    assert.equal(resolveMode("pulumi/www-testing", {}), "warn");
    assert.equal(resolveMode("pulumi/staging", {}), "skip");
});

// ---------------------------------------------------------------------------
// Layer 2: the wiring, with injected deps.
// ---------------------------------------------------------------------------

// Builds a deps object whose `exec` answers `pulumi` and `aws` from a small table.
// Anything not in the table comes back as a failed command, which is what the guard
// sees when a bucket has been cleaned up or an output doesn't exist.
function fakeDeps({
    stack = "www-production",
    outputs = {},
    config = {},
    localMetadata = null,
    liveObjects = {},
    env = {},
} = {}) {
    const logs = [];
    const fail = { status: 1, stdout: "" };
    const ok = (stdout) => ({ status: 0, stdout: `${stdout}\n` });

    return {
        logs,
        deps: {
            env,
            log: (message) => logs.push(message),
            fileExists: () => localMetadata !== null,
            readFile: () => JSON.stringify(localMetadata),
            exec(command, args) {
                if (command === "pulumi") {
                    const rest = args.slice(2); // drop -C <dir>
                    if (rest[0] === "stack" && rest[1] === "--show-name") {
                        return stack === null ? fail : ok(stack);
                    }
                    if (rest[0] === "stack" && rest[1] === "output") {
                        const value = outputs[rest[2]];
                        return value === undefined ? fail : ok(value);
                    }
                    if (rest[0] === "config" && rest[1] === "get") {
                        const value = config[rest[2]];
                        return value === undefined ? fail : ok(value);
                    }
                    return fail;
                }
                if (command === "aws") {
                    const uri = args[2];
                    const body = liveObjects[uri];
                    return body === undefined ? fail : ok(body);
                }
                return fail;
            },
        },
    };
}

// The standard "an older run is about to clobber a newer one" world.
function regressionWorld(extra = {}) {
    const incoming = {
        timestamp: 1_700_000_000_000,
        commit: "a".repeat(40),
        runId: 100,
        runAttempt: 1,
        bucket: "bucket-100",
        url: "http://old.invalid",
    };
    const live = {
        timestamp: 1_700_000_600_000,
        commit: "b".repeat(40),
        runId: 101,
        runAttempt: 1,
        bucket: "bucket-101",
        url: "http://new.invalid",
    };
    return fakeDeps({
        stack: "www-production",
        config: { "aws:region": "us-west-2", pathToOriginBucketMetadata: "../origin-bucket-metadata.json" },
        outputs: { originS3BucketName: live.bucket },
        localMetadata: incoming,
        liveObjects: { "s3://bucket-101/metadata.json": JSON.stringify(live) },
        ...extra,
    });
}

test("main blocks an out-of-order publish on www-production", () => {
    const { deps, logs } = regressionWorld();
    assert.equal(main(deps), EXIT_REGRESSION);
    const output = logs.join("\n");
    assert.match(output, /would move the live site BACKWARDS/);
    assert.match(output, /run 100 would publish over run 101/);
    // The message has to carry the way out, or it isn't usable at 2am.
    assert.match(output, new RegExp(OVERRIDE_VAR));
    assert.match(output, /::error::/);
});

test("main only warns on www-testing", () => {
    const { deps, logs } = regressionWorld({ stack: "www-testing" });
    assert.equal(main(deps), EXIT_OK);
    const output = logs.join("\n");
    assert.match(output, /::warning::/);
    assert.match(output, /Not failing the deploy/);
    assert.doesNotMatch(output, /::error::/);
});

test("main skips dev stacks without touching AWS", () => {
    let awsCalls = 0;
    const { deps, logs } = regressionWorld({ stack: "christian" });
    const inner = deps.exec;
    deps.exec = (command, args) => {
        if (command === "aws") {
            awsCalls += 1;
        }
        return inner(command, args);
    };
    assert.equal(main(deps), EXIT_OK);
    assert.equal(awsCalls, 0);
    assert.match(logs.join("\n"), /no shared publish ordering to protect/);
});

test("main allows an out-of-order publish when the override is set", () => {
    const { deps, logs } = regressionWorld({ env: { [OVERRIDE_VAR]: "true" } });
    assert.equal(main(deps), EXIT_OK);
    assert.match(logs.join("\n"), /rollback escape hatch/);
});

test("main is not fooled by GitHub's unchecked-boolean input", () => {
    const { deps } = regressionWorld({ env: { [OVERRIDE_VAR]: "false" } });
    assert.equal(main(deps), EXIT_REGRESSION);
});

test("main skips when the origin bucket is manually pinned", () => {
    const { deps, logs } = regressionWorld({
        config: {
            "aws:region": "us-west-2",
            pathToOriginBucketMetadata: "../origin-bucket-metadata.json",
            originBucketNameOverride: "some-pinned-bucket",
        },
    });
    assert.equal(main(deps), EXIT_OK);
    assert.match(logs.join("\n"), /originBucketNameOverride is pinned/);
});

test("main allows the first deploy of a stack with no prior output", () => {
    const { deps, logs } = regressionWorld({ outputs: {} });
    assert.equal(main(deps), EXIT_OK);
    assert.match(logs.join("\n"), /no originS3BucketName output yet/);
});

test("main allows when the live bucket's metadata can't be read", () => {
    const { deps, logs } = regressionWorld({ liveObjects: {} });
    assert.equal(main(deps), EXIT_OK);
    assert.match(logs.join("\n"), /could not read s3:\/\/bucket-101\/metadata\.json/);
});

test("main allows when the live bucket's metadata is not JSON", () => {
    const { deps, logs } = regressionWorld({
        liveObjects: { "s3://bucket-101/metadata.json": "<?xml version=\"1.0\"?><Error/>" },
    });
    assert.equal(main(deps), EXIT_OK);
    assert.match(logs.join("\n"), /not parseable JSON/);
});

test("main allows when there is no local metadata file", () => {
    const { deps, logs } = regressionWorld({ localMetadata: null });
    assert.equal(main(deps), EXIT_OK);
    assert.match(logs.join("\n"), /no metadata file at/);
});

test("main allows, and warns, when the live bucket predates run-id recording", () => {
    // What every production deploy sees on the first run after this lands.
    const { deps, logs } = regressionWorld({
        liveObjects: {
            "s3://bucket-101/metadata.json": JSON.stringify({
                timestamp: 1_700_000_600_000,
                commit: "b".repeat(40),
                bucket: "bucket-101",
                url: "http://new.invalid",
            }),
        },
    });
    assert.equal(main(deps), EXIT_OK);
    const output = logs.join("\n");
    assert.match(output, /carries no run id/);
    assert.match(output, /synced 10m BEFORE the live origin/);
});

test("main allows a healthy in-order publish and says so out loud", () => {
    // The happy path must leave evidence in the log. A check whose only visible
    // output is silence is indistinguishable from one that isn't running.
    const { deps, logs } = regressionWorld();
    deps.readFile = () => JSON.stringify({
        timestamp: 1_700_001_200_000,
        commit: "c".repeat(40),
        runId: 102,
        runAttempt: 1,
        bucket: "bucket-102",
        url: "http://newer.invalid",
    });
    assert.equal(main(deps), EXIT_OK);
    const output = logs.join("\n");
    assert.match(output, /OK -- run 102 is newer than the live run 101/);
    assert.match(output, /incoming: bucket-102, commit cccccccc, run 102/);
    assert.match(output, /live: {5}bucket-101, commit bbbbbbbb, run 101/);
});

test("main refuses to guess when it cannot resolve the stack", () => {
    // Failing open here would silently disable the check on every deploy.
    const { deps, logs } = regressionWorld({ stack: null });
    assert.equal(main(deps), EXIT_BROKEN);
    assert.match(logs.join("\n"), /a skipped check reads exactly like a passing one/);
});

test("main rejects an unknown PUBLISH_ORDERING_MODE rather than ignoring it", () => {
    const { deps, logs } = regressionWorld({ env: { [MODE_VAR]: "maybe" } });
    assert.equal(main(deps), EXIT_BROKEN);
    assert.match(logs.join("\n"), /unknown PUBLISH_ORDERING_MODE 'maybe'/);
});

// ---------------------------------------------------------------------------
// Layer 3: the real script, end to end, actually exiting nonzero.
// ---------------------------------------------------------------------------

// Writes fake `pulumi` and `aws` executables that answer from a fixture directory, and
// runs the guard as a real subprocess against them.
function runGuardE2E({ stack, liveBucket, liveMetadata, incomingMetadata, env = {} }) {
    const dir = fs.mkdtempSync(path.join(os.tmpdir(), "publish-ordering-"));
    const binDir = path.join(dir, "bin");
    fs.mkdirSync(binDir);

    const metadataPath = path.join(dir, "origin-bucket-metadata.json");
    fs.writeFileSync(metadataPath, JSON.stringify(incomingMetadata));

    const livePath = path.join(dir, "live-metadata.json");
    if (liveMetadata !== null) {
        fs.writeFileSync(livePath, JSON.stringify(liveMetadata));
    }

    fs.writeFileSync(
        path.join(binDir, "pulumi"),
        [
            "#!/bin/bash",
            'args="$*"',
            'case "$args" in',
            `  *"stack --show-name"*) echo "${stack}" ;;`,
            `  *"stack output originS3BucketName"*) echo "${liveBucket}" ;;`,
            `  *"config get pathToOriginBucketMetadata"*) echo "${metadataPath}" ;;`,
            '  *"config get aws:region"*) echo "us-west-2" ;;',
            "  *) exit 1 ;;",
            "esac",
            "",
        ].join("\n"),
        { mode: 0o755 },
    );

    fs.writeFileSync(
        path.join(binDir, "aws"),
        [
            "#!/bin/bash",
            `if [ -f "${livePath}" ]; then cat "${livePath}"; else exit 1; fi`,
            "",
        ].join("\n"),
        { mode: 0o755 },
    );

    let status = 0;
    let stdout = "";
    try {
        stdout = execFileSync("node", [GUARD_JS], {
            encoding: "utf8",
            env: { PATH: `${binDir}:${process.env.PATH}`, HOME: process.env.HOME || "", ...env },
            stdio: ["ignore", "pipe", "pipe"],
        });
    } catch (error) {
        status = error.status;
        stdout = error.stdout || "";
    }

    fs.rmSync(dir, { recursive: true, force: true });
    return { status, stdout };
}

const OLD_BUILD = {
    timestamp: 1_700_000_000_000,
    commit: "a".repeat(40),
    runId: 35266933458,
    runAttempt: 1,
    bucket: "www-production-pulumi-docs-origin-push-aaaaaaaa-fqwwnrm2",
    url: "http://old.invalid",
};

const NEW_BUILD = {
    timestamp: 1_700_000_600_000,
    commit: "b".repeat(40),
    runId: 35266996109,
    runAttempt: 1,
    bucket: "www-production-pulumi-docs-origin-push-bbbbbbbb-fqwwnrm9",
    url: "http://new.invalid",
};

test("end to end: the real script exits 1 when an older run would clobber a newer one", () => {
    const { status, stdout } = runGuardE2E({
        stack: "www-production",
        liveBucket: NEW_BUILD.bucket,
        liveMetadata: NEW_BUILD,
        incomingMetadata: OLD_BUILD,
    });
    assert.equal(status, 1);
    assert.match(stdout, /would move the live site BACKWARDS/);
    assert.match(stdout, /run 35266933458 would publish over run 35266996109/);
});

test("end to end: the real script exits 0 when the newer run publishes", () => {
    const { status, stdout } = runGuardE2E({
        stack: "www-production",
        liveBucket: OLD_BUILD.bucket,
        liveMetadata: OLD_BUILD,
        incomingMetadata: NEW_BUILD,
    });
    assert.equal(status, 0);
    assert.match(stdout, /OK -- run 35266996109 is newer than the live run 35266933458/);
});

test("end to end: the escape hatch lets the older build through", () => {
    const { status, stdout } = runGuardE2E({
        stack: "www-production",
        liveBucket: NEW_BUILD.bucket,
        liveMetadata: NEW_BUILD,
        incomingMetadata: OLD_BUILD,
        env: { [OVERRIDE_VAR]: "true" },
    });
    assert.equal(status, 0);
    assert.match(stdout, /rollback escape hatch/);
});

// ---------------------------------------------------------------------------
// The metadata document itself.
// ---------------------------------------------------------------------------

function renderMetadata(env) {
    return execFileSync(
        "bash",
        [
            "-c",
            `source "${COMMON_SH}" && render_origin_bucket_metadata 1700000000000 ` +
            `deadbeefcafefeed0123456789abcdef01234567 some-bucket http://some.invalid`,
        ],
        { env: { PATH: process.env.PATH, HOME: process.env.HOME || "", ...env }, encoding: "utf8" },
    );
}

test("render_origin_bucket_metadata emits valid JSON with a numeric run id in CI", () => {
    const doc = JSON.parse(renderMetadata({ GITHUB_RUN_ID: "35266996109", GITHUB_RUN_ATTEMPT: "2" }));
    assert.equal(doc.runId, 35266996109);
    assert.equal(doc.runAttempt, 2);
    assert.equal(doc.bucket, "some-bucket");
    assert.equal(doc.commit, "deadbeefcafefeed0123456789abcdef01234567");
    assert.equal(doc.timestamp, 1700000000000);
    assert.equal(doc.url, "http://some.invalid");
    // Numbers, not strings: the guard compares them without coercing.
    assert.equal(typeof doc.runId, "number");
});

test("render_origin_bucket_metadata emits JSON null off CI, not the string 'null'", () => {
    const doc = JSON.parse(renderMetadata({}));
    assert.equal(doc.runId, null);
    assert.equal(doc.runAttempt, null);
    // A laptop build must not be orderable by accident.
    assert.equal(toRunId(doc.runId), null);
});

test("render_origin_bucket_metadata stays valid JSON when the run id is garbage", () => {
    // GITHUB_RUN_ID is interpolated unquoted, so a non-numeric value would otherwise
    // emit a document nothing downstream can parse.
    const doc = JSON.parse(renderMetadata({ GITHUB_RUN_ID: 'oops", "x": "' }));
    assert.equal(doc.runId, null);
});

test("the document render_origin_bucket_metadata writes is what the guard reads", () => {
    // Ties the two halves together: if either side's field names drift, this fails.
    const doc = normalizeMetadata(
        JSON.parse(renderMetadata({ GITHUB_RUN_ID: "42", GITHUB_RUN_ATTEMPT: "1" })),
    );
    assert.equal(doc.runId, 42);
    assert.equal(doc.bucket, "some-bucket");
    assert.equal(decidePublish(doc, { ...doc, runId: 43, bucket: "other", commit: "z".repeat(40) }).regression, true);
});
