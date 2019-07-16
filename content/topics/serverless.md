---
title: Serverless Programming with Pulumi
layout: serverless
url: /serverless

meta_desc: Pulumi provides a cloud native programming model for serverless applications. Any code, any cloud, any app.

hero:
    title: Serverless Programming with Pulumi
    body:
        Pulumi provides a cloud native programming model for serverless
        applications &mdash; from high-level multi-cloud, to fine-grained
        cloud-specific libraries.


        Any code, any cloud, any language.
    code: |
        // Create a serverless REST API
        import * as cloud from "@pulumi/cloud";

        let app = new cloud.API("my-app");
        app.static("/", "www");

        // Serve a simple REST API at `GET /hello`.
        app.get("/hello", (req, res) => res.json({ hello: "World!" }));

        export let url = app.publish().url;

sections:
    - id: what-is-serverless
      label: What is Serverless?
    - id: serverless-building-blocks
      label: Serverless Building Blocks
    - id: code
      label: Code
    - id: get-started
      label: Get Started
    - id: contact
      label: Contact Us

examples:
    - id: code-api
      title: Creating a Serverless REST API
      body: >
          This example shows how to create a simple REST API that counts the number of times a
          route has been hit. To implement this API, we need a DynamoDB table, an API endpoint,
          and a Lambda function.
      code: |
          const cloud = require("@pulumi/cloud-aws");

          // Create a mapping from 'route' to a count.
          let counterTable = new cloud.Table("counterTable", "route");

          // Create an API endpoint.
          let endpoint = new cloud.API("hello-world");

          endpoint.get("/{route+}", (req, res) => {
              let route = req.params["route"];
              console.log(`Getting count for '${route}'`);

              // Get previous value and increment
              // reference outer `counterTable` object.
              counterTable.get({ route }).then(value => {
                  let count = (value && value.count) || 0;
                  counterTable.insert({ route, count: ++count }).then(() => {
                      res.status(200).json({ route, count });
                      console.log(`Got count ${count} for '${route}'`);
                  });
              });
          });

          exports.endpoint = endpoint.publish().url;
      cta:
          url: /docs/quickstart
          label: GET STARTED

    - id: code-bucket
      title: Using storage buckets easily
      body: >
          Pulumi makes it easy to setup storage in the cloud. Events raised by the storage object can be handled by Lambda functions as actual lambdas in code.


          This example sets up a storage bucket (using S3 on AWS) and a simple Lambda function to respond to new items being added to the bucket.
      code: |
          const cloud = require("@pulumi/cloud-aws");

          // A storage bucket.
          const bucket = new cloud.Bucket("bucket");
          const bucketName = bucket.bucket.id;

          // Trigger a Lambda function when something is added.
          bucket.onPut("onNewVideo", bucketArgs => {
              console.log(`*** New Item in Bucket`);
          }

          // Export the bucket name.
          exports.bucketName = bucketName;
      cta:
          url: /docs/quickstart
          label: GET STARTED

    - id: code-table
      title: Stash info into a document database
      body: >
          This example uses a serverless timer that fetches the Hacker News homepage every hour and
          stashes it into a document database, making use of Pulumi's ability to reference the
          <code>cloud.table</code> object.
      code: |
          import * as cloud from "@pulumi/cloud";

          let snapshots = new cloud.Table("snapshots");

          cloud.timer.daily("daily-yc-snapshot",
              { hourUTC: 0, minuteUTC: 0 }, () => {
                  let req = require("https")
                      .get("https://news.ycombinator.com", (res) => {
                  let content = "";
                  res.setEncoding("utf8");
                  res.on("data", (chunk) => { content += chunk });
                  res.on("end", () => {
                      snapshots.insert({
                          date: Date.now(), content: content
                      });
                  });
              });
              req.end();
          });
      cta:
          url: /docs/quickstart
          label: GET STARTED

    - id: code-timer
      title: Super-simple serverless cron jobs
      body: >
          Pulumi’s Cloud Framework has a timer module that lets you schedule cron jobs that run
          serverless functions. This is the easiest way to get up and running with serverless
          functions, because you don’t even need any other resources to trigger events from.


          There are several ways to schedule a timer, depending on your stylistic preferences. These
          examples simply print the current time to the console on a given interval.
      code: |
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
      cta:
          url: /docs/quickstart
          label: GET STARTED

    - id: code-queue
      title: Post AWS SQS Messages to Slack
      body: >
          This example wires up a serverless AWS Lambda to an AWS SQS queue and demonstrates posting
          a message to Slack. This program provisions resources using Pulumi's deployment system,
          but lets you write serverless code as ordinary JavaScript functions.
      code: |
          let aws = require("@pulumi/aws");
          let serverless = require("@pulumi/aws-serverless");
          let config = require("./config");

          let queue = new aws.sqs.Queue("mySlackQueue", { visibilityTimeoutSeconds: 180 });

          serverless.queue.subscribe("mySlackPoster",
              queue, async (e) => {
              let slack = require("@slack/client");
              let client = new slack.WebClient(config.slackToken);
              for (let rec of e.Records) {
                  await client.chat.postMessage({
                      channel: config.slackChannel,
                      text: `*Msg ${rec.messageId}*:\n${rec.body}\n`+
                          `(with :love_letter: from Pulumi)`,
                      as_user: true,
                  });
                  console.log(`Posted SQS message ${rec.messageId} to ${config.slackChannel}`);
              }
          }, { batchSize: 1 });

          module.exports = {
              queueURL: queue.id,
          };
      cta:
          url: /docs/quickstart
          label: GET STARTED

    - id: code-topic
      title: Subscribe to an SNS endpoint
      body: >
          This example users a timer to trigger a notification which then recursively
          triggers itself to countdown from 25..0 every five minutes.
      code: |
          import * as pulumi from "@pulumi/cloud";

          let countDown = new pulumi.Topic("examples-countDown");

          countDown.subscribe("watcher", async (num) => {
              console.log(num);
              if (num > 0) {
                  await countDown.publish(num - 1);
              }
          });

          pulumi.timer.interval("examples-heartbeat", {minutes: 5}, async () => {
              await countDown.publish(25);
          });
      cta:
          url: /docs/quickstart
          label: GET STARTED

    - id: code-state-machine
      title: Create state machines of functions
      body: >
          This example shows a very simple state machine using AWS Step Functions. When
          executed the state machine steps will execute the 'Hello' and then 'World', steps
          in order before exiting.
      code: |
          import * as aws from "@pulumi/aws";
          import * as pulumi from "@pulumi/pulumi";

          const helloFunction = new aws.serverless.Function(
              "helloFunction",
              { role: lambdaRole },
              (event, context, callback) => {
                  callback(null, "Hello");
              }
          );

          const worldFunction = new aws.serverless.Function(
              "worldFunction",
              {role: lambdaRole},
              (event, context, callback) => {
                  callback(null, `${event} World!`);
              }
          );
      cta:
          url: /docs/quickstart
          label: GET STARTED
---
