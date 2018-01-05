---
layout: default
nav_section: "how-to"
---

<p><a href="/how-to">How-to Guides</a> &gt; <b>Work with managed stacks in Pulumi</b></p>

# Create and work with managed stacks

When using a managed stack, preview and update operations are performed by the Pulumi service. Managed stacks are more robust, as deployment history and current state are all managed for you. This makes it safe to run deployments in a team or continuous deployment workflow.

This tutorial shows how to create and work with managed stacks using the CLI and Pulumi Console, with the following steps:

- Log in to the Pulumi Console and get your access token
- Log in to Pulumi from the CLI, using `pulumi login` and the access token
- Set values for your AWS credentials as part of your Pulumi program configuration
- Run the `preview` and `update` CLI commands

Then, you can view information about your stack in the console, as well as the output of the last `pulumi update`.

## Configure the sample project

1. Download and unzip the sample project [pulumi-url-shortener-example](/examples/pulumi-url-shortener-example.zip). 

1. In the root of the unzipped folder, run `npm install` to install the dependencies to your `node_modules` directory.

1. Link with the Pulumi SDK packages:

   ```bash
   $ npm link pulumi @pulumi/cloud
   ```

1. Compile the code via `npm build`.

1. Create a new repository via `pulumi init`.

## Create a managed stack

### Log in to Pulumi 

