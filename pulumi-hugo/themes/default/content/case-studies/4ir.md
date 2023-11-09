---
title_tag: Modernizing Manufacturing with 4IR and Pulumi | Case Studies
title: "Case Study: Modernizing Manufacturing with 4IR and Pulumi"
description: |
    4IR uses Pulumi to reduce infrastructure deployment times, up-skill its team, and accelerate time to market.
    
meta_desc: Learn how 4IR worked with Pulumi to cut deployment time from days to hours and saved $75k annually on outsourcing costs.

customer_name: 4IR
customer_logo: /logos/customers/4ir.png
customer_url: https://www.4ir.cloud/

hide_pulumi_footer: true

---

> ***“Pulumi has emerged as a key element in our strategy, creating tangible value for us by reducing infrastructure deployment time, up-skilling our team, and accelerating our time to market.”*** - *Joseph Dolivo, CTO, 4IR Solutions*

##### Learn how [4IR]((https://www.4ir.cloud/)) leveraged Pulumi to:

- Cut deployment time from days to hours
- Bring IaC in-house, saving $75,000/year on outsourcing costs
- Deliver an MVP 4 weeks earlier than scheduled

## Background

While technology and IT companies have been benefiting from cloud technologies for years, some industries, like manufacturing, have been slower to realize many of the benefits offered by modern cloud solutions.

Manufacturing veterans are currently experiencing an "IT-OT Convergence." Companies are integrating more traditional IT technologies, like IP-based solutions, into classic Operational Technology (OT) systems, that have typically used proprietary protocols, onto their factory floors. This shift has naturally extended to software as well, where Windows still dominates. Spurred in part by the global pandemic, manufacturers are advancing their digital transformations and urging suppliers to adopt modern, open technologies.

