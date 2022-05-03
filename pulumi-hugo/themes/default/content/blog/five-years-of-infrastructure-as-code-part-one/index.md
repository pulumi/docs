---
title: "All Roads Lead Back to Infrastructure as Code"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2022-05-03T10:16:25-07:00

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
meta_desc: "We just celebrated Pulumi's 5th birthday! To commemorate, we are publishing a multi-part series on all things infrastructure as code, starting with the why."

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
    - joe-duffy

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - infrastructure-as-code

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
---

Our mission with Pulumi was to make it 100x easier to program the cloud. We saw amazing new architectures and capabilities made possible by the modern cloud, and new and exciting software and business outcomes fueled by adopting them. And yet, back in 2017 when we began, we found the models for programming, composing, and building modern cloud software sorely lacking. “Infrastructure as code” is widely accepted as the table stakes solution, yet most people were copy-and-pasting config scripts in bash, encoding architecture in thousands of lines of YAML, and the best in class technologies used proprietary domain-specific languages that lacked great IDEs and true sharing and reuse, and were simply reinventing the wheel.

When we sat down to envision Pulumi, we had just been immersed in developer platforms for decades. We honestly had no idea we’d start with infrastructure as code. We tinkered with a new programming language, prototyped some higher level containers- and serverless-specific tools, frameworks, and programming models, … And yet, all roads kept coming back to infrastructure as code. It wasn’t that infrastructure as code was “bad” – indeed, it was essential – it was simply that the past attempts missed the mark. The “code” that these tools touted didn’t feel much like code to us at all in the usual sense. As a result, it didn’t have universal appeal, and most developers didn’t enjoy using these tools. In fact, it seemed the industry had taken a step back compared to the earliest infrastructure as code tools like Chef and Puppet that embraced languages. We realized that we could bring great programmability to all things modern cloud, opening it up to a universal audience.

Why did all roads lead back to infrastructure as code? Infrastructure as code offers a fundamental building block that gives us a highly programmable and composable surface area over the entirety of the modern cloud’s capabilities. Being able to abstract and encapsulate complexity, and build bigger things out of smaller things, is the key not just to productivity, but also many decades of prior success and progress in computer science. Infrastructure as code also introduces a necessary concept of cloud resource lifetime and management that we take for granted in other areas of programming, for instance, with in-memory or operating system resources. Our “ah-hah” moment was to take everything we knew and loved about general-purpose languages, and marry that with infrastructure as code. In short, we set out to stand on the shoulders of giants and re-imagine infrastructure as code from start to finish.

Let’s take a more in-depth look at that journey and how we ended up with Pulumi.

## The Cloud as the New Operating System

Most “code” we’ve written historically runs on a single computer. That single computer has resources like CPU, memory, disks, and network cards that the operating system manages. The lifetime of those hardware resources is relatively straightforward since programs have a finite lifetime. There are well defined process models where a program begins and ends running. Most resource usage is ephemeral and lasts no longer than a program’s lifetime, with the obvious exception of persistent state such as what gets written to the filesystem.

If you take a step back and think about what an operating system provides, it’s just a software abstraction that helps to manage and mediate access to this hardware and related services. An operating system has a kernel that allocates, schedules, and reclaims resources. It virtualizes access to compute, and provides a scheduler, so that applications can offer up jobs needing to execute, and the operating system can make that happen in the most effective way given various policies. There is a security model for users and groups and uses this to control access to I/O and other physical and logical resources. There’s an application model dictating how applications are installed, configured, and updated. Finally, there is an API for how programs interact with this operating system, enabling an ecosystem to build up around it.

When phrased that way, it’s interesting that the cloud has to do all of these things too. The cloud itself is simply a collection of hardware and software services, with an API, and its own security and application models. One key difference is  that workloads span multiple computers – most operating systems manage just one – and resource lifetime therefore spans multiple computers and software systems too.

Although operating systems like Linux, macOS, and Windows certainly keep innovating, most of the fastest-moving innovation agenda has moved into the clouds. Most of the platform innovation these days that fundamentally reshapes how we write applications is happening within clouds like AWS, Azure, Google Cloud, and cloud native technologies like Kubernetes.

## The Era of Distributed Computing is Here

