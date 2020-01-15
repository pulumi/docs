---
title: Modern Infrastructure as Code
type: page
layout: event-one-pager
url: /show
noindex: true

meta_desc: Pulumi provides a cloud native programming model for container management. Any code, any cloud, any app.

hero:
    title: Meet the Pulumi team for tech talks and beer on Wednesday 1/22
    body: >
        Join us at Create33 for talks that focus on the development process on K8s.
        From 5:00pm to 6:00pm we will be hosting a happy hour with the Meetup starting at 6:30pm.

        The happy hour and Meetup are at Create33, which is located on the 33rd floor of the Wells Fargo
        Center at 999 3rd Ave Seattle, WA. The entry doors may be locked when you arrive but we’ll have somebody
        nearby to let you in. Once inside, please take the elevator to the 33rd floor.
    code: |
          import * as kx from "@pulumi/kubernetesx";

          // Define a Pod.
          const pb = new kx.PodBuilder({ containers: [{ image: "nginx" }] });

          // Create a Kubernetes Deployment using the previous Pod definition.
          const deployment = new kx.Deployment("nginx", {
            spec: pb.asDeploymentSpec()
          });

          // Expose the Deployment using a load balanced Kubernetes Service.
          const service = deployment.createService({
              type: kx.types.ServiceType.LoadBalancer,
          });
    cta:
        url: https://www.meetup.com/Seattle-Kubernetes-Meetup/events/267073230/
        label: Register Here

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
          description: Use the same language, tools, and workflow, on any cloud.
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
