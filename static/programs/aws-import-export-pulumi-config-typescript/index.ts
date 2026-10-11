import * as pulumi from "@pulumi/pulumi";

// Create a new Pulumi Config
const config = new pulumi.Config();

// Retrieve the values of "region" and "apiKey"
const region = config.get("region");
const apiKey = config.getSecret("apiKey");

// Export values as stack output
export const Region = region;
export const ApiKey = apiKey;
