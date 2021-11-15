---
title: What Is Infrastructure as Code?
meta_desc: |
    Understand what is infrastructure as code, along with the main benefits and importance
    for modern application development.

type: what-is
page_title: What is Infrastructure as Code?

customer_logos:
  title: Leading engineering organizations are building with Pulumi
  logos:
    - items:
      - snowflake
      - tableau
      - atlassian
      - fauna
      - ware2go
    - items:
      - mindbody
      - sourcegraph
      - fenergo
      - skai
      - lemonade
    - items:
      - clearsale
      - angellist
      - webflow
      - supabase
      - ro

video:
  title: "A Quick Bite of Cloud Engineering: Infrastructure as Code"
  description: |
    What is infra as code (IaC)? Get a quick overview with Laura, one of Pulumi's developer advocates, in this episode of Quick Bites of Cloud Engineering.
  youtube_url: "https://www.youtube.com/embed/WhWf48kcEXU"
  transcript: |
    Welcome to your first quick bite of cloud engineering. I am Laura, and today we're gonna talk about infrastructure as code. So, what exactly is infrastructure as code? Infra as code, or IAC, is the idea that infrastructure configuration should be treated just as you would treat your code.

    So, that means putting it into source control, updating it with commits, doing code reviews, automating it as much as you possibly can, versioning it, testing it. IAC helps us automate the provisioning of infrastructure, which reduces mistakes. And, allows us to have multiple, near identical environments, without configuration drift. We can declare our configuration, and avoid hard coding secrets in, which in turn, helps to secure our systems.

    Why, exactly, does all of this really matter? Well, we can trigger builds of ephemeral or short-term environments, for things like development work, unit testing and integration testing, smoke testing, load testing, any kind of testing you really can think about. Security reviews, these environments can look and act exactly like production. Because, they're set up and built exactly the same way. All driven by code. Sure, you could use a cloud dashboard to set up everything, and somehow point and click your way through, to actually deploying your application.

    But, what happens if you click the wrong button and delete something? Or, your entire system goes down overnight? Or, maybe you just need to move to a new cloud provider? You can't remember what you set up, or the order you set it up in cause everything is named differently? We're developers and engineers. Instead of doing that point and click system, we write these instructions into code, to manage that infrastructure, leaving us with a source controlled, repeatable process that we can take anywhere, and scale on any system.

    Now, when we think about doing all of this, in real life, there's a few approaches you can do. You certainly can script up something with bash, and a cloud CLI, but that doesn't really track state, meaning where everything is. Or, the transitions between two states. Or, give us any other familiar tools.

    IAC, on the other hand, works by declaring a goal state. What you want your infrastructure to look like, when it is stable, deployed, and running as normal. To do that, we let an oracle, or the IAC engine, decide how best to carry out deployments. Both for brand new environments, or environments that are currently existing, that we want to actually scale up. These kinds of solutions are much better than your typical manual, or scripting changes.

    The first infra as code solutions use templating languages, like YAML and JSON. And nearly all cloud providers offer this type of solution. They can be very useful, because they're native to the ecosystem. But you do end up with vendor lock in, which can be expensive, if you want to change. And, obviously, you can't run systems across multiple clouds with that single tool, because it's locked into that specific vendor. There's also solutions like Terraform, which use a specific templating language, that can span cloud providers, to declare that goal state that you actually want.

    That means you can work with, again, those systems across multiple ones, making it easy to switch from one cloud to another. However, while these systems do actually have an idea of state, you still have to manage the state file, which is where everything's stored, all by yourself. And, you have to learn specialized languages and tools to be able to actually use something like it.

    Now, modern infra is complex. And, there's a lot of teams working in any platform, at any given time. We can't afford to continue to widen the gap between app teams and infra teams, and devs, and ops, and infrastructure, and security. So, there's new players in the field. And, this is where I might get a little bit biased. These new infra as code systems, known as, cloud engineering systems, like Pulumi, let you accomplish the same robust goal, of a good IAC system, but with everything we know and love about our favorite programming languages.

    We can use expressive capabilities, like four loops, abstraction and encapsulation, with classes and functions, and share and reuse common patterns, using packages. We can use our favorite tools, like linters, editors, debuggers, and test ring works. By doing so, we bring apps and infra closer together, and help devs and infrastructure experts collaborate more closely, all with a system that manages state for you, rather than having to manage it yourself.

    Of course, you can also go the DIY route, and build off the open source projects that are behind systems, like Terraform and Pulumi. Why would you want to do that? Well, you own it. You know how it works. You know where everything lives. You know why it works, and you know how to secure it. Or, you know how you secured it. However, there's the downside of you own it. You have to be there when it breaks, and you need to spend the time and money to continue to maintain it, and manage that entire system.

    It's really up to you. Overall, infra as code has been a great tool to work with the complexity of modern cloud based systems. We have a repeatable, scalable process to get the infrastructure we need, when we need it, and ship the features that we need, quickly. So, we can focus on getting out good code. This has been your quick bite of cloud engineering for this week.

    I'll be back in two weeks on Wednesday, to do another quick bite, for another topic on cloud engineering. So, subscribe if you want to get notified for the next episode. If you want to hear anything specific, leave me a note down in the comments, and we'll see if we can get that answered for ya. Anyway, that's it for Quick Bites. Take care. Bye.
