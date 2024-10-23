const pulumi = require("@pulumi/pulumi");
const random = require("@pulumi/random");
const aws = require("@pulumi/aws");

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

exports.PetName = petName.id;
