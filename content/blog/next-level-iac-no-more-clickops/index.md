---
title: "Next-level IaC: ClickOps No More"

date: 2024-07-15
draft: false
social_media: "Many organizations start out using Click-Ops, but find themselves digging a hole they can't get back out of. Pulumi to the rescue!"
meta_desc: "How to use Pulumi to dig yourself out of a Click-Ops hole."
meta_image: meta.png
authors:
    - troy-howard
tags:
    - next-level-iac
    - python
    - clickops
    - boto
    - import
---

Many organizations start out using Click-Ops, but find themselves digging a hole they can't find their way out of. Today we're going to show you how to use Pulumi to find your way out.

<!--more-->

Imagine this; you, a valiant keyboard warrior, skilled in the dark arts of Python, just joined a new company to do DevOps... and inherited some existing cloud infrastructure. The person before you just clicked around in AWS making things, instead of using infrastructure-as-code to manage it. Ugh... We call that "Click-Ops". Congratulations, you’ve found yourself in a Click-Ops hole.

The biggest problem with Click-Ops is reproducibility. There is no easy way to reliably recreate your environment. Suppose you want to be able to create a staging environment to test some changes, and you also want to be able to recreate the production environment in case of disaster. With Click-Ops that's a serious pain.

Let's fix that... by bringing our existing infrastructure under management by Pulumi.

## Explore your existing AWS infrastructure

The first step to undoing a Click-Ops mess is to have a look at what is already there. You can do this via the AWS web-based experience, or if you're in love with the command-line like we are, we can use the AWS CLI.

In this case we're going to assume that there is a existing AWS VPC that we want to bring under management by Pulumi. There are likely more than one, so lets look at a list of VPCs:

```shell
$ aws ec2 describe-vpcs --output JSON
```

This command shows you all the VPCs under your AWS account, in JSON format. Pulumi will let us describe and manage all of that with code, but creating it all from scratch that would need a lot of typing. Luckily, we can import this existing infrastructure with a single command `pulumi import`, which takes a list of resources in JSON format and outputs a Pulumi program in your preferred programming language.

However, the JSON that the AWS CLI outputs isn't in a format that Pulumi understands. Also a VPC isn't made of a single resource, but rather a graph of many types of resources such as *SecurityGroups*, *Subnets*, *RouteTables*, etc. Scanning all the necessary resources and generating Pulumi-compatible JSON is a complicated topic. For that we will need another tool.

## Using Boto to generate Pulumi-compatible JSON

{{% notes type="info" %}}
The command-line tool `jq` is really handy for viewing and filtering JSON. If you don't already have it set up go ahead and [get that installed](https://jqlang.github.io/jq/download/).
{{% /notes %}}

We put together a basic demo tool called [`pulumi-import-aws-account-scraper`][pulumi-import-aws-account-scraper] using Python’s [Boto library][boto-lib], which can scrape your AWS account, finding all the various resources. It outputs Pulumi compatible JSON which we can then use to generate a Pulumi program in your preferred language.

First, clone the [`pulumi/pulumi-import-aws-account-scraper`][pulumi-import-aws-account-scraper] repo and setup the tool:

