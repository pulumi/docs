import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

// [Step 1: Create an S3 bucket.]
const bucket = new aws.s3.Bucket("my-bucket");

// [Step 2: Create a Lambda function.]
// TO-DO

// [Step 3: Create an export.]
// TO-DO