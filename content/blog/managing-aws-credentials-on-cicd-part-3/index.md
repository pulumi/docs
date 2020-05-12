---
title: "Managing AWS Credentials on CI/CD - Part 3"
date: 2020-05-12
meta_desc: "Best practices for managing AWS credentials on CI/CD - Part 3 in the series"
authors:
    - chris-smith
    - sophia-parafina
tags:
    - CI/CD
    - secrets
---

This article is the third part of a series on best practices for securely managing AWS credentials on CI/CD. In this article, we cover the
last leg of the continuous delivery process to update your AWS resources and how to store sensitive data using Pulumi securely.
<!--more-->

Posts in this series:

- [Create a dedicated IAM User for your CI/CD]({{< relref "/blog/managing-aws-credentials-on-cicd-part-1#create-new-iam-user" >}})
- [Provide the IAM User’s credentials to your CI/CD system]({{< relref "/blog/managing-aws-credentials-on-cicd-part-2#providing-iam-credentials" >}})
- [Comparison with using hosted secret managers]({{< relref "/blog/managing-aws-credentials-on-cicd-part-2#using-a-secrets-service" >}})
- [Automate Rotating and Revoking AWS Credentials]({{< relref "/blog/managing-aws-credentials-on-cicd-part-2#automating-key-rotation" >}})
- [Assuming IAM Roles for performing updates](#assuming-iam-roles)
- [Securing sensitive data using Pulumi](#secrets-in-pulumi)

## Recap

In [part 1]({{< relref "/blog/managing-aws-credentials-on-cicd-part-1" >}}), we created a dedicated IAM User with
limited privileges. Then in [part 2]({{< relref "/blog/managing-aws-credentials-on-cicd-part-2" >}}), we set up a simple,
serverless Pulumi program that periodically rotated the User's access keys and updated the CI/CD system.

In this final post, we will _use_ those AWS credentials to update cloud resources as part of
a CI/CD workflow using Pulumi.

We will cover AWS's [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) and how they can be
used to safely manage the access Pulumi has to your AWS account. We will also cover how sensitive data in your
stack is stored within the Pulumi Console.

## Assuming IAM Roles for Performing Updates {#assuming-iam-roles}

In the previous post, we automatically create and rotate the AWS access keys for an IAM User. So it seems natural to
think that we should just use that same AWS access key to gain access to AWS resources. However, using the
access keys for an IAM User has a few major drawbacks.

First, those access keys are long-lived. If we didn't create that Pulumi program to rotate them automatically, the
key would last forever. (Meaning that a bad actor, perhaps elsewhere, or far in the future, could take advantage
of a compromised key.) Second, that access key could be used to do anything that the IAM User could. So you cannot
differentiate the set of capabilities based on the task at hand. (For example, if updating the Pulumi stack `website/staging`,
we might need a different set of permissions than if we were updating the stack `website/production`.)

The preferred alternative to using IAM User access keys is to "assume" an IAM Role. An IAM Role is similar to an IAM
User in that it grants a set of [policies and permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).
However, unlike an IAM User, an IAM Role does not have a password, nor can it be added to a Group and inherit any policies.
Also, the credentials for using an IAM Role are always short-lived. (Lasting no more than 12 hours, and likely much, much less.)

Instead, an IAM Role defines a set of capabilities that can be performed by any principal capable of assuming it. So
in other words, you can exchange your limited access IAM User's credentials for a specialized IAM Role. The IAM Role then
can be specifically tailored to a specific&mdash; wait for it&mdash; _role_ to perform.

Don't worry if that doesn't all make sense at first; let's look at a concrete example.

### Desired End State

In our situation, we want to create an IAM Role `WebsiteStackUpdaterRole` that grants permissions necessary for
Pulumi to update the `website/production` stack. We will custom tailor this role to only grant access to the set of resources
and operations we know the stack needs.

We also want to restrict who can assume the `WebsiteStackUpdaterRole`, so that only specific users/accounts can access it.
e.g., the IAM User `cicd-bot` but not IAM User `dwight-over-in-sales`.

And just to show a more real-world example, we'll do this using _multiple_ AWS accounts. Where the `website/production` stack's
resources are housed in a "production" AWS account, and the `cicd-bot` IAM User is defined in a
[bastion AWS account](https://blog.coinbase.com/you-need-more-than-one-aws-account-aws-bastions-and-assume-role-23946c6dfde3).

### Creating the IAM Role

The following snippet creates an [IAM Role]({{< ref "/docs/reference/pkg/aws/iam/role" >}}) resource using Pulumi. The
most important input property of which is the `assumeRolePolicy` document, which defines _who_ can assume this role.

> This is a situation where Pulumi's ability to declare the policy document in code is super-useful, as it makes it
> much easier to reference other resources (e.g., another AWS account's ID) as well as supporting inline comments.

```js
// IAM Role used by cicd-bot to update the website stack.
export const websiteStackUpdaterRole = new aws.iam.Role("WebsiteStackUpdaterRole", {
    name: "WebsiteStackUpdaterRole",
    description: "Broad access for updating Pulumi stacks in the 'production' AWS account.",
    maxSessionDuration: 30 * 60,  // 30 minutes
    assumeRolePolicy: {
        Version: "2012-10-17",
        Statement: [
            {
                Effect: "Allow",
                Principal: {
                    // We grant the "bastion account", which defines IAM Users the ability to assume this role.
                    // The IAM Policies in that other AWS account will then determine which users, groups, etc.
                    // will be able to use the `sts:AssumeRole` action on this IAM Role.
                    "AWS": `arn:aws:iam::${awsAccountIds.bastionAccount}:root`,
                },
                // But as an additional precaution against misconfiguration in the bastion account, we add
                // some additional checks to determine who can access this policy.
                Condition: {
                    "ForAllValues:StringEquals": {
                        "aws:PrincipalTag/access-to-production": "true",
                        "sts:ExternalId": [
                            "contoso/website/production",
                            "contoso/website/staging",
                        ],
                    },
                },
                Action: "sts:AssumeRole",
            },
        ],
    },
});
```

There's a lot packed into that IAM Role's configuration.

First, the "principal" (who can assume the role) references a specific AWS account. This is an example of how you
can associate one AWS account with another. (And is best practice for isolating data between different departments, etc.)
We'll cover how to configure the AWS bastion account side to use this role later.

The next thing to call out is the use of the `Condition` element of the policy document. To assume the role,
we require two checks to be performed.

- That the principal assuming the role (e.g. IAM User) have the tag `"access-to-production"` with value `"true"`. This way,
  we will reject any IAM User in the bastion account who isn't tagged with `"access-to-production"` from assuming this role.
- We also verify that the "external ID" (an optional parameter passed when assuming an IAM Role) matches a well-known Pulumi
  stack name. This way, we can double-check that the entity using the IAM Role is doing so to use a specific stack.
  (This is less of a security measure and more of a general hygiene type requirement.)

### IAM Policy Document

Now we have an IAM Role; we need to attach a policy document that defines what permissions are granted.

This is the **most important step** since it defines precisely what the CI/CD bot can able to do.

If we define the policy too broadly, then it is a general risk. For example, what if a compromised NPM package in your
Pulumi program did something nefarious. If the policy is defined too narrowly, then your `pulumi up` might fail because
the necessary permissions weren't available. When in doubt, err on the side of having a more restrictive policy.

> It can be advantageous to have an identical "staging" and "production" instance of the same Pulumi stack,
> so you can detect any permission issues before you update the user-facing production stack.

It can take some time to winnow down the specific set of permissions necessary since that is ultimately specific to
the Pulumi program. For example, if the stack governs the networking configuration, then you can simply not deny
to the `s3:*` actions.

Unfortunately, Pulumi doesn't currently support generating a reasonable IAM Policy document for your stack. But for a
good introduction to some of the "worst-case scenarios" that could arise from a misconfigured IAM Policy,
see [this blog post from BishopFox](https://know.bishopfox.com/research/privilege-escalation-in-aws).

The following is a hypothetical IAM policy that restricts the operations performed to just those for the
AWS CloudFront and S3 products. (Which might be sufficient for
[updating a CDN-based website hosted on AWS]({{< relref "serving-a-static-website-on-aws-with-pulumi" >}}), but
likely not much else.)

```typescript
// Policy document defining the permissions granted to the WebsiteStackUpdaterRole.
export const websiteUpdaterPolicyDocument: aws.iam.PolicyDocument = {
    Version: "2012-10-17",
    Statement: [
        // Grant access to all AWS S3 actions, but scoped to just the specific S3 buckets
        // used for the given Pulumi stack.
        {
            Sid: "GrantS3Access",
            Effect: "Allow",
            Action: "s3:*",
            Resource: [
                // Content bucket.
                "arn:aws:s3:::website-bucket",
                "arn:aws:s3:::website-bucket/*",
                // S3 bucket which stores the access logs.
                "arn:aws:s3:::website-logs-bucket",
                "arn:aws:s3:::website-logs-bucket/*",
            ],
        },
        // Grant access to update a CloudFront distribution. For more information, see:
        // https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/access-control-managing-permissions.html
        {
            Sid: "GrantCloudFrontAccess",
            Effect: "Allow",
            Action: [
                "cloudfront:CreateDistribution",
                "cloudfront:DeleteDistribution",
                "cloudfront:GetDistribution",
                "cloudfront:GetDistributionConfig",
                "cloudfront:ListDistributions",
                "cloudfront:UpdateDistribution",
                "cloudfront:ListCloudFrontOriginAccessIdentities",
            ],
            // The specific CloudFront distribution used in the stack.
            Resource: "arn:aws:cloudfront::0123456789:distribution/A123B1CABWZZ",
        },
    ],
};

const websiteUpdaterPolicy = new aws.iam.Policy("WebsiteUpdaterRolePolicy", {
    name: "WebsiteUpdaterRolePolicy",
    description: "Policy granting the permissions needed for updating the website/production Pulumi stack",
    policy: websiteUpdaterPolicyDocument,
}, resourceOptions);
```

To actually associate the IAM Policy document with the new IAM Role, we need to create a
[PolicyAttachment](https://www.pulumi.com/docs/reference/pkg/aws/iam/policyattachment/#policyattachment)
associating the two.

```typescript
const rolePolicyAttachment = new aws.iam.RolePolicyAttachment("WebsiteStackUpdaterRolePolicyAttachment", {
    role: websiteStackUpdaterRole,
    policyArn: websiteUpdaterPolicy.arn,
});
```

> Reminder, we defined the IAM Role in our production AWS account, which allows any principal in the AWS
> bastion account (with the right tag, external ID) to assume that role. We then need to update the bastion
> account to grant the `sts:AssumeRole` action on that IAM Role so it can be used! That isn't covered in this post.

### Assuming the IAM Role

Finally! With everyone in place, we can now _use_ the IAM Role.

The following is a set of commands you can run on your CI/CD worker to exchange the low-privilege IAM User
credentials for the specific IAM Role we just created in the production AWS account. But there are many
alternatives for programmatically assuming an IAM Role, such as using the
[`AWS_PROFILE` environment variable](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html))
or the [`assume-role`](https://github.com/coinbase/assume-role) tool.

```bash
# Use the AWS credentials passed to the CI system and available as environment variables.
# These are the low-privilege credentials that automatically get rotated.
aws configure set aws_access_key_id ${AWS_ACCESS_KEY_ID}
aws configure set aws_secret_access_key ${AWS_SECRET_ACCESS_KEY}
aws configure set region "${AWS_REGION:-us-west-2}"

# Assume the desired IAM Role. Note how we pass the stack name in the --external-id parameter,
# as required to assume the role.
readonly CREDS_JSON=$(aws sts assume-role \
                 --role-arn "${ARN_OF_IAM_ROLE_TO_ASSUME}" \
                 --role-session-name "<useful description of the context, such as CI/CD job ID>" \
                 --external-id "${TARGET_STACK}")

# The `aws sts assume-role` command just returns a JSON blob. So we now tease out the actual
# access key and set the corresponding environment variables.
export AWS_ACCESS_KEY_ID=$(echo "${CREDS_JSON}"     | jq ".Credentials.AccessKeyId" --raw-output)
export AWS_SECRET_ACCESS_KEY=$(echo "${CREDS_JSON}" | jq ".Credentials.SecretAccessKey" --raw-output)
export AWS_SESSION_TOKEN=$(echo "${CREDS_JSON}"     | jq ".Credentials.SessionToken" --raw-output)

# If everything worked correctly, then running the get-caller-identity command will refer to
# the IAM Role and not the IAM User we started as.
echo "Assumed AWS identity:"
aws sts get-caller-identity
```

## Storing Sensitive Data using Pulumi {#secrets-in-pulumi}

As a developer, the most critical security threat is access to your cloud account. Since that's
ultimately where your or your customer's data is stored. But beyond that, there are places where
sensitive data gets stored by Pulumi too.

Pulumi goes to great lengths to safeguard your data. Here we review where Pulumi interacts
with your sensitive data, and what you can do to safeguard it better.

### Secrets in Configuration

A Pulumi stack can have configuration data associated with it, which allows you to parameterize
cloud resources. For example, a `machine-size` configuration key might determine which class of
virtual machine to use. A dev stack might only need a `"t2.small"` but your production instance
might need something more powerful.

Configuration data is stored in a file like `Pulumi.website-production.yaml` should be checked in
along with the source code for a stack, so that builds and stack updates are reproducible.

However, what if those configuration settings contain secrets? Like you need to store an API key
to use a 3rd party API.

Pulumi supports the ability of [encrypting sensitive configuration data](https://www.pulumi.com/docs/intro/concepts/config/#secrets).
You just need to add the `--secret` flag.

```bash
# Securely add an API key to the stack's configuration.
pulumi config set api-key "hunter2" --secret
```

For stacks hosted on the [Pulumi Console](https://app.pulumi.com), the default is that your configuration
data is encrypted using a key specific to your stack. (So the ciphertext stored in the `Pulumi.yaml` file
is safe to check into your source tree, since it cannot be copied/decrypted for another stack.)

### Secrets in Checkpoint Files

Pulumi keeps track of your cloud resources in a something called a [checkpoint file]({{< ref "/docs/intro/concepts/state" >}}),
and that too might contain sensitive information. For example, a Pulumi resource might have a `"password"` output property.

Pulumi [has support]({{< ref "/docs/intro/concepts/programming-model#additionalsecretoutputs" >}}) to mark that resource
output as "secret" and make sure that it is encrypted within the checkpoint file. (So if you were to look at the checkpoint file
contents via [`pulumi stack export`]({{< ref "/docs/reference/cli/pulumi_stack_export" >}}), you would not be able to recover
the data.

Just like for secret configuration values, the default for stacks hosted on the Pulumi Console is to encrypt
this data using a key that Pulumi manages and is specific to your stack.

### Custom Secrets Providers

We at Pulumi take great care in safeguarding your data, especially configuration or checkpoint data that is marked as sensitive.
However, you might feel more comfortable if your stack's data were encrypted using a key that _you_ controlled. (So even if the
data stored on the Pulumi Console were available, it would be useless without your specific key.)

If that's the case, then you can use a configurable secrets provider, and swap out the default "Pulumi Console managed" encryption
scheme for your own. (And we won't take it personally, promise.)

When you create a new stack using [pulumi stack init]({{< ref "/docs/reference/cli/pulumi_stack_init" >}}), you can optionally
specify a `--secrets-provider` flag. That will determine the where and how of how secrets get managed on your stack.

For example, to use your own KMS key for encrypting data, you can pass the secrets provider
`"awskms://alias/ExampleAlias?region=us-east-1"`. The Pulumi command-line will work and behave the same. Except that
whenever it needs to encrypt or decrypt some data, it will refer to the custom provider.

> As you would expect, if you do use a custom secrets provider and lose access to your encryption key, then there is
> no way to recover the encrypted data stored on your stack.

For more information on custom secret providers, see
[Peace of Mind with Cloud Secret Providers]({{< relref "peace-of-mind-with-cloud-secret-providers" >}}) or
[Managing Secrets with Pulumi]({{< relref "managing-secrets-with-pulumi" >}}).

## Wrapping Up

Securely managing any sensitive data is challenging to get right. Especially if there are many moving parts, such as when
coordinating access between your AWS account, CI/CD provider, and your Pulumi stack.

In this blog series, we walked through the best practices in creating, securing, and managing access to an AWS account using
IAM Users and Roles. We then reviewed the specifics of where and how Pulumi stores sensitive data, in case you want to take
more control over your data.

If you have any other questions, corrections, or other ideas you'd like to discuss about Pulumi, Continuous Delivery, or
security, please join the conversation over on the [Pulumi Community Slack](https://slack.pulumi.com).
