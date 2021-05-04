const path = require("path");
const fs = require("fs");
const rest = require("@octokit/rest");
const { createActionAuth } = require("@octokit/auth-action");

const destination = path.join(__dirname, "..", "static", "versions.json");

const main = async () => {
  const auth = createActionAuth();
  const authentication = await auth();
  const octokit = new rest.Octokit(authentication);

  const tags = await octokit.paginate(octokit.repos.listTags, {
    repo: "pulumi",
    owner: "pulumi",
    per_page: 100,
  });

  // We only want ordinary release tags
  const releases = tags
    .filter((tag) => !tag.name.match(/sdk|pkg/))
    .map((tag) => tag.name);

  fs.writeFileSync(destination, JSON.stringify(releases, null, 2));
};

main().catch(console.error);
