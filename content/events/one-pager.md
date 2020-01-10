---
title: Modern Infrastructure as Code
type: page
layout: event-one-pager
url: /show
noindex: true

meta_desc: Pulumi provides a cloud native programming model for container management. Any code, any cloud, any app.

hero:
    title: Modern Infrastrucutre as Code
    body: >
        Create, deploy, and manage infrastructure, on any cloud, in any language.
        Enable developers and operators to work better together.

    code: |
        // Deploy Nginx to AWS Fargate
        import * as awsx from "@pulumi/awsx";

        let web = new awsx.elb.ApplicationLoadBalancer(
            "net-lb", { external: true }).
            createListener("web", { port: 80, external: true });

        let appService = new awsx.ecs.FargateService("nginx-svc", {
            taskDefinitionArgs: {
                container: {
                    image: "nginx",
                    portMappings: [ web ],
                },
            },
            desiredCount: 5,
        });

        export let url = web.endpoint.hostname;

carousel:
    - heading: Create
      label: Create
      description: modern applications.
      details:
        - title: Real programming languages.
          description: >
            Define infrastructure in JavaScript, TypeScript, Python, Go, or
            any .NET language, including C#, F#, and VB.
        - title: Your favorite tools.
          description: Use familiar IDEs, test frameworks, and tools.
        - title: Share and reuse.
          description: Codify best practices and share them with your team or a growing community of practitioners.

    - heading: Deploy
      label: Deploy
      description: to any cloud.
      details:
        - title: Many clouds, one workflow.
          description: Use the same language, tools, and workflow, no matter the cloud.
        - title: Collaborate.
          description: Harmonize your engineering practices between developers and operators.
        - title: Easy continuous delivery.
          description: >
            Deploy from the CLI, or integrate with your favorite CI/CD
            system, and review all changes before they are made.

    - heading: Manage
      label: Manage
      description: cloud environments.
      details:
        - title: Tame complexity.
          description: Gain visibility across all of your environments.
        - title: Audit and secure.
          description: >
            Know who changed what, when, and why. Enforce deployment policies with your
            identity provider of choice.
        - title: Secrets management.
          description: >
            Keep secrets safe with easy, built-in encrypted configuration.

contact_us_form:
    section_id: contact
    hubspot_form_id: 8381e562-5fdf-4736-bb10-86096705e4ee
    headline: Contact Us?
    quote:
        title: Learn how top engineering teams are using Pulumi to manage CI/CD in any cloud.
        name: Josh Imhoff
        name_title: Site Reliability Engineer, Cockroach Labs
        content: |
            We are building a distributed-database-as-a-service product that runs on Kubernetes clusters across multiple
            public clouds including GCP, AWS and others. Pulumi's declarative model, the support for real programming
            languages, and the uniform workflow on any cloud make our SRE team much more efficient.
---