```shell
git clone git@github.com:pulumi/pulumi-import-aws-account-scraper.git
cd pulumi-import-aws-account-scraper
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

Next we will use this demo tool to scan your account:

```shell
source venv/bin/activate
python3 account_scraper.py > resources.json
```

This will generate a JSON file with an entry for each resource under your account. However, we only want to import some of those. For this example, we'll assume there is a VPC named `thor` in that list, with associated resources also containing the term `thor` in their name. We can filter that out with a quick `jq` expression:

```shell
cat resources.json | jq '.resources |= map(select(.name | contains("thor")))' > resources-filtered.json
```

If you're working with a different resource type, with different names, feel free to customize this expression to filter out anything you don't want to bring under management by Pulumi.

## Run pulumi import to generate a Pulumi program

Ok, now we've got a file called `resources-filtered.json` in Pulumi-compatible JSON format, describing only the resources we want to import for our particular VPC.

Here's the magic moment! Let’s import that into Pulumi and generate our Pulumi program!

{{< chooser language "python, typescript" />}}

{{% choosable language python %}}

```shell
pulumi import -f resources-filtered.json -o __main__.py --protect=false
```

{{% /choosable %}}
{{% choosable language typescript %}}

```shell
pulumi import -f resources-filtered.json -o index.ts --protect=false
```

{{% /choosable %}}

That will generate a Pulumi program containing definitions for each resource. The code should look something like this:

{{< chooser language "python, typescript" />}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws

vpc_thor_vpc_abcdef0123456789 = aws.ec2.Vpc("vpc-thor-vpc-abcdef0123456789",
    cidr_block="10.0.0.0/16",
    instance_tenancy="default",
    tags={
        "Name": "vpc-thor",
    })

vpc_thor_public_1_subnet = aws.ec2.Subnet("vpc-thor-public-1-subnet-abcdef0123456789",
    availability_zone="us-west-2a",
    cidr_block="10.0.32.0/20",
    map_public_ip_on_launch=True,
    private_dns_hostname_type_on_launch="ip-name",
    tags={
        "Name": "vpc-thor-public-1",
        "SubnetType": "Public",
    },
    vpc_id=vpc_thor_vpc_abcdef0123456789.id)

# ...

```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const vpc_thor_vpc_abcdef0123456789 = new aws.ec2.Vpc("vpc-thor-vpc-abcdef0123456789", {
    cidrBlock: "10.0.0.0/16",
    instanceTenancy: "default",
    tags: {
        Name: "vpc-thor",
    },
});

const vpc_thor_public_1_subnet_abcdef0123456789 = new aws.ec2.Subnet("vpc-thor-public-1-subnet-abcdef0123456789", {
    availabilityZone: "us-west-2a",
    cidrBlock: "10.0.32.0/20",
    mapPublicIpOnLaunch: true,
    privateDnsHostnameTypeOnLaunch: "ip-name",
    tags: {
        Name: "vpc-thor-public-1",
        SubnetType: "Public",
    },
    vpcId: vpc_thor_vpc_abcdef0123456789.id,
});

// ...
```

{{% /choosable %}}
`

Next let's verify that's working and trying making a change.

## Verify our Pulumi program

Now that you have a Pulumi program describing your cloud resources, you can manage your with the `pulumi` CLI app.

Trying running `pulumi up`. It will list the resources it knows about it, and at this point it should show that there are no changes to make (`up` means `update`!).

```shell
$ pulumi up

Updating (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/troy-pulumi-corp/no-more-clickops/dev/updates/1

     Type                 Name        Status
     pulumi:pulumi:Stack  no-more-clickops-dev

Resources:
    18 unchanged

Duration: 7s
```

So let's give Pulumi something to do! Try opening the code and making a change to the VPC definition. We will add a tag called `test` with the value `I LOVE PULUMI`.

{{< chooser language "python, typescript" />}}

{{% choosable language python %}}

```python {hl_lines=[9,20]}
import pulumi
import pulumi_aws as aws

vpc_thor_vpc_abcdef0123456789 = aws.ec2.Vpc("vpc-thor-vpc-abcdef0123456789",
    cidr_block="10.0.0.0/16",
    instance_tenancy="default",
    tags={
        "Name": "vpc-thor",
        "test": "I LOVE PULUMI"
    })

vpc_thor_public_1_subnet = aws.ec2.Subnet("vpc-thor-public-1-subnet-abcdef0123456789",
    availability_zone="us-west-2a",
    cidr_block="10.0.32.0/20",
    map_public_ip_on_launch=True,
    private_dns_hostname_type_on_launch="ip-name",
    tags={
        "Name": "vpc-thor-public-1",
        "SubnetType": "Public",
        "test": "I LOVE PULUMI"
    },
    vpc_id=vpc_thor_vpc_abcdef0123456789.id)
# ...

```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript {hl_lines=[9,21]}
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const vpc_thor_vpc_abcdef0123456789 = new aws.ec2.Vpc("vpc-thor-vpc-abcdef0123456789", {
    cidrBlock: "10.0.0.0/16",
    instanceTenancy: "default",
    tags: {
        Name: "vpc-thor",
        test: "I LOVE PULUMI"
    },
});

