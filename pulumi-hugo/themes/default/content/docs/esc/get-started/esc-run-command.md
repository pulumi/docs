---
title_tag: Run Commands Without Local Secrets | Pulumi ESC
title: Run commands without local secrets
h1: "Pulumi ESC: Run Commands Without Local Secrets"
meta_desc: This page provides an overview on how to run commands without using local secrets using the "esc run" command.
weight: 6
menu:
  pulumiesc:
    parent: esc-get-started
    identifier: esc-get-started-esc-run-command
---

## Overview

The Pulumi ESC CLI also has a [`run` command](/docs/esc-cli/commands/esc_run/) that enables you to run other commands using environment variables without having to locally set the environment variables first. For example, let's say that you have a CI/CD pipeline that will automatically push blog post updates to a content-management system (CMS). Instead of storing the values of the CMS endpoint and the corresponding environment's API key locally, you can configure your pipeline to retrieve these values from your environment file before running the command to update the post.

## Expose environment variables

Values defined in your environment file are not exposed as environment variables by default. You can expose them by adding your key-value pairs under a second-level key labeled `environmentVariables`:

```yaml
values:
  environmentVariables: # Configuration will be exported to the provided environment variables.
    myEnvVarKey: myEnvVarValue
```

## Run commands with static secrets

Following the format above, add the following configuration to your environment file:

```yaml
values:
  environmentVariables:
    ENDPOINT_URL: "https://wordsapiv1.p.rapidapi.com/"
    API_KEY:
      fn::secret: "my-api-key-1234567"
```

Then run the following command to echo the value of `API_KEY`, which should be empty:

```bash
# The output should not return anything
$ echo $ENDPOINT_URL $API_KEY

```

 Now run the command using `esc run` as shown below, making sure to replace <your-pulumi-org-name> and <your-environment-name> with the names of your own Pulumi organization and environment respectively

```bash
esc run <your-pulumi-org-name>/<your-environment-name> -- bash -c "echo \$ENDPOINT_URL \$API_KEY"
```

{{< notes type="info" >}}
Commands run using `esc run` are not run in a subshell. This means that any commands that reference an environment variable like in the example shown above are not expanded by default. The `bash -c` portion of the command is what invokes the command inside a shell with environment variable expansion. See the [`esc run` documentation for the ESC CLI](/docs/esc-cli/commands/esc_run/) for more information.
{{< /notes >}}

Because you have stored the value of `API_KEY` [as a secret](/docs/esc/get-started/store-and-retrieve-secrets/), your output will resemble the following:

```bash
$ esc run pulumi/my-dev-environment -- bash -c "echo \$ENDPOINT_URL \$API_KEY"
https://wordsapiv1.p.rapidapi.com/ [secret]
```

The CLI intentionally redacts the secret value when printing to the terminal. If you want to disable the redaction, add the `--interactive` or `-i` flag to the command as shown below:

```bash
$ esc run pulumi/my-dev-environment -i -- bash -c "echo \$ENDPOINT_URL \$API_KEY"
https://wordsapiv1.p.rapidapi.com/ my-api-key-1234567
```

Alternatively, if you need to be able to run multiple commands without always having to specify the above command string each time, you can run the following command to open up a subshell that will have access to your values in your environment file:

```bash
$ esc run pulumi/my-dev-environment -i -- bash
```

From there, try running the `echo` command individually for each example variable:

```bash
$ echo $API_KEY
my-api-key-1234567

$ echo $ENDPOINT_URL
https://wordsapiv1.p.rapidapi.com/
```

You can close this subshell by running the `exit` command.

## Run commands with dynamic credentials

For supported cloud providers, the `esc run` command also enables you to run commands like `aws s3 ls` without having to manually configure provider credentials in your local environments. In this section, you will learn how to use Pulumi ESC with dynamically generated cloud credentials so that every provider command you run uses short-term, scoped credentials issued via OpenID Connect (OIDC).

If you have not done so already, make sure you have [configured OIDC connectivity](/docs/esc/get-started/begin/#configure-openid-connect-oidc) between Pulumi and one of the below supported providers.

{{< notes type="info" >}}
This functionality is currently not available for the Azure cloud provider.
{{< /notes >}}

{{% chooser cloud "aws,gcp" / %}}

{{% choosable cloud aws %}}

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

Then run the `aws s3 ls` command as normal. You should see the following response indicating that you do not have local credentials configured to run this command:

```bash
$ aws s3 ls

Unable to locate credentials. You can configure credentials by running "aws configure".
```

Now run the command using `esc run` as shown below, making sure to replace <your-pulumi-org-name> and <your-environment-name> with the names of your own Pulumi organization and environment respectively:

```bash
esc run <your-pulumi-org-name>/<your-environment-name> -- aws s3 ls
```

You should be presented with a list of S3 buckets in the account associated with your credentials.

```bash
# example command and output
esc run pulumi/my-dev-environment -- aws s3 ls

2023-12-10 02:52:46 my-bucket-4a67543
2023-11-16 21:37:40 my-bucket-4b1e6cb
2023-10-27 21:04:59 my-bucket-50da4ad
2023-11-02 18:57:36 my-bucket-51385eb
```

{{% /choosable %}}

{{% choosable cloud gcp %}}

First check that your local environment does not have any Google Cloud credentials configured by running the following command:

```bash
$ gcloud auth revoke
```

Then run the `gcloud iam service-accounts list` command as normal. You should see the following response indicating that you do not have local credentials configured to run this command:

```bash
$ gcloud iam service-accounts list
ERROR: (gcloud.iam.service-accounts.list) You do not currently have an active account selected.
Please run:

  $ gcloud auth login

to obtain new credentials.

If you have already logged in with a different account, run:

  $ gcloud config set account ACCOUNT

to select an already authenticated account to use.
```

Now run the command using `esc run` as shown below, making sure to replace <your-pulumi-org-name> and <your-environment-name> with the names of your own Pulumi organization and environment respectively:

```bash
esc run <your-pulumi-org-name>/<your-environment-name> -- gcloud iam service-accounts list
```

You should be presented with a list of Service Accounts in the account associated with your credentials.

```bash
# example command and output
$ esc run pulumi/my-dev-environment -- gcloud iam service-accounts list

DISPLAY NAME                            EMAIL                                                              DISABLED
service-account-1               service-account-1@my-project.iam.gserviceaccount.com                        False
service-account-2               service-account-2@my-project.iam.gserviceaccount.com                        False
```

{{% /choosable %}}

In the next section, you will learn how to retrieve secret values from external sources.

{{< get-started-stepper >}}
