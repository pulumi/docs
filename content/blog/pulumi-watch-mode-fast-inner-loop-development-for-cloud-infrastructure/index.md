---
title: "Pulumi Watch Mode - Fast Inner Loop Development for Cloud Infrastructure"
authors: ["luke-hoban"]
tags: ["serverless","kubernetes","Logging","New Features","applications"]
date: "2019-12-02"
meta_desc: "Pulumi Watch provides a mode for developing cloud infrastructure that speeds up the rate of iteration and allows cloud developers to focus on their code and infrastructure, instead of on the mechanics of their deployments, across modern cloud platforms including serverless, Kubernetes and more."
meta_image: "tbd.png"
---

A big part of our vision with Pulumi is to bring application developers and infrastructure teams closer together in the cloud.  That includes both providing infrastructure teams with better software engineering tools, as well as providing developers with easier access to cloud infrastructure.  We are often inspired by looking at great software engineering experiences in other development stacks and applying them to the cloud infrastructure space.  Whether it be general-purpose languages and rich IDEs, testing and package management, or components and rich APIs, at Pulumi, we’ve repeatedly applied successful development tools and practices to the challenges of building and scaling modern cloud infrastructure.

As we look across other areas of successful application development, one of the most  critical drivers of creativity and productivity is the **speed of iteration**.  When developers can make a change and see or experience the results nearly instantaneously, they can explore solutions quicker, can take more creative risks (and thus learn more), and can ultimately iterate more quickly toward their desired result.  From fast build times as a driving force in the design of the Go language, to the DevTools in Chrome, to Edit-and-Continue in Visual Studio, to the `watch` modes on tools like TypeScript, this idea of enabling quick or near-instantaneous feedback as code changes are made is a driving force behind many of the most successful developer experiences across a wide variety of software development environments.

## Introducing `pulumi watch` 

In Pulumi 1.5, we released a preview of a new `pulumi watch` command.  This command provides a mode for developing cloud infrastructure that speeds up the rate of iteration and allows cloud developers to focus on their code and infrastructure, instead of on the mechanics of their deployments.  With `pulumi watch`, cloud infrastructure feels like it’s truly at your fingertips.

{{< youtube "dCp2Nfa2S2Q?rel=0" >}}

The video above shows an example of working with some S3 resources.  Every time I hit “save” in my editor, `pulumi watch` automatically deploys any changes to my infrastructure.  If I add a new `BucketObject` resources and hit save, the object appears in S3.  If I add a loop around it and hit save, 10 new objects appear and the original object is removed.  And if I add an event handler, the 5 Lambda and IAM resources needed are deployed in seconds and are hooked up to the bucket.  You don’t have to switch back and forth between an editor and a terminal, and you don’t have to go through heavyweight infrastructure deployment tools like Terraform or wait on slow external services like CloudFormation or CI/CD.  Instead, changes appear directly in the cloud within seconds of hitting enter. You can try things out, experiment, learn, and rapidly iterate on your cloud infrastructure.

This new `watch` mode isn’t a replacement for a standard `pulumi preview`/`pulumi update`.  For production infrastructure deployments, it is critical to understand precisely what changes will happen before applying them, to integrate with CI/CD systems, to be able to do targeted updates, and to apply policy to guard the production environment against misconfiguration.  But that same level of care isn’t necessarily the right way to approach building new features in a development stack.  And it’s in these development environments that `pulumi watch` opens up a new experience for infrastructure development.  Although they are shorter periods relative to the full life of an infrastructure deployment, they are the majority of the time that creativity and creation is applied to cloud infrastructure, and thus represent a key opportunity to empower developers.

Not all cloud resources can be deployed or updated in seconds - but many of the most popular modern cloud primitives are built on platforms that enable and encourage quick iteration - and in particular both serverless and Kubernetes.  Watch mode can be used during the development of any infrastructure, but can really shine in these areas where the cloud platforms natively support fast iteration.

## Kubernetes Infrastructure + Applications

For Kubernetes, `pulumi watch` allows us to deploy changes to our cluster automatically as we author our Kubernetes resources.  Change the number of `replicas` for our `Deployment` and hit save and the new pods scale-out.  Add a `Service` to expose the deployment and public endpoint is available immediately.  This pairs beautifully with the recently released Pulumi Kubernetes Extensions (`kubernetesx`) library, which allows you to build Kubernetes applications with just a few lines of code - avoiding a lot of the boilerplate that slows down typical Kubernetes development when working with YAML.  We can see this combination in action in the video below:

{{< youtube "X96EMLi8uJY?rel=0" >}}

Both of the previous videos also highlight another interesting element of modern cloud infrastructure development.  In both the S3 example and the Kubernetes example, the Pulumi program deployed not just the infrastructure, but also the application code and assets.  By authoring and delivering both infrastructure and application code together, we remove another aspect of the silos that separate developers from infrastructure, and in doing so, unlock even faster iteration.  This is a pattern that Pulumi enables in a wide variety of unique ways, from Lambdas as lambdas, to build-and-push of Docker images, to deploying assets for static sites.  

## From Zero to Cloud Application in 90 Seconds

We can bring these ideas together, and show another example of what’s possible with `watch` mode using a serverless application example.  As with so many things these days,  a tweet inspired this example:

{{< tweet 1184295790438580224 >}}

Indeed, such simple tasks are often surprisingly complex and cumbersome with today’s infrastructure tools.  But with `pulumi watch` and the Pulumi Cloud Framework, we can go from nothing to having this application deployed in AWS (or Azure!) in under 90 seconds. 

{{< youtube "FuYwsXLqnTk?rel=0" >}}

# Conclusion

When using `pulumi watch`, working with cloud infrastructure *feels* so different - it feels malleable, it feels accessible, and it feels like it’s right at your fingertips.  By building on the same robust incremental deployment infrastructure as the rest of Pulumi, you get the same access to any cloud, and to a variety of languages and all the other benefits of Pulumi’s modern infrastructure as code tooling.  Pulumi watch triggers a deploy on any save - including both of files in the Pulumi program itself, as well as other assets that the Pulumi program may reference like application source code or static assets.  Pulumi watch also displays [runtime logs](https://www.pulumi.com/blog/unified-logs-with-pulumi-logs/) for supported platforms (Lambda, ECS, and Cloudwatch currently, more coming soon), and can be paired with another new feature, [Pulumi Query](https://www.pulumi.com/blog/query-kubernetes/), to get customized status about the runtime environment during rapid iteration. 

The `pulumi watch` command is available in preview now when the `PULUMI_EXPERIMENTAL` environment variable is set to `true`.  We are just getting started - and see many more opportunities to tighten the iteration cycle further, to support more logging capabilities, to integrate more deeply with `query`, and to be applied to more modern infrastructure scenarios.  

Give it a try today and drop us a note about where you’d like to see this go for [Pulumi 2.0](https://www.pulumi.com/blog/pulumi-2-0-roadmap/)!
