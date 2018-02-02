---
title: Why Pulumi?
---

<!-- TODO: need to be consistent between usage of "Cloud Application" and "program" -->

As a cloud developer, you want to be agile, so you provision and manage your own infrastructure. Frustratingly, you then have to use infrastructure tools that are designed for non-developers! To ensure automated and repeatable deployments, you end up writing markup in ill-suited "languages" with awkward formula syntax. What if you could do all this in a regular programming language?  

Even better, what if you could then combine your app logic and infrastructure requirements into *one* program?

With Pulumi, you use your favorite tools to write **programs** in JavaScript or TypeScript. (Python is on its way, followed by more of your favorite languages in the future.) With ordinary JavaScript syntax, your program defines *both* app logic and the infrastructure it needs. We simply call this a **Pulumi Cloud Application**. You'll soon notice that there's no longer a striking distinction between infrastructure and application code. In fact, we like to blur this line and simply think of Pulumi applications as distributed programs.

Here's the amazing thing that happens when you combine code and infrastructure: you can bring software engineering practices to cloud programming! You can create and share reusable components that define code alongside the infrastructure it depends on. 

For instance, suppose you want to create a component that provides a live leaderboard, backed by a managed Redis cache such as AWS ElastiCache:
- **Before Pulumi**, this "component" would actually just be a leaderboard *library*. The author would provide configuration instructions on how to provision the cache and connect it to the library. It's on you to create a repeatable deployment for the cache and set up the correct environment variables.
- **With Pulumi**, the author can create a **Cloud Component** that defines both the leaderboard logic and the infrastructure requirements. When you use this component in your code, Pulumi will automatically provision the cache for you. This is possible because we are using a real programming language where infrastructure requirements are an intimate part of your code---from source control, to build, and to deployment.

As an analogy, think of installing software on your machine. You could be given a zipfile along with detailed instructions on how to install it on your machine, or a macOS-like self-contained application package that you simply copy to the "Applications" folder. Pulumi Cloud Components are like an application package.

One interesting aspect of Pulumi infrastructure definitions is that they are a mix of a declarative and imperative model. You write imperative code to define the resources you need, but Pulumi turns this into a *declarative* plan of infrastructure changes to make to your cloud environment. So, Pulumi programs are repeatable: it is incredibly easy to stand up a new stack---perhaps in a new region---that is identical to the original stack!

Pulumi Cloud Applications use regular languages, but are run in a special way. Instead of running the application directly, you use the **`pulumi` command**. This CLI transforms your imperative code to a declarative plan and updates your application (including infrastructure!) when you've made a change. The Pulumi CLI does all this automatically, without you having to manually edit configuration or use a cloud console.
