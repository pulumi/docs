---
# Name of the webinar.
title: "The Future of Cloud Engineering: Culture, Process, & Tools"
meta_desc: "Learn from industry experts how teams and workflows are evolving to address the challenges of Cloud Engineering at organizations of every size."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars

# External webinars will link to an external page instead of a webinar
# landing/registration page. If the webinar is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the webinar page created.
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "the-future-of-cloud-engineering-culture-process-tools"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "The Future of Cloud Engineering: Culture, Process, & Tools"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "The Future of Cloud Engineering: Culture, Process, & Tools"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/akCODcU2vm4"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-10-08T10:00:00-07:00
    # Duration of the webinar.
    duration: "40 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Learn from industry experts how teams and workflows are evolving to address the challenges and opportunities of Cloud Engineering at organizations of every size.

    # The webinar presenters
    presenters:
        - name: Abby Kearns
          role: CTO, Puppet
        - name: Amanda Silver
          role: CVP of Product for Developer Tools, Microsoft
        - name: Jonathan Sullivan
          role: Co-founder and CTO, NS1
        - name: Avi Cavale
          role: VP of Engineering, JFrog
        - name: Lee Zen
          role: VP Engineering, Pulumi

# This section contains the transcript for a video. It is optional.
transcript: |
    **Lee Zen**

    Welcome everyone, to our panel on the Future of Cloud Engineering, especially around culture, process, and tools. We have a great panelist lineup here today. We have Abby Kearns, Amanda Silver, Jonathan Sullivan, and Avi Cavale. Thanks everyone for joining me today. I'll let each panelist introduce themselves, and then I'll talk a little bit about what we're going to be talking about today, and we'll jump right into it.

    I think we'll start in the order I see on my screen. And I have a fun warmup question for you all, so you can think about your answer to this, which is what is the best workplace perk you've ever had in your own opinion? Your favorite workplace perk since we're talking about teams and culture today. We'll start with Abby, please. And yeah, let us know about yourself and your favorite workplace perk.

    **Abby Kearns**

    Thanks, Lee. Abby Kearns, I'm the CTO at Puppet. A favorite workplace perk. I don't know, free coffee, I guess. I don't know. I'm still getting used to having workplace perks at all because my first 15 years of my career, there were no workplace perks.

    **Lee Zen**

    Amanda, you're next on my screen.

    **Amanda Silver**

    Hi. I'm Amanda Silver. I'm the CVP of Product Design and User Research in Microsoft's Developer Division. So we work on tools like Visual Studio Code, TypeScript, Visual Studio, all different kinds of developer tools and platforms. And my favorite workplace perk is definitely got to be comprehensive healthcare.

    **Lee Zen**

    Thanks, Amanda. Jonathan.

    **Jonathan Sullivan**

    Hi. I'm Jon Sullivan. I'm one of the co-founders and I'm CTO at NS1. And favorite workplace perk, I'd have to go with Abby on this one, coffee, just good coffee.

    **Lee Zen**

    Great. And Avi.

    **Avi Cavale**

    Hi. My name is Avi Cavale. I'm the Vice-President of Engineering for JFROG, focused on the Pipelines product of JFROG. I initially thought it was the workplace quirk, but I think I finally figured out it was perk. I'm glad other people went before me. My favorite perk would be I think we used to get haircuts at work. And I used to like that quite a bit.

    **Lee Zen**

    Awesome. That sounds really fun. I'd love to get a haircut.

    **Amanda Silver**

    No longer in quarantine, yeah.

    **Lee Zen**

    Exactly. Great. So today we're talking about culture, process, and tools, and really focusing on kind of as teams bringing applications to the cloud, often a big part of that is the tooling and the culture and the process that brings those applications there. And I want to talk about kind of how that's going to change as teams modernize and bring more and more to the cloud and kind of as the technology is changing more rapidly as well.

    I think I'll just open it up to everyone and start by asking kind of as your teams shifted to remote work this year, actually, I think that's an interesting place to start given we're all remote, what are some of the best practices you've observed and what are some of the mistakes you think teams should avoid?

    **Avi Cavale**

    Anybody can go?

    **Abby Kearns**

    I'll go first. I'll go from the avoid, maybe it's because this is something I'm currently struggling with, is the endless day of back-to-back Zoom calls. And so, I feel like Zoom fatigue is real and I feel like it's hard to replicate that in-person experience, that in-person opportunities for iteration. But at the end of the day, I do feel back-to-back Zoom calls just wears people down and makes people... My current thinking is it starts to make people less creative and less engaged.

    And so, I'm currently trying to figure out how do we shake things up, how do we really continue to build culture, keep teams engaged, but also figure out how to strike that balance, because I do feel like we all go into this slippery slope where we start our day with 6:00 AM Zoom calls and then continues on throughout the day, or Jon, I suspect in your case continues into the evening.

    And at the end of the day, you start to feel less productive and less engaged. And so, I think that's currently kind of the biggest challenge I'm trying to figure out how do I solve for. So if any one of you have any ideas, I'll take them.

    **Amanda Silver**

    I think what we found is that the transition during this period is not just work from home. It's work from home in the middle of a pandemic. And I think those two things are really, really different. I think one of the things that we're finding is that either because kids are also at home or because of the anxiety of the overall situation, there's just a lot of different psychological issues that are going on right now in terms of how people are able to show up at work and bring their best selves.

    And that's required a lot of adjustment and a lot of grace being given to employees to allow them to accommodate the psychological trauma that they're basically dealing with based on the fact that this is a pandemic situation.

    **Jonathan Sullivan**

    For us, we were about 30% remote before the pandemic hit. So, we had a pretty good culture in pockets of the company, but it was a real adjustment for different teams, particularly outside of engineering or outside of pockets, DevOps was very distributed, but the core team wasn't.

    One of the first things we did was there's a few companies out there, like HashiCorp and GitLab and Grafana, who are remote first. And they've all done some really good writing and have open-sourced their playbooks for building a solid remote-first culture. So there was a ton of really great advice in that. So finding companies who have already lived this.

    Some practical small stuff that we found really helps is requiring or encouraging people to leave both their video on and their microphones on. There's nothing worse than making a joke and trying to facilitate normal human interaction and then just having it echo in the silence because people are laughing into a muted microphone.

    So that's been really good from just a cultural perspective, and kind of welcoming the distractions if my dog is barking in the background or people who have kids, just acknowledging and not trying to hide the fact that we're all in this together working from home.

    I think Abby and Amanda have had great points around grace and boundaries. It's easier than ever to burnout. So helping people not feel bad about taking time, encouraging that, whatever little perks you can do for the team. We've gotten just good feedback from telling people, "Hey, take a day off," and also expensive dinner from Seamless or whatever local delivery thing you have on the company for you and your family, to just recognize that not only is it okay to take a break, but we want to encourage that. So that's been pretty helpful.

    **Avi Cavale**

    I think from a JFrog perspective, we worked remote quite a bit in a macro perspective. And we have distributed around the world, timezone complex, all of that stuff, we were all used to that. It was not that big of a change from that perspective. But what we did really miss is there used to be a lot of events where for example, in January, we had the entire company come to Cancun, and we do this thing called swamp hour, which is 600 people all fly into Cancun for a couple of days.

    And this time, it wasn't Cancun, but it's all over the world. But that kind of culture where there was a lot of in-person stuff that was going on in terms of morale, and everything took a big beating. So what we ended up doing is having a lot of leadership, all hands where people were communicating, and people were talking about what exactly was happening across the company, so that everybody just stayed connected.

    That was early on, and then slowly we ease that off once we felt like we started getting used to it. It was just people were very focused in trying to make sure that we don't lose touch with each other. And once we got that thing working, the process were already in there. We didn't really feel that much from just productivity and what we were shipping perspective.

    But it was just people that how they felt not having physical kind of presence in offices, which was causing them a lot of angst in which we kind of managed by just over communicating.

    **Lee Zen**

    And obviously, with the move to remote, lots of new tools and processes coming into place for various teams. Also curious, just that this is all happening in the backdrop of a large migration to the cloud by lots of companies, by lots of teams. And so also curious to hear what tools and processes you feel are having the largest impact on teams as they work today and what's coming in your opinion, that's going to have a big impact over the next few years.

    **Avi Cavale**

    I can go first on this one. I think the most important thing that we started doing is we started implementing this concept of communicate to yourself. Usually people think that communication is about I got to tell somebody what I'm doing or it sounds like as though it's an inquisition, even scrum meetings, everything it sounds like you're inquiring what exactly is happening and trying to prevent people from not slacking off.

    But what we ended up starting doing is we just communicate with yourself. Here's what I'm going to do. Here's what has happened. Here is where I'm stuck so that nobody really pings people to just ask them for status, they can all go look up on tickets and figure out where things are.

    So what ended up happening is the culture changed from people ping you to help you, as opposed to people pinging you to actually say, "Where are you in the process." So it became more collaborative. And I personally think that, that's one of the biggest things we need to do is to just communicate with yourself and let people go figure out what the status is. And that had really helped from a morale as well as productivity perspective across the teams.

    **Lee Zen**

    And Avi if you don't mind going a little bit deeper, what kind of tools do you use for that self communication?

    **Avi Cavale**

    You can use any ticketing system, whatever you're using, it's really not one tool or the other, it's more of if you're using GitHub issues, that's fine. If you're using JIRA, that's fine. But the idea behind it is, rather than having to speak in meetings, and we were really focused on reducing the Zoom burnout, we didn't want to have meetings. For us meetings was a sign of failure of how things should have actually happened. And so we were trying to get things back on track.

    So the way we kind of got done is just people would have JIRA tickets, which would fire automatic statuses into rooms, and people are following whatever topics they're interested in. Think of it as an RSS feed for your entire organization of what exactly is happening. And that really helped in terms of people pinpointing here is where I can help and places where I can't help I just did away from trying to just be a person in a meeting.

    **Amanda Silver**

    Yeah, I can definitely address both of those things. A couple of years ago, we started to study remote development teams and understand what are their biggest pain points. And there's a bunch of different things that we found, there's still so much pain in terms of what it's like to collaborate with somebody remotely.

    And there were two areas that we really focused on. One is how can we help developers collaborate on code, not just asynchronously post commit, but also pre commit? The problem when developers are working together is often not... It worked on my machine but actually it was broken on my machine. And I need your help to debug it. And so we started to work on a capability that we call live share, which actually allows two programmers to come in and basically have a pair programming environment where their code editor is shared and even their debug session can actually be shared.

    So that they can start to step through breakpoints and look at call stacks together, using their settings from their tools. Whether somebody has a different accessibility setting, high contrast mode, or other things like that, this we found to be incredibly helpful as everybody has transitioned to working from home. And it's become a daily tool for a lot of people both inside of Microsoft and outside of Microsoft.

    The other thing that we found as a big pain point is dev box setup. And we've all worked on containerizing applications over the past few years. But what's happened is we've now started to work on containerizing developer environments. And that has allowed us to basically make it really easy to replicate a dev environment, and then have that be hosted locally on a remote machine or in the public cloud.

    And so we've introduced those capabilities into Visual Studio Code and visual studio over the past couple of years. We found that to be super helpful as we've onboarded new developers, as developers start to take on new projects. In terms of what we think is coming, I think actually one of the most exciting things is the application of machine learning to coding.

    If you look at what are the most common CodeCommit comments that happen, a lot of it is style based so that developers can basically conform to the same styles as the rest of their development team. But also, obviously, there's best practices, idiomatic API call patterns, things like that. And these are things that we think that machine learning can actually help us codify. And then give developers guidance as they're typing code.

    **Jonathan Sullivan**

    Very cool. We've done a few similar things where as Avi mentioned, I think alignment is really critical. So if more meetings equals failure, knowing that and broadcasting that across the team so that everyone's on the same page, is really helpful because then everybody can contribute to one they understand what the cultural goal you're aiming for is and then two, you can start to get ideas from everybody on how to fix that. So for us, it's really important that we agree on and everybody knows what goes where and when, where conversations need to happen.

    For a lot of stand-ups, we just do this in slack now we have a little bot that every morning at some time just pings and we'll all jump in there. And that also hits on that idea of sort of a self check in to list out, here are the three things that I'm focused on today, or here's what happened yesterday, here's something I need help on.

    And then we have a few other slack channels or places in JIRA where different kind of thoughts go. So there's a cold brew cooler channel where it's just totally off topic. With a few guardrails to keep it civilized. And Hacker News Channel, that kind of stuff. There's another, maybe somebody remembers the name, it's totally escaping me at the moment, but particularly for new employees, where they can just basically post whatever it is they're working on, just broadcast it, and other people can kind of observe and if they're getting stuck on something they can jump in. I can't for the life of me remember what the term is for that. But that's been really helpful as well.

    **Abby Kearns**

    We're very similar here at Puppet Jon, we have the virtual slack stand up. So with a little bot, that reminds everybody. And for us, it's really been driving consistency and clarity around what we're working on, and where we're going next. And just the constant reminders of where we're evolving to, and as we implement more tools, and more services, how everyone can get access to those and really making sure there is a single system of record as it were for everyone, because there is a proliferation of tools.

    We're always trying to hone in a little bit more and start to connect the dots between what we're working on, what the different teams are working on around the world. And then how does that align to where we're going over the next 12, 18, 24 months,

    **Avi Cavale**

    I just want to add one more thing is that we went away from estimates. And that was something that didn't mean anything to us at all. What we ended up doing is something which is kind of what we call as critical chain program management, which is instead of looking from what I need to do, you just start from what needs to get done from a goal perspective, and you work backwards.

    So what ends up happening is things get broken down into subtasks, which are very manageable. So you start saying, let's assume like, I want to ship the next version of JFrog Pipelines, we start off with I want to ship it tomorrow, so why can't I do it, and then people start working backwards.

    We spend a lot of time upfront for a couple of days or three days in a group setting. We call it [inaudible 00:17:41] planning, where we break down all of the stuff into some sort of a bar chart. And then what we actually do is manage that from a... We have a visual diagram of all the stuff that needs to happen in terms of a graph and in terms of what needs to get done.

    And so we don't care about timelines, we just care about how many tasks are left, what percentage is complete. And then we look at risk. What ends up happening is we are focused mostly on mitigating risk in the plan as opposed to figuring out status and inferring risk. I think what we have done is, especially at JFrog, this is something that we are trying to do this across all of JFrog is that focus on actually having a good graph in terms of what needs to get done and have all the cross dependencies identified.

    So all the teams know where they become booking. And so most of our meetings are about blocking issues and prioritization issues where I need something from team B, and team B is working on something else. And because of that, I am blocked and I can't make any progress.

    It's more of like resolution of risks and figuring out what the plan needs to be as opposed to, "Hey, are we on track," because trust me on it, it's every single person. I mean, 20 years of software development, I've never had the first 80% of the project, say we are not on track.

    And I've never had a project in the last 20% where we were completely off track. I think it's super critical to kind of be more scientific about whether we're really on track or not. And that really helps pressure across the company. Because people are a lot more at ease, they know exactly what they need to do.

    **Lee Zen**

    So part of what you're talking about Avi I think is also, we're seeing teams move from longer release cycles toward more continuous development, continuous deployment practices, as teams also move toward the cloud. It's also kind of a natural fit to be able to do that kind of thing. I'm curious for all the panelists, what kind of tools and processes are you seeing teams undertake or use to help them make that transition? Or what advice would you give the teams that you think are going to help them become very successful in doing CICD?

    **Avi Cavale**

    I can go first because I work in that space quite a bit. I think people say a CICD in one breath. And that's a fundamental kind of flaw from what we're really talking about. They're fundamentally different aspects of it. What we really think about is, so there's a vertical wall that is in between CI and CD. So the idea behind it is CI is all about making sure my coordinator is not breaking, unit are surpassing, things are actually working.

    And there are no kind of security flaws or anything in the packages that I used and all of that stuff. At the end of the CI process, you get a checkpoint. And today, what we call that is a binary. It's some sort of a checkpoint, it could be as simple as a tarball on a zip file or whatever, but that basically is a version that is immutable, that says that this is blessed by my development organization.

    Now that wall is after... Anything to the right of that wall is what we call a CD. And that basically means you're actually assembling a bunch of these components to actually create a product that's meaningful and useful, that is deployable. So that's kind of where we see a fundamental difference between how people are trying to do.

    What people end up thinking is that, hey, from straight from get, I can actually do a deployment. You can do anything from anything. But the question is, is that the right thing to do from a macro perspective, and what we've also seen from our enterprise customers is that sometimes this whole notion of I can do constant changes, is very, very distracting for them.

    Because at the end of the day, we are in the tools business, and we are actually shipping something that allows other people to build software on top of it. And if you keep changing on how you're actually using this product, it is very, very distracting for all the [inaudible 00:21:50] because they're constantly in training mode, as opposed to execution mode, because you're so excited about shipping new features, but it's actually creating chaos in the customers who are actually using it.

    So what we ended up coming back to is yes, we have the capability to ship at any given point of time. And we use that significantly to do patching and bug fixes and everything so that people feel that if there is a feature that is having issues, we can get them, release is faster. But at the same point of time, we have gone into more of a structured release process for new features.

    And people need to make that decision. It's not like we are deploying Facebook and you're building enterprise applications on which are going into banks, which are going into healthcare, which are going in all kinds of stuff. And you just can't go and create a consumer behavior in that.

    So people need to understand what business they are in, what the customers expect and make sure that you're sending your processes, and not really combine CI and CD as like one single term. I mean, it's a completely different mindset. And it's important to think from the nuance of CI and CD.

    **Jonathan Sullivan**

    I think that's such a good point. Particularly that agility is only beneficial for things that need to be agile or benefit for being agile. And I'm sure there's a sports metaphor here somewhere where a tennis player is not going to be good at curling. And so things that don't need to move fast or change fast, you can undermine the stability of those systems by try to get them into continuous delivery, pipelines or practices.

    At our company, for example, we have a built pipeline that takes all of our software packages and runs it through all the tests that you would expect, and deploys it to basically a fake production environment that's not actually accessible to customers, but looks and feels and is treated exactly like production. And then from there, there's a manual rollout process, because sort of the critical nature of our platform. It's really making sure that I think, including those kind of CICD design principles, not as an afterthought, but as part of the development process.

    And how do we want to deploy this and what's the benefit we get from integrating with these various built processes and also as people are moving into that, I think a common place where we've seen, certainly ourselves go off track is biting off more than you can chew and trying to automate the whole thing versus finding a part that you'll benefit sort of the 80/20 rule or if I can automate this or automate the build container or development environments, like those are areas where there's huge game, and no operational problems if something goes wrong, because you can always build it manually.

    **Amanda Silver**

    I totally agree with the point that CI and CD are really not the same. And I think that also raises an aspect of one of the major transitions of moving to a DevOps mindset is, is also as you're moving to shipping constantly customer feedback and user feedback is also essential. And so there's all different aspects of how can we provide better insight into how the product is actually performing for customers. A lot of people think that this is something that only cloud or web applications can do.

    But this is also something that really all mobile and rich client applications should also be doing. So that they can get feedback from their users as they ship, and continually improve the success criteria for their customers, and shave off the edges of the customer journeys.

    And a big aspect of that is obviously things like feature flagging, but also things like experimentation, and AB experiments, which we've started to use a lot more heavily inside of, even our client applications like Visual Studio Code.

    **Abby Kearns**

    I wanted to add on, I thought Avi had a really great point about the segmentation between CI and CD. And one of the things I've been thinking a lot about, particularly as we start to think about what is DevOps? What is DevOps in an enterprise space? And what is the aspirations and what should the aspirations be for CI, CD? And how do you start to build the two things that I think are the biggest challenges, which is building that high trust in the system and the process and the people, and then building the ability to communicate clearly across a lot of different teams, the work that's happening, the work that needs to happen, and where things are.

    And so, for me I'm always fascinated by the intersection between the ask of CI, CD and DevOps and the execution of that in environments, particularly in enterprises that are highly regulated, or in the midst of a larger automation journey. Really how do they start to build those cultural practices in?

    **Lee Zen**

    And Abby I guess you asked a question in there, what is DevOps? I'm kind of curious, what is your take on what is DevOps? And then kind of maybe if you could follow up with just talking about how are you seeing roles on teams change as teams modernize and move to the cloud?

    **Abby Kearns**

    I will say my thinking on DevOps has changed a lot over the last eight, nine years. For many years, I didn't really the phrase DevOps because I really felt like it undermined and really didn't really clearly communicate to the work that had to happen, because it's not just bringing developers and operators together. It essentially to do it well, to do CI, CD well. To do any of these level of automation well, you're actually pulling together larger cross functional teams that are more than just developers and operators, there's product owners, there are line of business owners, there are platform architects in many of these companies.

    And so really, for me, it's how do you bring cross functional teams together and high trust environments, and allow them to both effectively communicate, but also effectively, quickly and iteratively deliver on software. And I do feel like we've been as a collective on this big journey around DevOps over the last decade. And we've really seen both the aspiration of where we wanted to be, but also as technology has improved.

    And as we've seen, more organizations really start to delve more deeply into this, the way that it's executed has changed over the years. And what's been really nice to see is a lot of organizations that are really improving upon those. We spend a lot of time in the global 5000.

    And really seeing how organizations are actually able to internalize the practices, and not just practices they would apply to deploying to cloud native or public clouds, but more importantly, how they're bringing those practices back for on-prem as well. And really starting to build those cross functional teams and changing the way the organization works.

    And so for me, once I think about where DevOps is, it's really those high trust small teams that are able to quickly identify, iterate and develop new software, and then really start to scale that across the business.

    **Avi Cavale**

    I agree with Abby on the DevOps term being kind of it's a wig term. One of the ways, I'm going to take a very radical approach on this one. And I personally think that there is the aspect of having empathy, communication, collaboration, all of that stuff. Those are all things that we should be doing no matter what. I don't think we need DevOps to do those things.

    I think I'm going to keep that completely separated out. And I say as humans, we should just be empathetic to people and what their situations are. But that being said, now I'm just going to bring it down to just pure tools.

    And I personally think that if a developer needs to know what an operator is going to do, and if an operator needs to know what type of application is being built, you have already lost the battle. I personally think that there needs to be complete deep coupling between the actual infrastructure on which your application runs.

    And the way application is designed, the infrastructure needs to be supported. It's more of two teams building the platform capabilities in order to be able to build the modern applications that you want. The idea of having software defined networking is an aspect of the operations team, improving the platform capabilities, so that developers can actually leverage software defined networking as part of their applications.

    I think yes, I want to do the collaboration, I want to understand each other's point of view and all of that stuff. But if as an organization, you need to be moving towards capabilities of what your operations and infrastructure team is providing you, and your application team should be able to leverage it and application teams should be providing monitoring hooks, logs, log aggregation, these kind of things, so that it helps the operations team to be able to monitor this better.

    I even talk about, like standardization of code. It's super important. I always tell people at 1AM in the morning, you get an error code, how do you know what part of the code is actually causing it? You need to be very, very clear about that. I think the more you decouple, I think it has a better success, as opposed to trying to couple everything, because trust me on it, there are folks who will love being in that operation level infrastructure SRE kind of mindset.

    And there are folks who are in the world who love to build software and build features and everything and trying to make everybody do everything, you'll end up with the lowest common denominator, as opposed to trying to go for the highest common factor.

    **Amanda Silver**

    It's kind of funny. I think everybody kind of thinks about it as software plus people and processes so that everybody is optimized. And as we realize that we have more of a need to integrate various different aspects of what it means to ship software, we keep creating these conglomerate words like DevSecOps, or it feels like German word construction a little bit.

    And so this question of like, where will it end? What would be the ultimate fusion of all of the aspects of software development and operations that would encompass everything that you'd need to think about?

    **Jonathan Sullivan**

    I think that's maybe a full stack engineer, but it only works at the very first employee for a startup. These are all just such great points. Kind of like Abby, I've given up trying to define DevOps, but I think it's also just been such a moving target. And can remember when it used to be very clearly developers, and then CIS admins, of which I was one, operating the thing that was thrown over the wall.

    And so that made sense, the union of those two things, I think, is where that for me anyway felt like it was coming from. The move from on-prem to the cloud, and back on-prem in a way that's kind of disappearing, thanks to containers, and contributions from all certainly all the companies on this call.

    The functional requirements are so different now too, it's not just developers and operators, it's a front end developer and a database engineer, and five other specialized roles who go into building this one application. And I love the phrase, small teams with high trust, they need to have those principles in there. And it's not like you're going in hiring a DevOps engineer, if you're doing that, there's probably a problem.

    And bringing all those things together to understand the whole objective and back to Avi's point about empathy for what does the code need to do once it's in production? That's really, to me, kind of where the heart of what DevOps as an ethos was, or is or will again be?

    **Avi Cavale**

    I think the funniest thing I see is DevOps training. I have no idea what that is. It's just crazy for me, if somebody says, I do DevOps training.

    **Amanda Silver**

    At the same time, I hear you on that, because it's such an ill defined term. But at the same time, I think we have to recognize that there are so many enterprises that are still very early in their journey towards even doing CI and recognizing things like what you observed earlier, in terms of the difference between CI and CD, it's a somewhat evolved viewpoint.

    I think a lot of DevOps training is really about just educating people on what are these practices as they start to move forward. Maybe there's not something specific like their discipline like mathematics or something like that, that is as tangible, but I think it is... A lot of it is discussion, just like what we're having here. Which is just what are these best practices as you change your culture and your tools and your processes?

    **Abby Kearns**

    I will say that to your point, I think DevOps is becoming the new digital transformation. Avi I think your point is, it's becoming all things to all people. I do think organizations are trying to wrap their heads around, how do we do this? How do we deliver software faster to production, full stop. And whatever you want to call that, if you want to call it agile DevOps, digital transformation, whatever works.

    But I think at the end of the day... I'm a big believer in the process and the culture part first, and then technology should follow because realistically, if you buy all of the best tools and buy all the automation tools, and you're running the full cloud native stack, and you're automating the entire pipeline, if you don't have the process and the culture around that, it doesn't work. If you don't understand and conceptually understand how to build those collaborative cross functional teams that are really starting to apply those processes to the way they work, you won't ever be able to get anything out the door, because it will get held up at all the gates you have already in place.

    And it won't shave any time. And so I think, for me, I even though I work at Puppet, and obviously we talk a lot about automation. And that's kind of where our focus is. I'm a big believer that the culture and the people in the process part is equally if not more important than the tools you invest in.

    **Lee Zen**

    And notice we're actually almost out of time. I just want to say thank you to everyone for spending the time with us today and having a chat. Any final thoughts or words from each of you?

    **Amanda Silver**

    I think one of the things that's very timely for the moment that we're all in is just [inaudible 00:36:47] it also speaks to the conversation about what is DevOps? And as we think about what are the constraints that everybody needs to be working with is just this idea of empathy for your customers, for your developers, for your operators, how using the idea of empathy as a way to understand the challenges that they face on a day-to-day basis, and then figuring out how you can partner with them to basically ease their challenges and the pain that they experience on an everyday basis? How can you make people's lives easier?

    **Avi Cavale**

    One last thought from my side is I think if people want to take away one thing from this is, I think most organizations should focus on mean time to recovery, as opposed to reducing failures. What I mean by that is, the more your products and stuff can roll back to the prior version, the backdoor you are in the majority of where you want to actually be.

    If you kind of constantly want to evaluate where you are, you just want to check on how quickly can I go back to the prior version and what does it actually take. And then as long as that number is reducing, that means it will actually increase confidence in all parts of the organization to be able to move faster. And I think I just kind of want to let folks to think about that and say, "Hey, how do I worry about mean time to recover, as opposed to number of failures?" That would be my closing point.

    **Abby Kearns**

    I want to plus one what Amanda said, I mean empathy and I would add to that patience. It's a journey and I feel like that is an overused term these days. But it is a journey and it's a process. And to really be patient and remain focused on your ultimate objective, what is your goal and just kind of remain focused on that. And the way every company gets there is slightly different. And I think just follow your own path, as you think about how do you want to drive towards that ultimate goal, which is delivering software faster.

    **Jonathan Sullivan**

    I wish I had something original to add. All of those are such important points. And I do think you can boil it down to empathy and patience as a great one. Maybe tying it back to setting really clear goals and expectations so SLAs, service level objectives, a clear understanding of where it's okay to push the boundaries for developers like if this system goes down for an hour, it's okay. You don't want everybody walking on eggshells, because then that stifles innovation.

    I think if you boil it down, it really means just focusing very closely on making your company a great place to work. And if you're digging on that and listening to people and the struggles they're having, things about hey it's too difficult to assemble the development environment where it takes forever to run the build or I have trouble deploying. Those things will fall out and making sure that at the highest levels and throughout the company that you're addressing those things will one [inaudible 00:39:57] retention is going to help with. Making it a better place to work.

    But ultimately, like Abby said, it will actually help you achieve whatever it is that you're setting out to achieve the goal as a company.

    **Lee Zen**

    Thanks to everyone, we really appreciate your time and thank you Avi, thank you Abby, thank you Jon and thank you Amanda.

    **Jonathan Sullivan**

    Very well.

    **Abby Kearns**

    Thank you.

    **Amanda Silver**

    Thanks for having us.

    **Jonathan Sullivan**

    Thanks.
aliases:
  - /resources/the-future-of-cloud-engineering-culture-process-tools
---
