import * as pulumi from "@pulumi/pulumi";

// Create a new Pulumi Config
const config = new pulumi.Config();

// Retrieve the value of "myEnvironment" from the Pulumi Config
const myValue = config.get("myEnvironment");

// Export "myValue" as a stack output named 'Value'
export const value = myValue;
