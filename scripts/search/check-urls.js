const fs = require("fs");
const axios = require("axios").default;
const retry = require("axios-retry").default;

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

    // Retry failed requests up to three times with exponential backoff.
    retry(axios, {
        retries: 3,
        retryDelay: (retryCount) => {
            return retryCount * 1000;  // Exponential backoff: 1s, 2s, 3s
        },
        shouldResetTimeout: true,
        onRetry: (count, error, config) => {
            const errorInfo = error.code || error.response?.status || error.message || 'Unknown error';
            console.log(`    ↳ ${config.url} failed (${errorInfo}). Retry ${count}/3...`);
        },
    });

    for await (const chunk of chunks) {
        console.log(` ↳ Checking group ${chunk.chunk + 1} of ${chunks.length} (${chunk.objects.length} URLs)...`);

        // Add delay before each batch to avoid rate limiting (except first batch)
        if (chunk.chunk > 0) {
            const delayMs = 10000;  // 10 seconds between batches
            console.log(`   [Waiting ${delayMs/1000}s before next batch...]`);
            await new Promise(resolve => setTimeout(resolve, delayMs));
        }

        const result = await Promise.allSettled(chunk.objects.map(obj => {
            const url = obj.href.startsWith("http") ? obj.href : `${baseURL}${obj.href}`;

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
                    // Log full error details for diagnosis
                    const errorDetails = {
                        code: error.code,
                        message: error.message,
                        status: error.response?.status,
                        statusText: error.response?.statusText,
                    };
                    console.error(`    ✗ ${url} error details:`, JSON.stringify(errorDetails));

                    // Reject with meaningful error message
                    const errorMsg = error.code || error.response?.status || error.message || 'Unknown error';
                    reject(`${url} ERROR: ${errorMsg}`);
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
            console.error(`\n✗ ${summary.rejected.length} URLs failed:\n`);

            // Group errors by type for better visibility
            const errorTypes = {};
            summary.rejected.forEach(reason => {
                const match = reason.match(/ERROR: (.+)$/);
                const errorType = match ? match[1] : 'Unknown';
                errorTypes[errorType] = (errorTypes[errorType] || 0) + 1;
            });

            console.error('Error types:');
            Object.entries(errorTypes).forEach(([type, count]) => {
                console.error(`  - ${type}: ${count} URLs`);
            });

            throw new Error(`One or more URLs failed:\n\n${summary.rejected.join("\n")}\n`);
        }
    });

// Exit non-zero when something goes wrong in the promise chain.
process.on("unhandledRejection", error => {
    console.error('Unhandled rejection:', error);
    process.exit(1);
});
