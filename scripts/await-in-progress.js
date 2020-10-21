const { Octokit } = require("@octokit/rest");

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
    const branch = process.env.GITHUB_HEAD_REF || GITHUB_REF.replace("refs/heads/", "");
    const status = "in_progress";

    const octokit = new Octokit({
        auth: githubToken,
    });

    // Given the current workflow name, fetch its ID.
    const workflows = await octokit.actions.listRepoWorkflows({ owner, repo });
    const workflow_id = workflows.data.workflows.find(workflow => workflow.name === workflowName).id;

    // Fetch a paginated list of in-progress runs of the current workflow.
    const runs = await octokit.paginate(
        octokit.actions.listWorkflowRuns.endpoint.merge({ owner, repo, branch, workflow_id, status }),
    );

    // Sort in-progress runs descendingly, excluding the current one.
    const recent = runs
        .sort((a, b) => b.id - a.id)
        .filter(run => run.id < currentRunID);

    console.log(`Found ${recent.length} other ${workflowName} job(s) running on branch ${branch}.`);

    if (recent.length > 0) {
        const [ mostRecent ] = recent;
        console.log(`Waiting for ${mostRecent.html_url} to complete before continuing.`);
        await Promise.resolve(setTimeout(waitForInProgressRuns, 60000)); // One minute.
    } else {
        console.log("Continuing.");
    }
}

waitForInProgressRuns();
