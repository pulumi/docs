"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");

const user = new aws.iam.User("webmaster", {
    path: "/system/",
    tags: { Name: "webmaster" },
});

const userAccessKey = new aws.iam.AccessKey("webmasterKey", { user: user.name });

const userPolicy = new aws.iam.UserPolicy("webmasterPolicy", {
    user: user.name,
    policy: JSON.stringify({
        Version: "2012-10-17",
        Statement: [
            {
                Action: ["ec2:Describe*"],
                Effect: "Allow",
                Resource: "*",
            },
        ],
    }),
});
