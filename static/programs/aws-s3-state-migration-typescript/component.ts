import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";
import { componentType, migrateBucketState } from "./migration";

export class VersionedBucket extends pulumi.ComponentResource {
    readonly bucketName: pulumi.Output<string>;
    readonly bucketId: pulumi.Output<string>;
    readonly bucketUrn: pulumi.Output<string>;

    constructor(name: string, bucketName: string, opts?: pulumi.ComponentResourceOptions) {
        super(componentType, name, {}, pulumi.mergeOptions(opts, {
            stateMigrations: [migrateBucketState],
        }));

        const bucket = new aws.s3.Bucket(name, {
            bucket: bucketName,
            forceDestroy: true,
            tags: {
                example: "s3-bucket-state-migration",
                "managed-by": "pulumi",
            },
            versioning: { enabled: true },
        }, { parent: this });

        this.bucketName = bucket.bucket;
        this.bucketId = bucket.id;
        this.bucketUrn = bucket.urn;
        this.registerOutputs({ bucketName: this.bucketName });
    }
}
