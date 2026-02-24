const { HtmlUrlChecker } = require("broken-link-checker");
const { WebClient, LogLevel } = require('@slack/web-api');
const httpServer = require("http-server");
const Sitemapper = require("sitemapper").default;
const sitemap = new Sitemapper();
const path = require("path");
const fs = require("fs");

// Internal domain for separating internal vs external broken links
const INTERNAL_DOMAIN = "pulumi.com";

// Helper function to check if a URL is an internal Pulumi link
function isInternalLink(url) {
    try {
        const urlObj = new URL(url);
        return urlObj.hostname === INTERNAL_DOMAIN || urlObj.hostname.endsWith(`.${INTERNAL_DOMAIN}`);
    } catch {
        return false;
    }
}

// Additional routes to check that are not included in the sitemap.
const additionalRoutes = [
    "https://github.com/pulumi/pulumi",
    // Alternative version of the home page for Google ads.
    "https://www.pulumi.com/b/",
    "https://www.pulumi.com/registry/sitemap.xml",
]


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
    // Split broken links into internal and external
    const internalLinks = brokenLinks.filter(link => isInternalLink(link.destination));
    const externalLinks = brokenLinks.filter(link => !isInternalLink(link.destination));

    // Apply filters to each group
    const filteredInternal = excludeAcceptable(internalLinks);
    const filteredExternal = excludeAcceptable(externalLinks);

    const totalFiltered = filteredInternal.length + filteredExternal.length;

    if (totalFiltered > 0) {

        // If we failed and a retry count was provided, retry. Note that retry count !==
        // run count, so a retry count of 1 means run once, then retry once, which means a
        // total run count of two.
        if (maxRetries > 0 && retryCount < maxRetries) {
            retryCount += 1;
            console.log(`Retrying (${retryCount} of ${maxRetries})...`);
            checkLinks();
            return;
        }

        // Post internal broken links first (if any)
        if (filteredInternal.length > 0) {
            const internalList = filteredInternal
                .map(link => `:link: <${link.source}|${new URL(link.source).pathname}> → ${link.destination} (${link.reason})`)
                .join("\n");

            const internalMessage = `:pulumipus-jedi: *Internal Broken Links (${filteredInternal.length} found)*\nThese are links within pulumi.com that need attention:\n\n${internalList}`;

            console.warn("Posting internal broken links to Slack: " + internalList);
            await postToSlack("docs-ops", internalMessage);
        }

        // Post external broken links second (if any)
        if (filteredExternal.length > 0) {
            const externalList = filteredExternal
                .map(link => `:link: <${link.source}|${new URL(link.source).pathname}> → ${link.destination} (${link.reason})`)
                .join("\n");

            const externalMessage = `:pulumipus-sith: *External Broken Links (${filteredExternal.length} found)*\nThese are links to third-party sites (may be false positives due to bot protection):\n\n${externalList}`;

            console.warn("Posting external broken links to Slack: " + externalList);
            await postToSlack("docs-ops", externalMessage);
        }
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
        "https://support.pulumi.com/",
        "https://www.pulumi.com/support/",
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
        "https://thenewstack.io/",
        "https://rootly.com/",
        "https://www.vultr.com/",
        "https://my.vultr.com/",
        "https://my.vultr.com/settings/#settingsapi",
        "https://shell.azure.com/",
        "https://portal.azure.com/",
        "https://www.noaa.gov/information-technology/open-data-dissemination",
        "https://www.inc.com/inc5000/2023",
        "https://www.inc.com/inc5000",
        "https://www.weforum.org/press/2020/10/recession-and-automation-changes-our-future-of-work-but-there-are-jobs-coming-report-says-52c5162fce/",
        "https://www.reuters.com/technology/chatgpt-sets-record-fastest-growing-user-base-analyst-note-2023-02-01/",
        "https://www.reddit.com/r/pulumi/comments/130b4rn/ama_with_luke_hoban_cto_on_pulumi_insightsai_at/",
        "https://dash.cloudflare.com/sign-up/",
        "https://www.sdxcentral.com/articles/news/pulumi-wants-to-piece-together-aws-lego-blocks/2019/06/",
        "https://www.sdxcentral.com/articles/news/pulumi-code-dev-platform-adds-premium-team-tier-scores-15m-series-a/2018/10/",
        "https://www.gartner.com/en/newsroom/press-releases/2023-11-29-gartner-says-cloud-will-become-a-business-necessity-by-2028",
        "https://www.gartner.com/en/articles/what-is-platform-engineering",
        "https://venturebeat.com/data-infrastructure/pulumi-infrastructure-as-code-goes-universal-to-build-cloud-apps/",
        "https://www.digitalnewsasia.com/business/idc-reveals-its-top-predictions-cloud-2023-and-beyond",
        "https://www.gartner.com/smarterwithgartner/welcome-to-the-api-economy",
        "https://code.visualstudio.com/",
        "https://www.honeycomb.io/",
        "https://wiki.osdev.org/Atomic_operation",
        "https://conference.pulumi.com/",
        "https://wallaroo.ai/",
        "https://www.gartner.com/en/infrastructure-and-it-operations-leaders/topics/platform-engineering",
        "http://127.0.0.1:5000/",
        "https://platform.openai.com",
        "https://openai.com/",
        "https://github.com/marketplace",
        "https://bard.google.com/",
        "https://cloud.getdbt.com/api",
        "https://dutchie.com/",
        "https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028",
        "https://www.gartner.com/en/webinar/445864/1051166",
        "https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md*",
	    "https://x.com*",
        "https://stackoverflow.com/questions/tagged/pulumi",
        "https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix",
        "https://blog.postman.com/postman-now-supports-grpc/",
        "https://dzone.com/articles/survey-reveals-rapid-growth-in-kubernetes-usage-se",
        "https://networkengineering.stackexchange.com/a/18877",
        "https://stackoverflow.com/questions/46604721/azure-ad-delete-user-group-unauthorized",
        "https://stackoverflow.com/a/69270933",
        "https://old.reddit.com/r/devops/comments/1izpca1/platform_engineering_fad/",
        "https://www.deepseek.com/",
        "https://marketplace.visualstudio.com/",
        "https://pulumi.com/authors/",
        "https://pulumi.com/tags/",
        "https://pulumi.com/collections/",
        "https://securityboulevard.com/2024/09/pulumi-adds-cloud-security-intelligence-tool-to-portfolio/",
        "https://awsinsider.net/articles/2019/06/12/pulumi.aspx",
        "https://www.tivityhealth.com/",
        "https://blog.ekik.org*",
        "https://www.crn.com*",
        "https://www.downelink.com/a-deep-dive-into-openais-text-embedding-ada-002-unlocking-the-power-of-semantic-understanding/",
        "https://github.com/serverless/components",
        "https://docs.spot.io/spot-connect/integrations/pulumi",
        // News/Media sites with aggressive bot protection
        "https://devops.com/",
        "https://www.bizjournals.com/",
        "https://redmonk.com/",
        "https://www.eweek.com/",
        "https://www.axios.com/",
        "https://www.mordorintelligence.com/",
        "https://betterprogramming.pub/",
        "https://garymarcus.substack.com/",
        "https://www.coingecko.com/",
        "https://news.ycombinator.com/",
        "https://www.gao.gov/",
        "https://apps.dtic.mil/",
        "https://queue.acm.org/",
        // NPM (block all, not just 429s)
        "https://www.npmjs.com/",
        "https://npmjs.com/",
        // Developer tools/platforms with bot protection
        "https://dev.mysql.com/",
        "https://circleci.com/docs/",
        "https://docs.gitlab.com/",
        "https://gitlab.com/help/",
        // Conference/event sites
        "https://sched.com",
        "https://static.sched.com/",
        "colocatedevents",
        "kccnc",
        "wasmcon",
        "gitopscon",
        // Archive/rate-limited Pulumi properties
        "https://archive.pulumi.com/",
        // Sites with known connection issues
        "https://trivy.dev/",
        "https://elastisys.com/",
        "https://cloudnativedenmark.dk/",
        "https://stackconf.eu/",
        // HashiCorp maintains redirects when reorganizing docs - skip checking entirely
        "https://developer.hashicorp.com/",
        "https://www.hashicorp.com/",
        // Archived/deleted personal repositories referenced in historical blog posts
        "https://github.com/chrsmith/static-website-aws",
        "https://github.com/chrsmith/browserhack-demo",
        "https://github.com/chrsmith/pulumi-aws-travis-cicd-demo",
        "https://github.com/jasonsmithio/pulumi-experiments",
        // Old example repository paths that have been renamed or removed
        "https://github.com/pulumi/examples/tree/master/aws-js-webserver",
        "https://github.com/pulumi/examples/blob/master/aws-js-webserver/index.js",
        "https://github.com/pulumi/examples/tree/master/aws-js-s3-folder",
        "https://github.com/pulumi/examples/tree/master/aws-js-sqs-slack",
        "https://github.com/pulumi/examples/tree/master/aws-py-oidc-provider-pulumi-cloud",
        "https://github.com/pulumi/examples/tree/master/gcp-py-oidc-provider-pulumi-cloud",
        "https://github.com/pulumi/examples/tree/master/google-native-ts-k8s-ruby-on-rails-postgresql",
        "https://github.com/pulumi/examples/tree/master/google-native-ts-functions",
        "https://github.com/kubernetes/examples/tree/master/guestbook",
        // Old internal URLs with working S3 redirects (issue #17449)
        "https://www.pulumi.com/docs/cli/commands/pulumi_plugin_install",
        "https://www.pulumi.com/docs/cli/commands/pulumi_schema_check",
        "https://www.pulumi.com/docs/using-pulumi/crossguard/compliance-ready-policies/",
        // External links reported as broken in issue #17495
        "https://roadmap.sh/videos/scaling-the-unscalable",
        "https://redis.io/docs/ui/cli/",
        "https://telephoneworld.org/telephone-sounds/",
        "https://aidevtlv.com/agenda/",
        "https://cloud.google.com/deployment-manager/docs",
        "https://daninacan.com/",
        "https://www.tigera.io/blog/top-5-kubernetes-trends-for-2019/",
    ];
}