While this trend continues to accelerate, a large skill gap remains. [4IR Solutions](https://www.4ir.cloud/) was founded with the mission to fill this gap, by using the best tools and practices from the IT industry to operate OT infrastructure for manufacturers at scale. With its FactoryStack™ and PharmaStack™ products, 4IR offers infrastructure and "DevOps-as-a-Service" to manufacturers, taking care of provisioning and operations including backup, upgrades, security services, secrets management, and CI/CD pipelines for OT software.

<img class="block mx-auto md:max-w-4xl my-8"
src="/images/case-studies/4ir-factorystack.png" alt="FactoryStack architecture diagram">

## Selecting Pulumi and its Business Impact

Before developing FactoryStack™, 4IR examined the existing landscape of Infrastructure as Code (IaC) tools. “We considered Terraform, but as a team of programmers, we were not excited to learn a new configuration language that relies on quirky workarounds for common constructs like loops,” said Joseph Dolivo, CTO of 4IR. “We also evaluated Ansible, which seemed better suited for configuration management, and CloudFormation, which only worked for AWS,” shared Dolivo.

4IR eventually discovered Pulumi via Hacker News. Since Pulumi supports TypeScript and its vast ecosystem, it enabled 4IR’s experienced programmers to hit the ground running on Day One. The 4IR engineering team wasn’t worried about getting locked into a proprietary platform with expensive monthly bills, since Pulumi embraces Open Source and offers support for self-hosted backends.

Pulumi quickly became a fan-favorite among 4IR’s team and offered immediate business value:

- Deployment time for customer infrastructure was cut from days to hours using Pulumi-powered automation.
- 4IR brought Infrastructure as Code in-house, up-skilling its team and saving an estimated $75,000 per year on outsourcing costs.
- 4IR delivered an MVP four weeks earlier than planned, due to its engineers not having to learn a new configuration language and toolset.

### Growing with Pulumi

4IR's initial MVP release was built on AWS, using the ECS module provided by Pulumi. As 4IR's customer base grew and attracted larger manufacturers, many of them had existing relationships and cloud spend agreements with Microsoft Azure.

To support these larger customers, the 4IR engineering team decided to adapt their solution to support multiple clouds and chose Kubernetes as a key enabling technology.

### Going Multi-Cloud with Kubernetes

Adopting Kubernetes was not an easy decision. Although cloud provider-managed offerings like AKS and EKS reduce required maintenance considerably, Kubernetes is still an advanced technology that requires specialized skill sets.

4IR created three projects. The first project provides the Kubernetes application layer, which uses Pulumi's Kubernetes provider and is written to be cloud agnostic. The second project is an AWS-specific layer which operates resources such as VPCs, EKS, and PostgreSQL on RDS. The third project is similar to the second, except that it is specific to Azure, and runs similar services, such as VNETs, AKS, and Azure Database for PostgreSQL. In short, both the AWS and Azure projects run the core compute, database, and networking infrastructure primitives, while the Kubernetes layer deploys Kubernetes applications across either cloud.

<img class="block mx-auto md:max-w-4xl my-8"
src="/images/case-studies/4ir-multicloud.png" alt="Multi-cloud architecture diagram with Apps on Azure Native and AWS Classic">

### Supporting Hybrid Cloud with Components

Manufacturers in regulated industries such as pharmaceuticals and nuclear energy often have strict data residency requirements. While these requirements can sometimes be met by limiting deployments to specific cloud regions, many manufacturers insist that their critical workloads are run on-premise.

4IR realized that in order to operate on-premise, certain cloud-native services, such as managed databases would not be available to them. They needed a way to selectively deploy parts of their infrastructure customized to their hosting environment.  Pulumi's Component Resources turned out to be the perfect solution.

<img class="block mx-auto md:max-w-4xl my-8"
src="/images/case-studies/4ir-pulumi-components.png" alt="Architecture diagram using Pulumi Components">

4IR created new Pulumi Components that the other projects would be able to selectively import from, depending on the environment into which they were deployed. Since 4IR’s engineering team programmed in TypeScript, they used an internal npm repository to store these packages.

<img class="block mx-auto md:max-w-4xl my-8"
src="/images/case-studies/4ir-react-code-sample.png" alt="Code snippet for FactoryStack Designer React application">

With this solution in hand, 4IR was able to make customizing their solutions even simpler.  “We created a front-end React application that we coined FactoryStack™ Designer. It provides a "drag-and-drop" interface to configure a customer's environment,” shared Dolivo. “The application, like all of our Pulumi code, is written in TypeScript. It can import interfaces from our Pulumi Components and keeps the front-end in sync with our Pulumi code. In the future, we plan for this application to integrate even more seamlessly with Pulumi via the Automation API.”

<img class="block mx-auto md:max-w-4xl my-8"
src="/images/case-studies/4ir-designer-screenshot-1.png" alt="Screenshot of FactoryStack Designer showing drag and drop interface">

### Over the Edge

In some cases, manufacturers may not require nor have the budget for a hybrid cloud solution.  In addition, they may be located in parts of the world where Internet access is limited. 4IR expects that some hardware needs to exist on-site to allow for control of equipment and buffering of data if connectivity is intermittent. Previously, 4IR has deferred the management of this on premise hardware and software to their end customers.

With their current environment well in hand, the next frontier for 4IR is tackling hardware fleet management. Several tools exist that perform remote updates and deployments of containerized applications at the Edge, often by targeting a runtime container directly. While Dolivo’s engineering team is still evaluating their preferred tool, they have complete confidence that Pulumi's Docker package will [play a key role in their coming solution](/blog/pulumi-and-docker-development-to-production/).

## Summary

Pulumi has worked with 4IR from prototype to production, with multiple enhancements along the way. “Pulumi has emerged as a key element in our strategy, creating tangible value for us by reducing infrastructure deployment time, up-skilling our team, and accelerating our time to market,” said Dolivo.

While the Infrastructure as Code landscape continues to evolve, Pulumi's recent [re-commitment to Open Source](/blog/pulumi-hearts-opensource/) gives Dolivo and his team confidence that they have selected the right technology partner to carry them through to their next big milestone and beyond.
