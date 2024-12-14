---
title_tag: Starburst | Case Studies
title: "Starburst:  112x Deployment Acceleration"
description: |
    Starburst transformed its infrastructure provisioning and management processes by switching from Terraform to Pulumi, resulting in a 112x faster deployment time and significant cost savings.
meta_desc: Starburst switched from Terraform to Pulumi, achieving 112x faster deployments, enhanced developer productivity, improved security, and cost savings.

customer_name: Starburst
customer_logo: /logos/customers/starburst.png

exec_summary: |
    Starburst, a leading data analytics company, transformed its infrastructure provisioning and management processes by switching from Terraform to Pulumi. The adoption of Pulumi resulted in a 112x faster deployment time, reducing infrastructure deployments from 2 weeks to just 3 hours. Pulumi's object-oriented programming support enabled the creation of abstractions for Kubernetes clusters and managed services across Azure, AWS, and Google Cloud. The transition to Pulumi Cloud provided access to deployments, dashboarding, analytics, state management, and security functionality, further enhancing Starburst's ability to innovate and grow their business rapidly. With Pulumi, Starburst achieved significant improvements in developer productivity, security, governance, and cost savings, positioning the company for continued success in the data analytics industry.

quote_block:
  quote: |
      "When we did it with Terraform, it took two weeks to do [infrastructure deployments]. Now we do it in about three hours a day. So that's how much of an improvement Pulumi gave us on our deployment time."
  quote_attrib: Matt Stephenson, Senior Principal Software Engineer
  headline_stat: Three hour
  headline: Deployments reduced from two weeks

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: Challenges
      anchor: infrastructure-as-code-scaling-challenges
    - label: Full Self-service
      anchor: full-infrastructure-self-service
    - label: Return to Pulumi Cloud
      anchor: return-to-pulumi-cloud
    - label: Conclusion
      anchor: conclusion
---


## About Starburst

Starburst is a data analytics company that provides data lake solutions. It is trusted by companies like Apache Corporation, Comcast, Doordash, DBS Bank, and VMware, and it has raised over $400M from Index Ventures, Coatue, Andreessen Horowitz, and Alkeon Capital. Starburst Galaxy is a fully managed Trino data lake service available across 22 regions worldwide on AWS, Azure, and GCP. The Galaxy control and data plane services run across 50-60 Kubernetes (K8s) clusters. The control plane mainly runs on Amazon Elastic Kubernetes Service (EKS) clusters while the data plane services run on the managed K8s services in each region of each cloud that Galaxy is available.

The Starburst platform team managed all the infrastructure across Starburst. The Galaxy service team builds, deploys, and operates the Galaxy service atop the infrastructure provided by the platform team. The Galaxy service is built using the Java Airlift framework, which is a framework for building REST services in Java. Each Airlift application runs as a service on a K8s cluster.

## Infrastructure as Code Scaling Challenges

Starburst previously used Terraform as its infrastructure as code (IaC) solution to provision and manage the Galaxy infrastructure. But Terraform presented many challenges for Starburst that drastically reduced its delivery velocity, ability to scale, and developer productivity.

### Slow Delivery Velocity

Every Galaxy service deployment followed a blue-green approach, which required the creation of new K8s clusters and service deployments in every region and the deletion of the old K8s clusters. Every deployment with Terraform would take 2 weeks because there were many glue scripts and manual executions needed to run the deployment across every region.

### Scaling Limitations

It was hard to automate build pipelines (e.g., GitHub Actions) using Terraform, which meant infrastructure orchestration and coordination was very manual and required a ton of fragile glue scripts. The manual nature of deployment made it very hard to scale out to new regions, limiting Starburst’s market growth. The other problem with Terraform was there was no easy way to create abstractions for different application stacks. Galaxy uses many different types of Kubernetes clusters with different configurations and shapes. Every cloud had different managed services that implemented common operations functions (e.g., autoscaling) differently. There was no easy way to create an abstraction that abstracted away the differences between the cloud because Terraform uses the Hashicorp Configuration Language which is a domain specific language and not a true programming language with access to object oriented programming primitives.

### Reduced Developer Productivity

Service team developers would file tickets to request new infrastructure from the platform team. Spinning up review and testing environments for every developer was a time consuming process that could take an hour. Developers didn’t have an easy way to self-service. While Terraform templates could handle the provisioning of the base infrastructure, there were configurations that needed to be added into each environment. There was no easy way to automate it through GitHub Actions.

## Full Infrastructure Self-service

Starburst needed a way to scale and ship software faster, so they decided to replace Terraform with Pulumi. Pulumi support for object-oriented programming languages like Java made it easy for Starburst to build abstractions for K8s clusters. They were able to create base clusters that could be easily configured based on the exact needs. They were able to create abstractions across the different K8s managed services across Azure, AWS, and Google Cloud, which allowed them to build generic functions for autoscaling, cluster version upgrades, creation and deletion of node groups, etc. All Pulumi programs managing Galaxy infrastructure were placed in a monorepo. All orchestration workflows like deployments were implemented in Automation API and executed through GitHub actions. Galaxy’s multi-region blue/green deployments, which previously took two weeks with Terraform, now take only three hours with Pulumi, a 112x improvement in speed. This acceleration is attributed to the ability to fully automate the infrastructure pipeline orchestration, eliminating the need for manual execution of glue scripts for every Terraform template.

