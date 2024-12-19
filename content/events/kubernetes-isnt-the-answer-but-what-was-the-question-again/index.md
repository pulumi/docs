---
# Name of the webinar.
title: "Kubernetes isn’t the answer but what was the question again?"
meta_desc: In this session, you'll learn to discover how to ask the right questions and how to find the right answers, using Kubernetes as an example.

cloud_engineering_summit:
    track: build

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
url_slug: "kubernetes-isnt-the-answer-but-what-was-the-question-again"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Kubernetes isn’t the answer, but what was the question again?"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Kubernetes isn’t the answer, but what was the question again?"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/XZPof6IBr_U"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T13:10:00-07:00
    # Duration of the webinar.
    duration: "16 minutes"
    # Description of the webinar.
    description: |
        What if I told you that you're making technology choices the wrong way? Instead of looking at the potential of a technology, we need to look at its potential friction, and take a step back to wonder what the question was, again.

        The right choice is almost always the technology that is the simplest and the easiest to implement. Rarely do teams need all the new technological innovations at once; instead they just want their biggest bottlenecks solved with the least amount of change. And you guessed it: those bottlenecks are often organizational in nature, not technological.

        Join me on the journey, using Kubernetes as an example, to discover how to ask the right questions, and how to find the right answers. You'll learn how technology impacts how people and organizations work, using metrics like cycle and takt time, one-piece flow, context switching, and adoption rate. We'll look at why simple and easy trump technological capabilities, and why avoiding complexity and organizational friction are key.

    # The webinar presenters
    presenters:
        - name: Joep Piscaer
          role:

