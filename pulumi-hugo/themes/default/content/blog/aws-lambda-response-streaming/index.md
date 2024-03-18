---
title: "AWS Lambda Response Streaming with Pulumi"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2023-04-06

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
# Max length is 160 characters.
meta_desc: Pulumi support for the newly announced Lambda Response Streaming from AWS 

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
    - isaac-harris
    - josh-kodroff

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - aws
    - lambda

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
---

Since its introduction in 2014, AWS Lambda has rapidly expanded its capabilities from simple “functions in the cloud” at launch to a comprehensive serverless platform with [support for containerized functions](https://www.pulumi.com/blog/aws-lambda-container-support/) and [public per-function URL endpoints](https://www.pulumi.com/blog/lambda-urls-launch/).

As serverless applications have increased in sophistication, developers have used functions-as-a-service as a first-class tool in their microservices strategy. As organizations increasingly look to break up their monolithic applications into services, adoption of AWS Lambda has not been a viable option for applications that return payloads larger than the 6 MiB Lambda service limit. In addition to the payload response limit, AWS Lambda has been limited to returning the entire response once it has been fully buffered in memory within the Lambda service. This historical limitation meant that end users would not see *any* response until the *entire* response was available. Both of these limitations made Lambda difficult or impossible to use for data-intensive or latency-sensitive use cases.

## Introducing Response Streaming

Today, AWS announced [Lambda Response Streaming](https://aws.amazon.com/blogs/compute/introducing-aws-lambda-response-streaming/): a new feature that enables response payloads beyond the 6MiB limit, supports binary content in responses and reduces response times for latency-sensitive applications. Response Streaming reduces the time to first byte (TTFB) by enabling your functions to send partial responses to the client as soon as they are ready instead of waiting for a fully-generated and buffered response. This reduces multi-second TTFB to milliseconds, and, you can stream payloads that are gigabytes in size with a soft 20MiB limit for streamed payloads. The maximum throughput for a streamed response is 2MiB/s.

Enabling Response Streaming requires a new Lambda function handler signature that provides a stream object that the function can write to. When your function writes data to this stream, it is sent immediately to the client. To help clients understand the contents of the stream, you can optionally set the Content-Type header for a response.

This feature supports NodeJS v14.x, v16.x and v18.x at launch and comes with an updated billing model that charges for bytes processed and streamed from your Lambda Function.

## Authoring a Lambda Function for Response Streaming

For an example of how response streaming works in practice, we’ve built a Lambda function that will stream the [Gettysburg Address](https://en.wikipedia.org/wiki/Gettysburg_Address) one sentence at a time with a one second pause between sentences. For brevity, each sentence is abbreviated below (but the code in GitHub, which demonstrates the same function with and without streaming, contains the full text of the speech):

```javascript
const handleInternal = async (_event, responseStream, _context) => {
 responseStream.setContentType("text/plain");

 const sentences = [
   "Fourscore and seven years ago...",
   "Now we are engaged in a great civil war...",
   "We have come to dedicate...",
   "It is altogether fitting...",
   "But, in a larger sense...",
   "The brave men...",
   "The world will little note...",
   "It is for us the living...",
 ]

 const timer = ms => new Promise( res => setTimeout(res, ms));

 for(let i = 0; i < sentences.length; i++) {
   responseStream.write(`${sentences[i]}\n`);
   await timer(1000);
 }

 responseStream.end();
}

exports.handler = awslambda.streamifyResponse(handleInternal);
```

The notable changes to the Lambda function code that support response streaming are:

- The function must be wrapped in the `awslambda.streamifyResponse()` middleware. (The `streamifyResponse()` function is defined in the Node runtime that’s supplied by the Lambda service.)
- Handler methods require an additional parameter to the usual `(event, context)` signature to become `(event, responseStream, context)`.
- The `responseStream` parameter implements Node’s [Writable](https://nodejs.org/docs/latest-v14.x/api/stream.html#stream_writable_streams) interface to give it a familiar API with other streams that Node developers may be familiar with.
- Responses to the client must be written via `responseStream.write()`, the method that writes to the stream.
- The function must call `responseStream.end()` to signal that no more data is expected.
- Note that functions authored for streaming can still be seamlessly invoked with buffered responses.

## Streaming Performance Considerations

For this simple text-based example, there is little need to worry about overall performance. However, if the response is large or the client is expected to perform a lot of processing on the response data, AWS suggests using Node’s `pipeline()` in place of the built-in `write()` method in case data is produced faster than it can be consumed by the client. `pipeline()` effectively helps you to pipe between streams, forward errors and properly clean up – providing a callback when the pipeline is complete. You can learn more about this approach in [Backpressuring in streams](https://nodejs.org/en/learn/modules/backpressuring-in-streams) in the Node docs.

## Packaging and deploying your Lambda Function for streaming with Pulumi

We can package our Lambda function for streaming with just a few dozen lines of code using Pulumi. First, we’ll need to import some libraries that will allow us to package our Lambda and create the necessary resources in AWS. For this exercise, we’ll be using both the [AWS Native](https://www.pulumi.com/registry/packages/aws-native/) provider and the [AWS Classic](https://www.pulumi.com/registry/packages/aws/) provider. The AWS Native provider works with the [AWS Cloud Control API](https://aws.amazon.com/cloudcontrolapi/) to enable same-day support for new AWS features like Lambda response streaming.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsNative from "@pulumi/aws-native";
```

Next, we’ll create an IAM role for our Lambda function to assume that has the standard required permissions for a Lambda function:

```typescript
const role = new aws.iam.Role("role", {
 assumeRolePolicy: JSON.stringify({
   "Version": "2012-10-17",
   "Statement": [{
     "Effect": "Allow",
     "Principal": {
       "Service": "lambda.amazonaws.com",
     },
     "Action": "sts:AssumeRole",
   }],
 }),
});

new aws.iam.RolePolicyAttachment("role-policy-attachment", {
 role: role.name,
 policyArn: "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
});
```

Streamed responses are not currently supported with API Gateway nor with Application Load Balancers, so they must be invoked via [Lambda Function URLs](https://www.pulumi.com/blog/lambda-urls-launch/) or invoked and streamed through the InvokeWithResponseStream API using the AWS SDK. Let’s create our function, add a function URL, and the necessary permissions to allow unauthenticated access to the function URL. Note that we set the `invokeMode` input of the function URL to `RESPONSE_STREAM`. This is what allows us to invoke the function with streaming enabled:

```typescript
const streamingFunc = new aws.lambda.Function("streaming-func", {
 code: new pulumi.asset.FileArchive("../../lambda"),
 role: role.arn,
 handler: "index.handler",
 runtime: "nodejs14.x",
 timeout: 30,
});

new aws.lambda.Permission("streaming-permission", {
 action: "lambda:InvokeFunctionUrl",
 "function": streamingFunc.arn,
 principal: "*",
 functionUrlAuthType: "NONE",
});

const streamingUrl = new awsNative.lambda.Url("streaming-url", {
 authType: "NONE",
 targetFunctionArn: streamingFunc.arn,
 invokeMode: "RESPONSE_STREAM",
});
```

Finally, we’ll add a [stack export](https://www.pulumi.com/learn/building-with-pulumi/stack-outputs/) so we can access the generated function URL from outside of our Pulumi program:

```typescript
exports.streamingUrl = streamingUrl.functionUrl;
```

To deploy our resources, we run `pulumi up -y`:

```bash
$ pulumi up -y
Previewing update (dev)

View Live: https://app.pulumi.com/jkodrofftest/aws-lambda-streaming/dev/previews/d2e04257-222e-4704-b163-98e6bf4ff704

 	Type                         	Name                  	Plan   	Info
 +   pulumi:pulumi:Stack          	aws-lambda-streaming-dev  create
 +   ├─ aws:iam:Role              	role                  	create
 +   ├─ aws:iam:RolePolicyAttachment  role-policy-attachment	create
 +   ├─ aws:lambda:Function       	streaming-func        	create
 +   ├─ aws:lambda:Permission     	streaming-permission  	create
 +   └─ aws-native:lambda:Url     	streaming-url         	create


Outputs:
	streamingUrl: output<string>


Updating (dev)

View Live: https://app.pulumi.com/jkodrofftest/aws-lambda-streaming/dev/updates/25

 	Type                         	Name                  	Status          	Info
 +   pulumi:pulumi:Stack          	aws-lambda-streaming-dev  creating (43s)...
 +   ├─ aws:iam:Role              	role                  	created (1s)
 +   ├─ aws:iam:RolePolicyAttachment  role-policy-attachment	created (0.33s)
 +   ├─ aws:lambda:Function       	streaming-func        	created (22s)
 +   ├─ aws-native:lambda:Url     	streaming-url         	created (2s)
 +   └─ aws:lambda:Permission     	streaming-permission  	created (0.58s)

Outputs:
	streamingUrl: "https://s5a3pi4zzsufh5cgaigdxq3wva0psaib.lambda-url.eu-west-1.on.aws/"

Resources:
	+ 6 created

Duration: 46s
```

## Reading a Response Stream

Now that we’ve deployed our streaming function, we can read a response stream from the deployed Lambda URL. Per AWS, we can use any client that supports HTTP/1.1 chunked transfer coding. In cURL, streamed responses can be read via the `-N` flag. We can also add output that displays our time to connect, time to first byte (TTFB), and the total time to return the response:

```bash
curl -N -w "Connect: %{time_connect} TTFB: %{time_starttransfer} Total time: %{time_total} \n" $(pulumi stack output streamingUrl)
```

When successful, your output will look like this:

[![asciicast](https://asciinema.org/a/Y6qAqgGD923jX2wzwzc4xPKzf.svg)](https://asciinema.org/a/Y6qAqgGD923jX2wzwzc4xPKzf)

This example visually shows the advantage of response streaming because the first message appears shortly (approximately 1 second) after invocation. If we disable streaming, the fully buffered response takes several seconds to arrive. You can [see the buffered response example in action](https://asciinema.org/a/90rcXiCllJuydwJDmX4QM5Y7z). This is precisely why TFFB is important: it’s the difference between an app or service that appears to hang while awaiting a response and one that feels much more responsive to an end user.

## Wrapping up

AWS Lambda Response Streaming continues the Lambda team’s steady drumbeat of innovation that adds new capabilities and use cases to serverless functions. Grab [the sample code](https://github.com/pulumi/blog-lambda-streaming-response) and give the feature a try. Then, let us know what you think in the Pulumi [Community Slack](https://slack.pulumi.com).
