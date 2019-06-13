---
title: Modify the Program
weight: 7
menu:
  quickstart:
    parent: aws
    identifier: aws-modify-program
---

Now that we have an instance of our Pulumi program deployed, let's update it to do something a little more interesting.

Replace the entire contents of {{< langfile >}} with the following:

{{< langchoose nogo >}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");
const awsx = require("@pulumi/awsx");

const size = "t2.micro"; // t2.micro is available in the AWS free tier

const ami = "ami-6869aa05" // AMI for us-east-1 (Virginia)
// const ami  = "ami-c55673a0" // AMI for us-east-2 (Ohio)
// const ami  = "ami-31490d51" // AMI for us-west-1 (California)
// const ami  = "ami-7172b611" // AMI for us-west-2 (Oregon)
// const ami  = "ami-f9dd458a" // AMI for eu-west-1 (Ireland)
// const ami  = "ami-ea26ce85" // AMI for eu-central-1 (Frankfurt)

// Create a new security group for port 80
const group = new aws.ec2.SecurityGroup("web-secgrp", {
    ingress: [
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});

// Create a simple web server using the startup script for the instance
const userData =
`#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 80 &`;

const server = new aws.ec2.Instance("web-server-www", {
    tags: { "Name": "web-server-www" },
    instanceType: size,
    securityGroups: [ group.name ], // reference the group object above
    ami: ami,
    userData: userData
});

// Export the host name
exports.host = server.publicDns;
```

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

const size = "t2.micro"; // t2.micro is available in the AWS free tier

const ami = "ami-6869aa05" // AMI for us-east-1 (Virginia)
// const ami  = "ami-c55673a0" // AMI for us-east-2 (Ohio)
// const ami  = "ami-31490d51" // AMI for us-west-1 (California)
// const ami  = "ami-7172b611" // AMI for us-west-2 (Oregon)
// const ami  = "ami-f9dd458a" // AMI for eu-west-1 (Ireland)
// const ami  = "ami-ea26ce85" // AMI for eu-central-1 (Frankfurt)

// Create a new security group for port 80
const group = new aws.ec2.SecurityGroup("web-secgrp", {
    ingress: [
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});

// Create a simple web server using the startup script for the instance
const userData =
`#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 80 &`;

const server = new aws.ec2.Instance("web-server-www", {
    tags: { "Name": "web-server-www" },
    instanceType: size,
    securityGroups: [ group.name ], // reference the group object above
    ami: ami,
    userData: userData
});

// Export the host name
export const host = server.publicDns;
```

```python
import pulumi
from pulumi_aws import ec2

size = 't2.micro'

ami = 'ami-6869aa05' # AMI for us-east-1 (Virginia)
# ami  = 'ami-c55673a0' # AMI for us-east-2 (Ohio)
# ami  = 'ami-31490d51' # AMI for us-west-1 (California)
# ami  = 'ami-7172b611' # AMI for us-west-2 (Oregon)
# ami  = 'ami-f9dd458a' # AMI for eu-west-1 (Ireland)
# ami  = 'ami-ea26ce85' # AMI for eu-central-1 (Frankfurt)

# Create a new security group for port 80
group = ec2.SecurityGroup('web-secgrp',
    description='Enable HTTP access',
    ingress=[
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] }
    ])

# Create a simple web server using the startup script for the instance
user_data = """
#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 80 &
"""

server = ec2.Instance('web-server-www',
    instance_type=size,
    security_groups=[group.name],
    user_data=user_data,
    ami=ami)

# Export the host name
pulumi.export('host', server.public_dns)
```

Our program now creates a simple EC2 virtual machine running a Python web server.

Next, we'll deploy the changes.

{{< get-started-stepper >}}
