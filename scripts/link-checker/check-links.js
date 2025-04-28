const { HtmlUrlChecker } = require("broken-link-checker");
const { WebClient, LogLevel } = require('@slack/web-api');
const Sitemapper = require("sitemapper");
const sitemap = new Sitemapper();
const path = require("path");
const fs = require("fs");
const axios = require("axios");

// Additional routes to check that are not included in the sitemap.
const additionalRoutes = [
    "https://github.com/pulumi/pulumi",
    // Alternative version of the home page for Google ads.
    "https://www.pulumi.com/b/",
    "https://www.pulumi.com/registry/sitemap.xml",
]

/**
 *  This script uses the programmatic API of https://github.com/stevenvachon/broken-link-checker
 *  to check the links (including images, iframes, and client-side redirects) for either an individual page
 *  or for a whole site. Usage:
 *
 *  # Standard check (default: no section filter)
 *  $ node scripts/link-checker/check-links.js "https://www.pulumi.com" 2
 *  
 *  # Check specific section (e.g., only check /docs/ URLs)
 *  $ node scripts/link-checker/check-links.js "https://www.pulumi.com" 2 "/docs/"
 *
 *  # Log successes as well as failures
 *  $ DEBUG=1 node scripts/link-checker/check-links.js "https://www.pulumi.com" 2
 */

