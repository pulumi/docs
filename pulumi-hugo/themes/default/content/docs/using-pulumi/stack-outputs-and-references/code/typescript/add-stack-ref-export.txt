import * as pulumi from "@pulumi/pulumi";

const stackRef = new pulumi.StackReference("my-org/my-first-program/dev");

// Add an export to output the value of the Lambda function name using the stack reference above
export const firstProgramLambdaName = stackRef.getOutput("lambdaName");