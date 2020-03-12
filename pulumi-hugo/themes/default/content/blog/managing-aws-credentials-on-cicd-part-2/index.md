---
title: "Managing AWS Credentials on CI/CD - Part 2"
date: 2020-03-12
meta_desc: "Best practices for managing AWS credentials on CI/CD - Part 2 in the series"
meta_image: meta.png
authors:
    - chris-smith
    - sophia-parafina
tags:
    - CI/CD
---

This is the second part in a series on the best practices for securely managing AWS credentials on
CI/CD. In this second part we will go in-depth on how to securely handle providing AWS credentials
to a 3rd party. (That's a dubious proposition, so we will also cover a Pulumi program for automatically
rotating those credentials is provided too, in order to mitigate the risks.)

<!--more-->

> **NOTE:** These recommendations do not apply if you are running your own CI/CD system within your
> AWS account, e.g., running a Jenkins server on EC2 or using [AWS CodeDeploy](https://aws.amazon.com/codedeploy/).
> In those cases, please refer to AWS's documentation for how to
> [assume IAM Roles when running on an EC2 instance](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html)
> instead.

Other posts in this series:

- [Create a dedicated IAM User for your CI/CD](--- link to other blog post ---)
- [Provide the IAM User’s credentials to your CI/CD system](--- link to heading in this post---)
- [Automating IAM credential rotation using Pulumi](--- link to heading in this post ---)
- _Assuming IAM Roles for performing updates_ (coming soon!)
- _Securing sensitive data using Pulumi_
- _Comparison with using hosted sercret managers_ [--- delete since it a subscection of this post ---]


## Provide that IAM credentials to your CI/CD system {#providing-iam-credentials}

In the [first post](---link-to-blog-post--) in our series, we created a dedicated IAM User who will
be used to perform updates to AWS resources within your CI/CD system. The next step is to then give
credentials for that user to your CI/CD user, so that they are available at build-time.

We need to take great caution here. [AWS’s documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)
states, **“Do not provide your access keys to a third party.”**

Providing AWS access keys to any system is dangerous because of the risk that a bad actor could
acquire those keys to do something nefarious. Even if your CI/CD service takes great care to
protecting your secrets, those AWS credentials could be inadvertently exposed in debugging
output, system logs, or some other way.

This is one of the main advantages of performing continuous deployment from within your own AWS account.
(For example, running Jenkins on an EC2 instance you manage, or using the AWS CodeDeploy service.) Because
when you are performing a deployment from within an AWS compute environment, you can use built-in mechanisms
to securely obtain credentials.

However, there are plenty of reasons to use a hosted service for performing your CI/CD as well. Ranging
from developer productivity, to ease of use and performance, to simply maintaining the current system
you have in-place already. It ultimately boils down to understanding the risks involved, and how to mitigate them.

> It is worth calling out that your CI/CD system could provide a hook for it to assume a role
> within your AWS account. That is, you could create an IAM Role policy that grants <3rd party service>
> the permissions needed to update the resources managed by a Pulumi program.
>
> If your CI/CD provider has such a feature, then taking advantage of that capability would provide
> a safer, and simpler approach for managing secrets. See your CI/CD provider's documentation to check
> if they offer such a feature.

### Why not use a "secrets manager" service?

> Rather than giving your CI/CD provider AWS credentials, why not have your CI/CD system obtain credentials
> from a specialized "secrets manager" type service?

This sounds like a good idea on the surface, but doesn't seem to make your data any more secure.

Abstractly the difference here is that the credentials are provided on-demand, rather than being
available to the CI/CD job when it starts. There are some advantages to this approach, but
in the context of accessing sensitive information within a CI/CD environment, it doesn't fundamentally
change the equation.

That secrets provider system needs to be presented with some form of credentials, too. And _those_
credentials need to be available to your CI/CD environment. So it's possible the secrets manager
leaves you in the same place you started: uneasy with providing sensitive data to your CI/CD provider.

And that isn't consider the additional security risks from having a high-value target like as a centeralized
credential service. Not only do you need to lockdown that service, but it also needs to be highly
available too. (Since any type of service disruption would mean that you would be unable to perform
deployments.)

So it does not seem that using a secrets manager to dole out AWS credentials to your CI/CD system
is a good practice to follow. And instead, focusing on other ways to reduce the risk if those
AWS credentials do get exposed.

### Properly Storing Credentials

If we do choose to provide credentials to a 3rd party, rather than hoping it will be 100% secure
forever (which is impossible), we can instead make those credentials _volatile_. If we regularly
invalidate and rotate the credentials given supplied to CI/CD system, we can dramatically reduce
the impact of any accidental disclosure. (Since even if the IAM User’s credentials were leaked, by
the time they were discovered and used, they would no longer be valid.)


While key rotation may thwart a compromised credential, we still need to take precautions to ensure that they are correctly stored.

Your CI/CD provider likely has built-in support for handling “secrets” or “secure variables.” Typically these are user-supplied configuration values that are write-only and only accessible by the CI/CD worker jobs at runtime. For example, Travis CI has [encrypted environment variables](https://circleci.com/docs/2.0/env-vars/#overview) or [secure environment variables](https://circleci.com/docs/2.0/env-vars/#overview) in CircleCI.

## Automate Rotating and Revoking those Credentials

When a CI/CD system has access to an IAM User’s AWS credentials, we need to take steps to rotate those credentials regularly, even if we trust the CI/CD provider to secure them properly.

This is one of the advantages of running your CI/CD system within your AWS account. If your deployment workers are EC2 instances, you wouldn’t need to share IAM User credentials. The EC2 instances [can be configured to assume an IAM Role](https://aws.amazon.com/blogs/security/new-attach-an-aws-iam-role-to-an-existing-amazon-ec2-instance-by-using-the-aws-cli/). The details about how IAM Roles are a more secure alternative to IAM User credentials are covered in the next section.

“Just create a new IAM User credential, log into the CI/CD system, and then update the job’s settings” sounds simple enough. But it’s likely going to be tedious, and if you need to repeat the process for dozens if not hundreds of CI/CD pipelines, you need a better solution. Unless you start with an automated approach for key rotation, you are unlikely to add one later.

The AWS security blog describes how to [rotate access keys for IAM Users](https://aws.amazon.com/blogs/security/how-to-rotate-access-keys-for-iam-users/).

1. Create a second access key in addition to the one in use.
1. Update all your applications to use the new access key and validate that the applications are working.
1. Change the state of the previous access key to inactive.
1. Validate that your applications are still working as expected.
1. Delete the inactive access key.


Alternatives: External Systems for Key Exchange
The guide has described the best practices for securing a CI/CD system using AWS. But you still might not be convinced that giving any AWS credentials to your CI/CD system is “secure enough”. Ultimately, it boils down to a matter of trust and risk tolerance.

When talking to other developers trying to automate DevOps as securely as possible, a common practice is to rely on an external tool or server to handle key exchange. So rather than providing credentials directly to the CI/CD system which would be available on each deployment, each deployment job would request credentials specifically for that job.
