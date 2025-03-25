---
title: "Introducing: Support For Using Any Terraform Provider with Pulumi"
date: 2024-08-29T10:00:00-06:00
allow_long_title: true
meta_desc: "Pulumi now supports using any Terraform or OpenTofu provider with Pulumi,
  in just a few seconds"
meta_image: meta.png # TODO
authors:
  - luke-hoban
  - ian-wahbe
  - matt-jeffryes
tags:
  - terraform
  - features

social:
  twitter: "You can now use ANY Terraform Provider from Pulumi! The entire ecosystem
    of Terraform/OpenTofu providers is now available to Pulumi users. And all the
    benefits of Pulumi are available to partners and developers building their own
    Terraform Providers, with no extra work!"
  linkedin: |
    You can now use ANY Terraform Provider from Pulumi! 

    The entire ecosystem of Terraform/OpenTofu providers is now available to Pulumi users. And all the benefits of Pulumi are available to partners and developers building their own Terraform Providers, with no extra work!

    Check it out at https://www.pulumi.com/registry/packages/terraform-provider/ today.

search:
  keywords:
    - terraform
    - opentofu
    - provider
    - introducing
    - seconds
    - using
    - support
---

One of our core goals at Pulumi is to provide access to manage **any** cloud infrastructure with a single unified programming model.  Whether it’s multi-cloud (AWS+Azure+Kubernetes), hybrid cloud (GCP+VMWare+Cisco), or managed services (Databricks+GitHub+Cloudflare), Pulumi makes it easy to deploy and manage infrastructure across all of your cloud environments using any of the 150+ cloud providers in the Pulumi Registry.

