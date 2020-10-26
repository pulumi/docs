const { SiteChecker, HtmlUrlChecker } = require("broken-link-checker");
const { WebClient, LogLevel } = require('@slack/web-api');
const httpServer = require("http-server");
const path = require("path");
const fs = require("fs");

/**
 *  This script uses the programmatic API of https://github.com/stevenvachon/broken-link-checker
    to check the links (including images, iframes, and client-side redirects) for either an individual page
    or for a whole site. Usage:

    # Check all links on pulumi.com:
    $ node scripts/check-links.js "https://www.pulumi.com" "site"

    # Check all links on pulumi.com, and retry failed runs up to 3 times:
    $ node scripts/check-links.js "https://www.pulumi.com" "site" 3

    # Check the links on pulumi.com/docs/get-started/install/versions:
    $ node scripts/check-links.js "https://www.pulumi.com/docs/get-started/install/versions/" "page"

    # Check the links of a local build (which starts a local server automatically):
    $ node scripts/check-links.js "local" "site"

    # Log successes as well as failures.
    $ DEBUG=1 node scripts/check-links.js "https://www.pulumi.com" "site"
 */

let [ baseURL, checkScope, maxRetries ] = process.argv.slice(2);
let retryCount = 0;

if (!baseURL) {
    throw new Error("A baseURL (e.g., 'https://pulumi.com') is required.");
}

if (!checkScope || !["site", "page"].includes(checkScope)) {
    throw new Error("A checkScope of either 'site' or 'page' is required.");
}

if (!maxRetries || Number.isNaN(maxRetries)) {
    maxRetries = 0;
}

// If the passed-in url is simply "local", assume that means we should start a server
// and to test a local build at the usual location. Otherwise, just test the URL.
if (baseURL === "local") {
    baseURL = "http://localhost:8888";

    const url = new URL(baseURL);
    const buildDir = "public";

    // Make sure there's a valid-looking build where one's supposed to be.
    if (!fs.existsSync(buildDir) || !fs.existsSync(`${path.join(buildDir, "index.html")}`)) {
        fail(new Error(`There's no build at ${buildDir}. You may need to run 'make build' first.`));
    }

    // Start a server, then run the checker.
    httpServer
        .createServer({
            root: buildDir,
        })
        .listen(url.port, url.hostname, () => {
            checkLinks();
        });

} else {

    // Just run the checker.
    checkLinks();
}

// Runs the checker.
function checkLinks() {
    const checker = getChecker(checkScope, []);
    checker.enqueue(baseURL);
}

// Returns an instance of either HtmlUrlChecker or SiteChecker.
function getChecker(scope, brokenLinks) {

    // For details about each of the options used below, see the BLC docs at
    // https://github.com/stevenvachon/broken-link-checker#options.
    const requestMethod = "GET";
    const filterLevel = 1;

    if (scope === "page") {
        const opts = {
            requestMethod,
            filterLevel,
            excludeInternalLinks: true,
            excludedKeywords: [
                ...getDefaultExcludedKeywords(),
                "https://www*"
            ]
        };

        // https://github.com/stevenvachon/broken-link-checker#htmlurlchecker
        return new HtmlUrlChecker(opts, getDefaultHandlers(brokenLinks));
    }

    if (scope === "site") {
        const opts = {
            requestMethod,
            filterLevel,
            excludedKeywords: getDefaultExcludedKeywords(),
        };

        // https://github.com/stevenvachon/broken-link-checker#sitechecker
        return new SiteChecker(opts, getDefaultHandlers(brokenLinks));
    }
}

// The set of event handlers common to HTMLUrlCheckers and SiteCheckers.
// https://github.com/stevenvachon/broken-link-checker#htmlurlchecker
// https://github.com/stevenvachon/broken-link-checker#sitechecker
function getDefaultHandlers(brokenLinks) {
    return {
        link: (result) => {
            try {
                onLink(result, brokenLinks);
            }
            catch (error) {
                fail(error);
            }
        },
        error: (error) => {
            fail(error);
        },
        page: (error, pageURL) => {
            try {
                onPage(error, pageURL, brokenLinks);
            }
            catch(error) {
                fail(error);
            }
        },
        end: async () => {
            try {
                await onComplete(brokenLinks);
            }
            catch (error) {
                fail(error);
            }
        },
    };
}

// Handles BLC 'link' events, adding broken links to the running list.
function onLink(result, brokenLinks) {
    const source = result.base.resolved;
    const destination = result.url.resolved;

    if (result.broken) {
        const reason = result.brokenReason;

        addLink(source, destination, reason, brokenLinks);

        // Always log broken links to the console.
        logLink(source, destination, reason);

    } else if (process.env.DEBUG) {

        // Log successes when DEBUG is truthy.
        logLink(source, destination, result.http.response.statusCode);
    }
}

// Handles BLC 'page' events. For page scope, we fail immediately, since that means the
// requested page was not found. Otherwise, we just log the failed URL to the running list
// of broken links.
function onPage(error, pageURL, brokenLinks) {
    if (error) {
        if (checkScope === "page") {
            throw new Error(`Failed to retrieve ${pageURL}: ${error.message}.`);
        }
        else {
            addLink(pageURL, pageURL, error.message, brokenLinks);
            logLink(pageURL, pageURL, error.message);
        }
    }
    else if (process.env.DEBUG) {
        logLink(pageURL, pageURL, "PAGE_OK");
    }
}

