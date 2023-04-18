---
title_tag: "Using AWS Elastic Load Balancing (ELB) | Crosswalk"
title: Using AWS Elastic Load Balancing (ELB)
meta_desc: Pulumi Crosswalk for AWS ELB provides easy provisioning Application and Network Load Balancers, and easily
           integrates with functionality of AWS other services.
linktitle: Elastic Load Balancing (ELB)
menu:
  userguides:
    parent: crosswalk-aws
    weight: 7

aliases: ["/docs/reference/crosswalk/aws/elb/"]
---

<a href="./">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) (ELB) automatically distributes incoming
application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and Lambda
Functions. It can handle the varying load of your application traffic in a single Availability Zone or across multiple
Availability Zones.

## Overview

Pulumi Crosswalk for AWS ELB provides easy APIs for provisioning Application and Network Load Balancers, and
integrates with functionality for other services, including [API Gateway](/docs/guides/crosswalk/aws/api-gateway/),
[Elastic Container Service (ECS)](/docs/guides/crosswalk/aws/ecs), [Lambda](/docs/guides/crosswalk/aws/lambda/), and [VPC](/docs/guides/crosswalk/aws/vpc/), to provide
configurable network accessibility to the different kinds of compute you will run inside of AWS.

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

> These types are similar and support many of the same scenarios. Most examples show using ALBs, however changing
> to an NLB is usually as simple as swapping out this class. Any differences will be noted below.

## Creating a Load Balancer

To create a new load balancer, allocate an instance of its class. In addition to creating the load balancer itself, we
must also create a _listener_ to let traffic reach it:

```typescript
import * as awsx from "@pulumi/awsx";

// Create an ALB associated with the default VPC for this region.
const alb = new awsx.lb.ApplicationLoadBalancer("web-traffic");

// Listen to HTTP traffic on port 80.
const listener = alb.createListener("web-listener", { port: 80 });

// Export the resulting URL so that it's easy to access.
export const endpoint = listener.endpoint;
```

