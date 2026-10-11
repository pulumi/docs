import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

// Create a Cloud Storage bucket using the GCP Classic provider.
const bucket = new gcp.storage.Bucket("my-bucket", {
    location: "US",
    uniformBucketLevelAccess: true,
    forceDestroy: true,
});

// Create a Cloud Run service.
const service = new gcp.cloudrunv2.Service("my-service", {
    location: "us-central1",
    deletionProtection: false,
    template: {
        containers: [{
            image: "us-docker.pkg.dev/cloudrun/container/hello",
        }],
    },
});

export const bucketName = bucket.name;
export const serviceUrl = service.uri;
