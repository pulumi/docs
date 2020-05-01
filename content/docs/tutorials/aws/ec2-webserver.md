---
title: Deploy a Webserver to AWS EC2
meta_desc: This tutorial will teach you how to deploy a simple webserver to an
           AWS EC2 instance.
aliases: ["/docs/reference/tutorials/aws/tutorial-ec2-webserver/"]
---

{{< github-buttons "aws-js-webserver" "aws-py-webserver" >}}

In this tutorial, we will show you how to use JavaScript or Python to deploy a simple webserver using an Amazon EC2 instance.

{{< multilang-tutorial-prereqs >}}

{{< chooser language "javascript,typescript,python,csharp" >}}

{{% choosable language "javascript,typescript" %}}
{{< install-node >}}
{{% /choosable %}}

{{% choosable language python %}}
{{< install-python >}}
{{% /choosable %}}

{{% choosable language "csharp,fsharp,visualbasic" %}}
{{< install-dotnet >}}
{{% /choosable %}}

{{< /chooser >}}

## Deploy the App

### Step 1: Create a new project from a template

Create a project directory, `webserver`, and change into it. Run [`pulumi new aws-<language> --name myproject`]({{< relref "/docs/reference/cli/pulumi_new" >}}) to create a new project using the AWS template for your chosen language. Replace `myproject` with your desired project name.

{{< chooser language "javascript,typescript,python,csharp" / >}}

{{% choosable language javascript %}}

```bash
$ mkdir webserver && cd webserver
$ pulumi new aws-javascript --name myproject
```

{{% /choosable %}}
{{% choosable language typescript %}}

```bash
$ mkdir webserver && cd webserver
$ pulumi new aws-typescript --name myproject
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
$ mkdir webserver && cd webserver
$ pulumi new aws-python --name myproject
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
$ mkdir webserver && cd webserver
$ pulumi new aws-csharp --name myproject
```

{{% /choosable %}}

### Step 2: Create an EC2 instance with SSH access

Open {{< langfile >}} and replace the contents with the following:

{{< chooser language "javascript,typescript,python,csharp" / >}}

{{% choosable language javascript %}}

```javascript
const aws = require("@pulumi/aws");

let size = "t2.micro";     // t2.micro is available in the AWS free tier
let ami = aws.getAmi({
    filters: [{
      name: "name",
      values: ["amzn-ami-hvm-*"],
    }],
    owners: ["137112412989"], // This owner ID is Amazon
    mostRecent: true,
});

let group = new aws.ec2.SecurityGroup("webserver-secgrp", {
    ingress: [
        { protocol: "tcp", fromPort: 22, toPort: 22, cidrBlocks: ["0.0.0.0/0"] },
    ],
});

let server = new aws.ec2.Instance("webserver-www", {
    instanceType: size,
    securityGroups: [ group.name ], // reference the security group resource above
    ami: ami.id,
});

exports.publicIp = server.publicIp;
exports.publicHostName = server.publicDns;
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

const size = "t2.micro";     // t2.micro is available in the AWS free tier
const ami = aws.getAmi({
    filters: [{
        name: "name",
        values: ["amzn-ami-hvm-*"],
    }],
    owners: ["137112412989"], // This owner ID is Amazon
    mostRecent: true,
});

const group = new aws.ec2.SecurityGroup("webserver-secgrp", {
    ingress: [
        { protocol: "tcp", fromPort: 22, toPort: 22, cidrBlocks: ["0.0.0.0/0"] },
    ],
});

const server = new aws.ec2.Instance("webserver-www", {
    instanceType: size,
    securityGroups: [ group.name ], // reference the security group resource above
    ami: ami.id,
});

export const publicIp = server.publicIp;
export const publicHostName = server.publicDns;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws

size = 't2.micro'
ami = aws.get_ami(most_recent="true",
                  owners=["137112412989"],
                  filters=[{"name":"name","values":["amzn-ami-hvm-*"]}])

group = aws.ec2.SecurityGroup('webserver-secgrp',
    description='Enable HTTP access',
    ingress=[
        { 'protocol': 'tcp', 'from_port': 22, 'to_port': 22, 'cidr_blocks': ['0.0.0.0/0'] }
    ])

server = aws.ec2.Instance('webserver-www',
    instance_type=size,
    security_groups=[group.name], # reference security group from above
    ami=ami.id)

pulumi.export('publicIp', server.public_ip)
pulumi.export('publicHostName', server.public_dns)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Aws;

class Program
{
    static Task Main() =>
        Deployment.Run(() =>
        {
            var size = "t2.micro";     // t2.micro is available in the AWS free tier
            var ami = Aws.GetAmi.InvokeAsync(new Aws.GetAmiArgs
            {
                Filters =
                {
                    new GetAmiFiltersArgs
                    {
                        Name = "name",
                        Values =  { "amzn-ami-hvm-*" },
                    },
                },
                Owners = { "137112412989" }, // This owner ID is Amazon
                MostRecent = true,
            });

            var group = new Aws.Ec2.SecurityGroup("webserver-secgrp", new Aws.Ec2.SecurityGroupArgs
            {
                Ingress =
                {
                    new Aws.Ec2.SecurityGroupIngressArgs
                    {
                        Protocol = "tcp",
                        FromPort = 22,
                        ToPort = 22,
                        CidrBlocks = { "0.0.0.0/0" },
                    },
                },
            });

            var server = new Aws.Ec2.Instance("webserver-www", new Aws.Ec2.InstanceArgs
            {
                InstanceType = size,
                SecurityGroups = { group.Name }, // reference the security group resource above
                Ami = ami.Id,
            });

            return new Dictionary<string, object>
            {
                { "publicIp", server.PublicIp },
                { "publicHostName", server.PublicDns },
            };
        });
}
```

