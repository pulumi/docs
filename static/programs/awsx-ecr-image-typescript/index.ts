import * as pulumi from "@pulumi/pulumi";
import * as awsx from "@pulumi/awsx";

const repository = new awsx.ecr.Repository("repository", {
    forceDelete: true,
});

const image = new awsx.ecr.Image("image", {
    repositoryUrl: repository.url,
    context: "./app",
    platform: "linux/amd64",
});

export const url = repository.url;
