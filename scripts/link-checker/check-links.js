const { HtmlUrlChecker } = require("broken-link-checker");
const { WebClient, LogLevel } = require('@slack/web-api');
const httpServer = require("http-server");
const Sitemapper = require("sitemapper");
const sitemap = new Sitemapper();
const path = require("path");
const fs = require("fs");

/**
 *  This script uses the programmatic API of https://github.com/stevenvachon/broken-link-checker
    to check the links (including images, iframes, and client-side redirects) for either an individual page
    or for a whole site. Usage:

    # Log successes as well as failures.
    $ DEBUG=1 node scripts/check-links.js "https://www.pulumi.com"
 */

let [ baseURL, maxRetries ] = process.argv.slice(2);
let retryCount = 0;

if (!baseURL) {
    throw new Error("A baseURL (e.g., 'https://pulumi.com') is required.");
}

if (!maxRetries || Number.isNaN(maxRetries)) {
    maxRetries = 0;
}

// Globally patch bhttp, broken-link-checker's HTTP library. We do with sadness because
// BLC doesn't expose an API for setting custom HTTP headers, and many services reject
// HTTP requests that lack certain headers (like Accept) or other characteristics.
const bhttp = require("bhttp");
const oldRequest = bhttp.request;
bhttp.request = function() {
    const [ url, options, callback ] = arguments;

    // Modify request options.
    // https://git.cryto.net/joepie91/node-bhttp/src/branch/master/lib/bhttp.js#L886
    options.headers.accept = "*/*";

    // Some CDNs reject requests that don't provide an acceptable accept-encoding header.
    // The checker's underlying HTTP library seems to support deflate compression best, so
    // we use that for all requests.
    options.headers["accept-encoding"] = "deflate";

    return oldRequest.apply(this, arguments);
};

// Run.
checkLinks();

// Runs the checker.
async function checkLinks() {
    const checker = getChecker([]);

    // Load all URLs.
    const urls = await getURLsToCheck(baseURL);

    // Start the checker.
    checker.enqueue(baseURL);
    urls.forEach(url => checker.enqueue(url));
}

// Returns an instance of either HtmlUrlChecker.
// https://github.com/stevenvachon/broken-link-checker#htmlurlchecker
function getChecker(brokenLinks) {

    // Specify an alternative user agent, as BLC's default doesn't pass some services' validations.
    const userAgent = "pulumi+blc/0.1";

    // For details about each of the options used below, see the BLC docs at
    // https://github.com/stevenvachon/broken-link-checker#options.
    const opts = {
        requestMethod: "GET",
        filterLevel: 1,
        userAgent,
        excludeInternalLinks: false,
        excludeExternalLinks: false,
        excludeLinksToSamePage: true,
        excludedKeywords: [
            ...getDefaultExcludedKeywords(),
        ]
    };

    return new HtmlUrlChecker(opts, getDefaultHandlers(brokenLinks));
}

// Returns the set of event handlers for HTMLUrlCheckers.
// https://github.com/stevenvachon/broken-link-checker#htmlurlchecker
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

