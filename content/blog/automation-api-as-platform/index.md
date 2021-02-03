---
title: "Build Self-Service Cloud Infrastructure with Automation API "
date: 2020-11-10
meta_desc: "With Pulumi's Automation API, you can build a REST API for creating, reading, updating, and deleting (CRUD) cloud resources."
meta_image: automation_api.png
authors:
    - sophia-parafina
tags:
    - Automation API
    - CRUD
---

If you could create infrastructure without using a cloud provider's console, a CLI, or a templating engine, what would you build? Pulumi's Automation API lets you create declarative infrastructure defined by your best practices and expose it behind a REST, gRPC, or custom API.

So just what is Automation API? Think of it as Pulumi's infrastructure as code engine as an SDK. Instead of writing code and using the CLI to declare infrastructure, you can directly tell the engine to build your infrastructure. This means that you're using the same declarative IaC tooling with the predictability, robustness, safety, and desired state management, except it has a new programmatic surface area. Imagine building an application that creates infrastructure via a REST interface. Get ready, because that's what we're going to do.

<!--more-->

## Self-service Cloud Infrastructure

Automation API is just another package that runs inside your favorite frameworks and works with other packages. You can create methods or functions to create infrastructure that you can call from other frameworks. One Automation API use case is a self-service infrastructure. You can create declarative infrastructure and expose it behind a REST interface. Your infrastructure is also backed by a JSON state file managed by the Pulumi SaaS that allows you to create and update them dynamically.