let [ baseURL, maxRetries, sectionFilter ] = process.argv.slice(2);
let retryCount = 0;
let totalCheckedLinks = 0;
let startTime = Date.now();

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
    const brokenLinks = [];
    const checker = getChecker(brokenLinks);

    console.log("=== Link Checker Started ===");
    console.log(`Base URL: ${baseURL}`);
    if (sectionFilter) {
        console.log(`Section filter: ${sectionFilter}`);
    }
    console.log(`Max retries: ${maxRetries}`);
    
    try {
        // Get all URLs from the main sitemap AND section sitemaps
        console.log("Fetching URLs from sitemaps...");
        const urls = await getAllUrlsToCheck(baseURL);
        
        console.log(`Found ${urls.length} URLs to check`);
        
        // Start the checker with the base URL and all URLs
        checker.enqueue(baseURL);
        urls.forEach(url => checker.enqueue(url));
    } catch (error) {
        console.error(`Error fetching URLs: ${error.message}`);
        process.exit(1);
    }
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
                totalCheckedLinks++;
                
                // Show progress periodically
                if (totalCheckedLinks % 500 === 0) {
                    const elapsedMinutes = ((Date.now() - startTime) / 1000 / 60).toFixed(1);
                    console.log(`Progress: Checked ${totalCheckedLinks} links in ${elapsedMinutes} minutes, found ${brokenLinks.length} broken links`);
                }
                
                onLink(result, brokenLinks);
            }
            catch (error) {
                console.error(`Error in link handler: ${error.message}`);
            }
        },
        error: (error) => {
            console.error(`Checker error: ${error.message}`);
        },
        page: (error, pageURL) => {
            try {
                onPage(error, pageURL, brokenLinks);
            }
            catch(error) {
                console.error(`Error in page handler: ${error.message}`);
            }
        },
        end: async () => {
            try {
                await onComplete(brokenLinks);
            }
            catch (error) {
                console.error(`Error in end handler: ${error.message}`);
                process.exit(1);
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
        logLink(source, destination, result.http?.response?.statusCode || "SUCCESS");
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
    const elapsedTime = ((Date.now() - startTime) / 1000).toFixed(1);

    console.log("=== Link Check Completed ===");
    console.log(`Total time: ${elapsedTime} seconds`);
    console.log(`Total links checked: ${totalCheckedLinks}`);
    console.log(`Total broken links found: ${filtered.length}`);

    if (filtered.length > 0) {
        // If we failed and a retry count was provided, retry. Note that retry count !==
        // run count, so a retry count of 1 means run once, then retry once, which means a
        // total run count of two.
        if (maxRetries > 0 && retryCount < maxRetries) {
            retryCount += 1;
            console.log(`Retrying (${retryCount} of ${maxRetries})...`);
            
            // Reset counters
            totalCheckedLinks = 0;
            startTime = Date.now();
            
            checkLinks();
            return;
        }

        // Group broken links by reason
        const groupedByReason = {};
        filtered.forEach(link => {
            if (!groupedByReason[link.reason]) {
                groupedByReason[link.reason] = [];
            }
            groupedByReason[link.reason].push(link);
        });

        // Display summary by reason
        console.log(`Broken links by reason:`);
        Object.keys(groupedByReason).forEach(reason => {
            console.log(`${reason}: ${groupedByReason[reason].length} links`);
        });

        // List all broken links
        console.log("\nList of all broken links:");
        filtered.forEach(link => {
            console.log(`${link.source} -> ${link.destination} (${link.reason})`);
        });

        // Format for Slack
        const list = filtered
            .map(link => `:link: <${link.source}|${new URL(link.source).pathname}> → ${link.destination} (${link.reason})`)
            .join("\n");

        // Post the results to Slack.
        console.log(`Posting ${filtered.length} broken links to Slack...`);
        await postToSlack("docs-ops", `Found ${filtered.length} broken links:\n${list}`);
        
        // Exit with error code
        process.exit(1);
    } else {
        console.log(`All links are valid!`);
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
        "https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md*"
    ];
}

// Filters out transient errors that needn't fail a link-check run.
function excludeAcceptable(links) {
    return (links
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

    try {
        const client = new WebClient(token, { logLevel: LogLevel.ERROR });
        return await client.chat.postMessage({
            text,
            channel: `#${channel}`,
            as_user: true,
            mrkdwn: true,
            unfurl_links: false,
        });
    } catch (error) {
        console.error(`Error posting to Slack: ${error.message}`);
    }
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
    if (reason && (reason.toString().startsWith('4') || reason.toString().startsWith('5') || 
              typeof reason === 'string' && !reason.match(/^2\d\d$/))) {
        console.log(`BROKEN: ${source} -> ${destination} (${reason})`);
    } else if (process.env.DEBUG) {
        console.log(`OK: ${source} -> ${destination} (${reason})`);
    }
}

// Get all URLs to check from multiple sitemaps
async function getAllUrlsToCheck(base) {
    try {
        // Set of URLs to check to avoid duplicates
        const allUrls = new Set();
        
        // Add the known section sitemaps for Pulumi docs site
        const sitemaps = [
            // Main sitemap
            `${base}/sitemap.xml`,
            
            // Section sitemaps (based on examining the repo)
            `${base}/static/sitemaps/sitemap-blog.xml`,
            `${base}/static/sitemaps/sitemap-docs.xml`,
            `${base}/static/sitemaps/sitemap-tutorials.xml`,
            `${base}/static/sitemaps/sitemap-templates.xml`,
            `${base}/static/sitemaps/sitemap-registry.xml`,
            `${base}/static/sitemaps/sitemap-case-studies.xml`,
            `${base}/static/sitemaps/sitemap-product.xml`,
            `${base}/static/sitemaps/sitemap-compliance.xml`,
            `${base}/static/sitemaps/sitemap-what-is.xml`,
            `${base}/static/sitemaps/sitemap-other.xml`,
        ];
        
        // Try each sitemap
        for (const sitemapUrl of sitemaps) {
            try {
                console.log(`Processing sitemap: ${sitemapUrl}`);
                const urls = await processSitemap(sitemapUrl, base);
                
                // Add to our set
                urls.forEach(url => allUrls.add(url));
                
                console.log(`Found ${urls.length} URLs in ${sitemapUrl}`);
            } catch (error) {
                console.log(`Could not process ${sitemapUrl}: ${error.message}`);
            }
        }
        
        // Convert to array
        let urls = [...allUrls];
        
        // Apply section filter if provided
        if (sectionFilter) {
            urls = urls.filter(url => url.includes(sectionFilter));
            console.log(`Applied section filter "${sectionFilter}": ${urls.length} URLs remaining`);
        }
        
        // Add the additional routes
        urls = urls.concat(additionalRoutes);
        
        return urls;
    } catch (error) {
        console.error(`Error processing sitemaps: ${error.message}`);
        throw error;
    }
}

// Process a single sitemap
async function processSitemap(sitemapUrl, base) {
    try {
        const result = await sitemap.fetch(sitemapUrl);
        
        if (!result || !result.sites || !Array.isArray(result.sites)) {
            return [];
        }
        
        const urls = result.sites;
        
        // Exclude resource docs, SDK docs, and CLI download pages.
        const filtered = urls
            .filter(page => !page.match(/\/registry\/packages\/.+\/api-docs\//)) 
            .filter(page => !page.match(/\/docs\/reference\/pkg\/nodejs|python\//)) 
            .filter(page => !page.match(/\/docs\/install\/versions\//)); 
        
        // Always check using the supplied baseURL.
        return filtered.map(url => {
            try {
                const newURL = new URL(url);
                const baseURLObj = new URL(base);
                newURL.hostname = baseURLObj.hostname;
                newURL.protocol = baseURLObj.protocol;
                return newURL.toString();
            } catch (e) {
                console.warn(`Skipping invalid URL: ${url}`);
                return null;
            }
        }).filter(url => url !== null);
    } catch (error) {
        console.error(`Error fetching sitemap ${sitemapUrl}: ${error.message}`);
        return [];
    }
}