1. Log in to the Pulumi Console. See [Logging in](./console.html#login-to-console).

1. Copy your access token from console **Account** page. For more information, see [Pulumi account](./console.html#account-page).

1. Run `pulumi login`. At the prompt, paste the access token that you copied in the previous step. 

   > Note: the Pulumi access token is a secret and should be kept secure.

   ```bash
   $ pulumi login
   Logging into Pulumi Cloud: https://api.pulumi.com
   Enter your Pulumi access token: w3lc0m370pulum1cl0ud=
   ```

1. To see that you are logged in, run the `pulumi` command and note the status text at the bottom.

   ```bash
   $ pulumi
   
   <snip>

   Currently logged into the Pulumi Cloud ☁️
      https://api.pulumi.com*
   ```

1. Create a managed stack via `stack init`:

   ```bash
   $ pulumi stack init donna-testing
   Created stack 'donna-testing' hosted in Pulumi Cloud PPC default
   ```   

### Configure AWS credentials

The sample program creates AWS resources in an account you specify via `pulumi config`. 

Any program that configures AWS resources requires three configuration variables: `aws:config:accessKey`, `aws:config:secretKey` and `aws:config:region`. If you omit any of these values, `pulumi preview` and `pulumi update` will tell you which settings are missing.

The value for `aws:config:secretKey` is a sensitive secret. To ensure it is not stored or transmitted in plain text, it should be stored in Pulumi config using the `--secret` flag.

1. Set your AWS region to `us-west-2`, or whichever region you prefer. The config value will be saved to `Pulumi.yaml` for the current stack.

   ```bash
   $ pulumi config set aws:config:region us-west-2
   warning: saved config key 'aws:config:region' value 'us-west-2' as plaintext; re-run with --secret to encrypt the value instead
   ```

1. Set the value for `aws:config:accessKey`. This is not a secret and can be stored as plaintext. 

   ```bash
   $ pulumi config set aws:config:accessKey 4w54cc355k3y
   warning: saved config key 'aws:config:accessKey' value '4w54cc355k3y' as plaintext; re-run with --secret to encrypt the value instead
   ```

1. Since `secretKey` is a secret (as the name implies), use the `--secret` flag:

   ```bash
   $ pulumi config set --secret aws:config:secretKey 53cr37k3yd0n7l34k170rb4d7h1n65w1llh4pp3n 
   Enter your passphrase to protect config/secrets: 
   Re-enter your passphrase to confirm: 
   ```

   A value for `encryptionsalt` will be stored in `Pulumi.yaml`. This value is based on your passphrase, but is not itself a secret; it can be stored safely in source control. 
   
   > If you wish to change your passphrase, delete the config value for `encryptionsalt` and delete your existing secure values.

   > Set the environment variable `PULUMI_CONFIG_PASSPHRASE` to avoid the interactive prompt.

1. View your configured values via `pulumi config`. To view the values of any secrets, pass the `--show-secrets` flag.
   
   ```bash
   $ pulumi config
   KEY                                              VALUE                                           
   aws:config:accessKey                             4w54cc355k3y                            
   aws:config:region                                us-west-2                                       
   aws:config:secretKey                             ********                                        
   ```

### Preview and deploy your program

When you do a CLI preview or update operation, your program is uploaded to Pulumi, which then runs the operation on your behalf.

```bash
$ pulumi preview
Previewing stack 'donna-testing' in the Pulumi Cloud ☁️
Enter your passphrase to unlock config/secrets
    (set PULUMI_CONFIG_PASSPHRASE to remember): 
Uploading program:  411.04 KiB / 411.04 KiB [===============] 100.00% 1s
Previewing changes:
+ pulumi:pulumi:Stack: (create)
    <snip many lines>
    ---outputs:---
    endpointUrl: computed<string>
info: 48 changes previewed:
    + 48 resources to create
```

If the changes look correct, run `pulumi update`:

```bash
$ pulumi update
Updating stack 'donna-testing' in the Pulumi Cloud ☁️
Enter your passphrase to unlock config/secrets
    (set PULUMI_CONFIG_PASSPHRASE to remember): 
Uploading program:  411.04 KiB / 411.04 KiB [===============] 100.00% 2s
Performing changes:
+ pulumi:pulumi:Stack: (create)
    [urn=urn:pulumi:donna-testing::url-shortener::pulumi:pulumi:Stack::url-shortener-donna-testing]
    ** more resources elided **
    ---outputs:---
    endpointUrl: "https://3tyk3ogkgc.execute-api.us-west-2.amazonaws.com/stage/"
info: 48 changes performed:
    + 48 resources created
Update duration: 1m48.031104748s
```

### View deployed resources 

You can view the currently deployed resources in your managed stack using either the Pulumi Console or the CLI.

#### Using the console

Using the console, you can view deployed resources and the log output of the last update.

**Stack.** To view your stack, navigate via the organization, repo, project and stack. From the stack details page, you can view the stack outputs and view the logs from the latest update.

For instance, the value of `endpointUrl` is displayed in the stack details page.

![stack-details](/images/docs-console/06-stack-details.png){:width="700px"}

**Update logs.** To view the  update logs, select **Latest Update Logs**. This will show the same logs that you previously saw in the terminal.

![stack-update-log](/images/docs-console/07-stack-update-log.png){:width="700px"}

#### Using the CLI

To view the resources in your managed stack, run `pulumi stack`:

```bash
$ pulumi stack
Current stack is donna-testing:
    Managed by https://api.pulumi.com ☁️
    Organization pulumi
    <snip>

Current stack resources (48):
    TYPE                           NAME
    pulumi:pulumi:Stack            url-shortener-donna-testing
    ** additional resources elided **

Current stack outputs (1):
    OUTPUT                         VALUE
    endpointUrl                    https://3tyk3ogkgc.execute-api.us-west-2.amazonaws.com/stage/

Use `pulumi stack select` to change stack; `pulumi stack ls` lists known ones
```

### Clean up

1. To clean up your deployed resources, use the `pulumi destroy` command. This will delete the AWS resources allocated by your Pulumi program. This operation cannot be undone. 

1. Delete the stack via `pulumi stack rm`.

1. Logout of Pulumi via `pulumi logout`.

## Learn more

To learn more about using managed stacks, see the following:

- [Using the Pulumi Console](./console.html)
- [Use Travis to continuously deploy Pulumi programs](./cicd-with-travis.html)
- [Pulumi CLI reference](./cli-commands.html)