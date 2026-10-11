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
function runSnippet(snippet, { errexit = true, env = {} } = {}) {
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
        // Mentions the lock phrase in passing, then dies of something unrelated.
        // An unanchored substring match reads this as a lock conflict and retries
        // a permanent failure for minutes.
        `mentions_lock_then_fails() {`,
        `    echo $(( $(cat "$COUNT") + 1 )) > "$COUNT"`,
        `    echo "warning: retrying: [409] Conflict: Another update is currently in progress."`,
        `    echo "error: update failed: aws:cloudfront/distribution: InvalidViewerCertificate" >&2`,
        `    return 9`,
        `}`,
        `other_failure() {`,
        `    echo $(( $(cat "$COUNT") + 1 )) > "$COUNT"`,
        `    echo "error: the stack has a resource in a failed state" >&2`,
        `    return 7`,
        `}`,
        `always_succeeds() { echo $(( $(cat "$COUNT") + 1 )) > "$COUNT"; echo "Resources: 1 unchanged"; }`,
        // Shadow the real sleep. Most tests pin PULUMI_LOCK_RETRY_DELAY to 0, but a
        // test that deliberately feeds the validation a bad value gets the real 30s
        // default back -- and then paid for it, adding 30 seconds to every
        // `make test`. The backoff schedule is documented in run-pulumi.sh and
        // asserted by reading it, not by waiting for it; nothing here tests timing.
        `sleep() { :; }`,
        extractFunction(),
        snippet,
    ].join("\n");

    const result = spawnSync("bash", ["-c", program], {
        encoding: "utf8",
        // A bug in the attempt cap means an unbounded loop, and with sleep stubbed
        // that loop spins hot -- it would hang the suite rather than fail it. Kill
        // it instead, so the bug surfaces as a failed assertion in seconds.
        timeout: 15000,
        env: {
            ...process.env,
            TMPDIR: scratch,
            // Keep the suite fast; the real defaults are 5 attempts / 30s.
            PULUMI_LOCK_MAX_ATTEMPTS: "3",
            PULUMI_LOCK_RETRY_DELAY: "0",
            ...env,
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

// The function can be flawless and still do nothing if it is not called. Deleting
// `retry_on_stack_lock` from both call sites left every other test in this file
// passing, which means the suite proved the logic and not the wiring -- for a
// change whose whole value is that it runs in production, that is the gap that
// matters. These two tests read the script rather than the extracted function.
test("both stack-taking commands go through the wrapper", () => {
    const source = fs.readFileSync(RUN_PULUMI_SH, "utf8");
    assert.match(source,
        /^\s*retry_on_stack_lock\s+pulumi\s+-C\s+infrastructure\s+refresh\b/m,
        "`pulumi refresh` must be wrapped in retry_on_stack_lock");
    assert.match(source, /^\s*retry_on_stack_lock\s+publish_if_newest\s*$/m,
        "`pulumi up` must run inside publish_if_newest, wrapped in retry_on_stack_lock");
});

// The publish-ordering check only means something if it runs on the same attempt
// as the `pulumi up` it guards. Checked once before the retry, a run that lost a
// lock conflict to a newer deploy would pass the stale check and then publish over
// that newer deploy on its retry -- the exact regression the check exists to stop.
test("the publish-ordering check runs inside the retried unit, before up", () => {
    const source = fs.readFileSync(RUN_PULUMI_SH, "utf8");
    const body = source.match(/publish_if_newest\(\)\s*\{([\s\S]*?)^\s*\}/m);
    assert.ok(body, "publish_if_newest() must exist");
    const check = body[1].search(/node\s+\.\/scripts\/check-publish-ordering\.js\s*\|\|\s*return/);
    const up = body[1].search(/pulumi\s+-C\s+infrastructure\s+up\b/);
    assert.ok(check >= 0, "publish_if_newest must run the ordering check and stop if it refuses");
    assert.ok(up > check, "the ordering check must come before `pulumi up`");
    const outside = source.replace(body[0], "");
    assert.doesNotMatch(outside, /check-publish-ordering\.js/,
        "the ordering check must not also run once outside the retried unit");
});

test("no bare pulumi refresh/up escapes the wrapper", () => {
    const source = fs.readFileSync(RUN_PULUMI_SH, "utf8");
    const body = source.match(/publish_if_newest\(\)\s*\{[\s\S]*?^\s*\}/m);
    const outside = body ? source.replace(body[0], "") : source;
    const bare = [...outside.matchAll(
        /^\s*pulumi\s+-C\s+infrastructure\s+(?:refresh|up)\b.*$/gm,
    )].map(m => m[0].trim());
    assert.deepEqual(bare, [],
        `these take the stack lock but are not wrapped: ${bare.join("; ")}`);
});

// F1's shape. The phrase appears in recovered-warning output, but the attempt died
// of something permanent. Retrying it burns the whole backoff budget and delays a
// real error -- exactly what the "fails fast" promise rules out.
test("does NOT retry a non-lock failure whose output merely mentions the lock", () => {
    const r = runSnippet(`retry_on_stack_lock mentions_lock_then_fails || echo "EXIT=$?"`);
    assert.match(r.stdout, /EXIT=9/, "the command's own status must surface");
    assert.equal(r.calls, 1, "a passing mention of the phrase must not trigger a retry");
});

// A non-numeric override made `[ 1 -ge five ]` exit 2, which `if` reads as false,
// so the attempt cap never tripped and the loop ran until the job timed out.
test("survives a non-numeric attempt cap instead of looping forever", () => {
    const r = runSnippet(
        `retry_on_stack_lock lock_then_succeed 99 || echo "EXIT=$?"`,
        { env: { PULUMI_LOCK_MAX_ATTEMPTS: "five" } },
    );
    assert.match(r.stdout, /EXIT=255/, "it must still terminate and propagate the failure");
    assert.equal(r.calls, 5, "a bad value must fall back to the documented default of 5");
    assert.match(r.stderr, /not a number/, "and say so, rather than failing silently");
});

test("survives a non-numeric retry delay", () => {
    const r = runSnippet(
        `retry_on_stack_lock lock_then_succeed 1 || echo "EXIT=$?"`,
        { env: { PULUMI_LOCK_RETRY_DELAY: "soon", PULUMI_LOCK_MAX_ATTEMPTS: "2" } },
    );
    assert.equal(r.calls, 2, "it must retry normally rather than hang on a bad delay");
    assert.match(r.stderr, /not a number/);
});
