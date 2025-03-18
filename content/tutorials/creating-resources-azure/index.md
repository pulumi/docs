---
title: "Creating Resources on Azure"
title_tag: "Creating Resources on Azure"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Learn how to define and provision resources on Azure using Pulumi.

# A similar description used for search results and social-media previews.
meta_desc: Learn how to define and provision resources on Azure using Pulumi.

# An image for the tutorial. It appears on tutorial page and in social-media previews.
meta_image: create-resources-azure-meta.png

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

   In this tutorial, you will create a simple static website hosted on an Azure Blob Storage account. You will then refer to documentation in the Pulumi Registry to configure the storage account as a website.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to create a new resource
    - How to reference resource definitions in the Pulumi documentation

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)
    - An [Azure account](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account)
    - The [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
    - Familiarity with one of [Pulumi's supported languages](/docs/iac/languages-sdks/)

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 10

# # An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
collections:
    - azure
---

## Create a new project

To start, [login to the Pulumi CLI](/tutorials/cli-authentication/) and [ensure it is configured to use your Azure account](/docs/iac/get-started/azure/begin/#configure-pulumi-to-access-your-microsoft-azure-account). Next, [create a new project and stack](/docs/iac/get-started/azure/create-project/).

```bash
# Example using Python
$ mkdir pulumi-tutorial-azure
$ cd pulumi-tutorial-azure
$ pulumi new azure-python
```

Then use the following code snippet to scaffold your project with the required imports and overall program structure that you will fill in as you go along:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="azure-native-static-website" language="javascript" from="1" to="13" >}}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="azure-native-static-website" language="typescript" from="1" to="12" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="azure-native-static-website" language="python" from="1" to="12" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="azure-native-static-website" language="go" from="1" to="18" >}}
{{< example-program-snippet path="azure-native-static-website" language="go" from="75" to="76" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="azure-native-static-website" language="csharp" from="1" to="15" >}}
{{< example-program-snippet path="azure-native-static-website" language="csharp" from="69" to="69" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="azure-native-static-website" language="yaml" from="1" to="8" >}}
```

{{% /choosable %}}

{{< notes type="info" >}}

If you are deploying your resources using Pulumi Python, this tutorial will make use of the [Pulumi Synced Folder](/registry/packages/synced-folder/) package, so you will also need to make sure to [install this dependency into your project](https://github.com/pulumi/pulumi-synced-folder?tab=readme-ov-file#installing).

{{< /notes >}}

## Create a resource group

The first resource you will create will be an [Azure Resource Group](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal). Azure Resource Groups provide a logical container to organize and manage resources in your Azure account. In Azure, resources like virtual machines, storage accounts, and databases are grouped together within a resource group.

The [Pulumi Registry](/registry/) provides the documentation for all of the Pulumi providers and their associated resources. Open the [azure-native.resources.ResourceGroup documentation page](/registry/packages/azure-native/api-docs/resources/resourcegroup/) to view a description of this resource, example usage, the resource definition, and supported properties. You will now define your resource group resource as shown below:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="azure-native-static-website" language="javascript" from="1" to="8" >}}

{{< example-program-snippet path="azure-native-static-website" language="javascript" from="15" to="18" >}}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="azure-native-static-website" language="typescript" from="1" to="7" >}}

{{< example-program-snippet path="azure-native-static-website" language="typescript" from="14" to="17" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="azure-native-static-website" language="python" from="1" to="7" >}}

{{< example-program-snippet path="azure-native-static-website" language="python" from="14" to="17" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="azure-native-static-website" language="go" from="1" to="13" >}}

{{< example-program-snippet path="azure-native-static-website" language="go" from="20" to="26" >}}

{{< example-program-snippet path="azure-native-static-website" language="go" from="75" to="76" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="azure-native-static-website" language="csharp" from="1" to="10" >}}

{{< example-program-snippet path="azure-native-static-website" language="csharp" from="17" to="21" >}}

{{< example-program-snippet path="azure-native-static-website" language="csharp" from="69" to="69" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="azure-native-static-website" language="yaml" from="1" to="3" >}}

{{< example-program-snippet path="azure-native-static-website" language="yaml" from="10" to="15" >}}
```

{{% /choosable %}}

