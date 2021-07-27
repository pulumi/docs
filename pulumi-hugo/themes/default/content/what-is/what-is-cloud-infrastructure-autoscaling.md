---
title: What Is Cloud Infrastructure Autoscaling?
meta_desc: |
    Autoscaling is a service offered by the cloud provider that will increase or decrease the number of servers, based on need.

type: what-is
page_title: Autoscaling 101

customer_logos:
  title: Leading engineering organizations are building with Pulumi
  logos:
    - items:
      - snowflake
      - tableau
      - atlassian
      - fauna
      - ware2go
    - items:
      - mindbody
      - sourcegraph
      - fenergo
      - kenshoo
      - lemonade
    - items:
      - clearsale
      - angellist
      - webflow
      - supabase
      - ro
---

Two of the great advantages to infrastructure in the cloud are flexibility and speed. You can quickly adjust your infrastructure to conform to variable conditions, such as the amount of traffic or the number of requests in a queue. In other words, you can scale your infrastructure up or down, depending on what you need at a particular time. Scaling often refers to servers (or instances), in particular.

## Scaling Up or Scaling Out

Scaling up is when you make a server more powerful so it can handle more load. Scaling out means distributing the workload by adding more servers.

To scale up (also called vertical scaling), you might add more CPUs, memory, or network capacity. Scaling up works well for applications that are difficult to distribute. A good example is a relational database. Distributing the database across multiple servers may have unintended consequences, such as changing the data. It might be easier to use a more powerful machine, instead.

Scaling out (also called horizontal scaling) spreads the workload across multiple servers that work in parallel. Applications that can sit on a single machine, such as websites, are well-suited to scaling out because you don’t need to coordinate tasks between servers. For example, a retail website might have peak periods, such as around the Christmas holiday or when there are sales. During those times, you would want to add more servers to handle the additional traffic so your site stays responsive to customer demand.

## What is Autoscaling?

Autoscaling is a service offered by the cloud provider. Once you configure it, that service automatically scales out for you. It increases or decreases the number of servers, based on need. With autoscaling, your workload gets exactly the resources it requires at any given time. You pay only for the server resources you use.

Autoscaling is a great feature if your workload is at all volatile. It isn’t practical to have someone manually adjusting the number of servers you need. Instead, use automation to make sure it happens instantly. You set the parameters, either through your cloud provider’s console or, even better, programmatically.

With a properly configured service, your infrastructure manages itself and you can be certain that when your application needs additional resources, those resources will be available. You can also know that, when demand decreases, you won’t be paying for servers you’re not using.

## Who Provides Autoscaling?

Autoscaling is a standard service offered by most cloud providers, although they each call it something different. For example:

- AWS provides Auto Scaling groups.
- Google Cloud provides Managed Instance Groups (MIGs).
- Microsoft has a service called Autoscale.

### AWS Auto Scaling

AWS Auto Scaling monitors your applications and automatically adjusts capacity to maintain steady, predictable performance. You can build scaling plans for resources including Amazon EC2 instances and Spot Fleets, Amazon ECS tasks, Amazon DynamoDB tables and indexes, and Amazon Aurora Replicas. The service provides recommendations to help you optimize performance, costs, or some balance between them.

### Google Cloud

MIGs (where an instance group is a collection of VM instances that you can manage as a single entity) allow you to automatically add or delete VM instances from a MIG, based on increases or decreases in load. You define an autoscaling policy and the autoscaler performs automatic scaling based on the measured load and the options you configured. The service also offers predictive autoscaling, where the autoscaler forecasts future load based on historical data and scales out a MIG in advance.

### Azure Autoscale

Autoscale is a built-in feature of Cloud Services, Mobile Services, Virtual Machine Scale Sets, and Websites. Autoscale can scale your service by a variety of criteria or you can define your own custom metrics. You can set a schedule so that you anticipate known spikes in demand. You can also set alerts based on metrics, such as CPU status or response time and create alerts for events, including when autoscale itself is triggered.

## Learn More

Ready to learn more? With Pulumi, you can create and manage infrastructure with the languages and tools you already know. To help you implement autoscaling on AWS, check out [Pulumi Crosswalk for AWS]({{< relref "/docs/guides/crosswalk/aws" >}}), which enables easy definition of Auto Scaling Groups (ASGs) to configure scaling of EC2 instances. You can [get started]({{< relref "/docs/get-started" >}}) for free today.
