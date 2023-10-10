---
title: Pulumi Deployments
layout: pulumi-deployments

meta_desc: Pulumi Deployments is a new feature that automates the execution of Pulumi programs on your behalf.

overview:
    title: The fastest way to go from code to cloud
    description: |
        [Pulumi Deployments](/docs/pulumi-cloud/deployments/) is a fast and flexible way to deploy infrastructure on any cloud and at any scale, using GitHub pull requests, API calls, and console. No CLI setup needed since [Pulumi Cloud](/product/pulumi-cloud/) manages deployments.

quotes:
    items:
        - company: mighty
          name: Aaron Gibralter
          name_title: Head of Engineering at Mighty
          quote: |
            “Pulumi allows every engineer to build and update infrastructure instead of only our infrastructure team. With Pulumi Deployments, we could easily set up a standardized CI/CD infrastructure workflow for every engineer that immediately makes them productive.”

        - company: alkira
          name: Santosh Dornal
          name_title: Head of Software Test & DevOps at Alkira
          quote: |
            “I’m making developers at Alkira significantly more productive while also making my job easier using Pulumi. I can get developers using IaC immediately with Pulumi Deployments and its GitHub integration, while Pulumi Insights makes it really easy to find idle developer environments that need to be shut down, which reduces our cloud costs.”

benefits:
    title: How will Pulumi Deployments benefit me?
    description: |
        Pulumi Deployments makes it easier for you and engineers on your team to collaborate on infrastructure changes and deploy changes automatically through your existing GitHub pull request workflow. There is minimal setup and you can standardize your deployment workflow through GitHub and Pulumi. In addition, you can build your own custom deployment workflows with [Automation API](/docs/using-pulumi/automation-api/) code and offload the deployment workload to Pulumi Deployments instead of running it locally with the Pulumi CLI. Pulumi Deployments is based on the same technology as [Pulumi Automation API](/docs/using-pulumi/automation-api/).

preview:
  youtube_url: https://www.youtube.com/embed/v48U7CNWutc

options:
    title: How can I use Pulumi Deployments today?
    description:
    items:
        - icon: git-merged
          icon_color: purple
          title: Git Push to Deploy
          description: Deploy infrastructure with each [push to a GitHub branch](/docs/pulumi-cloud/deployments/reference/#github-push-to-deploy), using pull requests to review changes in ephemeral [Review Stacks](/docs/pulumi-cloud/deployments/review-stacks/) before deploying them.
        - icon: upload-to-cloud
          icon_color: salmon
          title: Click to Deploy
          description: Deploy infrastructure with a click of a button from the Pulumi Cloud console. Run update, preview, refresh, and destroy commands.
        - icon: code-window
          icon_color: blue
          title: REST API
          description: Deploy infrastructure by calling the Pulumi Service REST API. You can also use the API to run [Remote Automation API](/docs/pulumi-cloud/deployments/reference/#rest-api) code.

form:
    hubspot_form_id: 35baf46c-fd6e-4321-a75f-fc9319e31efb

learn:
    title: Get Started
    items:
        - title: Try Pulumi Deployments today
          description: Deploy infrastructure on any cloud by creating a free Pulumi account.
          buttons:
            - link: https://app.pulumi.com/signup
              type: primary
              action: Sign up for Pulumi Cloud
        - title: Documentation
          description: Refer to our documentation to get Pulumi Deployments set up once you have been accepted into the Preview.
          buttons:
            - link: /docs/pulumi-cloud/deployments
              type: secondary
              action: Pulumi Deployments Docs
            - link: /docs/reference/deployments-rest-api
              type: secondary
              action: Pulumi Deployments REST API Docs
---