We’re excited to take this even further by introducing support for using [_any_ Terraform or OpenTofu provider](https://www.pulumi.com/registry/packages/terraform-provider/) from within your Pulumi programs.  If there is a long tail Cloud or SaaS platform that has a provider for those ecosystems, it now works with Pulumi as well.  And if your organization has built your own custom Terraform or OpenTofu provider to support an internal cloud platform, you can use it from Pulumi as well, without having to publish it to any registry.

<!--more-->

Terraform providers are the closest thing the industry has today to a "defacto standard" for describing the resource model of a cloud platform. The vast majority of these providers are implemented by cloud providers, partners, or cloud ecosystem contributors - as a way to describe what resources are available in their platform that can be managed via various kinds of infrastructure tooling. These investments become even more impactful when the work done to define the resource model can be widely leveraged by other tools for a variety of purposes - from IaC to Policy to Asset Inventory and more. There is nothing innately Terraform-specific about these providers - they are simply a standard resource model and the implementation of CRUD (Create-Read-Update-Delete) operations against that model. 

At Pulumi, we've supported bridging Terraform providers for use in Pulumi from the beginning.  Pulumi's provider model is even more expressive than Terraform's and we have a defined way to [map Terraform providers](https://github.com/pulumi/pulumi-terraform-bridge) (as well as other provider ecosystems) into the Pulumi provider model to be used by Pulumi's CLI and deployment orchestration engine.  Many of the most used providers in the Pulumi ecosystem are bridged Terraform providers. However, until now, bridging a new provider required a decent amount of up front and ongoing work, to maintain a separate repository, build and push separate releases, and publish resulting SDKs to every language's package manager. This meant that while the largest and most used Terraform providers were available in Pulumi, the long tail of providers were not as easily accessible. With this launch, we are now opening up easy access to *all* of these providers.

Using any Terraform or OpenTofu provider takes just a few seconds using a single command:

```shell
$ pulumi package add terraform-provider <your-terraform-provider>
```

This is enabled by our new Local Packages feature, which lets you generate Pulumi Packages locally into your Pulumi project, instead of relying only on packages published to the Pulumi Registry.  Support for generating local packages is available for all Pulumi languages.

  {{< video title="Using Planetscale with Pulumi" src="anytfplanetscale.mp4" autoplay="true" loop="true" >}}

Local packages are available as a convenient alternative to the existing support for authoring Native or Bridged Pulumi Packages. You can read more about all of the options available to authoring and using Pulumi Packages in the [Pulumi Packages documentation](https://www.pulumi.com/docs/iac/packages-and-automation/pulumi-packages/debugging-provider-packages/), or about how to generate a local package for a Terraform or OpenTofu provider in the [Any Terraform Provider](https://www.pulumi.com/registry/packages/terraform-provider/) docs.

## Walkthrough

Imagine you are working on a new cloud infrastructure project, and come across a technology you want to adopt, but don’t yet see a Pulumi provider in the Pulumi Registry.  What do you do?

Let’s walk through a concrete example.  We’ll work with a Python project:

```shell
$ pulumi new python
```

[Planetscale](https://planetscale.com/) is an exciting new fully-managed MySQL database platform. Although there isn’t yet an official Pulumi provider for Planetscale in the Pulumi Registry, we can easily use Planetscale from Pulumi if we want to.  First, we generate a local package using the `pulumi package add` command.

```shell
$ pulumi package add terraform-provider planetscale/planetscale
Successfully generated a Python SDK for the planetscale package at /Users/lukehoban/github/lukehoban/anytftest/sdks/planetscale

To use this SDK in your Python project, run the following command:

  echo sdks/planetscale >> requirements.txt

  pulumi install

You can then import the SDK in your Python code with:

  import pulumi_planetscale as planetscale
```

We ask to use the `terraform-provider` package, which implements support for any Terraform or OpenTofu provider, and then ask specifically for support for the `planetscale/planetscale` provider.  By default, this is pulled from the OpenTofu registry, but you can also specify a local path to the provider, or a fully-qualified reference to any Terraform Registry API-compatible server.

As we see from the output, this generates a local `./sdks/planetscale` folder with a Python SDK for using the Planetscale provider. 

After running the two commands provided in the output, we now have the local SDK incorporated into our project:

```shell
$ echo sdks/planetscale >> requirements.txt
$ pulumi install
```

We can add some code that uses this new SDK:

```python
import pulumi
import pulumi_planetscale as planetscale

db = planetscale.Database(
    resource_name="mydb", 
    organization="lukehoban", 
    cluster_size="PS-10"
)

pulumi.export("db_url", db.url)
```

We get strong typing, completion lists, and error reporting over this SDK from within our IDE.

Finally, we can deploy our code, deploying a new Planetscale database directly from Pulumi:

```shell
$ pulumi up
Updating (luke-pulumi-corp/dev2)

View in Browser (Ctrl+O): https://app.pulumi.com/luke-pulumi-corp/anytftest/dev2/updates/2

     Type                           Name            Status           
     pulumi:pulumi:Stack            anytftest-dev2                   
 +   └─ planetscale:index:Database  mydb            created (1s)     

Outputs:
  + db_url: "https://api.planetscale.com/v1/organizations/lukehoban/databases/mydb-77af236"

Resources:
    + 1 created
    1 unchanged

Duration: 3s
```

Clicking on the link, we see our new managed database ready for connections!  Within just a few seconds, we’ve incorporated support for this new service into our Pulumi infrastructure!

Planetscale is an exciting example, but it is just one of thousands of 3rd party (published in a public registry) and 2nd party (published internally within an organization) providers that are now available for use within Pulumi.

## Why Support All Terraform Providers?

Pulumi has a rich and expressive Native Provider model for building providers directly against the full capabilities of the Pulumi Infrastructure as Code resource model.  Many of the most important Pulumi providers are built directly on this foundation, including our [Azure Native](https://www.pulumi.com/registry/packages/azure-native/) and [Kubernetes](https://www.pulumi.com/registry/packages/kubernetes/) providers.  So why are we excited to support using Terraform and OpenTofu providers from Pulumi?

In short, we believe in giving Pulumi users access to every ecosystem of great providers and components available across the industry and in meeting partners where they are.  If a partner or user has built something exciting for managing infrastructure in the cloud, we want Pulumi users to benefit from it. Similarly, we want the partner or user to easily extend the value of their provider to also be able to reach the Pulumi user base, and all of the benefits that Pulumi can offer for Infrastructure as Code management, with no extra effort on their part.

We’ve embraced this approach in many other areas as well:

* Pulumi enables deploying and managing the lifecycle of any [Kubernetes YAML](https://kubernetes.io/docs/concepts/overview/working-with-objects/) file or [Helm Chart](https://helm.sh/). There’s a great ecosystem and library of Helm charts, and we make those all available to Pulumi users without any wrappers or indirections.
* We introduced the [Pulumi AWS CDK Adapter](https://www.pulumi.com/blog/aws-cdk-on-pulumi/) to enable Pulumi users to incorporate AWS CDK constructs directly into their Pulumi programs without rewriting in Pulumi first.
* And, of course, Pulumi offers features for deploying and managing [Azure Resource Manager templates](https://www.pulumi.com/registry/packages/azure-native/api-docs/resources/deploymentatscope/) and [CloudFormation templates](https://www.pulumi.com/registry/packages/aws/api-docs/cloudformation/stack/), enabling easy deployment of existing cloud provider IaC artifacts.

With the new support for Any Terraform Provider, we’re bringing this same experience to the Terraform and OpenTofu provider ecosystems.

## How Does This Work?

Two new technologies in the Pulumi open source project underpin support for using any Terraform or OpenTofu provider.

**Parameterized Providers** offer support for building a single provider that can implement many different “flavors.” For example, the `terraform-provider` provider can be parameterized to provide support for any Terraform or OpenTofu provider.

**Local Packages** offer the ability to generate a Pulumi SDK for the language of your Pulumi project into a local folder, which can be directly incorporated into your project via your existing package manager along with `pulumi install`.

Local packages are versioned, and parameterized providers support many different formats for their parameters.  For example, the most general form of the command to use an existing Terraform provider is:

```shell 
$ pulumi package add terraform-provider [<registry>/]<author>/<name> [version]
```

Or:

```shell
$ pulumi package add terraform-provider /path/to/my/terraform-provider-binary
```

## What’s Next?

Today’s release is a big step in opening up access to even more providers for Pulumi users.  But there is still a lot more we have planned to build on top of these new foundations.  

First, with locally generated SDKs, the documentation is available within the language SDK you generate (and so lights up in your IDE or development environment!). Still, there is no static docs page available in the Pulumi Registry to find and link to on the web.  In the future, we plan to offer the ability to publish documentation for locally bridged providers in the Registry. (tracked in [registry#5302](https://github.com/pulumi/registry/issues/5302))  In that case, the registry entry will be only the docs - the SDKs and provider binary will not need to be published/hosted in the Registry itself.  

Second, the underlying Local Packages and Parameterized Providers technologies for building different flavors of a single provider are applicable to many other use cases.  In addition to having a single provider that can be “parameterized” to act as any Terraform provider, we have plans to apply this technology to additional use cases, such as generating strongly typed providers over any Kubernetes CRD, any Helm Chart, any other Pulumi program, and many more ecosystems of exciting infrastructure components which can be deployed via Pulumi.

Take the new support for using any Terraform or OpenTofu provider from Pulumi for a spin today:

* [Getting Started](https://www.pulumi.com/registry/packages/terraform-provider/)
* [Installation and Configuration](https://www.pulumi.com/registry/packages/terraform-provider/installation-configuration/)
* [Overview of Pulumi Packages](https://www.pulumi.com/docs/iac/packages-and-automation/pulumi-packages/debugging-provider-packages/)
