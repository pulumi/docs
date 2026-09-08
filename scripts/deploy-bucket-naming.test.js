// Unit tests for the deploy-bucket naming logic in scripts/common.sh
// (deploy_bucket_name, deploy_run_uniquifier, to_base36) and its usage in
// scripts/sync-and-test-bucket.sh.
//
// These run against a bash subprocess with common.sh sourced and CI/git
// environment variables stubbed out, so no network, no AWS, and no real git
// repo state are required. See BUILD-AND-DEPLOY.md's "Origin Bucket" section
// for the naming scheme this guards.

const { test } = require("node:test");
const assert = require("node:assert/strict");
const { execFileSync } = require("node:child_process");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");

const COMMON_SH = path.join(__dirname, "common.sh");

// Runs `source common.sh` plus an extra bash snippet, with the given env vars
// stubbed. `git_sha_short` shells out to `git rev-parse HEAD`, so we stub
// that away too (via a fake `git` on PATH) rather than relying on the
// checkout's real HEAD, which would make the test depend on which commit is
// checked out.
function runBash(env, snippet) {
    const fakeBinDir = fs.mkdtempSync(path.join(os.tmpdir(), "fakebin-"));
    const fakeGitPath = path.join(fakeBinDir, "git");
    fs.writeFileSync(
        fakeGitPath,
        '#!/bin/bash\nif [ "$1" == "rev-parse" ]; then echo "deadbeefcafefeed0123456789abcdef01234567"; fi\n',
        { mode: 0o755 },
    );

    // Minimal `jq -r ".a.b.c"` stand-in, since the workstation running this test may not
    // have jq installed. Only supports the simple dot-path form build_identifier() and
    // git_sha() actually use (e.g. `jq -r ".number"`, `jq -r ".pull_request.head.sha"`).
    const fakeJqPath = path.join(fakeBinDir, "jq");
    fs.writeFileSync(
        fakeJqPath,
        [
            "#!/usr/bin/env node",
            "const fs = require('fs');",
            "const fields = process.argv[process.argv.length - 1].replace(/^\\./, '').split('.');",
            "const input = JSON.parse(fs.readFileSync(0, 'utf8'));",
            "let value = input;",
            "for (const field of fields) { value = value == null ? undefined : value[field]; }",
            "console.log(value);",
            "",
        ].join("\n"),
        { mode: 0o755 },
    );

    const fullEnv = {
        PATH: `${fakeBinDir}:${process.env.PATH}`,
        HOME: process.env.HOME || "",
        ...env,
    };

    const result = execFileSync(
        "bash",
        ["-c", `source "${COMMON_SH}" && ${snippet}`],
        { env: fullEnv, encoding: "utf8" },
    );

    fs.rmSync(fakeBinDir, { recursive: true, force: true });
    return result.trim();
}

// Builds a minimal GitHub Actions event-payload file for the given event
// name, so build_identifier()'s pull_request branch (which reads the PR
// number from $GITHUB_EVENT_PATH) has something to parse.
function withEventPath(eventName, body, fn) {
    const dir = fs.mkdtempSync(path.join(os.tmpdir(), "ghevent-"));
    const eventPath = path.join(dir, "event.json");
    fs.writeFileSync(eventPath, JSON.stringify(body));
    try {
        return fn(eventPath);
    } finally {
        fs.rmSync(dir, { recursive: true, force: true });
    }
}

// The events that can trigger a deploy-path (non-preview) build in
// build-and-deploy.yml, plus repository_dispatch and pull_request, which
// aren't currently deploy-path triggers but are included because they are
// the longest-name cases the naming scheme must never overflow on if a
// trigger is ever added later.
const EVENTS = [
    "push",
    "schedule",
    "workflow_dispatch",
    "repository_dispatch",
    "pull_request",
];
const DEPLOYMENT_ENVIRONMENTS = ["production", "testing"];

const S3_BUCKET_NAME_RE = /^[a-z0-9]([a-z0-9-]*[a-z0-9])?$/;

