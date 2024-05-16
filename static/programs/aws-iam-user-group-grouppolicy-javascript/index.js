"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");

// Create our users.
const jane = new aws.iam.User("jane");
const mary = new aws.iam.User("mary");

// Define a group and assign a policy for it.
const devs = new aws.iam.Group("devs", {
    path: "/users/",
});

const myDeveloperPolicy = new aws.iam.GroupPolicy("my_developer_policy", {
    group: devs.id,
    policy: {
        Version: "2012-10-17",
        Statement: [
            {
                Action: ["ec2:Describe*"],
                Effect: "Allow",
                Resource: "*",
            },
        ],
    },
});

// Finally add the users as members to this group.
const devTeam = new aws.iam.GroupMembership("dev-team", {
    group: devs.id,
    users: [jane.id, mary.id],
});
