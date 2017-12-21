---
layout: default
nav_section: "how-to"
---

<p><a href="/how-to">How-to Guides</a> &gt; <b>Create and manage Cloud Stacks</b></p>

# Create and manage Cloud Stacks

This tutorial shows how you can create and manage Pulumi Cloud Stacks in both the Pulumi CLI and Cloud Console.

## Configure the sample project

1. Download and unzip the sample project [pulumi-url-shortener-example](/examples/pulumi-url-shortener-example.zip). 

1. In the `pulumi-url-shortener-example` folder, run `npm install` to install the dependencies to your `node_modules` directory.

1. Link with the Pulumi Cloud SDK package.

   ```bash
   $ npm link pulumi @pulumi/cloud
   ```

1. Compile the code via `tsc` or `yarn build`.

## Create a Cloud Stack

The following sections describe how to create a Cloud Stack. You login to the Pulumi Console, set values for your AWS credentials, then run `pulumi preview` and `pulumi update` as usual. You can then view the output of the last `pulumi update` in the Pulumi Cloud Console, as well as information about your stack.

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

   ```bash
   $ pulumi config set aws:config:secretKey 53cr37k3yd0n7l34k170rb4d7h1n65w1llh4pp3n --secret
   Enter your passphrase to protect config/secrets: 
   Re-enter your passphrase to confirm: 
   ```

   A value for `encryptionsalt` will be stored in `Pulumi.yaml`. This value is based on your passphrase, but is not itself a secret and can be stored safely in source control. 
   
   > NOTE: If you wish to change your passphrase, delete the config value for `encryptionsalt` and delete your existing secure values.

   > You can set the environment variable `PULUMI_CONFIG_PASSPHRASE` to avoid the interactive prompt.

