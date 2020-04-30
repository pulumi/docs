---
title: Simple Serverless programming with Google Cloud Functions
h1: "Simple Serverless programming with Google Cloud Functions and Pulumi"
authors: ["cyrus-najmabadi"]
tags: ["Serverless","GCP"]
date: "2019-04-10"
meta_desc: "Pulumi lets you create, deploy, and manage Google Cloud applications and infrastructure in familiar languages without needing DSLs or YAML templating solutions."

---

Pulumi lets you create, deploy, and manage Google Cloud applications and
infrastructure in familiar languages like JavaScript, TypeScript, and
Python, and without needing to learn new DSLs or YAML templating
solutions. This means great productivity and getting to use tools you
already know and love. Since serverless is all about focusing more on
your application code, and less on infrastructure and configuration
toil, we absolutely love Google Functions.
<!--more-->

## The Simplest Way to Serverless

In fact, serverless has never been simpler than it is when you combine
Pulumi with Google Cloud Functions. Want to serve a simple HTTP API with
no fixed costs? It's just a few lines of code -- and no, we're not
hiding any YAML here:

```typescript
import * as gcp from "@pulumi/gcp";

let greeting = new gcp.cloudfunctions.HttpCallbackFunction("greeting", (req, res) => {
    // Change this code to fit your needs!
    res.send(`Greetings from ${req.body.name || 'Google Cloud Functions'}!`);
});

export let url = greeting.httpsTriggerUrl;
```

Thanks to Pulumi's language heritage, we know how to take that
function, serialize it, and publish it to a Google Bucket and Object,
eliminating those tedious manual steps behind a single `pulumi up` CLI
invocation.

