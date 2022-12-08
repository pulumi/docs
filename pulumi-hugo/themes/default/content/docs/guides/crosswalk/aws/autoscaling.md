---
title_tag: "Configuring AWS Auto Scaling | Crosswalk"
title: Configuring AWS Auto Scaling
meta_desc: Pulumi Crosswalk for AWS allows you to easily to define Auto Scaling Groups (ASGs) to configure scaling of EC2
           instances.
linktitle: Auto Scaling
menu:
  userguides:
    parent: crosswalk-aws
    weight: 2

aliases: ["/docs/reference/crosswalk/aws/autoscaling/"]
---

<a href="./">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[AWS Auto Scaling](https://aws.amazon.com/autoscaling) monitors your applications and automatically adjusts capacity to
maintain steady, predictable performance at the lowest possible cost. Using AWS Auto Scaling, it’s easy to setup
application scaling for multiple resources across multiple services in minutes. AWS Auto Scaling can be used to build
scaling plans for resources including Amazon EC2 instances and Spot Fleets, and Amazon ECS clusters and tasks. With AWS
Auto Scaling, your applications always have the right resources at the right time, and you pay only for the AWS
resources needed to run your applications and any associated Amazon CloudWatch monitoring fees.

{{% notes type="info" %}}
This functionality is currently only available in TypeScript and as part of the AWSx Classic namespace.
{{% /notes %}}

## Overview

Pulumi Crosswalk for AWS enables easy definition of Auto Scaling Groups (ASGs) to configure scaling of EC2
instances, for either VM or container workloads using ECS. Using this, combined with [Pulumi Crosswalk for AWS's support for Amazon CloudWatch](/docs/guides/crosswalk/aws/cloudwatch),
you can create powerful scaling policies that
meet your performance and scaling needs, while also maximizing cost effectiveness.

## Creating and Configuring Auto Scaling Groups

An [EC2 Auto Scaling Group (ASG)](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html) contains
a collection of Amazon EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and
management. An ASG also enables you to use Amazon EC2 Auto Scaling features such as health check replacements and
scaling policies. Both maintaining the number of instances in an ASG and automatic scaling are the core functionality
of the Amazon EC2 Auto Scaling service.

The size of an ASG depends on the number of instances you set as the desired capacity. You can adjust its size to meet
demand, either manually or by using automatic scaling, by defining constraints on the minimum, maximum and desired
number of instances that should be running. ASGs can also specify
[Scaling Schedules](#automatically-scaling-based-on-a-schedule) that control changing these desired values (for example,
to scale up on certain days with high expected load), as well as specifying
[Dynamic Scaling Policies](#dynamically-scaling-based-on-metrics-and-policies) that will adjust how the group scales in
response to events happening in the system.

### Creating Your Auto Scaling Group

To create an ASG, allocate an instance of `awsx.classic.autoscaling.AutoScalingGroup`. The constructor accepts properties
to control the network (`vpc` and `subnetIds`), scaling policies (`templateParameters`), EC2 instance properties
(`launchConfiguration`), and more.

This example creates an ASG that attempts to keep around at least 10 `t1.medium` EC2 instances:

```typescript
import * as classic from "@pulumi/awsx/classic";

const autoScalingGroup = new classic.autoscaling.AutoScalingGroup("testing", {
    templateParameters: { minSize: 10 },
    launchConfigurationArgs: { instanceType: "t2.medium" },
});
```

For detailed information about configuring your ASG, see
[Configuring Your Auto Scaling Group](#configuring-your-auto-scaling-group),
in addition to [the `AutoScalingGroup` API documentation](
/docs/reference/pkg/nodejs/pulumi/awsx/autoscaling#AutoScalingGroup).

#### Creating An Auto Scaling Group for ECS

Another way to create an ASG is to define it on an `awsx.ecs.Cluster` when auto-scaling the EC2 instances powering
our ECS cluster. This is not necessary when using ECS "Fargate", but by defining an ASG, you have complete control
over the scaling of your ECS cluster. For more information about ECS specifically, see the associated
[Pulumi Crosswalk for AWS ECS documentation](/docs/guides/crosswalk/aws/ecs/).

To make this easier, the `awsx.classic.ecs.Cluster` class offers a `createAutoScalingGroup` class that associates the newly
created ASG with the ECS cluster, and runs all container compute on it. For example:

```typescript
import * as classic from "@pulumi/awsx/classic";

const cluster = new classic.ecs.Cluster("testing", { vpc });

const autoScalingGroup = cluster.createAutoScalingGroup("testing", {
    templateParameters: { minSize: 10 },
    launchConfigurationArgs: { instanceType: "t2.medium" },
});
```

This will create an ASG that use the private subnets of the VPC, attempting to keep around at least 10 `t2.medium`
EC2 instances. If you want instances to be allowed access to the internet, this can be done by specifying:

```typescript
const autoScalingGroup = cluster.createAutoScalingGroup("testing", {
    // ... other parameters
    subnetIds: vpc.publicSubnetIds,
    launchConfigurationArgs: { instanceType: "t2.medium", associatePublicIpAddress: true },
});
```

Here we place in the public subnets of the VPC and provide `associatePublicIpAddress: true` so that instances
will have IPs that are externally reachable.

### Configuring Your Auto Scaling Group

The `AutoScalingGroup`'s `templateParameters` property allows one to control additional aspects of the ASG. For
example, the following are supported:

1. Setting a `maxSize` for the maximum number of instances that can be launched at a time.
2. Controlling how health checks are performed to determine if new instances should be created.
3. Specifying an appropriate `defaultCooldown` period which controls how often the ASG actually scales your instances.
   This cooldown period helps avoid rapid runaway scaling scenarios from happening.

For full details about what properties are available, refer to [the API Documentation](
/docs/reference/pkg/nodejs/pulumi/awsx/autoscaling#TemplateParameters)

### Specifying the Launch Configuration for EC2 Instances

The `launchConfiguration` (or `launchConfigurationArgs`) properties help control the configuration of the actual
instances that are launched by the ASG.  A launch configuration is an instance configuration template that an ASG uses
to launch new EC2 instances ait scales.

When you create a launch configuration, you specify information for the instances, including the Amazon Machine Image
(AMI), the instance type, a key pair, one or more security groups, and a block device mapping. If you've launched an
EC2 instance before, you specified the same information in order to launch the instance. If you don't provide these
properties, a default configuration will be created on your behalf with basic values set as appropriate.

For full details about what properties are available, refer to [the API Documentation](
/docs/reference/pkg/nodejs/pulumi/awsx/autoscaling#AutoScalingLaunchConfigurationArgs).

## Automatically Scaling Based on a Schedule

An ASG will automatically scale the EC2 instances using the specified launch configuration. One way to scale is
based on a schedule, so that you can set your own scaling schedule for predictable load changes. For example, if
the traffic to your web application starts to increase on Wednesday, remains high on Thursday, and starts to
decrease on Friday, you can plan your scaling actions based on the predictable traffic patterns of your web application.
Scaling actions are performed automatically as a function of time and date.

To create an ASG schedule, use [the `scaleOnSchedule` function](
/docs/reference/pkg/nodejs/pulumi/awsx/autoscaling#AutoScalingGroup-scaleOnSchedule) on the `AutoScalingGroup` class:

```typescript
// Schedule the ASG to go up to 20 instances on Friday and back down to 10 on Monday.
autoScalingGroup.scaleOnSchedule("scaleUpOnFriday", {
    desiredCapacity: 20,
    recurrence: { dayOfWeek: "Friday" },
});
autoScalingGroup.scaleOnSchedule("scaleDownOnMonday", {
    desiredCapacity: 10,
    recurrence: { dayOfWeek: "Monday" },
});
```

Alternatively, ASG schedules also support normal [Cron](https://en.wikipedia.org/wiki/Cron) format strings like so:

```typescript
// Schedule the ASG to go up to 20 instances on Friday and back down to 10 on Monday.
autoScalingGroup.scaleOnSchedule("scaleUpOnFriday", {
    desiredCapacity: 20,
    recurrence: "* * * * 5",
});
autoScalingGroup.scaleOnSchedule("scaleDownOnMonday", {
    desiredCapacity: 10,
    recurrence: "* * * * 1",
});
```

## Dynamically Scaling Based on Metrics and Policies

Although scaling based on fixed time schedules is an easy solution to many problems, it isn't as flexible as doing
so in reaction to real conditions happening in the environment. Scaling policies offer a more advanced way to scale.

Using an ASG scaling policy, you can define parameters that control the scaling process. For example, you could have a
web application that currently runs on two EC2 instances and you want the CPU utilization of the group to stay at around
50 percent when the load on the application changes. This is useful for scaling in response to changing conditions,
when you don't necessarily know a specific schedule when those conditions will change.

There are two main ways to express these dynamic scaling policies:

1. [Target Tracking](#dynamically-scaling-with-target-tracking-scaling). With target tracking scaling policies,
   you select a scaling metric and set a target value. Amazon EC2 Auto Scaling creates and manages the CloudWatch
   alarms that trigger the scaling policy and calculates the scaling adjustment based on the metric
   and the target value. The scaling policy adds or removes capacity as required to keep the metric
   at, or close to, the specified target value.

2. [Step Scaling](#dynamically-scaling-with-step-scaling). With step scaling, you choose scaling metrics and
   threshold values for the CloudWatch alarms that trigger the scaling process as well as define how your
   scalable target should be scaled when a threshold is in breach for a specified number of
   evaluation periods. Step scaling policies increase or decrease the current capacity of a scalable
   target based on a set of scaling adjustments, known as step adjustments. The adjustments vary
   based on the size of the alarm breach.

For extensive information about EC2 ASGs and scaling policies, refer to [Scaling the Size of Your Auto Scaling Group](
https://docs.aws.amazon.com/autoscaling/ec2/userguide/scaling_plan.html).

### Dynamically Scaling with Target Tracking Scaling

With target tracking scaling policies, you select a scaling metric and set a target value. Amazon
EC2 Auto Scaling creates and manages the CloudWatch alarms that trigger the scaling policy and
calculates the scaling adjustment based on the metric and the target value. The scaling policy adds
or removes capacity as required to keep the metric at, or close to, the specified target value. In
addition to keeping the metric close to the target value, a target tracking scaling policy also
adjusts to the changes in the metric due to a changing load pattern.

#### Using Predefined Target Tracking Scaling

Target Tracking Scaling for ASGs offer several pre-defined scaling metrics.

* Scaling based on CPU utilization:

    ```typescript
    // Try to keep the ASG using around 50% CPU.
    autoScalingGroup.scaleToTrackAverageCPUUtilization("keepAround50Percent", {
        targetValue: 50,
    });
    ```

    If you only want the ASG to scale up by adding instances, and not have it remove instances when usage falls, you
    can pass `disableScaleIn: true`.

    ```typescript
    autoScalingGroup.scaleToTrackAverageCPUUtilization("scaleDownOnMonday", {
        targetValue: 50,
        disableScaleIn: true,
    });
    ```

* Scaling based on the average number of bytes sent/received on all network interfaces in this ASG:

    ```typescript
    autoScalingGroup.scaleToTrackAverageNetworkIn("scaleDownOnMonday", {
        targetValue: 1024*1024*1024 /*1GB*/,
    });
    autoScalingGroup.scaleToTrackAverageNetworkOut("scaleDownOnMonday", {
        targetValue: 1024*1024*1024 /*1GB*/,
    });
    ```

* Scaling based on the average number of requests completed per ELB ALB target group in
  the ASG. In order to do this, the ASG must be informed of that particular TargetGroup at creation time. Scaling
  for ELB TargetGroups is only supported if the `targetType` is set to `"instance"`:

    ```typescript
    const cluster = new classic.ecs.Cluster("testing");
    const loadBalancer = new classic.lb.ApplicationLoadBalancer("testing");

    const targetGroup = loadBalancer.createTargetGroup("testing", { port: 80, targetType: "instance" });

    const autoScalingGroup = cluster.createAutoScalingGroup("testing", {
        targetGroups: [targetGroup],
        subnetIds: awsx.ec2.Vpc.getDefault().publicSubnetIds,
        templateParameters: { minSize: 10 },
        launchConfigurationArgs: { instanceType: "t2.medium", associatePublicIpAddress: true },
    });

    const policy = autoScalingGroup.scaleToTrackRequestCountPerTarget("onHighRequest", {
        targetValue: 1000,
        targetGroup: targetGroup,
    });
    ```

#### Using Custom Metric Target Tracking Scaling

On top of the predefined targets defined above, you can also scale using [a CloudWatch metric](/docs/guides/crosswalk/aws/cloudwatch#subscribing-to-cloudwatch-metrics), such as based on CPU or memory utilization.

Not all metrics work for target tracking, an important point when specifying a customized metric. The metric must be a
valid utilization metric and describe how busy an instance is. The metric value must increase or decrease proportionally
to the number of instances in the ASG so that the metric data can be used to proportionally scale the number of instances.

We recommend that you scale on Amazon EC2 instance metrics with a 1-minute frequency because that ensures a faster
response to utilization changes. Scaling on metrics with a 5-minute frequency can result in slower response times and
scaling on stale metric data. By default, Amazon EC2 instances are enabled for basic monitoring, which means metric
data for instances is available at 5-minute intervals. You can enable detailed monitoring to get metric data for
instances at 1-minute frequency. For more information, see [Configure-Monitoring-for-Auto-Scaling-Instances](
https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-monitoring.html#enable-as-instance-metrics).

The following example scales your ASG by attempting to keep EC2 instances around a 50% memory utilization:

```typescript
autoScalingGroup.scaleToTrackMetric("keepAround50Percent", {
    metric: classic.ecs.metrics.memoryUtilization({ service, statistic: "Average", unit: "Percent" }),
    targetValue: 50,
});
```

For additional details on Target Tracking Scaling, refer to
[Target Tracking Scaling Policies for Amazon EC2 Auto Scaling](
https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html).

### Dynamically Scaling with Step Scaling

Step scaling policies increase or decrease the current capacity of your ASG based on a set of scaling adjustments,
known as step adjustments. The adjustments vary based on the size of the alarm breach.

For example, consider the following step scaling description for an ASG that has both a current capacity and a desired
capacity of 10. The current and desired capacity is maintained while the aggregated metric value is greater than 40
and less than 60:

```typescript
autoScalingGroup.scaleInSteps("scale-in-out", {
    metric: classic.ecs.metrics.memoryUtilization({ service, statistic: "Average", unit: "Percent" }),
    adjustmentType: "PercentChangeInCapacity",
    steps: {
        lower: [{ value: 30, adjustment: -30 }, { value: 40, adjustment: -10 }],
        upper: [{ value: 60, adjustment: 10 }, { value: 70, adjustment: 30 }]
    },
};
```

This represents the following scaling strategy:

```
Memory utilization:

0%               30%    40%          60%     70%               100%
-------------------------------------------------------------------
|       -30%      | -10% | Unchanged  | +10%  |       +30%        |
-------------------------------------------------------------------
```

This step scaling configuration will end up setting two alarms for this metric. One for when the metric goes above 60%,
and another for where it goes below. Depending on which step range the value is in when the alarm fires, the ASG will
scale accordingly. Because we've chosen `"PercentChangeInCapacity"` as our adjustment type, a value of 65% would scale
the ASG up by 10%, while a value of 85% would scale the ASG up by 30%.

If the metric value gets to 60, Auto Scaling increases the desired capacity of the group by 1, to 11. That's based on
the second step adjustment of the scale-out policy (add 10 percent of 10). After the new capacity is added, Application
Auto Scaling increases the current capacity to 11. If the metric value rises to 70 even after this increase in capacity,
Application Auto Scaling increases the target capacity by 3, to 14. That's based on the third step adjustment of the
scale-out policy (add 30 percent of 11, 3.3, rounded down to 3).

If the metric value gets to 40, Application Auto Scaling decreases the target capacity by 1, to 13, based on the second
step adjustment of the scale-in policy (remove 10 percent of 14, 1.4, rounded down to 1). If the metric value falls to
30 even after this decrease in capacity, Application Auto Scaling decreases the target capacity by 3, to 10, based on
the third step adjustment of the scale-in policy (remove 30 percent of 13, 3.9, rounded down to 3).

Other adjustment types are possible as well.  The full list is:

1. `"ChangeInCapacity"`. This increases or decreases the current capacity of the group by the
   specified number of instances. A positive value increases the capacity and a negative adjustment
   value decreases the capacity.  For example: If the current capacity of the group is 3 instances
   and the adjustment is 5, then when this policy is performed, there are 5 instances added to the
   group for a total of 8 instances.

2. `"ExactCapacity"`. This changes the current capacity of the group to the specified number of instances.
   Specify a positive value with this adjustment type.  For example: If the current capacity of the group is
   3 instances and the adjustment is 5, then when this policy is performed, the capacity is set to 5 instances.

3. `"PercentChangeInCapacity"`. As shown above, increment or decrement the current capacity of the
   group by the specified percentage. A positive value increases the capacity and a negative value
   decreases the capacity. If the resulting value is not an integer, it is rounded.   for
   more) details.  With "PercentChangeInCapacity", you can also specify the minimum number of
   instances to scale using the `minAdjustmentMagnitude` parameter.

For more extensive information about step scaling, see
[Simple and Step Scaling Policies for Amazon EC2 Auto Scaling](
https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html).

## Additional Auto Scaling Resources

For more information about Amazon Auto Scaling, see the following:

* [Amazon Auto Scaling homepage](https://aws.amazon.com/autoscaling/)