In the 2000s, I worked on multicore. This included building technologies like [thread pools](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.487.7627&rep=rep1&type=pdf) and [work-stealing schedulers](http://supertech.csail.mit.edu/papers/cilk5.pdf), [task and data parallelism](https://docs.microsoft.com/en-us/dotnet/standard/parallel-programming/), and the foundations of what eventually became [async/await in many popular languages](https://en.wikipedia.org/wiki/Async/await). At the time, I noticed a peculiar thing: all the great research into concurrent programming, ranging from the 80s to even the late 50s, predicted the coming age of distributed computing. This included exotic fault-tolerant programming languages like [Argus](https://en.wikipedia.org/wiki/Argus_(programming_language)), [massively scalable algorithms](http://cva.stanford.edu/classes/cs99s/papers/hillis-steele-data-parallel-algorithms.pdf), and message-passing systems like [actors](https://apps.dtic.mil/sti/pdfs/ADA157917.pdf). And yet, at the time, distributed computing remained in the domain of textbooks, universities, and research labs that could afford multi-million-dollar supercomputers.

The cloud has ushered in true distributed computing, with infinite data and compute being readily available to all of us as a commodity. If you think about the aggregate behavior of the modern cloud systems we’re building, this represents a computer program in a very real sense. This “program” simply doesn’t have nearly as finite a lifetime or boundary you can draw around it when compared to classical operating system processes.

The world of programming models is a very different place now than in those early multicore days. Back then, most supercomputer developers used baroque C++-based [OpenMP](https://en.wikipedia.org/wiki/OpenMP) and [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface) frameworks, and [relatively immature web services protocols like SOAP and WS-*](https://en.wikipedia.org/wiki/SOAP). Today, we have async runtimes, [REST APIs](https://en.wikipedia.org/wiki/Representational_state_transfer), [RPC frameworks](https://grpc.io/), and rich protocols such as [HTTP/2](https://en.wikipedia.org/wiki/HTTP/2), distributed frameworks like [Hadoop](https://hadoop.apache.org/), [Tensorflow](https://www.tensorflow.org/), and [Temporal](https://temporal.io/), and [infinitely scalable cloud-hosted services](https://aws.amazon.com/lambda/) that can be paid for on-demand, frequently for just pennies. We have containers for easy packaging and distribution of microservices. Serverless provides ultra-fine-grained scheduling of individual application functions. We have countless data stores sitting in between, some temporary like [Redis](https://redis.io/), queue-based like [Kafka](https://kafka.apache.org/), and others durable.

The common challenge here is that these systems run somewhere, on something. Where and what is that? How do we program this cloud thing? That’s where infrastructure enters the picture. Before infrastructure as code, when you wanted to run a program on an operating system, you’d first have to go manually configure every resource it needed to use by hand: e.g., give that program X compute, Y memory, oh it can have some file handles and mutexes too, and so on. That’s a fairly tedious, restrictive, and slow-moving prospect! If that’s how we built real programs, most of the most exciting innovation in software simply wouldn’t have happened. Thankfully, we did better, and can learn from it.

## Infrastructure is Exciting

Before the modern cloud, “infrastructure” was static and simple. You wrote an N-tier application largely without concern for its hosting environment, filed a ticket to ask your IT team for “two virtual machines and a database,” and developed locally on your machine while patiently waiting for that ticket to be resolved next quarter. Maybe a year would pass, and you’d upgrade one of those virtual machines, or add one, or scale your database capacity. In short, needing to wait wasn’t a big deal, and manual steps were tolerated, because infrastructure was so far removed from day-to-day software development. And, hey, the world moved pretty slowly anyway.

These days, we’ve gone from shipping quarterly, to monthly, to weekly, to daily, and now, for many of us, multiple times per day – sometimes on every Git commit. We’ve gone from an application needing “two VMs and a database” to needing dozens, if not hundreds of cloud resources: microservices, clusters, container registries, networks, security roles and rules, encryption keys and secrets, load-balancers, serverless functions, pub/sub topics, queues, data stores of myriad flavors, hosted AI/ML services, and more. We’ve gone from having staging and production, to having multi-region environments, in some cases dozens devoted to production alone (or more), in addition to many dev and test environments, ephemeral environments, and so on. This has a multiplicative effect, meaning many teams need to manage 1,000s of resources. In short, we’ve seen an explosion in moving pieces. With this added complexity also comes incredible power to those who can wield it.

There is a meme which is that “infrastructure should be boring.” We believe the opposite: infrastructure is central to fully tapping into the distributed computing era. And that’s exciting! It’s true, “some infrastructure should be boring”: you don’t want your team innovating in and playing fast-and-loose with network security, for instance. But a lot of modern infrastructure can be harnessed to accelerate your team more effectively than ever before.

## Automate All the Things

Let’s imagine you buy the premise that infrastructure’s exciting, that there’s going to be a lot more of it, and that democratizing access to it by making it fully programmable is key to realizing the full power of the cloud. We’ll need to start by thinking about how to create, scale, and generally manage it, both for current workloads and environments, as well as those yet to come.

Remember, we are starting from a place of not having a true resource or application model for those cloud resources, like we already have with operating systems. How do we start building back up to that? The first step is to tame all that complexity with automation so that, rather than manually pointing and clicking to create, scale, and manage your 1,000s of cloud resources, it is repeatable and robust thanks to infrastructure as code. There’s an evolution in maturity here:

### 1. Manual point-and-click in the UI console

Many teams start with their cloud UI to spin up and manage infrastructure, such as AWS, Azure, VMWare vSphere, etc. This is much like just creating operating system resources using Windows’s old school MMC-style snap-in UIs. This has the advantage of being “quick and easy,” while also letting the end user explore visually. This can be  a real benefit, especially when the usage patterns for services aren’t obvious or known in advance. The downside, however, is that it’s a manual process. If something fails or gets deleted, you need to evolve the infrastructure, or need to scale in any dimension, you’re in for a slow and painful process. This is the same reason we seldom use those MMC snap-ins and instead use Bash or PowerShell scripts.

### 2. CLI commands or APIs

Most infrastructure providers offer command line interfaces (CLIs) for doing anything the UI console can do. This means that a sequence of point-and-click steps can be translated into a sequence of commands in Bash, PowerShell, or CMD. Related to that, cloud providers often similarly provide REST APIs, meaning that those commands can be encoded in curl commands. This has the benefit of being able to document procedures in playbooks and have some degree of repeatability. The downside, however, is that it’s still manual, hard to automate, easy to miss a step, and still a slow and painful recovery process should something go awry.

### 3. Shell scripts

Instead of manually running commands or curling REST APIs, the next level of maturity is to capture those well-defined sequences inside of shell scripts. This is a significant increase in maturity because scripts are far more repeatable and can be checked into version control. The downside is that these scripts can become very ad-hoc, requiring all sorts of gymnastics to make them resilient to failure. Often, a failure part-way through a script will leave infrastructure in an unknown state requiring manual recovery. Every upgrade path needs to be considered manually; for example, if you have three possible states, A, B, and C, you’ll need to manually reason about A->B, A->C, B->C, and as the system evolves, this can get out of hand.

### 4. SDK-driven code

A slight variant on creating scripts is to create software using a general-purpose language. Most cloud vendors offer SDKs in various languages that add convenience atop their REST APIs. This approach has all the benefits of scripting, but with many more, as you get more modern language facilities such as first-class error handling, logging, and debugging. It does, however, unfortunately suffer from similar problems to the scripting approach, including the difficulty of recovering from partial failures, as well as upgrade path combinatorial explosion.

### 5. Infrastructure as Code

The final level of maturity is infrastructure as code. In infrastructure as code, you declare the desired state of infrastructure required, instead of the specific steps needed to get there, and a “magical oracle” figures it out from there. Although (3) and (4) are already using “code,” infrastructure as code takes care of the partial failures, combinatorial upgrade path issue, and more. An infrastructure as code engine has a model of resource lifetime and how to properly manage all the possible state transitions that infrastructure might need to go through, and can recover from failure seamlessly. The result is that infrastructure as code tools make it possible to automate managing many environments robustly, repeatably, and reliably.

Before diving into the details of infrastructure as code, let’s set the scene further. During the gradual transition from the “two VMs and a database” world, to the more modern one which exhibits so many more moving pieces, two other important shifts also took place:

- The shift from mutable infrastructure to immutable infrastructure.
- The shift from configuration- to provisioning-based infrastructure as code.

## On Cattle and Pets

In the early cloud days, each server was special: it was created to serve a purpose, and there were so few of them that each one required its own care and feeding. We upgraded these servers in place with patches and upgrades rather than simply replacing them. If one of them died, it was a catastrophe, and required significant work to repair the environment to operability. The A->B/A->C/B->C upgrade challenges were pretty much a given in this world.

Fast forward to the modern cloud days of today, and we seldom do this any longer but for very specific usage patterns (like persistent storage services). Instead, we rely on cluster management software and serverless control planes to manage fleets of servers or pools of compute resources, dynamically scale them up or down as needed for a given workload, and load-balance or intelligently route traffic to facilitate ephemerality and dynamism. Instead of upgrading servers in place, we do rolling updates that replace the old with the new.

This newer approach has significant benefits. Fault tolerance is built in. Workloads can scale to zero when not in use, saving money. At the same time, they can  scale to new heights during peak times, to ensure good performance and end user experiences. Managing such an environment is easier because we can rely on declarative goal states and get ourselves out of the messy business of dealing with partial failures and upgrades.

For reasons that are probably obvious (and possibly disturbing to some), [old-world infrastructure is sometimes referred to as “pets,” while the new-world infrastructure is referred to as “cattle.”](https://www.engineyard.com/blog/pets-vs-cattle/) The idea here is that each individual pet is special to an individual, whereas with an entire farm of cattle, we focus more on the health of the herd than any one individual cow.

## Beyond Configuration

When describing infrastructure as code earlier, we skipped over some nuances, like how it all began. The first wave of infrastructure as code tools like <a href="https://cfengine.com/" target="_blank" rel="noopener noreferrer">CFEngine<i class="text-sm ml-2 fas fa-external-link-alt"></i></a>, <a href="https://puppet.com/" target="_blank" rel="noopener noreferrer">Puppet<i class="text-sm ml-2 fas fa-external-link-alt"></i></a>, <a href="https://www.chef.io/" target="_blank" rel="noopener noreferrer">Chef<i class="text-sm ml-2 fas fa-external-link-alt"></i></a>, <a href="https://www.ansible.com/" target="_blank" rel="noopener noreferrer">Ansible<i class="text-sm ml-2 fas fa-external-link-alt"></i></a>, and <a href="https://saltproject.io/" target="_blank" rel="noopener noreferrer">SaltStack<i class="text-sm ml-2 fas fa-external-link-alt"></i></a>, were born in the “two VMs and a database” world. The most common task was to configure a server after it is created – even when that creation itself was done manually by an operator clicking in the AWS EC2 or vSphere console – and then to keep it updated by patching it from then onwards. As such, these tools were very much oriented around configuration and pets, compared to modern tools that are more oriented towards provisioning and cattle.

The modern approach generally provisions the broad array of cloud infrastructure resources, from containers to serverless functions, and yes, even VMs, and everything in between. Some tools like [AWS CloudFormation](https://aws.amazon.com/cloudformation/) and [Azure Resource Manager (ARM)](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview) are cloud-specific, while others like Pulumi and [Terraform](https://terraform.io) are cloud-agnostic. In this world of many moving pieces, tools are focused on provisioning new things rather than configuring and patching. In “code,” you declare a desired state, and the infrastructure as code engine creates, updates, or deletes the necessary infrastructure resources to bring that desired state into being.

The lines between the tools can get blurry. Even provisioning-based infrastructure as code tools can update infrastructure in-place when it is idempotent and minimizes downtime. You can think of this as an optimization. The “inside” of a server is seldom patched in this world, however.ou will frequently find these tools used alongside newer compute services like containers and serverless functions that never in-place update the workload code they run.

## Infrastructure as Code FTW!

So as we saw above, infrastructure as code is the most advanced form of automation, and has become table stakes for many companies using the cloud. Let’s look at what’s common to all tools in this space — and then what’s different.

There are two major parts to any infrastructure as code technology: the programming model you use to express desired state, and the deployment engine itself which orchestrates the create, read, update, and delete operations (CRUD) as appropriate. Prior to Pulumi, the programming models used were typically markup languages like JSON or YAML, or domain-specific languages (DSLs) like HashiCorp’s Configuration Language (HCL). The major innovation with Pulumi was to bring general purpose languages to the space, while still preserving the ability to have a fully declarative infrastructure as code deployment engine. The best of both worlds!

In summary, here is what modern provisioning-based infrastructure as code tools do:

- [They have an expression language](/docs/intro/languages/) (markup, DSL, or general-purpose language) which a user declares a desired state within. This desired state represents the infrastructure building blocks, their names and property values, and how they connect to each other.

- They have a way to trigger an update, and might offer multiple ways to do so. This includes the first deployment to an environment as well as subsequent updates.

- [They typically offer facilities for managing multiple instances of the same program](/docs/intro/concepts/stack/) (frequently called something like stacks, environments, or workspaces). This makes it easier to spin up and scale multiple environments over time.

- [They track last-known deployment state](/docs/intro/concepts/state/). This is required for the tool to be able to determine a plan to alter reality to match the desired state when it changes. In some cases, the tool lets users interact with this state directly (Pulumi and Terraform), and in other cases, the state is abstracted away from the user behind a service (AWS CloudFormation). In other cases still, the user can pick between these two experiences based on power/convenience (Pulumi). In all cases, it exists in some form.

- [They have an engine](/docs/intro/concepts/how-pulumi-works/) which understands how to evaluate this expression language to create a desired state, map logical resources to physical ones, track dependencies for purposes of correct operation order and parallelism, diff declared state against the last-known state, and to devise a plan consisting of a specific sequence of create, read, update, and delete (CRUD) operations which will converge the actual real-world state with the desired state.

- [They have an extensible resource provider model](/docs/intro/concepts/resources/providers/). These providers are typically plug-ins that implement the CRUD operations. It is extensible because the world of resources is expected to grow significantly over time. This is especially true for multi-cloud infrastructure as code tools, which often allow for management of resources across many public, private, and hybrid cloud and SaaS resource providers, and even allow for custom extensions for managing infrastructure of your own choosing or creation.

- [They offer a way to serialize that plan independent of applying it](/blog/announcing-public-preview-update-plans/) for change control.

- They keep track of everything that has been deployed, inherent in the way the last-known deployment state is tracked and diffable from one deployment to the next.

- They sometimes offer a way to compare the last-known state, to the current real-world live state, to detect so-called “drift.” Drift is when the live state no longer matches the last-known deployed state, either due to manual changes (e.g., someone logs into the AWS console and opens up an SSH port to a server), or automation running outside of the purview if the infrastructure as code tool (e.g., a nightly script).

- Finally, they offer a way to destroy an environment in the case it needs to be partially or completely torn down.

I should note that most tools operate in one of two modes:

- **On-demand**: you must decide to run the tool, and at that moment, it will produce a desired-state, compare it to the last-known state, devise a plan, and carry it out. Often, but not always, a human is involved in deciding to review and/or apply the changes.

- **Continuous control-loop**: the tool simply runs regularly, sometimes reactively (such as when an event like a Git commit occurs), constantly producing new desired-states, comparing to the last-known state, and updating things as needed. Typically, a human is not involved in deciding to review and/or apply the changes.

Some tools, like Pulumi, offer both models, as each can be useful for different purposes: you can run the CLI at discrete times, trigger deployments from a [CI/CD pipeline](/docs/guides/continuous-delivery/) or [Kubernetes Operator](/docs/guides/continuous-delivery/pulumi-kubernetes-operator/), or using [arbitrary automation program logic](/automation/) with ultimate flexibility.

## Cloud Resources as Building Blocks

Up to now, we’ve described infrastructure as code in the usual way: as a way to provision and/or configure cloud building blocks. Consistent with the “infrastructure should be boring” meme, the way we describe it often  sounds boring too. But what we discovered when we started Pulumi is that it’s anything but boring. The ability to program the cloud is precisely what lays the foundation for our original goal of making the cloud 100x easier, and to unlock new experiences.

We began by exploring a new cloud programming language. Our founding team had collectively created, helped to found, or spent significant time developing, over a half-dozen languages over the years (C#, C++, Visual Basic, J++, F#, VB.NET, and research languages like M#, Spec#, and Axum, to name a few). We quickly realized something: just as with our async/await experiences back in the multicore days, most of the challenges you run into building modern cloud applications simply don’t require a new language. (We’ll get into this more in the next post.) But there was definitely something missing: an application and programming model for cloud resources.

To explore this point, let’s keep rolling with the operating system analogy:

If you sit down to write a typical Linux, macOS, or Windows program, do you split your application code entirely from the code which manages and interacts with the operating system? In certain cases, sure, but for most of us, we just program against usable APIs and let the operating system do its magic. If we need a file, we open it – sometimes thinking about the lifetime of that handle, but especially in higher-level languages, we just use it to do some I/O. If we need to schedule a thread, we spin one up, or just use a convenient asynchronous programming framework. If we want to interact with a hardware device, we just call some APIs. If we want to install, configure, update, or delete an application or utility, we probably just use some standard package manager or our operating system’s built-in application model facilities.

There are even higher-level languages and runtimes like Node.js, Python, and Ruby, which are operating system-agnostic. They pick the right level of abstraction to be able to work with files, spin up tasks, and send network requests, without needing to know the intricacies and peculiarities of every operating system and platform API that you’re using. This form of “multi-operating system” is very suggestive of what might be possible with “multi-cloud.”

As we’re using these operating system capabilities, what’s happening under the hood?

It turns out, a lot! The operating system is allocating and managing resources for a desired lifetime. That may require explicit participation by my application, or perhaps the ref-counting is abstracted away by finalizers in my language runtime of choice. It is also mediating between many competing requests. In the case of the scheduler, it is making intelligent choices to maximize latency and responsiveness, or throughput, depending on whether I’m on a server or in an interactive environment. It is authenticating, authorizing, and applying security policies.

Well, why can’t we just interact with cloud resources the same way? Why must I write dozens of lines of configuration goo for every serverless function that I want to spin up?

## The Programmable Cloud

The problem with cloud infrastructure is that it is more durable than most operating system resources. Whereas a process, thread, or file handle likely exists only so long as its parent process exists, a server, function, cluster, network, etc., may have a lifetime measured in days, months, or even years. The containment hierarchy also isn’t self-evident because, unlike with operating systems, cloud infrastructure isn’t “contained” by anything per se. A distributed application is made up of many parts and it’s not always clear what piece owns what.

That’s what leads to the discrete provisioning and configuring. Not all is lost, though. In the early days of operating systems and languages, we had very limited and explicit tools too. In many ways, we’re still in the days of writing assembly language – slowly advancing to C – and fumbling with low-level systems APIs like POSIX and Win32. We have yet to invent or begin to use the equivalent to Java, .NET, Node.js, Python, Ruby, and those lovable developer experiences.

But this is the very opportunity that excites us about Pulumi's approach to infrastructure as code. Every new platform starts with foundational building blocks. Infrastructure as code gives us a solution to the automation maturity problems above, sure, which is terribly important. But even more excitingly, by leveraging great programming languages, it also gives us the missing programming, application, and resource models needed to unlock immense innovation at higher layers in the stack. In short, infrastructure as code lets us program the cloud.

You can see that in action with normal Pulumi programs, where you get the full expressiveness of a language, in cases where you need for loops, conditionals, or abstraction by way of functions, methods, classes, or entire packages. This especially begins to shine with our [Automation API](/automation/), which began with the question of, “What if infrastructure as code was just a library and extension of my code, rather than being an entirely separate CLI tool?” You can see some of the power of bringing application and infrastructure code closer together with features like [Magic Functions](/blog/lambdas-as-lambdas-the-magic-of-simple-serverless-functions/), which let you just write serverless lambdas as lambdas in your language. And, of course, the ability to abstract and encapsulate common patterns eliminates copy-and-paste, delivers built-in best practices, and lets us move beyond endlessly stitching together building blocks, and towards real reusable architectures like our [Crosswalk for AWS](/docs/guides/crosswalk/aws/).

And from here we can build bigger things atop smaller things, the secret to the progress we have made in computer science for decades. And we think that’s enormously exciting.

## Winding Down

5 years! This journey started with a [big vision](http://joeduffyblog.com/2018/06/18/hello-pulumi/) and the key insight was to marry infrastructure as code with general-purpose languages, with an engine that is truly universal: any cloud, any language, any kind of architecture or cloud resource, and any cloud builder, developers or infrastructure experts alike. We are only getting started, but have made some terrific progress.

It has been wonderful to see infrastructure as code evolve in the industry in the past few years. Pulumi alone has seen explosive growth in our community and customers. A year after we launched, AWS shipped their own Cloud Development Kit (CDK) which is closer to the Pulumi programming model than anything else out there. We have seen the Pulumi and CDK approach subsequently applied to other deployment technologies than just AWS CloudFormation.

In this article, we’ve reviewed a bit of the backstory to infrastructure as code, and why this new approach is so exciting. We’ve witnessed the evolution from mostly static, slow-moving architectures, with configuration-based tools, to the modern world of dynamic, fast-moving complex distributed systems, with provisioning-based tools. We’ve seen that by thinking of the cloud as the new operating system, and by re-imagining infrastructure as code as the missing cloud resource model, we’ve laid a foundation that we can then now use to innovate up and down the stack, taking a major leap forward into our exciting distributed computing future.

But to do that, let’s first examine a bit more of the how, what, and why with respect to programming languages. Back in 2017, it seems the industry had decided “DSLs are best.” Taking any other path seemed radical and risky, and yet was essential to our goal, enabling us to stand on the shoulders of giants. We thought of creating a new language, which would have been fun, but ultimately decided to meet practitioners where they are and help bridge them to the cloud. Yet we faced a tough question: What language do we pick? Do we just pick one? If so, what one? Or should we embrace many languages? And what would that mean for our architecture, community, and ecosystem overall? Stay tuned – all of this is up next, and more!