---

Infrastructure as code (IaC) means using code to define and manage infrastructure. **Infrastructure as code is about bringing software engineering principles and approaches into the cloud infrastructure space.**

Infrastructure as code is the latest step in the evolving process of defining and managing infrastructure. Before infrastructure as code, infrastructure was (and in some cases still is!) provisioned by many methods such as pointing and clicking in a user interface, batch scripts, and configuration management tools that may not have been designed by the cloud. Today, modern approaches use platforms, such as [Pulumi](/), which embrace and support the full software engineering lifecycle.

The term “infrastructure as code” or IaC has become commonplace, but there are important questions attached to it. What is infrastructure as code really? What are the benefits of infrastructure as code?  How do you integrate infrastructure as code into your organization? In this article, we’re going to touch on all these points and discuss why infrastructure as code matters for modern application development.

## Why Has Infrastructure as Code Become Important?

Infrastructure as code matters because of three significant trends, all of them happening at the same time.

### The transition to the cloud

One trend, of course, is the ongoing transition to the cloud. More and more companies are shifting workloads from on-premises infrastructure to cloud environments. Cloud-based infrastructure is provisioned via APIs, and, as a result, can be easily managed with infrastructure as code tools.

### Cloud modernization

The second trend is cloud modernization. After organizations migrate to the cloud, they tend to look for opportunities to maximize the value they get from their cloud environment. This frequently involves adopting technologies such as serverless, containers and Kubernetes, which, when applied correctly, these technologies enable teams to deliver value more quickly, and uses managed services to offload some of the heavy lifting to the cloud provider. These technologies and services generally require a more granular management of infrastructure. Stitching together all the primitives that the cloud provider offers into solutions that serve the business is a great fit for infrastructure as code.

### Frequent infrastructure changes

Finally, the rate at which a company’s infrastructure changes is increasing. Cloud adoption and cloud modernization are two of the reasons this is happening. The third is that organizations are finding that they can move faster if they take advantage of the fundamental elasticity of the cloud.

For teams managing tens or hundreds of cloud resources that change once every few months, it may still be possible to manage infrastructure with point-and-click or scripts. But the more common situation today is that teams are managing thousands or tens of thousands of resources that change daily or even hourly. Infrastructure as code is how you take control of that kind of complexity.

## What Benefits Does Infrastructure as Code Provide?

Infrastructure as code tames the complexity of cloud infrastructure because it uses the same software engineering principles that have enabled other software-based systems to scale up. Here are some of the principles infrastructure as code enables.

### Version control

When infrastructure is described as code, it can be checked into source control, versioned and code-reviewed using existing software engineering practices. Changes to infrastructure can be deployed using existing CI/CD tools.

### Testing

