// Copyright 2016-2019, Pulumi Corporation.  All rights reserved.

import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";
import * as pulumi from "@pulumi/pulumi";

import * as fs from "fs";
import * as path from "path";
import * as tar from "tar";
import * as tmp from "tmp";

const stackConfig = new pulumi.Config();
const config = {
    // pathToWebsiteContents is a relative path to the website's contents.
    pathToWebsiteContents: stackConfig.require("root"),
};

// websiteBucket stores the static content to be served via the CDN.
const websiteBucket = new aws.s3.Bucket(
    "website-bucket",
    {
        acl: "public-read",
        website: {
            indexDocument: "index.html",
            errorDocument: "404.html",
        },
    },
    {
        protect: false,
    },
);

// The website bucket needs to have the "public-read" ACL so its contents can be read by
// CloudFront and served. But we deny the s3:ListBucket permission to anyone but account
// users to prevent unintended disclosure of the bucket's contents.
const policy = new aws.s3.BucketPolicy("website-bucket-policy", {
    bucket: websiteBucket.bucket,
    policy: websiteBucket.arn.apply(arn => JSON.stringify({
        Version: "2008-10-17",
        Statement: [
            {
                Effect: "Deny",
                Principal: "*",
                Action: "s3:ListBucket",
                Resource: arn,
                Condition: {
                    StringNotEquals: {
                        "aws:PrincipalAccount": aws.getCallerIdentity().accountId,
                    },
                },
            },
        ],
    })),
});

// archiveBucket receives uploaded tarballs of website builds.
const archiveBucket = new aws.s3.Bucket("archive-bucket");

// archiveHandler processes those uploads.
const archiveHandler = new awsx.ecs.FargateTaskDefinition("archive-handler", {
    container: {
        image: awsx.ecs.Image.fromPath("archive-handler-image", "./"),
        memory: 4096,
        cpu: 4,
    },
});

// Handle uploads by running the archiveHandler task, which downloads the file, unpacks
// it, and synchronizes its contents with S3.
const cluster = awsx.ecs.Cluster.getDefault();
archiveBucket.onObjectCreated("archive-bucket-subscription", new aws.lambda.CallbackFunction<aws.s3.BucketEvent, void>("archive-bucket-callback", {
    runtime: "nodejs10.x",
    policies: awsx.ecs.TaskDefinition.defaultTaskRolePolicyARNs(),
    callback: async bucketArgs => {
        if (!bucketArgs.Records) {
            return;
        }

        for (const record of bucketArgs.Records) {
            console.log(`A file was uploaded to the ${archiveBucket.id.get()} bucket: ${record.s3.object.key}`);
            const source = `s3://${archiveBucket.id.get()}/${record.s3.object.key}`;
            const dest = `s3://${websiteBucket.id.get()}`;

            console.log(`Running the container task...`);
            await archiveHandler.run({
                cluster,
                overrides: {
                    containerOverrides: [
                        {
                            name: "container",

                            // Pass the S3 URL of the uploaded tarball and destination
                            // bucket to the container task.
                            command: [
                                source,
                                dest,
                            ],
                        },
                    ],
                },
            });
        }
    },
}));

// If the current run is an update (i.e., not a preview), zip up the contents of the
// website directory and upload the archive to S3.
if (!pulumi.runtime.isDryRun()) {
    archiveBucket.id.apply(bucketID => {

        // Wait for the update to complete before running the code to upload the archive,
        // to ensure the task that handles it is the one most recently deployed.
        process.on("beforeExit", async (code) => {
            if (code === 0 /* success */) {
                const s3 = new aws.sdk.S3();

                // Tar up the files in the `public` directory.
                const archivePath = tmp.fileSync({ postfix: ".tgz" }).name
                tar.c(
                    {
                        gzip: true,
                        sync: true,
                        file: archivePath,
                        C: config.pathToWebsiteContents,
                        portable: true,
                    },
                    fs.readdirSync(config.pathToWebsiteContents),
                );

                // Upload the archive.
                const result = await s3.putObject({
                    Bucket: bucketID,
                    Key: path.basename(archivePath),
                    Body: fs.readFileSync(archivePath),
                })
                .promise();

                console.log(`Website archive ${archivePath} was uploaded.`);

                // Properly exit.
                process.exit(code);
            }
        });
    });
}

export const url = websiteBucket.websiteEndpoint;
