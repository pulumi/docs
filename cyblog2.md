Simple Serverless programmin in Google Cloud using Pulumi.

A main goal of Pulumi is to help simplify, or outright remove, the myriad forms of complexity around programming the cloud.  One of the main forms of complexity removed is needing to either manually create your infrastructure through cloud CLIs, or using different and esoteric languages to try to declare and maintain your cloud infrastructure.  Instead, we think you should be able to use the programming languages you know and are already comfortable with to easily define and maintain using the languages, libraries, patterns and abstractions you're already comfortable with.

Serverless programming is another area where we want to bring the same convenience and simplicity.  The main goal of Serverless programming is to enable users to just define a piece of code they want to run in the cloud in response to some event.  The cloud provider (AWS, GCP, Azure, etc.) is then responsible for executing that code by dynamically allocating, and normally charging for, the resources necessary for it.  The code is typically run inside stateless containers that can be triggered by a variety of events including http requests, bucket changes, pubsub messages, cron jobs, db events, etc.  However, while the different cloud providers make it simple to scale infrastructure for your Serverless code, it's often overly complex to actually supply them with the code you want to run, define when you want to run it, and then provide your code with the necessary information to access and effectively interact with the rest of your infrastructure.  With Pulumi, we've made it easy to do all on Google's cloud platform directly from your Pulumi App.

Let's start with a simple example that shows how you can do this in Pulumi today using the skeleton structure for a SlackBot:

```ts
// config we can use to validate incoming messages as well as properly authenticate if we send messages to slack ourself.
const config = new pulumi.Config("mentionbot");
const slackToken = config.get("slackToken");
const verificationToken = config.get("verificationToken");

// A topic that we can enqueue slack events to so they can be processed in batch later on.
const messageTopic = new gcp.pubsub.Topic("messages");

// Create an API endpoint that slack will use to push events to us with.
const endpoint = new gcp.cloudfunctions.HttpCallbackFunction("mentionbot", {
    callbackFactory: () => {
        const app = express();
        app.use(bodyParser.json());
        app.post("/events", (req, res) => {
            // Importantly: the code in this arrow-function is the code that will run in your serverless GCP cloud function!

            const body = req.body;
            
            // Process the body as appropriate.  if it's something we need to respond to immediately
            // (like a verification request), then do so. Otherwise, add the message to our pubsub
            // topic to be processed later:
            const pubSub = new PubSub();
            const topic = pubSub.topic(messageTopic.name.get());
            topic.publish(Buffer.from(JSON.stringify(body)));            

            // quickly respond with success so that slack doesn't retry.
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

This is the real structure for a *single* Pulumi App that both defines all the cloud resources you'd need, and also allows you to write your serverless functions inline, to make a real world SlackBot running in your GCP cloud.  All you'd need to do at this point is flesh out the code in the two JavaScript arrow-functions to add your domain-specific logic for your SlackBot.  To see a full example of take a look at our [@mentionbot example](https://github.com/pulumi/examples/tree/master/gcp-ts-slackbot).  This bot will listen for mentions of your name and will notify you of them in a channel of your choosing.  This gives you a persistent timeline you can go back to look at to make sure you can find, and have responded to, all important messages.

This example actually hides away a large amount of complexity that you would normally be responsible for.  For you would normally have to:

1. Figure out the shape (the input/output-types) for your Cloud Functions, and then create an appropriate program exporting the right entrypoint that matches.  In this case, because we've exposed the right abstractions (like `HttpCallbackFunction` and `Topic.onMessagePublished`), the arrow-functions you pass in will all have the right types, and your program will be typechecked by TypeScript.
1. Create separate Cloud Functions for each Serverless callback.  One for listening and responding to the initial Slack events, and the second for processing the messages in the Topic.  However, here you can write a single Pulumi App where all the code can be placed how you like it (in this case in a single file).
1. [Package](https://cloud.google.com/functions/docs/writing/) each callback up in the appropriate structure Cloud Functions expects, including how to include or reference your dependencies properly.
1. Create a [Storage Bucket](https://cloud.google.com/storage/docs/creating-buckets) for all of our packaged programs to live in.
1. Upload each packaged program to a [Bucket Object](https://cloud.google.com/storage/docs/uploading-objects) in that bucket.
1. Configure the appropriate triggers on your Cloud Function stating how it should be triggered (for example, in response to an [HTTP trigger](https://cloud.google.com/functions/docs/calling/http) or a [Pub/Sub trigger](https://cloud.google.com/functions/docs/calling/pubsub)).  
1. Include the right information in each Cloud Function's [environment variables](https://cloud.google.com/functions/docs/env-var) (or just hardcode them in '1' so that your program can access the rest of your cloud infrastructure.  In the above example, you can see how you can just reference your resources directly (like the PubSub Topic) *directly* from your Cloud Function callback.  Pulumi makes sure this all works, and that the data you use is available in that Cloud Function.
1. Figure out a safe way to encode and access secrets for your Cloud Function in case your code needs that to safely and securely accesss resources.  Here, we can just use Pulumi's [Config Secrets](https://pulumi.io/reference/config.html#secrets) to safely encrypt and make secrets available to your Cloud Function code.

This is a lot to figure out and continually manage over the lifetime of your cloud application.  If you want to tweak things even slightly you might need to go make many manual changes and updates to ensure everything is properly updated.  However, in that single Pulumi App this is all taken care of for you.  For example, say you were to change the above example to use [Cloud Tasks](https://cloud.google.com/tasks/) insead of [PubSub](https://cloud.google.com/pubsub/).  You would just have to change to use the resurce you wanted near the top of the file.  You'd then get automatically told by TypeScript that you were using the resource improperly in your code.  Once you fixed it up, you could simply run `pulumi up`, and have the entirety of your stack properly updated (including having all those steps above automatically taken care of for you).

At Pulumi, we think the cloud should be simpler to create and maintain applications for.  As we’ve seen above, with a tiny amount of code, you can easily define the Google Cloud resources you want to create (or reference your existing cloud resources). It’s then simple to add code to to run serverless Cloud Function code in response to the events you care about. One codebase, containing all the pieces of relevance for your cloud application, that's easy to create, update, and maintain for the life of your app.  We think this is how easy all cloud programming should be, and we hopw you think so too!

PS: If you're interested in how Pulumi manages to take a JavaScript/TypeScript `=>` function and somehow analyze and transform it into a form that Cloud Functions can use, please see our deep dive on this topic here: [Lambdas as Lambdas: The magic of simple serverless Functions](https://blog.pulumi.com/lambdas-as-lambdas-the-magic-of-simple-serverless-functions).  We're leveraging the same great programming language and analysis framework to power our GCP solution here.
