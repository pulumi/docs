---
title_tag: "Compliance Ready Policies | CrossGuard"
meta_desc: This page contains the documentation for Pulumi Compliance Ready Policies.
title: Compliance Ready Policies
h1: Compliance Ready Policies
weight: 3
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  usingpulumi:
    parent: crossguard
    identifier: crossguard-compliance-ready-policies
---

Pulumi Compliance Ready Policies, with a comprehensive coverage of AWS, Azure, Google, and Kubernetes, provide
an enhanced level of control and governance over your cloud resources. Although Compliance Ready Policies
are currently available in JavaScript and TypeScript, they can be used with Pulumi stacks written
in any language. Pulumi Compliance Ready Policies empower you to enforce best practices, security standards,
cost control and compliance requirements seamlessly within your infrastructure-as-code workflows.

If you're not yet familiar with Policy as Code, read more about it [here](..).

## Installation

Pulumi Compliance Ready Policies are already integrated with the Pulumi CLI. When you run [`pulumi policy new`](/docs/cli/commands/pulumi_policy_new/),
you are presented with a series of Compliance Ready Policies flavored Policy Packs such as `aws-compliance-policies-typescript`,
`aws-iso27001-compliance-policies-typescript` and `azure-iso27001-compliance-policies-typescript` along with
many others.

Upon selecting one of those pre-built Policy Packs, the Pulumi CLI takes care of downloading and installing
the required dependencies in your local environment.

Alternatively, a step-by-step wizard is available in the Pulumi Cloud Console with all the required
instructions for you to follow.