// Filters out transient errors that needn't fail a link-check run.
function excludeAcceptable(links) {
    // HTTP status codes to filter out for external sites (bot protection, auth walls, timeouts)
    const externalErrorReasons = ["HTTP_403", "HTTP_401", "HTTP_202", "HTTP_undefined"];

    return (links
        // Ignore GitHub and npm 429s (rate-limited). We should really be handling these more
        // intelligently, but we can come back to that in a follow up.
        .filter(b => !(b.reason === "HTTP_429" && b.destination.match(/github.com|npmjs.com|medium.com/)))

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

        // Ignore HTTP 502s (Bad Gateway - transient server errors).
        .filter(b => b.reason !== "HTTP_502")

        // Ignore HTTP 415s (Unsupported Media Type - often bot protection).
        .filter(b => b.reason !== "HTTP_415")

        // Ignore all HTTP 429s (rate limiting, bot protection).
        .filter(b => b.reason !== "HTTP_429")

        // Filter errors from external sites (bot protection, auth walls, connection issues)
        .filter(b => !(externalErrorReasons.includes(b.reason) && !isInternalLink(b.destination)))

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
                .filter(page => !page.match(/\/docs\/install\/versions\//))
                .filter(page => !page.match(/\/authors\//))
                .filter(page => !page.match(/\/collections\//))
                .filter(page => !page.match(/\/tags\//))
                .filter(page => !page.match(/\/crosswalk\//))

                // Always check using the supplied baseURL.
                .map(url => {
                    const newURL = new URL(url);
                    const baseURLObj = new URL(base);
                    newURL.hostname = baseURLObj.hostname;
                    newURL.protocol = baseURLObj.protocol;
                    return newURL.toString();
                })

                // Tack on any additional pages we'd like to check.
                .concat(additionalRoutes)

                // Sort everything alphabetically.
                .sort();

            // Return the list of URLs to be crawled.
            return urls;
        });
}

