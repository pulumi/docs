---
title: Kubernetes with Pulumi
layout: kubernetes
url: /kubernetes

meta_desc: Pulumi provides a cloud native programming model for Kubernetes deployments and orchestration. Any code, any cloud, any app.

hero:
    title: Kubernetes with Pulumi
    body: >
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque magna
        libero, viverra eu odio eget, finibus sodales orci. Donec ut nulla sit
        amet nisi dictum suscipit. Vestibulum maximus dui id lacinia dignissim.
        In quis turpis convallis, consequat libero ac, aliquet erat.


        Lorem ipsum dolor sit amet, consectetur.
    code: |
        import * as kx from "@pulumi/kubernetesx";

        const pb = new kx.PodBuilder({
            containers: [{
                image: "nginx",
                ports: { http: 80 }
            }]
        });

        const deployment = new kx.Deployment("nginx", {
            spec: pb.asDeploymentSpec({ replicas: 3 })
        });

        const service = deployment.createService({
            type: kx.types.ServiceType.LoadBalancer
        });

        export const serviceIP = service.ip;

kubernetes_overview:
    title: Vestibulum maximus dui
    description: |
        Donec auctor massa eu est gravida, et sollicitudin elit congue. Aliquam eu ligula leo. Phasellus blandit, velit at pretium convallis, velit felis placerat tortor, eu laoreet dolor dui id nunc.
    list:
        - Nam iaculis felis at arcu auctor pretium. Proin interdum mollis aliquam.
        - Phasellus nisl nulla, dapibus id facilisis vel, vestibulum et velit. Ut porttitor libero nec quam porttitor pretium. Vestibulum ante ipsum primis in faucibus orci.
        - Nulla ultrices est at orci egestas consectetur.
    cta: REQUEST MORE INFORMATION

superpowers:
    - title: Vestibulum maximus dui
      cta: Learn more
      ctaUrl: "/docs/get-started"
      iconType: cloud
      description: |
        Donec auctor massa eu est gravida, et sollicitudin elit congue.
        Aliquam eu ligula leo. Phasellus blandit, velit at pretium convallis,
        velit felis placerat tortor, eu laoreet dolor dui id nunc.

    - title: Vestibulum maximus dui
      cta: Learn more
      ctaUrl: "/docs/get-started"
      iconType: provisioning
      description: |
        Donec auctor massa eu est gravida, et sollicitudin elit congue.
        Aliquam eu ligula leo. Phasellus blandit, velit at pretium convallis,
        velit felis placerat tortor, eu laoreet dolor dui id nunc.

    - title: Vestibulum maximus dui
      cta: Learn more
      ctaUrl: "/docs/get-started"
      iconType: delivery
      description: |
        Donec auctor massa eu est gravida, et sollicitudin elit congue.
        Aliquam eu ligula leo. Phasellus blandit, velit at pretium convallis,
        velit felis placerat tortor, eu laoreet dolor dui id nunc.

    - title: Vestibulum maximus dui
      cta: Learn more
      ctaUrl: "/docs/get-started"
      iconType: architecture
      description: |
        Donec auctor massa eu est gravida, et sollicitudin elit congue.
        Aliquam eu ligula leo. Phasellus blandit, velit at pretium convallis,
        velit felis placerat tortor, eu laoreet dolor dui id nunc.

    - title: Vestibulum maximus dui
      cta: Learn more
      ctaUrl: "/docs/get-started"
      iconType: policy
      description: |
        Donec auctor massa eu est gravida, et sollicitudin elit congue.
        Aliquam eu ligula leo. Phasellus blandit, velit at pretium convallis,
        velit felis placerat tortor, eu laoreet dolor dui id nunc.

    - title: Vestibulum maximus dui
      cta: Learn more
      ctaUrl: "/docs/get-started"
      iconType: testing
      description: |
        Donec auctor massa eu est gravida, et sollicitudin elit congue.
        Aliquam eu ligula leo. Phasellus blandit, velit at pretium convallis,
        velit felis placerat tortor, eu laoreet dolor dui id nunc.

detail_sections:
    - title: Vestibulum maximus dui
      description: Donec auctor massa eu est gravida, et sollicitudin elit congue. Aliquam eu ligula leo. Phasellus blandit, velit at pretium convallis.
      cta: Contact Us
      ctaUrl: "/contact.md"
      items:
          - title: Vestibulum maximus dui
            description: Donec auctor massa eu est gravida, et sollicitudin elit congue. Aliquam eu ligula leo.
            icon: fa-car-side

          - title: Vestibulum maximus dui
            description: Donec auctor massa eu est gravida, et sollicitudin elit congue. Aliquam eu ligula leo.
            icon: fa-book

          - title: Vestibulum maximus dui
            description: Donec auctor massa eu est gravida, et sollicitudin elit congue. Aliquam eu ligula leo.
            icon: fa-key

          - title: Vestibulum maximus dui
            description: Donec auctor massa eu est gravida, et sollicitudin elit congue. Aliquam eu ligula leo.
            icon: fa-people-carry

    - title: Vestibulum maximus dui
      description: Donec auctor massa eu est gravida, et sollicitudin elit congue. Aliquam eu ligula leo. Phasellus blandit, velit at pretium convallis.
      cta: Contact Us
      ctaUrl: "/contact.md"
      items:
          - title: Vestibulum maximus dui
            description: Donec auctor massa eu est gravida, et sollicitudin elit congue. Aliquam eu ligula leo.
            icon: fa-user-tie

          - title: Vestibulum maximus dui
            description: Donec auctor massa eu est gravida, et sollicitudin elit congue. Aliquam eu ligula leo.
            icon: fa-phone

          - title: Vestibulum maximus dui
            description: Donec auctor massa eu est gravida, et sollicitudin elit congue. Aliquam eu ligula leo.
            icon: fa-chalkboard-teacher

          - title: Vestibulum maximus dui
            description: Donec auctor massa eu est gravida, et sollicitudin elit congue. Aliquam eu ligula leo.
            icon: fa-pager

contact_us_form:
    section_id: contact
    hubspot_form_id: 212ce93d-e081-4998-b14b-f26a974da4fb
    headline: Need help with Kubernetes?
    quote:
        title: Learn how top engineering teams are using Pulumi to manage and provision Kubernetes clusters in any cloud.
        name: Harrison Heck
        name_title: Head of DevOps, Linio
        content: |
            As the largest eCommerce platform in Latin America, our infrastructure has to be highly stable, well
            documented and agile. With Pulumi, we're able to develop new infrastructure, change existing infrastructure
            and more with greater speed and reliability than we've ever had before.
---