When your Policy Pack is ready, you may evaluate it locally, or publish it to your Pulumi Organization.
See below for [more details](#policy-pack-enforcement).

If you're starting from an existing Policy Pack, you need to install the necessary Compliance Ready Policies packages.
Note that `@pulumi/policy-manager` is always required and should be explicitly present in
your `package.json`.

Here is an example on how to install the Policy Manager and the Compliance Ready Policies for AWS.

```bash
npm install @pulumi/compliance-policy-manager @pulumi/aws-compliance-policies --save
```

Supported Compliance Ready Policy packages are:

* `@pulumi/compliance-policy-manager` (**Required**) Policy Manager is used to manage Compliance Ready Policies.
* `@pulumi/aws-compliance-policies` Set of Compliance Ready Policies for Amazon Web Services, for both
  AWS Native and AWS Classic providers.
* `@pulumi/azure-compliance-policies` Set of Compliance Ready Policies for Microsoft Azure, for both Azure
  Native and Azure Classic providers.
* `@pulumi/google-compliance-policies` Set of Compliance Ready Policies for Google Cloud Platform, for
  both Google Native and GCP providers.
* `@pulumi/kubernetes-compliance-policies` Set of Compliance Ready Policies for Kubernetes.

### Policy packages upgrade

Pulumi regularly publishes new policies, enhancements and bug fixes to its Compliance Ready Policies packages
and framework.

You should regularly update to the latest versions as you already do with the Pulumi providers and other
SDKs.

To check for newer versions, run `npm outdated`. If some packages are outdated, they will be listed
as shown below.

```text
Package                 Current  Wanted  Latest  Location
@pulumi/aws-compliance-policies      0.0.8   0.0.8  0.0.15  node_modules/@pulumi/aws-policies
@pulumi/compliance-policy-manager    0.0.3   0.0.3   0.0.6  node_modules/@pulumi/policy-manager
```

Then install the latest versions

```sh
npm install @pulumi/aws-compliance-policies@0.0.15 @pulumi/compliance-policy-manager@0.0.6 --save
```

{{% notes type="warning" %}}
Always upgrade Policy Manager and other Compliance Ready Policy Packages at the same time to ensure
Compliance Ready Policies are correctly registered with the Policy Manager.
{{% /notes %}}

Once your Policy Pack contains the latest versions, test it locally and finally publish a new version
of your Policy Pack into your Pulumi organization.

## Authoring a Policy Pack with Pulumi Compliance Ready Policies

Pulumi Compliance Ready
Policies come with a [Policy Manager](../api-policy-manager/) to help you quickly build policy packs
by selecting policies of interest or changing the enforcement level of your chosen policies.

There are 2 main ways to author a new Policy Pack. The methods described below can be
used side-by-side with each other if you desire so.

### Policy selection

Pulumi Compliance Ready Policies have been enriched with additional metadata allowing authors to quickly
select and use policies based on areas of focus.

Policies have 5 metadata fields:

* The `vendor` field holds the vendor's name to which the policy belongs to. For example `aws` is for
Amazon Web Services. If a vendor has more than one Pulumi provider (ie, AWS Classic and AWS Native),
then policies are grouped under the same vendor name. This is done so organizations have a complete
control over resource creation regardless of the Pulumi provider used.

* The `services` field holds the service name to which the policy belongs to. For example `s3` is for
Amazon Web Services Simple Storage Service (S3), or `containerservice` is for Azure Container Service.

* The `severity` field describes the policy severity across 4 severity levels: `low`, `medium`,
`high`, and `critical`. As some policies address more sensitive issues, this field highlights the
security risks associated.

* The `topics` field contains a set of keywords pertaining to the policy, such as `encryption`,
`cost`, `backup`, or `availability`. It allows organizations to select policies based on area
of focus.

* Finally, `frameworks` holds information about the policy and the compliance frameworks it belongs to --- for example, `pcidss` for the PCI-DSS framework. It enables organizations to quickly select policies
based on a compliance framework they wish to adhere.

The example below shows how to select policies for AWS that are related to the EC2 and S3 service and
for which the policy severity is rated either medium, high or critical, and where the policies are
related to encryption and to the PCI-DSS framework.

```ts
import { PolicyPack } from "@pulumi/policy";
import { policyManager } from "@pulumi/compliance-policy-manager";

new PolicyPack("aws-compliance-ready-policies-typescript", {
    policies:[
        ...policyManager.selectPolicies({
            vendors: ["aws"],
            services: ["ec2", "s3"],
            severities: ["medium", "high", "critical"],
            topics: ["encryption"],
            frameworks: ["pcidss"],
        }, "mandatory" ),
    ],
});

policyManager.displaySelectionStats({
    displayGeneralStats: true,
    displayModuleInformation: true,
    displaySelectedPolicyNames: true,
});
```

{{% notes type="info" %}}
Policy selection doesn't require any `import` statement other than Policy Manager. Policy Manager
automatically finds and loads policy packages as plugins. Make sure your `package.json`
contains the correct policy packages you wish to load and use.
{{% /notes %}}

To assist in policy selection visibility  and traceability, Policy Manager has the ability to display
selection statistics when calling `policyManager.displaySelectionStats()`. Each time your policies
are evaluated as part of a stack preview or stack update, statistics will also be displayed and
recorded in Pulumi Cloud as part of your Pulumi app output.

### Policy cherry-picking

When using Pulumi Compliance Ready Policies it's also possible to create finely-tuned Policy Packs by manually
selecting individual policies.

To allow Compliance Ready Policy cherry-picking, you need to `import` the policy package in your Policy Pack code.

It is recommended to use `policyManager.selectPolicies()` when cherry-picking Compliance Ready Policies so duplicated
policies are removed and your Policy Pack statistics are accurate. Not doing so may lead to duplicate
policy selection, the inability to publish your Policy Pack in your Pulumi organization, or inaccurate
Policy Pack statistics.

In this example, first the user is manually selecting policies for disabling HTTP traffic on CloudFront
distributions and ensuring encrypted volumes for EBS using the `mandatory` enforcement level.
In the second statement, the user is selecting policies to ensure modern TLS encryption is used on
CloudFront distributions but with an enforcement level of `advisory`.

It's worth noting in the example below that policies need to be individually selected for both classic
and native providers.

```ts
import { PolicyPack } from "@pulumi/policy";
import { policyManager } from "@pulumi/compliance-policy-manager";
import * as awsPolicies from "@pulumi/aws-compliance-policies";

new PolicyPack("aws-compliance-ready-policies-typescript", {
    policies:[
        ...policyManager.selectPolicies([
            awsPolicies.aws.cloudfront.Distribution.disallowUnencryptedTraffic,
            awsPolicies.awsnative.cloudfront.Distribution.disallowUnencryptedTraffic
            awsPolicies.awsnative.ec2.Volume.disallowUnencryptedVolume,
            awsPolicies.aws.ebs.Volume.disallowUnencryptedVolume,
        ], "mandatory"),
        ...policyManager.selectPolicies([
            awsPolicies.aws.cloudfront.Distribution.configureSecureTls,
            awsPolicies.awsnative.cloudfront.Distribution.configureSecureTls,
        ], "advisory"),
    ],
});

policyManager.displaySelectionStats({
    displayGeneralStats: true,
    displayModuleInformation: true,
    displaySelectedPolicyNames: true,
});
```

{{% notes type="info" %}}
Pulumi Compliance Ready Policies are structured the same way the provider services and resources are structured,
making them easy to navigate. Consider using a modern IDE to leverage code completion, linting and embedded
code documentation.
{{% /notes %}}

### Mixed authoring

Compliance Ready Policy selection and cherry picking methods can be combined.

```ts
import { PolicyPack } from "@pulumi/policy";
import { policyManager } from "@pulumi/compliance-policy-manager";
import * as awsPolicies from "@pulumi/aws-compliance-policies";
import * as k8sPolicies from "@pulumi/kubernetes-compliance-policies";

new PolicyPack("aws-compliance-ready-policies-typescript", {
    policies:[
        ...policyManager.selectPolicies({
            vendors: ["aws"],
            services: ["ec2", "s3"],
            severities: ["medium", "high", "critical"],
        }, "mandatory" ),
        ...policyManager.selectPolicies({
            vendors: ["kubernetes"],
            severities: ["high", "critical"],
        }, "mandatory"),
        ...policyManager.selectPolicies([
            awsPolicies.aws.alb.LoadBalancer.configureAccessLogging,
            awsPolicies.aws.alb.LoadBalancer.enableAccessLogging,
        ], "advisory"),
    ],
});
policyManager.displaySelectionStats({
    displayGeneralStats: true,
    displayModuleInformation: true,
    displaySelectedPolicyNames: true,
});
```

### Policy Pack Statistics

To assist in policy selection visibility and traceability, Policy Manager has the ability to display
selection statistics when calling `policyManager.displaySelectionStats()`. When your policies
are evaluated as part of a stack preview or stack update, statistics will also be displayed and
recorded in Pulumi Cloud as part of your Pulumi app output.

This feature allows your organization to track the policies evaluated during a stack update or a preview,
as well as the total number of policies selected, and the Pulumi Compliance Ready Policies packages versions
used in your Policy Pack.

To display statistics about your Policy Packs and the Compliance Ready Policies in use, add the following
statement at the bottom of your Policy Pack.

```ts
policyManager.displaySelectionStats({
    displayGeneralStats: true,
    displaySelectedPolicyNames: true,
    displayModuleInformation: true,
});
```

Setting `displayGeneralStats` to `true` will display general statistics about the number of available
policies across all installed policy packages, how many were selected by your Policy Pack and the remaining
number of (unselected) policies.

Setting `displaySelectedPolicyNames` to `true` will dump all the policy names that were selected by your
Policy Pack. This will help you track policy usage over time and when performing any audit.

Finally, setting `displayModuleInformation` to `true` will display the names and versions of your installed
policy packages.

### Additional Compliance Ready Policy Packages

Pulumi Compliance Ready Policies are published in per-vendor NPM packages. Each Compliance Ready Policy package contains
policies for both classic and native providers when they exist, as those providers are compatible with one another.

Adding a new Compliance Ready Policy package is done like any other NPM packages.

```bash
npm install --save @pulumi/aws-compliance-policies
```

The list of policies contained in each NPM policy package can be found below:

* [AWS Classic](../compliance-ready-policies-aws/)
* [AWS Native](../compliance-ready-policies-awsnative/)
* [Azure Classic](../compliance-ready-policies-azure/)
* [Azure Native](../compliance-ready-policies-azurenative/)
* [GCP](../compliance-ready-policies-gcp/)
* [Google Native](../compliance-ready-policies-googlenative/)
* [Kubernetes](../compliance-ready-policies-kubernetes/)

## Policy Pack enforcement

Like standard Pulumi policy packs, Compliance Ready Policy Packs may be run locally or enforced across your Pulumi Organization.

If a Policy Pack needs to be installed at a time of a preview or an update, the Pulumi CLI will transparently
take care of those steps on behalf of the user.

Before enforcing your Policy Pack, you may evaluate it locally using `pulumi preview --policy-pack <path-to-policy-pack-directory>`.
For additional details, please refer to our [documentation](https://www.pulumi.com/docs/using-pulumi/crossguard/get-started/#running-locally).

When your Policy Pack is ready, you should publish it in your Pulumi Organization with the aim to enforce
it. To publish your Policy Pack, run `pulumi policy publish <org-name>`.

```text
Obtaining policy metadata from policy plugin
Compressing policy pack
Uploading policy pack to Pulumi service
Publishing "my-policy-pack" - version 1.0.0 to "myorg"
Published as version 1.0.0
```

Additional details are available in our [documentation](https://www.pulumi.com/docs/using-pulumi/crossguard/get-started/#enforcing-a-policy-pack).

## Performance

Pulumi Compliance Ready Policies have been designed from the ground up to be efficient from the start. However,
like any software, we recommend Policy Pack Authors to be mindful of how they implement their Policy
Packs.

Pulumi recommends avoiding installing policy packages for vendors you don't use. Doing so will reduce
memory usage and will make the execution of your Pulumi app faster.

Pulumi recommends loading Compliance Ready Policies only for services and resources you intend to use. This will
result in faster Pulumi app execution.

Consider using multiple policy packs (one for each vendor) as this will result in faster installation
but at the expense of a slightly slower execution and larger memory footprint.

Pulumi also recommends upgrading your Pulumi Compliance Ready Policy packages regularly. Many Policies are added
and updated on a regular basis giving you better Infrastructure as Code guardrails.

## Troubleshooting and support

### Policy Pack is empty

At times, your Policy Pack may appear to be empty (ie, no policy is evaluated). There are 2 main reasons
for this to happen.

First, an incomplete upgrade was performed and some Compliance Ready Policies packages aren't on the latest version.

To address this issue, upgrade both the Policy Manager and the Compliance Ready Policies packages to their latest versions as described in the [Policy package upgrade documentation](#policy-packages-upgrade) above.

Second, at times the `node_modules` may reference NPM packages incorrectly. Remove the `node_modules`
directory and reinstall all your NPM packages.

## Support & feature requests

Additional support is available through our usual channels.

We encourage you to contact us via your dedicated Slack channel and ask questions directly there where
possible.

If you wish to report a bug or request a new feature (like a new policy), open a new public issue at
<https://github.com/pulumi/compliance-policies/issues/new/choose>

You may also open a new support ticket using our support center portal available at <https://support.pulumi.com/hc/en-us>.
