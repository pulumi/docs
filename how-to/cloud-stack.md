---
layout: default
nav_section: "how-to"
---

<p><a href="/how-to">How-to Guides</a> &gt; <b>Create and manage Cloud Stacks</b></p>

# Create and manage Cloud Stacks

This tutorial shows how you can create and manage Pulumi Cloud Stacks in both the Pulumi CLI and Cloud Console. This involves the following:

- Login to the Pulumi Console and get your access token
- Login to the Pulumi Cloud from the CLI, using `pulumi login` and the access token
- Set values for your AWS credentials as part of your Pulumi program
- Run the `preview` and `update` commands

Then, you can view information about your stack in the Pulumi Cloud Console, as well as the output of the last `pulumi update`.

## Configure the sample project

1. Download and unzip the sample project [pulumi-url-shortener-example](/examples/pulumi-url-shortener-example.zip). 

1. In the `pulumi-url-shortener-example` folder, run `npm install` to install the dependencies to your `node_modules` directory.

1. Link with the Pulumi Cloud SDK package.

   ```bash
   $ npm link pulumi @pulumi/cloud
   ```

1. Compile the code via `npm build`.

## Create a Cloud Stack

### Login and set your region

1. Create a new Pulumi repository via `pulumi init`.

1. Log in to Pulumi Cloud Console. See [Logging in](./console.html#login-to-console).

1. Copy your access token from Console account page. See documentation on the [Pulumi access token](./console.html#access-token).

1. Run `pulumi login`. At the prompt, paste the access token that you copied in the previous step.

   ```bash
   $ pulumi login
   Logging into Pulumi Cloud: https://api.pulumi.com
   Enter your Pulumi access token: w3lc0m370pulum1cl0ud=
   ```

1. To see that you are logged in, run the `pulumi` command. The status text at the bottom will show that you are logged in to the Pulumi Cloud.

   ```bash
   $ pulumi
   
   <snip>

   Currently logged into the Pulumi Cloud ☁️
      https://api.pulumi.com*
   ```

1. Create a Cloud Stack via `stack init`:

   ```bash
   $ pulumi stack init donna-testing
   Created stack 'donna-testing' hosted in Pulumi Cloud PPC default
   ```   

1. Set your AWS region to `us-west-2`, or whichever region you prefer. The config value will be saved to `Pulumi.yaml` for the current stack.

   ```bash
   $ pulumi config set aws:config:region us-west-2
   warning: saved config key 'aws:config:region' value 'us-west-2' as plaintext; re-run with --secret to encrypt the value instead
   ```

### Configure AWS credentials

Since your AWS credentials are not stored in the Pulumi Service itself, you need to pass them in as configuration as part of your program. This means that the Service cannot directly view your credentials; it only uses them to deploy your program. 

If you try to run `pulumi preview`, you'll see an error because the config value for `aws:config:accessKey` is not set. 

1. Set values for `aws:config:accessKey` and `aws:config:secretKey`. While `accessKey` is not a secret,  `secretKey` is a secret (as the name implies). Always use the `--secret` flag to encrypt sensitive values.

   ```bash
   $ pulumi config set aws:config:accessKey 4w54cc355k3y
   warning: saved config key 'aws:config:accessKey' value '4w54cc355k3y' as plaintext; re-run with --secret to encrypt the value instead
   ```

   Use the `--secret` flag for `aws:config:secretKey`:

   ```bash
   $ pulumi config set aws:config:secretKey 53cr37k3yd0n7l34k170rb4d7h1n65w1llh4pp3n --secret
   Enter your passphrase to protect config/secrets: 
   Re-enter your passphrase to confirm: 
   ```

   A value for `encryptionsalt` will be stored in `Pulumi.yaml`. This value is based on your passphrase, but is not itself a secret and can be stored safely in source control. 
   
   > NOTE: If you wish to change your passphrase, delete the config value for `encryptionsalt` and delete your existing secure values.

   > You can set the environment variable `PULUMI_CONFIG_PASSPHRASE` to avoid the interactive prompt.

1. View your configured values via `pulumi config`. To view the values of any secrets, pass the `--show-secrets` flag.
   
   ```bash
   $ pulumi config
   KEY                                              VALUE                                           
   aws:config:accessKey                             4w54cc355k3y                            
   aws:config:region                                us-west-2                                       
   aws:config:secretKey                             ********                                        
   ```

### Preview and deploy your program

Previewing and deploying your program is similar to the local stack case, except the preview and update are performed by the Pulumi Cloud Service. This means that you can have more robust deployments and the last known state of the deployment is stored by the Service. This makes it safe to run deployments in a team or continuous deployment scenario.

When you do a preview or update, your program will be uploaded to the Pulumi Cloud, which will then run the preview operation for you.

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
    + cloud:table:Table: (create)
        [urn=urn:pulumi:donna-testing::url-shortener::cloud:table:Table::urls]
        ...
    + cloud:http:HttpEndpoint: (create)
        [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint::urlshortener]
        ...
    + aws:s3/bucket:Bucket: (create)
        [urn=urn:pulumi:donna-testing::url-shortener::aws:s3/bucket:Bucket::urlshortener]
        ...
    + aws:iam/role:Role: (create)
        [urn=urn:pulumi:donna-testing::url-shortener::aws:iam/role:Role::urlshortener4c238266]
        ...
    <more resources elided>
    ---outputs:---
    endpointUrl: "https://3tyk3ogkgc.execute-api.us-west-2.amazonaws.com/stage/"
info: 48 changes performed:
    + 48 resources created
Update duration: 1m48.031104748s
```

### View resources and update logs 

You can see the resources that are currently deployed in your Cloud Stack via the Pulumi Cloud Console.

To view your stack, navigate via the organization, repo, project and stack. From the stack details page, you can view the stack outputs and view the logs from the latest update.

For instance, the value of `endpointUrl` is displayed in the stack details page.

![stack-details](/images/docs-console/06-stack-details.png)

From the stack details page, you can also view the latest update logs, which will show the same logs that you previously saw in your terminal.

![stack-update-log](/images/docs-console/07-stack-update-log.png)

### Clean up

To clean up your deployed resources, use the `pulumi destroy` command. This will delete the cloud resources allocated by your Pulumi program, and the operation cannot be undone. 

## Next steps

To learn more about using Pulumi cloud stacks, see the following:

- [Using the Pulumi Cloud Console](./console.html)
- [Use Travis to continuously deploy Pulumi programs](./cicd-with-travis.html)
- [Pulumi CLI reference](./cli-commands.html)