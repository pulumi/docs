---
# Name of the webinar.
title: "Rethinking the SDLC"
meta_desc: "This talk introduces this new model and discusses the need for how we talk about software to match the experience of development."

cloud_engineering_summit:
    track: keynote

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars
layout: cloud-engineering-summit-replay

# External webinars will link to an external page instead of a webinar
# landing/registration page. If the webinar is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the webinar page created.
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "rethinking-the-sdlc"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Rethinking the SDLC"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Rethinking the SDLC"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/42rWrRycw_o"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T08:00:00-07:00
    # Duration of the webinar.
    duration: "21 minutes"
    # Description of the webinar.
    description: |
        The software (or systems) development lifecycle has been in use since the 1960s. And it’s remained more or less the same since before color television and the touchtone phone. While it’s been looped it into circles and infinity loops and designed with trendy color palettes, the stages of the SDLC remain almost identical to its original layout. Yet the ecosystem in which we develop software is radically different. We work in systems that are distributed, decoupled, complex and can no longer be captured in an archaic model. It’s time to think different. It’s time for a revolution. The Revolution model of the SDLC captures the multi-threaded, nonsequential nature of modern software development. It embodies the roles engineers take on and the considerations they encounter along the way. It builds on Agile and DevOps to capture the concerns of DevOps derivatives like DevSecOps and AIOps. And it, well, revolves to embrace the iterative nature of continuous innovation. This talk introduces this new model and discusses the need for how we talk about software to match the experience of development.

    # The webinar presenters
    presenters:
        - name: Emily Freeman
          role: Principal, DevOps Solutions, AWS

