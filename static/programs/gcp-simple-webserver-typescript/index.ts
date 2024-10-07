import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

const region = "us-central1";
const zone = "us-central1-a";
const project = "pulumi-devrel"; // REPLACE

const startupScript = `#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 80 &`;

// Create a VPC network.
const vpcNetwork = new gcp.compute.Network("vpc-network", {
    project: project,
    autoCreateSubnetworks: true,
});

// Create an IP address.
const ipAddress = new gcp.compute.Address("ip-address", {
    project: project,
    region: region,
});

// Steps:
// [1] Create a compute instance.
// [2] Create and configure a firewall.

// [1] Create a compute instance.
const computeInstance = new gcp.compute.Instance("webserver-instance", {
    machineType: "f1-micro",
    project: project,
    zone: zone,
    metadataStartupScript: startupScript,
    bootDisk: {
        initializeParams: {
            image: "debian-cloud/debian-9-stretch-v20181210",
        },
    },
    networkInterfaces: [
        {
            accessConfigs: [
                {
                    natIp: ipAddress.address,
                },
            ],
            network: vpcNetwork.id,
        },
    ],
    serviceAccount: {
        scopes: ["https://www.googleapis.com/auth/cloud-platform"],
    },
});

// [2] Create and configure a firewall.
const firewall = new gcp.compute.Firewall("firewall", {
    project: project,
    network: vpcNetwork.selfLink,
    allows: [
        {
            protocol: "tcp",
            ports: ["80"],
        },
    ],
    sourceRanges: ["0.0.0.0/0"],
});

const instanceUrl = ipAddress.address.apply(address => `http://${address}`);

// Export the DNS name of the bucket
export const instanceURL = instanceUrl;
