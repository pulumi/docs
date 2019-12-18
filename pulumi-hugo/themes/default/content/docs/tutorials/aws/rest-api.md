---
title: "Serverless App Using API Gateways and Lambda"
meta_desc: This tutorial will teach you how to create a Serverless App using
           AWS Api Gateway and AWS Lambda.
aliases: ["/docs/reference/tutorials/aws/tutorial-rest-api/"]
---

In this tutorial, we'll show you how to write a Pulumi program that creates a serverless app serving static content, in addition to dynamic routes in AWS Lambda. We'll accomplish this using 5 lines of JavaScript, a few lines of configuration, and whatever static content we wish to serve. For this tutorial, we'll go with a simple HTML page and a favicon. After seeing this in action, we'll build on these basic concepts to explore additional containers, serverless, and infrastructure tutorials.

{{< aws-js-prereqs >}}

## Deploy the App

### Step 1: Create a new project from a template

Create a project directory, `ahoy-pulumi`, and change into it. Run [`pulumi new aws-javascript --name myproject`]({{< relref "/docs/reference/cli/pulumi_new" >}}) to create a new project using the AWS template for JavaScript. Replace `myproject` with your desired project name.

```bash
$ mkdir ahoy-pulumi && cd ahoy-pulumi
$ pulumi new hello-aws-javascript --name myproject
```

Follow the project initialization prompts. You can accept the defaults, or change the values according to your setup. For instance, you can change the AWS region to `us-west-2`.

<img src="/images/docs/quickstart/hello/Quickstart1.png" alt="Run Pulumi new" width="700">

### Step 2: Review your project files

After some dependency installations from npm, you'll see the few files that have been generated from the initialization process.

<img src="/images/docs/quickstart/hello/Quickstart2.png" alt="View files" width="700">

Let's review those files:

- `Pulumi.yaml` defines the [project]({{< relref "/docs/intro/concepts/project.md" >}}).
- `Pulumi.ahoy-pulumi-dev.yaml` is the [configuration file]({{< relref "/docs/intro/concepts/config.md" >}}) for the stack you initialized in the previous step.
- `www` contains the sample static content for this tutorial.
- `index.js` is the key file for defining your stack resources (which we will look at in the next step).

### Step 3: Review your stack resources

Normally, you would write some code to define the resources for your cloud stack, but the quickstart took care of that for you. Open up `index.js` using your preferred text editor.

```javascript
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");
const awsx = require("@pulumi/awsx");

// Create a public HTTP endpoint (using AWS APIGateway)
const endpoint = new awsx.apigateway.API("hello", {
    routes: [
        // Serve static files from the `www` folder (using AWS S3)
        {
            path: "/",
            localPath: "www",
        },

        // Serve a simple REST API on `GET /name` (using AWS Lambda)
        {
            path: "/source",
            method: "GET",
            eventHandler: (req, ctx, cb) => {
                cb(undefined, {
                    statusCode: 200,
                    body: Buffer.from(JSON.stringify({ name: "AWS" }), "utf8").toString("base64"),
                    isBase64Encoded: true,
                    headers: { "content-type": "application/json" },
                })
            }
        }
    ]
});

// Export the public URL for the HTTP service
exports.url = endpoint.url;
```

This example uses the [`@pulumi/awsx`]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws" >}}) package in JavaScript and TypeScript to create a public HTTP endpoint, and define the static and event handler routes. See [Module apigateway]({{< relref "/docs/reference/pkg/nodejs/pulumi/awsx/apigateway" >}}) to learn more about Pulumi's API Gateway module and components.

### Step 4: Preview and deploy your resources

To preview your Pulumi program, run [`pulumi up`]({{< relref "/docs/reference/cli/pulumi_up" >}}). The command shows a preview of the resources that will be created and prompts you to proceed with the deployment.

```bash
$ pulumi up
```

<img src="https://user-images.githubusercontent.com/4564579/46554998-da6c9980-c896-11e8-8530-6ca4c8db8123.png" alt="Stack preview" width="700">

Choose `yes` to create the resources in AWS. This may take a minute or two.

<img src="https://user-images.githubusercontent.com/4564579/46555042-fcfeb280-c896-11e8-8731-51c9ee78af23.png" alt="Stack update" width="700">

Since there was a stack export (via `exports.url`) in the code, `pulumi up` prints this in the output. You can easily `curl` this URL via `pulumi stack output`:

```bash
$ curl $(pulumi stack output url)
```

For a more interesting view that shows the result of calling a Lambda function, open the page in a browser:

<img src="/images/docs/quickstart/hello/Quickstart5.png" alt="Stack page in browser" width="600">

### Step 5: Manage the stack

The output also contained a permalink to the Pulumi Console. Click on that link to review the stack in the web UI, examine logs and resource usage, and learn how you can invite friends and coworkers to collaborate on stacks.

<img src="/images/docs/quickstart/hello/Quickstart6.png" width="600">

## Clean Up

{{< cleanup >}}

## Summary

{{< summary >}}
In this tutorial, we showed you the following:

- How Pulumi makes the definition of cloud resources and stacks a highly productive, code-driven activity.
- How the Pulumi CLI can initialize, configure, deploy, and manage cloud stacks.
- How the Pulumi dashboard can log, monitor, and manage information about a cloud stack.
{{< /summary >}}

## Next Steps

- [EC2 Linux WebServer]({{< relref "ec2-webserver" >}})
- [Containers on ECS Fargate]({{< relref "ecs-fargate" >}})
- [Serve a Static Website from S3]({{< relref "s3-website" >}})
