---
title: Modify the Program
weight: 8
menu:
  get-started:
    parent: gcp
    identifier: gcp-modify-program
---

Now that we have an instance of our Pulumi program deployed, let's update it to do something a little more interesting.

Replace the entire contents of {{< langfile >}} with the following:

{{< langchoose nogo >}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const gcp = require("@pulumi/gcp");

// Create a network
const network = new gcp.compute.Network("network");
const firewall = new gcp.compute.Firewall("firewall", {
    network: network.id,
    allows: [{
        protocol: "tcp",
        ports: [ "80" ],
    }],
});

// Create a simple web server using the startup script for the instance
const startupScript = `#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 80 &`;

// Create compute instance
const instance = new gcp.compute.Instance("instance", {
    machineType: "f1-micro",
    zone: "us-central1-a",
    metadataStartupScript: startupScript,
    bootDisk: { initializeParams: { image: "debian-cloud/debian-9" } },
    networkInterfaces: [{
        network: network.id,
        // accessConfigs must include a single empty config to request an ephemeral IP
        accessConfigs: [{}],
    }],
}, { dependsOn: [firewall] });

// Export the IP address
exports.ip = instance.networkInterfaces.apply(ni => ni[0].accessConfigs[0].natIp);
```

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

// Create a network
const network = new gcp.compute.Network("network");
const firewall = new gcp.compute.Firewall("firewall", {
    network: network.id,
    allows: [{
        protocol: "tcp",
        ports: [ "80" ],
    }],
});

// Create a simple web server using the startup script for the instance
const startupScript = `#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 80 &`;

// Create compute instance
const instance = new gcp.compute.Instance("instance", {
    machineType: "f1-micro",
    zone: "us-central1-a",
    metadataStartupScript: startupScript,
    bootDisk: { initializeParams: { image: "debian-cloud/debian-9" } },
    networkInterfaces: [{
        network: network.id,
        // accessConfigs must include a single empty config to request an ephemeral IP
        accessConfigs: [{}],
    }],
}, { dependsOn: [firewall] });

// Export the IP address
export const ip = instance.networkInterfaces.apply(ni => ni![0]!.accessConfigs![0].natIp);
```

```python
import pulumi
from pulumi_gcp import compute

# Create a network
network = compute.Network("network")
firewall = compute.Firewall(
    "firewall",
    network=network.id,
    allows=[
        { "protocol": "tcp", "ports": [ "80" ] }
    ])

# Create a simple web server using the startup script for the instance
startup_script = """
#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 80 &
"""

# Create compute instance
instance = compute.Instance(
    "instance",
    machine_type="f1-micro",
    zone="us-central1-a",
    metadata_startup_script=startup_script,
    boot_disk={ "initialize_params": { "image": "debian-cloud/debian-9" } },
    network_interfaces=[{
        "network": network.id,
        # accessConfigs must include a single empty config to request an ephemeral IP
        "access_configs": [{}],
    }],
    opts=pulumi.ResourceOptions(depends_on=[firewall]))

# Export the IP address
pulumi.export("ip", instance.network_interfaces.apply(lambda ni: ni[0]["accessConfigs"][0]["natIp"] if "accessConfigs" in ni[0] else None))
```

Our program now creates a simple virtual machine running a Python web server.

Next, we'll deploy the changes.

{{< get-started-stepper >}}
