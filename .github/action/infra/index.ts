import * as aws from "@pulumi/aws";
import * as fs from "fs";
import * as mime from "mime";
import * as path from "path";
import * as pulumi from "@pulumi/pulumi";

// The content comes from a configurable location.
const contentRoot = new pulumi.Config().require("root");

// Create a bucket to store and serve the static content.
const contentBucket = new aws.s3.Bucket("content", {
    acl: "public-read",
    // Have S3 serve its contents as if it were a website. This is how we get the right behavior
    // for routes like "foo/", which S3 will automatically translate to "foo/index.html".
    website: {
        indexDocument: "index.html",
        errorDocument: "404.html",
    },
});

// crawlDirectory recursive crawls the provided directory, applying the provided function
// to every file it contains. Doesn't handle cycles from symlinks.
function crawlDirectory(dir: string, f: (_: string) => void) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const filePath = `${dir}/${file}`;
        const stat = fs.statSync(filePath);
        if (stat.isDirectory()) {
            crawlDirectory(filePath, f);
        }
        if (stat.isFile()) {
            f(filePath);
        }
    }
}

// Sync the contents of the source directory with the S3 bucket.
crawlDirectory(contentRoot, (filePath: string) => {
    const relativeFilePath = filePath.substring(contentRoot.length+1);
    new aws.s3.BucketObject(relativeFilePath, {
        acl: "public-read",
        key: relativeFilePath,
        bucket: contentBucket,
        source: new pulumi.asset.FileAsset(filePath),
        contentType: mime.getType(filePath) || undefined,
    }, { parent: contentBucket });
});

// Export the bucket's URL for easy access.
export const url = pulumi.interpolate`http://${contentBucket.websiteEndpoint}`;
