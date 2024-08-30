const pulumi = require("@pulumi/pulumi");
const random = require("@pulumi/random");
const aws = require("@pulumi/aws");

// Create a random pet name
const petName = new random.RandomPet("my-pet-name");

// Create an S3 bucket
const bucket = new aws.s3.Bucket("b");

// Create an S3 BucketObject for index.html
const index = new aws.s3.BucketObject(
    "index.html",
    {
        bucket: bucket.bucket,
        content: "Thanks for using Pulumi!",
    },
    { parent: bucket },
);

// Create an S3 BucketObject for random.html with the random pet name as content
const randomSite = new aws.s3.BucketObject(
    "random.html",
    {
        bucket: bucket.bucket,
        content: petName.id,
    },
    { parent: bucket },
);

// Export the pet name
exports.PetName = petName.id;
