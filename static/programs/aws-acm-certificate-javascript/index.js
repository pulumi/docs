"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");

let certCertificate = new aws.acm.Certificate("cert", {
    domainName: "example.com",
    validationMethod: "DNS",
});
