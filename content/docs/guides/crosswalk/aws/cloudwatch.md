---
title_tag: "Using AWS CloudWatch | Crosswalk"
title: Using AWS CloudWatch
meta_desc: Pulumi Crosswalk for AWS CloudWatch help you operationally understand and manage your AWS CloudWatch metrics, resources and applications.
linktitle: CloudWatch
menu:
  userguides:
    parent: crosswalk-aws
    weight: 3

aliases: ["/docs/reference/crosswalk/aws/cloudwatch/"]
---

<a href="./">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) is a monitoring and management service built for developers,
system operators, site reliability engineers (SRE), and IT managers. AWS CloudWatch provides data and actionable insights
to monitor applications, understand and respond to system-wide performance changes, optimize resource utilization, and
get a unified view of operational health. AWS CloudWatch uses logs, metrics, and events to provide a
unified view of AWS resources, applications and services.

{{% notes type="info" %}}
This functionality is currently only available in TypeScript and as part of the AWSx Classic namespace.
{{% /notes %}}

## Overview

Pulumi Crosswalk for AWS CloudWatch will help you operationally understand and manage your AWS resources and applications,
including the following scenarios:

* [Configure logging](#configuring-cloudwatch-logging), for debugging and diagnosing problems after they have happened
* [Collect and track metrics](#subscribing-to-cloudwatch-metrics), which are variables you can measure, for health or
  performance
* [Create alarms](#creating-cloudwatch-alarms) to watch metrics and send notifications or automatically make changes
  when a threshold is breached
* [Define custom dashboards](#defining-cloudwatch-dashboards-in-code) to display these metrics or custom collections of
  metrics

For example, by setting up metrics to track the CPU usage and disk reads and writes of your Amazon EC2 instances,
you can create dashboards that report on health and set up alerts to notify you when you need to launch additional
instances to handle increased load. You can also use this same approach to stop under-used instances to save money.

Using Pulumi Crosswalk for AWS CloudWatch, you can more easily gain system-wide visibility into resource utilization,
application performance, and operational health.

## Configuring CloudWatch Logging

You can use Amazon CloudWatch Logs to monitor, store, and access your log files from Amazon Elastic Compute Cloud
(Amazon EC2) instances, AWS CloudTrail, Route 53, and other sources. CloudWatch Logs enables you to centralize the
logs from all of your systems, applications, and AWS services that you use, in a single, highly scalable service.
You can then easily view them, search them for specific error codes or patterns, filter them based on specific fields,
or archive them securely for future analysis. CloudWatch Logs enables you to see all of your logs, regardless of their
source, as a single and consistent flow of events ordered by time, and you can query them and sort them based on
other dimensions, group them by specific fields, and visualize log data in dashboards.

Pulumi Crosswalk for AWS supports configuring CloudWatch logging in the following ways:

* _Creating Log Groups_: A log group is a collection of logs with certain policies around retention and archival,
  to which logs may be sent from numerous AWS services. The
  [`aws.cloudwatch.LogGroup` class](/docs/reference/pkg/nodejs/pulumi/awsx/cloudwatch#LogGroup)
  may be used to create and configure new log groups.

* _Forwarding to Log Groups_: From any of the supported services, a CloudWatch log group may be supplied to configure
  said service to forward logs to that log group. Many services support doing so. For example,
  [ECS tasks and services](/docs/guides/crosswalk/aws/ecs/) offer a `logGroup` property that, when set, forwards all logs
  from your container instances.

* _Automatic Smart Defaults_: In many cases, using Pulumi Crosswalk for AWS uses smart defaults for whatever service
  you've chosen, so that automatic log groups and retention policies are used. So even if you do not specify a
  `logGroup` explicitly, logging is often happening on your behalf.

* _Viewing Log Group Outputs_: For any log groups in your Pulumi program, running the `pulumi logs` command line
  will aggregate and stream recent log entries to the console. The `--follow` option enables you to watch the
  logs unfold in real time, `--since` looks at log entries only within a certain time period, and `--resource` allows
  you to filter to specific log groups. Read more at
  [Unified Logs with Pulumi Logs](/blog/unified-logs-with-pulumi-logs/).

As an example, this code configures a custom CloudWatch log group with a 1 week retention policy for our ECS service:

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

const logGroup = new aws.cloudwatch.LogGroup("nginxLogs", {
    retentionInDays: 7,
});
const nginx = new awsx.ecs.FargateService("nginx", {
    taskDefinitionArgs: {
        logGroup, // use our custom LogGroup
        containers: {
            nginx: {
                image: "nginx",
                memory: 128,
            },
        },
    },
});
```

For details on all the capabilities of CloudWatch log groups, refer to the [Amazon CloudWatch Logs documentation](
https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html), in addition to the
[Pulumi CloudWatch API documentation](/docs/reference/pkg/nodejs/pulumi/awsx/cloudwatch/).

## Subscribing to CloudWatch Metrics

What are CloudWatch metrics? Metric resources are the fundamental monitoring unit in CloudWatch. A metric represents
a time-ordered set of data points that are published to CloudWatch. Think of a metric as a variable to monitor, and
the data points as representing the values of that variable over time. For example, the CPU usage of a particular EC2
instance is one metric provided by Amazon EC2. The data points themselves can come from any application or business activity
from which you collect data.

CloudWatch metrics in Pulumi Crosswalk for AWS are represented by an instance of the `awsx.cloudwatch.Metric` class.
To get such an instance, you can either [create one manually](#creating-a-metric-object), or, more commonly,
[use a pre-defined metric](#using-a-pre-defined-metric). From there, you can create
[alarms](#creating-cloudwatch-alarms) and [dashboards](#declaring-cloudwatch-dashboards-in-code).

AWS services send metrics to CloudWatch, and you can send your own custom metrics to CloudWatch. For these CloudWatch
custom metrics, you can add the data points in any order, and at any rate you choose. You can retrieve statistics about
those data points as an ordered set of time-series data.

CloudWatch Metrics exist only in the region in which they are created. Metrics cannot be deleted, but they automatically expire
after 15 months if no new data is published to them. Data points older than 15 months expire on a rolling basis; as
new data points come in, data older than 15 months is dropped.

CloudWatch Metrics are uniquely defined by a name, a namespace, and zero or more dimensions. Each data point in a metric has a
time stamp, and (optionally) a unit of measure. You can retrieve statistics from CloudWatch for any metric.

For more details on the concept of metrics, refer to the [CloudWatch Concepts documentation](
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Metric), and for additional
usage information refer to [Using Amazon CloudWatch Metrics](
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)

### Creating a Metric Object

To allocate a new `Metric` object, use its constructor, for instance:

```typescript
import * as awsx from "@pulumi/awsx";

// Create a lambda function (or use `aws.lambda.Function.get` to look up an existing one):
const func = new aws.lambda.CallbackFunction(...);

// Create a metric that tracks the duration of a Lambda's execution in seconds:
const funcMetric = new awsx.cloudwatch.Metric({
    namespace: "AWS/Lambda",
    name: "Duration",
    unit: "Seconds",
    function: func,
});
```

More commonly, applications will want to work with existing metrics produced by AWS services, using
[pre-defined metrics](#using-a-pre-defined-metric). In the event that you'd like to create a CloudWatch custom metric, or use a
service not already pre-defined, however, refer to the [API documentation for properties used when creating a new
`Metric` object](/docs/reference/pkg/nodejs/pulumi/awsx/cloudwatch#MetricArgs).

### Using a Pre-Defined Metric

Pre-defined metrics are exposed through the corresponding `awsx` module in a submodule called `metrics`. For example,
to access an AWS Lambda's metrics, we would use the `awsx.lambda.metrics` module. This module exposes numerous
functions, each corresponding to the metric in question. For example, this code uses `duration`:

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Create a lambda function (or use `aws.lambda.Function.get` to look up an existing one):
const func = new aws.lambda.CallbackFunction(...);

// Create a metric that tracks the duration of a Lambda's execution in seconds:
const funcMetric = awsx.lambda.metrics.duration({ function: func, unit: "Seconds" });
```

In this code, `funcMetric` represents information about how long each invocation of this function takes,
in seconds. Metrics sometimes relate to an entire service, or (like in the above example) will be tied to a specific
resource or subset of resources. When obtaining a metric, it's possible to specify the following:

1. The `period` of the metric. This specifies over what time period the data will be collected.
2. The `statistic` to be collected.  For example, the `Average`, or `Maximum` value of that metric over the period.
3. The `unit` the metric should be collected in. For example, `Megabytes/Second` for throughput.

Some metrics only support a subset of these properties, and not all values are legal for any given metric. For
example, some metrics may not support collecting the `Maximum` statistic. See the documentation below for the
event in question for information about what is available.

### Available CloudWatch Metrics for AWS Services

For details about all available CloudWatch Metrics in Pulumi Crosswalk for AWS, refer to the API documentation.
Here is a list of the AWS services that export metrics:

* [AWS Certificate Manager Private Certificate Authority (ACM PCA) CloudWatch Metrics](/docs/reference/pkg/nodejs/pulumi/awsx/acmpca#metrics)
* [AWS API Gateway CloudWatch Metrics](/docs/reference/pkg/nodejs/pulumi/awsx/apigateway#metrics)
* [AWS Autoscaling CloudWatch Metrics](/docs/reference/pkg/nodejs/pulumi/awsx/autoscaling#metrics)
* [AWS CloudFront CloudWatch Metrics](/docs/reference/pkg/nodejs/pulumi/awsx/cloudfront#metrics)
* [AWS CodeBuild CloudWatch Metrics](/docs/reference/pkg/nodejs/pulumi/awsx/codebuild#metrics)
* [AWS Cognito CloudWatch Metrics](/docs/reference/pkg/nodejs/pulumi/awsx/cognito#metrics)
* [AWS DynamoDB CloudWatch Metrics](/docs/reference/pkg/nodejs/pulumi/awsx/dynamodb#metrics)
* [AWS Elastic Block Store (EBS) CloudWatch Metrics](/docs/reference/pkg/nodejs/pulumi/awsx/ebs#metrics)
* [AWS Elastic Compute Cloud (EC2) CloudWatch Metrics](/docs/reference/pkg/nodejs/pulumi/awsx/ec2#metrics)
* [AWS Elastic Container Service (ECS) CloudWatch Metrics](/docs/reference/pkg/nodejs/pulumi/awsx/ecs#metrics)
* [AWS Elastic File System (EFS) CloudWatch Metrics](/docs/reference/pkg/nodejs/pulumi/awsx/efs#metrics)
* [AWS Elastic Load Balancing (ELB) CloudWatch Metrics](/docs/reference/pkg/nodejs/pulumi/awsx/lb#metrics)
* [AWS Lambda CloudWatch Metrics](/docs/reference/pkg/nodejs/pulumi/awsx/lambda#metrics)
* [AWS Relational Database Service (RDS) CloudWatch Metrics](/docs/reference/pkg/nodejs/pulumi/awsx/rds#metrics)
* [AWS Simple Storage Service (S3) CloudWatch Metrics](/docs/reference/pkg/nodejs/pulumi/awsx/s3#metrics)
* [AWS Simple Notification Service (SNS) CloudWatch Metrics](/docs/reference/pkg/nodejs/pulumi/awsx/sns#metrics)
* [AWS Simple Queue Service (SQS) CloudWatch Metrics](/docs/reference/pkg/nodejs/pulumi/awsx/sqs#metrics)

If certain metrics or services are missing from the list, refer to [AWS services that publish CloudWatch metrics](
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) for names
and namespaces, and then [use the `Metric` constructor directly](#creating-a-metric-object) to create an object.

## Creating CloudWatch Alarms

You can create a CloudWatch alarm that watches a single CloudWatch metric. An alarm can be in one
of three status: `OK` means the metric is within the defined threshold, `ALARM` means the metric is outside of the
defined threshold, or `INSUFFICIENT_DATA`, which means enough information has yet to be gathered which can
determine whether the metric is within or outside of the threshold range.

The alarm performs one or more actions based on the value of the metric or expression relative to a threshold over a
number of time periods. The action can be an Amazon EC2 action, an Amazon EC2 Auto Scaling action, or a notification
sent to an Amazon SNS topic, which can itself trigger an email, Lambda, or other custom actions.

You can also add alarms to CloudWatch dashboards and monitor them visually. When an alarm is on a dashboard, it turns
red when it is in the `ALARM` state, making it easier for you to monitor its status proactively.

Alarms invoke actions for sustained state changes only. CloudWatch alarms do not invoke actions because they are
in a particular state, the state must have changed and been maintained for a specified number of periods.

After an alarm invokes an action due to a change in state, its subsequent behavior depends on the type of action that
you have associated with the alarm. For Amazon EC2 Auto Scaling actions, the alarm continues to invoke the action for
every period that the alarm remains in the new state. For Amazon SNS notifications, no additional actions are invoked.

When creating an alarm, the following properties can be specified:

* `threshold`: The value to compare the metric value against.
* `comparisonOperator`: The type of comparison that should be made between the metric value and the threshold value.
  Legal values include `"GreaterThanOrEqualToThreshold"`, `"GreaterThanThreshold"`, `"LessThanThreshold"`, and
  `"GreaterThanOrEqualToThreshold"`. The default is `"GreaterThanOrEqualToThreshold"`.
* `evaluationPeriods`: The number of periods over which data is compared to the specified threshold.

To create an alarm from a metric object, call its `createAlarm` function:

```typescript
// Create a metric that measures invocation duration using a period of 300 seconds (5 minutes).
const func = new aws.lambda.CallbackFunction(...);
const funcMetric = awsx.lambda.metrics.duration({ function: func, period: 300, unit: "Seconds" });

// Now create an alarm that triggers if, over two periods (10 minutes), the invocation duration
// is greater than or equal to 120 seconds (2 minutes).
const alarm = funcMetric.createAlarm("alarm", {
    threshold: 120,
    evaluationPeriods: 2,
});
```

An alarm on its own doesn't do much. We need to specify one or more `alarmActions` which is one or more ARNs to
trigger when the metric transitions into the `ALARM` state. For example, this configures an SNS topic:

```typescript
// Create an SNS topic and configure the alarm to publish to it when triggered.
const alarmTopic = new aws.sns.Topic(...);
const alarm = funcMetric.createAlarm("alarm", {
    threshold: 120,
    evaluationPeriods: 2,
    alarmActions: [ alarmTopic ],
});
```

Such an approach can be combined with [Pulumi Crosswalk for AWS Lambda](/docs/guides/crosswalk/aws/lambda/) to define and run
custom code in response to metric alarms being triggered.

CloudWatch metrics may also be used to trigger changes to [Autoscaling Scaling Policies](/docs/guides/crosswalk/aws/autoscaling#scaling-policies) in response to events indicating that more or less capacity is desired.

## Defining CloudWatch Dashboards in Code

Amazon CloudWatch dashboards are customizable home pages in the CloudWatch console that you can use to monitor your
resources in a single view, even resources that are spread across different regions. You can use AWS CloudWatch dashboards
to create customized views of the metrics and alarms for your AWS resources.

With dashboards, you can create the following:

* A single view for selected metrics and alarms to help you assess the health of your resources and applications
  across one or more regions. You can select the color used for each metric on each graph, so that you can easily
  track the same metric across multiple graphs.
* An operational playbook that provides guidance for team members during operational events about how to respond
  to specific incidents.
* A common view of critical resource and application measurements that can be shared by team members for faster
  communication flow during operational events.

Using Pulumi Crosswalk for AWS CloudWatch you can define these dashboards in code. By doing so, it is easy to
manage and evolve the dashboards in a repeatable way, and it becomes much easier to provision dashboards for new
environments as they come online using Pulumi's standard support for stacks and configuration.

### Declaring Dashboard Layout Using Widgets

Dashboards are created from Widgets that are then automatically placed on a 24 unit wide, infinitely tall grid, based
on flow constraints. When creating widgets, a desired Width-x-Height cab be supplied (otherwise a default size of
6x6 is used). Widgets can then be related to other widgets by either placing them in a [Column](
/docs/reference/pkg/nodejs/pulumi/awsx/cloudwatch#ColumnWidget) or in a [Row](
/docs/reference/pkg/nodejs/pulumi/awsx/cloudwatch#RowWidget). Widgets placed in a column can flow vertically as far as
necessary. Widgets placed in a row will wrap automatically after 24 grid spaces.

#### Adding Text to a Dashboard

You can place a simple piece of text on the dashboard using a [Text Widget](
/docs/reference/pkg/nodejs/pulumi/awsx/cloudwatch#TextWidget). These can contain markdown and will be rendered by the
dashboard in the requested location and size.

#### Adding Spacing to a Dashboard

The [Space Widget](
/docs/reference/pkg/nodejs/pulumi/awsx/cloudwatch#SpaceWidget) acts as a simple mechanism to place a gap (with a desired
Width-x-Height) in between other widgets.

#### Adding Metrics to a Dashboard

The most common widgets that will be added to a Dashboard are metric widgets, i.e. widgets that display the latest
reported values of some metric. These metrics can be shown on the dashboard as either a [line graph](
/docs/reference/pkg/nodejs/pulumi/awsx/cloudwatch#LineGraphMetricWidget), [stacked area graph](
/docs/reference/pkg/nodejs/pulumi/awsx/cloudwatch#StackedAreaGraphMetricWidget), or as a [single number](
/docs/reference/pkg/nodejs/pulumi/awsx/cloudwatch#SingleNumberMetricWidget).

Creating a metric widget on your dashboard can be done like so:

```typescript
import * as aws from "@pulumi/aws";
import * as classic from "@pulumi/awsx/classic";

// Get the metric for the lambda that processing our topic requests.
const funcMetric = classic.lambda.metrics.duration({ function: func });

// Also create a dashboard to track two things:
//     1) Average requests/minute.
//     2) P90/95/99 latency durations.
const dashboardName = "funcDashboard";
const dashboard = new classic.cloudwatch.Dashboard(dashboardName, {
    widgets: [
        new classic.cloudwatch.SingleNumberMetricWidget({
            title: "Requests/Minute",
            width: 10,
            metrics: awsx.lambda.metrics.invocations({
                function: func,
                unit: "Count",
                statistic: "Average",
                period: 60,
            }),
        }),
        new classic.cloudwatch.LineGraphMetricWidget({
            title: "Lambda duration",
            width: 14,

            // Log our different p90/p95/p99 latencies
            metrics: [
                funcMetric.with({ extendedStatistic: 90, label: "Duration p90" }),
                funcMetric.with({ extendedStatistic: 95, label: "Duration p95" }),
                funcMetric.with({ extendedStatistic: 99, label: "Duration p99" }),
            ],
        }),
    ],
});

export const dashboardUrl =
    `https://${aws.config.region}.console.aws.amazon.com/cloudwatch/home?` +
        `region=${aws.config.region}#dashboards:name=${dashboardName}`;
```

After deploying this with `pulumi up`, the dashboard's URL will be printed, at which the dashboard is available.

Graph widgets can also have a line on them showing the breaching threshold for a specific alarm using `annotations`.
This can be done like so:

```typescript
// Create an alarm if this lambda takes more than 1000ms to complete in a period of 10 minutes over
// at least five periods in a row.
const funcAlarm1 = funcMetric.with({ unit: "Milliseconds", period: 600 })
                             .createAlarm("SlowUrlProcessing", { threshold: 1000, evaluationPeriods: 5 });

// Also create a dashboard to track this.
const dashboard = new classic.cloudwatch.Dashboard("TopicData", {
    widgets: [
        ...,
        new classic.cloudwatch.LineGraphMetricWidget({
            title: "Lambda duration",
            width: 14,

            // Place a line on the graph to indicate where our alarm will be triggered.
            annotations: new classic.cloudwatch.HorizontalAnnotation(funcAlarm1),

            // Log our different p90/p95/p99 latencies
            metrics: [
                funcMetric.with({ extendedStatistic: 90, label: "Duration p90" }),
                funcMetric.with({ extendedStatistic: 95, label: "Duration p95" }),
                funcMetric.with({ extendedStatistic: 99, label: "Duration p99" }),
            ],
        }),
    ],
});
```

More complex widget customization is possible. See the individual types and arguments in the
[Cloudwatch API](/docs/reference/pkg/nodejs/pulumi/awsx/cloudwatch/) for more details.

## Additional AWS CloudWatch Resources

For more information about Amazon CloudWatch, see the following:

* [Amazon CloudWatch homepage](https://aws.amazon.com/cloudwatch/)

Or [get started with Pulumi](/docs/get-started/aws/).
