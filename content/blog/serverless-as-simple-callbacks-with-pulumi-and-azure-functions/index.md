---
title: "Serverless as Simple Callbacks with Pulumi and Azure Functions"
authors: ["mikhail-shilkov"]
tags: ["Serverless","Azure"]
date: "2019-05-07"
meta_desc: "Pulumi's serverless programming model makes it easy to take a Node.js function and deploy it to Azure as an HTTP endpoint. Pulumi leverages general-purpose programming languages like TypeScript for a consistent approach to defining and delivering serverless applications such as asynchronous message passing, ServiceBus topic subscription, and Blob container image upload notification."

---

_Today's guest post is from [Mikhail Shilkov](https://mikhail.io/), a
Microsoft Azure MVP and early Pulumi user and contributor - enjoy!_

Serverless compute services, like Azure Functions, offer an amazing
power to application developers to leverage: highly available,
automatically scaled, low-ceremony, pay-per-value functions created in
several lines of code.
<!--more-->

So, what's **the simplest** way to take a Node.js function and deploy it
to Azure cloud as an HTTP endpoint? How about this little tutorial:

## 1. Create a new Pulumi program:

    $ pulumi new azure-typescript

## 2. Define an HTTP endpoint in `index.ts`:

```typescript
import * as azure from '@pulumi/azure';

const resourceGroup = new azure.core.ResourceGroup('example', { location: 'West US' });

const greeting = new azure.appservice.HttpEventSubscription('greeting', {
    resourceGroup,
    callback: async (context, req) => {
        return {
            status: 200,
            body: `Hello ${req.query['name'] || 'World'}!`
        };
    }
});

export const url = greeting.url;
```

## 3. Deploy:

    $ pulumi up
     
    Updating:
       Type
     + pulumi:pulumi:Stack
     + ├─ azure:appservice:HttpEventSubscription
     + │  ├─ azure:storage:Account
     + │  ├─ azure:appservice:Plan
     + │  ├─ azure:storage:Container
     + │  ├─ azure:storage:ZipBlob
     + │  └─ azure:appservice:FunctionApp
     + └─ azure:core:ResourceGroup
     
    Outputs:
       url: "https://greetingc21a23fe.azurewebsites.net/api/greeting"
    Resources:
       + 8 created

## 4. Access your function via HTTP:

    $ curl https://greetingc21a23fe.azurewebsites.net/api/greeting?name=Pulumi
    Hello Pulumi!

With 12 lines of code and two CLI commands, I've created all Azure
resources required to host a serverless function without an explicit
configuration of Azure services. Okay, I had to define a location for my
resource group, but that could also be accomplished via `pulumi config`.

Pulumi compiled my TypeScript function, serialized it to a JavaScript
file, created the bindings in a `function.json` file, hosting
configuration in a `host.json` file, uploaded all these assets to Blob
Storage, and configured a Consumption Plan and a Function App to run my
function. An automated and reproducible deployment in less than two
minutes.

## Beyond Hello-World

The power of Node.js comes from the richness of its library ecosystem.
There's an NPM package for everything, so you definitely want to use
those.

Serverless-function-as-callback imports dependencies in a transparent
way. Install the NPM packages of your choice and use them inside the
callback:

```typescript
import * as moment from 'moment';

const greeting = new azure.appservice.HttpEventSubscription('greeting', {
    resourceGroup,
    callback: async (context, req) => {
        return {
            status: 200,
            body: `Hello ${req.query['name'] || 'World'} at ${moment().format('LLLL')}!`
        };
    }
});
```

The packages get zipped up inside the deployment artifact automatically
so that the Function App can find them at the startup. So there's no
need to manually figure out how to produce the archive, get it uploaded,
and maintain it as your libraries get updated.

Stay tuned for another blog post with a full implementation of a
serverless URL shortener application deployed into multiple Azure
regions for fast response time and improved resiliency.

## Not Only HTTP

Your application might not be a bunch of HTTP functions. You probably
want to leverage queues for asynchronous message passing. How about
defining a callback on the queue object itself:

```typescript
const storageAccount = new azure.storage.Account("storage", {
   resourceGroupName: resourceGroup.name,
   location: resourceGroup.location,
   accountReplicationType: "LRS",
   accountTier: "Standard",
});

const queue = new azure.storage.Queue("myqueue", {
  resourceGroupName: resourceGroup.name,
  storageAccountName: storageAccount.name
});

queue.onEvent("newMessage",  async (context, msg) => {
   // code to process 'msg' however you want here
   console.log("Message received: " + msg.toString());
});
```

Alternatively, define a ServiceBus topic and immediately subscribe to
the messages:

```typescript
import * as servicebus from "@pulumi/azure/eventhub";

const namespace = new servicebus.Namespace("test", {
   resourceGroupName: resourceGroup.name,
   sku: "standard",
});

const topic = new servicebus.Topic("mytopic", {
   resourceGroupName: resourceGroup.name,
   namespaceName: namespace.name,
});

export const subscription = topic.onEvent("mysubscription", async (context, msg) => {
   console.log("Received: " + msg.toString());
});
```

In addition, get notified when a new PNG image is uploaded to a Blob
Container:

```typescript
const storageContainer = new azure.storage.Container("images-container", {
  resourceGroupName: resourceGroup.name,
  storageAccountName: storageAccount.name,
  name: "images",
});

storageContainer.onBlobEvent("newImage", {
   callback: async (context, blob) => {
       console.log("File size: " + context.bindingData.properties.length);
   },
   filterSuffix: ".png",
});
```

In all these examples, you get a fully configured Function App on
Consumption Plan ramped up and bound to the trigger of choice. Your
callback runs in the cloud handling every event with no manual work of
hooking these different components together.

Using a general-purpose language like TypeScript provides one consistent
approach to defining and delivering serverless applications and
infrastructure as one cohesive application.

We strive to make cloud development as simple as everyday JavaScript
development that made the language so successful. A lot is happening
behind the scenes, but the code still looks like "normal code".
Composition of cloud resources should be as straightforward as hooking
up components in any traditional application.

## Looking Ahead

Pulumi serverless programming model for Azure Functions is just ramping
up. There is only a handful of trigger types supported right now, and
some configuration parameters are not exposed yet.

So, today is the perfect time to chime in and join the discussion! Help
us answer the questions:

- Is this programming model beneficial to your scenarios?
- Which trigger types do you want to be supported?
- How should we package multiple functions into Function App(s)?
- Do you need input and output bindings to be supported, and if yes,
  in which shape?

Feel free to create an issue on
[GitHub](https://github.com/pulumi/pulumi-azure/), tag us on
[Twitter](https://twitter.com/PulumiCorp), or join our
[community Slack channel](https://slack.pulumi.com/).

Happy serverless programming!
