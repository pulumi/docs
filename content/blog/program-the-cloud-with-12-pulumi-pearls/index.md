---
title: "Program the Cloud with 12 Pulumi Pearls"
date: "2018-07-25"
meta_desc: "In this post, we'll look at some fun ways you can program the cloud using Pulumi, including infrastructure, serverless, containers, and general tips and tricks."
authors: ["joe-duffy"]
tags: ["Serverless","AWS","Containers","Infrastructure","TypeScript"]
---

In this post, we'll look at 12 "pearls" -- bite-sized code snippets --
that demonstrate some fun ways you can program the cloud using Pulumi.
In my introductory post, I mentioned [a few of my "favorite things"](http://joeduffyblog.com/2018/06/18/hello-pulumi/#my-favorite-things).
Now let's dive into a few specifics, from multi-cloud to cloud-specific,
spanning containers, serverless, and infrastructure, and generally
highlighting why using real languages is so empowering for cloud
scenarios. Since Pulumi lets you do infrastructure-as-code from the
lowest-level to the highest, we will cover a lot of interesting ground
in short order.

If you want to follow along and try some of this out, Pulumi is
[open source on GitHub](https://github.com/pulumi/pulumi), free to download
and use, and [the quickstart]({{< relref "/docs/get-started" >}}) will acquaint you with the CLI. Most of
the examples are directly runnable and available in [our examples repo](https://github.com/pulumi/examples), and are just a
`pulumi up` away, unlike other approaches that
require you to point-and-click around in your cloud's console, and/or
author reams of yucky YAML. And you get to use real languages!

Here is an index of the pearls in case you want to dive straight into
one in particular:

[**Infrastructure**](#infrastructure):

1. [Declare cloud infra using a real language (with loops!)](#real-languages)
2. [Make a reusable component out of your cloud infra](#reusable-components)

[**Serverless**](#serverless):

1. [Go serverless without the YAML](#no-yaml)
2. [Capture state in your serverless funcs, like real lambdas](#real-lambdas)
3. [Simple serverless cron jobs](#cron-jobs)
4. [Run Express-like serverless SPAs and REST APIs at near zero cost](#rest-apis)

[**Containers**](#containers):

1. [Deploy production containers without the fuss](#easy-deployment)
2. [Use containers without Dockerfiles](#no-dockerfiles)
3. [Invoke a long-running container as a task](#long-running-containers-as-tasks)

[**General Tips and Tricks**](#general-tips-and-tricks):

1. [Use code to avoid hard-coding config](#avoid-hard-coding-config)
2. [Use config to enable multi-instantiation and code reuse](#multi-instantiation-and-code-reuse)
3. [Give your components runtime APIs](#give-components-runtime-apis)

Even if you're uninterested in low-level infrastructure, it can be fun
to work through these examples; it's "turtles all the way down" with
Pulumi and doing so can help understand how the system works. And
similarly, it can be fun to see the high-level scenarios these building
blocks facilitate, even if you just want to stand up containers and
functions.

And with that, let's dive in.

## Infrastructure

### Real Languages

[ [Runnable Example](https://github.com/pulumi/examples/tree/master/aws-js-webserver) ]

Pulumi gives you a way to express infrastructure configuration using
your favorite programming language. In this article, we'll use
TypeScript on Node.js, as it delivers great productivity by blending
dynamic and static typing with the NPM ecosystem of reusable packages.

At the lowest layer, there are packages for all major cloud providers --
[AWS](https://github.com/pulumi/pulumi-aws),
[Azure](https://github.com/pulumi/pulumi-azure),
[Google Cloud](https://github.com/pulumi/pulumi-gcp) -- in addition to
[Kubernetes](https://github.com/pulumi/pulumi-kubernetes) and
[OpenStack](https://github.com/pulumi/pulumi-openstack). So, if you want
an EC2 instance, Azure CosmosDB, or Kubernetes Pod, you just
`new` up an object. From there, Pulumi uses an
infrastructure-as-code approach similar to using AWS CloudFormation,
Azure Resource Manager, Google Resource Manager, Kubernetes or Helm
YAML, or Terraform -- just without the YAML DSLs.

The strength of using a language truly begins to shine when you go
beyond `new`, however. Using a language gives you
control structures, like for loops and if branches. This is easy to take
for granted, but compared to existing YAML DSLs, it is very powerful.

For example, let's create three EC2 VMs and export their IP addresses.
Normally you'd need to copy-and-paste, however for loops to the rescue!

**index.ts**:

```javascript
import * as aws from "@pulumi/aws";

let webSg = new aws.ec2.SecurityGroup("web-secgrp", {
    ingress: [
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});

let webServers = [];
for (let i = 0; i < 3; i++) {
    webServers.push(new aws.ec2.Instance(`web-server-${i}`, {
        instanceType: "t2.micro",
        ami: "ami-6869aa05", // us-east-1-only
        securityGroups: [ webSg.name ],
        userData: `#!/bin/bashn` +
            `echo 'Hello, World #${i}!' > index.htmln` +
            `nohup python -m SimpleHTTPServer 80 &n`,
    }));
}
export let publicHostnames = webServers.map(s => s.publicDns);
```

This provisions three web servers, each of which runs a simple Python
webserver.

Of course, this can unlock far more sophisticated scenarios. For
example, our own [AWS Infrastructure](https://github.com/pulumi/pulumi-aws-infra) package
offers core AWS infrastructure components using AWS's own best
practices, and a community member [built an AWS Virtual Private Cloud (VPC) component](https://github.com/jen20/pulumi-aws-vpc) that
automatically distributes subnets across all availability zones in a
region, including smartly calculating the CIDR addresses, hiding lots of
the messy details of AWS networking.

### Reusable Components

[ [Runnable Example](https://github.com/pulumi/pulumi-aws/blob/master/examples/webserver-comp/) ]

Speaking of components, this is another benefit of using real languages:
abstraction. This includes the ability to hide uninteresting details
through encapsulation, and create bigger things out of smaller things, a
key to how we've become so productive with programming languages
generally over the years. Applied to infrastructure, this enables some
powerful scenarios.

For instance, perhaps you want a standard base class for all servers in
your organization, enforcing security policy or even just naming
conventions. Or maybe you want to ensure there is an Envoy proxy sidecar
for all of your Kubernetes pods. No matter the scenario, we call these
things "components" and Pulumi has a rich model that supports parents
and children.

To stick with the running example, let's make a WebServer class that
internally creates the EC2 VM so that callers don't need to know messy
details like how to create and configure a SecurityGroup and choosing
the right image:

**web.ts**:

```javascript
import * as aws from "@pulumi/aws";

let webSg = new aws.ec2.SecurityGroup("web-secgrp", {
    ingress: [
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});

export class WebServer {
    public readonly vm: aws.ec2.Instance;

    constructor(name: string) {
        this.vm = new aws.ec2.Instance(`${name}`, {
            instanceType: "t2.micro",
            ami: "ami-6869aa05", // us-east-1-only
            securityGroups: [ webSg.name ],
            userData: `#!/bin/bashn` +
                `echo 'Hello from ${name}!' > index.htmln` +
                `nohup python -m SimpleHTTPServer 80 &n`,
        });
    }
}
```

Now we can go back to our original program and tidy it up a bit:

**index.ts**:

```javascript
import { WebServer } from "./web";

let webServers = [];
for (let i = 0; i < 3; i++) {
    webServers.push(new WebServer(`web-server-${i}`));
}
export let publicHostnames = webServers.map(s => s.vm.publicDns);
```

Not only is the result simpler, but we now have a way to divvy up
responsibilities within a team, helping Dev and DevOps to work better
together.

This example used purely local components, but you can of course publish
and consume any old packages from your favorite package manager --
including private registries for your own team.

We will return to these examples later on and improve them to be more
reusable through configuration, however let's first tour some fun
serverless and container pearls.

## Serverless

### No YAML

[ [Runnable Example](https://github.com/pulumi/examples/tree/master/aws-js-webserver) ]

Let's shift gears and jump into serverless. Pulumi is unique in that its
goal is to be a platform for all aspects of modern cloud programming, so
that includes serverless, in addition to the abovementioned
infrastructure examples and the soon-to-be-mentioned container ones.
Most real-world examples we see in fact mix all of these things together
in the same program.

Because of the way it uses real languages, there are great benefits to
serverless programming in Pulumi. No YAML required -- just write lambdas
in your favorite language, and our compiler/runtime magic will deal with
them. But first, let's start simple.

The [AWS Serverless](https://github.com/pulumi/pulumi-aws-serverless)
package provides event sources for all of the possible AWS Lambda
triggers. This leverages the
`aws.serverless.Function` abstraction that takes a
lambda in your language and translates it into a package suitable for
uploading to AWS. No need to embed code in YAML files, manually upload
to S3, etc. Pulumi handles all of this including versioning.

Let's look at a simple example that simply posts a Slack message for
every new message that arrives in an SQS queue
([a new capability recently added to AWS](https://aws.amazon.com/blogs/aws/aws-lambda-adds-amazon-simple-queue-service-to-supported-event-sources/)).
The way you express serverless functions in Pulumi is by writing
ordinary lambdas and the way you hook them up to event sources is by
using an event-driven style on your existing cloud resources:

**index.ts**:

```javascript
import * as aws from "@pulumi/aws";
import * as serverless from "@pulumi/aws-serverless";

let queue = new aws.sqs.Queue("mySlackQueue");
serverless.queue.subscribe("mySlackPoster", queue, async (e) => {

let slack = require("@slack/client");
let client = new slack.WebClient(config.slackToken);
    for (let rec of e.Records) {
        await client.chat.postMessage({
            channel: config.slackChannel,
            text: `*SQS message ${rec.messageId}*:n${rec.body}n`+
                `(with :love_letter: from Pulumi)`,
            as_user: true,
        });
        console.log(`Posted SQS message ${rec.messageId} to ${config.slackChannel}`);
    }
});
export let queueURL = queue.id;
```

The code and instructions for running this example are available
[in our examples repo](https://github.com/pulumi/examples/tree/master/aws-js-sqs-slack).

Serverless programs written in this style feel just like your favorite
event-driven frameworks, and -- because these are just ordinary lambdas
in your language of choice -- they compose in all the usual ways,
unlocking some fascinating future possibilities (like serverless Spark
and/or RxJS). Behind the scenes, Pulumi is doing the hard work to
extract out the body of the function, rewrite it minimally but as needed
to wire it up to AWS Lambda, and package it up. Subsequent deployments
are as easy as the first one, as Pulumi does diffing to compute the
minimal deltas.

Not everybody will want to mix infrastructure definitions and runtime
code like this. Because these are just ordinary programs, you are free
to split code into submodules and structure your workspace as you see
fit. In fact, you can create distinct stacks for the different pieces.

This example is AWS-specific, however the [Pulumi Cloud Framework](https://github.com/pulumi/pulumi-cloud) offers several
multi-cloud serverless (and container) capabilities. We will see some
examples of that package in action below, however being able to target
your cloud of choice directly means you can use all of its underlying
features.

### Real Lambdas

[ [Runnable Example](https://github.com/pulumi/examples/tree/master/aws-js-webserver) ]

Pulumi also lets you capture state in your serverless functions. This is
one of the major advantages to this approach; normally you'd need to
awkwardly arrange for such state to be passed into your function through
some sideband mechanism, such as environment variables.

In Pulumi, we just capture state. Just like in your favorite language.

Let's say we want the Slack information above to be configurable -- a
good idea, since the Slack token is a secret that should be configured
using the --secret flag. To do so, first let's create a config module:

**config.ts**:

```javascript
import * as pulumi from "@pulumi/pulumi";
let config = new pulumi.Config(pulumi.getProject());

export let slackChannel = config.get("slackChannel") || "#general",
export let slackToken: config.require("slackToken");
```

And now let's go back to our above program, and use the config module
for these properties. Notice that we simply capture a reference to the
config module -- that's it!

**index.ts**:

```javascript
import * as config from "./config";
import * as aws from "@pulumi/aws";
import * as serverless from "@pulumi/aws-serverless";

let queue = new aws.sqs.Queue("mySlackQueue");
serverless.queue.subscribe("mySlackPoster", queue, async (e) => {
    let slack = require("@slack/client");
    let client = new slack.WebClient(config.slackToken);

    for (let rec of e.Records) {
        await client.chat.postMessage({
            channel: config.slackChannel,
            text: `*SQS message ${rec.messageId}*:n${rec.body}n`+
                `(with :love_letter: from Pulumi)`,
            as_user: true,
        });
        console.log(`Posted SQS message ${rec.messageId} to ${config.slackChannel}`);
    }
});
export let queueURL = queue.id;
```

We often call this "capture by serialization" because, of course, the
captured state is marshaled into the serverless function's package, and
then unmarshaled at runtime at the time of use. The semantics of capture
are specific to each language, but for JavaScript, we do a deep
serialization of the object, including its prototype chain, so that the
full structure is preserved.

Because of this, functions are even available. We use this capability to
let you capture resources by-value that internally have references to a
live cloud resource. We will see that next in our serverless cron job
example.

### Cron Jobs

[ [Runnable Example](https://github.com/pulumi/pulumi-cloud/tree/master/examples/timers) ]

[Pulumi's Cloud Framework](https://github.com/pulumi/pulumi-cloud) has
an ultra-straightforward timer module that lets you schedule cron jobs
that run serverless functions. This is the easiest way to get up and
running with serverless functions, because you don't even need any other
resources to trigger events from.

There are several ways to schedule a timer, depending on your stylistic
preferences. These examples simply print the current time to the console
on a given interval:

**index.ts**:

```javascript
import * as cloud from "@pulumi/cloud";

// Run a timer every minute:
cloud.timer.interval("interval-timer", { minutes: 0 }, () => {
    console.log(`interval-timer: ${Date.now()}`);
});

// Run a timer every minute (cron-style expression):
cloud.timer.cron("cron-timer", "0 * * * * *", () => {
    console.log(`cron-timer: ${Date.now()}`);
});

// Run a timer every day at 7:30 UTC:
cloud.timer.daily("daily-timer", { hourUTC: 7, minuteUTC: 30 }, () => {
    console.log(`daily-timer: ${Date.now()}`);
});

// Run a timer at the 45th minute UTC of every hour:
cloud.timer.hourly("hourly-timer", { minuteUTC: 45 }, () => {
    console.log(`hourly-timer: ${Date.now()}`);
});
```

To make things slightly more interesting, let's write a serverless timer
that fetches the Hacker News homepage every hour and stashes it into a
document database:

**index.ts**:

```javascript
import * as cloud from "@pulumi/cloud";

let snapshots = new cloud.Table("snapshots");
cloud.timer.daily("daily-yc-snapshot", { hourUTC: 0, minuteUTC: 0 }, () => {
    let req = require("https").get("https://news.ycombinator.com", (res) => {
    let content = "";

    res.setEncoding("utf8");
    res.on("data", (chunk) => { content += chunk });
        res.on("end", () => {
            snapshots.insert({ date: Date.now(), content: content });
        });
    });
    req.end();
});
```

We are using the ability to capture a reference to our
`cloud.Table` and call functions on it, like
`insert`. Of course, the body of that function can
do absolutely anything that you'd like.

### REST APIs

[ [Runnable Example](https://github.com/pulumi/examples/tree/master/cloud-js-api) ]

Us Node.js programmers love web frameworks, whether that be serving
static content using a single page application (SPA) built using
React.js, Vue.js, or Angular.js, a program built using dynamic
server-side logic using Express.js, or some combination thereof.
Serverless offers a way to run these programs at incredible density and
low cost, often reducing a VM- or container-based solution to 1/10th its
cost (or better). The problem is, this usually means abandoning
productive frameworks, and resorting to YAML, hand-authoring Swagger
files, and configuring complex API Gateway machinery -- all foreign
concepts when you just want to run a website.

Pulumi lets you just write code to host both static and dynamic content
simply, using its cross-cloud framework's cloud.API abstraction. It has
been designed to have a familiar Node.js feel. The following example
serves all static content underneath my www directory at the root, and
provides a simple GET endpoint at `/hello` that
returns a `{ hello: "World!" }` JSON object:

**index.ts**:

```javascript
import * as cloud from "@pulumi/cloud";
// Create a new API endpoint:
let app = new cloud.API("my-app");
// Serve static files from the `www` folder (using AWS S3):
app.static("/", "www");
// Serve a simple REST API on `GET /hello` (using AWS Lambda):
app.get("/hello", (req, res) => res.json({ hello: "World!" }));
// Export the public URL for the HTTP service:
export let url = app.publish().url;
```

All of the usual verbs are available -- `post`,
`patch`, etc. -- as is support for middleware.

The structure of my local filesystem will demonstrate how some of this
ties together:

```
.
├── Pulumi.yaml
├── index.ts
├── package.json
└── www
├── favicon.png
└── index.html
1 directory, 5 files
```

Again, all we need to do is `pulumi up`, and Pulumi
will figure out what has changed. So, if we are building an SPA using
React.js, etc., then we would simply have a build step that updates the
content, and the next time we run `pulumi up`, it
will figure out what has changed and make the minimal set of updates.
Similarly, if we edit a dynamic function, it will update just the
function.

As you can imagine, things get fun when you start mixing scenarios. Say
we wanted a web frontend to our Hacker News timer fetcher above. Thanks
to the way we can simply capture a reference to the snapshots database
and use it in the body of our API, this is extremely trivial.

Per the earlier conversation around mixing infrastructure and
application code, some folks prefer to split the routes from the
application code. This is a fine convention, and easy to do:

**index.ts**:

```javascript
import * as cloud from "@pulumi/cloud";
import * as routes from "./app/routes";

// Create an API like before, but use a routes module instead of defining inline:
let app = new cloud.API("my-app");
app.get("/hello", routes.hello);

export let url = app.publish().url;
```

For now, Pulumi only offers an AWS implementation of these APIs, but
more clouds are on their way!

## Containers

### Easy Deployment

[ [Runnable Example](https://github.com/pulumi/examples/tree/master/cloud-js-containers) ]

Let's shift gears again and take a look at containers. Pulumi supports
programming against raw container orchestrators -- Amazon's ECS, Azure's
ACS, Google Cloud's GKE, Kubernetes directly, and so on -- using the
cloud resources directly. In this mode, Pulumi is entirely unopinionated
about how containers are built, published, and deployed to your
orchestrator.

It is important that Pulumi supports that low-level approach, and is
what distinguishes it compared to PaaS-like offerings. This entails
significant spelunking at a level that is only loosely connected to the
task of standing up a container, however, which can be time-consuming
and frustrating for many developers. To make this common case easier,
Pulumi also offers higher-level abstractions to make these common cases
easier, similar in spirit to Docker Compose, except that you can mix
these abstractions with all your other cloud resources.

For example, to create a load balanced Nginx container using an image
from the Docker Hub:

**index.ts**:

```javascript
import * as cloud from "@pulumi/cloud";

let nginx = new cloud.Service("nginx", {
    image: "nginx",
    ports: [{ port: 80 }],
    replicas: 2,
});

export let url = nginx.defaultEndpoint;
```

This is all you need to run Nginx with 2 load balanced replicas
listening on port 80. By default, this will run in Fargate when
targeting AWS, which means you can skip the complications of configuring
an orchestrator. After running `pulumi up`, the
auto-assigned URL will be printed.

The image directive supports any normal Docker image URL, so private
registries work just as well as the default public Docker Hub. And there
are a number of other supported properties for memory and CPU
constraints, advanced port mapping, and volumes.

Now things get a bit more interesting. Let's say we wanted to build our
own custom container instead. Normally that would mean defining a
Dockerfile, provisioning a private registry, and manually building and
publishing your image to the registry, and then consuming that container
image from the registry. That's a lot of boilerplate scripting!

Pulumi unifies all container building, publishing, and consumption
underneath a simple `pulumi up`:

**index.ts**:

```javascript
import * as cloud from "@pulumi/cloud";

let nginx = new cloud.Service("nginx", {
    build: ".",
    ports: [{ port: 80 }],
    replicas: 2,
});

export let url = nginx.defaultEndpoint;
```

**Dockerfile**:

```
FROM nginx
COPY ./www /usr/share/nginx/html
```

This is trivial Dockerfile that derives from the nginx base image and
copies the ./www directory into the Nginx HTML target so that it will be
served up. This is our directory structure:

```
.
├── Dockerfile
├── Pulumi.yaml
├── index.ts
├── package.json
└── www
├── favicon.png
└── index.html
1 directory, 5 files
```

Of course, this Dockerfile could be arbitrarily complex, using any
Docker image.

### No Dockerfiles

[ [Runnable Example](https://github.com/pulumi/pulumi-cloud/tree/master/examples/containers) ]

The above example showed you how to create services that use Docker
containers, either via a pre-built image stored in a registry like the
Docker Hub, or by building one from a Dockerfile. The cloud.Service
class supports a third possibility, which is really fun, as it takes
advantage of Pulumi's serverless programming model earlier to define a
container and its service.

Imagine we want to define a simple Node.js webserver rather than using
Nginx like this. Perhaps it uses Express.js. For this blog post,
however, let's stick with the most basic http-module-based webserver:

**index.ts**:

```javascript
import * as cloud from "@pulumi/cloud";

let www = new cloud.Service("www", {
    function: () => {
        let rand = Math.random();
        require("http").createServer((req, res) => {
            res.end(`Hello, world! (from ${rand})`);
        }).listen(80);
    },
    ports: [{ port: 80 }]
    memory: 128,
    replicas: 2,
});

export let url = www.defaultEndpoint;
```

This code defines a load balanced service, backed by a container that
Pulumi builds on your behalf out of the body of the function provided in
the program, all done with a simple `pulumi up`
gesture. This function, of course, can close over other state just like
the earlier serverless examples, including cloud resources, making it as
easy as can be to connect your microservices.

### Long Running Containers as Tasks

[ [Runnable Example](https://github.com/pulumi/examples/tree/master/cloud-js-thumbnailer) ]

The above examples are great if what you want is a load balanced,
long-running service. Sometimes a container is useful simply for
executing a long-running task, or one that has very specific
requirements about its execution environment (such as a specific base
image).

For those cases, a cloud.Task is just what the doctor ordered. Task
supports all the same construction techniques as Service, so you can
give it a pre-built image, a build directive, or an inline function. For
purposes of illustration, let's build a custom Dockerfile that performs
an FFMPEG transformation, to extract a thumbnail anytime someone adds a
video to a bucket:

**index.ts**:

```javascript
let cloud = require("@pulumi/cloud-aws");
// A bucket to store videos and thumbnails.
let videos = new cloud.Bucket("bucket");
// A task which runs an FFMPEG transform to extract a thumbnail image.
let ffmpegThumbnailTask = new cloud.Task("ffmpegThumbTask", {
    build: ".",
    memoryReservation: 512,
});

// When a new video is uploaded, run the FFMPEG task on the video file.
videos.onPut(
    "onNewVideo",
    args => {
        let file = args.key;
        ffmpegThumbnailTask.run(
        {
            environment: {
                "S3_BUCKET":   videos.bucket.name.get(),
                "INPUT_VIDEO": file,
                "TIME_OFFSET": file.substring(file.indexOf('_')+1, file.indexOf('.')).replace('-',':'),
                "OUTPUT_FILE": file.substring(0, file.indexOf('_')) + '.jpg',
            },
        });
    },
    { keySuffix: ".mp4" });

exports.bucketName = videos.bucket.name;
```

**Dockerfile**:

```
FROM jrottenberg/ffmpeg
RUN apt-get update &&      apt-get install python-dev python-pip -y &&      apt-get clean
RUN pip install awscli
WORKDIR /tmp/workdir
ENTRYPOINT
echo "Starting ffmpeg task... " &&
echo "Copying video from s3://${S3_BUCKET}/${INPUT_VIDEO} to ${INPUT_VIDEO}..." &&
aws s3 cp s3://${S3_BUCKET}/${INPUT_VIDEO} ./${INPUT_VIDEO} &&
ffmpeg -v error -i ./${INPUT_VIDEO} -ss ${TIME_OFFSET} -vframes 1 -f image2 -an -y ${OUTPUT_FILE} &&
echo "Copying thumbnail to S3://${S3_BUCKET}/${OUTPUT_FILE} ..." &&
aws s3 cp ./${OUTPUT_FILE} s3://${S3_BUCKET}/${OUTPUT_FILE}
```

Notice that, just like before, this is backed by an ordinary Dockerfile.
This example actually showcases serverless and containers living
alongside one another in harmony. Notice how we kick off the task --
simply by capturing a reference to the Task from the serverless event
handler, and invoking its run method. This leverages Pulumi's ability to
give resources like Tasks custom APIs that can be invoked at runtime,
something we will return to again later on.

## General Tips and Tricks

### Avoid Hard-Coding Config

Let's return to our webserver example from earlier. Unfortunately, this
code will only work in one region, because we hard-coded the
`"ami-6869aa05"` image name (AMI). (Image names in
AWS are region-specific.) In general, we prefer to build Pulumi programs
that can be multi-instantiated across different regions. Pulumi's stacks
model streamlines this workflow, making it easy to spin up fresh copies
of your entire application and/or infrastructure when you need to scale,
while also reducing friction during development and testing. Such
hard-coding is a definite code smell and impediment, however.

Because we are using a real language, we can do anything that real
languages can do. That includes dynamically querying sources of
information which, in this case, can be used to avoid hard-coding. We
can even use the AWS SDK, which gives us full access to all AWS
functionality:

**ami.ts**:

```javascript
import * as aws from "@pulumi/aws";

export function getLinuxAmi(): Promise<string> {
    return new Promise<string>((resolve, reject) => {
        let ec2 = new (require("aws-sdk")).EC2({ region: aws.config.requireRegion() });
        ec2.describeImages(
            {
                Owners: [ "amazon" ],
                Filters: [{
                    Name: "name",
                    Values: [ "amzn-ami-hvm-????.??.?.x86_64-gp2" ],
                }],
            },
            (err: any, data: any) => {
                if (err) {
                    reject(err);
                } else {
                    let newestImage: string | undefined;
                    let newestImageDate: number | undefined;
                    for (let image of data.Images) {
                        let imageDate = Date.parse(image.CreationDate);
                        if (!newestImage || !newestImageDate ||
                            imageDate > newestImageDate) {
                            newestImage = image.ImageId;
                            newestImageDate = imageDate;
                        }
                    }
                    if (newestImage) {
                        console.log(`AMI: ${newestImage} (${newestImageDate})`);
                        resolve(newestImage);
                    } else {
                        reject("No Linux AMI found for the current region");
                    }
                }
            },
        );
    });
}
```

I'll be the first to admit that this is code that only a mother could
love. Even better would be to wrap it up in a reusable NPM package that
others can use without the boilerplate! Either way, it's very powerful
to have the full capabilities of a language at our fingertips, as this
sort of thing simply isn't possible in other infra-as-code solutions.

Now that we have this function, we can revisit the way we set the AMI
property on our VMs:

**web.ts**:

```javascript
import * as aws from "@pulumi/aws";
import { getLinuxAmi } from "./ami";

let webSg = new aws.ec2.SecurityGroup("web-secgrp", {
    ingress: [
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});

export class WebServer {
    public readonly vm: aws.ec2.Instance;

    constructor(name: string) {
        this.vm = new aws.ec2.Instance(`${name}`, {
            instanceType: "t2.micro",
            ami: getLinuxAmi(),
            securityGroups: [ webSg.name ],
            userData: `#!/bin/bashn` +
                `echo 'Hello from ${name}!' > index.htmln` +
                `nohup python -m SimpleHTTPServer 80 &n`,
        });
    }
}
```

Given this change, we can safely deploy our WebServer to any AWS region.

### Multi-Instantiation and Code Reuse

In the webserver example, we used the
`aws.config.requireRegion()` function to obtain the
configured AWS region. Using configuration in this manner lets us
multi-instantiate stacks; in other words, to easily stand up multiple
copies of a service, application, or infrastructure.

We can even make the quantity configurable using Pulumi's config system:

**index.ts**:

```javascript
import { WebServer } from "./web";
import { Config, getProject } from "@pulumi/pulumi";

let config = new Config(getProject());
let webServers = [];
let webServersCount = config.getNumber("count") || 3;
for (let i = 0; i < webServersCount; i++) {
    webServers.push(new WebServer(`web-server-${i}`));
}

export let publicHostnames = webServers.map(s => s.vm.publicDns);
```

Given this specific program, we can easily change the number of servers
created from the default of three, to something larger:

```
$ pulumi config set count 7
```

There are plenty of opportunities for configuration like this, like the
machine size. By making such settings configurable, different
environments can easily have different settings, while still sharing the
same code beneath them, eliminating copy-and-paste and its associated
pitfalls.

### Give Components Runtime APIs

[ [Runnable Example](https://github.com/pulumi/examples/blob/master/cloud-ts-url-shortener-cache/cache.ts) ]

As our final example, let's see how to give your own components APIs
that can be invoked at runtime. We've already seen this a few times now,
such as managing data in a cloud.Table that has been captured in a
lambda, and cloud.Task's run method. Pulumi is built to be extensible,
so you can define your own abstractions just like these with APIs too.

For this example, let's take a simple Redis cache service and turn it
into a component. After doing so, we can then add simple
`get`/`set` APIs on it that let
you interact with the cache at runtime in simple ways. By providing this
sort of abstraction, we open up interesting possibilities. For instance,
our default implementation can use a custom container-backed service,
via `cloud.Service`, but opt to use a simpler hosted
solution when running in a public cloud -- AWS ElastiCache, Azure Redis
Cache, or Memorystore in Google Cloud.

To make our component, we will simply allocate a
`cloud.Service` in the constructor, taking an
optional memory parameter to control its memory reservation. We are
using configuration to read the Redis password using Pulumi's built-in
secrets mechanism. To give that component APIs, we just define methods
on the class that access Redis through its own NPM package, and that's
it! The way lambda capture works will ensure that these functions are
accessible:

**cache.ts**:

```javascript
import * as cloud from "@pulumi/cloud";
import * as config from "./config";

// A simple cache abstraction that wraps Redis.
export class Cache {
    public readonly get: (key: string) => Promise<string>;
    public readonly set: (key: string, value: string) => Promise<void>;
    private readonly redis: cloud.Service;

    constructor(name: string, memory: number = 128) {
        this.redis = new cloud.Service(name, {
            image: "redis:alpine",
            memory: memory,
            ports: [{ port: 6379 }],
            command: ["redis-server", "--requirepass", config.redisPassword],
        });
    }

    public async get(key: string): Promise<string> {
        let client = await this.createRedisClient();
        return new Promise<string>((resolve, reject) => {
                client.get(key, (err: any, v: any) => {
                if (err) reject(err);
                else     resolve(v);
            });
        });
    }

    public async set(key: string, value: string): Promise<void> {
        let client = await this.createRedisClient();
        return new Promise<void>((resolve, reject) => {
            client.set(key, value, (err: any, v: any) => {
                if (err) reject(err);
                else     resolve();
            });
        });
    }

    private async createRedisClient(): Promise<any> {
            let ep = (await this.redis.defaultEndpoint).get();
            return require("redis").createClient(
                ep.port, ep.hostname, { password: config.redisPassword });
        }
    }
}
```

Because this is just a class, we have all the standard programming
facilities available to us. If we wanted to specialize it to use our
cloud's hosted Redis services, we could do that using the standard
techniques, including conditional code or, slightly more elegantly,
using concrete subclasses for the different options.

Now that we've defined our cache, we can create an instance, and then
use it from within a callback, such as a serverless API implementation.
This is a fairly complex application that acts as a URL shortener, with
both GET and POST endpoints, but really shows off the power of combining
many of the techniques we've seen throughout this post:

**index.ts**:

```javascript
import * as cloud from "@pulumi/cloud";
import * as cache from "./cache";

// Create a URL shortener app and a table to hold shortened URLs.
let app = new cloud.API("shortener");
let urlTable = new cloud.Table("urls", "name");

// Use our cache component to cache frequently accessed URLs.
let urlCache = new cache.Cache("urlcache");

// GET /url lists all URLs currently registered.
endpoint.get("/url", async (req, res) => {
    try {
        res.status(200).json(await urlTable.scan());
    } catch (err) {
        res.status(500).json(err.stack);
    }
});

// GET /url/{name} redirects to the target URL based on a short-name.
endpoint.get("/url/{name}", async (req, res) => {
    let name = req.params["name"];
    try {
        // First try the Redis cache. If we miss, consult the table.
        let url = await urlCache.get(name);
        if (url) {
            res.setHeader("X-Powered-By", "redis");
        } else {
            let value = await urlTable.get({ name });
            if (value && value.url) {
                url = value.url;
                urlCache.set(name, url); // cache for next time.
            }
        }

        // If we found an entry, 301 redirect to it; else, 404.
        if (url) {
            res.setHeader("Location", url);
            res.status(302);
            res.end("");
        } else {
            res.status(404);
            res.end("");
        }
    } catch (err) {
        res.status(500).json(err.stack);
    }
});

// POST /url registers a new URL with a given short-name.
endpoint.post("/url", async (req, res) => {
    let url = req.query["url"];
    let name = req.query["name"];

    try {
        // Insert into the table and our URL cache.
        await urlTable.insert({ name, url });
        await urlCache.set(name, url);
        res.json({ shortenedURLName: name });
    } catch (err) {
        res.status(500).json(err.stack);
    }
});

export let url = endpoint.publish().url;
```

Notice that we can capture and use our `Cache`
component just like we can the `cloud.Table`!

We've only scratched the surface of what's possible with components and
custom APIs, however hopefully you're starting to get a sense of why
this is such a powerful capability.

## Winding Down

In this post, we've seen how Pulumi can define infrastructure,
containers, and serverless cloud software, often combining many of the
techniques together to build powerful distributed applications. This
includes programming to specific resources that your cloud of choice
provides, in addition to writing higher level cloud programs that are
able to target many clouds (expect more multi-cloud progress here in the
weeks to come -- including Kubernetes). Each pearl is a topic unto
itself; we'd love your feedback on what topics to dig into next.

Happy hacking -- and have fun programming the cloud!
