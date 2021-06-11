const { Octokit } = require("@octokit/rest");
const parseDiff = require("parse-diff");
const execSync = require("child_process").execSync;

// Find the commits that occurred between the two commits provided
// and return a bulleted list of their GitHub links.
async function getCommitsBetween(base, head) {
    const githubToken = process.env.GITHUB_TOKEN;
    const [ owner ] = process.env.GITHUB_REPOSITORY.split("/");
    const repo = "pulumi-hugo";

    const octokit = new Octokit({
        auth: githubToken,
    });

    const commits = await octokit.rest.repos.compareCommits({
      owner,
      repo,
      base,
      head,
    });

    console.log(`${commits.data.commits.map(commit => `* ${commit.html_url}`).join("\n")}`);
}

const diff = execSync("git diff").toString("utf-8");
const files = parseDiff(diff);

// Loop through the files of the diff (if any) looking for changes to go.mod specifically.
files.forEach(file => {
    if (file.from === file.to && file.to === "go.mod") {
        let deletion, addition;

        file.chunks.map(chunk => {
            chunk.changes.map(change => {
                if (change.del) {
                    deletion = change.content;
                } else if (change.add) {
                    addition = change.content;
                }
            });
        });

        if (deletion && addition) {
            // Extract the Git SHA from the go.mod reference line -- e.g.,
            // "github.com/pulumi/pulumi-hugo/themes/default v0.0.0-20210409102228-8b0e4c5741cb // indirect"
            const re = /github\.com\/pulumi\/pulumi-hugo\/themes\/default [v\.0]+-[\d]+-([\w]+)/;

            const base = deletion.match(re)[1];
            const head = addition.match(re)[1];

            if (base && head) {
                getCommitsBetween(base, head);
            }
        }
    }
});

// Unhandled errors that happen within Promises yield warnings, but do not yet cause the
// process to exit nonzero.
// https://nodejs.org/api/process.html#process_event_unhandledrejection
process.on("unhandledRejection", (error) => {
    throw error;
});