# This section contains the transcript for a video. It is optional.
transcript: |
    Hi, I'm Emily Freeman. I'm the author of "DevOps for Dummies" and the co-curator of "97 Things Every Cloud Engineer Should Know." I am thrilled to be here with you all and I just want to thank Pulumi and the team for inviting me to speak and share this wild idea. A complete re-imagining of the SDLC. I want to be clear before I even get into this, I want your feedback.

    I came up with this wild idea, but I want to make sure that it works for you and your specific situations and I want to hear how you think it could be improved. You can always find me on Twitter, @editingemily. Most of my work centers around DevOps and I really can't overstate the sheer impact the concept of DevOps has had on the tech industry. In many ways it built on the foundation of Agile to become a default, a standard we all reach for in our everyday work. When DevOps surfaced as an idea in 2008, the tech industry was in a vastly different space.

    AWS was in infancy, offering only a handful of services. Azure and GCP didn't exist yet. The majority of companies maintained their own infrastructure. Developers wrote code and relied on sysadmins to deploy new code at scheduled intervals. Container technology hadn't been invented.

    Applications adhered to a monolithic architecture. Databases were relational, and server-less wasn't even a concept. Everything from the application to the engineers was centralized. Our current ecosystem couldn't be more different. Now, software is still hard, don't get me wrong.

    We continue to find novel solutions to consistently difficult, persistent problems. Now some of these end up being a sort of rebranding of old ideas, but others are a unique and clever take to abstracting complexity or automating toil, or perhaps most important, rethinking, even challenging the premises we have accepted as canon for years, if not decades. In the years since, DevOps has attempted to answer the critical conflict between developers and operations, engineers. DevOps has become a catch all term. Then there have been a number of derivative works.

    DevOps means 5,000 different things to 5,000 different people. Now for some, it can be distilled to continuous integration, continuous delivery, CI/CD. For others, it's deploying code more frequently, adding tests. For others still, it's organizational. They've added a platform team, perhaps even a questionably named DevOps team, or have created a engineering structure that focuses on a separation of concerns, leaving feature teams to not only develop, but also deploy, secure and maintain their siloed services.

    Whatever the interpretation, what's important is there isn't a universally accepted standard for what DevOps is or what it looks like in execution. It's a philosophy, more than anything else. A framework that everyone can utilize to configure and customize their specific circumstances to modern development practices. The characteristics of DevOps that I think we can all agree on is that it attempted to capture the challenges of software development along the entire path, from start to finish. It's that broad umbrella, that holistic view that I want to breathe life into again.

    The challenge we face is that DevOps is an increasingly outmoded solution to a previous problem. Developers now face cultural and technical challenges far greater than they did a decade ago. Cloud native is the future, the next collection of default development decisions and one the DevOps story can't absorb in its current form. I believe that era of DevOps is waning. And in this moment, as the sun begins to set on DevOps, we have a unique opportunity to rethink, rebuild.

    Now, I don't have a crystal ball that would be mighty handy. I'm not completely certain what the next decade in tech looks like, no one does. I know that I can't write this story alone. I need you. But I have some ideas to get the conversation started.

    I believe to build on what was, we have to throw away assumptions that we've taken for granted all this time. In order to move forward, we must first step back. The Software or Systems Development Lifecycle, what we call the SDLC, has been in use since the 1960s and it's remained more or less the same since before color television and the touch-tone phone. Over the last 60 or so odd years, we've made tweaks, slight adjustments. We've zhuzh-ed it a bit.

    The stages and steps are always slightly different. With Agile, we made it a circle and DevOps, an infinity loop. We've added pretty colors, but it's more or less remained the same. And the SDLC has become an assumption. We don't even think about it anymore, it just is.

    Universally adopted constructs like the SDLC have an unspoken permanence. They feel as if they have always been and will always be. I think the impact of that is even more potent if you were born after a construct was popularized. Nearly everything around us is a construct, a model, an artifact of a human idea. The chair you're sitting in, the desk you work at, the mug from which you drink coffee and sometimes an after-work beverage, buildings, toilets, plumbing, roads, cars, art, computers, everything.

    The SDLC is a remnant, an artifact of a previous era. And I think we should throw it away, or perhaps more accurately, replace it. Replace it with something that better reflects the nature of our everyday work. A linear, single-threaded model, designed for the manufacture of material goods cannot possibly capture the distributed complexity of modern socio-technical systems. It just can't.

    And these two ideas aren't mutually exclusive, that the SDLC was industry-changing, valuable and extraordinarily impactful, and that it's time for something new. I believe we are strong enough to hold these two ideas at the same time, showing respect for the past while envisioning the future. I don't know about you, I have never had a software project go smoothly in a single go. It's always chaos. Software is a study in entropy and it's not exactly getting any more simple.

    The model with which we think and talk about software development must capture the multi-threaded, non-sequential nature of our work. It should embody the roles engineers take on and the considerations they encounter along the way. It should build on the foundations of Agile and DevOps and represent the iterative nature of continuous innovation. When I was thinking about this, and I took a lot of time to think about it, I was inspired by ideas like extreme programming on the spiral method or model. They were getting pretty close.

    I wanted something that would have layers, threads even, a way of visually representing multiple processes happening in parallel. What I settled on was the revolution model. I believe this visualization is capable of capturing the pivotal moments of any software scenario. And I'm going to dive into all the discreet little parts, but I want to give you a moment to have a first impression and really absorb my idea. I call it revolution because, well, it revolves.

    Its circular shape reflects the continuous and iterative nature of our work, but also because it is revolutionary. I am challenging a 70-year old model that is embedded into our daily language. I don't expect Gartner to build a magic quadrant around this tomorrow, but that would be really cool, and you should call me. My mission in this is to challenge the status quo and create a model that I think more accurately reflects the complexity of modern, cloud-native software development. The revolution model is constructed of five concentric rings describing the critical roles of software development.

    Architecting, developing, automating, deploying, and operating. Intersecting each loop are six spokes that describe the production considerations every engineer must consider throughout the development process. Testability, securability, reliability, observability, flexibility, and scalability. The considerations listed are not all encompassing. That's probably what a lot of you are thinking.

    There are, of course, things not explicitly included, but I figured if I added all the considerations we have to think about, we may get a little overwhelmed. Certainly, I would. Now let's dive into each element. We have long used personas as the default way to divide audiences and tailor messages, to group people. Every company in the world right now is repeating the mantra of, "Developers, developers, developers," but personas have always bugged me a little bit because the approach is typically either oversimplifies someone's career or needlessly complicates it.

    Few people fit cleanly and completely into persona-based buckets like developers and operations anymore. The lines have gotten fuzzy. On the other hand, I don't think we need to tailor messages so specifically as to call out the difference between a DevOps Engineer and a Release Engineer or a Security Administrator and a Security Engineer. But perhaps most critically, I believe personas are immutable. A persona is wholly dependent on how someone identifies themselves.

    It's intrinsic, not extrinsic. Their titles may change, their jobs may differ, but they're probably still selecting the same persona from that ubiquitous drop down we all use when registering for an event, probably this one too. I was a developer. I will always identify as a developer despite doing a ton of work in other areas like DevOps, AIOps, DevRel. I think about problems from the perspective of a developer.

    It influences my thinking and my approach. Roles are very different. Roles are temporary, inconsistent, constantly fluctuating. If I were an actress, the parts I played would be lengthy and varied, but the persona I would identify as would remain an actor, an artist. Your work isn't confined to a single set of skills.

    It may have been a decade ago, but not today. In any given week or sprint, you may play the role of architect thinking about how to design a feature or service, a developer building out code or fixing a bug, an automation engineer thinking about how to improve the manual processes that we often refer to as toil, a release engineer deploying code to different environments or releasing it to customers, or an operations engineer ensuring an application functions in consistent, expected ways. And no matter what role we play, we have to consider a number of issues. The first is testability. All software systems require testing of various types to assure architects that design works, developers that code works, operators that infrastructure is running as expected and engineers of all disciplines that code changes won't bring down the system, probably.

    Testing in its many forms is what enables systems to be durable and have longevity. It's what reassures engineers that changes won't impact current functionality and a system without tests is a disaster waiting to happen, which is why it's first among equals in this particular round table. Security is everyone's responsibility, but I think few of us understand how to design and execute a secure system. I certainly struggle with that. Security incidents, for the most part, are what we call high impact, low probability events.

    These are the really big disasters, the ones that get us all free credit reporting for a year and end up on the news. They don't happen super frequently. And thank goodness, because we all know that there are endless small vulnerabilities lurking in our systems. Security is something we know we should dedicate time to, but often don't make time for, and let's be honest, it's hard and complicated and a little bit scary. It's intimidating.

    DevSecOps, the first derivative of DevOps asked engineers to move security left. This approach meant that security was a consideration early in the process and not something that would block a release at the last moment. This is also the consideration under which I'm putting compliance and governance. Now it's not perfectly aligned, but I figure everything you call a lawyer for, should lived together. But in all seriousness, these three concepts are really about risk management.

    Identity, data, authorization. There's a ton of different derivatives, but the question is really who has access to what, when and how, and that is everyone's responsibility at every stage. Site Reliability Engineering or SRE is a discipline, a job, an approach, for good reason. It is absolutely critical that applications and services work as expected for the vast majority of time. That said, availability is often mistakenly treated as a synonym for reliability, but it's not.

    It's a single aspect of the concept. If a system is available and usable, but customer data is inaccurate or out of sync, the system is not reliable. Reliability has five key components, availability, latency, throughput, fidelity, and durability. Reliability may be the end result, but it's resiliency, for me, the journey, the action, that engineers can actually take to improve reliability. I'll talk more about that in another talk.

    Observability is the capability to have insight into an application or system. It's the combination of telemetry, monitoring, alerting, all of it. Everything that is available to engineers and leadership to have visibility into their system. There's an aspect of observability that overlaps with reliability. But for me, the purpose of observability isn't to maintain a reliable system, though that is important.

    Instead it's the capacity for engineers working in a system to have that visibility to the inner workings of that system. The concept of observability originates in linear dynamic systems, fancy, and is defined as how well internal states of a system can be understood based on information about its external outputs. It's critical when companies move systems to the cloud or utilize managed services that they don't lose visibility and confidence in their systems. The shared responsibility model of cloud storage, compute and managed services require engineering teams to be able to quickly be alerted to, identify and remediate the issues as they arise. Flexible systems are capable of adapting to meet the ever-changing needs of the customer and the market segment.

    Flexible code bases absorb new code smoothly, embody a clean separation of concerns, are partitioned into small components or classes and are architected for the now, as well as the next. And flexible systems change dependencies are reduced or eliminated ideally. Database schemas accommodate change well and components communicate via a standardized and well-documented API. The only thing constant in our industry is change. And in every role we play, creating flexible systems and solutions that will grow as the applications grow and the customer base grows is critical.

    Finally, scalability. Scalability refers to more than a system's ability to scale for additional load. It implies growth. Scalability in the revolution model carries that continuous innovation of a team and all the byproducts of that growth within a system. And for me, scalability is the most human of the considerations.

    It requires each of us in our various roles to consider everyone around us. Our customers who use the system and rely on its services, our colleagues, current and future, with whom we collaborate and even our future selves. Pulumi has this great perspective on cloud engineering, that it can be divided into three main components, build, deploy, and manage. I really love this. It's simplicity and clarity, and I especially love how it fits the new model.

    If you overlay cloud engineering onto revolution, you get this perfect target that allows all of us to focus on the various roles and considerations. Software development isn't a straight line, nor is it a perfect loop. Software is an ever-changing complex dance. There are twirls and pivots and difficult spins, forward and backward, engineers move in parallel creating truly magnificent pieces of art. We need a modern model for a modern era, and I believe this is just the revolution to get us started. Thank you so much.
---
