import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

export interface StaticPageArgs {
    indexContent: pulumi.Input<string>;
}

export class StaticPage extends pulumi.ComponentResource {
    public readonly endpoint: pulumi.Output<string>;

    constructor(name: string, args: StaticPageArgs, opts?: pulumi.ComponentResourceOptions) {
        super("sample-components:index:StaticPage", name, args, opts);

        const bucket = new aws.s3.Bucket(`${name}-bucket`, {}, { parent: this });

        const bucketWebsite = new aws.s3.BucketWebsiteConfiguration(
            `${name}-website`,
            {
                bucket: bucket.bucket,
                indexDocument: { suffix: "index.html" },
            },
            {
                parent: this,
            },
        );

        new aws.s3.BucketObject(
            `${name}-index-object`,
            {
                bucket: bucket.bucket,
                key: "index.html",
                content: args.indexContent,
                contentType: "text/html",
            },
            {
                parent: this,
            },
        );

        const publicAccessBlock = new aws.s3.BucketPublicAccessBlock(
            `${name}-public-access-block`,
            {
                bucket: bucket.id,
                blockPublicAcls: false,
            },
            {
                parent: this,
            },
        );

        new aws.s3.BucketPolicy(
            `${name}-bucket-policy`,
            {
                bucket: bucket.id,
                policy: bucket.bucket.apply(this.allowGetObjectPolicy),
            },
            {
                parent: this,
                dependsOn: publicAccessBlock,
            },
        );

        this.endpoint = bucketWebsite.websiteEndpoint;

        this.registerOutputs({
            endpoint: bucketWebsite.websiteEndpoint,
        });
    }

    allowGetObjectPolicy(bucketName: string) {
        return JSON.stringify({
            Version: "2012-10-17",
            Statement: [
                {
                    Effect: "Allow",
                    Principal: "*",
                    Action: ["s3:GetObject"],
                    Resource: [`arn:aws:s3:::${bucketName}/*`],
                },
            ],
        });
    }
}
