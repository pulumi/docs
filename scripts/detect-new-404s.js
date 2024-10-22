const Sitemapper = require("sitemapper");
const sitemap = new Sitemapper();
const fs = require("fs");

let [ baseURL, testURL, prefix ] = process.argv.slice(2);

if (!baseURL) {
    throw new Error("A baseURL (e.g., 'https://pulumi.com') is required.");
}

if (!testURL) {
    throw new Error("A testURL (e.g., 'http://localhost:1313') is required.");
}

async function checkURLs() {
    const urls = await getURLsToCheck(baseURL);
    const badURLs = [];

    const batchSize = 50;
    console.log(`Checking ${urls.length} URLs...`);

    for (let i = 0; i < urls.length; i += batchSize) {
        const batch = urls.slice(i, i + batchSize);
        const requests = batch.map(async (url) => {
            const newURL = url.replace(baseURL, testURL);
            let response;
            let attempts = 0;
            const maxAttempts = 2;

            while (attempts <= maxAttempts) {
                response = await fetch(newURL, { method: "HEAD" });
                if (response.status === 200) break;
                attempts++;
            }

            if (response.status !== 200) {
                badURLs.push(`${newURL} : ${response.status}`);
            }
        });

        await Promise.all(requests);
    }

    return badURLs;
}

async function getURLsToCheck(base) {
    return await sitemap
        .fetch(`${base}/sitemap.xml`)
        .then(map => {
            return map.sites
                .filter(page => !prefix || page.match(prefix))
                .map(page => new URL(new URL(page).pathname, base).toString())
                .sort();
        });
}

checkURLs().then(results => {
    if (results.length >0 ) {
        console.error(`\n${results.length} new 404s were detected:\n`)
        results.forEach(item => console.error(item.replace(testURL, "")));
        console.error(`\nThese are pages that exist on pulumi.com but do not exist at ${testURL}.\n`)
        console.error("Please make sure any content that's been moved has been an appropriate alias or redirect in place.");
        process.exit(1);
    } else {
        console.log("Everything looks good! ✅");
        process.exit(0);
    }
});
