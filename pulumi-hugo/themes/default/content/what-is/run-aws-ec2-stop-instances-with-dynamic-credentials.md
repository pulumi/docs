---
title: Run 'aws ec2 stop-instances' using Dynamic Credentials
meta_desc: |
     Learn how to use dynamic credentials in Pulumi ESC for executing commands like 'aws ec2 stop-instances' in a more secure and efficient manner.

type: what-is
page_title: Run 'aws ec2 stop-instances' using Dynamic Credentials
---

The [`aws ec2 stop-instances` command](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/stop-instances.html) is part of the AWS Command Line Interface (CLI) and is utilized for stopping Amazon Elastic Compute Cloud (Amazon EC2) instances that are currently running. Amazon EC2 provides scalable computing capacity in the AWS cloud, enabling users to launch and manage virtual servers as per their requirements.

Using the `aws ec2 stop-instances` command is key in managing EC2 instances, providing an easy way to bring an instance into an inactive state. This command is executed in the terminal using the AWS CLI and necessitates proper management of AWS credentials for security. Typically, there are two kinds of credentials used: temporary credentials, offering heightened security but requiring manual updates, and long-term credentials, which are more convenient but pose greater security risks.

With [Pulumi ESC (Environments, Secrets, and Configurations)](/docs/pulumi-cloud/esc/), handling these credentials becomes simpler and more secure. Pulumi ESC facilitates [managing dynamic credentials from AWS using OIDC](/blog/esc-env-run-aws/), ensuring all your AWS CLI commands, including `aws ec2 stop-instances`, are executed seamlessly. This approach eliminates concerns over invalid credentials and reduces the risks associated with manual credential management.

## Using Pulumi ESC for dynamic credentials with AWS

[Pulumi ESC](https://www.pulumi.com/product/esc/) is a service that helps to alleviate the burden of managing cloud configuration and secrets by providing a centralized way to handle these critical aspects of cloud development. The `esc run` command of this service in particular helps to resolve concerns around how to:

- Securely share credentials with teammates in a consistent way.
- Minimize the risks associated with locally configured, long-lived and highly privileged credentials.
- Ensure teams can easily and safely run commands like aws ec2 stop-instances without requiring deep security expertise.

## What is the esc run command?

The [Pulumi documentation for the `esc run` command](https://www.pulumi.com/docs/esc-cli/commands/esc_run/) states the following:

> This command opens the environment with the given name and runs the given command. If the opened environment contains a top-level ’environmentVariables’ object, each key-value pair in the object is made available to the command as an environment variable.

But what does this actually mean? If we use AWS as an example, it means that we can run commands like `aws ec2 stop-instances` without the need to configure AWS credentials locally each time. It’s a significant stride towards making your cloud interactions more efficient and less error-prone, and here’s a deeper dive into why:

- **Seamless Command Execution** - The `esc run` command lets you execute AWS commands effortlessly, freeing you from the intricacies of managing AWS credentials on your local machine. Simply put, it significantly reduces the overhead of credential setup and maintenance.

- **Enhanced Security** - One of the standout features of `esc run` is its commitment to security. By removing the local storage of credentials, it drastically reduces the risk of accidental exposure. Your credentials and secrets are securely managed within the Pulumi environment.

- **Streamlined Collaboration** - Because credentials will be centralized, `esc run` facilitates smoother team collaboration by providing a consistent environment for all team members to run commands with. Everyone can access the same secure environment which reduces the complexities of coordinating credentials and configurations across teams.

## Getting started with esc run

### Step 1: Install and login to Pulumi ESC

To begin, you’ll need to [install Pulumi ESC](/docs/install/esc/). Once the installation is complete, run the `esc login` command and follow the steps to login to the CLI.

```bash
$ esc login
Manage your Pulumi ESC environments by logging in.
Run `esc --help` for alternative login options.
Enter your access token from https://app.pulumi.com/account/tokens
    or hit <ENTER> to log in using your browser                   :  
Logged in to pulumi.com as …
```

### Step 2: Create the OIDC configuration

Pulumi ESC offers you the ability to manually set your credentials as secrets in your Pulumi ESC environment files. When it comes to something like OIDC configuration, a more secure and efficient alternative is to leverage yet another great feature of Pulumi ESC: dynamic credentials.

This service can dynamically generate credentials on your behalf each time you need to interact with your AWS environments. To do so, follow the steps in the [guide for configuring OIDC between Pulumi and AWS](/docs/pulumi-cloud/oidc/aws/). Make sure that the IAM role you create has sufficient permissions to perform EC2 actions.

### Step 3: Create a new Pulumi ESC environment

Once OIDC has been configured between Pulumi and AWS, the next steps is to create a new environment in the [Pulumi Cloud](https://app.pulumi.com/). Make sure that you have the correct organization selected in the left-hand navigation menu. From there, click the **Environments** link, then click the **Create environment** button. In the following pop-up, provide a name for your environment before clicking the **Create environment** button.

{{< video title="Open environment in Pulumi ESC console" src="/what-is/esc-create-new-env.mp4" autoplay="true" loop="true" >}}

### Step 4: Add the AWS provider integration

Once you’ve created your new environment, you will be presented with a split-pane editor view. You’ll want to clear out the default placeholder content in the editor on the left-hand side and replace it with the following code, making sure to replace <your-oidc-iam-role-arn> with the value of your IAM role ARN from the configure OIDC step:

```yaml
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

### Step 5: Run the aws ec2 stop-instances command

First check that your local environment does not have any AWS credentials configured by running the `aws configure list` command as shown below:

```bash
$ aws configure list
      Name                    Value             Type    Location
      ----                    -----             ----    --------
   profile                <not set>             None    None
access_key                <not set>             None    None
secret_key                <not set>             None    None
    region                <not set>             None    None
```

You can then use the following command to stop a running instance as shown below, making sure to replace `<your-pulumi-org-name>`, `<your-environment-name>`, and `<your-running-instance-id>` with the names of your own Pulumi organization, environment, and desired EC2 instance ID respectively:

```bash
esc run <your-pulumi-org-name>/<your-environment-name> -- aws ec2 stop-instances --instance-ids <your-running-instance-id>
```

## Conclusion

Pulumi ESC makes it easier than ever to tame infrastructure complexity, especially when running commands like aws ec2 stop-instances. Pulumi ESC supports dynamic credentials using OIDC across AWS, Azure, and Google Cloud. Check out the following links to learn more about Pulumi ESC today.

- [Getting Started](/docs/pulumi-cloud/esc/get-started)
- [Documentation](/docs/pulumi-cloud/esc)
- [Open Source](https://github.com/pulumi/esc)

Feel free to [join our community on Slack](https://slack.pulumi.com/) and let us know what you think!
