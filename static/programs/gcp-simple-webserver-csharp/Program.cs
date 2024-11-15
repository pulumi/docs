﻿using Pulumi;
using Gcp = Pulumi.Gcp;
using System.Linq;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
    var region = "us-central1";
    var zone = "us-central1-a";
    var project = "pulumi-devrel"; // REPLACE
    var startupScript = @"#!/bin/bash
    echo ""Hello, World!"" > index.html
    nohup python -m SimpleHTTPServer 80 &";
    // Create a VPC network.
    var vpcNetwork = new Gcp.Compute.Network("vpc-network", new()
    {
        Project = project,
        AutoCreateSubnetworks = true,
    });
    var ipAddress = new Gcp.Compute.Address("ip-address", new()
    {
        Project = project,
        Region = region,
    });
    // Steps:
    // [1] Create a compute instance.
    // [2] Create and configure a firewall.
    // [1] Create a compute instance.
    var computeInstance = new Gcp.Compute.Instance("webserver-instance", new()
    {
        MachineType ="f1-micro",
        Project = project,
        Zone=zone,
        MetadataStartupScript=startupScript,
        BootDisk= new Gcp.Compute.Inputs.InstanceBootDiskArgs
        {
            InitializeParams = new Gcp.Compute.Inputs.InstanceBootDiskInitializeParamsArgs
            {
                Image="debian-cloud/debian-9-stretch-v20181210"
            }
        },
        NetworkInterfaces= new[]
        {
            new Gcp.Compute.Inputs.InstanceNetworkInterfaceArgs
            {
                AccessConfigs = new[]
                {
                    new Gcp.Compute.Inputs.InstanceNetworkInterfaceAccessConfigArgs
                    {
                        NatIp = ipAddress.IPAddress
                    }
                },
                Network = vpcNetwork.Id
            }
        },
        ServiceAccount = new Gcp.Compute.Inputs.InstanceServiceAccountArgs
        {
            Scopes = new[] 
            {
                "https://www.googleapis.com/auth/cloud-platform"
            },
        }
    });
    // [2] Create and configure a firewall.
    var computeFirewall = new Gcp.Compute.Firewall("firewall", new()
    {
        Project = project,
        Network = vpcNetwork.SelfLink,
        Allows = new[]
        {
            new Gcp.Compute.Inputs.FirewallAllowArgs
            {
                Protocol = "tcp",
                Ports = new[]
                {
                    "80",
                },
            },
        },
        SourceRanges = new[]
        {
            "0.0.0.0/0",
        },
    });
    var instanceUrl = ipAddress.IPAddress.Apply(ipAddress => $"http://{ipAddress}");
    // Export the URL of the server
    return new Dictionary<string, object?>
    {
        ["instanceURL"] = instanceUrl
    };
});