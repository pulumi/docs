---
title: "Creating Resources on Google Cloud"
title_tag: "Creating Resources on Google Cloud"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Learn how to define and provision resources on Google Cloud using Pulumi.

# A similar description used for search results and social-media previews.
meta_desc: Learn how to define and provision resources on Google Cloud using Pulumi.

# An image for the tutorial. It appears on tutorial page and in social-media previews.
meta_image: create-resources-gcp-meta.png

# An optional video for the tutorial. When present, it appears at the top of the page, replacing
# the meta image. YouTube and HTML5 video sources are supported.
# video:
#     url: /blog/drift-detection/drift.mp4
#     youtube: Q8tw6YTD3ac

# The order in which the tutorial appears in most lists. Order is ascending, so higher numbers
# mean the tutorial will appear further down the list. Positive integers only.
weight: 999

# A brief summary of the tutorial. It appears at the top of the tutorial page. Markdown is fine.
summary: |
   In Pulumi, resources represent the fundamental units that make up your infrastructure, such as virtual machines, networks, storage, and databases. A resource is used to define and manage an infrastructure object in your Pulumi configuration.
   In this tutorial, you will create a simple static website hosted on an Google Cloud virtual instance. You will then refer to documentation in the Pulumi Registry to configure the storage account as a website.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to create a new resource
    - How to reference resource definitions in the Pulumi documentation

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)
    - A [Google Cloud account](https://cloud.google.com/cloud-console)
    - The [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)
    - Familiarity with one of [Pulumi's supported languages](/docs/iac/languages-sdks/)

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 10

# # An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
collections:
    - gcp
---

## Create a new project

To start, [login to the Pulumi CLI](/tutorials/cli-authentication/) and [ensure it is configured to use your Google Cloud account](/docs/iac/get-started/gcp/begin/#configure-pulumi-to-access-your-google-cloud-account). Next, [create a new project and stack](/docs/iac/get-started/gcp/create-project/).

```bash
# Example using Python
$ mkdir pulumi-tutorial-gcp
$ cd pulumi-tutorial-gcp
$ pulumi new gcp-python
```

Then use the following code snippet to scaffold your project with the required imports and overall program structure that you will fill in as you go along, making sure to replace the value of `project` with the name/ID of your own Google Cloud project:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="gcp-simple-webserver" language="javascript" from="1" to="27" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="javascript" from="68" to="71" >}}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="gcp-simple-webserver" language="typescript" from="1" to="26" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="typescript" from="67" to="70" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="gcp-simple-webserver" language="python" from="1" to="26" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="python" from="63" to="68" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="gcp-simple-webserver" language="go" from="1" to="39" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="go" from="92" to="100" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="gcp-simple-webserver" language="csharp" from="1" to="32" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="csharp" from="93" to="100" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="gcp-simple-webserver" language="yaml" from="1" to="26" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="yaml" from="59" to="62" >}}
```

{{% /choosable %}}

The above code creates the following on your behalf:

- A VPC network
- An IP address
- An output of the web server's URL

## Create a virtual machine

The first resource you will create will be virtual machine that will host the web server. The specific details of how to create your virtual machine differ by cloud provider. In the case of Google Cloud, you will be creating a [virtual machine instance](https://cloud.google.com/compute/docs/instances). The [Pulumi Registry](/registry/) provides the documentation for all of the Pulumi providers and their associated resources. Open the [gcp.compute.Instance documentation page](/registry/packages/gcp/api-docs/compute/instance/) to view a description of this resource, example usage, the resource definition, and supported properties. You will now define your instance resource as shown below:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="gcp-simple-webserver" language="javascript" from="1" to="23" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="javascript" from="29" to="55" >}}
// TO-DO

{{< example-program-snippet path="gcp-simple-webserver" language="javascript" from="68" to="71" >}}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="gcp-simple-webserver" language="typescript" from="1" to="22" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="typescript" from="28" to="54" >}}
// TO- DO

{{< example-program-snippet path="gcp-simple-webserver" language="typescript" from="67" to="70" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="gcp-simple-webserver" language="python" from="1" to="22" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="python" from="28" to="51" >}}
# TO-DO

{{< example-program-snippet path="gcp-simple-webserver" language="python" from="63" to="68" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="gcp-simple-webserver" language="go" from="1" to="35" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="go" from="41" to="72" >}}
        // TO-DO

{{< example-program-snippet path="gcp-simple-webserver" language="go" from="92" to="100" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="gcp-simple-webserver" language="csharp" from="1" to="28" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="csharp" from="34" to="71" >}}
    // TO-DO

{{< example-program-snippet path="gcp-simple-webserver" language="csharp" from="95" to="100" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="gcp-simple-webserver" language="yaml" from="1" to="22" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="yaml" from="28" to="49" >}}
  # TO-DO

{{< example-program-snippet path="gcp-simple-webserver" language="yaml" from="59" to="62" >}}
```

