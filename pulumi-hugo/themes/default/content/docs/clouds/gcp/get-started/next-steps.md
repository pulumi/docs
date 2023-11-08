---
title_tag: Next Steps | Google Cloud
meta_desc: This page provides a list of tutorials that take a deeper dive into
            Google Cloud cloud resources.
title: Next steps
h1: "Pulumi & Google Cloud: Next steps"
weight: 9
menu:
  clouds:
    parent: google-cloud-get-started
    identifier: gcp-next-steps

aliases:
- /docs/quickstart/gcp/next-steps/
- /docs/get-started/gcp/next-steps/
---

Congrats! You've deployed your first project on Google Cloud with Pulumi. Here are some next steps, depending on your learning style.

## Learn Pulumi

Dive into Learn Pulumi for a comprehensive walkthrough of key Pulumi concepts in the context of a real-life application.

{{< get-started-next-step path="/learn/pulumi-fundamentals" label="Learn Pulumi Fundamentals" ref="gs-gcp-learn" >}}

## Launch a new project with a template

Easily deploy the most common cloud architectures, from [static websites](/templates/static-website/gcp/) to [serverless applications](/templates/serverless-application/gcp/), [virtual machines](/templates/virtual-machine/gcp/), [container services](/templates/container-service/gcp/), and [Kubernetes clusters](/templates/kubernetes/gcp/).

{{< get-started-next-step path="/templates/" label="Browse templates" ref="gs-gcp-guides" >}}

## Dive into the docs

Read more about Pulumi's architecture and foundational concepts in depth, including [projects](/docs/concepts/projects/), [stacks](/docs/concepts/stack/), [configuration](/docs/concepts/config/), [secrets](/docs/concepts/secrets/), [resources](/docs/concepts/resources/), [state](/docs/concepts/state/), and more.

{{< get-started-next-step path="/docs/concepts/" label="Read the docs" ref="gs-gcp-docs" >}}

## Try Pulumi ESC (Environments, Secrets, and Configuration)

In this guide, you used [stack configuration](/docs/concepts/config/) and environment variables to configure a single project and stack. Did you know you can also configure multiple Pulumi projects, and even other applications, with [Pulumi ESC](/product/esc/)?

Pulumi ESC introduces the concept of _environments_ --- managed collections of static and dynamic settings that you can use to configure any project, stack, application, or service, including with short-lived cloud credentials through OpenID Connect.

{{< get-started-next-step path="/blog/environments-secrets-configurations-management/" label="Learn more about Pulumi ESC" ref="gs-gcp-esc" >}}

## Check out the blog

Browse the latest posts on using Pulumi with Google Cloud, including everything from new Google Cloud products and features to technical architectures and best practices.

{{< get-started-next-step path="/blog/tag/google-cloud/" label="Browse Google Cloud posts" ref="gs-gcp-blog" >}}