1. View your configured values via `pulumi config`. To view the values of secrets, pass the `--show-secrets` flag.
   
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
    + aws:iam/rolePolicyAttachment:RolePolicyAttachment: (create)
        [urn=urn:pulumi:donna-testing::url-shortener::aws:iam/rolePolicyAttachment:RolePolicyAttachment::urlshortener4c238266]
        ...
    + aws:s3/bucketObject:BucketObject: (create)
        [urn=urn:pulumi:donna-testing::url-shortener::aws:s3/bucketObject:BucketObject::urlshortener4c238266/bootstrap.min.css]
        ...
    + aws:s3/bucketObject:BucketObject: (create)
        [urn=urn:pulumi:donna-testing::url-shortener::aws:s3/bucketObject:BucketObject::urlshortener4c238266/favicon.png]
        ...
    + aws:s3/bucketObject:BucketObject: (create)
        [urn=urn:pulumi:donna-testing::url-shortener::aws:s3/bucketObject:BucketObject::urlshortener4c238266/index.html]
        ...
        + cloud:function:Function: (create)
            [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function::urlshortener0f7d8d8d]
    + cloud:global:infrastructure: (create)
        [urn=urn:pulumi:donna-testing::url-shortener::cloud:global:infrastructure::global-infrastructure]
        + aws:sns/topic:Topic: (create)
            [urn=urn:pulumi:donna-testing::url-shortener::cloud:global:infrastructure$aws:sns/topic:Topic::pulumi-d-unhandled-error]
            name: "pulumi-d-unhandled-error-f3beab2"
            ---outputs:---
            ...
            + aws:serverless:Function: (create)
                [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:serverless:Function::urlshortener0f7d8d8d]
                ...
                + aws:iam/role:Role: (create)
                    [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:serverless:Function$aws:iam/role:Role::urlshortener0f7d8d8d]
                    ...
                + aws:iam/rolePolicyAttachment:RolePolicyAttachment: (create)
                    [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:serverless:Function$aws:iam/rolePolicyAttachment:RolePolicyAttachment::urlshortener0f7d8d8d-32be53a2]
                    policyArn: "arn:aws:iam::aws:policy/AWSLambdaFullAccess"
                    role     : "urlshortener0f7d8d8d-07a591a"
                    ---outputs:---
                    id       : "urlshortener0f7d8d8d-07a591a-20171221031918666800000002"
                + aws:iam/rolePolicyAttachment:RolePolicyAttachment: (create)
                    [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:serverless:Function$aws:iam/rolePolicyAttachment:RolePolicyAttachment::urlshortener0f7d8d8d-fd1a00e5]
                    policyArn: "arn:aws:iam::aws:policy/AmazonEC2ContainerServiceFullAccess"
                    role     : "urlshortener0f7d8d8d-07a591a"
                    ---outputs:---
                    id       : "urlshortener0f7d8d8d-07a591a-20171221031919838900000003"
                + aws:lambda/function:Function: (create)
                    [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:serverless:Function$aws:lambda/function:Function::urlshortener0f7d8d8d]
                    ...
            + aws:cloudwatch/logGroup:LogGroup: (create)
                [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:cloudwatch/logGroup:LogGroup::urlshortener0f7d8d8d]
                name           : "/aws/lambda/urlshortener0f7d8d8d-c30bd17"
                retentionInDays: 1
                ---outputs:---
                arn            : "arn:aws:logs:us-west-2:153052954103:log-group:/aws/lambda/urlshortener0f7d8d8d-c30bd17:*"
                id             : "/aws/lambda/urlshortener0f7d8d8d-c30bd17"
                retentionInDays: "1"
    + cloud:logCollector:LogCollector: (create)
        [urn=urn:pulumi:donna-testing::url-shortener::cloud:logCollector:LogCollector::pulumi-donna-testing]
        + aws:serverless:Function: (create)
            [urn=urn:pulumi:donna-testing::url-shortener::cloud:logCollector:LogCollector$aws:serverless:Function::pulumi-donna-testing]
            ...
            + aws:iam/role:Role: (create)
                [urn=urn:pulumi:donna-testing::url-shortener::cloud:logCollector:LogCollector$aws:serverless:Function$aws:iam/role:Role::pulumi-donna-testing]
                ...
            + aws:iam/rolePolicyAttachment:RolePolicyAttachment: (create)
                [urn=urn:pulumi:donna-testing::url-shortener::cloud:logCollector:LogCollector$aws:serverless:Function$aws:iam/rolePolicyAttachment:RolePolicyAttachment::pulumi-donna-testing-32be53a2]
                policyArn: "arn:aws:iam::aws:policy/AWSLambdaFullAccess"
                role     : "pulumi-donna-testing-be5a01f"
                ---outputs:---
                id       : "pulumi-donna-testing-be5a01f-20171221031938826900000004"
            + aws:lambda/function:Function: (create)
                [urn=urn:pulumi:donna-testing::url-shortener::cloud:logCollector:LogCollector$aws:serverless:Function$aws:lambda/function:Function::pulumi-donna-testing]
                ...
        + aws:lambda/permission:Permission: (create)
            [urn=urn:pulumi:donna-testing::url-shortener::cloud:logCollector:LogCollector$aws:lambda/permission:Permission::pulumi-donna-testing]
            action     : "lambda:invokeFunction"
            function   : "pulumi-donna-testing-d70370c"
            principal  : "logs.us-west-2.amazonaws.com"
            statementId: "pulumi-donna-testing-2a2eab5"
            ---outputs:---
            id         : "pulumi-donna-testing-2a2eab5"
            + aws:cloudwatch/logSubscriptionFilter:LogSubscriptionFilter: (create)
                [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:cloudwatch/logSubscriptionFilter:LogSubscriptionFilter::urlshortener0f7d8d8d]
                destinationArn: "arn:aws:lambda:us-west-2:153052954103:function:pulumi-donna-testing-d70370c"
                logGroup      : "/aws/lambda/urlshortener0f7d8d8d-c30bd17"
                name          : "urlshortener0f7d8d8d-02fa07c"
                ---outputs:---
                id            : "cwlsf-175410676"
        + cloud:function:Function: (create)
            [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function::urlshortenerd9505e4a]
            + aws:serverless:Function: (create)
                [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:serverless:Function::urlshortenerd9505e4a]
                ...                
                + aws:iam/role:Role: (create)
                    [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:serverless:Function$aws:iam/role:Role::urlshortenerd9505e4a]
                    ...                                    
                + aws:iam/rolePolicyAttachment:RolePolicyAttachment: (create)
                    [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:serverless:Function$aws:iam/rolePolicyAttachment:RolePolicyAttachment::urlshortenerd9505e4a-32be53a2]
                    policyArn: "arn:aws:iam::aws:policy/AWSLambdaFullAccess"
                    role     : "urlshortenerd9505e4a-5b0786e"
                    ---outputs:---
                    id       : "urlshortenerd9505e4a-5b0786e-20171221031957624600000005"
                + aws:iam/rolePolicyAttachment:RolePolicyAttachment: (create)
                    [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:serverless:Function$aws:iam/rolePolicyAttachment:RolePolicyAttachment::urlshortenerd9505e4a-fd1a00e5]
                    policyArn: "arn:aws:iam::aws:policy/AmazonEC2ContainerServiceFullAccess"
                    role     : "urlshortenerd9505e4a-5b0786e"
                    ---outputs:---
                    id       : "urlshortenerd9505e4a-5b0786e-20171221031958708200000006"
                + aws:lambda/function:Function: (create)
                    [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:serverless:Function$aws:lambda/function:Function::urlshortenerd9505e4a]
                    ...                
            + aws:cloudwatch/logGroup:LogGroup: (create)
                [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:cloudwatch/logGroup:LogGroup::urlshortenerd9505e4a]
                name           : "/aws/lambda/urlshortenerd9505e4a-e66a77d"
                retentionInDays: 1
                ---outputs:---
                arn            : "arn:aws:logs:us-west-2:153052954103:log-group:/aws/lambda/urlshortenerd9505e4a-e66a77d:*"
                id             : "/aws/lambda/urlshortenerd9505e4a-e66a77d"
                retentionInDays: "1"
            + aws:cloudwatch/logSubscriptionFilter:LogSubscriptionFilter: (create)
                [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:cloudwatch/logSubscriptionFilter:LogSubscriptionFilter::urlshortenerd9505e4a]
                destinationArn: "arn:aws:lambda:us-west-2:153052954103:function:pulumi-donna-testing-d70370c"
                logGroup      : "/aws/lambda/urlshortenerd9505e4a-e66a77d"
                name          : "urlshortenerd9505e4a-1c94204"
                ---outputs:---
                id            : "cwlsf-2588808429"
        + cloud:function:Function: (create)
            [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function::urlshortenereeb67ce9]
            + aws:serverless:Function: (create)
                [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:serverless:Function::urlshortenereeb67ce9]
                ...                
                + aws:iam/role:Role: (create)
                    [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:serverless:Function$aws:iam/role:Role::urlshortenereeb67ce9]
                    ...                
                + aws:iam/rolePolicyAttachment:RolePolicyAttachment: (create)
                    [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:serverless:Function$aws:iam/rolePolicyAttachment:RolePolicyAttachment::urlshortenereeb67ce9-32be53a2]
                    ...                

                + aws:iam/rolePolicyAttachment:RolePolicyAttachment: (create)
                    [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:serverless:Function$aws:iam/rolePolicyAttachment:RolePolicyAttachment::urlshortenereeb67ce9-fd1a00e5]
                    ...
                + aws:lambda/function:Function: (create)
                    [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:serverless:Function$aws:lambda/function:Function::urlshortenereeb67ce9]
                    ...
            + aws:cloudwatch/logGroup:LogGroup: (create)
                [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:cloudwatch/logGroup:LogGroup::urlshortenereeb67ce9]
                ...                

            + aws:cloudwatch/logSubscriptionFilter:LogSubscriptionFilter: (create)
                [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$cloud:function:Function$aws:cloudwatch/logSubscriptionFilter:LogSubscriptionFilter::urlshortenereeb67ce9]
                destinationArn: "arn:aws:lambda:us-west-2:153052954103:function:pulumi-donna-testing-d70370c"
                logGroup      : "/aws/lambda/urlshortenereeb67ce9-f49e4f5"
                name          : "urlshortenereeb67ce9-c6f93f4"
                ---outputs:---
                id            : "cwlsf-3270915532"
        + aws:apigateway/restApi:RestApi: (create)
            [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$aws:apigateway/restApi:RestApi::urlshortener]
            ...                

        + aws:apigateway/deployment:Deployment: (create)
            [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$aws:apigateway/deployment:Deployment::urlshortener-e79b5b01]
            ...
        + aws:apigateway/stage:Stage: (create)
            [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$aws:apigateway/stage:Stage::urlshortener]
            ...
        + aws:lambda/permission:Permission: (create)
            [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$aws:lambda/permission:Permission::urlshortener-0f7d8d8d]
            ...                
        + aws:lambda/permission:Permission: (create)
            [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$aws:lambda/permission:Permission::urlshortener-eeb67ce9]
            ...
        + aws:lambda/permission:Permission: (create)
            [urn=urn:pulumi:donna-testing::url-shortener::cloud:http:HttpEndpoint$aws:lambda/permission:Permission::urlshortener-d9505e4a]
            ...
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

To clean up your deployed resources, use the `pulumi destroy` command.

## Next steps

To learn more about using Pulumi cloud stacks, see the following:

- [Using the Pulumi Cloud Console](./console.html)
- [Use Travis to continuously deploy Pulumi programs](./cicd-with-travis.html)
- [Pulumi CLI reference](./cli-commands.html)