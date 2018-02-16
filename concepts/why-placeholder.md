---
title: Why Placeholder?
---

As a cloud developer, you want to be agile, so you provision and manage your own infrastructure. Frustratingly, you then have to use infrastructure tools that were designed in an era when there were organizational silos between developers and operations teams. This creates extra friction; there are additional toolchains to learn, understand, and automate.

With Placeholder, you use your favorite tools to write **programs** in JavaScript or Python, with more languages on the way. (TODO: LINK to GitHub issue tracking language requests.) With ordinary JavaScript or Python syntax, your program defines *both* its application logic and the infrastructure it needs. You'll notice that in a Placeholder program, there's no longer a striking distinction between infrastructure and application code. In fact, we like to blur this line and simply think of Placeholder applications as distributed programs.

Here's the amazing thing that happens when you combine code and infrastructure: you can bring software engineering practices to cloud programming! You can even create and share reusable components that define application code alongside the infrastructure it depends on. 

For instance, suppose you want to create a component that provides a live leaderboard, backed by a managed Redis cache such as AWS ElastiCache:
-  **Before Placeholder**, this "component" would actually just be a leaderboard *library*. The author would provide configuration instructions on how to provision the cache and connect it to the library, in the form of several manual steps. It's on you to create a repeatable deployment for the cache and set up the correct environment variables.
-  **With Placeholder**, the author can create a **cloud component** that defines both the leaderboard logic and its infrastructure requirements. When you use this component in your code, Placeholder will automatically provision the cache for you. A Placeholder component is infrastructure as *software*. Like software, it can be shared, extended, and reused.

As an analogy, think of installing software on your machine. You could be given a zipfile along with detailed instructions on how to install it on your machine, or a macOS-like self-contained application package that you simply copy to the "Applications" folder. Placeholder components are like an application package.

One interesting aspect of Placeholder infrastructure definitions is that their neither strictly imperative or declarative. You write *imperative* code to define the resources you need, but Placeholder turns this into a *declarative* plan of infrastructure changes to make to your cloud environment. So, Placeholder programs are repeatable: it is incredibly easy to stand up a new stack---perhaps in a new region---that is identical to the original stack! Because Placeholder knows about the entire set of application resources and how they relate to one another, you can easily do incremental updates or destroy the entire stack once you are done.

Placeholder programs use a regular programming language but are run in a special way: instead of running the code directly, you use the Placeholder CLI. This CLI transforms your imperative code to a declarative plan and updates your application (including infrastructure!) when you've made a change. And, this all happens automatically, without you having to manually edit configuration or use a cloud console.