As any critical system grows in complexity, people can start to feel nervous about making changes. With infrastructure as code, teams can write tests for their infrastructure to ensure its correctness.  They can encode policies so that all provisioned infrastructure and its configurations [are compliant](/docs/guides/testing/property-testing/). Once they’re tested, infrastructure components can be reusable pieces of code that capture best practices and that can be shared across teams. No more reinventing the wheel.

### Use of IDEs

Most developers have an IDE that they use all the time. When infrastructure is code, you can take advantage of all the features that an IDE offers, such as autocompletion and the ability to look up methods and their parameters.

### DevOps

Infrastructure as code enables infrastructure teams and software development teams to adopt DevOps principles and work together more closely.  When infrastructure is code and is integrated into your company’s software lifecycle, there’s a common language and a common set of practices that stakeholders already understand. That common understanding fosters cross-team collaboration, which is fundamental to DevOps

## How Do I Get Started with Infrastructure as Code

Bringing infrastructure as code into a startup or a company with many greenfield applications may not be difficult. For most companies, however, it’s not so straightforward. Many companies, both large and small, have a lot of infrastructure that was created by pointing and clicking in the console of a cloud provider. That’s how many new projects get started. Then, one day, an ops engineer wakes up and realizes that the new project is now production infrastructure. To make it more “official,” they write a run book or a wiki that describes what buttons to click when someone wants to do some common task. Another common situation is that there are Bash or PowerShell scripts floating around that only one or two people know about. What do you do if that’s your situation?

Here are steps you can take to adopt infrastructure as code.

### Define “Good”

The first step, even before you begin to [evaluate tools and approaches](/blog/configuring-your-dev-environment/), is to define what “good” looks like to your company. Achieving that ideal doesn’t depend on which technology you use. It depends on understanding what assumptions will remain true regardless of the tools you use.  For many companies those assumptions are:

- The amount of infrastructure is going to be high.
- The number of interconnections between managed services will be high.
- The rate of change should be high, in order to take maximum advantage of what your cloud provider(s) offer.
- The number of people who have access to your cloud’s capabilities should grow.
- Infrastructure code should be integrated into your continuous delivery system.

A team made up of all the stakeholders is one way to define what your company wants to achieve with its cloud infrastructure.

### Import Existing Infrastructure

You probably already have a lot of existing infrastructure.  Make sure you can [import that existing infrastructure](/blog/adopting-existing-cloud-resources-into-pulumi/) into your new world. For example, you might have a production database that you want to manage as infrastructure as code. Your tool should let you reliably manage state changes, let you make changes without any downtime, let you test and version those changes, preview the changes, and get pull requests.

### Integrate with existing engineering practices

Assuming your infrastructure code is integrated with your continuous delivery pipeline, you can start instituting the same best practices you use with your application software. For example, to understand your infrastructure’s correctness, [you’ll need tests](/blog/testing-your-infrastructure-as-code-with-pulumi/). Some tests should run before delivering the infrastructure to ensure that the program is logically correct and that it provisions the infrastructure correctly. Other tests should run when you deploy your infrastructure to ensure that the deployment was successful.

### Think about policies and security

Next, you’ll want to enforce policy for the entire organization. That way, you’ll have a standard that applies to everyone who builds infrastructure. [Those policies should run against everything anyone does](/blog/benefits-of-policy-as-code/).

It’s important to plan policies and security because one of the goals of Infrastructure as Code is to empower the development teams and give them as much flexibility as possible. Without planning, you may find that you’ll create an interface that’s so restrictive, teams find ways to go around the platforms. It’s a balancing act that requires input from everyone.

### Start Small

Any time you make a significant change in technology, you want to do it incrementally. You might start with a new service so you don’t disrupt existing ones. Once you've figured out what successful patterns look like, go back and figure out how to transform some existing infrastructure. Pick a project where you’ll start seeing value early and then iterate.

## Learn More

Pulumi offers a truly modern approach to infrastructure as code. With Pulumi, you can create, deploy, and manage infrastructure on any cloud using the programming languages and tools you already know. [Get started today](/docs/get-started/).
