const fs = require("fs");
const path = require("path");
const { Octokit } = require("@octokit/rest");

// How long to sleep between checks for other in-progress runs.
const pollIntervalMs = 60000;

// Stop waiting after this long. A deploy runs ~9 minutes, so a healthy queue
// never approaches it; hitting it means a predecessor is wedged.
const maxWaitMs = 45 * 60 * 1000;

// Where we record the number of seconds this run spent parked in the queue. The
// build-duration alert (scripts/ci-build-duration-alert.sh) reads this file and subtracts
// the wait from the wall-clock time of the "Build and deploy" step, so a backed-up queue
// doesn't get reported in Slack as a slow build. A missing file means "no wait." Honors
// CI_BUILD_QUEUE_WAIT_FILE so the writer and the alert script's reader can't drift apart.
const queueWaitFile = process.env.CI_BUILD_QUEUE_WAIT_FILE
    || path.join(__dirname, "..", ".build-queue-wait-seconds");

// Wait for any in-progress run of the same workflow — on ANY branch — to complete before
// proceeding. What this serializes is the `pulumi up` in run-pulumi.sh, and the thing that
// needs serializing is the Pulumi stack it updates, which is a property of the workflow
// (one stack per workflow: www-testing for testing-build-and-deploy.yml, production for
// build-and-deploy.yml), NOT of the branch. Two runs of the same workflow on two different
// branches update the same stack.
//
// This used to pass `branch` to listWorkflowRuns, so it only ever waited for a run on the
// *same* branch. That made it blind to exactly the collision it exists to prevent: on
// 2026-09-17 a dispatched staging deploy for PR #21698 (branch fix/broken-links-2026-09-17,
// run 35266933458) and a master push (run 35266996109) overlapped by 39 seconds, each
// reported "Found 0 other job(s) running", and the second one into `pulumi refresh` died on
//
//     error: [409] Conflict: Another update is currently in progress.
//
// after having already built the site and synced the bucket — ~7 minutes in, and reported
// on the PR as failed staging evidence for a two-line redirect change.
//
// Dropping the branch filter is safe against deadlock because the wait is strictly
// ordered: a run only ever waits for runs with a LOWER id, so the oldest in-flight run
// never waits for anybody. Inspired by https://github.com/softprops/turnstyle.
async function waitForInProgressRuns() {

    // See https://docs.github.com/en/free-pro-team@latest/actions/reference/environment-variables
    // for an explanation of each of these variables.
    const githubToken = process.env.GITHUB_TOKEN;
    const currentRunID = parseInt(process.env.GITHUB_RUN_ID, 10);
    const workflowName = process.env.GITHUB_WORKFLOW;
    const [ owner, repo ] = process.env.GITHUB_REPOSITORY.split("/");
    // Both statuses that hold the stack. `in_progress` alone left a hole the
    // branch fix below did not close: a QUEUED run (waiting for a runner, or
    // waiting on environment approval) is not returned by
    // `status=in_progress`. Run 100 queued while 101 is running → 101 lists
    // in-progress runs, sees none, proceeds; 100 then starts, sees 101, and
    // discards it because 101 > 100 — both enter `pulumi up` on the same
    // stack and one takes the 409 this script exists to prevent. Queued runs
    // are the common case precisely when the queue is backed up.
    const statuses = ["in_progress", "queued", "waiting"];

    const octokit = new Octokit({
        auth: githubToken,
    });

    // Resolve the current workflow's ID from the run itself. Looking it up by name in
    // listRepoWorkflows was a paginated search that only ever read the first page of 30:
    // the repo has more workflows than that, and the API lists disabled workflows last,
    // so a workflow that was disabled while a run was in flight (or that simply sorted
    // past page 1) came back undefined and this script crashed after the bucket was built
    // but before `pulumi up`. The run already knows which workflow it belongs to.
    const currentRun = await octokit.rest.actions.getWorkflowRun({ owner, repo, run_id: currentRunID });
    const workflow_id = currentRun.data.workflow_id;

    let waitedMs = 0;

    while (true) {
        // Fetch every run of this workflow that is holding or about to hold
        // the stack. No `branch` filter: the stack is shared by every
        // branch's run of this workflow. See the header comment.
        const pages = await Promise.all(statuses.map(status =>
          octokit.paginate(
            octokit.rest.actions.listWorkflowRuns.endpoint.merge({
              owner,
              repo,
              workflow_id,
              status,
            })
          )
        ));
        const byId = new Map();
        for (const run of pages.flat()) {
            byId.set(run.id, run);  // a run can change status between calls
        }
        const runs = [...byId.values()];

        // Sort in-progress runs descendingly, excluding the current one.
        const recent = runs
            .sort((a, b) => b.id - a.id)
            .filter(run => run.id < currentRunID);

        console.log(`Found ${recent.length} other ${workflowName} job(s) running or queued (all branches).`);

        if (recent.length === 0) {
            break;
        }

        const [ mostRecent ] = recent;
        if (waitedMs >= maxWaitMs) {
            // Proceeding is the lesser evil: a 409 fails one deploy loudly,
            // where an unbounded wait parks this job until the six-hour
            // default and fails it with nothing to read.
            console.log(`::warning::Waited ${Math.round(waitedMs / 60000)}m for ` +
                `${mostRecent.html_url}; giving up on the queue and proceeding. ` +
                `A [409] Conflict here means that run is still holding the stack.`);
            break;
        }
        console.log(`Waiting for ${mostRecent.html_url} to complete before continuing.`);
        await new Promise(resolve => setTimeout(resolve, pollIntervalMs)); // One minute.
        waitedMs += pollIntervalMs;
    }

    const waitedSeconds = Math.round(waitedMs / 1000);
    console.log(`Continuing. Waited ${waitedSeconds}s for other runs to finish.`);
    recordQueueWait(waitedSeconds);
}

// Records the queue wait for the build-duration alert. Best-effort: failing to write this
// file must never fail the deploy, so we log and move on.
function recordQueueWait(seconds) {
    try {
        fs.writeFileSync(queueWaitFile, `${seconds}\n`);
    } catch (error) {
        console.log(`Unable to record the queue wait in ${queueWaitFile}: ${error.message}`);
    }
}

// Unhandled errors that happen within Promises yield warnings, but do not (yet) cause the
// process to exit nonzero. Since we want this script to fail loudly when something goes
// wrong, we listen for unhandledRejection events and rethrow, exiting 1.
// https://nodejs.org/api/process.html#process_event_unhandledrejection
process.on("unhandledRejection", (error) => {
    throw error;
});

waitForInProgressRuns();