// Handles the BLC 'complete' event, which is raised at the end of a run.
async function onComplete(brokenLinks) {
    const filtered = excludeAcceptable(brokenLinks);

    if (filtered.length > 0) {

        // If we failed and a retry count was provided, retry. Note that retry count !==
        // run count, so a retry count of 1 means run once, then retry once, which means a
        // total run count of two.
        if (maxRetries > 0 && retryCount < maxRetries) {
            retryCount += 1;
            console.log(`Retrying (${retryCount} of ${maxRetries})...`);
            checkLinks();
            return;
        }

        const list = filtered
            .map(link => `• <${link.source}|${new URL(link.source).pathname}> → ${link.destination} (${link.reason})`)
            .join("\n");

        // Post the results to Slack.
        await postToSlack(
            "ops-notifications",
            `Eek! :scream_cat: There are broken links on ${new URL(baseURL).hostname}: \n\n ${list}`
        );

        throw new Error("Finished, but failed with errors. See the log for details.");
    }
}

/**
    We exclude some links:
    - Our generated API docs have lots of broken links.
    - Our available versions page includes links to private repos.
    - GitHub Edit Links may be broken, because the page might not yet exist!
    - Our LinkedIn page, for some reason, returns an HTTP error (despite being valid).
    - Our Visual Studio Marketplace link for the Azure Pipelines task extension,
      although valid and publicly available, is reported as a broken link.
    - A number of synthetic illustrative links come from our examples/tutorials.
    - GitLab 503s for requests for protected pages that don't contain certain cookies.
*/
function getDefaultExcludedKeywords() {
    return [
        "/docs/reference/pkg",
        "/docs/get-started/install/versions",
        "https://api.pulumi.com/",
        "https://github.com/pulls?",
        "https://github.com/pulumi/docs/edit/master",
        "https://github.com/pulumi/docs/issues/new",
        "https://www.linkedin.com/",
        "https://marketplace.visualstudio.com/items?itemName=pulumi.build-and-release-task",
        "https://blog.mapbox.com/",
        "https://www.youtube.com/",
        "https://apps.twitter.com/",
        "https://www.googleapis.com/",
        "https://us-central1-/",
        "https://www.mysql.com/",
        "https://ksonnet.io/",
        "https://www.latlong.net/",
        "https://www.packet.com/",
        "https://www.random.org",
        "https://mbrdna.com",
        "https://www.linode.com/",
        "https://www.hetzner.com/cloud",
        "https://media.amazonwebservices.com/architecturecenter/AWS_ac_ra_web_01.pdf",
        "https://kubernetes-charts-incubator.storage.googleapis.com",
        "https://kubernetes-charts.storage.googleapis.com",
        "http://web-lb-23139b7-1806442625.us-east-1.elb.amazonaws.com",
        "https://ruby-app-7a54c5f5e006d5cf33c2-zgms4nzdba-uc.a.run.app",
        "https://hello-a28eea2-q1wszdxb2b-ew.a.run.app",
        "https://ruby-420a973-q1wszdxb2b-ew.a.run.app",
        "https://280f2167f1.execute-api.us-east-1.amazonaws.com",
        "http://my-bucket-1234567.s3-website.us-west-2.amazonaws.com",
        "https://gitlab.com/users/sign_in",
        "https://gitlab.com/profile/applications",
        "https://blog.coinbase.com/",
    ];
}

// Filters out transient errors that needn't fail a link-check run.
function excludeAcceptable(links) {
    return (links

        // Ignore GitHub 429s (rate-limited). We should really be handling these more
        // intelligently, but we can come back to that in a follow up.
        .filter(b => !(b.reason === "HTTP_429" && b.destination.match(/github.com/)))

        // Ignore remote disconnects.
        .filter(b => b.reason !== "ERRNO_ECONNRESET")

        // Ignore complaints about MIME types. BLC currently hard-codes an expectation of
        // type text/html, which causes it to fail on direct links to images, PDFs, and
        // other media.
        // https://github.com/stevenvachon/broken-link-checker/issues/65
        // https://github.com/stevenvachon/broken-link-checker/blob/43770535ad7b84cadec9dc54c5140694389e33dc/lib/internal/streamHTML.js#L36-L39
        .filter(b => !b.reason.startsWith(`Expected type "text/html"`))
    );
}

// Posts a message to the designated Slack channel.
function postToSlack(channel, text) {
    const token = process.env.SLACK_ACCESS_TOKEN;

    if (!token) {
        console.warn("No SLACK_ACCESS_TOKEN on the environment. Skipping.");
        return;
    }

    const client = new WebClient(token, { logLevel: LogLevel.ERROR });
    return client.chat.postMessage({
        text,
        channel: `#${channel}`,
        as_user: true,
        mrkdwn: true,
        unfurl_links: false,
    });
}

// Adds a broken link to the running list.
function addLink(source, destination, reason, links) {
    links.push({
        source,
        destination,
        reason,
    });
}

// Logs a link result to the console.
function logLink(source, destination, reason) {
    console.log(source);
    console.log(`  -> ${destination}`);
    console.log(`  -> ${reason}`);
    console.log();
}

// Logs and exits immediately.
function fail(error) {
    console.error(error.message);
    process.exit(1);
}
