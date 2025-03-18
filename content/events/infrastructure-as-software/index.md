---
# Name of the webinar.
title: "Infrastructure as Software"
meta_desc: Let's put the Dev back in DevOps and talk about why Turing complete config management is an antipattern.

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
url_slug: "infrastructure-as-software"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Infrastructure as Software"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Infrastructure as Software"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/rtng6GNQd4w"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T09:00:00-07:00
    # Duration of the webinar.
    duration: "23 minutes"
    # Description of the webinar.
    description: |
        Let's put the Dev back in DevOps and talk about why Turing complete config management is an antipattern.

    # The webinar presenters
    presenters:
        - name: Kris Nova
          role: Senior Principal Engineer, Twilio

# This section contains the transcript for a video. It is optional.
transcript: |
    Hello, take 21. Hello and welcome. I'm your host, Kris Nova, and today we are going to be talking about infrastructure as software, take 21. I have been working at this all day, so hopefully this will be a good one. We'll see how it goes.

    So, hi, I am Kris Nova and today we're going to be talking about infrastructure as software, particularly what it's like to manage infrastructure with software. And we're here at the Pulumi Cloud Engineering Summit. A big shout out to my friends Mattie and Kat for helping me get on board here. Shout out to Joe for letting all this happen and big shout out to my favorite underdog, my sister from another mister, my girl Liz in Seattle. I love you, I miss you.

    I see you out there in the streets doing good work. I love you, girl. I know you're out there. So anyway, we're gonna be talking about infrastructure as software. So a bit about me, other than the fact that I give my presentation in a Unix terminal here.

    I am the Lead Senior Principal Architect and I work on Kubernetes at Twilio. So we do a lot of Kubernetes things and we're working on a new Kubernetes project and I'm the lead architect on the project. And you can find out more about what I do in open source on my personal blog, Nivenly.com. And I encourage all of you to buy several copies of my book, "Cloud Native Infrastructure," which we'll look at in just a moment, for your friends and extended family.

    And you can see all of my lovely open source code in chicken scratch on GitHub.com/kris-nova. And you can follow me on Twitch where I do a lot of live streams, not recorded streams 'cause recording is really hard for me, but I do live stuff all the time. If you wanna come watch me live, I'm there pretty much every day. And I'm on Twitter.

    Please don't follow me on Twitter. You're welcome to read my tweets from time to time and they get me in trouble more often than not as we're about to find out. Cool, so speaking of tweets that get me in trouble, here's a great one here on the left side of the screen. So I made the mistake of tweeting this "stop doing infrastructure as code" the other day and this is what led me to realize I actually draw a line between infrastructure as software and infrastructure as code and I kind of thought everybody had made that mental leap at some point. And the more I talked to folks, the more I realized that I had created a big line in the sand in my own brain that I don't think other folks had created.

    So I get asked this question a lot. How is infrastructure as code different from infrastructure as software? If I do my job correctly in this talk, you should have a good idea of what these words mean to me. And I will be because I do feel like in the ability to be different with our definitions comes a lot of value and ultimately a lot of more resilient infrastructure for you and your team. So anyway, if you like this topic and you want to see more, go check out the book. We have an ASCII condor here on the screen that should match our cloud native infrastructure condor here as well in a lot of what I'm talking about, particularly the infrastructure as software, the testing, the infrastructure teams, all of this is also found in the book that we published back in 2017.

    So we'll start off with some simple definitions so that we can grow them moving forward. What is infrastructure? It's the bottom half of the OSI reference model, right? Application is at the tippy, tippy top of the OSI reference model and in order for an application to exist, we need all of this noisy stuff underneath, and we call this noisy stuff infrastructure, and typically people don't wanna deal with it. We like to pretend like it's not there. It's stupid, it's hard, it's frustrating, which is why I'm in this biz. So anyway, I like to break these down into my three favorite pillars or tenants of computer science, compute, network and storage.

    I think everything we do in computers can be broken down into one of those three categories. So let's look at some example. So in compute, servers, operating systems, container run times, processes, things that run, things that start to give us abstractions for software. Storage, disks, memory, staple disks, virtual disks, LVMs, these are all places where we can write things down virtually and come back and read them later. Network, everybody's favorite, the relationships of computer science, like the drama, right? That's where all this really good relationship stuff happens, you know, like subplots and everything.

    Load balancers, firewalls, network switches, security groups, VPCs, all this fun stuff that involves our network and how computers connect to each other. What is code? In its most literal form, it's just the plain text representation of a program or a configuration. Yep, it's just the shit you can read. It's a text file. So I look at some example code here.

    So we have, you know, int main, we have some example code that does various things. We have some example Python. I'm sure we've all seen Python before and you can see it. It does similar things. And what I want you to remember is the code is just the things that are important to humans, the stuff we write, the stuff we can read, and it's just the encapsulation of it, right? What's a text file? It has to live somewhere.

    However, there is a program that takes this text file and does things with it. And typically we, as code engineers, care very deeply about the thing that turns this plain text into whatever we want it to do. So let's talk about Turing completion, 'cause this is gonna be really important for us to understand how code turns into these programs that we want. We want people to run. We want these programs to do things for us.

    So all a Turing complete program is, is it's something that can compute any other program, right? It's got some fundamentals of computer science, you know, the ability to manage memory. It's got iteration and it has a logical switch. And if statement, if you see an if statement, there's a good chance what you're looking at is actually Turing complete at the end of the day. And because of that, you can run theoretically, any program on top of that. So Microsoft Excel does have a concept of if statements, if this, do that, which means in theory, if we wanted to write the obstructions, we could run something like Doom on Microsoft Excel.

    We really could. You absolutely could make that happen if you truly wanted to. In most cases, that's just the thought exercise, but I think it's an important one to call out. So what is software? So it's a Turing complete program like Microsoft Excel and it's at runtime. So when we say runtime, we mean the time is now, it's running now.

    As a side, you'll notice my screen is flickering and well, I run Arch, by the way. So we'll look at these programs at runtime, and we can see that we provide ways, little windows for us to view just very temporary ephemeral little glimpses of what the program is doing at a given instance and we see things like process managers or task managers and their ability to represent what's happening and the moment you view this as it's already outdated because it's sure enough moved on at runtime, so these are just small glimpses into reality. What is infrastructure as code? Well, think about it. If code is just the plain text representation, it's just our ability to represent infrastructure using code. So I'm sure we've all seen Terraform before where we can write things like the cider block of a VPC and we can define things like a sub-net and give the sub-net, you know, a slash 24 from within our slash 16 above.

    And you can see that we can start to break apart different pieces of infrastructure and we represent them as code. Now in the same way that a C program goes from C code to a C program, your infrastructure goes from infrastructure code to, and that's most infrastructure as code stops. And that's where the infrastructure as code engineer mindset typically goes away, right? We say our code is done, therefore, I'm done. I can go to lunch. I can have a cup of coffee.

    My work here is done. And I'm here to challenge that. So what is infrastructure as software? Well, it's fundamentally, it's the actual process that is running the code that we've already written and it's running that code at runtime and we take ownership of it. We are responsible for the pieces of software that are running on the backend. So I do believe that infrastructure is software is an ownership change, it's a shift in ownership.

    It's putting the dev back into dev ops. It's saying we not only write the code, but we also care intimately about the thing that renders the code, the thing that brings the code to life, the thing that does the thing with the code, we care about that. In the same way that a Python engineer cares about which version of Python they're running, we as infrastructure engineers should take ownership of the thing that's reconciling our infrastructure. And now I'm not suggesting everybody to go rewrite Terraform. That's not what I'm saying here.

    What I'm saying is we can start to imagine as a community, as an industry, what little pieces of software you and your team could write that could do really handy things for you. And we can abstract things away that are boiler plate, like Terraform does, and we can start to create little logical systems that do really powerful things for us and we can do those in very, very solid insane way by following in the footsteps of our software engineering older siblings. So here we look at cluster API dot YAML and the YAML's defined it down here below and you can see that this YAML is actually the first half of bringing these pods to life. So here we have a cluster controller, we have cluster validation, we have cluster heartbeat, and you can see, these are small programs that I wrote. I'm a software engineer now and I wrote these programs to manage infrastructure and this one reconciles the cluster itself, and this one validates the cluster and ensures it does everything I want any cluster to do.

    And this one just checks and make sure it's online. And I can now start to weave these components together to build really complicated systems that are really easy to manage. So let's talk about software teams, aka, those meddling engineers. As I mentioned earlier, there's a lot we can learn from them. And I do want to draw attention to some of the things software engineering teams do that I think works really well.

    The first one is feature-driven workflows. So in a world where people need things from you and your team, I'm sure as infrastructure engineers, we're all familiar with somebody needing something, right? This is literally the story of our lives. In a world where people need things or want things or think they need things, we typically are rewarded for responding with, "Yes, right away, we'll get it done immediately." And software engineering teams don't always respond that way. Sometimes they say, "Yes, we'll get it done.

    We'll prioritize it and we'll create a feature request for you and we'll make it out on the next release." And as it turns out, people are actually more receptive to "not right now" instead of a hard "no." So I think the ability to say "not right now" is actually quite valuable because it gives, it buys you and your team time to do the thing you need to do correctly, and it also gives the person requesting something from you an ability to deliver a promise and that promise is, "Not this week, but it will come soon." And with that promise comes trust, and with that trust comes a healthy working relationship, and with that healthy working relationship comes the ability for us to by the time we need to do things correctly, and that's how I think we stay out of infrastructure debt. Time-based releases, these are your ability to cut releases on a timely manner instead of on a need-to-need manner.

    And I think any concern you would see with a software engineering team is equally as relevant with managing infrastructure as software. What about a release gate? How do we ensure that our software does what we want it to do? How do we ensure that the person who's making a change is going to be able to programmatically prove it's gonna do what they advertise it's going to do? How do we test? What about validation? How do we ensure that what we're changing is sane? How do we monitor it after it's running? What about logging? What if something goes wrong? Observability, anything that we would potentially add to a modern software engineering stack, we can also adopt an application infrastructure engineering as well. Now there's a very clear problem here, which is if we're now modern-day application engineers, where do we run the applications that manage our infrastructure? And that's where I like to say, "We love infrastructure so much we put infrastructure on your infrastructure." And that is a problem and it is a problem you have to solve and I do think in my mind that this is evidence that an infrastructure team is typically stronger and needs to be stronger and more resilient than a typical engineering team because they have to do everything a regular engineering team does and more. So let's talk a little bit about what I learned at Twilio with GitOps and this is very relevant to the differences in what I see as infrastructure as code and infrastructure as software and I really think GitOps is a good example of meddling the two and why I think it's important to draw a difference between the two.

    So let's break GitOps down. What is Git? It's a version control tool that you can use to manage software. However, this is designed for teams working on different sides of the world, you know, distributed teams to do the things correctly. We want to be very meticulous and very intimate with our lines of code and we want to work on these and we want a really good way to manage these lines of code. In fact, we would be willing to exchange time for resiliency.

    We value right more than we value right now. What is ops? Doing shit manually in a pinch, right? I need to get things done and he need to do it now. And these are chores. These are things that you do. And typically these value right now instead of right.

    So GitOps is doing the right now thing using a tool that was designed to do the right thing. And I think that's why I think GitOps is a bit of an anti-pattern, I really do. I think that just because you put something in Git, or just because it has a config, doesn't mean it's a good idea. It doesn't mean that you're using Git the way Git was intended to be used. The whole point of Git was to give us visibility into the changes and I have seen that Git is now just basically used as a database and you're still able to do just as much damage as you did SSH-ing into a server, except now you have three button clicks in a YAML file to abstract away your SSH command.

    I'm still able to break production using GitOps, except for now it comes with added complexity in a build pipeline to go into the whole process. So I still look at GitOps as infrastructure, as menial chores, if anything, and it's brought to you by a fancy new pull request in some code. But look at the difference. We obsessed with Git the code, the managing the code. We got very good at managing the code and putting the code in version control, but we were still doing the ops mentality.

    And I'm here to say, let's put the dev back in dev ops and let's consider dropping the ops all together, or at least being aware that we want to be dev heavy in some cases. So here it is, the whole point of the talk. If you take anything away from this talk, it should be this ASCII diagram with my IDE flickering in the background. I want, let's see if I can't clean it up, there we go. I want you to screenshot this, send it to your friend, you know, text it to your partner and whatever.

    What are the differences between infrastructure as code and infrastructure as software, now that we've kind of defined them? So the big one is dev versus ops, right? I think infrastructure software is more dev than ops. The next one is I think where they stop, right? It's the definition of done in where it stops. I think that infrastructure as code stops at a working config and infrastructure as software typically stops at what we call production ready and I think with that paradigm shift comes a different level of responsibility and a different level of ownership. So I think an infrastructure as code, it's completely normal to have logical Turing complete systems without tests. Think about it.

    How many of us have written helm charts or Terraform or Puppet or Chef and we didn't provide tests to our changes? We just wrote the if statement, we just wrote the for loop, we just wrote the logical system, but we didn't offer tests to prove that it was going to do what we thought it did or prove that it was going to mutate the infrastructure the way that we thought it did. I know everyone out there has committed Terraform or public config and pushed it live and hoped for the best or ran it, you know, it worked in staging and you're kind of like that's the best we can do and that's what you do. Whereas if you look at infrastructure as software, you flip it around. It's actually unusual to have logical systems without tests. And yes, I know we live in an imperfect world where not every piece of software has tests, however, I think it's pretty common knowledge that we would like for it to have tests.

    You know, there is this concept of perfect world conditions that exist in a software pipeline that I don't think we see in a infrastructure as code pipeline. I don't see nearly as many folks making jokes about where our Terraform doesn't test that our servers are online in the same way that we make jokes about not having unit tests in production and that's because I don't think the paradigm is there. I just don't want to think that people and folks I see in the wild are really truly considering having infrastructure tests and I think we should. I really do. I think there's enough software in place today that we should be writing tests to go and actually validate our infrastructure does what we want it to do and introduce confidence there.

    Because of this, I think we have a lower quality definition of done, flat out. I just think that in a world where we're not considering validating and ensuring our shit does what we want it to do, I think it's just not gonna be as high caliber of a product and I think in infrastructure as software, I think that naturally we're creating this more resilient, more meticulous and more testable and programmatic system that we use to work through and it's a workflow change. This is a big one, Turing completion. We talked about this earlier. I think infrastructure as code doesn't embrace Turing completion, it just says, "Yeah, you'll probably get there one day."

    You might throw an if statement or two in, but it's nothing to worry about and you can probably just get away with not worrying too much about it. Whereas I feel like infrastructure as software is like, "Bro, you're a software engineer. You're writing a Turing complete program. It is time for you to accept the fact that you are a software dev and you're working on an engineering team and because you're writing Turing complete code, you should offer tests for your code." Working as an operations team values right now.

    Working as an engineering team typically values right. Do I do the quality thing or the quantity thing? So I think we see that a lot in infrastructure as code versus infrastructure as software. The end game that you hope to get to with code is you'll probably end up with some logic and if you're lucky, that logical will work. Whereas I feel like the end game that you hope you get to with software is you probably end up with tests and if you're lucky, your test will pass and I think that we're just raising the bar. It literally is just raising the caliber of what we consider done.

    And ultimately I think infrastructure as code is we get shit done quickly. And I think infrastructure as software is our shit has tests and we can count on it. It might take us a little bit longer, but it's not gonna break. And I think a lot of us are in this situation in our careers where we now are finding ourselves having more and more time to build right instead of right now. So let's answer some questions.

    Is infrastructure a software right for everything? God, no, no, it is not. Do not stop what you're doing and go start writing go and, you know, building these things from scratch and telling yourself it's gonna make all your problems go away. No, don't do it. I know you're thinking about doing it, don't do it, because this is the whole thing we were trying to get away from in the first place. What I am trying to say is that there are situations where adopting the mindset of a team, of the human resource element of a software engineering team where you might actually find a lot of value in managing infrastructure as code, as software.

    And as we saw with Cluster API earlier, there is a big similarity between the code and the software. The code turns into the software, that's the point, but we're now taking ownership of the software as well. So look at this very simple, lovely ASCII diagram I did. If this is you and you're managing a lot of fucking servers and those servers are breaking from time to time and you're seeing servers coming into and out of existence, having a small piece of software to help you manage this and identify these might be a lot easier than trying to go and find it manually and you'll get here quickly as you and your team grow. So understanding that you're going to get here and that you can borrow from infrastructure as software early is going to make this situation a lot more manageable when you get here.

    So I'm gonna stop here. We're at 23 minutes, I got seven minutes with my girl, Kat. We're gonna talk to you all about all kinds of fun stuff. And I want to just again, say thank you to Pulumi for letting me come and give this talk. And I'm going to also record a small 10 minute case study about a program I did call NAML that is a concrete example of how to do some of this and I'll talk a little bit about the pros and cons and I'll post this on my blog if folks wanna see the case study of what I'm talking about later.

    So thanks for coming to my talk and I will see you all next time.
---
