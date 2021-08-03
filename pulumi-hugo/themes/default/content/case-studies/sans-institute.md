---
title: SANS Institute
description: |
    The DevOps team at SANS Institute, which provides cybersecurity training & certification, uses Pulumi to streamline delivering applications and infrastructure.
meta_desc: |
    The DevOps team at SANS Institute, which provides cybersecurity training & certification, uses Pulumi to streamline delivering applications and infrastructure.

customer_name: SANS Institute
customer_logo: /logos/customers/sans-wordmark.svg
customer_url: https://www.sans.org/

exec_summary: |
    The DevOps team at SANS Institute, which provides cybersecurity training and certification, uses Pulumi to streamline delivering applications and infrastructure through CI/CD processes for many business units at SANS. By using Pulumi, the organization was able to adopt cloud engineering practices that enabled it to reduce deployment times by 70%. SANS increased delivery speed, quality, and consistency by using cloud engineering practices such as building infrastructure as code using general purpose languages and software tools, and deploying cloud applications with Git and automated delivery pipelines.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: About SANS Institute
      anchor: about-sans-institute
    - label: Bringing Cloud Engineering to SANS
      anchor: bringing-cloud-engineering-to-sans
    - label: Streamlining Cloud Application Delivery
      anchor: streamlining-cloud-application-delivery
    - label: The Result
      anchor: the-result
    - label: Summary
      anchor: summary
---

## About SANS Institute

Founded in 1989, SANS Institute is the global leader in cybersecurity training. Its mission is to empower cybersecurity professionals with the practical skills and knowledge they need to make the world a safer place. To that end, SANS offers foundational training, degree programs, GIAC (Global Information Assurance Certification) certifications, and cyber ranges—platforms that provide hands-on cybersecurity practice.

## Bringing Cloud Engineering to SANS

Tyler Mulligan and Chris Klewin are Senior DevOps Engineers at SANS. With an “automate everything” attitude, they specialize in building infrastructure as code, CI/CD pipelines that use GitFlow, and pre-production environments such as developer sandboxes. Their goal is to ensure that SANS developers use consistent processes from development to production.

Tyler and Chris realized that SANS needed a better and more efficient way to build, deploy, and manage its cloud applications and infrastructure after the COVID-19 pandemic hit. With a  weakened economy looming, SANS leadership asked them to behave more like a startup—move faster while using fewer resources.

This goal would be difficult to achieve using SANS’ existing tools and practices. Their most recent application used a microservices architecture with a front-end application. The application used 12 Git repositories (one for each stack) that they versioned and deployed together. There were interdependencies across stacks that complicated matters. They managed the entire application with a combination of tools stitched together: Legacy Infrastructure as Code tools like AWS CloudFormation and Terraform, AWS Lambda functions, and Bash scripts. Tyler and Chris needed a cleaner solution built for the modern cloud that would be more scalable and easier to manage.

“Pulumi was an option that we looked at, and we found that it was pretty easy to get started,” Tyler said. “As the work progressed, we saw that using general-purpose programming languages (in their case, TypeScript) to express our infrastructure resources yielded noticeable improvements. Plus, Pulumi’s state dependency management was a natural fit.”

Using the lessons learned from this application, they looked around SANS for new challenges where they and Pulumi could help.

## Streamlining Cloud Application Delivery

Tyler and Chris began to work with the SANS Labs business unit, which is responsible for delivering in-depth labs where students can apply their training in a cyber-range environment. For example, SANS Labs’ NetWars game servers work in tandem with local virtual machines that students run to solve various security problems.

When Tyler and Chris talked to the SANS Labs team, they found that many of their pain points centered around the deployment process for game servers. When they investigated, they found that, as with their first project, the technology stack was comprised of many different tools that  held the CI/CD pipelines together.

“To provide students with a virtual training environment, SANS instructors needed a way to spin up ephemeral Amazon EC2 instances and related resources that host the environment,” Chris explained. “The instructors needed to send a request to the ops team, who would spin up the infrastructure using a semi-automated process operated through Jira tickets and Rundeck. That platform kicked off Bash scripts, and those kicked off another tool that ran still other scripts that made commits to Git to do all of this.”