# This section contains the transcript for a video. It is optional.
transcript: |
    Thanks for attending my talk on making technology choices the right way. My name is Joep Piscaer. My handle on Twitter is at jpiscaer I'm an independent industry analyst and tech marketer at CLA tech. You may wonder what the TLA stands for, but it's just a three-letter acronym. So let's begin with the why, why are we here? Well, we're here because everyone's talking about Kubernetes, the technology aspect of it and its potential, but I don't hear many people talking about the consequences over making one technology choice over another.

    And it looks like we often forget what problem we're actually solving. Take, for example, this self-operating napkin, which is definitely a solution. What problem it solves though? No one knows. And this happens with Kubernetes and other technologies too. And even Gardner agrees that Kubernetes isn't always the answer.

    Unfortunately, they didn't mention what the question was either. So unfortunately we, we still don't know. In this talk, I want to help you figure out what the question actually is by showing you how we are collectively making technology choices. No wrong way. Not that I'm not saying Kubernetes is the wrong choice per se.

    I'm just saying that the way we make technology decisions is often too technology focused. Now we all know Kubernetes has lots of potential. It democratizes infrastructure for developers. It allows them to deploy apps more easily, more quickly, more often using it's declarative constructs. It has a large ecosystem for things like CIC, security, storage, observability, you name it, but you shouldn't really look at that.

    Don't let the potential of the technology guide you. At least not too much, because potential is not real. Potential is unrealized success. Hope and hope is postponed disappointment. The burden of over-complicated technology is real and the future disappointment is too.

    The problem is if we don't know what business problems we're actually solving, how do we know if we're successful? And if we don't know that we'll end up adopting technology for technology sake. Kubernetes can solve many problems, but did we actually solve the right one? This animation kind of sums up why that's hard. The falling person on top is, is Kubernetes. The leaves are the organization and look at how long it takes before the organization starts moving. And how chaotically, it moves.

    You can do so much with the technology, but you would need to successfully adopted first, which requires changing the way your organization works in so many areas. It's just not realistic to change organizational structure, the way people work, team responsibilities, team dynamics. All at once. Organizations have natural inertia. They don't want to change, but once you do start the process of change, you'll notice friction in lots of unexpected places.

    So in order to be successful, you need to minimize the amount of simultaneous change happening. So instead of looking at the potential of a technology, we need to look at it as potential friction and how to successfully overcome that friction to be able to adopt new technology. Put differently, if we know that change, any change requires us to put in effort to overcome the inertia. We can decide whether the sum of technological potential is worth the friction that we need to overcome. Is it worth it? And a key part of overcoming friction is reducing complexity because complexity does create that friction and friction kills your chances of successfully adopting a technology.

    And often teams don't need all features at once right now, maybe they'll need them in the future, who knows, I mean, look at the amount of tools on this Swiss army knife. Do you need them all at once or even at all? And so the right choice is almost always the technology that's the simplest and easiest to implement while still solving the business problem. That piece of technology could be anything from a serverless function to a fully fledged Kubernetes platform or something in between maybe a managed SASS service. Again, I'm not arguing against one over the other. I'm just saying that if you minimize the complexity that causes organizational friction, you'll have a much higher chance of success because you'd take the limits of how much your organization can handle in terms of change into account.

    So we now know that we're solving for organizational friction and inertia, the incapacity to change. If there's one thing I want you to take home is that your almost always solving an organizational limitation alongside the introduction of a new piece of technology. Business problems are rarely addressed merely by technology solutions. So that's why I recommend taking a minimalist approach to technology. You solve the business problem with the least of least amount of change.

    Literally you minimize the amount of tech you use to solve the business problem, and you focus on the organizational side of things. So for Kubernetes, that could mean implementing the core scheduler, but not introduce observability or fixed up one specific issue with releasing because the team is bound by a third-party outsourcer, but not give them, you know, artists curling just yet, because that's too complex too much, or you move a team that's just beginning with containers to a bare bones environment so they can get accustomed to containers in the first place without explaining them what chat ops is. I'm just giving an example here. So all of this also means you need to solve organizational problems before while, and after introducing technological solutions. As I know, solving organizational problems is much harder and much less fun than introducing new technology solutions.

    I mean, that's why I'm giving this talk At a company I used to work at years ago, we had a saying, don't try to solve organizational issues with technical solutions. And we lived this mantra, but I feel the adoption of technology and enterprises in the last couple of years pushed this approach to the background a bit too much or too technology focused, not enough focus on the organizational side. And this is to me, what makes making the technology choices the right way is all about awareness of the organizational limitations and issues and choosing the right technology to match those limitations. For instance, dev ops teams with both Devin ops, it works great if you develop an app in house, but what do you deal with a commodity off the shelf application that only needs ops. Outsourcing is an, are a big indicator of organizational friction, the contracts, the financials involved, the project management.

    They all stand in the way of making the right technology choices the right way. Instead technology choices, take a back seat to the outsourcer, trying to remain relevant. Often bearing themselves in processes, handovers dependencies, or you have those traditional long cross-functional teams, silos of different teams in different roles, in different teams using tickets and queuing to get things done. And we all know ticketing system as a communication communication method just don't work no matter how much technology you throw at it. And similarly, if you have a lot of handovers across or even within a team, you won't be able to release quickly and often, regardless of whether you're using Kubernetes or another piece of technology.

    So again, indicating you'll have an organizational problem. You cannot really solve that by technology because handovers are often a sign of unhealthy inter-team dependencies due to command and control hierarchies. And they probably have historical instead of actual good reasons for organizing that way. Again, if you have to break, you have to break down these paradigms before you can really reap the benefits of communities and other cloud native technologies. And let's not forget shared responsibilities across teams blurring the lines of who's responsible for what.

    And so that kills the ability to do technological innovation quickly because you need sole or end to end responsibility to fix those unclear boundaries. Likewise, too many stakeholders are a sure fire way to grind innovation to a halt. So approval gates, long chase control, processes, chains, advisory boards, they're all signs of organizational issues that you need to address before and during the introduction of new technology and while not entirely organizational, if you still have inflexible computer environments, it does indicate you're lagging behind the enterprise It adoption curve, which means you probably shouldn't seek out bleeding edge technology just yet take small steps first. In addition, DIY technology platforms without using managed services is another sign of organizational issues. Kubernetes, for instance, isn't a core business for the vast majority of you companies out there, unless you are in the business of selling Kubernetes, either as a service or a distribution, but if you're not, why the heck are you DIY in the platform? Often that's because that's what engineers do not because that's what the business wanted.

    Another indication of organizational issues are high cycle time and high lead time for any type of work. So usually these indicate your teams can effectively pick up a piece of work, executed, call it done, but whether those times are high because of handovers, low degree of automation or other blockers and bottlenecks, it's kind of hard to tell, but it's definitely worth diving into just like too much work in progress, which indicates you have too much active work in your system leading to lower quality manual work and lots of rework. So work in progress is also an indication of bad automation and toil in general, which can be caused by any number of things. For instance, past technology choices gone wrong, historical organizational reasons. And so the solution to all of this, isn't simple, or even a single solution.

    Certainly there's no amount of technology that'll fix your organization if it's broken. So don't introduce Kubernetes. If you don't at least partly have solved these and other organizational challenges, one big way that technology can help solve issues is by creating on demand, self service consumption models of services in a vending machine type model. So these can be services for anything from setting up a cloud tenant to a best practices, ready to go secure database, or even a new Kubernetes cluster in the cloud. Self-service cuts, inter-team dependencies.

    It reduces queuing and handovers. It removes those human approval gates and ticketing systems. It reduces lead time, cycle time. So technology can definitely play a supporting role use Kubernetes if you have to have a business driver to do so, but don't default to it, figuring out what organizational challenges you actually have can be hard. One way of finding out is by doing a value stream mapping, a way to see how work flows through an organization.

    In addition to mapping out value streams or work in your organization, you can map the role technology has in each of these steps. This helps make visible whether you have an organizational problem or technical problem, or more likely a combination of both. It helps you visualize where you have dependencies, handover, toil, high cognitive load complexity, inefficient team structures, high lead on cycle times and too much work in progress. Often the so-called red items are a sign of overly complex path technology choices or some organizational inertia that is overdue for some action. So annihilate these red steps, unfortunately diving into the how of fixing your organization is a bit much for a short talk like this, but by doing a VSM you gain insights into how your organization works, allowing you to move away from that big bang transformation dream and removing reds from your workflow.

    And by automating, by introducing new technology while taking those organizational limits into account, you can start to continuously improve, becoming better at dealing with the organizational friction that happens every time you go through a valley like that, and instead have many little happy accidents that you'll learn from, and that actually solve your business problems, creating a solid bedrock to start adopting newer and more bleeding edge technology. Put differently, you can reduce the risk and associated cost by making continuous small improvements to your organization. Instead of following some technological pipe dream where someone sells you, Kubernetes. Small, but continuous improvements help your organization climb out of that valley of despair of bad organizational culture and technology can start to play a bigger and bigger role. Now introducing new technology without thinking about its adoption and the organizational friction, the adoption will cause, you will guaranteed introduce rework; things you have to do over.

    Rework can take a while to show, but it's missed quality that will rear its ugly head sometime not only does it create technical debt, it will also add to the cognitive load later in the lifecycle, forcing engineers to spend time on fixing a platform and doing operational support work instead of creating new applications or delivering new features. So in other words, if you account for the maturity of your organization, you will prevent missteps along the way with a better adoption as a result. So hopefully you start recognizing that the organization you're introducing technology to has to be ready for that technology. Often however, that's not the case. Introducing new technology will not solve much in those cases, even if it takes a while for that new car smell to disappear.

    I hope I helped you realize that technology is but a small part of successful organizations and that successful organizations are organizations that solve their own inertia and friction with you guessed it. Organizational improvements, not technology advancements. I mean, who am I kidding? Of course you need Kubernetes, Kubernetes, all the things come on, ignore me at will, but for now, thank you for listening. Feel free to ask a question in the Q and a below or hit me up on Twitter until next time.
---
