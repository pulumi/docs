const fs = require("fs");

// Site sections whose pages emit an index.md artifact alongside index.html (the
// `markdown` output format, enabled via `outputs`/`cascade` front matter in
// content/docs/_index.md, content/what-is/_index.md and content/product/_index.md;
// the homepage enables it in config/_default/config.yml). Keep in step with the
// allowlists in infrastructure/cloudfrontFunctions.ts.
const MARKDOWN_SECTIONS = ["docs/", "what-is/", "product/"];

// Paths inside those sections that are NOT Hugo pages and so have no index.md:
// the generated SDK API reference (copied in from static-prebuilt/) and the
// frozen versioned-docs archive, which is served from its own bucket.
const NON_MARKDOWN_PREFIXES = ["docs/reference/pkg/", "docs/versioned/"];

// Absolute redirect targets on this origin are treated like site-relative ones.
const SITE_ORIGINS = ["https://www.pulumi.com"];

function hasMarkdownArtifact(path) {
    // `path` is site-relative without the leading slash, e.g. "docs/iac/" or "".
    if (path === "") {
        return true; // the homepage emits /index.md
    }
    return MARKDOWN_SECTIONS.some(prefix => path.startsWith(prefix))
        && !NON_MARKDOWN_PREFIXES.some(prefix => path.startsWith(prefix));
}

// Given a redirect target, return the URL of that page's markdown artifact, or
// null when the target isn't a markdown-enabled page on this site (external URLs,
// file targets like foo.html, the API reference, sections without index.md).
function markdownLocation(location) {
    let origin = "";
    let rest = location;
    if (!location.startsWith("/")) {
        origin = SITE_ORIGINS.find(o => location.startsWith(o + "/"));
        if (!origin) {
            return null;
        }
        rest = location.slice(origin.length);
    }
    if (rest.startsWith("//")) {
        return null; // protocol-relative URL to another host
    }

    const match = rest.match(/^([^?#]*)(.*)$/);
    const path = match[1];
    const suffix = match[2];
    if (!path.endsWith("/")) {
        return null;
    }
    if (!hasMarkdownArtifact(path.slice(1))) {
        return null;
    }
    return `${origin}${path}index.md${suffix}`;
}

// For moved pages in markdown-enabled sections, also create redirects for the
// old .md keys, so a .md-suffix client (or an Accept: text/markdown request,
// which the CloudFront functions rewrite to .../index.md) gets a 301 instead of
// a 404. When the target is itself a markdown-enabled page, the .md redirect
// points at its index.md artifact, so the client stays on markdown instead of
// being handed the HTML page (pulumi/docs#20594). Other targets keep the HTML
// location, which still beats a 404.
//
// A page source outside the markdown sections (e.g. a top-level alias like
// get-started/index.html) gets a .md duplicate only when its target has a
// markdown artifact: there was never an old .md URL to preserve, but the literal
// artifact path should resolve the same way the page does.
function buildMarkdownRedirects(redirects) {
    const mdRedirects = [];
    for (const line of redirects) {
        const [key, location = ""] = line.split("|");
        if (!key.endsWith(".html")) {
            continue;
        }
        const mdKey = key.replace(/\.html$/, ".md");
        // Source side: every key under a markdown section, as before. The CloudFront
        // functions rewrite Accept: text/markdown requests for any URI there to
        // .../index.md, so dropping a duplicate would turn a 301 into a 404.
        const inMarkdownSection = MARKDOWN_SECTIONS.some(prefix => key.startsWith(prefix));
        if (!inMarkdownSection && !key.endsWith("/index.html")) {
            continue;
        }
        const mdLocation = markdownLocation(location);
        if (mdLocation) {
            mdRedirects.push(`${mdKey}|${mdLocation}`);
        } else if (inMarkdownSection) {
            mdRedirects.push(`${mdKey}|${location}`);
        }
    }
    return mdRedirects;
}

function readRedirects(redirectsFile) {
    // Skip blank lines and # comments, which would otherwise be uploaded as
    // S3 objects keyed by the comment text.
    return fs.readFileSync(redirectsFile, "utf-8")
        .split("\n")
        .map(line => line.trim())
        .filter(line => line && !line.startsWith("#"));
}

async function doRedirects(bucket, redirectsFile, region) {
    const { PutObjectCommand, S3Client } = require("@aws-sdk/client-s3");

    let redirects = readRedirects(redirectsFile);
    const mdRedirects = buildMarkdownRedirects(redirects);
    redirects = redirects.concat(mdRedirects);

    console.log(`Processing ${redirects.length} redirects (${mdRedirects.length} .md duplicates)...`);

    const client = new S3Client({ region, endpoint: `https://s3.${region}.amazonaws.com` });

    // Chunk requests into groups of a thousand to process them more efficiently.
    const chunkSize = 1000;
    const chunks = [];
    const results = [];

    for (let i = 0; i < redirects.length; i += chunkSize) {
        chunks.push({ chunk: i / chunkSize, lines: redirects.slice(i, i + chunkSize) });
    }

    for await (const chunk of chunks) {
        console.log(` ↳ Processing group ${chunk.chunk + 1} of ${chunks.length} (${chunk.lines.length} URLs)...`);

        const result = await Promise.allSettled(chunk.lines.map(line => {
            const [ key, location ] = line.split("|");

            return new Promise(async (resolve, reject) => {
                try {
                    console.log(` ↳ Redirecting ${key} to ${location}`);

                    const command = new PutObjectCommand({
                        Bucket: bucket,
                        Key: key,
                        WebsiteRedirectLocation: location,
                        ACL: "public-read",
                        Body: "",
                        ContentLength: 0,
                    });

                    const res = await client.send(command);
                    const status = res.$metadata.httpStatusCode;

                    if (status < 400) {
                        resolve(status);
                    } else {
                        reject(status);
                    }
                }
                catch (error) {
                    reject(`Error redirecting ${key}: ${error}`);
                }
            });
        }));

        results.push(...result);
    }

    return results;
}

module.exports = { buildMarkdownRedirects, markdownLocation, hasMarkdownArtifact };

if (require.main === module) {
    const bucket = process.argv[2];
    const redirectsFile = process.argv[3] || "./public/redirects.txt";
    const region = process.argv[4] || "us-west-2";

    doRedirects(bucket, redirectsFile, region)
        .then(results => {

            const summary = {
                checked: results.length,
                fulfilled: results.filter(r => r.status === "fulfilled").map(r => r.value) || [],
                rejected: results.filter(r => r.status === "rejected").map(r => r.reason) || [],
            };

            console.log(" ↳ Done. ✨\n");

            if (summary.rejected.length > 0) {
                throw new Error(`One or more redirects failed: \n\n${summary.rejected.join("\n")}\n`);
            }
        });

    // Exit non-zero when something goes wrong in the promise chain.
    process.on("unhandledRejection", error => {
        throw new Error(error);
    });
}
