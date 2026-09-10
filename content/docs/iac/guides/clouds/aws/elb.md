---
title_tag: "Using AWS Elastic Load Balancing (ELB)"
title: ELB
h1: AWS Elastic Load Balancing (ELB)
meta_desc: The AWSx ELB component provisions Application and Network Load Balancers, and integrates with other AWS services.
menu:
  iac:
    parent: iac-guides-clouds-aws
    name: ELB
    identifier: aws-guides-elb
    weight: 70

aliases:
- /docs/integrations/clouds/aws/guides/elb/
- /docs/iac/clouds/aws/guides/elb/
- /docs/reference/crosswalk/aws/elb/
- /docs/guides/crosswalk/aws/elb/
- /docs/clouds/aws/guides/elb/
---

[Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) (ELB) automatically distributes incoming
application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and Lambda
Functions. It can handle the varying load of your application traffic in a single Availability Zone or across multiple
Availability Zones.

## Overview

The AWSx ELB component provides APIs for provisioning Application and Network Load Balancers, and
integrates with other services, including [API Gateway](/docs/iac/guides/clouds/aws/api-gateway/),
[Elastic Container Service (ECS)](/docs/iac/guides/clouds/aws/ecs/), [Lambda](/docs/iac/guides/clouds/aws/lambda/), and [VPC](/docs/iac/guides/clouds/aws/vpc/), to give
the different kinds of compute you run in AWS configurable network accessibility.

Elastic Load Balancing offers multiple types of load balancers that all feature the high availability, automatic
scaling, and robust security necessary to make your applications fault tolerant:

* [Network Load Balancer (NLB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) is
  best suited for load balancing of Transmission Control Protocol (TCP) and Transport Layer Security (TLS) traffic where
  extreme performance is required. Operating at the connection level (Layer 4), Network Load Balancer routes traffic to
  targets within Amazon Virtual Private Cloud (Amazon VPC) and is capable of handling millions of requests per second
  while maintaining ultra-low latencies. Network Load Balancer is also optimized to handle sudden and volatile traffic
  patterns.

* [Application Load Balancer (ALB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
  is best suited for load balancing of HTTP and HTTPS traffic and provides advanced request routing targeted at the
  delivery of modern application architectures, including microservices, containers, and HTTP/2 traffic. Operating at
  the individual request level (Layer 7), Application Load Balancer routes traffic to targets within Amazon Virtual
  Private Cloud (Amazon VPC) based on the content of the request.

Each kind of load balancer is represented by a class in the `awsx.lb` module:

* `NetworkLoadBalancer` is used for NLBs
* `ApplicationLoadBalancer` is used for ALBs.

{{< notes >}}
These types are similar and support many of the same scenarios. Most examples here use ALBs, but switching
to an NLB is usually just a matter of swapping out this class. Any differences are noted below.
{{< /notes >}}

## Creating a load balancer

To create a new load balancer, instantiate its class. You also need a _listener_ so that traffic can reach the
load balancer:

{{< example-program path="awsx-elb-web-listener">}}

This load balancer listens on port 80, in your account's per-region default VPC, using its public subnets, thereby
exposing it to the internet. See below for instructions on how to
[make your load balancer private](#listening-on-private-subnets) or to
[run in a custom VPC](#creating-a-load-balancer-in-a-custom-vpc).

You can also set these properties:

* `enableHttp2`: Set to `true` to enable HTTP/2 traffic on your ALB. HTTP/2 is not supported for NLBs.

* `enableDeletionProtection`: Set to `true` to disable deletion of the resource. This can be helpful to avoid
  accidentally deleting a long-lived, but auto-generated, load balancer URL.

* `idleTimeout`: The time in seconds a connection is permitted to be idle before being severed. The default is `60`.

* `tags`: Can be used to tag your load balancer with metadata about its purpose, for reporting or compliance.

For the load balancer to do anything useful, you must also specify a _target_ for traffic to be routed to.
The target could be an EC2 instance, an ECS service, or anything else with an IP address. You
also have to configure security groups to let traffic flow inside your VPC on the correct ports.

## Load balancing EC2 instance targets

To target an EC2 instance with your load balancer, you must do the following:

1. Open ingress traffic to your load balancer. Explicitly needed for NLB, but not ALB.
1. Open egress traffic from your EC2 instance to your load balancer (for health checks).
1. Ensure the security group for your load balancer at least contains the ingress rule from (1).
1. Create the EC2 instance(s) in the same VPC and ensure the security group contains the egress rule (2).
1. Attach your load balancer's target group to the desired EC2 instance(s).

Aside from those five steps, the code and capabilities of the load balancer are the same as shown above.

{{< notes >}}
ALBs automatically open ingress traffic to the ports they listen on, whereas NLBs do not.
{{< /notes >}}

Here is an example that creates an EC2 instance per availability zone, running an Amazon Linux 2 web server:

{{< example-program path="awsx-load-balanced-ec2-instances" >}}

After deploying this with `pulumi up`, you have a fully functional endpoint:

```bash
$ for i in {1..5} ; do curl "http://$(pulumi stack output endpoint)" ; done
Hello World, from Server 1!
Hello World, from Server 1!
Hello World, from Server 3!
Hello World, from Server 2!
Hello World, from Server 1!
```

The load balancer creates a default target group that forwards traffic on the same port. If you need
to configure the way that traffic is forwarded, health checks, and so on, see
[Advanced load balancer listener and target group configuration](#advanced-load-balancer-listener-and-target-group-configuration) below.

For more advanced cases, you will most likely want to use [EC2 Auto Scaling](
https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html), rather than hard-coding
the number and placement of VMs. Refer to the API docs for
[LaunchTemplate](/registry/packages/aws/api-docs/ec2/launchtemplate/) and
[AutoScalingGroup](/registry/packages/aws/api-docs/autoscaling/group/) for details on how to do so.

## Load balancing ECS service targets

Your ECS service can use ELB to distribute traffic evenly across each of your service's tasks. To target an ECS service
with your load balancer, pass the load balancer's target group in your task definition's `portMappings`. AWSx uses that
target group to populate the ECS service's load balancer configuration for you:

{{< example-program path="awsx-load-balanced-fargate-nginx" >}}

{{< notes >}}
[The AWSx ECS component](/docs/iac/guides/clouds/aws/ecs/) — the classes in the `awsx.ecs` package — creates the
right ingress and egress rules automatically. If you are using raw `aws.ecs`, you need to manage the security group
ingress and egress rules yourself, much like the [EC2 instance](#load-balancing-ec2-instance-targets) example earlier.
{{< /notes >}}

After deploying this with `pulumi up`, you have a fully functional endpoint:

```bash
$ curl $(pulumi stack output url)
<!DOCTYPE html>
<html>
<body>
<h1>Welcome to nginx!</h1>
</body>
</html>
```

This load balancer uses reasonable targeting defaults and health checks. If you'd like to customize these,
see [Advanced load balancer listener and target group configuration](#advanced-load-balancer-listener-and-target-group-configuration) below.

Although ECS supports both NLB and ALB, ALBs offer two features that make them more attractive for ECS:

* Dynamic host port mapping enables multiple tasks from the same service to use the same container instance.
* Path-based routing and priority rules allow multiple services to use the same listener port on a single ALB.

We recommend ALBs for your ECS services unless a service requires a feature that's only available with NLBs.

For more extensive information about load balancing and ECS services, refer to AWS's
[Service Load Balancing](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html)
documentation.

## Listening on private subnets

By default, your load balancer is created as _internet-facing_, meaning it'll use the VPC's public subnets and listen for traffic coming from the internet.
If you want to instead keep your load balancer private, servicing traffic inside of your VPC over its private subnets,
set the `internal` property to `true`:

{{< example-program path="awsx-elb-private-subnet">}}

For complete control, you can pass an explicit list of subnets instead, using either the `subnets` property (subnet
objects) or the `subnetIds` property (subnet IDs).

## Creating a load balancer in a custom VPC

Each region contains [a default VPC](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html) for your
account. The load balancers created above will use it automatically, in addition to its default public or private
subnets, depending on whether you've overridden the default of public using `internal`.

If you'd like to create a load balancer for a custom VPC, provision (or look up) the VPC, then use the `subnetIds`
property of the load balancer to associate it with the VPC's public or private subnet:

{{< example-program path="awsx-elb-vpc" >}}

For more information on creating and configuring VPCs, refer to [the AWSx VPC component guide](/docs/iac/guides/clouds/aws/vpc/).

## Advanced load balancer listener and target group configuration

The above examples were simplistic in their usage of target groups and listeners. In many scenarios, that's all you
need. However, target groups and listeners are more powerful than this and have advanced functionality built-in.

Both NLB and ALB style load balancers share the same core concepts:

* A _load balancer_ serves as the single point of contact for clients. The load balancer distributes incoming
  application traffic across multiple targets, such as EC2 instances, in multiple availability zones. This increases
  the availability of your application. You add one or more listeners to your load balancer.

* A [_listener_](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html) checks
  for connection requests from clients, using the protocol and port that you configure, and forwards
  requests to one or more target groups, based on the rules that you define. Each rule specifies a target group,
  condition, and priority. When the condition is met, the traffic is forwarded to the target group. You must define a
  default rule for each listener, and you can add rules that specify different target groups based on the content of the
  request (also known as content-based routing).

* Each [_target group_](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html) routes
  requests to one or more registered targets, such as EC2 instances, using the protocol and
  port number that you specify. You can register a target with multiple target groups. You can configure health checks
  on a per target group basis. Health checks are performed on all targets registered to a target group that is
  specified in a listener rule for your load balancer.

Many of the examples above rely on smart defaults in the `NetworkLoadBalancer` and `ApplicationLoadBalancer` classes,
including target groups that are created automatically from the same inbound port information as the listeners.

### Manually configuring listeners

When you create a listener, the `listener` property chooses smart defaults based on whether the listener is created
against a load balancer or a target group. These configuration options are also available:

* `protocol`: NLBs support `TCP`, `TLS`, `UDP`, `TCP_UDP`, `QUIC`, and `TCP_QUIC`, while ALBs support `HTTP` and
  `HTTPS`. If not specified, NLBs default to `TCP` and ALBs will select `HTTP` or `HTTPS` based on the port supplied.

* `certificateArn` and `sslPolicy`: Enables SSL using the given certificate and policy. This policy controls how
  SSL connections are terminated, among other things. Refer to
  [Create an HTTPS listener for your Application Load Balancer](
  https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html) for more information.

* `defaultActions`: Configure the rules and actions to take in response to traffic reaching your
  load balancer. By default, that entails forwarding traffic to a target group. However, additional options are
  available via the `ListenerDefaultAction` type. You may provide multiple rules:

    * `authenticateCognito`: Enable Cognito authentication for access through your load balancer. For more
      information, see [Authenticate users using an Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html).

    * `authenticateOidc`: Authenticate access through your load balancer using an OpenID Connect (OIDC) compliant
      identity provider.

    * `fixedResponse`: Return a custom HTTP response, rather than forwarding traffic. For details, see
      [Fixed-response actions](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/rule-action-types.html#fixed-response-actions).

    * `redirect`: Redirect from one URL to another. For details, see
      [Redirect actions](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/rule-action-types.html#redirect-actions).

As an example of a custom action, the following load balancer redirects HTTP traffic on port 8080 to port 8081 by defining two listeners, one configured to redirect to the other:

{{< example-program path="awsx-elb-multi-listener-redirect" >}}

```bash
$ curl -I "http://$(pulumi stack output endpoint):8080"

HTTP/1.1 301 Moved Permanently
Location: http://lb-692829a-1197942792.us-west-2.elb.amazonaws.com:8081/
```

For more information on listener rules, refer to the [AWS documentation about listener rules](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-rules.html).

### Manually configuring target groups

A target group is automatically created for each listener that doesn't override the default action. This group
can then be used to load balance any number of targets, including EC2 instances, ECS services, or arbitrary IPs.

You can also create a target group manually, either by defining a `defaultTargetGroup` on the load balancer directly or by creating a
`TargetGroupAttachment` resource. When doing so, the following additional options are available:

* `deregistrationDelay`: The amount of time for ELB to wait before changing the state of a load balancer from
  draining to unused. The range is 0–3600 seconds, and the default is 300. This is how long an application has to
  shut down gracefully before its traffic is severed.

* `slowStart`: The amount of time for ELB to wait before sending a target its full share of requests. This can give
  the application time to boot and warm up before it takes traffic. The range is 30–900 seconds, or 0 to disable.
  Slow start is disabled by default.

* `stickiness`: If enabled (for ALBs only), a cookie will be used to ensure traffic consistently flows to the same
  targets, provided they remain active.

* `targetType`: The kind of target this target group registers. The possible values are `instance` (an EC2 instance
  ID), `ip` (an IP address), `lambda` (a Lambda function), and `alb` (an Application Load Balancer). The default is
  `instance`. Note also that IP addresses must be routable within your VPC and cannot be public IP addresses: they
  must fall within your VPC's private subnet range, the RFC 1918 ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16),
  or the RFC 6598 range (100.64.0.0/10).

* `healthCheck`: Overrides the default health check behavior. The parameters available vary by target protocol
  and differ considerably between NLB and ALB. This includes:

    * `interval`: The approximate amount of time, in seconds, between health checks of an individual
       target. The range is 5–300 seconds, and the default is 30 seconds.

    * `healthyThreshold`: The number of consecutive successful health checks required before considering an
      unhealthy target healthy. The range is 2–10, and the default is 3.

    * `unhealthyThreshold`: The number of consecutive failed health checks required before considering the target
       unhealthy. For NLBs, this value must be the same as `healthyThreshold`. The range is 2–10, and the default
       is 3.

    * `path`: For ALB only, the required destination for health check requests. This allows for application level
      health checking, versus NLBs which only support health checking the availability of the target.

    * `timeout`: The amount of time, in seconds, during which no response from a target means a failed health
      check. The range is 2–120 seconds. When you don't set it, AWS applies its own default: 6 seconds for `HTTP`
      target groups, and 10 seconds for `HTTPS`, `TCP`, and `TLS` target groups.

    * `matcher`: For ALB only, the HTTP codes to use when checking for a successful response from a target. You can
      specify multiple values (for example, "200,202") or a range of values (for example, "200-299").

* `tags`: Can be used to tag your target group with metadata about its purpose, for reporting or compliance.

For more extensive information on ELB target groups, [refer to the AWS documentation](
https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html).
