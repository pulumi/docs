The magic of simple, serverless, computing.

Many Cloud providers, like AWS, Azure and GCP, have all embraced the idea of providing [Function as a Service](https://en.wikipedia.org/wiki/Function_as_a_service) (FaaS) functionality to their platforms.  This functionality allows users of that platform to easily run logic for their cloud applications, without necessarily having to build or otherwise maintain the necessary underlying infrastructure for that logic themselves.  FaaS systems tend to differ from more established [Platform as a Service](https://en.wikipedia.org/wiki/PaaS) (PaaS) systems in that they tend to be able to 'spin down' to using no cloud compute resources when not in use, while also being able to 'spin up' to respond to requests very quickly (ideally in milliseconds).  These systems are commonly called 'serverless', which while being a complete misnomer (of course servers are involved!), does help convey the idea that in general you are free to squint and to not think about those servers too much.

While FaaS systems have become heavily adopted by many, the process of getting up and running with them can still feel overly complex compared to the ease at which they work at runtime.  Looking at AWS' FaaS offering [Lambda](https://aws.amazon.com/lambda/) (and the same applies for Azure), there is a distinct split between doing all the work to configure the Lambda runtime itself (i.e. how much memory to use, what environment variables should be present, etc.), versus how to write and maintain the code that will execute *in* the Lambda itself when triggered.  For AWS, the code itself needs to written and packaged up with all its dependencies into a single zip-file, stored as a blob that is then placed in [AWS S3](https://aws.amazon.com/s3/).  This blob is then referenced by Lambda so that it can be loaded on-demand when necessary.  Updating just a single character of this code then requires fully repackaging and reuploading everything.  Compounding all of that, this code is necessary independent of any other pieces of ones cloud-infrastructure.  If the code for the Lambda needs to read or write to an S3 bucket, it needs a good way to have that bucket's information passed to it.  Same with publishing to an [AWS Sns](https://aws.amazon.com/sns/) topic, or any other relevant resources needed.

At Pulumi, we thought there could be a better way to do this.  We already wanted to supply an easy way for developers to simply spin up their cloud infrastructure using languages and tooling they were already familiar with.  However, when it came to FaaS offerings, things still felt a bit too onerous at first.  While you could certainly create an AWS Lambda with code like `new aws.lambda.Function("myfunc")`, you would still have to do all the work external to your Pulumi application to define your code, its dependencies, a way to pass necessary information into it, as well as potentially needing to have build tasks running to keep this all up to date.  That's a lot of extra, out-of-band, effort.  Doubly-so since a Pulumi application is *already* code!  Why have to jump out of that code just to create another bit of code that you still running for your Cloud application?  From a desire to do better here, the "closure serialized function" was borne.  However, "closure serialized function" is pretty geeky sounding, so I like just calling them "magic functions".  Before diving more deeply into them, let's take a look at how they look in action (note: some of this example depends on  API changes that will be present in an upcoming release):

```ts
// Example simplified to not get too bogged down :)
import * as sharp from "sharp";

const videoBucket = new aws.s3.Bucket("videos");
const videoTopic = new cloud.Topic("videoTopic");

videoBucket.onObjectCreated("onNewVideo", async (event) => {
    for (const record of event.Records) {
        const dimensions = computeDimensions(record.s3.object.key);
        videoTopic.publish({ s3ObjectKey: record.s3.object.key, time: record.eventTime });
    }
});

function computeDimentions(objectKey: string): { height: number, width: number } { 
    /* simplified */ 
    const metadata = await sharp(...);
    return { height: metadata.height, width: metadata.width };
}

videoTopic.subscribe("compressVideo", async (event) => {
    const { s3ObjectKey, time } = event;

    // actually compress video.
});

videoTopic.subscribe("createThumbnail", async (event) => {
    const { s3ObjectKey, time } = event;

    // actually create thumbnail.
});
```

I've tried to make the example simple, but let's still walk through it to see what's happening.  First, we're just defining two simple resources.  An `S3 bucket`, where we expect new video files to be uploaded to, and a `cloud.Topic` that will inform interested parties when new videos are uploaded.  Right after defining the resources, we start creating our first FaaS resources.  The bucket resource has an event `onObjectCreated` that tells us when new objects appear.  The code asks to listen for those events, and then provides a *real*, JavaScript (or TypeScript) [arrow-function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) which defines the code that will execute in AWS Lambda in the cloud at *runtime*.  This code is pretty magical in a few ways.  To see how it's magice, let's consider a fairly naive way to create a Lambda from this Function. Specifically, by just taking the raw source text of this arrow-function (i.e. `toString`ing it) and using that as the text of the Lambda code.  i.e.:

```ts
// index.js

module.exports = async (event) => {
    foreach (var record in event.Records) {
        const dimensions = computeDimensions(record.s3.object.key);
        videoTopic.publish({ s3ObjectKey: record.s3.object.key, time: record.eventTime });
    }
};
```

 Now, the above translation could have worked for an extremely basic function, but totally breaks down here for several reasons.  First, 'computeDimensions' isn't included, which will make this immediately fail if ever called.  Second, if 'computeDimensions' was included, it wouldn't work unless the 'sharp' module was properly imported for it.  Third, even if the module was imported in the code, the actual npm package would have to be available along with the code in the cloud. Fourth, if that module was properly imported, and the package was properly included, the code is both referencing 'videoTopic' (a resource defined when the application originally ran), *and* it is invoking a helper method on it.  Remember, this code is going to be executing at cloud *runtime*, not at the time when Pulumi is actually executing the application on your developer machine, and actually doing things like running the `const videoTopic = new cloud.Topic("videoTopic")` code.  But, despite all those issues, Pulumi is able to make that original application code work and it is able to magically effectively translate the above into a working Lambda.  

So how does this all really work?  Well, if you want some of the more nitty gritty details, we have a [doc](https://github.com/pulumi/docs/blob/master/reference/serializing-functions.md) going in depth.  However, for now, we'll try to provide a high-level overview of what's going on.  Pulumi executes your application as a normal Nodejs application.  As such, when it hits the `const videoBucket = new aws.s3.Bucket("videos")` lines, it actually goes and creates those resources.  When it then hits the `videoBucket.onObjectCreated("onNewVideo", async (event) => {` line this executes a normal line of JavaScript.  Namely, onObjectCreated is a normal JavaScript function that will be passed the 'name' parameter as the first arg, and the JavaScript [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions) as the second arg.  [onObjectCreated](https://github.com/pulumi/pulumi-aws/blob/2159b44b296ab66ce4386d42b28fb22f27a6ef6a/sdk/nodejs/s3/s3Mixins.ts#L223) eventually bottoms out with a call to a call to [pulumi.runtime.serializeFunction](https://github.com/pulumi/pulumi/blob/fb18032a42eb34e9b5cbbe22a77a1b292d260a24/sdk/nodejs/runtime/closure/serializeClosure.ts#L89).  This function is the root of where our deep analysis of your JavaScript function analysis and translation will happen.  Using awesome analysis APIs (like those provided by [TypeScript](https://github.com/Microsoft/TypeScript)), we start introspecting the function instance, seeing what code it contains, and what external objects it references.  These objects include (but aren't limited) to things like simple JavaScript objects, other functions (like `computeDimensions`), modules (like `sharp`), other Pulumi resources (like `videoTopic`), and even complex beasts like [Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).  When Pulumi determines that these objects are referenced, it automatically includes enough information about them into the final translated Lambda code file so that they are available and can be effectively used at runtime.  Thanks to JavaScript's deep introspection capabilities, as well as its rich APIs for creating nearly anything at runtime, it's very possible to effectively 'dehydrate' out all the information present when Pulumi runs, and put it into a form that can be cheaply and accurately 'rehydrated' when the Lambda runs.  This analysis also understands the npm package structure of an application and its dependencies, ensuring that necessary imported packages are properly included with the final Lambda.  This analysis is also very smart about not including things that aren't necessary at all.  For example, it might drop information from being de/rehydrated if it can prove that would never be observable.  There are definite subtleties and interesting cases that can arise here, and for those very curious, reading the documentation linked above may be very enlightening.  

With this approach the work to create a Lambdas gets dramatically simpler.  Any sorts of changes to the code in the JavaScript function (including anything it depends on) is properly tracked and understood by Pulumi, allowing an easy development model where FaaS code can be easily modified and republished without any extra hoops to jump through.  On top of all of that, because this is just code itself, and because these are normal APIs, other tooling (like your editor) knows exactly what is going on and can guide you through this.  For example:

![image](https://user-images.githubusercontent.com/4564579/46366582-69847200-c649-11e8-8f97-6db5efadb978.png)

While there's a lot of really cool tech going on under the covers here, we really hope that this ends up just feeling super-awesome to use for you.  Now that we have this functionality, we wouldn't want to ever write an AWS Lambda any other way!