// build_identifier() only emits the "<event>-" segment when BOTH GITHUB_EVENT_NAME and
// GITHUB_EVENT_PATH are set (that is how it tells a CI build from a local one), so every
// event gets a real, if minimal, payload file here. Without it the identifier collapses to
// the bare SHA and the length checks below would pass for any event name whatsoever.
function deployBucketNameFor(env, eventName, { runId, runAttempt, eventPath } = {}) {
    const run = (path) =>
        runBash(
            {
                DEPLOYMENT_ENVIRONMENT: env,
                GITHUB_EVENT_NAME: eventName,
                GITHUB_EVENT_PATH: path,
                GITHUB_RUN_ID: runId ?? "1234567890",
                GITHUB_RUN_ATTEMPT: runAttempt ?? "1",
            },
            "deploy_bucket_name",
        );
    return eventPath ? run(eventPath) : withEventPath(eventName, {}, run);
}

test("deploy_bucket_name: every event/environment combination fits the S3 63-char limit and is a valid bucket name", () => {
    for (const env of DEPLOYMENT_ENVIRONMENTS) {
        for (const eventName of EVENTS) {
            const run = () => {
                const name =
                    eventName === "pull_request"
                        ? withEventPath(
                              eventName,
                              { number: 99999, pull_request: { head: { sha: "deadbeefcafefeed0123456789abcdef01234567" } } },
                              (eventPath) => deployBucketNameFor(env, eventName, { eventPath }),
                          )
                        : deployBucketNameFor(env, eventName);

                assert.ok(
                    name.length <= 63,
                    `${env}/${eventName}: expected <=63 chars, got ${name.length} ("${name}")`,
                );
                assert.match(
                    name,
                    S3_BUCKET_NAME_RE,
                    `${env}/${eventName}: "${name}" is not a valid S3 bucket name`,
                );
            };
            run();
        }
    }
});

test("deploy_bucket_name: two runs of the same commit/event with different run IDs produce different names", () => {
    const nameA = deployBucketNameFor("production", "schedule", { runId: "1111111111" });
    const nameB = deployBucketNameFor("production", "schedule", { runId: "2222222222" });
    assert.notEqual(
        nameA,
        nameB,
        "same-commit scheduled reruns must not collide on the same bucket name",
    );
});

test("deploy_bucket_name: a re-run (same run ID, different run attempt) also produces a different name", () => {
    const nameA = deployBucketNameFor("production", "push", { runId: "1111111111", runAttempt: "1" });
    const nameB = deployBucketNameFor("production", "push", { runId: "1111111111", runAttempt: "2" });
    assert.notEqual(nameA, nameB, "a workflow re-run must not collide with the original run");
});

test("deploy_bucket_name: fails loudly instead of silently truncating when the name doesn't fit", () => {
    // A caller-supplied BUILD_IDENTIFIER deliberately sized so that prefix + identifier +
    // uniquifier can't possibly fit in 63 chars. There is no trimming fallback: the SHA and
    // the uniquifier are never shortened, and the event segment is aliased, not trimmed.
    assert.throws(() => {
        runBash(
            {
                DEPLOYMENT_ENVIRONMENT: "production",
                BUILD_IDENTIFIER: "x".repeat(40),
                GITHUB_RUN_ID: "",
                GITHUB_RUN_ATTEMPT: "",
            },
            "deploy_bucket_name",
        );
    });
});

test("preview builds keep the original, non-uniquified bucket name (regression guard for the HUGO_BASEURL coupling in build-site.sh)", () => {
    const eventPath = fs.mkdtempSync(path.join(os.tmpdir(), "ghevent-"));
    const eventJsonPath = path.join(eventPath, "event.json");
    fs.writeFileSync(
        eventJsonPath,
        JSON.stringify({ number: 4242, pull_request: { head: { sha: "deadbeefcafefeed0123456789abcdef01234567" } } }),
    );
    try {
        const name = runBash(
            {
                DEPLOYMENT_ENVIRONMENT: "testing",
                GITHUB_EVENT_NAME: "pull_request",
                GITHUB_EVENT_PATH: eventJsonPath,
            },
            'echo "$(origin_bucket_prefix)-$(build_identifier)"',
        );
        assert.equal(name, "www-testing-pulumi-docs-origin-pr-4242-deadbeef");
    } finally {
        fs.rmSync(eventPath, { recursive: true, force: true });
    }
});

