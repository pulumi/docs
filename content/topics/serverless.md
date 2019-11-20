---
title: Serverless Programming with Pulumi
layout: serverless
url: /serverless

meta_desc:
    Pulumi makes serverless applications easy by letting you focus on business logic and managing
    infrastructure in the same familiar language you're already writing your code in.

hero:
    title: Serverless In Just a Few Lines of Code
    body:
        Pulumi makes serverless applications easy by letting you focus on business logic and managing
        infrastructure in the same familiar language you're already writing your code in.


        Any code, any cloud, any language.
    code: |
        // Create a serverless REST API
        import * as awsx from "@pulumi/awsx";

        // Serve a simple REST API at `GET /hello`.
        let app = new awsx.apigateway.API("my-app", {
            routes: [{
                path: "/hello",
                method: "GET",
                eventHandler: async (event) => {
                    return {
                        statusCode: 200,
                        body: JSON.stringify({ hello: "World!" }),
                    };
                },
            }],
        });

        export let url = app.url;

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
          import * as aws from "@pulumi/aws";
          import * as awsx from "@pulumi/awsx";

          // Create a mapping from 'route' to a count.
          let counterTable = new aws.dynamodb.Table("counterTable", {
              attributes: [{ name: "id", type: "S" }],
              hashKey: "id",
              readCapacity: 5,
              writeCapacity: 5,
          });

          // Create an API endpoint.
          let endpoint = new awsx.apigateway.API("hello-world", {
              routes: [{
                  path: "/{route+}",
                  method: "GET",
                  eventHandler: (req, res) => {
                      let route = event.pathParameters!["route"];
                      let client = new aws.sdk.DynamoDB.DocumentClient();

                      // Get previous value and increment our table entry.
                      let tableData = await client.get({
                          TableName: counterTable.name.get(),
                          Key: { id: route },
                          ConsistentRead: true,
                      }).promise();

                      let value = tableData.Item;
                      let count = (value && value.count) || 0;
                      await client.put({
                          TableName: counterTable.name.get(),
                          Item: { id: route, count: ++count },
                      }).promise();

                      return {
                          statusCode: 200,
                          body: JSON.stringify({ route, count }),
                      };
                  },
              }],
          });

          exports.endpoint = endpoint.url;
      cta:
          url: /docs/get-started/
          label: GET STARTED

    - id: code-bucket
      title: Using storage buckets easily
      body: >
          Pulumi makes it easy to setup storage in the cloud. Events raised by the storage object can be handled by Lambda functions as actual lambdas in code.


          This example sets up a storage bucket (using S3 on AWS) and a simple Lambda function to respond to new items being added to the bucket.
      code: |
          const aws = require("@pulumi/aws");

          // A storage bucket.
          const videos = new aws.s3.Bucket("bucket");

          // Trigger a Lambda function when something is added.
          videos.onPut("onNewVideo", bucketArgs => {
              console.log(`*** New Item in Bucket`);
          }

          // Export the bucket name.
          exports.bucketName = videos.bucket;
      cta:
          url: /docs/get-started/
          label: GET STARTED

    - id: code-table
      title: Stash info into a document database
      body: >
          This example uses a serverless timer that fetches the Hacker News homepage every day at 8:30AM and
          stashes it into a document database, making use of Pulumi's ability to reference resources
          by capturing them inside of serverless lambdas.
      code: |
          const aws = require("@pulumi/aws");

          const snapshots = new aws.dynamodb.Table("snapshots", {
              attributes: [{ name: "id", type: "S", }],
              hashKey: "id", billingMode: "PAY_PER_REQUEST",
          });

          aws.cloudwatch.onSchedule("daily-yc-snapshot", "cron(30 8 * * ? *)", () => {
              require("https").get("https://news.ycombinator.com", res => {
                  let content = "";
                  res.setEncoding("utf8");
                  res.on("data", chunk => content += chunk);
                  res.on("end", () => new aws.sdk.DynamoDB.DocumentClient().put({
                      TableName: snapshots.name.get(),
                      Item: { date: Date.now(), content },
                  }).promise());
              }).end();
          });
      cta:
          url: /docs/get-started/
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
          import * as aws from "@pulumi/aws";

          // Run a timer every minute:
          aws.cloudwatch.onSchedule("everyMinute", "rate(1 minute)", async (event) => {
              console.log(`everyMinute: ${Date.now()}`);
          });

          // Run a timer every minute (cron-style expression):
          aws.cloudwatch.onSchedule("everyMinuteCron", "cron(0 * * * * *)", async (event) => {
              console.log(`everyMinuteCron: ${Date.now()}`);
          });

          // Run a timer every day at 7:30 UTC:
          aws.cloudwatch.onSchedule("everyDay730", "cron(30 7 * * ? *)", async (event) => {
              console.log(`everyDay730: ${Date.now()}`);
          });
      cta:
          url: /docs/get-started/
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
          url: /docs/get-started/
          label: GET STARTED

    - id: code-topic
      title: Subscribe to an SNS endpoint
      body: >
          This example uses an SNS topic to hold a list of website URLs to crawl,
          and does so everytime a new message arrives.
      code: |
          import * as aws from "@pulumi/aws";
          import * as fetch from "node-fetch";

          const topic = new aws.sns.Topic("sites-to-process-topic");
          topic.onEvent("for-each-url", async (event) => {
              const records = event.Records || [];
              for (const record of records) {
                  // Fetch the contents at the URL
                  const url = record.Sns.Message;
                  console.log(`${url}: Getting`);
                  try {
                      const res = await fetch.default(url);
                  } catch (err) {
                      console.log(`${url}: Failed to GET`);
                      return;
                  }
              }
          });
      cta:
          url: /docs/get-started/
          label: GET STARTED

contact_us_form:
    section_id: contact
    hubspot_form_id: c086198d-0e76-4ec3-9304-7f2c60788447
    headline: Need help with container management?
    quote:
        title: Lean how top engineering teams are using Pulumi to simplify their 'Serverless' applications.
        name: Josh Imhoff
        name_title: Site Reliability Engineer, Cockroach Labs
        content: |
            We are building a distributed-database-as-a-service product that runs on Kubernetes clusters across
            multiple public clouds including GCP, AWS and others. Pulumi's declarative model, the support for real
            programming languages, and the uniform workflow on any cloud make our SRE team much more efficient.
---
