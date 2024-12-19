---
title: "Creating Resources on AWS"
title_tag: "Creating Resources on AWS"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Learn how to define and provision resources on AWS using Pulumi.

# A similar description used for search results and social-media previews.
meta_desc: Learn how to define and provision resources on AWS using Pulumi.

# # An image for the tutorial. It appears on tutorial page and in social-media previews.
# meta_image: meta.png

# An optional video for the tutorial. When present, it appears at the top of the page, replacing
# the meta image. YouTube and HTML5 video sources are supported.
video:
    youtube: Q1pL30ifeZ8

# The order in which the tutorial appears in most lists. Order is ascending, so higher numbers
# mean the tutorial will appear further down the list. Positive integers only.
weight: 999

# A brief summary of the tutorial. It appears at the top of the tutorial page. Markdown is fine.
summary: |
   In Pulumi, resources represent the fundamental units that make up your infrastructure, such as virtual machines, networks, storage, and databases. A resource is used to define and manage an infrastructure object in your Pulumi configuration.

   In this tutorial, you will create a simple Nginx web server. You will then refer to documentation in the Pulumi Registry to create a security group resource to make the server publicly accessible.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to create a new resource
    - How to update an existing resource
    - How to reference resource definitions in the Pulumi documentation

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)
    - The [Pulumi CLI](/docs/install/)
    - An [Amazon Web Services](https://aws.amazon.com/) account
    - The [AWS CLI](https://aws.amazon.com/cli/)
    - "[Node.js](/docs/languages-sdks/javascript/) or [Python](/docs/languages-sdks/python/) installed"

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 10

# # An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
collections:
    - aws

aliases:
  - /docs/using-pulumi/define-and-provision-resources/
  - /tutorials/define-and-provision-resources/
  - /tutorials/pulumi-fundamentals/configure-and-provision/
---

## Create a virtual machine

The first step is to create a virtual machine resource that will be used to host the web server. The specific details of how to create your virtual machine differ by cloud provider. For the purposes of this tutorial, you will be creating your resources on AWS in the `us-east-1` region.

### Amazon Elastic Compute Cloud (EC2)

Amazon Elastic Compute Cloud (EC2) provides managed virtual server hosting that makes it straightforward to run applications in your AWS account. In AWS, a virtual server is referred to as an "instance". These instances can host a variety of operating systems, tools, and applications, each configured according to your specific requirements.

#### Create a new project

{{< tutorials/create-new-proj >}}

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="typescript" from="1" to="2" >}}

{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="typescript" from="25" to="25" >}}

{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="typescript" from="12" to="12" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="python" from="1" to="2" >}}

{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="python" from="22" to="22" >}}

{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="python" from="13" to="13" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="yaml" from="1" to="3" >}}

{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="yaml" from="18" to="18" >}}

{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="yaml" from="6" to="6" >}}
```

{{% /choosable %}}

### Define an EC2 instance

The Pulumi Registry provides the documentation for all of the Pulumi providers and their associated resources. Open the [`aws.ec2.Instance` documentation page](https://www.pulumi.com/registry/packages/aws/api-docs/ec2/instance/) to view a description of this resource, example usage, the resource definition, and supported properties.

You will now define your EC2 instance resource below.

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="typescript" from="1" to="10" >}}

{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="typescript" from="23" to="29" >}}
{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="typescript" from="31" to="33" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="python" from="1" to="11" >}}

{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="python" from="22" to="27" >}}
{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="python" from="29" to="31" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="yaml" from="1" to="5" >}}
{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="yaml" from="18" to="30" >}}

{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="yaml" from="34" to="35" >}}
```

{{% /choosable %}}

{{< notes type="warning" >}}
If you are deploying resources in a region other than the `us-east-1` region, make sure to replace the AMI ID value with the ID that is [specific to your region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html). Otherwise you may run into an `InvalidAMIID.NotFound` error.
{{< /notes >}}

