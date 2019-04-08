Simple Serverless programming in Google Cloud using Pulumi.

Serverless has never been simpler than it is with Pulumi + Google Cloud Functions.  Want to serve a simple HTTP API with no fixed costs?  It's just a few lines of code:

```typescript
import * as gcp from "@pulumi/gcp";

let greeting = new gcp.cloudfunctions.HttpCallbackFunction("greeting", (req, res) => {
    // Add more code here as you see fit!
    res.send(`Greetings from ${req.body.name || 'Google Cloud Functions'}!`);
});

export let url = greeting.httpsTriggerUrl;
```

Or perhaps a [pubsub](https://cloud.google.com/pubsub/) topic that runs some custom code on every message received:

```typescript
// Create a PubSub Topic
let requests = new gcp.pubsub.Topic("requests");
// Print out a log message for every message on the Topic
requests.onMessagePublished("newMessage", (data) => {
    // Add more code here as you see fit!
    console.log(Buffer.from(data.data, "base64").toString());
});
```

Or perhaps respond to any uploads of new objects to your [storage](https://cloud.google.com/storage/) bucket:


```typescript
// Create a Storage Bucket
let requests = new gcp.storage.Bucket("data");
// Print out a log message for every message on the Topic
requests.onObjectFinalized("newobject", (data) => {
    // Add more code here as you see fit!
    console.log(`New file uploaded: ${data.name}`);
});
```

For an idea of how you might fit these together to make a real-world cloud application, let's look a simple skeleton structure for a SlackBot using Pulumi:

```ts
// config tokens to use to validate incoming messages as well as properly authenticate ourserlf when sending messages to slack
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
            // Importantly: the code in this arrow-function is the code that will run in your serverless GCP cloud function!

            const body = req.body;
            
            // Process the body as appropriate.  If it's something we need to respond to immediately
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
    // Importantly: the code in this arrow-function is the code that will run in your serverless GCP cloud function!
});

// Give this url to slack to let them know where to post their events to.
export const url = endpoint.httpsTriggerUrl;
```

This is the real code for a complete SlackBot application running on GCP, from the cloud resources to the Serverless code, all within a unified Pulumi App!  Customizing this for your own use case is as simple as changing the code in the two JavaScript arrow-functions.  To see the complete project, take a look at our [@mentionbot example](https://github.com/pulumi/examples/tree/master/gcp-ts-slackbot).  That example will listen for mentions of your name and will notify you of them in a channel of your choosing, giving you you a persistent timeline you can go back to look at to make sure you can find all these messages.

Although it's a simple example, there are a lot of moving parts that you would normally be responsible for:

1. figure out the shape (the input/output-types) for your Cloud Functions, and then create an appropriate program exporting the right entrypoint that matches.  In this case, because we've exposed the right abstractions (like `HttpCallbackFunction` and `Topic.onMessagePublished`), the arrow-functions you pass in will all have the right types, and your program will be typechecked by TypeScript.
1. Create separate Cloud Functions for each Serverless callback.  One for listening and responding to the initial Slack events, and the second for processing the messages in the Topic.  Here, you can write a single Pulumi App where all the code can be placed how you like it (in this case in a single file).
1. [package](https://cloud.google.com/functions/docs/writing/) each callback up in the appropriate structure Cloud Functions expects, including how to include or reference your dependencies properly.
1. create a [Storage Bucket](https://cloud.google.com/storage/docs/creating-buckets) for all of our packaged programs to live in.
1. upload each packaged program to a [Bucket Object](https://cloud.google.com/storage/docs/uploading-objects) in that bucket.
1. configure the appropriate triggers on your Cloud Function stating how it should be triggered (for example, in response to an [HTTP trigger](https://cloud.google.com/functions/docs/calling/http) or a [Pub/Sub trigger](https://cloud.google.com/functions/docs/calling/pubsub)).  
1. include the right information in the function so you can interact with your other cloud resources in the Pulumi App.  Without this, you would need to find a way to include that data in each Cloud Function's [environment variables](https://cloud.google.com/functions/docs/env-var) (or just hardcode them in '1') so that your program can access the rest of your cloud infrastructure.  In the above example, you can see how you can just reference your resources directly (like the PubSub Topic) *directly* from your Cloud Function callback.  Pulumi makes sure this all works, and that the data you use is available in that Cloud Function.
1. Figure out a safe and secure way to encode and access secrets for your Cloud Function.  Here, we can use Pulumi's [Config Secrets](https://pulumi.io/reference/config.html#secrets) to safely encrypt and manage secrets for your Cloud Function code.

This is a lot to figure out and continually manage over the lifetime of your cloud application.  If you want to tweak things even slightly you might need to go make many manual changes and updates to ensure everything is properly updated.  With Pulumi, all this complexity is handled with a single update!  Let's just take a look at what Pulumi does when you tweak those `=>` functions in some way.

```bash
$ pulumi up
Updating (slackbot):
     Type                                       Name                        Status       Info
     pulumi:pulumi:Stack                        slackbot
 +-  ├─ gcp:pubsub:Topic                        messages                    replaced     [diff: +labels~name]
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
```

The cloud provides tremendous potential, and we want to make it easy for developers to tap into those resources. Using Pulumi, it's easy to mix and match cloud resources with your own business logic, bringing the focus back to the problems you care about. One codebase, from cloud infrastructure to app logic, that's easy to create, update, and maintain.

PS: If you're interested in how Pulumi manages to take a JavaScript/TypeScript `=>` function and somehow analyze and transform it into a form that Cloud Functions can use, please see our deep dive on this topic here: [Lambdas as Lambdas: The magic of simple serverless Functions](https://blog.pulumi.com/lambdas-as-lambdas-the-magic-of-simple-serverless-functions).  We're leveraging the same great programming language and analysis framework to power our GCP solution here.
