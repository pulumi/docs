---
title: "Introducing Pulumi ESC: Easy and Secure Environments, Secrets and Configuration"
allow_long_title: true

date: 2023-10-10T04:00:00-07:00

meta_desc: "Introducing Pulumi ESC: Hierarchical Environments, Secrets Management and Configuration-as-Code for the Cloud"

meta_image: meta.png

authors:
    - luke-hoban

tags:
    - esc
    - secrets
    - platform-engineering

---

Today, we’re excited to introduce [**Pulumi ESC**](/product/esc/), a new product from Pulumi that manages and tames secrets and configuration complexity across all of your cloud infrastructure and application environments.  Pulumi ESC introduces a new category of configuration-as-code product, motivated by our experience working with hundreds of Pulumi IaC customers to address their needs in managing secrets and configuration at scale within their Pulumi infrastructure and across other cloud applications and infrastructure projects.

<!--more-->

{{< youtube "MtV_LPZKNP8?rel=0" >}}

Pulumi ESC enables teams to aggregate secrets and configuration from many sources, manage hierarchical collections of configuration and secrets ("environments"), and consume those configuration and secrets from a variety of different infrastructure and application services.  Pulumi ESC works hand-in-hand with Pulumi IaC to simplify configuration management, but also works independently from Pulumi IaC, as a solution for managing environments, secrets and configuration for any application or infrastructure project.

For example, the Pulumi ESC CLI (`esc`) makes it possible to give your developers immediate, just-in-time authenticated and short-lived access to cloud credentials across any cloud provider with just a single command: `esc run aws-staging -- aws s3 ls`.

![Pulumi ESC Overview GIF](esc.gif)

Here are just a few of the exciting use cases we've seen for Pulumi ESC:

* Do you have configuration for dozens of environments that is copy/pasted around and prone to drift?  Pulumi ESC lets you manage this as code using a simple set of environments that naturally and flexibly compose to derive all of your different configurations.

* Is it hard for developers in your organization to get access to short-lived credentials to work in the environments they need to develop and deploy into?  Pulumi ESC lets you configure OIDC to pull short-lived credentials and other secrets dynamically from all of your cloud and secrets providers and present them in a logical way to other tools with a single command like `esc run aws-staging -- aws s3 ls`.

* Have your Pulumi IaC configuration files grown to hundreds of lines of configuration spread across many different stack files?  Pulumi ESC introduces a simple way to consume Pulumi IaC configuration directly from Pulumi ESC environments, enabling a much richer secrets and configuration management for Pulumi IaC.

Pulumi ESC is available today in preview via the new `esc` CLI, as part of Pulumi Cloud, via the Pulumi Cloud REST API, and has direct integration with Pulumi IaC stack configuration and new `pulumi env` commands.  It also supports dynamically pulling secrets and configuration from other sources of truth, including AWS OIDC, AWS Secrets Manager, Azure OIDC, Azure KeyVault, Google Cloud OIDC, Google Secrets Manager, HashiCorp Vault, and Pulumi IaC Stack References - with many more sources like 1Password coming soon.

[Get Started](/docs/pulumi-cloud/esc/) with Pulumi ESC today!

![ESC Overview](esc-overview.png)


## A Taste of Pulumi ESC

Pulumi ESC allows you to define _environments_, each of which specifies a collection of _secrets_ and _configuration_ values. Environments are specified as _code_, and each environment can import one or more other environments (for composition and inheritance), and can specify its own configuration values directly, or be pulled from another secrets provider.

The following example shows a Pulumi ESC environment which dynamically pulls values from AWS OIDC, HashiCorp Vault and AWS Secrets Manager, as well as setting environment-specific configuration and overriding inherited configuration.

```yaml
# imports allow you to compose other pre-existing environments
imports:
  # AWS creds via OIDC
  - aws-production
  # stripe API keys imported from vault
  - stripe-production
  # keys for signing docker images via AWS Secrets Manager
  - docker-signing-production
values:
  # environment-specific configuration
  desiredInstanceCount: 8
  # overriding imports
  aws:region: us-west-2
```