const vpc_thor_public_1_subnet_abcdef0123456789 = new aws.ec2.Subnet("vpc-thor-public-1-subnet-abcdef0123456789", {
    availabilityZone: "us-west-2a",
    cidrBlock: "10.0.32.0/20",
    mapPublicIpOnLaunch: true,
    privateDnsHostnameTypeOnLaunch: "ip-name",
    tags: {
        Name: "vpc-thor-public-1",
        SubnetType: "Public",
        test: "I LOVE PULUMI"
    },
    vpcId: vpc_thor_vpc_abcdef0123456789.id,
});

// ...
```

{{% /choosable %}}

Now try running `pulumi up` again. This time it should detect and deploy our change.

```shell
$ pulumi up

Updating (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/troy-pulumi-corp/no-more-clickops/dev/updates/2

     Type                 Name                                        Status              Info
     pulumi:pulumi:Stack  no-more-clickops-dev
 ~   ├─ aws:ec2:Vpc       vpc-thor-vpc-abcdef0123456789              updated (2s)        [diff: ~tags,tag
 ~   └─ aws:ec2:Subnet    vpc-thor-public-1-subnet-abcdef0123456789  updated (0.91s)     [diff: ~tags,tag

Resources:
    ~ 2 updated
    16 unchanged

Duration: 6s
```

We can verify that by looking at the VPC through the AWS CLI tool.

First get the ID of the VPC. You can find this by running `pulumi stack -i` to show all the resources under management and their IDs:

```shell
$ pulumi stack -i

...
Current stack resources (21):
    TYPE                                        NAME
    pulumi:pulumi:Stack                         no-more-clickops-dev
    ├─ aws:ec2/vpc:Vpc                          vpc-thor-vpc-abcdef0123456789
    │     ID: vpc-abcdef0123456789

...
```

Then run `describe-vpcs` with the `--vpc-ids` option to only show that particular VPC:

```shell
aws ec2 describe-vpcs --vpc-ids=vpc-abcdef0123456789
```

If all went well you should see output like:

```shell
...
|||+-------------------+-------------------------------+|||
|||                        Tags                         |||
||+----------------+------------------------------------+||
|||       Key      |               Value                |||
||+----------------+------------------------------------+||
|||  test          |  I LOVE PULUMI                     |||
|||  Name          |  vpc-thor                          |||
||+----------------+------------------------------------+||
```

Alright, so to review, we used the Python [Boto][boto-lib] library to create a list of resources we wanted to bring under management by Pulumi. Then, we used the `pulumi import` command to import those resources and convert them to a Pulumi program in a standard programming language. This blog shows Python and TypeScript, but we could have just as easily done that in Go, C#, or any other of the many languages that Pulumi supports.

## Next Steps

If you haven't already, [install Pulumi][pulumi-install] today, and follow our self-directed [Getting Started guides][pulumi-start] to learn more about making the most of Pulumi's next-level infrastructure management features at your organization.

To learn more, you can watch the following video which provides a high level overview of how Pulumi works:

<div class="rounded-md shadow border border-gray-300 w-3/4 mx-auto my-4" style="position: relative; padding-bottom: 40.25%; height: 0; overflow: hidden;">
    <iframe
        src="//www.youtube.com/embed/Q8tw6YTD3ac?rel=0"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;"
        allowfullscreen=""
        title="Introduction to Pulumi in Three Minutes"
        srcdoc="<style>*{padding:0;margin:0;overflow:hidden}html,body{height:100%}img{position:absolute;width:100%;top:0;bottom:0;margin:auto}</style><a href=https://www.youtube.com/embed/Q8tw6YTD3ac?autoplay=1><img src='/images/home/youtube-getting-started.png' alt='Introduction to Pulumi in Three Minutes'></a>">
    </iframe>
</div>

## Pulumi Cloud

The Pulumi Cloud is a fully managed service that helps you adopt Pulumi’s open source SDK with ease. It provides built-in state and secrets management, integrates with source control and CI/CD, and offers a web console and API that make it easier to visualize and manage infrastructure. It is free for individual use, with features available for teams.

<a class="btn btn-secondary" href="https://app.pulumi.com/signup" target="_blank">Create an Account</a>

[install-jq]: https://jqlang.github.io/jq/download/
[boto-lib]: https://pypi.org/project/boto/
[pulumi-import-aws-account-scraper]: https://github.com/pulumi/pulumi-import-aws-account-scraper
[pulumi-install]: https://www.pulumi.com/docs/install/
[pulumi-start]: https://www.pulumi.com/start
