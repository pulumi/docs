const { Octokit } = require("@octokit/rest");
const parseDiff = require("parse-diff");
const execSync = require("child_process").execSync;

// Find the commits that occurred between the two commits provided
// and return a bulleted list of their GitHub links.
async function getCommitsBetween(owner, repo, base, head) {
    const githubToken = process.env.GITHUB_TOKEN;

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
const changes = {};

// Loop through the files of the diff (if any) looking for changes to go.mod specifically.
files.forEach(file => {
    if (file.from === file.to && file.to === "go.mod") {
        file.chunks.map(chunk => {
            chunk.changes.map(change => {

                // Extract the repo owner, repo name, and commit SHA from the go.mod reference line.
                const parts = change.content.match(/github.com\/(.+) [v\.0]+-[\d]+-([\w]+)/);

                if (parts) {
                    const [_, module, ref] = parts;

                    if (module && ref) {
                        const [ owner, repo ] = module.split("/");
                        const key = `${owner}/${repo}`;

                        if (!changes[key]) {
                            changes[key] = {
                                owner,
                                repo,
                            };
                        }

                        if (change.del) {
                            changes[key].base = ref;
                        } else if (change.add) {
                            changes[key].head = ref;
                        }
                    }
                }
            });
        });

        Object.values(changes).forEach(e => {
            if (e.owner && e.repo && e.base && e.head) {
                getCommitsBetween(e.owner, e.repo, e.base, e.head);
            }
        });
    }
});

// Unhandled errors that happen within Promises yield warnings, but do not yet cause the
// process to exit nonzero.
// https://nodejs.org/api/process.html#process_event_unhandledrejection
process.on("unhandledRejection", (error) => {
    throw error;
});