Tyler and Chris wanted to significantly simplify this architecture by eliminating the manual steps and the need for gluing together multiple provisioning and scripting tools. To do this, they used Pulumi to build a self-service platform (called the “game server service”) that enables instructors to quickly provision virtual learning environments using a fast and automated process. The game server service can automatically deploy, configure, and destroy approved infrastructure with best practices baked-in from SANS security and operations teams, eliminating the need for a manual ticketing process. To enable this automation, they used [Pulumi's Automation API]({{< relref "/docs/guides/automation-api" >}}), which exposes the full power of infrastructure as code through a programmatic interface, instead of through CLI commands. Using the Automation API, they deployed TypeScript code that runs Pulumi in a Node.js container and built a REST API around it. The container can create, update, configure, and destroy infrastructure dynamically through API calls.

“The Pulumi Automation API made [deploying the application and its infrastructure] a much cleaner process,” Tyler said. “With the old architecture, it was much more manual, stitched together with bash scripts, and then wrapped in another tool with its DSL.”

### The game server service architecture

Here is a high-level diagram of the game server service used by SANS Labs.

<img class="block mx-auto md:max-w-4xl my-8"
src="/images/case-studies/sans-game-server-diagram.png" alt="SANS Game Server">

The architecture uses a GitHub-centric approach. All cloud resources are deployed with Pulumi via CI/CD pipelines.

Essentially, the architecture converts REST API calls made by instructors into CloudWatch events. When events are published, it triggers the game server builder to deploy and configure the infrastructure. It does this by calling a Node.js container running Pulumi (via the Automation API), which pulls in the game server factory to build the dynamic configuration, using the information from the incoming API request. That turns into an event to spin up a specific game server with those parameters, using an AMI provided by the instructor. The game server also uses some shared assets stored as persistent data in S3.

### Leveraging software engineering to improve code and project quality

Chris and Tyler both felt that using general purpose programming languages for infrastructure made code quality much better across all projects.

“We have very strong opinions about code,” Tyler said. “With a standard programming language, we can take advantage of other products in the ecosystem, such as Prettier and ESLint. When we look at legacy projects built with many other tools and bash scripts, you can tell multiple people had their hands on the code. The code our team writes is clean and uniform.”

### Using a GitOps strategy for deploying infrastructure and applications

Tyler and Chris implemented a GitOps strategy for automating the building, testing, and deploying of applications and infrastructure when a Git commit is made. They accomplished this by using Pulumi to deploy to three different AWS accounts for each environment. There’s an account for the sandbox environment, one for the development environment, and one for production. For the sandbox, they use Pulumi locally to deploy to that environment manually. For the other two environments, they use pipelines and GitFlow-based deployments. When a pull request passes CI tests and is merged into the develop branch, it is deployed to the development environment.  Likewise, when a release branch is merged into the master branch, a release is created, and it is deployed to the production environment.

Chris added, “We’re using a polyrepo, in case that isn't apparent. We have a repository for each sort of responsibility. We have a single Git repository for shared infrastructure, another for the REST API service, another one for the factory, and so on. We try to segregate the logic based on repositories.”

This diagram shows the code promotion workflow, where developers develop different projects and deploy them to the sandbox environments.

<img class="block mx-auto md:max-w-4xl my-8"
src="/images/case-studies/sans-code-promotion-diagram.png" alt="SANS Institute Code Promotion">

### Enforcing security and best practices with Pulumi

Because students are taught to hack systems, it’s important that they don’t turn their talents on the SANS infrastructure itself. To ensure that their infrastructure is secure, Tyler and Chris use a variety of methods. One is Pulumi’s [Policy as Code]({{< relref "/crossguard" >}}) framework that lets them enforce compliance for cloud resources. Additionally, they took advantage of [Pulumi's collection of libraries]({{< relref "/crosswalk/aws" >}}) that model AWS infrastructure patterns using well-architected best practices. This allows them to use default configurations for resources such as Amazon CloudWatch Alarms, CloudWatch Metrics, and CloudWatch Dashboards.

They’ve also begun developing their own SANS policy pack to verify that resources are spun up according to SANS standards, such as ensuring that Amazon S3 buckets are always encrypted and closed to public access. In addition, Tyler and Chris are currently working on improving the monitoring service. That service will monitor the resources being spun up and send some default CloudWatch alarms, metrics, dashboards and log metric filters, again using Pulumi Crosswalk.

## The Result

Using Pulumi, Chris and Tyler greatly simplified the SANS Labs architecture and created a better user experience for SANS Labs instructors and students. Now, instructors can more easily and quickly provision virtual environments because they reduced deployment times from around 10 minutes down to 3 to 5 minutes. In the future, Chris and Tyler plan to use Pulumi and [cloud engineering best practices]({{< relref "/cloud-engineering" >}}) to help other business units modernize their practices and tools, such as the GIAC certification unit.

## Summary

Here is a summary of how Pulumi helped the DevOps team at SANS:

- Reduced deployment times for the game servers by up to 70%
- Simplified their deployment process by eliminating the need to “glue together” several infrastructure as code tools, scripts, and functions, and it removed a manual ticketing step
- Enabled developers to use familiar programming languages and tools, which also helped make their code cleaner and more uniform, resulting in streamlined pipelines
- Helped to identify opportunities in other SANS departments where Pulumi can streamline operations
