import * as aws from "@pulumi/aws";

const role = new aws.iam.Role("my-role", {
    assumeRolePolicy: {
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
    },
});

const profile = new aws.iam.InstanceProfile("instance-profile", { role });
