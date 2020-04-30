---
title: "Provisioning and Managing Cloud Infrastructure with Pulumi"
authors: ["donna-malayeri"]
tags: ["JavaScript","AWS","Infrastructure"]
date: "2018-07-20"
meta_desc: "Use Pulumi AWS, Azure, and GCP libraries to provision and manage infrastructure. Configure alerting & monitoring directly in code using Pulumi."

---

If you've been following the blog, you know that Pulumi is great for
building [serverless applications]({{< prelref "code-deploy-and-manage-a-serverless-rest-api-on-aws-with-pulumi" >}}),
[container-based applications]({{< prelref "deploying-production-ready-containers-with-pulumi" >}}),
and a [combination of the two]({{< prelref "build-a-video-thumbnailer-with-pulumi-using-lambdas-containers-and-infrastructure-on-aws" >}}).
But, did you know that you can manage any cloud resource in AWS, Azure, or Google Cloud Platform?
<!--more-->

You can use the
[AWS]({{< prelref "/docs/reference/pkg/aws" >}}),
[Azure]({{< prelref "/docs/reference/pkg/azure" >}}),
or [Google Cloud]({{< prelref "/docs/reference/pkg/gcp" >}})
libraries to manage cloud resources. Using these libraries, you can
directly manage the properties of any cloud resource.

For example, in just a few lines of code, you can provision a security
group and an EC2 instance:

    let group = new aws.ec2.SecurityGroup("web-secgrp", {
        ingress: [
            { protocol: "tcp", fromPort: 22, toPort: 22, cidrBlocks: ["0.0.0.0/0"] },
        ],
    });

    let server = new aws.ec2.Instance("web-server-www", {
        instanceType: "t2.micro",
        securityGroups: [ group.name ],   // reference the group object above
        ami: "ami-7172b611",
    });

Next, let's add a a CloudWatch metric alarm that is triggered when when
the CPU utilization is over 80%:

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

In addition to alerting, you may want to provision a [CloudWatch dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)
to have a single monitoring view for all your application resources. You
can define this dashboard directly in code using Pulumi. The following
code defines a dashboard and specifies the widgets to include:

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
              }
          ]
        })
    });

Perhaps you want to post to an SNS topic whenever a user signs in to the
AWS console for your production account. This requires provisioning
three resources: the SNS topic, a CloudWatch event rule, and a
CloudWatch event target. With Pulumi, this can all be specified with
just a few lines of JavaScript:

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

These are just a few examples of the AWS resources you can manage in
Pulumi. You can provision
[Athena databases]({{< prelref "/docs/reference/pkg/aws/athena" >}}),
[DynamoDB tables]({{< prelref "/docs/reference/pkg/aws/dynamodb" >}}),
[IAM users, roles, groups, and role policies]({{< prelref "/docs/reference/pkg/aws/iam" >}}),
[Kinesis streams]({{< prelref "/docs/reference/pkg/aws/kinesis" >}}), and more.

To learn more, take a look at the
[AWS API documentation]({{< prelref "/docs/reference/pkg/aws" >}})
and the [sample code that provisions a variety of infrastructure resources](https://github.com/pulumi/examples/blob/master/aws-ts-resources/index.ts).
