import * as pulumi from "@pulumi/pulumi";
import * as random from "@pulumi/random";
import * as aws from "@pulumi/aws";

const petName = new random.RandomPet("my-pet-name");

const bucket = new aws.s3.Bucket("b");

const index = new aws.s3.BucketObject(
    "index.html",
    {
        bucket: bucket.bucket,
        content: "Thanks for using Pulumi!",
    },
    { parent: bucket },
);

const randomSite = new aws.s3.BucketObject(
    "random.html",
    {
        bucket: bucket.bucket,
        content: petName.id,
    },
    { parent: bucket },
);

export const PetName = petName.id;
