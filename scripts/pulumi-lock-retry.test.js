// Unit tests for retry_on_stack_lock in scripts/run-pulumi.sh.
//
// That function retries a Pulumi operation that failed *only* because another
// update held the stack lock ("[409] Conflict: Another update is currently in
// progress"), and must not retry anything else. Both halves matter: the first
// is why a merge train no longer takes hard failures when
// scripts/await-in-progress.js gives up and proceeds; the second is why a
// genuine deploy error still fails fast instead of burning minutes of backoff.
//
// Like scripts/deploy-bucket-naming.test.js, these run against a bash
// subprocess with fake commands standing in for pulumi, so no network, no AWS
// and no Pulumi CLI are required.

const { test } = require("node:test");
const assert = require("node:assert/strict");
const { spawnSync } = require("node:child_process");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");

const RUN_PULUMI_SH = path.join(__dirname, "run-pulumi.sh");

// Pull just the function out of the script. run-pulumi.sh cannot be sourced --
// it exits on a missing action argument and then does real work -- so the test
// extracts the definition instead. If the function is renamed or reformatted
// past this marker, fail loudly rather than silently testing nothing.
function extractFunction() {
    const source = fs.readFileSync(RUN_PULUMI_SH, "utf8");
    const match = source.match(/^retry_on_stack_lock\(\) \{\n[\s\S]*?^\}$/m);
    assert.ok(
        match,
        "could not find retry_on_stack_lock() in run-pulumi.sh -- if it was renamed " +
            "or reformatted, update this test rather than deleting it",
    );
    return match[0];
}

// Runs `snippet` with the extracted function in scope, under the same shell
// options run-pulumi.sh sets. Returns the exit status plus a call counter that
// the fake commands increment, so a test can tell "failed once" from "failed
// after three retries" -- the two look identical by exit status alone.
function runSnippet(snippet, { errexit = true } = {}) {
    const tmpdir = fs.mkdtempSync(path.join(os.tmpdir(), "lock-retry-"));
    const counter = path.join(tmpdir, "calls");
    fs.writeFileSync(counter, "0");

    // A dedicated TMPDIR so the leak check below is deterministic: mktemp honors
    // it, and nothing else writes here.
    const scratch = path.join(tmpdir, "scratch");
    fs.mkdirSync(scratch);

    const program = [
        `set -o pipefail`,
        errexit ? `set -o errexit` : `set +o errexit`,
        `COUNT="${counter}"`,
        // Fails with the stack-lock 409 for the first $1 calls, then succeeds.
        `lock_then_succeed() {`,
        `    local fail_times=$1 n`,
        `    n=$(( $(cat "$COUNT") + 1 )); echo "$n" > "$COUNT"`,
        `    if [ "$n" -le "$fail_times" ]; then`,
        `        echo "error: [409] Conflict: Another update is currently in progress." >&2`,
        `        return 255`,
        `    fi`,
        `    echo "Updating (pulumi/www-production)"`,
        `}`,
        `other_failure() {`,
        `    echo $(( $(cat "$COUNT") + 1 )) > "$COUNT"`,
        `    echo "error: the stack has a resource in a failed state" >&2`,
        `    return 7`,
        `}`,
        `always_succeeds() { echo $(( $(cat "$COUNT") + 1 )) > "$COUNT"; echo "Resources: 1 unchanged"; }`,
        extractFunction(),
        snippet,
    ].join("\n");

    const result = spawnSync("bash", ["-c", program], {
        encoding: "utf8",
        env: {
            ...process.env,
            TMPDIR: scratch,
            // Keep the suite fast; the real defaults are 5 attempts / 30s.
            PULUMI_LOCK_MAX_ATTEMPTS: "3",
            PULUMI_LOCK_RETRY_DELAY: "0",
        },
    });

    const leaked = fs.readdirSync(scratch);
    const calls = Number(fs.readFileSync(counter, "utf8").trim());
    fs.rmSync(tmpdir, { recursive: true, force: true });

    return {
        status: result.status,
        stdout: result.stdout,
        stderr: result.stderr,
        calls,
        leaked,
    };
}

test("succeeds on the first attempt", () => {
    const r = runSnippet(`retry_on_stack_lock always_succeeds`);
    assert.equal(r.status, 0);
    assert.equal(r.calls, 1);
});

test("retries the stack lock and succeeds once it clears", () => {
    const r = runSnippet(`retry_on_stack_lock lock_then_succeed 2`);
    assert.equal(r.status, 0, "should succeed on the third attempt");
    assert.equal(r.calls, 3);
});

test("gives up after max attempts and propagates the failure", () => {
    const r = runSnippet(`retry_on_stack_lock lock_then_succeed 99 || echo "EXIT=$?"`);
    assert.match(r.stdout, /EXIT=255/, "the command's own status must surface");
    assert.equal(r.calls, 3, "must stop at PULUMI_LOCK_MAX_ATTEMPTS, not retry forever");
});

// The guard that keeps this from being a blanket retry. Without it a real
// deploy error would be retried too, delaying the report by minutes of backoff.
test("does NOT retry a failure that is not the stack lock", () => {
    const r = runSnippet(`retry_on_stack_lock other_failure || echo "EXIT=$?"`);
    assert.match(r.stdout, /EXIT=7/, "the command's own status must surface unchanged");
    assert.equal(r.calls, 1, "a non-lock failure must fail immediately, not retry");
});

test("streams the command's output rather than swallowing it", () => {
    const r = runSnippet(`retry_on_stack_lock lock_then_succeed 1`);
    assert.match(r.stdout, /Updating \(pulumi\/www-production\)/);
});

test("leaves no temp files behind", () => {
    const r = runSnippet(`retry_on_stack_lock lock_then_succeed 1`);
    assert.deepEqual(r.leaked, [], "the capture file must be cleaned up");
});

// The function turns errexit off to handle failures itself. It has to put the
// caller's setting back exactly as it found it -- an earlier draft switched it
// on unconditionally, which would silently change the semantics of any caller
// that had deliberately turned it off.
test("restores the caller's errexit when it was set", () => {
    const r = runSnippet(
        [`retry_on_stack_lock always_succeeds`, `false`, `echo "REACHED"`].join("\n"),
        { errexit: true },
    );
    assert.doesNotMatch(r.stdout, /REACHED/, "errexit must still abort the caller");
    assert.notEqual(r.status, 0);
});

test("restores the caller's errexit when it was NOT set", () => {
    const r = runSnippet(
        [`retry_on_stack_lock always_succeeds`, `false`, `echo "REACHED"`].join("\n"),
        { errexit: false },
    );
    assert.match(r.stdout, /REACHED/, "errexit must not be switched on behind the caller's back");
});