{{% /choosable %}}

All resources have a required [`name`](https://www.pulumi.com/docs/concepts/resources/names/) argument. Each resource has both a [logical name](https://www.pulumi.com/docs/concepts/resources/names/#logicalname) and a [physical name](https://www.pulumi.com/docs/concepts/resources/names/#autonaming). The **logical name** is how the resource is known inside Pulumi. This is the value provided to the required `name` argument. The **physical name** is the name used for the resource in the cloud provider that a Pulumi program is deploying to. It is a combination of the logical name plus a random suffix which helps to prevent resource naming collisions.

In the above example, the logical name for our `instance` resource is **"website-server"**, and the physical name might typically look something like **"website-server-d7c2fa0"**.

In addition to names, resources have properties and options.

**Properties** are used to specify what type of resource to create. Properties are often resource-specific, and they can be required or optional depending on the specifications of the provider.

Some of the properties inside of your `gcp.compute.Instance` resource include:

| Property | Description |
|--------------|-------------|
| **machine type** | tells the Google Cloud provider what type of machine to create |
| **boot disk** | tells the provider the configuration for the instance's boot disk |
| **network interfaces** | tells the provider what networks to attach to the instance |

**Options** let you control certain aspects of a resource (such as showing explicit dependencies or importing existing infrastructure). You do not have any options defined for this resource, but you can learn more about how it works in the [Resource options documentation](/docs/iac/concepts/options/).

## Deploy your resources

Now run the `pulumi up` command to preview and deploy the resouces you've just defined in your project.

```bash
$ pulumi up -y

Previewing update (web-server)

     Type                     Name                Plan
 +   pulumi:pulumi:Stack      gcp-web-server      create
 +   ├─ gcp:compute:Network   vpc-network         create
 +   ├─ gcp:compute:Address   ip-address          create
 +   └─ gcp:compute:Instance  webserver-instance  create

Outputs:
    instanceURL: output<string>

Resources:
    + 4 to create

Updating (web-server)

     Type                     Name                Status
 +   pulumi:pulumi:Stack      gcp-web-server      created (73s)
 +   ├─ gcp:compute:Address   ip-address          created (3s)
 +   ├─ gcp:compute:Network   vpc-network         created (53s)
 +   └─ gcp:compute:Instance  webserver-instance  created (15s)

Outputs:
    instanceURL: "http://34.171.149.220"

Resources:
    + 4 created

Duration: 1m15s
```

The public IP address of your instance has been provided for you as an output, and you can use this to access your web server. However, if you try to visit this address, your request will eventually time out. This is because you have not yet configured web traffic access for your instance. You will do this by creating your firewall resource.

## Create a firewall

In this section, you will use Pulumi documentation to configure the firewall on your own. The firewall must allow web traffic on port 80 in order for you to access your web server. Use the following steps as a guide for adding the firewall resource:

- Navigate to the [Google Cloud Registry documentation page](/registry/packages/gcp/)
- Search for the `gcp.compute.Firewall` resource
- Define the firewall resource in your project code
- Configure the firewall to allow traffic on port 80
- Preview and deploy your updated project code

Once you have completed these steps, navigate to your instance IP address again. You should now be greeted with a "Hello world!" home page message that indicates your web server is running and publically accessible.

### View complete solution

You can view the complete project code below:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="gcp-simple-webserver" language="javascript" from="1" to="23" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="javascript" from="29" to="71" >}}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="gcp-simple-webserver" language="typescript" from="1" to="22" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="typescript" from="28" to="70" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="gcp-simple-webserver" language="python" from="1" to="22" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="python" from="28" to="68" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="gcp-simple-webserver" language="go" from="1" to="35" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="go" from="41" to="100" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="gcp-simple-webserver" language="csharp" from="1" to="28" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="csharp" from="34" to="100" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="gcp-simple-webserver" language="yaml" from="1" to="22" >}}

{{< example-program-snippet path="gcp-simple-webserver" language="yaml" from="28" to="62" >}}
```

{{% /choosable %}}

## Clean up

{{< cleanup >}}

## Next steps

In this tutorial, you create a virtual machine instance configured as a web server, and you created a firewall resource configured for public web access by referencing the Pulumi Registry. You also reviewed resource properties and example usage of various resources.

To learn more about creating resources in Pulumi, take a look at the following resources:

- Learn more about stack outputs and references in the [Stack Outputs and References](/tutorials/stack-outputs-and-references/) tutorial.
- Learn more about inputs and outputs in the [Inputs and Outputs](/docs/concepts/inputs-outputs/) documentation.
- Learn more about [resource names](/docs/concepts/resources/names/), [options](/docs/concepts/options/), and [providers](/docs/concepts/resources/providers/) in the Pulumi documentation.
