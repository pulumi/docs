import * as aws from "@pulumi/aws";
import * as awssdk from "aws-sdk";
import * as awsx from "@pulumi/awsx";
import * as child_process from "child_process";
import * as fs from "fs";
import * as https from "https";
import * as path from "path";
import * as pulumi from "@pulumi/pulumi";
import * as tar from "tar";
import * as tmp from "tmp";
import * as uuid from "uuid/v1";

// TODO(joe): better region management -- since it can be overridden.
const region = aws.config.region;

export class BucketDirectory extends pulumi.ComponentResource {
    constructor(name: string, args: BucketDirectoryArgs, opts?: pulumi.ComponentResourceOptions) {
        super("awsx:s3:BucketDirectory", name, args, opts);

        // Upload the target directory a single object at a time. This allows us to minimize
        // copying over the Internet, and then to apply an efficient "S3 sync" from within the
        // Amazon data center, where bandwidth to the target S3 bucket will be maximized.
        const arch = tmp.fileSync({ postfix: ".tgz" }).name;
        // TODO(joe): this always shows up as a diff; is it because of timestamps?
        tar.c({ gzip: true, sync: true, file: arch, C: args.source }, fs.readdirSync(args.source));

        // TODO(joe): when archive can be an asset, we can just use this line, instead of manual tgzing:
        // const arch = new pulumi.asset.FileArchive(args.source);

        // Now create a single object in the target bucket to hold the resulting archive.
        const archive = new aws.s3.BucketObject(`${name}-archive`, {
            key: "__aws.s3.BucketDirectory.archive.tar.gz",
            bucket: args.bucket,
            source: new pulumi.asset.FileAsset(arch),
        }, { parent: this });

        // Create the dynamic resource that'll decompress and bulk-sync the contents.
        const syncer = new BucketDirectorySyncer(`${name}-syncer`, {
            archive,
            objectAcl: args.objectAcl,
        }, { parent: this });
    }
}

// TODO(joe): allow copying to a sub-directory in the bucket.
export interface BucketDirectoryArgs {
    /**
     * The S3 bucket to copy the contents of the directory to.
     */
    bucket: aws.s3.Bucket;
    /**
     * The relative directory to copy into the bucket.
     */
    source: string;
    /**
     * The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply.
     * Defaults to "private".
     */
    objectAcl?: string;
}

async function invokeSync(inputs: any, action: string): Promise<void> {
    try {
        const bucket = inputs["bucket"] as string;
        if (!bucket) {
            throw new Error("Missing bucket in BucketDirectory inputs");
        }
        const archiveKey = inputs["archiveKey"] as string;
        if (!archiveKey) {
            throw new Error("Missing archiveKey in BucketDirectory inputs");
        }
        const objectAcl = inputs["objectAcl"] as string;
        const syncFunc = inputs["syncFunc"] as string;
        if (!syncFunc) {
            throw new Error("Missing syncFunc ARN in BucketDirectory inputs");
        }

        // Run the copy function and then wait for it to finish.
        const lambda = new awssdk.Lambda({ region });
        console.log(`Invoking copy function: ${syncFunc}`);
        const resp = await lambda.invoke({
            FunctionName: syncFunc,
            Payload: JSON.stringify({
                Action: action,
                Bucket: bucket,
                ArchiveKey: archiveKey,
                ObjectAcl: objectAcl,
            }),
        }).promise();
        if (resp.FunctionError) {
            throw new Error(
                `Invoking copy function failed [${resp.FunctionError}]: ${resp.Payload ? resp.Payload.toString() : ""}`);
        }
        console.log(`Invocation complete.`);
    } catch (err) {
        // TODO[pulumi/pulumi#2721]: this can go away once diagnostics for dynamic providers is improved.
        console.log(err);
        throw err;
    }
}

class BucketDirectorySyncer extends pulumi.dynamic.Resource  {
    static provider = {
        create: async(inputs: any): Promise<pulumi.dynamic.CreateResult> => {
            await invokeSync(inputs, "Update");
            return { id: uuid() };
        },
        update: async(id: pulumi.ID, olds: any, news: any): Promise<pulumi.dynamic.UpdateResult> => {
            await invokeSync(news, "Update");
            return {};
        },
        delete: async(id: pulumi.ID, olds: any): Promise<void> => {
            await invokeSync(olds, "Delete");
        },
    };

    static createSyncFunc(name: string, bucket: pulumi.Output<string>, parent?: pulumi.Resource): pulumi.Output<string> {
        const syncFuncRole = new aws.iam.Role(`${name}-copyfunc-role`, {
            assumeRolePolicy: {
                Version: "2012-10-17",
                Statement: [{
                    Action: "sts:AssumeRole",
                    Principal: {
                        Service: "lambda.amazonaws.com"
                    },
                    Effect: "Allow",
                    Sid: "",
                }],
            },
        }, { parent });
        const syncFunc = new aws.lambda.Function(`${name}-copyfunc`, {
            timeout: 60*5,
            memorySize: 1024,
            runtime: "python3.7",
            code: new pulumi.asset.FileArchive("./lambda/bin"),
            handler: "index.handler",
            role: syncFuncRole.arn,
        }, { parent });

        // Allow Lambda to read/write from the S3 bucket.
        const bucketArn = pulumi.interpolate`arn:aws:s3:::${bucket}`;
        const syncFuncPolicy = new aws.iam.Policy(`${name}-copyfunc-policy`, {
            path: "/",
            policy: {
                Version: "2012-10-17",
                Statement: [
                    // Allow S3 Bucket operations.
                    {
                        Effect:"Allow",
                        Action: "s3:ListBucket",
                        Resource: bucketArn,
                    },
                    {
                        Effect: "Allow",
                        Action: [
                            "s3:PutObject",
                            "s3:PutObjectAcl",
                            "s3:GetObject",
                            "s3:GetObjectAcl",
                            "s3:DeleteObject"
                        ],
                        Resource: pulumi.interpolate`${bucketArn}/*`,
                    },
                    // Allow use of CloudWatch logs.
                    {
                        Action: "logs:*",
                        Resource: "arn:aws:logs:*:*:*",
                        Effect: "Allow",
                    },
                ],
            },
        }, { parent });
        const syncFuncPolicyAtt = new aws.iam.RolePolicyAttachment(`${name}-copyfunc-policy-att`, {
            role: syncFuncRole.name,
            policyArn: syncFuncPolicy.arn,
        }, { parent });

        // Return the ARN for the function, but also join with the policy attachment so consumers don't try
        // to use the function before the policy attachment has occurred (this can lead to permissions errors).
        return pulumi.all([ syncFunc.arn, syncFuncPolicyAtt.id ]).apply(([ arn, _ ]) => arn);
    }

    constructor(name: string, args: BucketDirectorySyncerArgs, opts?: pulumi.ResourceOptions) {
        // Create a Lambda function that will copy and extract files using "aws s3 sync".
        opts = opts || {};
        const syncFunc = BucketDirectorySyncer.createSyncFunc(name, args.archive.bucket, opts.parent);

        // Now initialize the dynamic resource provider, etc.
        const superArgs = {
            syncFunc,
            bucket: args.archive.bucket,
            archiveKey: args.archive.key,
            objectAcl: args.objectAcl,
        };
        super(BucketDirectorySyncer.provider, name, superArgs, opts);
    }
}

interface BucketDirectorySyncerArgs {
    /**
     * The archive to sync into the enclosing bucket.
     */
    archive: aws.s3.BucketObject;
    /**
     * The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply.
     * Defaults to "private".
     */
    objectAcl?: string;
}
