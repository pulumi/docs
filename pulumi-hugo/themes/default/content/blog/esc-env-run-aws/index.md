---
title: "From Zero to esc run"
authors: ["torian-crane"]
tags: ["aws", "secrets", "credentials-management"]
meta_desc: "From Zero to esc run placeholder area for blog content."
date: "2023-10-25"
meta_image: "meta.png"
---

In a world where cloud computing is the backbone of modern applications, managing environments and secrets is of the utmost importance. Earlier this month we released a new service called [Pulumi ESC (Environments, Secrets, and Configuration)](https://www.pulumi.com/product/esc/), the focus of which is to help alleviate the burden of managing cloud configuration by providing a centralized way to handle these critical aspects of cloud development. It's like having a Swiss Army knife in your toolkit, ready to tackle the challenges of cloud infrastructure. This post is the first post in a series that will highlight the specific challenge of **credentials management**, and we’ll specifically dive into how using the `esc run` functionality of Pulumi ESC will make that easier.

<!--more-->

## The Power of esc run

The [Pulumi documentation for the `esc run` command](https://www.pulumi.com/docs/esc-cli/commands/esc_run/) states the following:

> This command opens the environment with the given name and runs the given command. If the opened environment contains a top-level ’environmentVariables’ object, each key-value pair in the object is made available to the command as an environment variable.

But what does this actually mean? If we use AWS as an example, it means that we can run commands like `aws s3 ls` without the need to configure AWS credentials locally each time. It’s a significant stride towards making your cloud interactions more efficient and less error-prone, and here’s a deeper dive into why:

- **Seamless Command Execution** - The `esc run` command lets you execute AWS commands effortlessly, freeing you from the intricacies of managing AWS credentials on your local machine. Simply put, it significantly reduces the overhead of credential setup and maintenance.

- **Enhanced Security** - One of the standout features of `esc run` is its commitment to security. By removing the local storage of credentials, it drastically reduces the risk of accidental exposure. Your credentials and secrets are securely managed within the Pulumi environment.

- **Streamlined Collaboration** - Because credentials will be centralized, `esc run` facilitates smoother team collaboration by providing a consistent environment for all team members to run commands with. Everyone can access the same secure environment which reduces the complexities of coordinating credentials and configurations across teams.

## Getting Started with esc run

Now that we've covered why `esc run` is so valuable, let's dive into how you can start using it! We'll walk you through everything you need to do to run the `aws s3 ls` command without configuring local AWS credentials.

### Step 1: Install and login to Pulumi ESC

To begin, you’ll need to [install Pulumi ESC](https://www.pulumi.com/docs/install/esc/). Once the installation is complete, run the `esc login` command and follow the steps to login to the CLI.

```
$ esc login
Manage your Pulumi ESC environments by logging in.
Run `esc --help` for alternative login options.
Enter your access token from https://app.pulumi.com/account/tokens
    or hit <ENTER> to log in using your browser                   :  
Logged in to pulumi.com as …
```

### Step 2: Create the OIDC configuration

While you can [manually set your credentials as secrets](https://www.pulumi.com/docs/esc-cli/commands/esc_env_set/) in your Pulumi ESC environment files, it isn’t a recommended best practice to create or maintain long-lived credentials for your cloud environments. A more secure and efficient alternative is to leverage yet another great feature of Pulumi ESC: dynamic credentials.

Pulumi ESC can dynamically generate credentials on your behalf each time you need to interact with your AWS environments. To do so, you'll need to [configure OpenID Connect (OIDC) between Pulumi and AWS](https://www.pulumi.com/docs/pulumi-cloud/esc/providers/#setting-up-oidc). On the AWS side, there are two resources you'll need to create:

- An IAM OIDC provider
- An IAM Role

Let's start by creating the OIDC provider resource. There are a number of ways you can do this in AWS, but we will demonstrate how to create it via the AWS console.

{{< notes type="info" >}}
Please note that while we’re providing the steps and screenshots that are accurate as of the date of this post, AWS documentation is subject to change. For the most current and precise information, always refer to the [official AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html).
{{< /notes >}}

#### a. Add identity provider

In the navigation pane of the [IAM console](https://console.aws.amazon.com/iam/), choose **Identity providers**, and then choose **Add provider**.

{{< video title="Navigating to the IAM console and opening the Create Identity Provider wizard" src="./create-idp-start.mp4" autoplay="true" loop="true" >}}

In the **Provider type** section, click the radio button next to **OpenID Connect**. For the **Provider URL**, provide the following URL:

```
https://api.pulumi.com/oidc
```

Then click the **Get thumbprint** button. The thumbprint value that you will be presented with is what you can use to verify the certificate of the provider i.e. Pulumi.

{{< notes type="info" >}}
The AWS console generates the thumbprint value on your behalf. However, if you are creating the OIDC provider programmatically, you will need to generate this value yourself and provide the thumbprint value as a part of your resource definition. You can learn more about what a thumbprint is and how to generate/verify it by referring to the [relevant AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc_verify-thumbprint.html).
{{< /notes >}}

For the **Audience** field, provide the name of your Pulumi organization. Then scroll down to the bottom of the page and click **Add provider**.

{{< video title="Filling out the fields of the Create Identity Provider wizard" src="./create-idp-wizard.mp4" autoplay="true" loop="true" >}}

#### b. Assign IAM role

You’ll see a notification at the top of your screen prompting you to assign an IAM role to your newly created provider. Click the **Assign role** button.

This will prompt you to either create a new role or use an existing role. For the purposes of this blog, we will select the **Create a new role** option and demonstrate how to configure it for use with Pulumi ESC.

{{< video title="Prompt for assigning IAM role" src="./assign-iam-role-prompt.mp4" autoplay="true" loop="true" >}}

This will then direct you to the IAM **Create role** page. The **Web identity** radio button should already be selected for you but if not, make sure that it is selected. Then scroll down and make sure that the following is selected in the **Web identity** section:

- the `api.pulumi.com/oidc` provider is selected under **Identity provider**
- the name of your Pulumi organization is selected under **Audience**

{{< video title="Create IAM role wizard" src="./create-role-wizard.mp4" autoplay="true" loop="true" >}}

Click **Next** which will direct you to the **Add permissions** page. This is where you will select what permissions you will allow your Pulumi ESC environment to have in your AWS account. Since we want to interact with S3, let’s go ahead and select the **AmazonS3FullAccess** policy from the list. Then scroll down and click **Next**.

{{< video title="Adding S3 permissions to IAM role" src="./create-role-add-perms.mp4" autoplay="true" loop="true" >}}

You will be directed to the last page of the wizard, where you can provide the name and an optional description for the role and review all of the role’s configuration details before creating it.

{{< video title="Adding name and description to role then creating it" src="./create-role.mp4" autoplay="true" loop="true" >}}

#### c. Review trust policy

One area that we want to draw your attention to is the **Select trusted entities** section which is where the trust policy of the role is defined.

![An image of the IAM role trust policy](./review-trust-policy.png)

This definition currently allows any Pulumi service to assume this role, but only if the request comes from your organization. You can edit this policy to further limit access to this role to just the Pulumi ESC service, and you can make it even more granular by limiting access to a specific environment. This more detailed configuration is outside the scope of this blog post, but you can learn more about it by checking out the [relevant Pulumi documentation](https://www.pulumi.com/docs/pulumi-cloud/esc/providers/aws-login/#configuring-the-iam-role-and-trust-policy).

After creating your role, make sure to make a note of your role’s ARN value as you will need it in the next step.

### Step 3: Create a new environment

Now that we’ve created all the necessary AWS resources, let’s move over to the Pulumi side of things. You’ll first want to create a new environment in the [Pulumi Cloud](https://app.pulumi.com/). Make sure that you have the correct organization selected in the left-hand navigation menu. Then click the **Environments** link, and click the **Create environment** button. In the following pop-up, provide a name for your environment before clicking the  **Create environment** button.

{{< video title="Creating a new Pulumi ESC environment" src="./create-new-environment.mp4" autoplay="true" loop="true" >}}

### Step 4: Add the AWS provider integration

Once you’ve created your new environment, you will be presented with a split-pane editor view. You’ll want to clear out the default placeholder content in the editor on the left-hand side and replace it with the following code, making sure to provide the value of your IAM role ARN from the previous step:

```
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: <your-oidc-iam-role-arn>
          sessionName: pulumi-environments-session
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}
```

The variables defined under the `environmentVariables` parameter above are the same environment variables that AWS uses when you’re locally authenticating using the AWS CLI. You can find out more about this provider definition and how it works in the Pulumi ESC documentation for [the AWS provider](https://www.pulumi.com/docs/pulumi-cloud/esc/providers/aws-login/#example) as well as the documentation for [projecting environment variables](https://www.pulumi.com/docs/pulumi-cloud/esc/environments/#projecting-environment-variables).

Scroll to the bottom of the page and click **Save**.

{{< video title="Adding configuration to Pulumi ESC environment" src="./add-environment-config.mp4" autoplay="true" loop="true" >}}

### Step 5: Run your command

Now to the fun part! With your environment set up, try it out by listing all of the S3 buckets in your AWS account. Start by running the `aws s3 ls` command as normal, making sure that the environment that you're working from does not have any AWS credentials configured. You should see the following response:

```
$ aws s3 ls

Unable to locate credentials. You can configure credentials by running "aws configure".
```

Now run the command using `esc run` as shown below, making sure to replace the placeholder text with the names of your own Pulumi organization and environment:

```
esc run <your-pulumi-org-name>/<your-environment-name> -i aws s3 ls
```

Voila! You’ve just run an AWS command without any local AWS credential configuration. This is just the tip of the iceberg of how the `esc run` command can be a game-changer in how you and your team manage and interact with cloud resources.

{{< notes type="info" >}}
Manually navigating through the steps of configuring an OIDC provider in AWS can be a bit of a puzzle. However, we've got you covered! We've also crafted an automated [example](https://github.com/pulumi/examples/tree/master/aws-py-oidc-provider-pulumi-cloud) using Pulumi Infrastructure as Code (IaC). Dive in and explore how we've simplified the process!
{{< /notes >}}

## Real-World Use Case: Automated Data Backup

To further illustrate the power of Pulumi ESC, let's consider a real-world use case: automated data backup. Imagine you have a web application that generates daily logs stored in an S3 bucket. You want to schedule a daily backup job to copy these logs to a separate bucket without exposing your AWS credentials in your scripts or having to manually configure them each time.

With Pulumi ESC, you can create an environment, dynamically generate and securely store your AWS credentials, and schedule a daily backup job using a simple script that runs the `aws s3 cp` command. This ensures your backups are automated, secure, and easily maintainable, all thanks to Pulumi ESC.

## Conclusion

Pulumi ESC, and the `esc run` command in particular, are designed to make your cloud journey smoother, more secure, and less daunting. So, the next time you find yourself drowning in a sea of cloud configurations, remember, with Pulumi ESC and a dash of code, you can say goodbye to manual configuration hassles and hello to efficient, secure, and scalable cloud development with Pulumi ESC. Feel free to [join our community on Slack](https://slack.pulumi.com/) and let us know what you think!
