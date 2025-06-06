---
title: Run 'aws s3 sync' with Dynamic Credentials
meta_desc: |
     Learn how to use dynamic credentials in Pulumi ESC for executing commands like 'aws s3 sync' more securely and efficiently.

type: what-is
page_title: Run 'aws s3 sync' with Dynamic Credentials
---

The [`aws s3 sync`](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html) command is part of the AWS Command Line Interface (CLI) and synchronizes files and directories between your local file system and Amazon S3 buckets. This command simplifies uploading files to and downloading files from S3.

The `aws s3 sync` command can be a powerful tool, especially when dealing with large datasets or multiple files. This command is executed in the terminal using the AWS CLI and necessitates proper management of AWS credentials. Typically, two kinds of credentials are used: temporary credentials, which offer heightened security but require manual updates, and long-term credentials, which are more convenient but pose more significant security risks.

With [Pulumi ESC (Environments, Secrets, and Configurations)](/docs/pulumi-cloud/esc/), handling these credentials becomes more straightforward and secure. Pulumi ESC facilitates [managing dynamic credentials from AWS using OIDC](/blog/esc-env-run-aws/), ensuring all your AWS CLI commands, including `aws s3 sync`, execute successfully. This approach eliminates concerns over invalid credentials and reduces the risks associated with manual credential management.

## Using Pulumi ESC for dynamic credentials with AWS

[Pulumi ESC](https://www.pulumi.com/product/esc/) is a service that helps to alleviate the burden of managing cloud configuration and secrets by providing a centralized way to handle these critical aspects of cloud development. The `esc run` command of this service, in particular, helps to resolve concerns around how to:

- Share credentials with teammates consistently and securely.
- Minimize the risks associated with locally configured, long-lived, and highly privileged credentials.
- Ensure teams can quickly and safely run commands like `aws s3 sync` without requiring deep security expertise.

## What is the esc run command?

The [Pulumi documentation for the `esc run` command](/docs/esc/cli/commands/esc_run/) states the following:

> This command opens the environment with the given name and runs the given command. If the opened environment contains a top-level ’environmentVariables’ object, each key-value pair in the object is made available to the command as an environment variable.

But what does this actually mean? If we use AWS as an example, it means that we can run commands like `aws s3 sync` without the need to configure AWS credentials locally each time. It’s a significant stride towards making your cloud interactions more efficient and less error-prone, and here’s a deeper dive into why:

- **Seamless Command Execution** - The `esc run` command lets you execute AWS commands effortlessly, freeing you from the intricacies of managing AWS credentials on your local machine. Simply put, it significantly reduces the overhead of credential setup and maintenance.

- **Enhanced Security** - One of the standout features of `esc run` is its commitment to security. Removing the local storage of credentials reduces the risk of accidental exposure. Your credentials and secrets are securely managed within the Pulumi environment.

- **Streamlined Collaboration** - Because credentials are centralized, `esc run` facilitates smoother team collaboration by providing a consistent environment for all team members to leverage. Everyone can access the same secure environment, reducing the complexities of coordinating credentials and configurations across teams.

## Getting started with esc run

### Step 1: Install and login to Pulumi ESC

To begin, you’ll need to [install Pulumi ESC](/docs/install/esc/). Once the installation is complete, run the `esc login` command and follow the steps to log in to the CLI.

```bash
$ esc login
Manage your Pulumi ESC environments by logging in.
Run `esc --help` for alternative login options.
Enter your access token from https://app.pulumi.com/account/tokens
    or hit <ENTER> to log in using your browser                   :
Logged in to pulumi.com as …
```

### Step 2: Create the OIDC configuration

Pulumi ESC allows you to manually set your credentials as secrets in your Pulumi ESC environment files. When it comes to something like OIDC configuration, a more secure and efficient alternative is to leverage yet another great feature of Pulumi ESC: dynamic credentials.

This service can dynamically generate credentials on your behalf whenever you interact with your AWS environments. To do so, follow the [guide for configuring OIDC between Pulumi and AWS](/docs/esc/environments/configuring-oidc/aws/). Ensure the IAM role you create has sufficient permissions to perform the AWS S3 actions.

### Step 3: Create a new Pulumi ESC environment

Once you have OIDC configured between Pulumi and AWS, the next step is to create a new environment in [Pulumi Cloud](https://app.pulumi.com/).

- Navigate to your [Pulumi Cloud](https://app.pulumi.com/) home page.
- Select the correct organization in the left-hand navigation menu.
- Click the **Environments** link.
- Click the **Create environment** button.
- In the pop-up window, provide a name for your environment. e.g., `aws-prod-env`
- Click the **Create environment** button.

{{< video title="Open environment in Pulumi ESC console" src="https://www.pulumi.com/uploads/esc-create-new-env.mp4" autoplay="true" loop="true" >}}

### Step 4: Add the AWS provider integration

Once you’ve created your new environment, you will be presented with a split-pane document view.

- Clear out the default placeholder content in the editor on the left-hand side.
- Replace it with the following code, making sure to replace `<your-oidc-iam-role-arn>` with the value of your IAM role ARN from the configure OIDC step:

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

### Step 5: Run aws s3 sync

With your environment set up, validate your configuration.

- Check your local environment does not have any AWS credentials configured by running the `aws configure list` command as shown below:

```bash
$ aws configure list
      Name                    Value             Type    Location
      ----                    -----             ----    --------
   profile                <not set>             None    None
access_key                <not set>             None    None
secret_key                <not set>             None    None
    region                <not set>             None    None
```

You can optionally create a dummy local directory and file to test the sync functionality.

```bash
$ mkdir my-local-dir
$ touch my-local-dir/helloWorld.txt
```

To sync to s3, run the command using `esc run` as shown below, making sure to replace `<your-pulumi-org-name>`, `<your-project-name>`, `<your-environment-name>`, `<your-s3-bucket>` and `<aws-region>` with the names of your own Pulumi organization, ESC environment, your existing S3 Bucket, and AWS Region, respectively.

```bash
$ esc run <your-pulumi-org-name>/<your-project-name>/<your-environment-name> -- aws s3 sync ./my-local-dir/ s3://<your-s3-bucket>/ --region <aws-region>
```

Then validate that your output is similar to the following:

```bash
upload: my-local-dir/helloWorld.txt to s3://pulumi-esc-demo/helloWorld.txt
```

## Conclusion

Pulumi ESC makes it easier than ever to tame infrastructure complexity, especially when running commands like `aws s3 sync`. Pulumi ESC supports dynamic credentials using OIDC across AWS, Azure, and Google Cloud. Check out the following links to learn more about Pulumi ESC today.

- Follow the [Getting Started](/docs/pulumi-cloud/esc/get-started) guide.
- Read the [Documentation](/docs/pulumi-cloud/esc) for all the commands and features available.
- Visit the [Open Source](https://github.com/pulumi/esc) repo for Pulumi ESC.

[Join our community on Slack](https://slack.pulumi.com/) to discuss this topic further, and let us know what you think.
