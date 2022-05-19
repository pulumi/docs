const Sitemapper = require("sitemapper");
const sitemap = new Sitemapper();

/**
* This script returns a list of URLs to check. It accepts two command-line arguments:

  * baseURL: The URL from which to fetch the sitemap (e.g., "https://www.pulumi.com"). Required.

  * from: The URL from which to start checking. Useful for debugging, it allows you to restart a
    failed run from a particular URL in the list. Optional.

  Usage:

  # Generate a complete list of all URLs to check, based on https://www.pulumi.com/sitemap.xml:
  $ node scripts/link-checker/get-pages-to-check.js "https://www.pulumi.com"

  # Generate the same complete list, but take only the URLs list after "https://www.pulumi.com/superpowers/":
  $ node scripts/link-checker/get-pages-to-check.js "https://www.pulumi.com" "https://www.pulumi.com/superpowers/"
*/

let [ baseURL, from ] = process.argv.slice(2);

// Start by fetching the sitemap from `baseURL`.
sitemap
    .fetch(`${baseURL}/sitemap.xml`)
    .then(map => {
        const urls = map.sites

            // Exclude resource docs, SDK docs, and CLI download pages.
            .filter(page => !page.match(/\/registry\/packages\/.+\/api-docs\//))
            .filter(page => !page.match(/\/docs\/reference\/pkg\/nodejs|python\//))
            .filter(page => !page.match(/\/docs\/get-started\/install\/versions\//))

            // Tack on any additional pages we'd like to check.
            .concat([
                "https://github.com/pulumi/pulumi",
                "https://slack.pulumi.com",
            ])

            // Sort everything alphabetically.
            .sort();

        // Find the position of the passed in "start from" URL, if any.
        const startIndex = Math.max(urls.indexOf(from), 0);

        // Output the list of URLs to be crawled.
        urls.slice(startIndex)
            .forEach(page => {
                console.log(page);
            });
    });
