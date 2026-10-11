const path = require("path");
const fs = require("fs");

const destination = path.join(__dirname, "..", "data", "versions.json");
const latestVersionPath = path.join(__dirname, "..", "static", "latest-version");

const baseUrl = "https://get.pulumi.com/releases/sdk";

const query = `
  query GetTagsWithDate($cursor: String) {
    repository(name: "pulumi", owner: "pulumi") {
      refs(refPrefix: "refs/tags/", first: 100, after: $cursor) {
        pageInfo {
          hasNextPage
          endCursor
        }
        nodes {
          name
          target {
            ... on Tag {
              tagger { date }
            }
            ... on Commit {
              committedDate
            }
          }
        }
      }
    }
  }
`;

const fetchTagsPage = async (token, cursor) => {
  const res = await fetch("https://api.github.com/graphql", {
    method: "POST",
    headers: {
      authorization: `token ${token}`,
      "content-type": "application/json",
      "user-agent": "pulumi-docs-get-cli-versions",
    },
    body: JSON.stringify({ query, variables: { cursor } }),
  });
  if (!res.ok) {
    throw new Error(`GitHub GraphQL HTTP ${res.status}: ${await res.text()}`);
  }
  const body = await res.json();
  if (body.errors) {
    throw new Error(`GitHub GraphQL errors: ${JSON.stringify(body.errors)}`);
  }
  return body.data.repository.refs;
};

const listTags = async (token) => {
  const all = [];
  let cursor = null;
  for (;;) {
    const refs = await fetchTagsPage(token, cursor);
    all.push(...refs.nodes);
    if (!refs.pageInfo.hasNextPage) return all;
    cursor = refs.pageInfo.endCursor;
  }
};

const downloadLinks = (version) => ({
  "linux-x64": `${baseUrl}/pulumi-${version}-linux-x64.tar.gz`,
  "linux-arm64": `${baseUrl}/pulumi-${version}-linux-arm64.tar.gz`,
  "darwin-x64": `${baseUrl}/pulumi-${version}-darwin-x64.tar.gz`,
  "darwin-arm64": `${baseUrl}/pulumi-${version}-darwin-arm64.tar.gz`,
  "windows-x64": `${baseUrl}/pulumi-${version}-windows-x64.zip`,
  "windows-arm64": `${baseUrl}/pulumi-${version}-windows-arm64.zip`,
});

const main = async () => {
  const token = process.env.GITHUB_TOKEN;
  if (!token) {
    console.error(
      "GITHUB_TOKEN is required. In CI it's exported from ESC. Locally, run `export GITHUB_TOKEN=$(gh auth token)` and re-run."
    );
    process.exit(1);
  }

  const tags = await listTags(token);
  const latestVersion = fs.readFileSync(latestVersionPath, "utf-8");

  const releases = tags
    .filter((tag) => !tag.name.match(/sdk|pkg/))
    .map((tag) => ({
      version: tag.name,
      date: tag.target?.committedDate || tag.target?.tagger?.date,
      downloads: downloadLinks(tag.name),
      checksums: `${baseUrl}/pulumi-${tag.name.slice(1)}-checksums.txt`,
      latest: latestVersion === tag.name.slice(1) ? true : undefined,
    }))
    .reverse();

  fs.writeFileSync(destination, JSON.stringify(releases, null, 2));
};

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