{{% /choosable %}}

> **Note:** The example configuration is designed to work on most EC2 accounts, with access to a default VPC. For EC2 Classic users, please use t1.micro for `size`.

This example uses the [`@pulumi/aws`]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws" >}}) package in JavaScript and TypeScript code and the [`pulumi_aws`]({{< relref "/docs/reference/pkg/python/pulumi_aws" >}}) package in Python code to create two resources:

| AWS Resource | Description | TypeScript / JavaScript Resource | Python Resource |
|--------------|---------|----------------------------------|-----------------|
| Security Group | Created for allowing incoming SSH access | [aws.ec2.SecurityGroup][Security Group] | [ec2.SecurityGroup]({{< relref "/docs/reference/pkg/python/pulumi_aws/ec2#pulumi_aws.ec2.SecurityGroup" >}}) |
| EC2 Instance | Created in that security group using the appropriate Amazon Machine Image (AMI) for the region where you deploy the program | [aws.ec2.Instance][EC2 Instance] | [ec2.Instance]({{< relref "/docs/reference/pkg/python/pulumi_aws/ec2#pulumi_aws.ec2.Instance" >}}) |

### Step 3: Preview and deploy your resources

To preview your Pulumi program, run [`pulumi up`]({{< relref "/docs/reference/cli/pulumi_up" >}}). The command shows a preview of the resources that will be created and prompts you to proceed with the deployment.  Note that the stack itself is counted as a resource, though it does not correspond to a physical cloud resource.

```bash
Previewing update (webserver-dev):

     Type                      Name                     Plan
 +   pulumi:pulumi:Stack       myproject-webserver-dev  create
 +   ├─ aws:ec2:SecurityGroup  webserver-secgrp         create
 +   └─ aws:ec2:Instance       webserver-www            create

Resources:
    + 3 to create

Do you want to perform this update?
  yes
> no
  details
```

Next, proceed with the deployment, which takes about 40 seconds to complete.

```bash
Do you want to perform this update? yes
Updating (webserver-dev):

     Type                      Name                     Status
 +   pulumi:pulumi:Stack       myproject-webserver-dev  created
 +   ├─ aws:ec2:SecurityGroup  webserver-secgrp         created
 +   └─ aws:ec2:Instance       webserver-www            created

Outputs:
    publicHostName: "ec2-34-217-110-29.us-west-2.compute.amazonaws.com"
    publicIp      : "34.217.110.29"

Resources:
    + 3 created

Duration: 40s

Permalink: https://app.pulumi.com/bermudezmt/myproject/webserver-dev/updates/1
```

### Step 4: View your stack resources

#### **Pulumi Console**

To see the full details of the deployment and the resources that are now part of the stack, open the update link in a browser. The **Resources** tab on the Pulumi Console has a link to the AWS console for the provisioned EC2 instance.

#### **Pulumi CLI**

To view the provisioned resources on the command line, run [`pulumi stack`]({{< relref "/docs/reference/cli/pulumi_stack" >}}). You'll also see two [stack outputs]({{< relref "/docs/intro/concepts/stack#outputs" >}}) corresponding to the IP and the fully qualified domain name (FQDN) of the EC2 instance we've created.

```
Current stack is webserver-dev:
    Owner: <your-org-name>
    Last updated: 10 minutes ago (2019-09-20 11:57:55.90881794 -0700 PDT)
    Pulumi version: v1.1.0
Current stack resources (4):
    TYPE                                 NAME
    pulumi:pulumi:Stack                  myproject-webserver-dev
    pulumi:providers:aws                 default_1_2_1
    aws:ec2/securityGroup:SecurityGroup  webserver-secgrp
    aws:ec2/instance:Instance            webserver-www

More information at: https://app.pulumi.com/<your-org-name>/myproject/webserver-dev

Use `pulumi stack select` to change stack; `pulumi stack ls` lists known ones
```