// Handles BLC 'page' events.
function onPage(error, pageURL, brokenLinks) {
    if (error) {
        addLink(pageURL, pageURL, error.message, brokenLinks);
        logLink(pageURL, pageURL, error.message);
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
            .map(link => `:link: <${link.source}|${new URL(link.source).pathname}> → ${link.destination} (${link.reason})`)
            .join("\n");

        // Post the results to Slack.
        await postToSlack("docs-ops", list);

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
        "example.com",
        "/docs/reference/pkg",
        "/registry/packages/*/api-docs",
        "/logos/pkg",
        "/docs/get-started/install/versions",
        "https://api.pulumi.com/",
        "https://github.com/pulls?",
        "https://github.com/pulumi/docs/edit/master",
        "https://github.com/pulumi/docs/issues/new",
        "https://github.com/pulumi/registry/edit/master",
        "https://github.com/pulumi/registry/issues/new",
        "https://github.com/pulumi/pulumi-hugo/edit/master",
        "https://github.com/pulumi/pulumi-hugo/issues/new",
        "https://www.linkedin.com/",
        "https://linkedin.com/",
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
        "https://www.netfilter.org/",
        "https://codepen.io",
        "https://twitter.com",
        "https://t.co",
        "https://www.akamai.com",
        "http://localhost:16686/search", // Local Jaeger endpoint presented in troubleshooting guide.
        "https://ceph.io",
        "https://www.pagerduty.com",
        "https://support.pulumi.com",
        "https://pbs.twimg.com/profile_images/",
        "https://linen.dev/",
        "https://cloud.yandex.com/",
        "http://localhost:3000",
        "https://data-flair.training",
        "https://opensource.org/licenses",
        "https://console.eventstore.cloud/authentication-tokens",
        "https://telecomreseller.com/2019/03/20/crossing-cloud-chasms-avoiding-catastrophic-cloud-calamities",
        "https://www.enterprisetech.com/2018/10/23/startup-pulumi-rolls-cloud-native-tools",
        "http://optout.networkadvertising.org/?c=1",
    ];
}

// Filters out transient errors that needn't fail a link-check run.
function excludeAcceptable(links) {
    return (links
        // Ignore 403's
        .filter(b => b.reason !== "HTTP_403")

        // Ignore GitHub and npm 429s (rate-limited). We should really be handling these more
        // intelligently, but we can come back to that in a follow up.
        .filter(b => !(b.reason === "HTTP_429" && b.destination.match(/github.com|npmjs.com/)))

        // Ignore remote disconnects.
        .filter(b => b.reason !== "ERRNO_ECONNRESET")
        
        // Ignore BLC_UNKNOWN's
        .filter(b => b.reason !== "BLC_UNKNOWN")
            
        // Ignore BLC_INVALID's
        .filter(b => b.reason !== "BLC_INVALID")

        // Ignore HTTP 308s.
        .filter(b => b.reason !== "HTTP_308")
            
        // Ignore HTTP 503s.
        .filter(b => b.reason !== "HTTP_503")

        // Ignore complaints about MIME types. BLC currently hard-codes an expectation of
        // type text/html, which causes it to fail on direct links to images, PDFs, and
        // other media.
        // https://github.com/stevenvachon/broken-link-checker/issues/65
        // https://github.com/stevenvachon/broken-link-checker/blob/43770535ad7b84cadec9dc54c5140694389e33dc/lib/internal/streamHTML.js#L36-L39
        .filter(b => !b.reason.startsWith(`Expected type "text/html"`))
    );
}

// Posts a message to the designated Slack channel.
async function postToSlack(channel, text) {
    const token = process.env.SLACK_ACCESS_TOKEN;

    if (!token) {
        console.warn("No SLACK_ACCESS_TOKEN on the environment. Skipping.");
        return;
    }

    const client = new WebClient(token, { logLevel: LogLevel.ERROR });
    return await client.chat.postMessage({
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

// Start by fetching the sitemap from `baseURL`.
async function getURLsToCheck(base) {
    return await sitemap
        .fetch(`${base}/sitemap.xml`)
        .then(map => {
            const urls = map.sites

                // Exclude resource docs, SDK docs, and CLI download pages.
                .filter(page => !page.match(/\/registry\/packages\/.+\/api-docs\//))
                .filter(page => !page.match(/\/docs\/reference\/pkg\/nodejs|python\//))
                .filter(page => !page.match(/\/docs\/get-started\/install\/versions\//))

                // Always check using the supplied baseURL.
                .map(url => {
                    const newURL = new URL(url);
                    const baseURLObj = new URL(base);
                    newURL.hostname = baseURLObj.hostname;
                    newURL.protocol = baseURLObj.protocol;
                    return newURL.toString();
                })

                // Tack on any additional pages we'd like to check.
                .concat([
                    "https://github.com/pulumi/pulumi",
                ])

                // Sort everything alphabetically.
                .sort();

            // Return the list of URLs to be crawled.
            return urls;
        });
}
