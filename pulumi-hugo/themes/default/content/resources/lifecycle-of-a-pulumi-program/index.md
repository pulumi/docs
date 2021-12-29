---
# Name of the webinar.
title: "Lifecycle of a Pulumi Program"
meta_desc: In this talk, you will learn how Apple leveraged a custom state backend with SSO, RBAC, and pipelines powered by the Pulumi Automation API to drive IaC.

cloud_engineering_summit:
    track: manage

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars
layout: cloud-engineering-summit-replay

# External webinars will link to an external page instead of a webinar
# landing/registration page. If the webinar is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the webinar page created.
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "lifecycle-of-a-pulumi-program"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Lifecycle of a Pulumi Program"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Lifecycle of a Pulumi Program"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/5U7q9miKWj0"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T15:00:00-07:00
    # Duration of the webinar.
    duration: "24 minutes"
    # Description of the webinar.
    description: |
        Infrastructure as Code provides a way for teams and companies to standardize the way they manage and secure applications. In this talk, Fariba Khan and Stephen Van Gordon will share how they leverage a custom state backend with SSO, RBAC, and programmatically configurable pipelines powered by CICD tooling and the Pulumi Automation API to drive IaC at Apple.

        This framework of tools enables teams to provision secure-by-default Compute, Storage, Identity, Ingress, and other components available in multiple languages in very little time and without any manual interventions. This experience is complemented by operations-friendly workflows previewing infrastructure changes between deployments, as well as cost and policy violations directly in Github comments. This results in reduced cognitive overhead when making changes to a deployment. Finally, by providing the state store for IaC stacks our team gains insight into usage patterns, security issues, and compliance via rich data and analytics.

    # The webinar presenters
    presenters:
        - name: Fariba Khan
          role: Engineer, Cloud Services, Apple
        - name: Stephen Van Gordon
          role: Engineer, Cloud Services, Apple

