---
title: "Creating an AWS CloudWatch Monitoring Service"
meta_desc: "Learn how to use Pulumi to define an AWS CloudWatch resource which can then be deployed to AWS and managed as infrastructure as code."
meta_image: "/images/docs/service/aws-cloudwatch.png"

service: "CloudWatch"
description: "is a monitoring service for AWS cloud resources and the applications you run on Amazon Web Services."
aws_here: "https://aws.amazon.com/cloudwatch/"

layout: aws-single
menu:
  aws:
    name: CloudWatch
---

## Create an AWS CloudWatch resource using `@pulumi/aws`

The `@pulumi/aws` library enables fine-grained control over the AWS CloudWatch resource meaning it can be coded, deployed, and managed entirely in code.

```javascript
const aws = require("@pulumi/aws");

const dashboard = new aws.cloudwatch.Dashboard("mydashboard", {
    dashboardName: "my-dashboard",
    dashboardBody: JSON.stringify({
        widgets: [
            {
                type: "metric",
                x: 0,
                y: 0,
                width: 12,
                height: 6,
                properties: {
                    metrics: [
                        [
                            "AWS/EC2",
                            "CPUUtilization",
                            "InstanceId",
                            "i-012345"
                        ]
                    ],
                    period: 300,
                    stat: "Average",
                    region: "us-east-1",
                    title: "EC2 Instance CPU"
                }
            },
            {
                type: "text",
                x: 0,
                y: 7,
                width: 3,
                height: 3,
                properties: {
                    markdown: "Hello world"
                }
            }
        ]
    })
});

const loginsTopic = new aws.sns.Topic("myloginstopic");

const eventRule = new aws.cloudwatch.EventRule("myeventrule", {
    eventPattern: JSON.stringify({
        "detail-type": [
            "AWS Console Sign In via CloudTrail"
        ]
    })
});

const eventTarget = new aws.cloudwatch.EventTarget("myeventtarget", {
    rule: eventRule.name,
    targetId: "SendToSNS",
    arn: loginsTopic.arn
})

const logGroup = new aws.cloudwatch.LogGroup("myloggroup");

const logMetricFilter = new aws.cloudwatch.LogMetricFilter("mylogmetricfilter", {
    pattern: "",
    logGroupName: logGroup.name,
    metricTransformation: {
        name: "EventCount",
        namespace: "YourNamespace",
        value: "1"
    }
});

const logStream = new aws.cloudwatch.LogStream("mylogstream", {
    logGroupName: logGroup.name
});

const metricAlarm = new aws.cloudwatch.MetricAlarm("mymetricalarm", {
    comparisonOperator: "GreaterThanOrEqualToThreshold",
    evaluationPeriods: 2,
    metricName: "CPUUtilization",
    namespace: "AWS/EC2",
    period: 120,
    statistic: "Average",
    threshold: 80,
    alarmDescription: "This metric monitors ec2 cpu utilization"
});
```
