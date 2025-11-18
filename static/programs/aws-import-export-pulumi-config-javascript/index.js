"use strict";
const pulumi = require("@pulumi/pulumi");

// Create a new Pulumi Config
const config = new pulumi.Config();

// Retrieve the values of "region" and "apiKey"
const region = config.get("region");
const apiKey = config.getSecret("apiKey");

// Export values as stack outputs
module.exports = {
    Region: region,
    ApiKey: apiKey,
};
