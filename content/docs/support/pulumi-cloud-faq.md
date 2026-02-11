---
title_tag: "Pulumi Cloud: Frequently Asked Questions"
title: "Frequently Asked Questions"
h1: "Pulumi Cloud: Frequently Asked Questions"
meta_desc: A collection of Frequently Asked Questions (FAQ) about Pulumi Cloud.
menu:
    support:
        name: Pulumi Cloud FAQ
        parent: support-faq
        weight: 5
        identifier: support-faq-pulumi-cloud
aliases:
  - /docs/support/pulumi-cloud-faq/
  - /docs/pulumi-cloud/faq/
---

## General

### How does Pulumi store state?

Pulumi needs to store the result of operations. On creation of a Pulumi resource, Pulumi makes a call to the cloud provider's API and then it stores the result of that API call. The place where Pulumi stores that result is called the "state" or "checkpoint". The state can be stored using the Pulumi Cloud or in files on Amazon S3, Azure Blob Storage, Google Cloud Storage Buckets, or as a file on your local machine that you manage yourself.

## What browsers are supported?

The Pulumi Cloud supports the following browsers:

| Browser |
|--------|
| Chrome |
| Firefox |
| Safari |
| Edge |

### How does Pulumi depend on the Pulumi Cloud?

Pulumi uses the Pulumi Cloud to store information about the current state of your application, which is used during updates, previews, and destroys as the source of truth for the current state of your cloud resources. We refer to this state as the "checkpoint" for your application. In addition, the Pulumi Cloud ensures that for a given stack, only a single update is running at once (so, if you and someone else are collaborating on a stack together, it ensures that you both don't update the same stack at the same time.) Once your stack has been deployed, it has no dependency on the Pulumi Cloud. To learn more about how the Pulumi engine uses pulumi.com, see [How Pulumi Works](/docs/concepts/how-pulumi-works/).

### What happens if app.pulumi.com is down?

Any infrastructure that you’ve deployed using Pulumi will continue working and can be managed with your cloud provider’s console or CLI. app.pulumi.com does not affect any runtime behavior of your application.

If app.pulumi.com is down, you'll be unable to preview, update, or destroy a stack using Pulumi. Some commands, like `pulumi logs`, use app.pulumi.com to find the correct log stream so will not function until pulumi.com recovers; however, your cloud provider will still produce logs that you can use for diagnostics, which you can view via your cloud console or CLI.

### Can I use Pulumi without depending on the Pulumi Cloud?

Using the Pulumi Cloud with Pulumi provide a good combination of usability, safety, and security. However, for users with especially unique requirements, it is possible to use Pulumi apart from the Pulumi Cloud.

When you use Pulumi without the Pulumi Cloud, the checkpoint for your stack is stored locally or in your own external [DIY backend](/docs/concepts/state/#using-a-diy-backend). If that file is lost or outdated, Pulumi can no longer operate on your stack. To collaborate with others on your stack, you must host this file yourself and protect against conflicting updates to it. If you use your own checkpoint file, the Pulumi Cloud features, such as the deployment history and resource view, will not be available.

To use Pulumi without the Pulumi Cloud, log in using `pulumi login --local` or by logging in to an alternative backend. For more information, read more at [State and Backends](/docs/concepts/state/).

### How can I go back to using the Pulumi Cloud?

Run `pulumi login`, and you’ll be back to using the Pulumi Cloud. You will need to migrate any existing stacks to the Pulumi Cloud.

### How to migrate from a DIY backend to the Pulumi Cloud?

The Pulumi CLI allows you to export and import checkpoints so you can do the following. Suppose the stack “my-app-production” has been managed with a local checkpoint file, and you want to migrate it to pulumi.com. If you are currently logged in to the local endpoint, run the following commands:

```sh
$ pulumi stack select my-app-production # switch to the stack we want to export
$ pulumi stack export --file my-app-production.checkpoint.json # export the stack's checkpoint to a local file
$ pulumi logout
$ pulumi login
$ pulumi stack init my-app-production # create a new stack with the same name on pulumi.com
$ pulumi stack import --file my-app-production.checkpoint.json # import the new existing checkpoint into pulumi.com
```

In addition, if you have any encrypted configuration in your stack, you'll need to re-run `pulumi config set --secret <key> <value>` because pulumi.com uses a different key to encrypt your secrets than the local endpoint does.

### Which domains and IPs should I allowlist?

Should your network have egress limitations, please ensure you allowlist the subsequent domain and IP addresses:

- app.pulumi.com
- api.pulumi.com
- 34.208.94.47
- 34.212.116.224
- 44.241.59.217
- 52.40.198.20

These IP addresses and URL are the external facing addresses of the Pulumi Cloud SaaS and should be added to your allowlist to allow traffic from your network to reach our services.

## Organizations

### What is an organization?

An organization is a shared workspace for your business to collaborate
across multiple projects at once. Organizations may be backed by your
existing source control system (GitHub, GitLab, Atlassian), identity
provider (any SAML/SSO provider, including Okta and Active Directory),
or managed manually. Organization owners and administrators can manage
access to the organization's projects with security and administrative
features.

### How do I create a stack inside an Organization instead of my User account?

To create a stack in a different Pulumi organization, prefix the stack's
name with the organization name. For example:

```sh
$ pulumi stack init acme-corp/widget-server
```

### How do I migrate stacks from an individual account to an organization account?

The [Pulumi Cloud](https://app.pulumi.com/) allows you to transfer stacks from your individual account to any organization account you belong to as an administrator.

To transfer a stack from your individual account to an organization, navigate to the Stacks page and select **Transfer stacks**.

From there, select the transfer destination and tick any stacks you'd like to transfer.

To learn more about this process, see [Transferring Stacks](/docs/deployments/projects-and-stacks#transferring-stacks).

## Pricing

### How do I get started for free?

To get started, simply sign up for free using your identity provider of
choice (ideally the same one your organization will be backed by). From
there, create an organization that your team members will use. To use
the free Community Edition, just [download the CLI](/docs/get-started/) and
sign into the free tier of the service when it prompts you.

### Are organizations available in the free Community Edition?

The key distinction between Pulumi's free Community Edition and its paid
offerings — Team Starter, Team Pro, and Enterprise — is the presence
of an organization. The Community Edition is meant for individuals using
Pulumi for their private projects, but this tends not to work in a team
setting. Most teams want multiple engineers to have access to their
projects. This is precisely what organizations deliver to you. The
advanced tiers offer even more sophisticated organization management
facilities, including RBAC for advanced policy controls.

### Can I start small and upgrade later?

Yes! We designed the editions to make it easy to get started with Team
Starter, and once you've outgrown it, upgrading to Team Pro is a single
click away. To upgrade to Enterprise, please [contact
us](/contact).

### I'm an existing customer on a per stack plan -- what do I do?

We are in the process of reaching out to all existing customers to offer
a switch to one of the new plans. If you haven't heard from us yet,
please don't hesitate to [drop us a
line](/contact). If now isn't the right time to change
for your team, however, don't worry — we are happy to honor your
existing subscription terms.

### Do you offer custom pricing for large teams?

We are always happy to discuss the best way to ensure Pulumi can work
for your team. To talk with a leader at the company, please simply [fill
out the contact us form](/contact) and we'll be
in touch.

### What payment options do you accept?

All subscriptions can be paid with a credit card (we use Stripe for
processing). The Pulumi Service is meant to be easy to sign up for, so feel free
to simply begin your trial, and then you may enter your credit card on
your organization's Settings page.

For annual subscriptions, we also offer invoicing that is payable with
bank transfer or check. To discuss those options in more detail, please
[contact us](/contact/).

### What upgrade editions are available?

The following editions are also available as upgrade options:

- **Pulumi Team** is ideal for teams of up to 10 members and provides the basics of infrastructure as code in popular languages, enabling teams to ship faster. Includes 150K free credits each month.

- **Pulumi Enterprise** is ideal for large teams and organizations in production. It offers an unlimited number of members and teams and provides full cloud engineering capabilities.

- **Pulumi Business Critical** is ideal for enterprises that have specific requirements, like advanced security and compliance features, premium support, and [self-hosting options](/docs/pulumi-cloud/self-hosted/).

For more information about the specific differences and capabilities offered for the
Pulumi Team, Enterprise and Business Critical editions, refer to the [pricing page](/pricing/).

## GitLab Support

### I use my GitHub identity to login into GitLab. How do I do that with Pulumi?

Click the **GitLab** sign-in button on <app.pulumi.com>, Pulumi
will redirect you to [gitlab.com](https://gitlab.com) where GitLab will
present you with the sign-in options to login into your GitLab account.
At that point, you may choose any of the sign-in options GitLab provides
to sign-in.

### I already have an account on Pulumi. Will signing-in with my GitLab identity create a new account?

Yes. Signing-in with a GitLab account will create a new account. That
means, your stacks and activity will stay with the other account. You
can migrate them by performing a
[`pulumi stack export`](/docs/cli/commands/pulumi_stack_export)
from your source stack and then importing it using
[`pulumi stack import`](/docs/cli/commands/pulumi_stack_import)
in a new stack in your GitLab-based account.

If you would like to add your GitLab identity to your _existing_ Pulumi account, you can
do so by connecting your GitLab identity from your Pulumi account's profile page.

### How do I login into the pulumi CLI on my local machine using my GitLab-backed Pulumi account?

One of the benefits of using <app.pulumi.com> is to track the state of
your stacks. When you are running the pulumi CLI on your machine, you
can login into your account by typing `pulumi login`. There are two
options for you to complete the login process. You can either create an
Access Token on <app.pulumi.com> or simply press **ENTER** to let the
CLI launch the browser.

If you would like to let the CLI launch the browser, ensure that you are
already signed-in using GitLab at <app.pulumi.com> using your machine's
*default* browser. This way, when the browser is launched by the CLI,
your Pulumi account based on your GitLab identity would be automatically
used.

## More FAQ

- [Pulumi IaC FAQ](/docs/iac/support/faq/)
- [Pulumi ESC FAQ](/docs/support/faq/secrets-config/)
- [Pulumi Cloud SCIM FAQ](/docs/administration/access-identity/scim/faq/)
- [Pulumi Policies FAQ](/docs/support/faq/policies)
