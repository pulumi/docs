package main

import (
	"github.com/pulumi/pulumi-gcp/sdk/v8/go/gcp/compute"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		region := "us-central1"
		zone := "us-central1-a"
		project := "pulumi-devrel" // REPLACE

		startupScript := `#!/bin/bash
		echo "Hello, World!" > index.html
		nohup python -m SimpleHTTPServer 80 &`

		// Create a VPC network.
		vpcNetwork, err := compute.NewNetwork(ctx, "vpc-network", &compute.NetworkArgs{
			Project: pulumi.String(project),
			AutoCreateSubnetworks: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		// Create an IP address.
		ipAddress, err := compute.NewAddress(ctx, "ip-address", &compute.AddressArgs{
			Project: pulumi.String(project),
			Region: pulumi.String(region),
		})
		if err != nil {
			return err
		}

		// Steps:
		// [1] Create a compute instance.
		// [2] Create and configure a firewall.

		// [1] Create a compute instance.
		_, err = compute.NewInstance(ctx, "webserver-instance", &compute.InstanceArgs{
			Project: pulumi.String(project),
			Zone: pulumi.String(zone),
			MachineType: pulumi.String("f1-micro"),
			MetadataStartupScript: pulumi.String(startupScript),
			BootDisk: &compute.InstanceBootDiskArgs{
				InitializeParams: &compute.InstanceBootDiskInitializeParamsArgs{
					Image: pulumi.String("debian-cloud/debian-9-stretch-v20181210"),
				},
			},
			NetworkInterfaces: compute.InstanceNetworkInterfaceArray{
				&compute.InstanceNetworkInterfaceArgs{
					AccessConfigs: &compute.InstanceNetworkInterfaceAccessConfigArray{
						&compute.InstanceNetworkInterfaceAccessConfigArgs{
							NatIp: ipAddress.Address,
						},
					},
					Network: vpcNetwork.ID(),
				},
			},
			ServiceAccount: &compute.InstanceServiceAccountArgs{
				Scopes: pulumi.StringArray{
					pulumi.String("https://www.googleapis.com/auth/cloud-platform"),
				},
			},
		})
		if err != nil {
			return err
		}

		// [2] Create and configure a firewall.
		_, err = compute.NewFirewall(ctx, "firewall", &compute.FirewallArgs{
			Project: pulumi.String(project),
			Network: vpcNetwork.SelfLink,
			Allows: compute.FirewallAllowArray{
				&compute.FirewallAllowArgs{
					Protocol: pulumi.String("tcp"),
					Ports: pulumi.StringArray{
						pulumi.String("80"),
					},
				},
			},
			SourceRanges: pulumi.StringArray{
				pulumi.String("0.0.0.0/0"),
			},
		})
		if err != nil {
			return err
		}

        instanceUrl := ipAddress.Address.ApplyT(func(address string) string {
			return "http://" + address
		}).(pulumi.StringOutput)

		// Export the URL of the server
		ctx.Export("instanceURL", instanceUrl)
		return nil
	})
}