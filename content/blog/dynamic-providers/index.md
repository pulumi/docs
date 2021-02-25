---
title: "Dynamic Providers"
date: 2020-01-16
meta_desc: "Pulumi Dynamic Providers manage resources that are not covered in pre-built providers"
meta_image: meta.png
authors:
    - praneet-loke
tags:
    - providers
    - resources
---

Pulumi has many resource providers that allow you to interact with your favorite cloud or resource. There are times when a provider may not deliver on the specific task that you want to accomplish. Dynamic Providers can be a powerful tool to help accomplish your infrastructure tasks.

<!--more-->

A provider manages the CRUD (Create, Read, Update, Delete) life-cycle of a resource against some underlying service. The underlying service can be one of the public clouds or an on-premise service. For example, AWS, Azure, GCP, and Kubernetes have resource providers, which can manage resources by request.

## Resource Provider

A resource provider is made up of two different pieces:

1. A resource plugin, which is the binary used by the deployment engine to manage a resource. These plugins are stored in the plugin cache (located in `~/.pulumi/plugins`) and can be managed using the [`pulumi plugin`](https://www.pulumi.com/docs/reference/cli/pulumi_plugin/) set of commands.

1. An SDK which provides bindings for each type of resource the provider can manage.

![How Pulumi works](./engine-block-diagram.png)

A resource provider is an extension of the API exposed by the respective cloud providers. As such, it can be the limiting factor. Thankfully, there is a solution to this. Since the Pulumi engine works with life-cycle callbacks handing control to the provider at appropriate times, it is easy to write a provider that implements custom logic in those callbacks.

Learn more about how Pulumi works [here](https://www.pulumi.com/docs/intro/concepts/how-pulumi-works/).

## Dynamic Resource Provider

> **Note**: Dynamic providers are currently only supported in JavaScript, TypeScript, and Python.

Pulumi provides appropriate life-cycle callbacks through the `pulumi.dynamic.ResourceProvider` abstract class. While Pulumi does not know what sort of resources a Dynamic Provider will create, the life-cycle hooks must return data in specific formats, which Pulumi uses to call the appropriate callbacks.

For example, if the user changes an input property to your dynamic resource, the `diff` hook will be called with both the old (if applicable) and new inputs. You can compare then to see which input properties have changed and give hints to Pulumi as to whether `delete` should be called or whether to call the `update` hook.

> The `check` life-cycle hook will be called before any other hook to let you validate the inputs and populate defaults, if necessary.

When a dynamic resource instance updates, the `delete` hook will be called to allow you to perform any necessary cleanups before the dynamic resource is removed from your stack’s state.

### Provider Credentials

If you need to use the credentials used by the rest of your Pulumi app, also known as the ambient provider credentials, you can access the relevant credentials (and other configuration) through the `<provider>.config` where `provider` is the imported provider module.

## Sample Use Cases

Dynamic providers can be used for almost any task. Since Pulumi uses general-purpose programming languages, you can do almost anything you would outside of your infrastructure app. You can even use libraries that are standard to the respective programming language.

Here are some use cases:

* Run a command-line tool when a dependent resource is created.
* Copy files to a VM once the VM is created.
* Call REST APIs in each life-cycle hook (CRUD) to adopt an external resource under the cloud resource model.

### Examples

#### Enable Azure Storage's Static Websites Feature

The Azure resource provider does not support enabling the [static website](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-static-website) feature for a storage account. However, there is a REST API that can be called to enable the feature, so we can easily call the API from within the dynamic provider.

[Here's](https://github.com/pulumi/examples/blob/master/azure-ts-static-website/staticWebsite.ts) the source for this example. The following is an excerpt from the [example](https://github.com/pulumi/examples/blob/master/azure-ts-static-website/index.ts) where the dynamic provider is actually used. Note that the Azure Storage Account is created before using this dynamic provider.

```ts
...
...
// Create a Storage Account for our static website
const storageAccount = new azure.storage.Account("websitesa", {
    resourceGroupName: resourceGroup.name,
    accountReplicationType: "LRS",
    accountTier: "Standard",
    accountKind: "StorageV2",
});

const staticWebsite = new StorageStaticWebsite("website-static", {
	accountName: storageAccount.name,
});
```

#### Add A Custom Domain To An Azure CDN endpoint

Similar to the previous example, this is another example of a shortcoming of the regular Azure resource provider available in Pulumi. However, due to the availability of a REST API, we can easily add a custom domain to an Azure CDN resource using a dynamic provider.

Along with adding a custom domain to the CDN endpoint, this dynamic provider also enables HTTPS provided by Azure's one-click [HTTPS enablement](https://docs.microsoft.com/en-us/azure/cdn/cdn-custom-ssl?tabs=option-1-default-enable-https-with-a-cdn-managed-certificate).

As before, details such as the creation of the CDN profile and its endpoint are omitted for clarity. You can check out the full example [here](https://github.com/pulumi/examples/tree/master/azure-ts-dynamicresource).

```ts
...
...
const cdnEndpoint = new azure.cdn.Endpoint("cdnEndpoint", {
    /**
     * Specify a well-known name for the endpoint name,
     * so you can add a CNAME record for your custom domain
     * pointing to this CDN endpoint to it.
     *
     * For example, the URL for this CDN endpoint when it is created
     * would be `my-cdn-endpoint.azureedge.net`.
     */
    name: "my-cdn-endpoint",
    resourceGroupName: resourceGroup.name,
    profileName: cdnProfile.name,
    isHttpsAllowed: true,
    isHttpAllowed: false,
    isCompressionEnabled: true,
    originHostHeader: storageAccount.primaryBlobHost,
    contentTypesToCompresses: [
        "text/plain",
        "text/html",
        "text/css",
        "text/javascript",
        "application/x-javascript",
        "application/javascript",
        "application/json",
        "application/xml",
        "image/png",
        "image/jpeg",
    ],
    origins: [
        {
            name: "cdn-origin",
            hostName: storageAccount.primaryBlobHost,
            httpsPort: 443,
        },
    ],
});

export const cdnCustomDomainResource = new CDNCustomDomainResource("cdnCustomDomain", {
        	resourceGroupName: resourceGroupName,
        	// Ensure that there is a CNAME record for mycompany.com
        	// pointing to my-cdn-endpoint.azureedge.net.
        	// You would do that in your domain registrar's portal.
        	customDomainHostName: "mycompany.com",
        	profileName: cdnProfileName,
        	endpointName: cdnEndpointName,
        	// This will enable HTTPS through Azure's one-click
        	// automated certificate deployment.
        	// The certificate is fully managed by Azure from provisioning
        	// to automatic renewal at no additional cost to you.
        	httpsEnabled: true,
    	}, { parent: cdnEndpoint });
```

#### Dynamic Providers As Provisioners

Provisioning a VM after it is created is a common problem. Developers have the option to run user-supplied scripts while creating the VM itself. For example, the AWS EC2 resource has a `userData` parameter, that allows you to specify an inline script, which EC2 will run at instance startup.

Scripts provided through the `userData` parameter can be configured to run every time the instance is restarted. But what if you wanted to run the script every time the _script_ changes? To do that you could use SCP to transfer the file and then execute the script on the VM. This [example](https://github.com/pulumi/examples/tree/master/aws-ts-ec2-provisioners) shows you how you can do that. Although the example uses TypeScript and is specific to AWS EC2, you can easily adapt this to other cloud providers.

This snippet of the code shows how, the dynamic resources for copying a file and executing it, are used:

```ts
...
...
const conn = {
	host: server.publicIp,
	username: "ec2-user",
	// The EC2 instance is created with the corresponding SSH public key.
	// Read more here: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html.
	privateKey,
	privateKeyPassphrase,
};

// Copy a config file from the local filesystem to the instance.
const cpConfig = new provisioners.CopyFile("config", {
	conn,
	src: "myapp.conf",
	dest: "myapp.conf",
}, { dependsOn: server });

// Execute a basic command on the instance.
const catConfig = new provisioners.RemoteExec("cat-config", {
	conn,
	command: "cat myapp.conf",
}, { dependsOn: cpConfig });
…
...
```

Read more about dynamic providers in our [docs]({{< relref "/docs/intro/concepts/resources#dynamicproviders" >}}). Let us know what cool dynamic providers you create by dropping us a note on our community [Slack](https://slack.pulumi.com/)!
