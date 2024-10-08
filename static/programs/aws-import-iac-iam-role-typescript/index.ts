import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const importedRole = new aws.iam.Role(
    "imported_role",
    {
        name: "pulumi-tutorial-iam-role",
        description: "Allows Lambda functions to call AWS services on your behalf.",
        assumeRolePolicy: JSON.stringify({
            Version: "2012-10-17",
            Statement: [
                {
                    Action: "sts:AssumeRole",
                    Effect: "Allow",
                    Sid: "",
                    Principal: {
                        Service: "lambda.amazonaws.com",
                    },
                },
            ],
        }),
    },
    {
        import: "pulumi-tutorial-iam-role",
    },
);
