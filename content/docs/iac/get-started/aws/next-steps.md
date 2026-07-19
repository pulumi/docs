---
title_tag: Next Steps | AWS
title: Next steps
h1: Next steps
stepper_link: "Next: Wrap up"
meta_desc: This page provides a list of tutorials that take a deeper dive into
            AWS cloud resources.
weight: 10
menu:
    iac:
        name: Next steps
        parent: aws-get-started
        weight: 10

aliases:
    - /docs/iac/get-started/aws/b/next-steps/
    - /docs/clouds/aws/get-started/next-steps/
    - /docs/iac/get-started/aws/create-component/
    - /docs/iac/get-started/aws/b/create-component/
---

Congratulations! You now know how to provision and manage cloud infrastructure with Pulumi. In this guide, you learned how to:

- Create and configure a Pulumi project and stack
- Provision new cloud resources
- Update existing cloud resources
- Use the Pulumi CLI to perform common operations
- Cleanly destroy cloud resources and stacks

Below are a few good next steps to build on this foundation and keep the learning going.

## Create reusable components

[Components](/docs/iac/concepts/resources/components/) are infrastructure abstractions that encapsulate complexity and enable sharing and reuse. Rather than copy and paste common patterns, you can encode them as components and share them with your team with just a few lines of code. [Learn more about components](/docs/iac/concepts/resources/components/) or [follow the guide](/docs/iac/guides/building-extending/components/build-a-component/) to build your own.

{{< get-started-next-step path="/docs/iac/guides/building-extending/components/build-a-component/" label="Build a component" ref="gs-aws-components" >}}

## Try Pulumi ESC (Environments, Secrets, and Configuration)

[Pulumi ESC](/docs/esc/) is a centralized secrets and configuration service that introduces the concept of _environments_ — managed collections of static and dynamic settings that you can use to configure any project, stack, application, or service, including with short-lived cloud credentials through OpenID Connect.

{{< get-started-next-step path="/docs/esc/get-started/" label="Learn more about Pulumi ESC" ref="gs-aws-esc" >}}

## Launch a new project with a template

Easily deploy the most common cloud architectures, from [static websites](/templates/static-website/aws/) to [serverless applications](/templates/serverless-application/aws/), [virtual machines](/templates/virtual-machine/aws/), [container services](/templates/container-service/aws/), and [Kubernetes clusters](/templates/kubernetes/aws/).

{{< get-started-next-step path="/templates/" label="Browse templates" ref="gs-aws-guides" >}}

## Dive into the docs

Read more about Pulumi's architecture and foundational concepts in depth, including [projects](/docs/concepts/projects/), [stacks](/docs/concepts/stack/), [configuration](/docs/concepts/config/), [secrets](/docs/concepts/secrets/), [resources](/docs/concepts/resources/), [state](/docs/concepts/state/), and more.

{{< get-started-next-step path="/docs/concepts/" label="Read the docs" ref="gs-aws-docs" >}}

## Check out the blog

Browse the latest posts on using Pulumi with AWS, including everything from new AWS products and features to technical architectures and best practices.

{{< get-started-next-step path="/blog" label="Visit the blog" ref="gs-aws-blog" >}}
