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

function deployBucketNameFor(env, eventName, { runId, runAttempt, eventPath } = {}) {
    const bashEnv = {
        DEPLOYMENT_ENVIRONMENT: env,
        GITHUB_EVENT_NAME: eventName,
        GITHUB_EVENT_PATH: eventPath || "",
        GITHUB_RUN_ID: runId ?? "1234567890",
        GITHUB_RUN_ATTEMPT: runAttempt ?? "1",
    };
    return runBash(bashEnv, "deploy_bucket_name");
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

test("deploy_bucket_name: fails loudly instead of silently truncating when there's no room even after trimming", () => {
    // A caller-supplied BUILD_IDENTIFIER with no event segment to trim, deliberately
    // sized so that prefix + identifier + uniquifier can't possibly fit in 63 chars.
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
