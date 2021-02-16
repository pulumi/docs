---
title: "Managing AWS Credentials on CI/CD - Part 2"
date: 2020-03-26
meta_desc: "Best practices for managing AWS credentials on CI/CD - Part 2 in the series"
meta_image: key.png
authors:
    - chris-smith
    - sophia-parafina
tags:
    - CI/CD
    - secrets
---

This article is the second part of a series on best practices for securely managing AWS credentials on CI/CD. In this article, we go in-depth on providing AWS credentials securely to a 3rd party and introduce a Pulumi program to automate rotating access keys.

<!--more-->

> **NOTE:** These recommendations do not apply if you are running a CI/CD system within your
> AWS account, e.g., running a Jenkins server on EC2 or using [AWS CodeDeploy](https://aws.amazon.com/codedeploy/).
> In those cases, please refer to AWS's documentation for how to
> [assume IAM Roles when running on an EC2 instance](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html)
> instead.

Posts in this series:

- [Create a dedicated IAM User for your CI/CD]({{< relref "/blog/managing-aws-credentials-on-cicd-part-1#create-new-iam-user" >}})
- [Provide the IAM User’s credentials to your CI/CD system]({{< relref "/blog/managing-aws-credentials-on-cicd-part-2#providing-iam-credentials" >}})
- [Comparison with using hosted secret managers]({{< relref "/blog/managing-aws-credentials-on-cicd-part-2#using-a-secrets-service" >}})
- [Automate Rotating and Revoking AWS Credentials]({{< relref "/blog/managing-aws-credentials-on-cicd-part-2#automating-key-rotation" >}})
- [Assuming IAM Roles for performing updates]({{< relref "/blog/managing-aws-credentials-on-cicd-part-3#assuming-iam-roles" >}})
- [Securing sensitive data using Pulumi]({{< relref "/blog/managing-aws-credentials-on-cicd-part-3#secrets-in-pulumi" >}})

## Provide IAM credentials to your CI/CD system {#providing-iam-credentials}

In the [first post]({{< relref "/blog/managing-aws-credentials-on-cicd-part-1">}}) in our series, we created a dedicated IAM User to perform updates to AWS resources within your CI/CD system. The next step is to pass the AWS access keys for that user to your CI/CD system.

We need to take great caution. [AWS's documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) states, **"Do not provide your access keys to a third party"**.

Providing AWS access keys to any system is dangerous because of the risk that a bad actor could obtain those keys and do something nefarious. Even if your CI/CD service takes great care to protect your secrets, those AWS credentials could be inadvertently exposed in debugging output, system logs, or in some other way.

This is one of the main advantages of performing continuous deployment from within your AWS account. For example, running Jenkins on an EC2 instance you manage, or using the AWS CodeDeploy service. Because when performing a deployment from within an AWS compute environment, you can use built-in mechanisms to obtain credentials securely.

However, there are many reasons to use a hosted service for performing your CI/CD, such as developer productivity, ease of use, performance, or simply because you don't want to recreate your existing deployment workflows.

Ultimately, it is essential to understand the risks involved and how to mitigate them.

## Properly Storing Credentials

If you choose to provide your CI/CD with credentials, the most important thing is to mark them as secret. Your CI/CD provider typically has built-in support for handling "secure variables" or other sensitive information. As opposed to general, configuration data or environment variables.

User-supplied configuration values are typically write-only and only accessible by the CI/CD worker jobs at runtime. For example, Travis CI has [encrypted environment variables](https://circleci.com/docs/2.0/env-vars/#overview) or [secure environment variables](https://circleci.com/docs/2.0/env-vars/#overview) in CircleCI.

Please consult your CI/CD provider's documentation for how to pass and store sensitive information appropriately.

### Why not use a "secrets manager" service? {#using-a-secrets-service}

A common question when discussing is how to pass access keys to a CI/CD system securely:

> Rather than giving your CI/CD provider AWS credentials, why not have your CI/CD system obtain credentials from a specialized "secrets manager" service?

In other words, if you choose _not_ to trust your CI/CD system with this data, can you _instead_ trust some other system dedicated for securely storing and retrieving sensitive information?

It sounds like a good idea on the surface but doesn't seem to make your data any more secure.

Abstractly, the difference here is that the credentials are provided on-demand, rather than being available to the CI/CD job when it starts (and stored via the CI/CD provider). Instead, your CI/CD job would obtain credentials from the "secrets manager" only when needed.

There are some advantages to this approach, such as providing a clear audit trail for access and more control over the distribution of sensitive information.

However, the secrets provider system needs to be presented with some form of credentials. And _those_ credentials need to be available to your CI/CD environment. So using a secrets manager leaves you in the same place you started, i.e., needing to provide sensitive data to your CI/CD provider.

Also, by adding a dependency on a secrets manager, you introduce additional risks. Not only do you need to be even more security-conscious about that secrets manager, but it also needs to be highly available.  Any outage for that service would mean that you would be unable to perform deployments!

So it does not seem that using a secrets manager to dole out AWS credentials to your CI/CD system is a good practice to follow. Or, at the very least, makes some tradeoffs without fundamentally making your approach to CI/CD any more or less secure.

Instead, it is better to focus on other ways to reduce the risk if those AWS credentials do get exposed.

## Automate Rotating and Revoking AWS Credentials {#automating-key-rotation}

When providing credentials to a 3rd party, rather than hoping it will be 100% secure forever (which is impossible), we can make those credentials _volatile_. If we regularly invalidate and rotate the credentials supplied to the CI/CD system, we can dramatically reduce the impact of any accidental disclosure. Even if the IAM User's credentials were leaked, by the time they were discovered and used, they would no longer be valid.

The AWS security blog describes how to [rotate access keys for IAM Users](https://aws.amazon.com/blogs/security/how-to-rotate-access-keys-for-iam-users/), by using the following steps:

1. Create a second access key in addition to the one in use.
1. Update all your applications to use the new access key.
1. Change the state of the previous access key to inactive.
1. Verify everything is still working as expected.
1. Delete the inactive access key.

That all sounds simple enough, but it's certainly tedious. And if you need to repeat the process across dozens, if not hundreds of different CI/CD pipelines, you need a better solution. Fortunately, Pulumi provides an excellent and extensible way for writing a serverless program to
automate rotating credentials.

The next few sections describe a simple infrastructure application for automating AWS IAM credential rotation. You can see the full application on GitHub at
[chrsmith/pulumi-aws-travis-cicd-demo](https://github.com/chrsmith/pulumi-aws-travis-cicd-demo).

### AWS Credential Rotator 9000

The affectionally titled _AWS Credential Rotator 9000_ is a simple, serverless Pulumi application for rotating AWS access keys.

It creates an AWS lambda function that's triggered on a regular schedule, e.g., every 30 minutes, and performs the next step in the sequence for rotating access keys as outlined above.

First, it creates a new access key and pushes the new value out. On the next iteration, it marks the older access key as "inactive."  On the following iteration, the inactive key is deleted. The process repeats, generating a new key and removing the inactive key.

### Periodically Invoking an AWS Lambda

The heart of the application is triggering it to execute on a fixed interval. Thankfully this is super-easy to do using Pulumi since it allows you to seamlessly blend your "cloud infrastructure" with "code" in a natural way. The user guide for Pulumi Crosswalk for AWS has more information on [serverless eventing]({{< relref "/docs/guides/crosswalk/aws/lambda" >}})
if you would like to learn more.

The following snippet is the core part of the credential rotator app. We define a function to handle the logic of key rotation in `rotateIAMUserKeys`. Then we create an AWS Lambda resource
named `lambda`. Finally, the `triggerSchedule` resource invokes our lambda on a fixed schedule, thereby ensuring that the key rotation process goes on indefinitely. You can see the full code
[here](https://github.com/chrsmith/pulumi-aws-travis-cicd-demo/blob/master/infrastructure/key-rotator/iam-key-rotator.ts).

```ts
async function rotateIAMUserKeys(iamUser: aws.iam.User, onNewCredentials: (key: string, secret: string) => Promise<void>) {
    ...
}

const lambda = new aws.lambda.CallbackFunction<aws.cloudwatch.EventRuleEvent, void>(
    "keyRotatorLambda",
    {
        callback: async (e) => {
            await rotateIAMUserKeys(userToRotate, async (newKey: string, newSecret: string) => {
                console.log("onNewCredentials callback called!");
                console.log(`A new AWS access key "${newKey}" has been created.`);
            });
        },

        role: lambdaRole,
        runtime: "nodejs10.x",
    });

const triggerSchedule = aws.cloudwatch.onSchedule(
    "keyRotatorScheduler", "rate(1 hour)", lambdaCallbackFn);
```

When writing reusable infrastructure components in Pulumi however, it is helpful to organize things into a [custom resource]({{< ref "/docs/intro/concepts/resources#custom-resources" >}}).

For example, we can bundle together the AWS Lambda, CloudWatcn schedule, and the associated IAM policies into a single conceptual resource `AccessKeyRotator`. Bundling resources allows for the code reuse.

```ts
const rotator = new AccessKeyRotator("rotator", {
    interval: config.require("rate"),
    user: user,
    credentialPusher: demoTravisCIPusher,
})
```

### Pushing Credentials

With the mechanics of updating an AWS access key out of the way, the next step is to notify dependent systems what the new access key should be. The key rotator app has a `CredentialPusher` abstraction to provide a pluggable way for you to send credentials to where they need to be. The example on GitHub only supports updating a Travis CI project (See [`credential-pusher-travis.ts`](https://github.com/chrsmith/pulumi-aws-travis-cicd-demo/blob/master/infrastructure/key-rotator/credential-pusher-travis.ts).), but  it could be easily extended to support other CI/CD
systems.

The following snippet shows how the `CredentialPusher` is configured in the key rotator app. We load a Travis CI access token from the
[Pulumi stack's configuration](https://www.pulumi.com/docs/intro/concepts/config/), and hard-code the specific set of projects and encrypted environment variables to
store the new access key.

```ts
// A "credential pusher" is the component that pushes new AWS IAM credentials out to 3rd parties
// as the older ones get rotated. For demonstration purposes, this updates the Travis CI settings
// for the chrsmith/pulumi-aws-travis-cicd-demo repo. But you can imagine another implementation
// that pushes the new IAM credentials to GitLab CI, or updating multiple CI/CD pipelines.

const demoTravisCIPusher = new CredentialPusher(
    new TravisCIPusher(),
    {
        accessKey: config.require("travis-ci-token"),
        projects: [
            {
                project: "chrsmith/pulumi-aws-travis-cicd-demo",
                // In the Travis CI configuration for that GitHub repo, there are two
                // environment variables for storing the AWS credentials. So whenever the
                // AWS credentials get rotated, the job's configuration settings will be
                // updated to reflect the new values.
                accessKeyIDLocation: "AWS_ACCESS_KEY_ID",
                secretAccessKeyLocation: "AWS_SECRET_ACCESS_KEY",
            }
        ],
    });
```

### Demo

To demonstrate the access keys rotation, we can examine the log files generated from AWS Lambda. These can be accessed from the command-line using the [`pulumi logs`]({{< ref "/docs/reference/cli/pulumi_logs" >}}) command.

Here's a summary of the output for clarity:

```bash
 START RequestId: 9406913e-a9d0-46a4-b861-2efdee508b2b Version: $LATEST
    9406913e-a9d0-46a4-b861-2efdee508b2b    INFO    IAM User has 2 keys:
    9406913e-a9d0-46a4-b861-2efdee508b2b    INFO     - AKIASHIVKXX3QEQNZNX5 [Active] Tue Mar 24 2020 12:37:03 GMT+0000 (Coordinated Universal Time)
    9406913e-a9d0-46a4-b861-2efdee508b2b    INFO     - AKIASHIVKXX3SA2K3ME7 [Inactive] Tue Mar 24 2020 09:37:03 GMT+0000 (Coordinated Universal Time)
    9406913e-a9d0-46a4-b861-2efdee508b2b    INFO    Deleting older, inactive access key AKIASHIVKXX3SA2K3ME7 [Inactive]
    9406913e-a9d0-46a4-b861-2efdee508b2b    INFO    Key rotation step complete.
 END RequestId: 9406913e-a9d0-46a4-b861-2efdee508b2b

 START RequestId: 05644e4a-81a4-4197-8ad7-fc3517998270 Version: $LATEST
    05644e4a-81a4-4197-8ad7-fc3517998270    INFO    IAM User has 1 keys:
    05644e4a-81a4-4197-8ad7-fc3517998270    INFO     - AKIASHIVKXX3QEQNZNX5 [Active] Tue Mar 24 2020 12:37:03 GMT+0000 (Coordinated Universal Time)
    05644e4a-81a4-4197-8ad7-fc3517998270    INFO    Created new key key AKIASHIVKXX3YX4IXRVH
    05644e4a-81a4-4197-8ad7-fc3517998270    INFO    Pushing out the new key to 3rd party services...
    05644e4a-81a4-4197-8ad7-fc3517998270    INFO    Pushing new credentials to Travis CI project 'chrsmith/pulumi-aws-travis-cicd-demo'
    05644e4a-81a4-4197-8ad7-fc3517998270    INFO    Updating env var 'AWS_ACCESS_KEY_ID' (b246ab3b-c4cb-e76f-a6fc-50f4cbf451c0)
    05644e4a-81a4-4197-8ad7-fc3517998270    INFO    Updated AWS access key ID. Got response code (200)
    05644e4a-81a4-4197-8ad7-fc3517998270    INFO    Updating env var 'AWS_SECRET_ACCESS_KEY' (ba9ac4be-fbb3-4da9-c5b8-35a1afe9e02b)
    05644e4a-81a4-4197-8ad7-fc3517998270    INFO    Updated AWS secret access key. Got response code (200)
    05644e4a-81a4-4197-8ad7-fc3517998270    INFO    Key rotation step complete.
 END RequestId: 05644e4a-81a4-4197-8ad7-fc3517998270

 START RequestId: ca204959-32a7-44a8-ba20-738d139542ba Version: $LATEST
    ca204959-32a7-44a8-ba20-738d139542ba    INFO    IAM User has 2 keys:
    ca204959-32a7-44a8-ba20-738d139542ba    INFO     - AKIASHIVKXX3YX4IXRVH [Active] Tue Mar 24 2020 15:37:03 GMT+0000 (Coordinated Universal Time)
    ca204959-32a7-44a8-ba20-738d139542ba    INFO     - AKIASHIVKXX3QEQNZNX5 [Active] Tue Mar 24 2020 12:37:03 GMT+0000 (Coordinated Universal Time)
    ca204959-32a7-44a8-ba20-738d139542ba    INFO    Invalidating older access key AKIASHIVKXX3QEQNZNX5
    ca204959-32a7-44a8-ba20-738d139542ba    INFO    Key rotation step complete.
 END RequestId: ca204959-32a7-44a8-ba20-738d139542ba

 START RequestId: de753fb4-0720-4f4f-a7aa-ad6b9d4c8832 Version: $LATEST
    de753fb4-0720-4f4f-a7aa-ad6b9d4c8832    INFO    IAM User has 2 keys:
    de753fb4-0720-4f4f-a7aa-ad6b9d4c8832    INFO     - AKIASHIVKXX3YX4IXRVH [Active] Tue Mar 24 2020 15:37:03 GMT+0000 (Coordinated Universal Time)
    de753fb4-0720-4f4f-a7aa-ad6b9d4c8832    INFO     - AKIASHIVKXX3QEQNZNX5 [Inactive] Tue Mar 24 2020 12:37:03 GMT+0000 (Coordinated Universal Time)
    de753fb4-0720-4f4f-a7aa-ad6b9d4c8832    INFO    Deleting older, inactive access key AKIASHIVKXX3QEQNZNX5 [Inactive]
    de753fb4-0720-4f4f-a7aa-ad6b9d4c8832    INFO    Key rotation step complete.
 END RequestId: de753fb4-0720-4f4f-a7aa-ad6b9d4c8832
```

As you can see, the AWS credentials for the IAM User are automatically updated every few hours. And whenever a new access key is created, the value is pushed out to the impacted Travis CI projects automatically.

## Wrapping Up

In this post, we covered some of the things to consider when providing AWS credentials to your CI/CD system. (In short, be cautious and follow best practices.)

We then showed how relatively easy it is to stand up a Pulumi infrastructure application for automatically rotating AWS access keys and updating your CI/CD system. By rotating credentials, you can limit the impact if the value is inadvertently disclosed.

At this point, we've now given access keys to a CI/CD system for a low-privilege AWS IAM User account. But we still can't _do_ anything with it. The IAM User whose credentials we have given to the CI/CD system doesn't have access to your production AWS account.

In the next post, we'll go into the details about IAM Roles, and they can be used to securely and temporarily gain access to additional resources. This is how our low-privilege IAM User can access needed to update production data for your CI/CD pipelines.