All resources have a required [`name`](https://www.pulumi.com/docs/concepts/resources/names/) argument. Each resource has both a [logical name](https://www.pulumi.com/docs/concepts/resources/names/#logicalname) and a [physical name](https://www.pulumi.com/docs/concepts/resources/names/#autonaming). The **logical name** is how the resource is known inside Pulumi. This is the value provided to the required `name` argument. The **physical name** is the name used for the resource in the cloud provider that a Pulumi program is deploying to. It is a combination of the logical name plus a random suffix which helps to prevent resource naming collisions.

In the above example, the logical name for our `ResourceGroup` resource is **"website-resource-group"**, and the physical name might typically look something like **"website-resource-group-d7c2fa0"**.

## Create a storage account

The next step will be to create an [Azure Blob Storage account](https://azure.microsoft.com/en-us/products/storage/blobs) that will be used to host the website. Once again, you can refer to the Pulumi registry, specificaly the [`azure-native.storage.StorageAccount` resource page](/registry/packages/azure-native/api-docs/storage/storageaccount/), to define your storage account as shown below:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="azure-native-static-website" language="javascript" from="1" to="8" >}}

{{< example-program-snippet path="azure-native-static-website" language="javascript" from="15" to="27" >}}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="azure-native-static-website" language="typescript" from="1" to="7" >}}

{{< example-program-snippet path="azure-native-static-website" language="typescript" from="14" to="26" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="azure-native-static-website" language="python" from="1" to="7" >}}

{{< example-program-snippet path="azure-native-static-website" language="python" from="14" to="27" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="azure-native-static-website" language="go" from="1" to="13" >}}

{{< example-program-snippet path="azure-native-static-website" language="go" from="20" to="38" >}}

{{< example-program-snippet path="azure-native-static-website" language="go" from="75" to="76" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="azure-native-static-website" language="csharp" from="1" to="10" >}}

{{< example-program-snippet path="azure-native-static-website" language="csharp" from="17" to="32" >}}

{{< example-program-snippet path="azure-native-static-website" language="csharp" from="69" to="69" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="azure-native-static-website" language="yaml" from="1" to="3" >}}

{{< example-program-snippet path="azure-native-static-website" language="yaml" from="10" to="23" >}}
```

{{% /choosable %}}

In addition to names, resources have properties and options. **Properties** are used to specify what type of resource to create. Properties are often resource-specific, and they can be required or optional depending on the specifications of the provider.

The properties inside your `StorageAccount` resource are:

| Property | Description |
|--------------|-------------|
| **resource group name** | tells the Azure Native what resource group to associate this resource with |
| **kind** | tells the provider the type of storage account to create, e.g. `StorageV2` |
| **sku** | tells the provider the SKU to use when creating the resource, e.g. `Standard_LRS` |

**Options** let you control certain aspects of a resource (such as showing explicit dependencies or importing existing infrastructure). We do not have any options defined for this resource, but you can learn more about options in the [Pulumi documentation](/docs/concepts/options).

## Deploy your storage account

Now run the `pulumi up` command to preview and deploy the resouces you've just defined in your project.

```bash
$ pulumi up -y
Previewing update (static-website)

     Type                                     Name                    Plan
 +   pulumi:pulumi:Stack                      azure-static-website    create
 +   ├─ azure-native:resources:ResourceGroup  website-resource-group  create
 +   └─ azure-native:storage:StorageAccount   websiteblob             create

Resources:
    + 3 to create

Updating (static-website)

     Type                                     Name                    Status
 +   pulumi:pulumi:Stack                      azure-static-website    created (39s)
 +   ├─ azure-native:resources:ResourceGroup  website-resource-group  created (4s)
 +   └─ azure-native:storage:StorageAccount   websiteblob             created (30s)

Resources:
    + 3 created

Duration: 41s
```

## Configure the static website

In this section, you will use the Pulumi documentation to configure the storage account as a static website on your own. To prepare for the configuration of the storage account, you will need to create a folder labeled `www` in your project. Inside this project, you will need to create an `index.html` file and an `error.html` file with the content as shown below.

Contents of the `index.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Hello, world!</title>
</head>
<body>
    <h1>Hello, world! 👋</h1>
    <p>Deployed with 💜 by <a href="https://pulumi.com/">Pulumi</a>.</p>