## Why Pulumi ESC?

Working with Pulumi customers, we’ve seen the incredible benefits they get from managing IaC complexity in their code using Pulumi, and yet they frequently end up with a lot of complexity remaining at the boundary to their IaC code - at the configuration and secrets they need to get into Pulumi IaC.  Users frequently show us configuration files that are hundreds of lines long, with tons of copy/paste both between Pulumi configuration and between other sources of truth and Pulumi configuration, and with more long lived static secrets being copied around than they would like - creating maintenance burden, security concerns, frequent drift, and operational risk.

As we looked at solving these problems for Pulumi we quickly realized that none of these problems are actually specific to Pulumi - they are all things that customers talked about seeing consistently throughout their infrastructure and application projects.  With other IaC tools, with Kubernetes configuration, with 12-factor app environment configuration, and everywhere in between.  Everyone we talked to had plenty of scar tissue built up from struggling with a common set of challenges in managing configuration and secrets across a complex set of interrelated environments:

* __Secrets and Configuration Sprawl__: Data in many systems. Challenging to audit. Lots of application-specific logic to acquire and compose configuration from multiple sources. Divergent solutions for Infrastructure and Application configuration.
* __Duplication and Copy/Paste__: Secrets are duplicated in many places. Frequently coupled to application/system-specific configuration stores.
* __Too Many Long-lived Static Secrets__: Long lived static credentials are over-used, exposing companies to significant security risk.  Rotation is operationally challenging. Not all systems support direct integration with OIDC and other dynamic secrets provisioning systems.

While customers frequently had good solutions for pure secrets management (AWS Secrets Manager, HashiCorp Vault, etc.), none of these solutions extended into managing the complexities of actually getting these secrets as well as non-secret configuration into the collection of logical environments that define how they will be consumed in infrastructure and applications.  Customers struggled with too many walled gardens for secrets management and configuration, and lack of any consistent set of tools and workflows to help manage the complexity of how secrets and configuration flow between these systems.

Pulumi ESC was born to address these problems and needs head on.  It does so through a few core design principles:

* __Hierarchical and Composable__: Environments contain collections of secrets and configuration, but can also import one or more other environments.  Values can be overridden, interpolated from other values, and arbitrarily nested.  This allows for flexible composition and reuse, and avoids copy paste.
* __Any Secrets Provider__:  Support for dynamic configuration providers allow Pulumi ESC to integrate with secrets stored in any other provider.  Organizations often use AWS Secrets Manager, Vault, Azure OIDC and/or 1Password plus many more sources of truth for their secrets and configuration.  Pulumi ESC supports them all, providing a single interface to your configuration and secrets, no matter where their source of truth is.  Pulumi ESC works with these tools to provide improved management of secrets and configuration.
* __Consume from Anywhere__: The `esc` CLI and the Pulumi ESC Rest API enables environments to be accessed from any application, infrastructure provider, or automation system.  At launch, first-class integrations are available with Pulumi IaC, local environment and .env files, GitHub Actions, and more.
* __Auditable__: Environments must be "opened" to compute and see the set of value they provide, and this action is recorded in audit logs, including a full record of how each value was sourced from within the hierarchy of environments that contributed to it.
* __Authentication and RBAC__:  Pulumi ESC brokers access to secrets and configuration that live in other systems, and so authentication and granular RBAC are critical to ensure robust access controls across your organization.  Pulumi ESC leverages the same Pulumi Cloud identity, RBAC, Teams, SAML/SCIM and scoped access tokens that are used for Pulumi IaC today, extending these all to managing access to Environments as well as Stacks.
* __Configuration as Code__:  Environments are defined as YAML documents which can describe how to project and compose secrets and configuration, integrate dynamic configuration providers, and compute new configuration from other values (construing a URL from a DNS name, or concatenating multiple configuration values into a derived value).  The incredible flexibility of a code-based approach over traditional point-and-click interfaces allows Pulumi ESC to offer rich expressiveness for managing complex configuration.
* __Fully Managed__: Pulumi ESC is offered as a fully managed cloud service in Pulumi Cloud (and Pulumi Cloud Self-hosted in the near future). The pulumi/esc project is [open source](https://github.com/pulumi/esc/), and contains the evaluation engine for environments, the esc CLI, and in the future, the extensible plugins for source and target integrations.

Pulumi ESC enables a new kind of solution for configuration management of modern cloud infrastructure.

## A Tour of Pulumi ESC

We can start by creating a few simple environments using Pulumi ESC.  This can be done in the Pulumi Cloud console, using the new `esc` CLI, or using the new `pulumi env` sub-commands in the Pulumi CLI. Let’s take a look at these in action.

### Creating and Managing Environments, Secrets and Configuration

First, in the Pulumi Cloud console, we can go to the Environments tab and create a new environment called `aws-staging`.

![Create a New Environment in the Pulumi Cloud Console](console-env.png)

We can then define some configuration for our environment.  For example, defining our AWS region:

```yaml
# aws-staging
values:
  aws:
    region: us-west-2
```

This defines a configuration object with a top level `aws` key, and a nested region key whose value is `us-west-2`.   When we save this, the preview on the right shows the definition of a configuration object that produces the following JSON:

```json
{
  "aws": {
    "region": "us-west-2"
  }
}
```

We can make this more interesting by also integrating with AWS OIDC to define the AWS credentials we want to access.  To do this, we change our environment to add a `creds` key to the `aws` object:

```yaml
# aws-staging
values:
  aws:
    region: us-west-2
    creds:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789012:role/pulumi-environments-oidc
          sessionName: pulumi-environments-session
          duration: 1h
```

This indicates that we want to pull a set of AWS credentials from the aws-login dynamic provider, which expects a few inputs - including a `roleArn` we would like to assume and a `duration` for the short lived AWS credentials that will be returned.  If we have [configured OIDC in AWS](/docs/pulumi-cloud/esc/providers/aws-login) to allow this Pulumi Cloud organization and environment to request short-lived credentials, then this will allow our environment to dynamically pull in those credentials for an authenticated user, and present back a config object that includes them.

To see the values computed by an environment, we need to "open" it.  That can be done via the CLI, the REST API or the integrations into other systems (like Pulumi IaC).  Let’s open it with the `esc` CLI first.  [Download the `esc` CLI](/docs/install/esc/), and then run the following commands:

```shell
$ esc env ls
demo/aws-staging

$ esc open demo/aws-staging
{
  "aws": {
    "creds": {
      "accessKeyId": "ASIAVNHUKX5VGSMMR2DJ",
      "secretAccessKey": "REDACTED",
      "sessionToken": "REDACTED"
    },
    "region": "us-west-2"
  }
}
```

The `aws-login` provider returns three values, one non-secret and two secret, which provide the short-lived credentials necessary to authenticate with AWS.

We can also use this configuration as both environment variables and Pulumi IaC config.  To do so, we extend our environment to the following:

```yaml
# aws-staging
values:
  aws:
    region: us-west-2
    creds:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789012:role/pulumi-environments-oidc
          sessionName: pulumi-environments-session
          duration: 1h
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.creds.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.creds.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.creds.sessionToken}
  pulumiConfig:
    aws:region: ${aws.region}
```

The top-level `environmentVariables` key is used by convention to project out a set of environment variables for this environment.  The top level `pulumiConfig` key is used by convention to project out a set of Pulumi IaC configuration for this environment.  Note that they can pull their values from other configuration in this environment (or, as we’ll see soon, any environment they import).  That includes using the values from dynamic providers like `aws-login`.

Now that we’ve got a complete environment configured for setting up access to our AWS account, we can use this with esc run to run a command (`aws s3 ls`) using the environment variables:

```shell
$ esc run demo/aws-staging -- aws s3 ls
2023-09-07 16:35:11 accesslogs-1284c27
2023-04-13 15:04:41 accesslogs-6652a3d
2023-01-20 16:52:04 accesslogs-7ea7130
2023-08-23 17:50:24 accesslogs-8ad28c2
...
```

Note that when we run this command, `esc run` uses our local authentication credentials (including RBAC permissions) for Pulumi ESC to authenticate our access to this environment, and then uses the environment’s identity to get a short-lived AWS credential via AWS OIDC.  It then brings back this unique credential just for the lifetime of the `aws s3 ls` subcommand.  This provides very granular authentication and auditability of the operations run, while also not requiring the user to have a long lived AWS credential on their machine to run operational commands against the account.

![A Pulumi ESC Environment in the Pulumi Console](./console-env.png)

### Using Pulumi ESC with Pulumi IaC

Next, we can define a second environment for our shopping-service application.  This will be deployed with Pulumi IaC, so we’ll provide some default configuration for this service in the `pulumiConfig` section.

We run `esc env init shopping-service` to create our new environment. And then `esc env edit shopping-service` to open an editor to populate our new environment.  We can then add the following to our environment, where it will be encrypted and stored for us.

```yaml
# shopping-service
values:
  pulumiConfig:
    numInstances: 4
    domainName: shopping.acmecorp.com
    dbPassword:
      fn::secret: hunter2
```

To use this from our Pulumi IaC program, we want to consume the information in both the `shopping-service` and `aws-staging` environments.  We can define another environment which just imports these two!  Let’s call this third environment `shopping-service-staging` and define it:

```yaml
imports:
  - aws-staging
  - shopping-service
values:
  pulumiConfig:
    numInstances: 2
```

This uses the imports top level key which allows us to compose together configuration from multiple other environments.  We don’t have to copy/paste configuration and secrets between stacks, or from other sources of truth -- we just import them!  This keeps our configuration as [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) as possible.

Note that we also specified a new value for `numInstances` which overrides what was imported.  This allows us to customize the values if this particular environment needs to provide a different value than what it imports.

Now, we can use this directly within our Pulumi IaC project by modifying its stack file.  Inside our `Pulumi.staging.yaml` file for the `shopping-service` project, we can remove the config section, and just replace it with:

```yaml
# Pulumi.staging.yaml
environment:
  - shopping-service-staging
```

If I run `pulumi preview` now on my Pulumi IaC project (in this case, a project which just outputs the configuration values), we will see that configuration values for `aws:region`, `numInstances`, and `dbPassword` are all available. I didn’t have to copy them into this stack, they were automatically pulled out of the environment in Pulumi ESC.  And note that the secretness of the `dbPassword` configuration value flowed through into Pulumi IaC’s config system to ensure this value is encrypted in any place it is used within our infrastructure as code.

```
Previewing update (pulumi/staging)

View in Browser (Ctrl+O): https://app.pulumi.com/pulumi/shopping-service/staging/previews/f0f9a124-88e1-4d4a-8025-178aac9127c3

     Type                 Name                      Plan       Info
 +   pulumi:pulumi:Stack  shopping-service-staging  create     3 warnings

Outputs:
    dbPassword  : [secret]
    numInstances: 2
    region      : "us-west-2"

Resources:
    + 1 to create
```

Finally, we can give other users in our organization access to this environment by configuring our Engineering team within Pulumi Cloud to be allowed to "Open" the environment.

![RBAC for ESC in the Pulumi Cloud console](./console-rbac.png)

Pulumi ESC enables us to define environments containing secrets and configuration using a flexible, code-based approach, leveraging composition in order to keep our configuration DRY, as well as dynamic providers to pull secrets and credentials from other providers like AWS OIDC.  While this example used AWS, everything discussed works with any cloud, and with an even wider variety of secrets providers.

## The Future of Pulumi ESC

We’re excited to launch the public preview of Pulumi ESC today, and see it solving many pressing problems with the feature set available today.  We see even more opportunity to enhance this foundation, and have designed Pulumi ESC with a few new capabilities in mind.  These features will ship in the coming months.

### Application-level SDKs

Pulumi ESC can already be accessed from application code via the REST API, but we will be extending this to native SDKs for TypeScript, Python, Go and .NET.  These SDKs will enable configuration from ESC to be directly pulled into applications at runtime, instead of, or as well as, provisioning via environment variables or other mechanisms at deployment time.  See [pulumi/esc#60](https://github.com/pulumi/esc/issues/60).

### Syncing Configuration to External Systems

While the `esc` CLI and REST APIs can be used today to pull configuration down into many existing places where environments will be consumed, there are also many systems that store their configuration in more "walled gardens" which would need to be pushed into for optimal usability.  For example, pushing configuration values into a CI/CD system’s configuration system to avoid needing to copy/paste configuration and secrets manually into their UI.  We are working on additional integrations for Pulumi ESC that can "push"/"sync" configuration into systems directly, so that you can still benefit from the usability of their native configuration systems, without having to take on the problems of configuration sprawl, long-lived static secrets and duplication and copy/paste of secrets.  See [pulumi/esc#58](https://github.com/pulumi/esc/issues/58).

### Dynamic Configuration Provider Ecosystem

We are already working with many additional partners to support pulling configuration and secrets from additional sources of truth into Pulumi ESC - including 1Password, Cloudflare and more.  Our goal is to support rich composition of configuration and secrets no matter where they live, and in the most secure way possible, and working with these providers will enable ESC to integrate natively with their systems. As part of this, we will also be working to bring the provider plugin model into the open source pulumi/esc repository along with the existing dynamic configuration providers. See [pulumi/esc#64](https://github.com/pulumi/esc/issues/64) and [pulumi/esc#65](https://github.com/pulumi/esc/issues/65).

### Versioning Environments

At launch, environments are managed directly in Pulumi Cloud.  But we’ve already heard early preview users express a desire to also be able to manage these via source-controlled code.  We’re exploring adding environments to the Pulumi Cloud Pulumi Provider to enable using desired state IaC to manage the definition of environments.  We’ve also worked with customers looking to be able to pin their projects that consume environments to specific versions of the environment, to avoid risk of breaking when environments are updated, and are working on extensions to enable this as well. See [pulumi/esc#59](https://github.com/pulumi/esc/issues/59) and [pulumi/esc#63](https://github.com/pulumi/esc/issues/63).

### Easy-to-Use Key/Value Interface in Pulumi Cloud
For the preview, we focused on document-based editing experience for environments, which provides direct access to the full richness of Pulumi ESC.  For many common use cases, it’s helpful to have a simple key/value-based interface for adding and configuring secrets. We will add the ability to switch between both of these UI experiences in the Pulumi Cloud console soon.  See [pulumi/esc#62](https://github.com/pulumi/esc/issues/62). Below is an early sketch of this additional table-based user interface.

![Key/Value based Environment Editor in the Pulumi Console](./table-view.png)

## Conclusion

Pulumi ESC is a new kind of configuration management offering that addresses pervasive issues faced by teams performing application and infrastructure development. We’re incredibly excited to launch the public preview, and to work with our community to continue our journey together.  While in preview, Pulumi ESC is available at no additional cost to all Pulumi Cloud users.

You can learn more about Pulumi ESC at:

* [Getting Started](/docs/pulumi-cloud/esc/get-started)
* [Documentation](/docs/pulumi-cloud/esc)
* [Open Source](https://github.com/pulumi/esc)
* [Community Slack](https://slack.pulumi.com/)