This load balancer listens on port 80, in our account's per-region default VPC, using its public subnets, thereby
exposing it to the Internet. See below for instructions on how to
[make your load balancer private](#listening-on-private-subnets) or to
[run in a custom VPC](#creating-a-load-balancer-in-a-custom-vpc).

There are a number of additional properties you may set:

* `enableHttp2`: Set to `true` to enable HTTP/2 traffic on your ALB. HTTP/2 is not supported for NLBs.

* `enableDeletionProtection`: Set to `true` to disable deletion of the resource. This can be helpful to avoid
  accidentally deleting a long-lived, but auto-generated, load balancer URL.

* `enableCrossZoneLoadBalancing`: Set to `true` to enable your NLB to load balance across availability zones.

* `idleTimeout`: The time in seconds a connection is permitted to be idle before being severed. The default is `60`.

* `tags`: Can be used to tag your load balancer with metadata about its purpose, for reporting or compliance.

For the load balancer to do anything useful, we must also specify a _target_ that traffic will be routed to.
The target could be an EC2 instance, ECS service, or anything with an IP address, for instance. We
will also have to configure SecurityGroups to let traffic flow inside of our VPC on the correct ports.

## Load Balancing EC2 Instance Targets

To target an EC2 instance with your load balancer, you must do the following:

1. Open ingress traffic to your load balancer. Explicitly needed for NLB, but not ALB.
2. Open egress traffic from your EC2 instance to your load balancer (for health checks).
3. Ensure the security group for your load balancer at least contains the ingress rule from (1).
4. Create the EC2 instance(s) in the same VPC and ensure the security group contains the egress rule (2).
5. Attach your load balancer's target group to the desired EC2 instance(s).

Aside from those three steps, the code and capabilities of the load balancer are the same as shown above.

> Note that ALBs automatically open ingress traffic to the ports listened on, whereas NLBs do not.

Here is an example that creates an EC2 instance per availability zone, running a simple Ubuntu web server:

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";
import * as pulumi from "@pulumi/pulumi";

export = async () => {
  const config = new pulumi.Config("aws");
  const providerOpts = { provider: new aws.Provider("prov", { region: <aws.Region>config.require("region") }) };
  // Create a security group to open ingress to our load balancer on port 80, and egress out of the VPC.
  const vpc = awsx.ec2.Vpc.getDefault();
  const sg = new awsx.ec2.SecurityGroup("web-sg", {
      vpc,
      // 1) Open ingress traffic to your load balancer. Explicitly needed for NLB, but not ALB:
      // ingress: [{ protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: [ "0.0.0.0/0" ] }],
      // 2) Open egress traffic from your EC2 instance to your load balancer (for health checks).
      egress: [{ protocol: "-1", fromPort: 0, toPort: 0, cidrBlocks: [ "0.0.0.0/0" ] }],
  });

  // Creates an ALB associated with the default VPC for this region and listen on port 80.
  // 3) Be sure to pass in our explicit SecurityGroup created above so that traffic may flow.
  const alb = new awsx.lb.ApplicationLoadBalancer("web-traffic", { securityGroups: [ sg ] });
  const listener = alb.createListener("web-listener", { port: 80 });
  const publicIps: pulumi.Output<string>[] = [];
  const subnets = await vpc.publicSubnets;

  // For each subnet, and each subnet/zone, create a VM and a listener.
  for (let i = 0; i < subnets.length; i++) {
      // 4) Create the instance in the same VPC, passing in the security group with egress rule.
      const vm = new aws.ec2.Instance(`web-${i}`, {
          ami: aws.getAmi({
              filters: [
                  { name: "name", values: [ "ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-*" ] },
                  { name: "virtualization-type", values: [ "hvm" ] },
              ],
              mostRecent: true,
              owners: [ "099720109477" ], // Canonical
          }).then(ami => ami.id),
          instanceType: "t2.micro",
          subnetId: subnets[i].subnet.id,
          availabilityZone: subnets[i].subnet.availabilityZone,
          vpcSecurityGroupIds: alb.securityGroups.map(sg => sg.securityGroup.id),
          userData: `#!/bin/bash
  echo "Hello World, from Server ${i+1}!" > index.html
  nohup python -m SimpleHTTPServer 80 &`,
        }, providerOpts);
        publicIps.push(vm.publicIp);
        // 5) Attach your load balancer's target group the target EC2 instance(s).
        alb.attachTarget("target-" + i, vm);
      };
  }

  // Export the resulting URL so that it's easy to access.
  export const endpoint = listener.endpoint.hostname;
};
```

After deploying this using `pulumi up`, we will have a fully functional endpoint:

```bash
$ for i in {1..5}; do curl http://$(pulumi stack output endpoint); done
Hello World, from Server 1!
Hello World, from Server 1!
Hello World, from Server 2!
Hello World, from Server 2!
Hello World, from Server 1!
```

The load balancer creates a default target group that forwards traffic on the same port. If you need
to configure the way that traffic is forwarded, health checks, and so on, see
[Advanced NLB Target Group and Listener Configuration](#advanced-nlb-target-group-and-listener-configuration) below.

For more advanced cases, you will most likely want to use [EC2 Auto Scaling](
https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html), rather than hard-coding
the number of and placement of VMs. Refer to the API docs for
[LaunchConfiguration](/registry/packages/aws/api-docs/ec2/launchconfiguration/) and
[AutoScalingGroup](/registry/packages/aws/api-docs/autoscaling/group/) for details on how to do so.

## Load Balancing ECS Service Targets

Your ECS service can use ELB to distribute traffic evenly across each of your service's tasks. To target an ECS service
with your load balancer, pass the listener in your task definition's `portMappings`:

```typescript
import * as awsx from "@pulumi/awsx";

// Create a new ECS cluster. This will use the default VPC; to override, pass in a VPC manually.
const cluster = new awsx.ecs.Cluster("my-cluster");

// Create an ALB associated with the default VPC for this region and listen for HTTP on port 80.
const alb = new awsx.lb.ApplicationLoadBalancer("web-traffic");
const listener = alb.createListener("web-listener", { port: 80 });

// Create a new ECS service using the 'nginx' image. Supply the listener we just created
// in the `portMappings` section. This will both properly connect the service and launched
// instances to the target group. Although we show FargateService, EC2Service works too.
const nginx = new awsx.ecs.FargateService("nginx-task", {
    cluster,
    taskDefinitionArgs: {
        containers: {
            nginx: {
                image: "nginx",
                memory: 128,
                portMappings: [ listener ],
            },
        },
    },
    desiredCount: 2,
});

// Export the resulting URL so that it's easy to access.
export const endpoint = listener.endpoint.hostname;
```

> [Pulumi Crosswalk for AWS ECS](/docs/guides/crosswalk/aws/ecs/) -- those classes in the `awsx.ecs` package -- will automatically create the
> right ingress and egress rules. If you are using raw `aws.ecs`, you will need to manually manage the security group
> ingress and egress rules, much like the [EC2 Instance](#load-balancing-ec2-instances) example earlier.

After deploying this using `pulumi up`, we will have a fully functional endpoint:

```bash
$ curl http://$(pulumi stack output endpoint)
<!DOCTYPE html>
<html>
<body>
<h1>Welcome to nginx!</h1>
</body>
</html>
```

This load balancer uses reasonable targeting defaults and health checks. If you'd like to customize these,
see [Advanced NLB Target Group and Listener Configuration](#advanced-nlb-target-group-and-listener-configuration) below.

Although ECS supports both NLB and ALB, ALB offer several features that make them more attractive for ECS:

* Dynamic host port mapping enables multiple tasks from the same service to use the same container instance.
* Path-based routing and priority rules allow multiple services to use the same listener port on a single ALB.

We recommend using ALBs for your ECS services unless it requires a feature that is only available with NLBs.

For more extensive information about load balancing and ECS Services, refer to AWS's
[Service Load Balancing](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html)
documentation.

## Listening on Private Subnets

By default, your load balancer will use the VPC's public subnets. This listens for traffic coming from the Internet.
If you want to instead keep your load balancer private, servicing traffic inside of your VPC over its private subnets,
set the `external` property to `false`:

```typescript
import * as awsx from "@pulumi/awsx";

// Creates an ALB associated with the default VPC for this region, using its private subnets.
const alb = new awsx.lb.ApplicationLoadBalancer("web-traffic", { external: false });

// Listen to HTTP traffic on port 80.
const listener = alb.createListener("web-listener", { port: 80 });

// Export the resulting URL so that it's easy to access.
export const endpoint = listener.endpoint;
```

For complete control, you can elect instead to pass in an explicit list of subnets using the `subnets` property.

## Creating a Load Balancer in a Custom VPC

Each region contains [a default VPC](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html) for your
account. The load balancers created above will use it automatically, in addition to its default public or private
subnets, depending on whether you've overridden the default of public using `external`.

If you'd like to create a load balancer for a custom VPC, pass the `vpc` property:

```typescript
import * as awsx from "@pulumi/awsx";

// Allocate (or get) a custom VPC:
const vpc = new awsx.ec2.Vpc("web-vpc", { ... });

// Creates an ALB associated with our custom VPC.
const alb = new awsx.lb.ApplicationLoadBalancer("web-traffic", { vpc });

// Listen to HTTP traffic on port 80.
const listener = alb.createListener("web-listener", { port: 80 });

// Export the resulting URL so that it's easy to access.
export const endpoint = listener.endpoint;
```

For more information on creating and configuring VPCs, refer to [Pulumi Crosswalk for AWS VPC](/docs/guides/crosswalk/aws/vpc/).

## Advanced Load Balancer Listener and Target Group Configuration

The above examples were simplistic in their usage of target groups and listeners. In many scenarios, that's all we
need. However, target groups and listeners are more powerful than this and have advanced functionality built-in.

Let's review the core concepts involved in both NLB and ALB style load balancers:

* A _load balancer_ serves as the single point of contact for clients. The load balancer distributes incoming
  application traffic across multiple targets, such as EC2 instances, in multiple Availability Zones. This increases
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

Many of the examples above leverage smart defaults in the `NetworkLoadBalancer` and `ApplicationLoadBalancer` classes.
This includes creating target groups automatically that leverage the same inbound port information as the listeners.

### Manually Configuring Listeners

A listener may be created as shown earlier (by calling `createListener` on a load balancer), from a target group if
we want to automatically associate that as its default action (by calling `createListener` on a target group), or
by allocating a `NetworkTargetGroup` or `ApplicationTargetGroup` explicitly.

During the creation of a listener, there are numerous options available. The `createListener` functions will attempt
to choose smart defaults based on the scenario of creating the listener against a load balancer or target group.

These options include:

* `protocol`: NLBs support `TCP`, `TLS`, `HTTP`, and `HTTPS`, while ALBs support `HTTP` and `HTTPS`. If not specified,
  NLBs default to `TCP` and ALBs will select `HTTP` or `HTTPS` based on the port supplied.

* `certificateArn` and `sslPolicy`: Enables SSL using the given certificate and policy. This policy controls how
  SSL connections are terminated, among other things. Refer to
  [Create an HTTPS Listener for Your Application Load Balancer](
  https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html) for more information.

* `defaultAction` and `defaultActions`: Configure the rules and actions to take in response to traffic reaching your
  load balancer. By default, that entails forwarding traffic to a target group. However, additional options are
  available via the `ListenerDefaultActionArgs` type. You may provide multiple rules, each with a priority.

    * `authenticateCognito`: Enable Cognito authentication for access through your load balancer. For more
      information, see [Authenticate Users Using and Application Load Balancer](
      https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html).

    * `authenticateOidc`: Authenticate access through your load balancer using an OpenID Connect (OIDC) compliant
      identity provider.

    * `fixedResponse`: Return a custom HTTP response, rather than forwarding traffic. For details, see
      [Fixed-Response Actions](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#fixed-response-actions)

    * `redirect`: Redirect from one URL to another. For details, see
      [Redirect Actions](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#redirect-actions)

As an example of a custom action, the following load balancer ensures all HTTP traffic is redirected to HTTPS:

```typescript
import * as awsx from "@pulumi/awsx";

// Create an ALB. One listener on port 80 redirects to port 443, while the 443 listener passes traffic through.
const alb = new awsx.lb.NetworkLoadBalancer("web-traffic");
const httpListener = alb.createListener("http-listener", {
    port: 80,
    protocol: "HTTP",
    defaultAction: {
        type: "redirect",
        redirect: {
            protocol: "HTTPS",
            port: "443",
            statusCode: "HTTP_301",
        },
    },
});
const target = alb.createTargetGroup("web-target", { ... });
const httpsListener = target.createListener("http-listener", { port: 443, ... });
// attach the target to something that can serve traffic.

// Export the resulting URL so that it's easy to access.
export const endpoint = listener.endpoint;
```

For more information on listener rules, refer to the [AWS documentation about listeners](
https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#rule-action-types).

### Manually Configuring Target Groups

A target group is automatically created for each listener that doesn't override the default action. This group
can then be used to load balance any number of targets, including EC2 instances, ECS services, or arbitrary IPs.

To create a target group manually, call `createTargetGroup` on the load balancer, or allocate a
`NetworkTargetGroup` or `ApplicationTargetGroup` by hand. When doing so, the following additional options are available:

* `deregistrationDelay`: The amount of time for ELB to wait before changing the state of a load balancer from
  draining to unused. The range is 0-3600 seconds, and the default is 300. This is the period of time in which
  an application should gracefully shut down before traffic to it is severed.

* `slowStart`: The amount of time for ELB to wait before sending a target its full share of requests. This can give
  the application time to boot and warm up before it takes traffic. The range is 30-900 seconds or 0 to disable. The
  default is for slow start to be disabled.

* `stickiness`: If enabled (for ALBs only), a cookie will be used to ensure traffic consistently flows to the same
  targets, provided they remain active.

* `targetType`: The type of target you will be using with this target group. The possible values are `instance`,
  if targeting an EC2 instance ID directly, or `ip`, if targeting an IP address. The default is `ip`. Note also that
  IP addresses must be routable within your VPC and cannot be public IP addresses (within your VPC's private subnet
  range, the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).

* `healthCheck`: Overrides the default health check behavior. The parameters available vary by target protocol
  and differ considerably between NLB and ALB. This includes:

    * `interval`: The approximate amount of time, in seconds, between health checks of an individual
       target. The range is between 5-300 seconds, and defaults to 30 seconds.

    * `healthyThreshold`: The number of consecutive health checks successes required before considering an
      unhealthy target healthy. The default is 3.

    * `unhealthyThreshold`: The number of consecutive health check failures required before considering the target
       unhealthy. For NLBs, this value must be the same as `healthyThreshold`. The default is 3.

    * `path`: For ALB only, the required destination for health check requests. This allows for application level
      health checking, versus NLBs which only support health checking the availability of the target.

    * `timeout`: For ALB only, the timeout in seconds for health check requests. The range is 2-60 seconds, and the
      default value is 5 seconds.

    * `matcher`: For ALB only, the HTTP codes to use when checking for a successful response from a target. You can
      specify multiple values (for example, "200,202") or a range of values (for example, "200-299").

* `tags`: Can be used to tag your target group with metadata about its purpose, for reporting or compliance.

For more extensive information on ELB target groups, [refer to the AWS documentation](
https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html).

## Additional ELB Resources

For detailed reference documentation, visit the [API docs](
/docs/reference/pkg/nodejs/pulumi/awsx/lb).