All resources have a required [`name`](https://www.pulumi.com/docs/concepts/resources/names/) argument. Each resource has both a [logical name](https://www.pulumi.com/docs/concepts/resources/names/#logicalname) and a [physical name](https://www.pulumi.com/docs/concepts/resources/names/#autonaming).

The logical name is how the resource is known inside Pulumi. This is the value provided to the required `name` argument.

The physical name is the name used for the resource in the cloud provider that a Pulumi program is deploying to. It is a combination of the logical name plus a random suffix which helps to prevent resource naming collisions.

In the above example, the logical name for your `aws.ec2.Instance` resource is **"webserver-www"**, and the physical name might typically look something like **"webserver-www-d7c2fa0"**.

In addition to names, resources have properties and options.

**Properties** are used to specify what type of resource to create. Properties are often resource-specific, and they can be required or optional depending on the specifications of the provider.

The properties inside your `aws.ec2.Instance` resource are:

| Property | Description |
|--------------|-------------|
| **instance_type** | tells the AWS provider to create an EC2 instance of type/size `t2.micro` |
| **ami** | tells the provider to create the instance using the `ami-09538990a0c4fe9be` machine image |
| **user_data** | tells the provider to initialize the instance with the script you have defined |

**Options** let you control certain aspects of a resource (such as showing explicit dependencies or importing existing infrastructure). You do not have any options defined for this resource, but you can learn more about options in the [Pulumi documentation](/docs/concepts/options).

### Deploy your EC2 instance

Now let's run the `pulumi up` command to preview and deploy the resource you just defined in your project.

```bash
Previewing update (webserver-dev):

     Type                      Name                     Plan
 +   pulumi:pulumi:Stack       myproject-webserver-dev  create
 +   └─ aws:ec2:Instance       webserver-www            create

Resources:
    + 2 to create

Do you want to perform this update? yes
Updating (webserver-dev):

     Type                      Name                     Status
 +   pulumi:pulumi:Stack       myproject-webserver-dev  created
 +   └─ aws:ec2:Instance       webserver-www            created

Outputs:
    publicIp      : "34.217.110.29"

Resources:
    + 2 created

Duration: 17s
```

The public IP address of your instance has been provided for you as an output, and you can use this to access your web server. However, if you try to visit this address, your request will eventually time out. This is because you have not yet configured web traffic access for your instance. You will do this by creating your security group resource.

## Create a security group

In this section, you will use Pulumi documentation to configure the security group on your own. The security group must allow web traffic on port 80 in order for you to access your web server. An updated version of the project code has been provided below as a starting point.

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="typescript" from="1" to="12" >}}
const securityGroup = // TO-DO

{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="typescript" from="23" to="31" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="python" from="1" to="13" >}}
security_group = # TO-DO

{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="python" from="22" to="31" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="yaml" from="1" to="7" >}}
    # TO-DO

{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="yaml" from="18" to="35" >}}
```

{{% /choosable %}}

You may have noticed that the placeholder code for the security group resource has been moved above the code for the EC2 instance resource. This was done intentionally to accommodate for variable declaration and usage order in your code.

If you place the security group resource definition after the EC2 instance and try to deploy your program, it will fail. This is because the security group variable must be declared before you can tell your EC2 instance resource to use it.

Use the following steps as a guide for adding the Security Group resource:

- Navigate to the [AWS Registry documentation page](https://www.pulumi.com/registry/packages/aws/)
- Search for the EC2 Security Group resource
- Define the EC2 Security Group resource in your project code
- Configure the security group to allow traffic on port 80
- Update the EC2 instance resource to use the security group
- Preview and deploy your updated project code

Once you have completed these steps, navigate to your instance IP address again. You should now be greeted with a "Welcome to nginx!" home page message that indicates your web server is running and publically accessible.

{{< notes type="info" >}}
If your web server is still timing out, make sure you are accessing your web server's IP address via HTTP and not HTTPS.
{{< /notes >}}

{{< details "Click here to view the complete project code" >}}

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="typescript" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="python" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="aws-ec2-sg-nginx-server" language="yaml" >}}
```

{{% /choosable %}}

{{< /details >}}

## Clean up

{{< cleanup >}}

## Next steps

In this tutorial, you made an EC2 instance configured as an Nginx webserver and made it publicly available by referencing the Pulumi Registry to define the security group. You also reviewed resource properties and example usage.

To learn more about creating resources in Pulumi, take a look at the following resources:

- Learn more about stack outputs and references in the [Reference AWS Resources Across Stacks tutorial](/tutorials/stack-outputs-refs-aws/) tutorial.
- Learn more about inputs and outputs in the [Inputs and Outputs](/docs/concepts/inputs-outputs/) documentation.
- Learn more about [resource names](/docs/concepts/resources/names/), [options](/docs/concepts/options/), and [providers](/docs/concepts/resources/providers/) in the Pulumi documentation.
