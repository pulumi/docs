---
title: "How to create an AWS Cloudwatch monitoring service with Pulumi"
cloud: "AWS"
service: "Cloudwatch"
description: "is a monitoring service for AWS cloud resources and the applications you run on Amazon Web Services."
library: "@pulumi/aws"
brand: "aws"
og:
    description: "Use Pulumi to code, deploy, and manage cloud, serverless, and container apps and infrastructure"
    image: "/images/service/aws-cloudwatch.png"
---
<!-- Links -->
[AWS here]: https://aws.amazon.com/cloudwatch/
[Reference docs]: ../reference/aws.html
[Github @pulumi/aws]: https://github.com/pulumi/pulumi-aws 
[Configure AWS]: ../install/aws.html

This reference shows how to use Pulumi to define an {{ page.cloud }} {{ page.service }} resource using pure code which can then be deployed to {{ page.cloud }} and managed as infrastructure as code.

<div class="row">
<div class="col-md-9" markdown="1">

## What is {{ page.cloud }} {{ page.service }}?

<img class="how-to-logo" src="../images/brand/{{ page.brand }}.png" alt="{{ page.brand }}" width="100">

{{ page.cloud }} {{ page.service }} {{ page.description }}. Find out more at [AWS here].

</div>
<div class="col-md-3 find-out-more" markdown="1">

### Find out more

* [Reference docs]
* [GitHub @pulumi/aws]
* [Configure AWS]

</div>
</div>



## Create an {{ page.cloud }} {{ page.service }} resource using `{{ page.library }}`

The `{{ page.library }}` library enables fine-grained control over the {{ page.cloud }} {{ page.service }} resource meaning it can be coded, deployed, and managed entirely in code. 

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