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

Pulumi needs to store the result of operations. On creation of a Pulumi resource, Pulumi makes a call to the cloud provider's API and then it stores the result of that API call. The place where Pulumi stores that result is called the "state" or "checkpoint". The state can be stored in Pulumi Cloud or in files on Amazon S3, Azure Blob Storage, Google Cloud Storage Buckets, or as a file on your local machine that you manage yourself.

### What browsers are supported?

Pulumi Cloud supports the following browsers:

| Browser |
|--------|
| Chrome |
| Firefox |
| Safari |
| Edge |

### How does Pulumi depend on Pulumi Cloud?

Pulumi uses Pulumi Cloud to store information about the current state of your application, which is used during updates, previews, and destroys as the source of truth for the current state of your cloud resources. We refer to this state as the "checkpoint" for your application. In addition, Pulumi Cloud ensures that for a given stack, only a single update is running at once (so, if you and someone else are collaborating on a stack together, it ensures that you both don't update the same stack at the same time.) Once your stack has been deployed, it has no dependency on Pulumi Cloud. To learn more about how the Pulumi engine uses pulumi.com, see [How Pulumi Works](/docs/iac/guides/basics/how-pulumi-works/).

### What happens if app.pulumi.com is down?

Any infrastructure that you’ve deployed using Pulumi will continue working and can be managed with your cloud provider’s console or CLI. app.pulumi.com does not affect any runtime behavior of your application.

If app.pulumi.com is down, you'll be unable to preview, update, or destroy a stack using Pulumi. Some commands, like `pulumi logs`, use app.pulumi.com to find the correct log stream so will not function until pulumi.com recovers; however, your cloud provider will still produce logs that you can use for diagnostics, which you can view via your cloud console or CLI.

### Can I use Pulumi without depending on Pulumi Cloud?

Pulumi Cloud offers a good combination of usability, safety, and security, but you can use Pulumi without it.

When you use Pulumi without Pulumi Cloud, the checkpoint for your stack is stored locally or in your own external [DIY backend](/docs/iac/concepts/state-and-backends/#using-a-diy-backend). If that file is lost or outdated, Pulumi can no longer operate on your stack. To collaborate with others on your stack, you must host this file yourself and protect against conflicting updates to it. If you use your own checkpoint file, Pulumi Cloud features such as the deployment history and resource view will not be available.

To use Pulumi without Pulumi Cloud, log in with `pulumi login --local` or log in to an alternative backend. For more information, see [State and backends](/docs/iac/concepts/state-and-backends/).

### How can I go back to using Pulumi Cloud?

Log in to Pulumi Cloud with `pulumi login`, then follow [Migrating between state backends](/docs/iac/concepts/state-and-backends/#migrating-between-state-backends).

### Which domains and IPs should I allowlist?

If you have requirements to allow egress access to or ingress access from Pulumi Cloud, please ensure you allowlist the subsequent hostnames and IP addresses:

- app.pulumi.com
- api.pulumi.com
- 34.208.94.47
- 34.212.116.224
- 44.241.59.217
- 52.40.198.20

These IP addresses and hostnames are the external-facing addresses of the Pulumi Cloud SaaS.

## Organizations

### What is an organization?

An organization is a shared workspace for your business to collaborate
across multiple projects at once. Organizations may be backed by your
existing source control system (GitHub, GitLab, Atlassian), identity
provider (any SAML/SSO provider, including Okta and Active Directory),
or managed manually. Organization owners and administrators can manage
access to the organization's projects with security and administrative
features.

For more information, see [Organizations](/docs/administration/concepts/organizations/).

### How do I create a stack inside an Organization instead of my User account?

To create a stack in a different Pulumi organization, prefix the stack's
name with the organization name. For example:

```sh
$ pulumi stack init acme-corp/widget-server
```

### How do I migrate stacks from an individual account to an organization account?

[Pulumi Cloud](https://app.pulumi.com/signin) lets you transfer stacks from your individual account to any organization account you belong to as an administrator.

To transfer a stack from your individual account to an organization, navigate to the Stacks page and select **Transfer stacks**.

From there, select the transfer destination and tick any stacks you'd like to transfer.

To learn more about this process, see [Transferring stacks](/docs/administration/concepts/organizations/#transferring-stacks).

### How can I delete a Pulumi organization?

Organization deletion is a permanent action and can only be performed by an organization admin.

In [Pulumi Cloud](https://app.pulumi.com/signin), open your organization, navigate to **Settings**, and select the **Delete organization** option.

If you don't see this option, confirm you're an organization admin.

For detailed steps, see [Deleting an organization](/docs/administration/concepts/organizations/#deleting-an-organization).

### How do I link an existing Pulumi account to my company's organization?

To join your company's organization, you must sign in with the identity provider that organization is backed by (for example, GitHub, GitLab, SAML/SSO, or email).

If you already have a Pulumi account, navigate to your profile in [Pulumi Cloud](https://app.pulumi.com/signin) and connect that identity provider, then accept the organization invite.

If this fails, delete your account, then accept the organization invite.

{{% notes type="warning" %}}
Note that deleting your account will remove access to any stacks and environments still under the account. Transfer any stacks you want to keep before proceeding.
{{% /notes %}}

For more about joining organizations, see [Joining an organization](/docs/administration/concepts/organizations/#joining-an-organization).

## Account

### How can I delete my Pulumi account?

You can delete your personal account from your account settings in [Pulumi Cloud](https://app.pulumi.com/signin).

Before deleting your account, make sure you have transferred any stacks you want to keep and that you are no longer required as an admin in any organization.

For more information, see [Deleting your account](/docs/administration/concepts/accounts/#deleting-your-account).

## Pricing

### How do I get started for free?

Sign up with the identity provider your organization uses, then
[download the CLI](/docs/get-started/) and sign in when it prompts you. The
Individual edition is free forever and needs no credit card. It covers one user,
unlimited projects, stacks, and environments, and unlimited updates and history.

### Are organizations available on the Individual edition?

No. The Individual edition covers a single user, which suits private projects but
not a team. Organizations — the shared workspace where several engineers work on
the same projects — start with the Team edition. Enterprise and Business Critical
add [role-based access control](/docs/administration/concepts/rbac/) and
[SAML/SSO](/docs/administration/guides/saml/) on top of that.

### Can I start small and upgrade later?

Yes. You can move up an edition at any time from your organization's
**Billing & usage** settings in [Pulumi Cloud](https://app.pulumi.com/signin).
Your stacks, environments, and history carry over untouched. Business Critical is
priced per organization, so [contact us](/contact/?form=sales) for that one.

### I'm on a legacy Starter, Pro, or per-stack plan. What do I do?

Those editions are retired and don't include newer capabilities such as
[Pulumi Deployments](/docs/deployments/), [Pulumi Insights](/docs/insights/), and
[Pulumi Neo](/docs/ai/neo/). [Contact us](/contact/?form=sales) to move to a
current edition. If now isn't the right time for your team, we're happy to honor
your existing terms.

### Do you offer custom pricing for large teams?

We are always happy to discuss the best way to ensure Pulumi can work
for your team. To talk with a leader at the company, please [fill
out the contact us form](/contact) and we'll be
in touch.

### What payment options do you accept?

You can pay by credit card (we use Stripe for processing). Start your trial
first, then add a card from your organization's **Billing & usage** settings.

For annual billing we also offer invoicing, payable by bank transfer or check.
To discuss that, [contact us](/contact/).

### What editions are available?

- **Individual** is free forever for one user, and covers state management,
  unlimited projects, stacks, and environments, and unlimited updates and history.

- **Team** adds organizations for up to 10 users, secure collaboration and CI/CD,
  resource search, webhooks, and automatic secrets rotation.

- **Enterprise** adds unlimited users, SAML/SSO and role-based access control,
  audit logs, drift detection and remediation, time-to-live stacks, and
  customer-managed keys.

- **Business Critical** adds [self-hosting](/docs/administration/self-hosting/),
  built-in compliance frameworks,
  [SCIM](/docs/administration/guides/scim/) user and group sync, audit
  log export, and 24x7 support.

For a feature-by-feature comparison, see the [pricing page](/pricing/).

### How can I update my payment information?

Self-serve organization admins and Billing Managers can update payment details from the organization's **Billing & usage** settings in [Pulumi Cloud](https://app.pulumi.com/signin) under **Payment methods**.

If you need to delegate billing-only access, see [Billing Managers](/docs/administration/concepts/billing-managers/).

## GitLab Support

### I use my GitHub identity to login into GitLab. How do I do that with Pulumi?

Click the **GitLab** sign-in button on <app.pulumi.com>, Pulumi
will redirect you to [gitlab.com](https://gitlab.com) where GitLab will
present you with the sign-in options to login into your GitLab account.
At that point, you may choose any of the sign-in options GitLab provides
to sign in.

### I already have an account on Pulumi. Will signing-in with my GitLab identity create a new account?

Yes. Signing in with a GitLab account will create a new account. That
means, your stacks and activity will stay with the other account. You
can copy stack state, but not Pulumi Cloud activity history, by performing a
[`pulumi stack export`](/docs/iac/cli/commands/pulumi_stack_export)
from your source stack, creating a new empty target stack in your GitLab-based account, and importing it using
[`pulumi stack import`](/docs/iac/cli/commands/pulumi_stack_import).
Importing state overwrites the selected target stack state.

If your source stack uses service-managed secrets, contact Pulumi Support before copying it. The destination account might not decrypt imported secrets.

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

## Learn more

- [Pulumi IaC FAQ](/docs/support/faq/infrastructure/)
- [Pulumi ESC FAQ](/docs/support/faq/secrets-config/)
- [Pulumi Policies FAQ](/docs/support/faq/policies/)
