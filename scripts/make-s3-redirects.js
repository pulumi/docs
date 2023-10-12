const { PutObjectCommand, S3Client } = require("@aws-sdk/client-s3");
const fs = require("fs");

const bucket = process.argv[2];
const redirectsFile = process.argv[3] || "./public/redirects.txt";
const region = process.argv[4] || "us-west-2"

async function doRedirects(bucket, region) {
    const redirects = fs.readFileSync(redirectsFile, "utf-8").trim().split("\n");
    console.log(`Processing ${redirects.length} redirects...`);

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

                    const putCommand = new PutObjectCommand({
                        Bucket: bucket,
                        Key: key,
                        WebsiteRedirectLocation: location,
                        ACL: "public-read",
                        Body: "",
                        ContentLength: 0,
                    });

                    const putResponse = await client.send(putCommand);
                    const putStatus = putResponse.$metadata.httpStatusCode;

                    if (putStatus < 400) {
                        resolve(putStatus);

                        // The redirect succeeded, so we can delete the file.
                        fs.rmSync(`./public/${key}`, { force: true });

                    } else {
                        reject(putStatus);
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

doRedirects(bucket, region)
    .then(results => {

        const summary = {
            checked: results.length,
            fulfilled: results.filter(r => r.status === "fulfilled").map(r => r.value) || [],
            rejected: results.filter(r => r.status === "rejected").map(r => r.reason) || [],
        };

        console.log(" ↳ Done. ✨\n");

        if (summary.rejected.length > 0) {
            throw new Error(`One or more redirects failed: \n\n${summary.rejected.join("\n")}\n`);
        } else {
            console.log(` ↳ ${summary.fulfilled.length} redirects completed successfully.`);
        }
    });

// Exit non-zero when something goes wrong in the promise chain.
process.on("unhandledRejection", error => {
    throw new Error(error);
});
