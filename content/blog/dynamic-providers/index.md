---
title: "Dynamic Providers"
date: 2019-12-20
meta_desc: "Pulumi dynamic providers manage resources that do not have prebuilt providers such as AWS, Azure, and GCP"
meta_image: meta.png
authors:
    - praneet-loke
tags:
    - providers
    - resources
---

Pulumi has several resource providers (over 45X!) that allow you to interact with your favorite cloud provider or resource using a programming language. But what if there isn’t a provider available for what you want to accomplish? That’s where dynamic providers can help you. They can be an extremely important part of your infrastructure app.

<!--more-->

A provider manages the CRUD lifecycle of a resource against some underlying service. The underlying service can be one of the public clouds or an on-premise service. For example, AWS, Azure, GCP, and Kubernetes are all resource providers, which can create/update/destroy resources in the respective clouds.

## _Dynamic_ Resource Provider

> **Note**: Dynamic providers are currently only supported in Javascript, Typescript, and Python.

Pulumi provides appropriate lifecycle callbacks through the `pulumi.dynamic.ResourceProvider` abstract class. While Pulumi does not know what sort of resources a dynamic provider will create, the lifecycle hooks must return data in specific formats, which Pulumi uses as hints to call the appropriate lifecycle hooks.

For example, if the user changes an input property to your dynamic resource, the `diff` hook will be called with both the old (if applicable) and new inputs. You can then compare to see which input properties have changed and give hints to Pulumi as to whether `delete` should be called or whether to call the `update` hook.

> The `check` lifecycle hook will be called before any other hook to let you validate the inputs and populate defaults, if necessary.

When a dynamic resource instance updates, the `delete` hook will be called to allow you to perform any necessary cleanups before the dynamic resource is removed from your stack’s state.

### Provider Serialization

It is important to note that once an instance of the dynamic resource is created, Pulumi serializes the provider and stores it in your [state](https://www.pulumi.com/docs/intro/concepts/state/#state) file. When you change the source code of your dynamic resource, the serialized version is updated.

## Use Cases

Dynamic providers can be used for almost any task. Here are some use cases:

Run a command-line tool when a dependent resource is created.
Copy files to a VM once the VM is created.
Call REST APIs in each lifecycle hook (CRUD) to adopt an external resource under the cloud resource model.

### Examples

#### Enable Azure Storage's Static Websites Feature

[Here's](https://github.com/pulumi/examples/blob/master/azure-ts-static-website/staticWebsite.ts) the source for this example. The following is an excerpt from the [example](https://github.com/pulumi/examples/blob/master/azure-ts-static-website/index.ts) where the dynamic provider is actually used. Note that the Azure Storage Account is created before using this dynamic provider.

```ts
const staticWebsite = new StorageStaticWebsite("website-static", {
	accountName: storageAccount.name,
});
```

#### Add A Custom Domain To An Azure CDN endpoint

Along with adding a custom domain to the CDN endpoint, this dynamic provider also enables HTTPS provided by Azure's one-click [HTTPS enablement](https://docs.microsoft.com/en-us/azure/cdn/cdn-custom-ssl?tabs=option-1-default-enable-https-with-a-cdn-managed-certificate).

As before, some of the details, such as the creation of the CDN profile and its endpoint are omitted here for brevity. You can check out the full example [here](https://github.com/pulumi/examples/tree/master/azure-ts-dynamicresource).

```ts
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

Scripts provided through the `userData` parameter run every time the instance is restarted. But what if you only want to run the script once? You could use SCP to transfer the file and then execute the script on the VM. This [example](https://github.com/pulumi/examples/tree/master/aws-ts-ec2-provisioners) does exactly that. Although the example uses TypeScript and is specific to AWS EC2, you can easily adapt this to other cloud providers.

This snippet of the code shows how the dynamic resources for copying a file and executing it are used:

```ts
…
…
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

Read more about dynamic providers in our [docs](https://www.pulumi.com/docs/intro/concepts/programming-model/#dynamicproviders). Let us know what cool dynamic providers you create by dropping us a note on our community [Slack](https://slack.pulumi.com/)!
