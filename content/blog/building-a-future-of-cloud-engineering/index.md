---
title: "Building a future of cloud engineering"
date: "2018-10-22"
meta_desc: "Using your favorite general purpose programming language to define your cloud infrastructure and applications. Program the cloud with Pulumi."
authors: ["joe-duffy"]
tags: ["Pulumi-News"]
---


We founded Pulumi because of a deeply held belief that the cloud
promises to change all aspects of software development and that there
remains an incredible opportunity to reimagine the entire experience,
from idea to creation to delivery to management, with one person in
mind: you, the engineer.
<!--more-->

Too often, we still think of the cloud as an afterthought, as though it
were still 1998 with virtual machines and XML configuration. At Pulumi,
we believe instead that the cloud is a first class application
architecture concern. We still use thankless tools, markup languages,
and brittle, homegrown delivery platforms. At Pulumi, we believe instead
in a lovable and productive development experience, with excellent
collaboration and reuse.

Since getting started just over a year and a half ago, we've stood on
the shoulders of giants, tapping into decades of progress our industry
has made in programming languages, runtimes, and frameworks, and
marrying it with all the amazing innovation in cloud containers,
orchestrators, managed data and AI services, and serverless
capabilities.

The best part of this journey has been hearing from our [passionate
community](https://slack.pulumi.com/). Thousands of engineers, and
hundreds of companies, have created and deployed cloud applications and
infrastructure using Pulumi. We are proud to be [an open source
company](https://github.com/pulumi/pulumi), and thrive on the daily
collaboration and evolution of the platform.

And we're just getting started! Today we are thrilled to announce that
we've raised $15M in additional funding from our partners, Madrona
Venture Group and Tola Capital, both here in Seattle. We are honored by
their shared belief in our vision and our team. [Read more in our press
release.](https://info.pulumi.com/press-release/pulumi-announces-15m-in-series-a-funding-to-accelerate-development-and-adoption-of-its-cloud-native-development-platform)

## How We Got Here, a Tale of Cloud Evolution

We have seen stunning advancement in cloud platform capabilities. It's
hard to believe that Docker was launched just five years, and AWS Lambda
only three, ago! And yet, these technologies change all aspects of how
we create, deliver, and manage cloud software. Meanwhile, the cloud has
become more programmable with APIs everywhere.

At the same time, "DevOps" as an approach to organizing teams and
developing software has matured greatly, and is now the default for many
organizations. New practices such as infrastructure-as-code, immutable
infrastructure, and Site Reliability Engineering have modernized these
roles, giving us approaches that can leverage a more rigorous software
engineering practices to tasks that used to be more ad-hoc, manual, and
error prone.

But despite these fundamental changes, the way we engineer the cloud
hasn't fundamentally changed. As cloud engineers, we still think of configuration as an
afterthought and a task best suited for JSON, YAML, or DSLs. Each
individual resource we provision -- even fine-grained ones like
serverless functions -- requires often an equal amount of configuration
as there is actual application code. The lack of expressiveness has led
us to resort to bolting on templating systems, writing mountains of
bash, and overall find ourselves swimming in a sea of complexity.

The problem is, these are crude approximations of real languages. They
lack real abstraction, sharing, and reuse. You can't fire up your editor
and refactor, test, or analyze your code to find bugs ahead of time.
Instead, you find simple syntax errors when it's too late, after
production is on the floor. Developers hate to touch those configuration
languages, and yet simultaneously operators want to be more productive
and empower their teams to collaborate.

It's safe to conclude: we have hit the limits of the "afterthought"
approach.

## Towards Cloud Engineering

We believe in a future where developers and operators alike can meet on
common ground to work together. We like to call this combined discipline
**cloud engineering**. It's not Dev, it's not DevOps, and it's not
SRE; cloud engineering is the best of all of them. In this new future, our teams will
experience more joy, collaboration, and productivity than ever before.

Enter Pulumi.

Using your favorite general purpose programming language -- whether it
is JavaScript, TypeScript, Python, Go, or something else -- you can
express the entirety of your cloud software. As a cloud engineer, you can develop it in your
favorite editor, with statement completion, built-in documentation, and
interactive feedback when you've got something wrong. You can test
things and benefit from static analysis and linters that enforce best
practices. You can reuse packages, publish your own, and refactor your
code just like with application code. In fact, after living in this
world for long enough, the boundary between infrastructure and
application code begins to blur.

This has led to a phrase we use a lot at Pulumi -- **program the
cloud** -- our rally cry, if you will.

Just like code, we can collaborate with source control systems like Git
-- code reviewing changes, pushing and pulling code to perform
deployments -- using easy but robust continuous delivery workflows.
Thanks to real languages, a cloud object model, and programmable cloud
APIs, the system has true semantic understanding of your cloud software,
its resources and their relationships, which can be used for rich
deployment statuses and to organize and find information more easily.
It's never been such a breeze to go from idea to production.

We've become enamored by this new approach to creating software that is
truly born in the cloud. But it's not just our own belief -- this new age of cloud engineering is
working terrifically in practice. We have worked with organizations of
all sizes -- small ISVs to Fortune 500 Enterprises -- to vastly
improve their team efficiency and velocity. We almost always reduce
configuration sprawl by an order of magnitude thanks to Pulumi, leading
to a level of productivity that these teams previously hadn't imagined
was possible. Developers, operators, and managers alike are loving
living in this future of cloud engineering.

## Pulumi's Next Chapter

We've only just begun. Pulumi supports AWS, Azure, Google Cloud
Platform, and Kubernetes in a big way, with early support for VMWare
vSphere and OpenStack. Our delivery platform works great with your
favorite CI systems. Expect to see continued growth in all of these
areas, in addition to new clouds, languages, and integrations.

Today we launched [the Team Edition]({{< prelref "/pricing" >}}) for our
SaaS delivery platform. This includes many features that you, the cloud engineering
community, told us you need to better operationalize Pulumi within your
teams. We already have many happy customers using these features
successfully for organizations big and small. Expect to see a steady
stream of improvements, in addition to Enterprise Edition capabilities
for the largest of organizations needing on-premises, advanced security,
and custom identity. Please always [let us
know]({{< prelref "/contact.md" >}}) how we can better meet your
needs.

This new round of funding will allow us to strengthen our commitment to
open source and community, increase our R&D velocity, and also scale our
business to enable organizations of all sizes to successfully achieve
cloud engineering within their teams. We are [hiring in all areas of the
company]({{< prelref "/careers" >}}) as we enter this next exciting
chapter of the company.

[Download Pulumi]({{< prelref "/docs/get-started/install" >}}) -- we
can't wait to see all the great things you build next with Pulumi!

Joe & Eric