### Step 5: Update the Pulumi program

Now that you have an instance of the Pulumi program deployed, you may want to make changes. You do so by updating the
Pulumi program to define the new state you want your infrastructure to be in, and then running `pulumi up` to commit the changes.

Replace the creation of the two resources with the following code. This exposes an additional port, `80`, and adds a startup
script to run a simple HTTP server at startup.

{{< chooser language "javascript,typescript,python,csharp" >}}

{{% choosable language javascript %}}

```javascript
...

let group = new aws.ec2.SecurityGroup("webserver-secgrp", {
    ingress: [
        { protocol: "tcp", fromPort: 22, toPort: 22, cidrBlocks: ["0.0.0.0/0"] },
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
        // ^-- ADD THIS LINE
    ],
});

let userData = // <-- ADD THIS DEFINITION
`#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 80 &`;

let server = new aws.ec2.Instance("web-server-www", {
    instanceType: size,
    securityGroups: [ group.name ], // reference the group object above
    ami: ami.id,
    userData: userData,             // <-- ADD THIS LINE
});

...
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
...

const group = new aws.ec2.SecurityGroup("webserver-secgrp", {
    ingress: [
        { protocol: "tcp", fromPort: 22, toPort: 22, cidrBlocks: ["0.0.0.0/0"] },
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
        // ^-- ADD THIS LINE
    ],
});

const userData = // <-- ADD THIS DEFINITION
`#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 80 &`;

const server = new aws.ec2.Instance("webserver-www", {
    instanceType: size,
    securityGroups: [ group.name ], // reference the security group resource above
    ami: ami.id,
    userData: userData,             // <-- ADD THIS LINE
});

...
```

{{% /choosable %}}
{{% choosable language python %}}

```python
...

group = ec2.SecurityGroup('webserver-secgrp',
    description='Enable HTTP access',
    ingress=[
        { 'protocol': 'tcp', 'from_port': 22, 'to_port': 22, 'cidr_blocks': ['0.0.0.0/0'] },
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] }
        # ^-- ADD THIS LINE
    ])

user_data = """
#!/bin/bash
echo "Hello, World!" > index.html
nohup python -m SimpleHTTPServer 80 &
"""
# ^-- ADD THIS DEFINITION

server = ec2.Instance('webserver-www',
    instance_type=size,
    security_groups=[group.name], # reference security group from above
    user_data=user_data, # <-- ADD THIS LINE
    ami=ami.id)

...
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
//...
var group = new Aws.Ec2.SecurityGroup("webserver-secgrp", new Aws.Ec2.SecurityGroupArgs
{
    Ingress =
    {
        new Aws.Ec2.SecurityGroupIngressArgs
        {
            Protocol = "tcp",
            FromPort = 22,
            ToPort = 22,
            CidrBlocks = { "0.0.0.0/0" },
        },
        new Aws.Ec2.SecurityGroupIngressArgs
        {
            Protocol = "tcp",
            FromPort = 80,
            ToPort = 90,
            CidrBlocks = { "0.0.0.0/0" },
        },
        // ^-- ADD THIS item
    },
});

var userData = // <-- ADD THIS DEFINITION
@"#!/bin/bash
echo ""Hello, World!"" > index.html
nohup python -m SimpleHTTPServer 80 &";

var server = new Aws.Ec2.Instance("webserver-www", new Aws.Ec2.InstanceArgs
{
    InstanceType = size,
    SecurityGroups = { group.Name }, // reference the security group resource above
    Ami = Ami.Id,
    UserData = userData,             // <-- ADD THIS LINE
});
```

{{% /choosable %}}

{{< /chooser >}}

> Note that the `userData` script is defined inline in a string. In this example, `index.html` will be created in the root directory `/`. Because you are using a programming language to write your Pulumi program, you could also read this from a file, construct this string programmatically, or even build up a string that depends on other resources
defined in your program.  You'll see in later sections how to deploy and version the application code of your
program in a variety of different ways using Pulumi.

Run `pulumi up` to preview and deploy the changes. You'll see two changes: the `ingress` property of the `SecurityGroup` will be _updated_ in-place.  Secondly, the `Instance` will be _replaced_ with a new EC2 instance which will run the new script on startup. Pulumi understands which changes to a given cloud resource can be made in place, which require replacement, and computes the minimally disruptive change to achieve the desired state.

```bash
Previewing update (webserver-dev):

     Type                      Name                     Plan        Info
     pulumi:pulumi:Stack       myproject-webserver-dev
 ~   ├─ aws:ec2:SecurityGroup  webserver-secgrp         update      [diff: ~ingress]
 +-  └─ aws:ec2:Instance       webserver-www            replace     [diff: +userData~securityGroups]

