import * as pulumi from "@pulumi/pulumi";

// Create a new Pulumi Config
const config = new pulumi.Config();

// Retrieve the values of "myEnvironment" and "myPassword"
const environment = config.get("myEnvironment");
const password = config.get("myPassword");

// Export values as stack output
export const Environment = environment;
export const Password = password;
