import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as cloudfront from "@aws-sdk/client-cloudfront";
import * as childProcess from "child_process";
import * as fs from "fs";

const config = new pulumi.Config("aws");
const region = config.require("region");

// Build the website.
const result = childProcess.execSync("hugo --destination ./public", { stdio: "pipe", cwd: "./www" });

// Log the build output to the console.
console.log(result.toString());

// Provision a storage bucket for the website.
const bucket = new aws.s3.Bucket("bucket", {
    website: {
        indexDocument: "index.html",
    },
});

// Apply some ownership controls and public-access privileges.
const ownershipControls = new aws.s3.BucketOwnershipControls("ownership-controls", {
    bucket: bucket.id,
    rule: {
        objectOwnership: "ObjectWriter",
    },
});

const publicAccess = new aws.s3.BucketPublicAccessBlock("public-access-block", {
    bucket: bucket.id,
    blockPublicAcls: false,
});

// Copy the website home page into the bucket.
const homepage = new aws.s3.BucketObject(
    "index.html",
    {
        bucket: bucket.id,
        content: fs.readFileSync("./www/public/index.html", "utf-8"),
        contentType: "text/html",
        acl: "public-read",
    },
    { dependsOn: [ownershipControls, publicAccess] },
);

// Fetch some redirects from a hypothetical CMS.
const redirects = fetch(`${process.env.CMS_ENDPOINT}/redirects.json`)
    .then(response => response.json())
    .then(items =>
        items.forEach((redirect: any, i: number) => {
            // Create an S3 website redirect for each one.
            new aws.s3.BucketObject(
                `redirect-${i}`,
                {
                    bucket: bucket.id,
                    key: redirect.from,
                    websiteRedirect: redirect.to,
                    acl: "public-read",
                },
                { dependsOn: [ownershipControls, publicAccess] },
            );
        }),
    );

// Create a CloudFront distribution for the website.
const cdn = new aws.cloudfront.Distribution("cdn", {
    enabled: true,
    defaultRootObject: "index.html",
    origins: [
        {
            originId: bucket.arn,
            domainName: bucket.websiteEndpoint,
            customOriginConfig: {
                originProtocolPolicy: "http-only",
                httpPort: 80,
                httpsPort: 443,
                originSslProtocols: ["TLSv1.2"],
            },
        },
    ],
    defaultCacheBehavior: {
        targetOriginId: bucket.arn,
        viewerProtocolPolicy: "redirect-to-https",
        allowedMethods: ["GET", "HEAD", "OPTIONS"],
        cachedMethods: ["GET", "HEAD", "OPTIONS"],
        forwardedValues: {
            queryString: true,
            cookies: {
                forward: "all",
            },
        },
    },
    restrictions: {
        geoRestriction: {
            restrictionType: "none",
        },
    },
    viewerCertificate: {
        cloudfrontDefaultCertificate: true,
    },
});

function createInvalidation(id: string) {
    // Only invalidate after a deployment.
    if (pulumi.runtime.isDryRun()) {
        console.log("This is a Pulumi preview, so skipping cache invalidation.");
        return;
    }

    process.on("beforeExit", () => {
        const client = new cloudfront.CloudFrontClient({ region });
        const command = new cloudfront.CreateInvalidationCommand({
            DistributionId: id,
            InvalidationBatch: {
                CallerReference: `invalidation-${Date.now()}`,
                Paths: {
                    Quantity: 1,
                    Items: ["/*"],
                },
            },
        });

        client
            .send(command)
            .then(result => {
                console.log(`Invalidation status for ${id}: ${result.Invalidation?.Status}.`);
                process.exit(0);
            })
            .catch(error => {
                console.error(error);
                process.exit(1);
            });
    });
}

// Register a function to be invoked before the program exits.
cdn.id.apply(id => createInvalidation(id));

// Export the URL of the CDN.
export const cdnURL = pulumi.interpolate`https://${cdn.domainName}`;