// The deploy-path events and the fixed event segment each maps to. Names must come out
// as exactly <prefix>-<alias>-<sha8>-<uniquifier>, with nothing trimmed, in BOTH
// environments -- so the segment is stable and a per-event prefix filter
// (`list-recent-buckets.sh dispatch`) can match it.
const EVENT_ALIASES = {
    push: "push",
    schedule: "schedule",
    workflow_dispatch: "dispatch",
    repository_dispatch: "repo",
};

test("deploy_bucket_name: every deploy-path event uses its fixed alias, untrimmed, in every environment", () => {
    for (const env of DEPLOYMENT_ENVIRONMENTS) {
        for (const [eventName, alias] of Object.entries(EVENT_ALIASES)) {
            const name = deployBucketNameFor(env, eventName, { runId: "34279127122", runAttempt: "2" });
            const prefix = `www-${env}-pulumi-docs-origin`;
            // sha8 of the stubbed git HEAD; uniquifier is base36(34279127122) + attempt "2".
            assert.equal(
                name,
                `${prefix}-${alias}-deadbeef-fqwwnrm2`,
                `${env}/${eventName}: expected the aliased, untrimmed shape`,
            );
        }
    }
});

test("deploy_bucket_name: the per-event prefix filter get_recent_buckets() uses matches the aliased name", () => {
    // list-recent-buckets.sh <event> filters with starts_with("<prefix>-<event>"). With
    // the old trim-to-fit scheme, a workflow_dispatch bucket in testing came out as
    // "...-workflow-dispat-<sha>-<uniq>" and the documented "workflow-dispatch" filter
    // could never match it. The alias is what the filter must be given.
    const name = deployBucketNameFor("testing", "workflow_dispatch");
    assert.ok(
        name.startsWith("www-testing-pulumi-docs-origin-dispatch-"),
        `expected a "dispatch" event segment, got "${name}"`,
    );
});

test("deploy_bucket_name: an unaliased event with no room fails loudly rather than trimming", () => {
    assert.throws(() => {
        deployBucketNameFor("production", "some_very_long_hypothetical_event_name_nobody_aliased");
    });
});

test("deploy_bucket_name: result always starts with origin_bucket_prefix()-, so cleanup prefix matching keeps working", () => {
    const name = deployBucketNameFor("production", "schedule");
    assert.ok(
        name.startsWith("www-production-pulumi-docs-origin-"),
        `expected name to start with the origin bucket prefix, got "${name}"`,
    );
});

test("sanity check: this harness actually exercises the fix -- the OLD (pre-fix) same-SHA scheme would collide", () => {
    // This reconstructs the *old* destination_bucket formula
    // (origin_bucket_prefix()-build_identifier(), no uniquifier) to prove the harness
    // would have failed against the pre-change code, i.e. that test two above is not
    // vacuously true.
    const oldNameA = runBash(
        { DEPLOYMENT_ENVIRONMENT: "production", GITHUB_EVENT_NAME: "schedule", GITHUB_RUN_ID: "1111111111" },
        'echo "$(origin_bucket_prefix)-$(build_identifier)"',
    );
    const oldNameB = runBash(
        { DEPLOYMENT_ENVIRONMENT: "production", GITHUB_EVENT_NAME: "schedule", GITHUB_RUN_ID: "2222222222" },
        'echo "$(origin_bucket_prefix)-$(build_identifier)"',
    );
    assert.equal(
        oldNameA,
        oldNameB,
        "expected the pre-fix formula (no uniquifier) to collide across run IDs at the same commit -- if it doesn't, the new test's coverage is not meaningful",
    );
});
