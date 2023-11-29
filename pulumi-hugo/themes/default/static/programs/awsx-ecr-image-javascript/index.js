"use strict";
const pulumi = require("@pulumi/pulumi");
const awsx = require("@pulumi/awsx");

const repository = new awsx.ecr.Repository("repository", {
    forceDelete: true,
});

const image = new awsx.ecr.Image("image", {
    repositoryUrl: repository.url,
    context: "./app",
    platform: "linux/amd64",
});

exports.url = repository.url;
