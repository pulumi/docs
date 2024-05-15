import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const policy: aws.iam.PolicyDocument = {
    Version: "2012-10-17",
    Statement: [
        {
            Action: "sts:AssumeRole",
            Principal: {
                Service: "ec2.amazonaws.com",
            },
            Effect: "Allow",
        },
    ],
};

const role = new aws.iam.Role("instance-role", {
    assumeRolePolicy: policy,
    path: "/",
});

const profile = new aws.iam.InstanceProfile("instance-profile", { role });
