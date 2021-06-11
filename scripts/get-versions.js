const path = require("path");
const fs = require("fs");
const { graphql } = require("@octokit/graphql");
const { createActionAuth } = require("@octokit/auth-action");

const destination = path.join(__dirname, "..", "data", "versions.json");
const latestVersionPath = path.join(__dirname, "..", "static", "latest-version");

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
              tagger {
                date
              }
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

const listTags = async (graphqlWithAuth, cursor) => {
  const {
    repository: { refs },
  } = await graphqlWithAuth(query, {
    cursor,
  });

  if (refs.pageInfo.hasNextPage) {
    const res = await listTags(graphqlWithAuth, refs.pageInfo.endCursor);
    return [...refs.nodes, ...res];
  }
  return refs.nodes;
};

const baseUrl = "https://get.pulumi.com/releases/sdk";

const createDownloadLinks = (version) => ({
  "linux-x64": `${baseUrl}/pulumi-${version}-linux-x64.tar.gz`,
  "linux-arm64": `${baseUrl}/pulumi-${version}-linux-arm64.tar.gz`,
  "darwin-x64": `${baseUrl}/pulumi-${version}-darwin-x64.tar.gz`,
  "darwin-arm64": `${baseUrl}/pulumi-${version}-darwin-arm64.tar.gz`,
  "windows-x64": `${baseUrl}/pulumi-${version}-windows-x64.zip`,
});

const main = async () => {
  const auth = createActionAuth();
  const graphqlWithAuth = graphql.defaults({
    request: {
      hook: auth.hook,
    },
  });

  const tags = await listTags(graphqlWithAuth);

  const latestVersion = fs.readFileSync(latestVersionPath, 'utf-8');

  // We only want ordinary release tags
  const releases = tags
    .filter((tag) => !tag.name.match(/sdk|pkg/))
    .map((tag) => ({
      version: tag.name,
      date: tag.target?.committedDate || tag.target?.tagger?.date,
      downloads: createDownloadLinks(tag.name),
      checksums: `${baseUrl}/pulumi-${tag.name.slice(1)}-checksums.txt`,
      latest: latestVersion === tag.name.slice(1) ? true : undefined,
    }))
    .reverse();

  fs.writeFileSync(destination, JSON.stringify(releases, null, 2));
};

main().catch(console.error);