This example demonstrates how to create infrastructure with Automation API and the [Express](https://expressjs.com/) Node.js  framework. To keep this example simple, we'll deploy the REST API locally. To deploy the code in the cloud, for example, in a virtual machine, we'll need to create an [instance profile](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) to store AWS credentials. Deploying Automation API is beyond this article's scope, so we'll use `localhost` as the server's endpoint. We'll cover deploying Automation API in the cloud in subsequent articles.

### Infrastructure as a function

We use an `inline` Pulumi program that doesn't require a separate package with `index.ts` and `Pulumi.yaml` files, although they can be authored in an `index.ts` file or imported from another package. The example deploys an AWS S3 website with the context and deployment automation defined in a function. Functions can be [components]({{< relref "/docs/intro/concepts/resources#components" >}}), in this case, a static S3 website. However, they can be more complex, such as a Kubernetes cluster with accompanying containers and AWS resources.

```typescript
const projectName = "pulumi_over_http";

const createPulumiProgram = (content: string) => async () => {
    // Create a bucket and expose a website index document
    const siteBucket = new s3.Bucket("s3-website-bucket", {
        website: {
            indexDocument: "index.html",
        },
    });
```

This part of the function lets users write content.

```typescript
    // Our HTML is defined based on what the caller sends.
    const indexContent = content;

    // write our index.html into the site bucket
    let object = new s3.BucketObject("index", {
        bucket: siteBucket,
        content: indexContent,
        contentType: "text/html; charset=utf-8",
        key: "index.html"
    });
```

To make the contents accessible, we create and set a policy for the S3 bucket.

```typescript
    // Create an S3 Bucket Policy to allow public read of all objects in bucket
    function publicReadPolicyForBucket(bucketName): PolicyDocument {
        return {
            Version: "2012-10-17",
            Statement: [{
                Effect: "Allow",
                Principal: "*",
                Action: [
                    "s3:GetObject"
                ],
                Resource: [
                    `arn:aws:s3:::${bucketName}/*` // policy refers to bucket name explicitly
                ]
            }]
        };
    }

    // Set the access policy for the bucket so all objects are readable
    let bucketPolicy = new s3.BucketPolicy("bucketPolicy", {
        bucket: siteBucket.bucket, // refer to the bucket created earlier
        policy: siteBucket.bucket.apply(publicReadPolicyForBucket) // use output property `siteBucket.bucket`
    });

    return {
        websiteUrl: siteBucket.websiteEndpoint,
    };
};
```

### Building the REST API

We use the Express `RequestHandler` callback to create the S3 static website buckets by creating the stack locally. Calling this handler creates a new bucket which represents an individual site. It's important to note that one of the advantages of using code is the ability to detect and handle error scenarios, which is necessary for online infrastructure or when embedding it in other complex software.

```typescript
// creates new sites
const createHandler: express.RequestHandler = async (req, res) => {
    const stackName = req.body.id;
    const content = req.body.content as string;
    try {
        // create a new stack
        const stack = await LocalWorkspace.createStack({
            stackName,
            projectName,
            // generate our pulumi program on the fly from the POST body
            program: createPulumiProgram(content),
        });
        await stack.setConfig("aws:region", { value: "us-west-2" });
        // deploy the stack, tailing the logs to console
        const upRes = await stack.up({ onOutput: console.info });
        res.json({ id: stackName, url: upRes.outputs.websiteUrl.value });
    } catch (e) {
        if (e instanceof StackAlreadyExistsError) {
            res.status(409).send(`stack "${stackName}" already exists`);
        } else {
            res.status(500).send(e);
        }
    }
};
```

These callbacks implement the range of REST API requests for a bucket which includes adding content with a POST request, updating content with a PUT request, getting site content and a list of sites with GET requests, and deleting a site/bucket with a DELETE request.

```typescript
// lists all sites
const listHandler: express.RequestHandler = async (req, res) => {
    try {
        // set up a workspace with only enough information for the list stack operations
        const ws = await LocalWorkspace.create({ projectSettings: { name: projectName, runtime: "nodejs" } });
        const stacks = await ws.listStacks();
        res.json({ ids: stacks.map(s => s.name) });
    } catch (e) {
        res.status(500).send(e);
    }
};
// gets info about a specific site
const getHandler: express.RequestHandler = async (req, res) => {
    const stackName = req.params.id;
    try {
        // select the existing stack
        const stack = await LocalWorkspace.selectStack({
            stackName,
            projectName,
            // don't need a program just to get outputs
            program: async () => { },
        });
        const outs = await stack.outputs();
        res.json({ id: stackName, url: outs.websiteUrl.value });
    } catch (e) {
        if (e instanceof StackNotFoundError) {
            res.status(404).send(`stack "${stackName}" does not exist`);
        } else {
            res.status(500).send(e);
        }
    }
};
// updates the content for an existing site
const updateHandler: express.RequestHandler = async (req, res) => {
    const stackName = req.params.id;
    const content = req.body.content as string;
    try {
        // select the existing stack
        const stack = await LocalWorkspace.selectStack({
            stackName,
            projectName,
            // generate our pulumi program on the fly from the POST body
            program: createPulumiProgram(content),
        });
        await stack.setConfig("aws:region", { value: "us-west-2" });
        // deploy the stack, tailing the logs to console
        const upRes = await stack.up({ onOutput: console.info });
        res.json({ id: stackName, url: upRes.outputs.websiteUrl.value });
    } catch (e) {
        if (e instanceof StackNotFoundError) {
            res.status(404).send(`stack "${stackName}" does not exist`);
        } else if (e instanceof ConcurrentUpdateError) {
            res.status(409).send(`stack "${stackName}" already has update in progress`)
        } else {
            res.status(500).send(e);
        }
    }
};
// deletes a site
const deleteHandler: express.RequestHandler = async (req, res) => {
    const stackName = req.params.id;
    try {
        // select the existing stack
        const stack = await LocalWorkspace.selectStack({
            stackName,
            projectName,
            // don't need a program for destroy
            program: async () => { },
        });
        // deploy the stack, tailing the logs to console
        await stack.destroy({ onOutput: console.info });
        await stack.workspace.removeStack(stackName);
        res.status(200).end();
    } catch (e) {
        if (e instanceof StackNotFoundError) {
            res.status(404).send(`stack "${stackName}" does not exist`);
        } else if (e instanceof ConcurrentUpdateError) {
            res.status(409).send(`stack "${stackName}" already has update in progress`)
        } else {
            res.status(500).send(e);
        }
    }
};
const ensurePlugins = async () => {
    const ws = await LocalWorkspace.create({});
    await ws.installPlugin("aws", "v3.2.1");
};

// install necessary plugins once upon boot
ensurePlugins();

// configure express
const app = express();
app.use(express.json());
```

Creating routes in Express to the callbacks is straightforward and requires mapping the route to the appropriate callback.

```typescript
// setup our RESTful routes for our Site resource
app.post("/sites", createHandler);
app.get("/sites", listHandler);
app.get("/sites/:id", getHandler);
app.put("/sites/:id", updateHandler);
app.delete("/sites/:id", deleteHandler);

// start our http server
app.listen(1337, () => console.info("server running on :1337"));
```

## Trying it out

The complete example is available on [GitHub](https://github.com/pulumi/automation-api-examples/tree/main/nodejs/pulumiOverHttp-ts), along with other examples in both Nodejs and go. To run the TypeScript example, run:

```bash
$ yarn install
$ yarn start
```

Let's test it by sending requests to the server on `http://localhost:1337`.

{{% notes type="info" %}}
If you use [Postman](https://www.postman.com/), you can import a [Postman Collection](https://gist.github.com/pulumipus/56d1ee83f295971e2a26a8091880c482) to send requests to the server.
{{% /notes %}}

First let's create our first website which returns the website path (`id`) and the URL of the static website.

```bash
$ curl --header "Content-Type: application/json"   --request POST   --data '{"id":"hello","content":"hello world\n"}'   http://localhost:1337/sites
$ {"id":"hello","url":"s3-website-bucket-db5dae8.s3-website-us-west-2.amazonaws.com"}
```

We can view the content then update it, then view it again.

```bash
$ curl s3-website-bucket-db5dae8.s3-website-us-west-2.amazonaws.com
$ curl --header "Content-Type: application/json"   --request PUT   --data '{"id":"hello","content":"hello updated world!\n"}'   http://localhost:1337/sites/hello
$ curl s3-website-bucket-db5dae8.s3-website-us-west-2.amazonaws.com
```

Once we're done, we can delete the website.

```bash
$ curl --header "Content-Type: application/json"   --request DELETE http://localhost:1337/sites/hello
```

## Pulling it all together

So what can you do with this? We used a static website in this example so that results are immediately available. However, this application does basic [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) operations, which are the basis of many applications. For example, an application could send photos to a bucket or send data to a database application.

Automation API enables building your custom cloud platforms. This example has shown us how to take our customized unit of infrastructure and expose it to our broader team via a REST interface that we define and control. This interface is familiar to developers and feels more comfortable than using IaC directly. Today, we expose a static website, but tomorrow it could be a Kubernetes application platform with all of our networking and security best practices.

Automation API lets you build and explore new implementation patterns with cloud resources. Check out the other things you can build with Automation API.

- [The Pulumi Automation API - The Next Quantum Leap in IaC]({{< relref "/blog/automation-api" >}})
- [Automation API Examples](https://github.com/pulumi/automation-api-examples)
