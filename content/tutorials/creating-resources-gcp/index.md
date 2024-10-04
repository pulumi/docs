---
title: "Create Resources on Google Cloud"
title_tag: "Create Resources on Google Cloud"
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
   In this tutorial, you will create a simple static website hosted on an Azure Blob Storage account. You will then refer to documentation in the Pulumi Registry to configure the storage account as a website.

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
# collections:
#     - some-non-existent-collection
---

## Create a new project

To start, [login to the Pulumi CLI](/tutorials/cli-authentication/) and [ensure it is configured to use your Google Cloud account](/docs/iac/get-started/gcp/begin/#configure-pulumi-to-access-your-google-cloud-account). Next, [create a new project and stack](/docs/iac/get-started/gcp/create-project/).

```bash
# Example using Python
$ mkdir pulumi-tutorial-gcp
$ cd pulumi-tutorial-gcp
$ pulumi new gcp-python
```

Then use the following code snippet to scaffold your project with the required imports and overall program structure that you will fill in as you go along:

TBD

Next, run the following commands to set your Google Cloud project, region, and zone, making sure to replace `<your-gcp-project-id>` with the ID of your project:

```bash
$ pulumi config set gcp:project <your-gcp-project-id>
$ pulumi config set gcp:region us-east1
$ pulumi config set gcp:zone us-east1-a
```

## Create a VPC network

TBD

## Deploy your resources

Now run the `pulumi up` command to preview and deploy the resouces you've just defined in your project.

```bash
$ pulumi up -y
TBD
```

The public IP address of your instance has been provided for you as an output, and you can use this to access your web server. However, if you try to visit this address, your request will eventually time out. This is because you have not yet configured web traffic access for your instance. You will do this by creating your firewall resource.

## Create a firewall

In this section, you will use Pulumi documentation to configure the firewall on your own. The firewall must allow web traffic on port 80 in order for you to access your web server. An updated version of the project code has been provided below as a starting point.

TBD

Use the following steps as a guide for adding the Security Group resource:

Navigate to the AWS Registry documentation page
Search for the EC2 Security Group resource
Define the EC2 Security Group resource in your project code
Configure the security group to allow traffic on port 80
Update the EC2 instance resource to use the security group
Preview and deploy your updated project code

Once you have completed these steps, navigate to your instance IP address again. You should now be greeted with a “Welcome to nginx!” home page message that indicates your web server is running and publically accessible.

### View complete solution

You can view the complete project code below:

TBD

## Clean up

{{< cleanup >}}

## Next steps

In this tutorial, you made a resource group and a storage account, and you configured your storage account as a static website by referencing the Pulumi Registry. You also reviewed resource properties and example usage of various resources.

To learn more about creating resources in Pulumi, take a look at the following resources:

- Learn more about stack outputs and references in the [Stack Outputs and References](/tutorials/stack-outputs-and-references/) tutorial.
- Learn more about inputs and outputs in the [Inputs and Outputs](/docs/concepts/inputs-outputs/) documentation.
- Learn more about [resource names](/docs/concepts/resources/names/), [options](/docs/concepts/options/), and [providers](/docs/concepts/resources/providers/) in the Pulumi documentation.
