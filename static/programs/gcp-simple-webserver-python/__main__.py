import pulumi
from pulumi_gcp import compute

region = "us-central1"
zone = "us-central1-a"
project = "pulumi-devrel" # REPLACE

startup_script = """#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 80 &"""

# Create a VPC network.
vpc_network = compute.Network("vpc-network",
    project=project,
    auto_create_subnetworks=True
)

# Create an IP Address
ip_address = compute.address.Address("ip-address",
    project=project,
    region=region
)

#### Steps:
# [1] Create a compute instance.
# [2] Create and configure a firewall.

# [1] Create a compute instance.
compute_instance = compute.Instance(
    "webserver-instance",
    machine_type="f1-micro",
    project=project,
    zone=zone,
    metadata_startup_script=startup_script,
    boot_disk=compute.InstanceBootDiskArgs(
        initialize_params=compute.InstanceBootDiskInitializeParamsArgs(
            image="debian-cloud/debian-9-stretch-v20181210"
        )
    ),
    network_interfaces=[compute.InstanceNetworkInterfaceArgs(
            network=vpc_network.id,
            access_configs=[compute.InstanceNetworkInterfaceAccessConfigArgs(
                nat_ip=ip_address.address
            )],
    )],
    service_account=compute.InstanceServiceAccountArgs(
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
)

# [2] Create and configure a firewall.
compute_firewall = compute.Firewall(
    "firewall",
    project=project,
    network=vpc_network.self_link,
    allows=[compute.FirewallAllowArgs(
        protocol="tcp",
        ports=["80"],
    )],
    source_ranges=["0.0.0.0/0"]
)

# Export the URL of the server
instance_url = ip_address.address.apply(
    lambda address: "http://" + address
)

pulumi.export("instanceURL", instance_url)