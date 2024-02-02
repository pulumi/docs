---
title_tag: BMW | Case Studies
title: "BMW: Mission Critical Platforms Require Pulumi"
description: |
    BMW used Pulumi to build a scalable and resilient hybrid cloud implementation that could handle more than eleven thousand developers.
meta_desc: Learn how BMW used Pulumi to simplify the automation of their AWS and on-premises infrastructure.

customer_name: BMW
customer_logo: /logos/customers/bmw-logo.png
customer_url: https://www.bmwusa.com/

exec_summary: |
   BMW, with the assistance of BearingPoint, was determined to build a scalable and resilient Gerrit infrastructure across cloud and on-premises instances. They needed a hybrid cloud implementation that could handle more than eleven thousand developers and hundreds of thousands of builds a day across three distinct environments. The solution needed to be self-documenting, highly available, and have a streamlined disaster recovery approach. BMW utilized Pulumi because it simplified scaling the automation of this architecture out across AWS and on-premises instances while also ensuring that compliance is baked into every step.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: Challenges
      anchor: designed-for-scale
    - label: Results
      anchor: pulumi-for-deployment
    - label: Conclusion
      anchor: how-pulumi-is-changing-the-game-for-bmw

aliases:
    - /case-studies/codecraft
---

## About CodeCraft

The automobile is becoming increasingly more connected over time and software is now central to the operation of nearly every component. This necessitates a development platform that is designed for the continuous evolution of technology in vehicles and the additional complexity it brings. CodeCraft is BMW’s integrated toolchain for the software-defined-vehicle that is managed and deployed by Pulumi.

{{< youtube "MKklVdn0LwE?rel=0" >}}

## Designed for Scale

As one of the leading luxury vehicle manufacturers, BMW operates at a scale that naturally brings complexity to the infrastructure and development processes. They needed to architect a toolchain including Gerrit that can scale to more than 11,000 developers and 100,000 builds a day while heavily utilizing Kubernetes across AWS and two on-premises OpenStack regions.
The solution also needed to be highly available across all three regions and have a hot failover ready in AWS for disaster recovery purposes. The architecture was designed for autoscaling to dynamically grow or shrink with needs over time to ensure readiness at all times. The criticality of this platform requires that a DevOps team is available and on-call 24/7.

## Pulumi for Deployment

The requirements for scale and the highly available nature created challenges for BMW on how to define and manage these infrastructure components. The platform required the careful configuration and deployment of more than 20 individual tools. The desire for standardization and consistency drove BMW/BearingPoint to select Pulumi for their deployments.
As the core of the platform is based around Gerrit on Kubernetes, Pulumi is being utilized for deployment of all of the Kubernetes components as well as the authorization policies, ConfigMaps and secrets, services, and StatefulSets. Pulumi makes it simple to generate random secrets and layer them into the configuration to support the secure interaction between the regions and Gerrit instances.
The multi-site Gerrit implementation also required AWS Kinesis and DynamoDB for cross-region synchronization. These components are defined and configured with Pulumi and automatically pull in the required randomly generated secrets. Both of these components are critical to scaling out Gerrit and have been designed with Pulumi to autoscale as needed.
The infrastructure as code and configuration is being continually validated by Pulumi’s policy as code. This means that every change that is defined and implemented has gone through their custom policies for standardization, security, and compliance.

## How Pulumi is Changing the Game for BMW

Pulumi enables BMW to abstract the complexity of numerous software development tools and a hybrid cloud infrastructure down to a standardized and repeatable approach. Pulumi provides the framework to enforce policy across all changes to ensure that compliance is never left behind. As the needs for highly connected automobiles and their software continue to grow, BMW can rely on the highly scalable automated infrastructure deployed by Pulumi.
