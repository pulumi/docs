"use strict";
const pulumi = require("@pulumi/pulumi");

// Create a new Pulumi Config
const config = new pulumi.Config();

// Retrieve the value of "myEnvironment" from the Pulumi Config
const myValue = config.get("myEnvironment");

// Export "myValue" as a stack output named 'value'
module.exports = {
    value: myValue,
};