Service team developers requested infrastructure just by modifying a list and making a pull request against the monorepo. The workflows executed through Automation API created all the infrastructure for a seamless self-service experience.

Starburst used Pulumi Cloud to manage the infrastructure state, however in 2023 management wanted to cut costs. Pulumi Cloud was dropped and Starburst had to create a DIY S3 backend to manage Pulumi state.

## Return to Pulumi Cloud

The switch off of Pulumi Cloud was shortlived because replacing all the rich functionality of Pulumi Cloud meant developing and maintaining another service. Managing the S3 state store and maintaining the code turned out to require more time than the platform team would have liked to prioritize. On average, it took 2 engineers one to two days a week. It came to be a tradeoff between building and maintaining all the features provided by Pulumi Cloud like state management, dashboarding, insights, deployments or working on new features for customers. The platform team adopted Pulumi Cloud because of the gains achieved in developer productivity, enhancements in security and governance, and cost savings.

### Developer Productivity Gains

Pulumi Cloud greatly increased developer productivity. With Pulumi Cloud, Starburst is planning to use Pulumi Deployments and replace executing Automation API through GitHub Actions. Previously, Starburst had started to use Spot instances in its GitHub Actions, which interrupted infrastructure updates when a Spot instance was lost. With Deployments, they will do all their application build work with Spot instances and then execute all the Pulumi code using Pulumi Deployments.

Previously, developers ran Galaxy locally on their laptop for testing and development as Docker containers. Running end to end tests in a Docker environment locally wasn’t scaling, so they wanted to be able to spin up a full stack in the cloud and have it torn down after the review was done or after a set period of time. With Pulumi Cloud, Starburst plans to utilize review and TTL stacks to spin up tests for every commit. Without Pulumi Deployments, this used to take an hour to spin up the testing environment, and with Deployments the time will drop to half.

Starburst also found Pulumi AI to be a game-changer in terms of productivity. The platform team rewrote all their provisioning code for AWS VPCs and EKS clusters. Instead of spending weeks digging through API documentation, Pulumi AI provided contextual descriptions and code examples, allowing developers to rewrite their provisioning code in a matter of days.

### Security and Governance Enhancements

With Pulumi Cloud's drift detection feature, Starburst could proactively identify and address manual changes to their infrastructure, preventing potential issues and ensuring consistent deployments. For example, someone on-call might make a manual change which could break the next release. With drift detection, an alert will happen, allowing the drift to be remediated without breaking future releases.

Starburst also plans to use Pulumi ESC (Environments, Secrets, and Configuration).  Previously, each developer environment required manual configuration and copying of keys from AWS Key Management Service (KMS), which was a slow and potentially insecure process. With ESC, each developer environment can securely pull credentials and configurations from a centralized location, significantly improving security and efficiency. ESC also enables dynamic credential management, further enhancing security by eliminating the need to share static credentials across environments.

### Cost Savings

Adopting Pulumi Cloud proved to be a cost-effective decision for Starburst. By leveraging Pulumi's visualization tools, the platform team could efficiently identify and decommission obsolete resources, recouping enough cost savings to cover the cost of Pulumi Cloud itself. Pulumi Cloud's proactive alerting system also notified the team of potential infrastructure issues, further contributing to cost optimization and risk mitigation.

Starburst will also realize significant cost savings through Pulumi Cloud’s review and TTL stacks. These features allow the company to spin up complete testing environments on-demand and have them automatically torn down after a set period or upon review completion. This eliminates the need for manual cleanup and ensures that resources are not left running unnecessarily, translating into cost savings.

## Conclusion

In conclusion, Starburst's adoption of Pulumi has transformed their infrastructure provisioning and management processes, significantly enhancing delivery velocity, scalability, and developer productivity. The transition from Terraform to Pulumi gave Starburst the ability to create easy to use abstractions and enabled full infrastructure automation and self-service, resulting in a remarkable 99% reduction in deployment time. The reinstatement of Pulumi Cloud gave Starburst access to deployments, dashboarding, analytics, state management, and security functionality that would have to otherwise be independently implemented and operated. Pulumi Cloud gives Starburst notable gains in developer productivity, security, and cost savings. Starburst would not be able to innovate and grow their business as fast without the Pulumi platform.

### Key Stats

* Previously, Terraform multi-region blue/green deployments took 2 weeks. With Pulumi, these deployments now take only 3 hours, which is 112 times faster than before. This significant improvement is because the infrastructure pipeline orchestration can be fully automated, eliminating the need for manually executing glue scripts.
* Testing environments are expected to be spun up 2 times faster by using Pulumi Deployments' TTL (Time-to-Live) stacks and Reviews stacks, allowing individual testing environments to be created for each developer.
* Pulumi AI accelerated development by a factor of 10. Starburst rewrote their AWS provisioning code, a task that would have taken a couple of months, in just a week or two, thanks to the power of Pulumi AI.
* Pulumi Cloud pays for itself through the savings achieved by identifying and shutting down unused infrastructure using Pulumi Insights and the Cloud dashboard.
