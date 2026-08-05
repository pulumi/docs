const fs = require("fs");
const path = require("path");
const { Octokit } = require("@octokit/rest");

// How long to sleep between checks for other in-progress runs.
const pollIntervalMs = 60000;

// Where we record the number of seconds this run spent parked in the queue. The
// build-duration alert (scripts/ci-build-duration-alert.sh) reads this file and subtracts
// the wait from the wall-clock time of the "Build and deploy" step, so a backed-up queue
// doesn't get reported in Slack as a slow build. A missing file means "no wait." Honors
// CI_BUILD_QUEUE_WAIT_FILE so the writer and the alert script's reader can't drift apart.
const queueWaitFile = process.env.CI_BUILD_QUEUE_WAIT_FILE
    || path.join(__dirname, "..", ".build-queue-wait-seconds");

// Wait for any in-progress runs of the same workflow on this branch to complete before
// proceeding. In other words, if the current workflow is an instance of the "foo"
// workflow, and there's another "foo" workflow running for a different commit on the same
// branch as this one, wait for that workflow to complete before exiting (in order to
// prevent the current workflow from continuing).
// Inspired by https://github.com/softprops/turnstyle.
async function waitForInProgressRuns() {

    // See https://docs.github.com/en/free-pro-team@latest/actions/reference/environment-variables
    // for an explanation of each of these variables.
    const githubToken = process.env.GITHUB_TOKEN;
    const currentRunID = parseInt(process.env.GITHUB_RUN_ID, 10);
    const workflowName = process.env.GITHUB_WORKFLOW;
    const [ owner, repo ] = process.env.GITHUB_REPOSITORY.split("/");
    const branch = process.env.GITHUB_HEAD_REF || process.env.GITHUB_REF.replace("refs/heads/", "");
    const status = "in_progress";

    const octokit = new Octokit({
        auth: githubToken,
    });

    // Given the current workflow name, fetch its ID.
    const workflows = await octokit.rest.actions.listRepoWorkflows({ owner, repo });
    const workflow_id = workflows.data.workflows.find(workflow => workflow.name === workflowName).id;

    let waitedMs = 0;

    while (true) {
        // Fetch a paginated list of in-progress runs of the current workflow.
        const runs = await octokit.paginate(
          octokit.rest.actions.listWorkflowRuns.endpoint.merge({
            owner,
            repo,
            branch,
            workflow_id,
            status,
          })
        );

        // Sort in-progress runs descendingly, excluding the current one.
        const recent = runs
            .sort((a, b) => b.id - a.id)
            .filter(run => run.id < currentRunID);

        console.log(`Found ${recent.length} other ${workflowName} job(s) running on branch ${branch}.`);

        if (recent.length === 0) {
            break;
        }

        const [ mostRecent ] = recent;
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
