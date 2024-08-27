"use strict";
const pulumi = require("@pulumi/pulumi");

// Create a new Pulumi Config
const config = new pulumi.Config();

// Retrieve the values of "myEnvironment" and "myPassword"
const environment = config.get("myEnvironment");
const password = config.getSecret("myPassword");

// Export values as stack outputs
module.exports = {
    Environment: environment,
    Password: password,
};
