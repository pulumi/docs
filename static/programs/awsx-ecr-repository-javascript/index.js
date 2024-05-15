"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");
const awsx = require("@pulumi/awsx");

const repo = new awsx.ecr.Repository("repo");
exports.url = repo.url;