# This section contains the transcript for a video. It is optional.
transcript: |
    My name is Stephen. My colleague Fariba and I are excited to talk about the work our team at Apple has been doing using Pulumi. Here's what we're going to talk about today. First, we will share a little about our team at Apple Cloud Services. Then, we will discuss some of the challenges to maintaining engineer velocity when working in the cloud.

    Next, we will talk about some of the foundations that we provide to help teams be productive on their cloud engineering journey. Then, to make things concrete, we will look at a case study of a few Pulumi programs that bring up a service managed by a small team. That service also happens to be our state backend. Finally, we will share a few recommendations, based on our experiences. Fariba and I are members of the Hybrid Cloud Engineering Team, a part of Apple Cloud Services.

    Apple Cloud Services builds managed services, first party cloud resources, bill automation tools and developer experience products for Apple engineers. Basically, we focus on taking the complexity out of the cloud. We use infrastructure as code principles to increase engineering velocity and help Apple engineers follow security and cloud engineering best practices. Next, we'll talk about some of the challenges to maintaining engineer velocity while working in the cloud. Based on our experience, we saw that teams were encountering similar sets of challenges on their cloud engineering journeys.

    When resources are fragmented across many different cloud providers and types of resources, the number of tools and interfaces that engineers must learn increases exponentially. Velocity is increased with repeatable processes, without any one-offs or bespoke infrastructure, which fragmentation doesn't allow. We want to treat our stacks and resources as interchangeable. We strive for ephemeral stacks and environments. We want to be able to bring up and tear down stacks and environments without side effects.

    Security is hard and infrastructure is hard. And putting the two things together is harder. There's a lot that people need to do to make the infrastructure secure. But they also need to know how to make their infrastructure secure. This becomes harder with fragmentation, when engineers are working across different interfaces.

    As the number of stacks increases, and as the relationships between them becomes more complex, we need tools to manage these relationships. This touches on repeatability. We want engineers to be able to drive updates from CICD. It also touches on fragmentation. We don't want engineers to have to cobble together a disk script's set of scripts in YAML, for making critical production changes.

    And when engineers are making that critical production change, they want to be confident that their change is not going to have any side effects or break something unexpectedly. We don't want teams to be in a situation where there's a risk that a small, one line config change could bring down a production cluster. Best practices are not always documented. And there are rarely trivial to implement. It's difficult enough to learn a single cloud ecosystem.

    As we work across multiple cloud providers, the problem only becomes pronounced. Our team wants to enable engineers to run their infrastructure without having to be an expert in everything. Now let's look at an example of some of these challenges in practice. Think of a typical scenario for a service having to rotate its enterprise DNS load balancer certificate. This is critical to keep the service not only secure, but live.

    If the certificate is short-lived, frequent rotation becomes a maintenance burden. If the certificate is long lived, it is easier to forget when it has to be rotated. If the certificate is mis-configured or expired, the service will go down. Speaking from personal experience, this is something that you can keep you up at night. Certificate rotation should be simple, but it can easily involve a number of complex steps.

    An engineer might need to go to a dashboard, create another certificate, and then make sure the new certificate has the correct properties to match what's running in production. For example, SAN DNS name. Then the engineer must upload the certificate as a Kubernetes secret and wait for redeployment. Throughout this process, if a mistake has been made, even a simple typo, it brings the service down. With the tools and automation we have set up using Pulumi, the program and the pipeline automates this to be risk and toil free.

    Fariba will talk about this workflow in more detail later on. But first, let's go through the foundations of our ecosystem. These are what we consider the foundations for maintaining engineer velocity. Our team has built higher order components for common patterns. We've brought first party cloud resources under Pulumi management.

    And we also provide templates of common resource patterns as a starting point for Apple engineers. We publish policy packs that reduce the cognitive load of following best practices and helps teams follow security guidelines. Now, while there are published SDKs and policy packs solve so some of the problems within a stack, like repeatability, we need tools to help bring together different stacks. The Pulumi automation API has turned out to be a powerful tool for a team to orchestrate engineer workflows. Both for program development and for CI/CD environments and production pipelines.

    As teams grow their portfolio of resources and services, we've found it is important to think deeply about how to design and architect programs and stats. Let's take a closer look at these foundations, starting with the SDK. Our SDK contains security reviewed and production-ready cloud resources. Examples include security-compliant multi-region object storage buckets, or Kubernetes clusters. The components our team has built has safe and sane defaults.

    Engineers don't need to learn the implementation details or become experts in a given cloud environment to follow best practices. These components also work together and can be reused and composed to create new components. Our multi-regional bucket, for example, is built from our teams bucket and bucket replication components. These components are also used as building blocks by other teams. For example, the Kubernetes cluster is used by other teams to build their own clusters tailored to their specific use cases.

    Another thing we've done with our SDK, is bring first party cloud resources under management by custom Pulumi resource providers. Within Apple, there is existing work on using Terraform providers to manage first party cloud resources. Our routine brought those resources into the Pulumi ecosystem. And we've also written new providers when needed. There's much existing tooling around integrating Terraform providers into Pulumi, and we've used that to build upon.

    We use TF bridge to generate the language SDKs, and we use the existing Pulumi tools to generate documentation. Some of the resources that teams are now able to manage using Pulumi include global server load balancers and enterprise certificates. This allows Apple engineers to use our SDK's to manage both their first-party and third-party cloud resources using Pulumi. There's a single interface for managing these resources. Engineers now have a repeatable and safe process for updates.

    Teams are able to manage more resources and we are able to support our teams. We provide a set of starting examples for Apple engineers, which we've made available to teams through the Pulumi new command. Engineers can quickly get up and running on Pulumi, or quickly get a piece of infrastructure up and running. For example, we provide a template with an Apple Kubernetes cluster that is available both in Python and TypeScript. You can go from zero to a real life case cluster in 30 minutes, which I think is pretty cool.

    We also provide multi-stack examples as reference implementations for orchestration of complex resources. Providing these templates reduces the cognitive burden for learning a new resource or provider, enables us to scale out and support more teams and helps disseminate best practices. The hybrid cloud team has created policy packs that we distribute to Apple engineers. The SDKs are secured by default, but they cannot validate runtime usage. The policy packs provide checks and balances for stacks at runtime.

    One thing we do differently is making policy packs available through internal NTM registries. This provides a central place for internal Apple engineers to share and contribute to policy packs. There's a few examples here. The cost estimate policy provides an estimate of the cost of the cloud resources in the stack. Engineers can see if an update would cause a major shift in resource usage and teams can avoid surprises if something is going to cost more than they thought.

    There's also the object storage policy, which checks that storage buckets follow best practices and the end config policy, which sanity checks an engineer's environment for repeatability of updates. These are building blocks our team provides for infrastructure provisioning. They can do a lot to help engineers with the management of their resources in their stacks. But the truth is, in the real world, we work with projects that are more than just individual pieces of infrastructure, or even just individual stacks. Teams need to orchestrate these stacks.

    You need to have deployment strategies and they need to have testing strategies. To talk more about the tooling that we use to help manage these challenges, Fariba is going to take a look at a complex service that we've brought up. Thank you, Stephen. And hello everyone. I'm Fariba.

    I'll share our teams, how we share programs, stack and pipeline design principles, and walk through our usage of the tool built with Pulumi automation API through this service. This is our state and policy manage backend architecture. We deploy hybrid cloud service with the cloud SDKs we have built in-house using components from the TypeScript SDK and applying on first party and third party cloud across two regions. We run in an active standby configuration. Our goal is to automate everything so that we are able to bring up an ephemeral environment for testing at any time.

    That meant we couldn't have one-offs in our programs, or stack design. And we had to have repeatability across regions and deployment environments. We had to develop our testing and promotion strategy, consider safe database schema migrations, and manage Kubernetes and data store life cycles. Based on this experience, our team developed set of recommendations for program stack and pipeline design. And built a tool for Apple engineers with Pulumi automation API, to make this a lean continuous deployment process.

    Let's go through these recommendations and see how we apply those to our service. Our think team came up with a few strategies that added to develop our productivity related to designing Pulumi programs. The first recommendation is: Group things with a similar life cycle together. If the service architecture has both resources that are frequently updated and that are rarely updated, they should be grouped into programs accordingly. This reduces the blast radius if an update goes in an unexpected way.

    For example, our team recommends that Kubernetes clusters with infrequent updates and Kubernetes deployments with frequent updates recite in separate programs. Otherwise they'll create toil and risk, as the stack is regularly updated for deployments. When we group resources with similar life cycles, we know that an update could only have affected a certain subset of the infrastructure, which makes it easier to reason about things. Grouping resources with similar life cycles results in more meaningful diffs. Core changes are targeted to a specific part of the infrastructure with a quieter diff and fewer resources in it, it makes it easier to understand what the changes actually are.

    This also provides more confidence when doing an update. Engineers don't have to scan each diff to make sure that they're only making the changes they intend to. And related to this, use stack references. The stack outputs and references should build an explicit contract between stacks. For example, a par-q fake reference in a deployment program as an output of a Kubernetes cluster program.

    Let's see how we applied these to Hybrid Cloud Service programs. The first program provisions are global load balancer, object store, and certificates. So it's fairly rarely updated. The outputs of this program are referenced in many other programs. The structure of data store has an active passive configuration.

    So we decided to put it in its own program. A Kubernetes cluster has a slightly different life cycle. We rotate the images pretty aggressively for security reasons. The regional load balancer is its own program. This imports the regional endpoint domain names.

    The monitoring part for vector par-q and its cluster in a program and they depend on the Kubernetes program. And finally the service, which is updated the most frequently and depends on many of these components, is its own program. We also have a process for making safe schema changes to the data store as part of this service program. We recommend to make schema changes along with your deployments. So in this case, you wouldn't want to have a separate pipeline for this.

    Our team also has recommendations on how to create stacks from these programs. We mentioned earlier, we recommend stack references to pass information between stacks. Including the environment name in the stack name can provide a way to parameterize stack references. For example, a config variable can be used for environment and it can have values: dev test prod. Now to reference the dev data store, the stack reference can be to the stack dev dash data store.

    For resources that are region specific, we recommend to also encode the region. For our service, we also encode if it's a canary or a primary deployment. For hybrid cloud service, the GSLB and the data store have their own stacks. The regional load balancers, the Kubernetes clusters have separate stacks for each region. And the service has even more stacks with canary and primary in each region.

    Once teams have their programs and stacks, they actually have to think about how to orchestrate them in continuous deployment pipelines. We keep a linear relationship between stacks and deployment pipelines. A stack may have downstream dependent pipelines. If so, triggering a stack's update will trigger updates in all of its downstream pipelines. Trying to determine which pipeline needs to be triggered can be a challenge.

    The trick here is we do not try to determine whether an update is necessary in a downstream pipeline. If a pipeline is downstream from an updated stack, we'll always run an update in that stack. If there is no changes, it's a no-op. This simplifies the orchestration logic. For example, if the load balancer certificate is updated in a stack, the stack will trigger the downstream regional load balancer stack.

    But the load balancer end point does not change. So the downstream stack update will be a no-op. For hybrid cloud service, we have three production environments. So the set of stacks are repeated in each of them. We have a pipeline for each stack for each of these environments.

    That means we have 40 stacks for one service and same number of build pipelines. That's a lot of stacks to configure in a build environment. Our team has a solution for that. Enter Pulumi automation API. Our team has built a tool with the Pulumi automation API to help Apple engineers manage the life cycle of their stacks.

    Apple engineers can point the tool at a source repository. With the Pulumi project, provide it some conflicts and it will run through a planned Pulumi update. For example, in the sample conflict file here, we have few parameters. The refresh stack would make sure that there is no drift in this stack before any update is run. The previous stack option will enable Pulumi preview and corresponding pull request commands for the update.

    And after update, it will run updates again with the expect no changes option to ensure that the code and the stack are stable. The automation API allows us to use code to define things like the exact sequence of Pulumi steps to be run, and config and environment variables to set. Taking the person out of the loop at runtime helps ensure repeatable builds. Using the API, we also post the results of an update back to the PR. Internally, the team uses the same tool for automation.

    This tool makes it easier for us to support Apple engineers. Because they're using the same set of build tools as everyone else. We also use the automation API to drive testing of our SDKs and examples. And a fun little aside, because the service we are running is a state backend. The automation API also drives the acceptance test of our own service.

    Let's look at the developer workflow for updating resources with this. First, the Apple engineer raises a PR to make changes to the program. This is a simple change as seen in the diff ruling the version of the service forward. The PR triggers a pull request build. The pull request build is cycle initialized a Pulumi preview.

    With the preview, the hybrid cloud service gets the new state file with the corresponding proposed changes along with policy pack reports. This diff and the policy pack reports are posted back to the source code repository as a PR comment. Now the team members can review this along with code changes. Not only that, the reviewer also gets an update that resources for other programs like the global load balancer, the monitoring pods and the Kubernetes cluster resources have not changed. This builds confidence in fearless deployments.

    The PR merge pipeline finally triggers the changes reviewed by the team and the resource changes are provisioned in cloud providers. Now let's see how the hybrid cloud team takes this all to production environment. Each environment it's tied to its own gate branch and every change that could eventually end up in production has to always go through the previous environments. Whenever we want to change something, we create a branch off of the diff branch, we do our work and open a pull request. The pull request triggers the corresponding diff branch pipeline.

    As we saw in the deployment workflow. Let's look at the case through writing certs in the global load balancer, object store and certificate program. After the diff she has seen that the stack runs all the top pipelines, depending on this will be triggered. And you remember, there were plenty. The GSLB program is the one that almost every other program is referring to through stack references.

    But the good thing is each deployment goes through a validation test. Once the test passes, the next pipeline is triggered. If the test fails, for some reason, the changes are not propagated anymore. For example, here, if the GSLB stack failed, other pipelines will not be triggered. The incorporation of the validation test to be part of the pipeline has been a big automation gain for us.

    We recommend this highly. The service deployments are also triggered in order. If the diff service in canary, in region one failed validation, the other service pipelines would not get triggered. To get these changes to test, we have a promotion pipeline that merges the diff branch to the test branch. And then the test pipelines can be triggered.

    With validation in both regions in diff, there's confidence to promote this to test and then to production. To get to production, we use another pipeline to merge test to prod. While this process may take time with Pulumi refresh, previews, updates, long PRB build times, it's worth it, because we are confident through our repeatable DevOps process. To wrap up, let's summarize some of the learnings we had in infrastructure as code. We suggest making an explicit goal for building ephemeral environments and identify automation opportunities.

    Build best practice components according to the needs of your organization. Encode environment name in stack name. This is a big value add to recognize what environment and stack is impacting just for the clients. Group resources with similar life cycle in a stack to reduce blast radius and have meaningful diffs. This is a big developer velocity gain.

    Define stack contracts with outputs and references. Our team highly recommends the Pulumi automation API for CICD. And finally, avoid one-off items to make your programs and pipelines uniform. For example, we didn't have to have two regions for our dev environment. But this allowed us to have uniformity in programs and pipelines across dev and production environment. That wraps up our presentation. On behalf of our team at Apple, Stephen and I thank you for listening in.
---
