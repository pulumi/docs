// Unit tests for dropStaleRuns in scripts/await-in-progress.js.
//
// The turnstile's only early exit is `recent.length === 0`, so a run that never
// completes blocks it forever: it stays lower-id than every new run, the loop
// always runs out the 45-minute cap, and the script then proceeds unserialized.
// Three such runs accumulated here by 2026-09 and GitHub refuses to cancel or
// delete two of them, so filtering by age is the only remedy. These tests pin
// both halves: a wedged run is dropped, and a live one never is.

const { test } = require("node:test");
const assert = require("node:assert/strict");

const { dropStaleRuns, maxRunAgeMs } = require("./await-in-progress.js");

const NOW = Date.parse("2026-09-21T23:00:00Z");
const ago = ms => new Date(NOW - ms).toISOString();
const HOUR = 60 * 60 * 1000;

// html_url is derived from id rather than fixed, because the warning names the run
// by its URL -- a hardcoded url would let a test assert on an id the message never
// actually contains.
function run(overrides = {}) {
    const id = overrides.id ?? 1;
    return {
        id,
        status: "in_progress",
        html_url: `https://github.com/pulumi/docs/actions/runs/${id}`,
        run_started_at: ago(5 * 60 * 1000),
        ...overrides,
    };
}

// Collects log output so a test can assert the skip is announced, not silent.
function capture() {
    const lines = [];
    return { lines, log: line => lines.push(line) };
}

test("keeps a run that just started", () => {
    const kept = dropStaleRuns([run()], NOW, () => {});
    assert.equal(kept.length, 1);
});

test("keeps a long-running but still-possible run", () => {
    // Just inside the bound. A real deploy this slow would be pathological, but
    // run age is not job runtime -- a run can sit queued for a long time and then
    // execute -- so anything inside the bound must still be waited on.
    const kept = dropStaleRuns([run({ run_started_at: ago(maxRunAgeMs - HOUR) })], NOW, () => {});
    assert.equal(kept.length, 1, "a run inside the bound must still be waited on");
});

// Run age is not job runtime: GitHub's six-hour timeout starts when the job gets
// a runner, so a queued-then-executing run can legitimately be older than six
// hours while genuinely holding the stack. The bound has to clear that case.
test("keeps a run older than the six-hour job timeout but inside the bound", () => {
    const kept = dropStaleRuns([run({ run_started_at: ago(12 * HOUR) })], NOW, () => {});
    assert.equal(kept.length, 1, "12h old is not proof a run is wedged");
});

test("drops a run older than a job can possibly run", () => {
    const kept = dropStaleRuns([run({ run_started_at: ago(maxRunAgeMs + HOUR) })], NOW, () => {});
    assert.equal(kept.length, 0);
});

// The real thing: run 32907599016, queued since 2026-08-25 and uncancellable.
test("drops the real wedged run that caused this", () => {
    const zombie = run({
        id: 32907599016,
        status: "queued",
        run_started_at: "2026-08-25T22:44:44Z",
        html_url: "https://github.com/pulumi/docs/actions/runs/32907599016",
    });
    const live = run({ id: 35659427886 });

    const kept = dropStaleRuns([zombie, live], NOW, () => {});
    assert.deepEqual(kept.map(r => r.id), [35659427886], "the zombie must not survive");
});

// Without a log line a wedged queue is indistinguishable from a busy one, which
// is exactly why this went unnoticed for three days.
test("announces every run it skips, naming it", () => {
    const { lines, log } = capture();
    dropStaleRuns([run({
        id: 32907599016,
        status: "queued",
        run_started_at: "2026-08-25T22:44:44Z",
        html_url: "https://github.com/pulumi/docs/actions/runs/32907599016",
    })], NOW, log);

    assert.equal(lines.length, 1);
    assert.match(lines[0], /32907599016/, "the skipped run must be identified");
    assert.match(lines[0], /queued/, "its status belongs in the message");
    assert.match(lines[0], /\d+h ago/, "its age belongs in the message");
});

test("says nothing when it skips nothing", () => {
    const { lines, log } = capture();
    dropStaleRuns([run(), run({ id: 2 })], NOW, log);
    assert.deepEqual(lines, [], "a healthy queue must stay quiet");
});

// Fail safe: this filter may only remove runs it can prove are too old. An
// unusable timestamp is not proof, and waiting needlessly beats deploying into
// a stack someone else holds.
test("keeps a run whose timestamp is missing or unparseable", () => {
    const kept = dropStaleRuns([
        run({ id: 1, run_started_at: undefined, created_at: undefined }),
        run({ id: 2, run_started_at: "not a date" }),
    ], NOW, () => {});
    assert.equal(kept.length, 2, "an unreadable timestamp must not cause a skip");
});

test("falls back to created_at when run_started_at is absent", () => {
    const kept = dropStaleRuns([run({
        run_started_at: undefined,
        created_at: ago(maxRunAgeMs + HOUR),
    })], NOW, () => {});
    assert.equal(kept.length, 0, "created_at should be used when run_started_at is missing");
});

test("preserves the other runs and their order", () => {
    const runs = [run({ id: 3 }), run({ id: 1, run_started_at: ago(maxRunAgeMs * 30) }), run({ id: 2 })];
    const kept = dropStaleRuns(runs, NOW, () => {});
    assert.deepEqual(kept.map(r => r.id), [3, 2], "filtering must not reorder what it keeps");
});

// GitHub renders at most 10 warning annotations per step. dropStaleRuns is called
// once per poll -- up to ~45 times per deploy -- so without a shared `warned` set
// one wedged run would crowd out the "giving up on the queue" warning that
// actually explains the deploy's behaviour.
test("announces each wedged run once across repeated polls", () => {
    const { lines, log } = capture();
    const warned = new Set();
    const zombie = run({ id: 32907599016, run_started_at: "2026-08-25T22:44:44Z" });

    for (let poll = 0; poll < 45; poll++) {
        dropStaleRuns([zombie], NOW, log, warned);
    }

    assert.equal(lines.length, 1, "45 polls must produce one warning, not 45");
});

test("still drops the run on every poll, not just the first", () => {
    const warned = new Set();
    const zombie = run({ id: 32907599016, run_started_at: "2026-08-25T22:44:44Z" });

    const first = dropStaleRuns([zombie], NOW, () => {}, warned);
    const second = dropStaleRuns([zombie], NOW, () => {}, warned);

    assert.equal(first.length, 0);
    assert.equal(second.length, 0, "suppressing the log must not stop the filtering");
});

test("announces each distinct wedged run once", () => {
    const { lines, log } = capture();
    const warned = new Set();
    const runs = [
        run({ id: 23509983446, run_started_at: "2026-03-24T20:09:46Z" }),
        run({ id: 32907599016, run_started_at: "2026-08-25T22:44:44Z" }),
    ];

    dropStaleRuns(runs, NOW, log, warned);
    dropStaleRuns(runs, NOW, log, warned);

    assert.equal(lines.length, 2, "each run gets its own warning, once");
    assert.match(lines.join("\n"), /23509983446/);
    assert.match(lines.join("\n"), /32907599016/);
});
