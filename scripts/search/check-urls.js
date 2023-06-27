const fs = require("fs");
const axios = require("axios").default;
const retry = require("axios-retry");

async function checkSearchURLs(baseURL) {

    // We operate on the result of a call to the Algolia CLI to fetch the full index, which is
    // returned as a newline-delimited list of JSON strings. So we join turn that list into a
    // JavaScript array to make it easier to work with.
    const objects = fs.readFileSync("./public/search-index.json", "utf-8").split("\n").filter(o => !!o).map(s => JSON.parse(s));
    console.log(`Checking ${objects.length} search URLs...`);

    // Since we end up checking tens of thousands of URLs here, we chunk them up into groups
    // of a thousand to process them more efficiently.
    const chunkSize = 1000;
    const chunks = [];
    const results = [];

    for (let i = 0; i < objects.length; i += chunkSize) {
        chunks.push({ chunk: i / chunkSize, objects: objects.slice(i, i + chunkSize) });
    }

    // Retry failed requests up to three times.
    retry(axios, {
        retries: 3,
        shouldResetTimeout: true,
        onRetry: (count, error, config) => console.log(`    ↳ ${config.url} failed (${error.message}). Retrying...`),
    });

    for await (const chunk of chunks) {
        console.log(` ↳ Checking group ${chunk.chunk + 1} of ${chunks.length} (${chunk.objects.length} URLs)...`);

        const result = await Promise.allSettled(chunk.objects.map(obj => {
            const url = `${baseURL}${obj.href}`;

            return new Promise(async (resolve, reject) => {
                try {
                    // Make a HEAD request for the URL.
                    const res = await axios.head(url, { timeout: 60000 });
                    const status = `${url} ${res.status}`;

                    // Anything less than 400 is considered OK.
                    if (res.status < 400) {
                        resolve(status);
                    } else {
                        reject(status);
                    }
                }
                catch (error) {
                    reject(`${url} ERROR: ${error}`);
                }
            });
        }));

        results.push(...result);
    }

    return results;
}

checkSearchURLs(process.argv[2] || "https://www.pulumi.com")
    .then(results => {

        const summary = {
            checked: results.length,
            fulfilled: results.filter(r => r.status === "fulfilled").map(r => r.value) || [],
            rejected: results.filter(r => r.status === "rejected").map(r => r.reason) || [],
        };

        fs.writeFileSync(`./public/search-check-results.json`, JSON.stringify(summary, null, 4));
        console.log(" ↳ Done. ✨\n");

        if (summary.rejected.length > 0) {
            throw new Error(`One or more URLs failed: \n\n${summary.rejected.join("\n")}\n`);
        }
    });

// Exit non-zero when something goes wrong in the promise chain.
process.on("unhandledRejection", error => {
    throw new Error(error);
});
