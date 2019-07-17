---
title: "API Gateways and Lambda"
menu:
  reference:
    parent: tutorials-aws
---

In this tutorial, we'll use Pulumi to create a serverless app that serves static content, in addition to dynamic routes
in AWS Lambda. We'll do this with 5 lines of JavaScript, a few lines of configuration, and whatever static content we
wish to serve (in this case, a simple HTML page and a favicon). After seeing this in action, we'll build on these basic
concepts to explore additional containers, serverless, and infrastructure tutorials.

## What we'll do

- **Initialize** a new Pulumi project
- **Define** our program in JavaScript
- **Deploy** our stack to AWS
- **Manage** our stack in the Pulumi dashboard
- Tear it down

{{< aws-js-prereqs >}}

## Initialize the project

Let's use the Pulumi CLI to initialize a new project:

```bash
$ mkdir ahoy-pulumi && cd ahoy-pulumi
$ pulumi new hello-aws-javascript
```

You can accept the defaults for this command. For instance, you can change the AWS region to `us-west-2`.

<img src="/images/docs/quickstart/hello/Quickstart1.png" alt="Run Pulumi new" width="700">

After some dependency installations from NPM, you'll see a few files have been generated from this initialization process. 

<img src="/images/docs/quickstart/hello/Quickstart2.png" alt="View files" width="700">

Let's look at some of those.

- `Pulumi.yaml` defines the [project]({{< relref "/docs/reference/project.md" >}}).
- `Pulumi.ahoy-pulumi-dev.yaml` is the [configuration file]({{< relref "/docs/reference/config.md" >}}) for the stack we initialized.
- `www` contains our sample static content.
- The key file for defining our stack resources `index.js` so let's examine that.

## Define stack resources

Normally, we'd write some code to define resources for our cloud stack, but in the quickstart this work is done for us. This is the content of `index.js`:

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

See the [reference documentation]({{< relref "/docs/reference" >}}) for details on the APIs we're using.

## Deploy the stack

The stack is ready to deploy, which is done as follows:

```bash
$ pulumi up
```

This command instructs Pulumi to determine the resources needed to create the stack. First, a preview is shown of the changes that will be made:

<img src="https://user-images.githubusercontent.com/4564579/46554998-da6c9980-c896-11e8-8530-6ca4c8db8123.png" alt="Stack preview" width="700">

Choosing `yes` will create resources in AWS. This may take a minute or two.

<img src="https://user-images.githubusercontent.com/4564579/46555042-fcfeb280-c896-11e8-8731-51c9ee78af23.png" alt="Stack update" width="700">

Since there was a stack export (via `exports.url` in the code), this is printed in the output of `pulumi up`. We can easily `curl` this URL via `pulumi stack output`:

```bash
$ curl $(pulumi stack output url)
```

For a more interesting view that shows the result of calling a Lambda function, open the page in a browser:

<img src="/images/docs/quickstart/hello/Quickstart5.png" alt="Stack page in browser" width="600">

## Manage the stack

Our output also contained a permalink to the Pulumi dashboard. We can review the stack in the UI, and examine logs and resource usage, along with inviting friends and co-workers to collaborate on stacks.

<img src="/images/docs/quickstart/hello/Quickstart6.png" width="600">

## Tear Down

To destroy resources, run the following:

```bash
$ pulumi destroy
```

Once confirmed, Pulumi will remove all of the resources you've created. The stack itself is preserved in the Pulumi dashboard and is ready to go again as needed.

## Recap

In this example we've seen:

- How Pulumi makes the definition of cloud resources and stacks a highly productive, code-driven activity.
- How the Pulumi CLI can initialize, configure, deploy, and manage cloud stacks.
- How the Pulumi dashboard can log, monitor, and manage information about a cloud stack.

## Next Steps

From here, you can dive deeper:

- Try out additional AWS tutorials:
  - [Containers]({{< relref "tutorial-service.md" >}}): Create a load-balanced, hosted NGINX container service
  - [Infrastructure]({{< relref "tutorial-ec2-webserver.md" >}}): Create an EC2-based WebServer and associated infrastructure
- Try out some multi-cloud serverless and container tutorials (that also run on AWS):
  - [Multi-cloud Serverless with Document Database]({{< relref "/docs/quickstart/cloudfx/tutorial-rest-api.md" >}}): Create multi-cloud serverless
        REST APIs that use a document database
  - [Multi-cloud Serverless plus Containers]({{< relref "/docs/quickstart/cloudfx/tutorial-thumbnailer.md" >}}): Create a multi-cloud video
        thumbnail app that uses containers, serverless, and infrastructure together
- Take [a tour of Pulumi]({{< relref "/docs/tour" >}}).