Or perhaps a [pubsub](https://cloud.google.com/pubsub/) topic that runs
some custom code on every message received. This sounds like a perfect
use case for an event-driven style of programming, so why don't we
write it that way!

```typescript
// Create a PubSub Topic
let requests = new gcp.pubsub.Topic("requests");
requests.onMessagePublished("newMessage", (data) => {
    // Print out a log message for every message on the Topic.
    // Change this code to fit your needs!
    console.log(Buffer.from(data.data, "base64").toString());
});
```

Because Pulumi knows how to manage infrastructure as code, it can
provision and manage not only the Google Cloud Function, but also the
pubsub topic resource itself, for each creation and management.

Or perhaps, we'd like a function that respond to any uploads of new
objects to your [storage](https://cloud.google.com/storage/) bucket:

```typescript
// Create a Storage Bucket
let bucket = new gcp.storage.Bucket("data");
bucket.onObjectFinalized("newobject", (data) => {
    // Print out a log message for every upload to the Bucket.
    // Change this code to fit your needs!
    console.log(`New file uploaded: ${data.name}`);
});
```

## A Complete Google Functions Slack Bot

For an idea of how you might fit these together to make a real-world
cloud application, let's look a simple skeleton structure for a
[Slack Bot](https://api.slack.com/bot-users) using Pulumi and Google Cloud
Functions:

```typescript
// secure config tokens to use to validate incoming messages as well as authenticate ourself to slack
const config = new pulumi.Config("mentionbot");
const slackToken = config.get("slackToken");
const verificationToken = config.get("verificationToken");

// A topic that we can enqueue slack events to so they can be processed in batch later on
const messageTopic = new gcp.pubsub.Topic("messages");

// Create an http endpoint that slack will use to push events to us.
const endpoint = new gcp.cloudfunctions.HttpCallbackFunction("bot", {
    callbackFactory: () => {
        const app = express();
        app.use(bodyParser.json());
        app.post("/events", (req, res) => {
            // Importantly: This is the code that will run in your serverless GCP cloud function!

            const body = req.body;

            // Process the body as appropriate. If it's something we need to respond to immediately
            // (like a verification request), then do so. Otherwise, add the message to our pubsub
            // topic to be processed later:
            const pubSub = new PubSub();
            const topic = pubSub.topic(messageTopic.name.get());
            topic.publish(Buffer.from(JSON.stringify(body)));

            // Quickly respond with success so that slack doesn't retry.
            res.status(200).end();
        });

        return app;
    }
});

messageTopic.onMessagePublished("processTopicMessage", async (data) => {
    // Actually handle the 'data' in the pubsub message.
    // Importantly: This is the code that will run in your serverless GCP cloud function!
});

// Give this url to slack to let them know where to post their events to.
export const url = endpoint.httpsTriggerUrl;
```

This is the real code for a complete SlackBot application running on
GCP, from the cloud resources to the serverless code, all within a
unified Pulumi application! Customizing this for your own use case is as
simple as changing the code in the two JavaScript arrow-functions.

To see the complete project, take a look at our
[@mentionbot example](https://github.com/pulumi/examples/tree/master/gcp-ts-slackbot).
That example will listen for mentions of your name and will notify you
of them in a channel of your choosing, giving you you a persistent
timeline you can go back to look at to make sure you can find all these
messages.

Although it's a simple example, there are a lot of moving parts this
takes care of that you would normally be responsible for. This includes:

1. Figuring out the shape (the input/output-types) for your Cloud
    Functions, and then creating an appropriate program that exports the
    right entrypoint that matches. In this case, because we've exposed
    the right abstractions (like `HttpCallbackFunction` and
    `Topic.onMessagePublished`), the arrow-functions you pass in will
    all have the right types, and your program will be typechecked by
    TypeScript.
2. Creating separate Cloud Functions for each serverless callback. One
    for listening and responding to the initial Slack events and the
    second for processing the messages in the Topic. Here, you can write
    a single Pulumi App where all the code can be placed how you like it
    (in this case in a single file).
3. [Packaging](https://cloud.google.com/functions/docs/writing/) each
    callback up in the appropriate structure Cloud Functions expects,
    including how to get all your dependencies in place.
4. Creating a [Storage
    Bucket](https://cloud.google.com/storage/docs/creating-buckets) for
    all of your packaged programs to live in.
5. Uploading each packaged program to a [Bucket
    Object](https://cloud.google.com/storage/docs/uploading-objects) in
    that bucket.
6. Configuring the appropriate triggers on your Cloud Functions stating
    how they should be triggered (for example, in response to an [HTTP
    trigger](https://cloud.google.com/functions/docs/calling/http) or a
    [Pub/Sub
    trigger](https://cloud.google.com/functions/docs/calling/pubsub)).
7. Including the right information in the function so you can interact
    with your other cloud resources in the Pulumi App. Without this, you
    would need to find a way to include that data in each Cloud
    Function's [environment
    variables](https://cloud.google.com/functions/docs/env-var) (or just
    hardcode them in '1') so that your program can access the rest of
    your cloud infrastructure. In the above example, you can see how you
    can just reference your resources directly (like the PubSub Topic)
    *directly* from your Cloud Function callback. Pulumi makes sure this
    all works, and that the data you use is available in that Cloud
    Function when it finally is triggered.
8. Figuring out a safe and secure way to encode and access secrets for
    your Cloud Function. Here, we can use Pulumi's
    [Config Secrets]({{< prelref "/docs/intro/concepts/config#secrets" >}}) to safely
    encrypt and manage secrets for your Cloud Function code.

Not to mention that by doing all of that, you can achieve continuous deployment
[Pulumi and Google Cloud Build]({{< prelref "/docs/guides/continuous-delivery/google-cloud-build" >}}).

## Updating Your Google Functions Code

This is a lot to figure out to manage cloud applications and
infrastructure. If you want to tweak things even slightly you might need
to go make many manual changes and updates to ensure everything is
properly updated. With Pulumi, all this complexity is handled with a
single update! Just run `pulumi up` , and it figures out the rest.

Let's just take a look at what Pulumi does when you tweak a few things
in the program:

    $ pulumi up
    Updating (slackbot):
         Type                                       Name                        Status       Info
         pulumi:pulumi:Stack                        slackbot
     +-  ├─ gcp:pubsub:Topic                        messages                    replaced     [diff: +labels]
         │  └─ gcp:cloudfunctions:CallbackFunction  processTopicMessage
     +-  │     ├─ gcp:storage:BucketObject          processTopicMessage         replaced     [diff: ~name,source]
     ~   │     └─ gcp:cloudfunctions:Function       processTopicMessage         updated      [diff: ~eventTrigger,sourceArchiveObject]
         └─ gcp:cloudfunctions:CallbackFunction     mentionbot
     +-     ├─ gcp:storage:BucketObject             mentionbot                  replaced     [diff: ~name,source]
     ~      └─ gcp:cloudfunctions:Function          mentionbot                  updated      [diff: ~sourceArchiveObject]
     
    Outputs:
        url: "https://***.cloudfunctions.net/mentionbot"
     
    Resources:
        ~ 2 updated
        +-3 replaced
        2 changes. 5 unchanged
     
    Duration: 52s

One command later, and your entire stack is updated properly!

## Winding Down

The cloud provides tremendous potential, and we want to make it easy for
developers to tap into that potential. Using Pulumi, it's easy to blur
the line between business logic and serverless resources, bringing the
focus back to the problems you care about. One codebase that's easy to
create, update, and maintain.

To check things out, get started today:

- [Get Started with Pulumi on GCP]({{< prelref "/docs/get-started/gcp" >}})
- [Deploy a Minimal Google Cloud Function Application](https://github.com/pulumi/examples/tree/master/gcp-ts-functions)

PS: If you're interested in how Pulumi manages to take a
JavaScript/TypeScript `=>` function and somehow analyze and transform it
into a form that Cloud Functions can use, please see our deep dive on
this topic in:
[**Lambdas as Lambdas: The magic of simple serverless Functions**]({{< prelref "lambdas-as-lambdas-the-magic-of-simple-serverless-functions" >}}).
We're leveraging the same great programming language and analysis
framework to power our GCP solution here.