Resources:
    ~ 1 to update
    +-1 to replace
    2 changes. 1 unchanged
```

When prompted to confirm your update, you may review the planned changes to your stack resources by selecting `details`.

```bash
Do you want to perform this update? details
  pulumi:pulumi:Stack: (same)
    [urn=urn:pulumi:webserver-dev::myproject::pulumi:pulumi:Stack::myproject-webserver-dev]
    ~ aws:ec2/securityGroup:SecurityGroup: (update)
        [id=sg-0317c16c7015d7fd0]
        [urn=urn:pulumi:webserver-dev::myproject::aws:ec2/securityGroup:SecurityGroup::webserver-secgrp]
        [provider=urn:pulumi:webserver-dev::myproject::pulumi:providers:aws::default_1_2_1::eec9bbfb-0881-4f75-a0cb-35395a0240e2]
      ~ ingress: [
          ~ [0]: {
                  ~ cidrBlocks : [
                      ~ [0]: "0.0.0.0/0" => "0.0.0.0/0"
                    ]
                  - description: ""
                  ~ fromPort   : 22 => 22
                  ~ protocol   : "tcp" => "tcp"
                  ~ self       : false => false
                  ~ toPort     : 22 => 22
                }
          + [1]: {
                  + cidrBlocks: [
                  +     [0]: "0.0.0.0/0"
                    ]
                  + fromPort  : 80
                  + protocol  : "tcp"
                  + self      : false
                  + toPort    : 80
                }
        ]
    ++aws:ec2/instance:Instance: (create-replacement)
        [id=i-0a639b62c37bf712c]
        [urn=urn:pulumi:webserver-dev::myproject::aws:ec2/instance:Instance::webserver-www]
        [provider=urn:pulumi:webserver-dev::myproject::pulumi:providers:aws::default_1_2_1::eec9bbfb-0881-4f75-a0cb-35395a0240e2]
      ~ securityGroups: [
          ~ [0]: "webserver-secgrp-2398ba7" => output<string>
        ]
      + userData      : "#!/bin/bash\necho \"Hello, World!\" > index.html\nnohup python -m SimpleHTTPServer 80 &"
    +-aws:ec2/instance:Instance: (replace)
        [id=i-0a639b62c37bf712c]
        [urn=urn:pulumi:webserver-dev::myproject::aws:ec2/instance:Instance::webserver-www]
        [provider=urn:pulumi:webserver-dev::myproject::pulumi:providers:aws::default_1_2_1::eec9bbfb-0881-4f75-a0cb-35395a0240e2]
      ~ securityGroups: [
          ~ [0]: "webserver-secgrp-2398ba7" => output<string>
        ]
      + userData      : "#!/bin/bash\necho \"Hello, World!\" > index.html\nnohup python -m SimpleHTTPServer 80 &"
    --aws:ec2/instance:Instance: (delete-replaced)
        [id=i-0a639b62c37bf712c]
        [urn=urn:pulumi:webserver-dev::myproject::aws:ec2/instance:Instance::webserver-www]
        [provider=urn:pulumi:webserver-dev::myproject::pulumi:providers:aws::default_1_2_1::eec9bbfb-0881-4f75-a0cb-35395a0240e2]
```

Select `yes` to confirm the update.

You can use `pulumi stack output` to get the value of stack outputs from the CLI.  To do so, `curl` the EC2 instance to confirm that the HTTP server is running. Stack outputs can also be viewed on the Pulumi Console.

```bash
$ curl $(pulumi stack output publicHostName)
Hello, World!
```

## Clean Up

{{< cleanup >}}

## Summary

{{< summary >}}
In this tutorial, we showed you how to use Pulumi programs to create and manage cloud resources in AWS, using TypeScript, JavaScript, or Python (and its corresponding package manager).
{{< /summary >}}

<!-- Common links -->
[EC2 Instance]: {{< relref "/docs/reference/pkg/nodejs/pulumi/aws/ec2#Instance" >}}
[Security Group]: {{< relref "/docs/reference/pkg/nodejs/pulumi/aws/ec2#SecurityGroup" >}}
[@pulumi/aws]: {{< relref "/docs/reference/pkg/nodejs/pulumi/aws" >}}
<!-- End common links -->

## Next Steps

- [Containers on ECS Fargate]({{< relref "/docs/tutorials/aws/ecs-fargate" >}})
- [API Gateways and Lambda]({{< relref "/docs/tutorials/aws/rest-api" >}})
- [Serve a Static Webstie from S3]({{< relref "/docs/tutorials/aws/s3-website" >}})