</body>
</html>
```

Content of the `error.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Page not found</title>
</head>
<body>
    Oops! That page wasn't found. Try our <a href="/">home page</a> instead.
</body>
</html>
```

An updated version of the project code has been provided below as a starting point:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="azure-native-static-website" language="javascript" from="1" to="8" >}}

{{< example-program-snippet path="azure-native-static-website" language="javascript" from="15" to="29" >}}
// TO-DO

{{< example-program-snippet path="azure-native-static-website" language="javascript" from="37" to="50" >}}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="azure-native-static-website" language="typescript" from="1" to="7" >}}

{{< example-program-snippet path="azure-native-static-website" language="typescript" from="14" to="28" >}}
// TO-DO

{{< example-program-snippet path="azure-native-static-website" language="typescript" from="36" to="49" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="azure-native-static-website" language="python" from="1" to="7" >}}

{{< example-program-snippet path="azure-native-static-website" language="python" from="14" to="29" >}}
# TO-DO

{{< example-program-snippet path="azure-native-static-website" language="python" from="38" to="48" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="azure-native-static-website" language="go" from="1" to="13" >}}

{{< example-program-snippet path="azure-native-static-website" language="go" from="20" to="40" >}}
        // TO-DO

{{< example-program-snippet path="azure-native-static-website" language="go" from="51" to="76" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="azure-native-static-website" language="csharp" from="1" to="10" >}}

{{< example-program-snippet path="azure-native-static-website" language="csharp" from="17" to="34" >}}
    // TO-DO

{{< example-program-snippet path="azure-native-static-website" language="csharp" from="43" to="69" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="azure-native-static-website" language="yaml" from="1" to="3" >}}

{{< example-program-snippet path="azure-native-static-website" language="yaml" from="10" to="25" >}}
  # TO-DO

{{< example-program-snippet path="azure-native-static-website" language="yaml" from="34" to="58" >}}
```

{{% /choosable %}}

Use the following steps as a guide for adding the storage :

- Navigate to the [Azure Native Registry](/registry/packages/azure-native/)
- Search for the `StorageAccountStaticWebsite` resource
- Define the `StorageAccountStaticWebsite` resource in your project code
- Preview and deploy your updated project code

The website URL has been provided for you as an output, and you can use this to access your static website once the deployment has completed. You should be greeted with a "Hello, world!" homepage message that indicates your static website has been successfully created.

### View complete solution

You can view the complete project code below:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="azure-native-static-website" language="javascript" from="1" to="8" >}}

{{< example-program-snippet path="azure-native-static-website" language="javascript" from="15" to="50" >}}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="azure-native-static-website" language="typescript" from="1" to="7" >}}

{{< example-program-snippet path="azure-native-static-website" language="typescript" from="14" to="49" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="azure-native-static-website" language="python" from="1" to="7" >}}

{{< example-program-snippet path="azure-native-static-website" language="python" from="14" to="48" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="azure-native-static-website" language="go" from="1" to="13" >}}

{{< example-program-snippet path="azure-native-static-website" language="go" from="20" to="76" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="azure-native-static-website" language="csharp" from="1" to="10" >}}

{{< example-program-snippet path="azure-native-static-website" language="csharp" from="17" to="69" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="azure-native-static-website" language="yaml" from="1" to="3" >}}

{{< example-program-snippet path="azure-native-static-website" language="yaml" from="10" to="58" >}}
```

{{% /choosable %}}

## Clean up

{{< cleanup >}}

## Next steps

In this tutorial, you made a resource group and a storage account, and you configured your storage account as a static website by referencing the Pulumi Registry. You also reviewed resource properties and example usage of various resources.

To learn more about creating resources in Pulumi, take a look at the following resources:

- Learn more about stack outputs and references in the [Reference AWS Resources Across Stacks tutorial](/tutorials/stack-outputs-refs-azure/) tutorial.
- Learn more about inputs and outputs in the [Inputs and Outputs](/docs/concepts/inputs-outputs/) documentation.
- Learn more about [resource names](/docs/concepts/resources/names/), [options](/docs/concepts/options/), and [providers](/docs/concepts/resources/providers/) in the Pulumi documentation.
