---
# Name of the webinar.
title: "Kelsey Hightower & Joe Duffy Fireside Chat"
meta_desc: Listen in on as Kelsey Hightower and Joe Duffy discuss the past, present, and future of the cloud infrastructure landscape.

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
url_slug: "kelsey-hightower-joe-duffy-fireside-chat"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Kelsey Hightower & Joe Duffy Fireside Chat"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Kelsey Hightower & Joe Duffy Fireside Chat"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/w6Dj2zf-39M"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T08:30:00-07:00
    # Duration of the webinar.
    duration: "39 minutes"
    # Description of the webinar.
    description: |
        Listen in on as Kelsey Hightower and Joe Duffy discuss the past, present, and future of the cloud infrastructure landscape. Hear key insights from Kelsey on everything from best development practices to how to run an engineering that lives in the customer's shoes.

    # The webinar presenters
    presenters:
        - name: Kelsey Hightower
          role:
        - name: Joe Duffy
          role: CEO & Founder, Pulumi

# This section contains the transcript for a video. It is optional.
transcript: |
    Can you reach out and pull that up. Who knows I didn't wax today. So if I start sweating profusely they said, they can Photoshop that out. Do I look at just into this camera, is that okay. And then get back.

    Welcome everyone Oh, should I not talk to the camera? Everybody here already knows who you are not me. So I'll introduce myself. Kelsey. I think, I think you and I both sort of share a background in software engineering. We somehow found ourselves working a lot in the Cloud and infrastructure for the better part of the last decade.

    I'm curious to hear a little bit more about your story and what led you to an infrastructure and why are you excited about the Cloud? Yeah, a lot of people, you know, you start your career in tech mine in particular. Tech support, system administration and I'm talking about the type where you're SSH into servers, writing bash scripts. Those were the tools that I started on. And I remember around like the 2009, 2008 timeframe. And that's when I was introduced to that concept of configuration management. Yep.

    And the tool I was using at the time, you know, its idea was let's bring a real programming language with the DSL to this space and formalize the way we're thinking about automation. And that was kinda my introduction to infrastructure's code and I went to go work at that place. So I think that's where we have a lot of commonalities building tools to help people automate those infrastructures and, you know, since then I went full circle, you know, the whole container movement, this idea of even though we have infrastructure as code, should we think about changing the things that we're automating and deliver some new abstractions?

    Yeah. I remember, you know, back, back in the days we racked and stacked servers, and then suddenly you actually had a, an API that things were behind, what are some of the biggest changes that you've seen in the last 10 years since, since then.

    You know what, when I actually think through that? Unfortunately, not a lot. Because the fundamentals are roughly the same. If you think about the whole virtualization path, it's literally trying to mimic and recreate that physical world. But in more than a virtual sense, it was almost one-on-one to one mapping, still IP addresses and virtual machines and Linux operating systems. And so instead of racking and stacking, you literally do have people that have a console of all their servers.

    They didn't give them names like transformer names. I'm like, what are you doing? These are, you know, these are inanimate objects. Why are you naming them? But that's still a thing. So I think that the world, as much as it's changed at some level, a lot of the fundamentals are roughly the same and I think this is why it's still hard. You can't assume everyone has access to the Cloud and the new abstractions most of this work.

    And I think the reason why Pulumi exists is because of all the complexity of trying to take multiple systems that have evolved at different paces and try to automate them to make them feel like a single system. So I think the biggest changes that I've seen that are on the sides are the new abstractions. You know, the whole world talks about containerization, even with all the hype. I think the biggest thing that we've gained is more concrete abstractions like we have in the server world. When someone says that they rack and stack a server, they know it's going to be about 42 inches.

    They know that there's going to be a switch at the top and they can plug in an ethernet cable, pretty much everyone knows how to make one. So you have this level of consistency because we have shared vocabulary for that physical world. And now some of the newer attractions like containerization are given us the same thing at the application level. And now we have a much better target in Warsaw automate. Yep.

    Yeah. It's, it's interesting for me, you go and draw a piece of software or an architecture on a whiteboard. Often I find it's conceptually simple and then mapping that into the real world is where it gets messy. In a lot of that concept, you just mentioned everywhere it gets messy, you know, networking, storage. Why is it that the gap is so large and continues to be so large, do things like serverless and containers really promise to solve that gap?

    I think the biggest challenges that we're all practicing, this isn't a hard science where these things are universally true for everyone like security, isn't practiced the same by everyone. Some people need to take certain trade-offs and some people can't make those trade offs depending on the type of data that they're handling. So given that this is a practice, there is no static way of doing it. This idea that there's a way of doing it right. That's where I think a lot of times we get astray in the industry. So new tool shows up, we'll say, this is the right way of doing something, or we'll make a claim that this is the best practice.

    And then what I think that does is it starts to distract us from the reality is that every organization, every developer, every team, every situation is literally a practice. And we have certain tools at our disposal to allow us to practice. So the reason why it's hard is that different people are practicing based on their own unique situation. If you've never had a security incident before you have no practice. So this is why we're always learning on the fly.

    Most people are just learning in production. As we learn, we try to incorporate their feedback into the tools. And I think that's why it's hard and why it's never finished. Yep. When configuration management came on the scene.

    I first learned about it through promise theory. And if people they're not familiar with promise theory, I think the biggest learning there was, these are promises. We are trying to tell these systems how we would like them to behave. We're trying to write code that make them behave that way, but it's literally a promise and those promises are built on assumptions. We're assuming people won't type bad things into that little text box that we give them to put their first and last name in.

    But when they violate that contract, then you have the potential for the promise to be broken. And so I think the fact that we're still kind of operating in this mode of like promise theory, there was no way to have some guarantees that we all assume in certain walks of life. My observation is many more developers are getting hands, you know, their hands dirty or with the Cloud, and really learning more about the underlying infrastructure that powers their applications. And, and it actually, some of the aspects of distributed systems are as powerful in many ways as the quote business logic itself, because you can build these infinitely, scalable applications. How have you seen the role of the developer change in these last 10 years?

    So there's some positives from that, given the complexity of all of these systems and the amount of expertise it takes to operate at the top of the stack, you're a developer, you just want to write an app that people can just use, but that has to run on something.

    The unfortunate side of this is that someone needs to know all of this to be effective. This is the equivalent of asking someone who just wants to cook a dish like a chef, "Hey, before you start making that macaroni and cheese, we're gonna have to teach you how the power of good works. We're gonna have the teacher you how to run a gas pipeline to the restaurant. So you can actually have gas to create a flame in order to cook, oh yeah, Before you can use a pot, we're going to have to show you how to meld the port from raw metal." Like this is insane asking professionals to have to learn every part of the chain before they can be productive, has been a big productivity loss in lots of capital for the whole tech industry.

    The real question we have to ask is why, why is it necessary in 2021? I've been in industry for about 20 plus years. And I know some people have been at this for 30, 40 years. And if you asked them what they were working on then, and what we're working on now, it's very similar. And so I think the question is, is there hope in these mentioned serverless platforms where we say, if you want to send email, you can just use something like Gmail, for example. And that know how to set up a mail server and secure from spam.

    Can we do that to other systems like compute and databases and networking. And I think that is the promise that we talk about when we say things like serverless. And so, I think that where we're evolving is that people now respect how hard each of those layers are and giving that respect, I think the more people that learn the trade off. Are you willing to change the way you write applications to conform to the systems that are performing, that capture all the things we've learned, or do you want to do everything you want? And therefore, you're going to have to inherit the responsibility of building systems from scratch to do so.

    You mentioned compute storage services, more things, softwares and servers, effectively more things available on demand behind an API so that it's easy to use without having to care about how the abstraction works under the hood. What is the role of the infrastructure team in this kind of modern world where they're trying to empower developers more often than not? When I was driving on the way here I was asking a simple question's like, what, what is the asphalt made of, of the road that I was driving on? I Don't know.

    You were wondering that? That was silly wondering, no, seriously. I have no idea. I have no idea who made the concrete for the barriers so that I don't drive off the side. You don't know. Yeah. And that is a good sign of infrastructure. The people who work on that are invisible. And the only time we think about the freeways is when there's a traffic jam, there's a pothole, right? You have a car accident. So usually some thing as bad is triggering the thought process there.

    In enterprise IT typically, most people have so much friction that they're always thinking about it. There's never this idea that you can get in your car and just drive straight to your destination. In enterprise IT is like, "All right, there's only one lane and I know everyone's on it. And I don't think we fixed any of those potholes from the '80s, the '90s, the '00s. And then there's half built bridges.

    People are building bridges because they have to be done by Friday. The bridge is not even safe because you don't have time to test the bridge. And you're the first car on the bridge. And you're sitting there like, wow, I mean, this team has never built the bridge before. Is this even safe? And then you drive across it and you fall over and they say, "We'll fix it, we'll patch it."

    This bridge needs more than a patch. And I think a lot of enterprise IT systems have gone beyond where a patch is going to cut it. And so I think the biggest challenge we have in enterprise IT is number one, we're asking people to build systems they've never built before. We're asking people to kind of figure it out as they go, and then have another team trust that it's going to be stable, that they can rely on it in production. And then we're asking our customers to trust this fragile machine with my data, my ability to jump on an airplane, my medical records.

    And so I think this is a real thing that all developers, infrastructure folks are coming to terms with is that can we reliably build infrastructure, millions of companies all get to the same equal footing. And I think what we're learning as an industry is that answer is probably no. There's probably going to have to be some area where we can trust each other, just like the public highways. Let's get it right once. And ideally, if we build it in a way that's fairly flexible, large tractor trailers can pass through it. And even an electric bike, if need be.

    I look at customers that we work with who are being wildly successful, using things like GKE, you know, autopilot, using you know, Cloud spanner, big query, these hosted services where you don't have to be the expert in how to build reliable, robust infrastructure. You can depend on, you know, somebody who does that for a living. So that's certainly in my opinion, kinda plays a significant role in, in, in addressing some of this kind of to your point the challenge that I see often is what are the best practices for how to stitch these things together? How do people navigate that? It's a very complicated world. You know, we talk about the CNCF landscape and for those that have not seen that landscape in a long time, if you look at it, there's like 10,000 building blocks in there.

    And the challenging part is some of the building blocks do the exact same thing. And so now you have to make a decision, not just on all the layers, but which one of those building blocks, what are the best practices? And I think every five to 10 years ago, those best practices manifest themselves. Kubernetes and Kubernetes to me represents when you peel back the onion, it is the best practices of assembling a bunch of virtualization components and taming them in a way that you can use to deploy applications. But there's other things there, security, policy, where do you put your data? What part of the world do you run in for regulation purposes? Sometimes you need to run a multiple parts of the world at the same time. And this is where I think the serverless platform start to encode so, when people ask me, "What's next?" What's next can be identified by the things that are lacking from the current tools.

    So as great as kubernetes is all of its gaps, all this friction points, the things we're doing to solve that is the next thing. So I think when people say, what is the best practice, I always ask the customer, what are you trying to do, exactly? Not what everyone else is doing. What are you trying to do exactly? And the better that answer, the better the recommendation is. And typically where we can do and say, look, the thing you're trying to do, I'm gonna be honest with you. As unique as your idea is, I'm going to probably guess that it's doing the exact same thing that everybody else is doing.

    And if that's the case, then you might be able to use an existing platform, but you're going to have to conform a bit at your current, can't be wider than a lane. If you can shrink the size of your car down, I mean, you can get to a tractor trailer size so, you should be able to accommodate what you're trying to do. Then you can just use the same highway instead of attempting to try to build your own.

    How does somebody know whether they should go build their own thing versus just using off the shelf components? When, do you know your requirements are unique enough to go forge that path and try to build your own platform or build your own solution? A lot of these things are super domain specific. They're trying to address problems of the previous programming languages.

    And so in the case of like these new languages, like Swift for the apple ecosystem, if you want to write an application for the iPhone, then apple is going to say the best practices come in this framework. And that framework has a language called Swift. And if you learn it, we're going to make it real easier, easy as possible to write in a mobile app or iPhone. If you want to write something for the web, that's works across multiple browsers, then JavaScript's going to be your jam. And of course you get to these things like frameworks.

    But I think the thing that is dangerous is, is not the fact that their not invented here, you know, that lead to innovation sometimes you know, for a fact how something works and then you decide from an position of educated position and then you decide to strategically make a new thing. The problem though, is most people are not making educated decisions. Most people are just saying, I don't understand that. So I think the phrase is like not understood here. Right.

    This is the real challenge. We don't even understand what this is. So you find yourself actually reinventing the wheel because you never saw one. And I think that's the biggest challenge. So I think as engineers, what we have to do is be learning, what are the things that are available? How do they work and make a real evaluation of when should you depart? And I think it's getting even harder because a lot of the most successful projects are open source.

    So the need to start something from scratch has been reduced over time, I think now at this point, worst case, you can extend something that already exists to fit your needs. And I think the underlying systems are getting better at realizing that one size won't fit all. And there has to be natural extension points. And I think that's just where we are in 2021.

    Yeah, 'cause you alluded to something a few questions to go around, building half-built bridges and then you not feeling like people can finish or create the level of stability in the infrastructure that's actually required of the organization around them, is that, and you've told me, talked a lot of CTOs and advise them on these topics that, is that a cultural problem.

    Is that a leadership problem? Is it a, a tooling problem? Are the building blocks we're building on just fundamentally too shaky right now? Like what, what advice would you give to people to navigate that requirement to, you know, ship fast and break things without breaking them?

    Yeah. I think it's society, it's a societal problem. It's just the way humans work with systems, right? Typically we try to figure out and explore new things. And usually during that exploration phases, it's going to be less stable because we don't know, but we're still trying to explore and push things forward so maybe we go into places that no one's ever gone before and that's okay, that's healthy. But at some point, though, if you want other people to travel the same road, ideally you want to make sure that it's safe, it's sustainable and also think about who's going to maintain those roads if it's not you.

    And I think that's the part where most people don't think through these decisions. And so that's where we find ourselves in these tricky situations where I think the saying goes, "Most software is just abandoned." Right. Right. You launch it, you get some customers, you get some traction and then it gets a little stale.

    Maybe we don't update to the newest version. Maybe no one looks at it because it's working. And then a decade goes by and then you step back and say, "Yo, this is no longer secure." There are new ways of doing this and we haven't kept up incrementally. And you just look at this huge hill to climb so what most humans like to do, we start over.

    Your house is too old, buy a new one, your computer's too old, buy a new one. And the problem with software is it's not that easy to just say, "Let's just throw away the software and try to relearn everything that took us 20 years to encode into this application." So we don't necessarily have that luxury to just throw away all the software and create new ones, so I think that's the biggest challenge.

    Is it hopeless? Are there any techniques that you see, enterprises practicing to help deal with legacy and modernize legacy? And what is your advice to enterprise is dealing with that trail of legacy. I'm going down the dangerous sports analogy path but you know, like American football is typically someone will consider a young man's game and rookies are drafted every year with all this high potential.

    And we apply the fastest, the strongest, the people can jump the highest, score the most points. And then if they do a really good job of that, we induct them in the hall of fame and their careers, their legacy. And then they kind of fade off to the sunset and the new players arrive and we repeat this process every season. And then you have people like, Tom Brady who are playing into their forties. And do you look at him because of his age and say, "He's a legacy football player."

    Do you induct them in the hall of fame, even though he just won the super bowl? Do you say that this is the end of his career? And I think the way we look at software, even just like the word legacy, we don't necessarily use it in a positive way when we talk about software. Yep

    Legacy is like the old thing that we all want to get away from. And the truth is it still works. And I think the maturity part of software that needs to, the discipline needs to be, who maintains it, who updates it. If you learn a new practice, for example, in some of the old stuff that runs on the mainframe, could you add health checks to it? Sure.

    you could, you could implement the same new protocols that are available on Cloud native based systems. And I think it's just the maturity of understanding the platform and the fundamentals can be separated. You can implement most of the fundamentals on any platform. So I think that's the part where as an industry, we could do a lot better by not classifying these systems by their age, but asking ourselves, like in the case of IBM, when the new mainframe rolls out, will it be able to support these new practices and fundamentals, when the answer is yes, then we can evolve that software to incorporate those versus abandoning ship and going, hunting for a new platform. And the way I like to frame it is all the new stuff that we're working on, if we're lucky, it'll be around long enough for other people to hate it.

    And I think the thing that we have to be careful with is separating the fundamentals from the platform, right? And the fundamentals and best practices evolve over time. And when you think about it, you can take those fundamentals and best practices and apply them to pretty much any platform. So I think the goal really is to not necessarily think about them as legacy versus new versus Cloud native, but to ask ourselves if this platform is capable of running these new fundamentals. Yeah. It's, it's interesting.

    I know there's a system. I think it's called saber. And I, I think a lot of airlines still use Saber and it was probably written in Fortran or something. I'm probably making it up, but I have to imagine given the high availability requirements of that system and the fact that it's available through modern web interfaces, there's probably a rest API, there's probably health checks for all I know it's actually using containers somewhere under the hood. And to your point, it's solving a business problem. Why go reinvent the wheel when the thing actually works?

    Yeah. I mean, I could see a situation where some of that software is unsuited for, you know, certain capacity needs. You know, I think when the internet came around, it put a lot of stress on some of these existing systems. Some of them didn't even support these protocols like, TCP/IP. And so that means that those systems do have to evolve, where things start to get dangerous though, is when those systems get so old where there's no one that knows how to operate them, that education part so we didn't really talk too much about as a industry, who's teaching new developers, Fortran, and then you have a problem over time where, when you're trying to hire people to come work on one of these airlines systems, and there's only like 10 people in the world that can do that, that's a major problem.

    So as an industry, we have to think about it is, how many of these systems exist? And then how do we make sure that there's a healthy group of people who can manage those systems? And then how is that relationship with those vendors? Right? Because sometimes, and we've seen it in the past, When a vendor throws up their hands and says, "We're no longer maintaining this software." And we saw that a lot with proprietary software in the past, and there was no way for someone else to pick up and continue on. So this is why I think open source is a really big, important element to this because even if one company stops developing that technology, well, maybe another community can pick it up and train that next generation to keep these systems alive and evolving over time.

    What is the right level of abstraction? Is abstraction a good thing when it comes to infrastructure or a bad thing, because we all know, you know, abstractions can be leaky and when they leak it can be painful. And at that point you might just wish that you had coded to the underlying raw concepts, under the, whether it's VMs or what have you, how do you know which level of obstruction to pick both as a developer, but also as an infrastructure person who's trying to ship a platform to enable your team.

    Let's say you want to target managing a database on Kubernetes. So you take Pulumi maybe use Pulumi to provision the cluster. All right, cool points. You might use Pulumi to install the database. Great.

    But now you need to know everything that goes in that config file for that particular database, you need to know how to safely back up the database. When there's a new version of that database, you need to understand how to roll it out safely. And when you look at Pulumi, luckily it's powerful enough for you to articulate all of these nuances. But the reality is you're building a very complex state machine from the outside. And the reason why I picked something like a database is it's infinitely harder than like the web applications people build today.

    On the database side, you literally need to know when it's safe to upgrade that database, 'cause once you lose the data, then all bets are off. So in the world that Pulumi, you can get really far from brute force. So then you ask yourself, is there a better way, because we're now we're linking to many of the details, and maybe you're going to ask a developer to configure some of these knobs that should actually be inside of the system. So where do you put it? And I think the evolution where people explore is like, maybe we put it in the platform. Some people would argue, maybe we tell Kubernetes to have better extractions for running a database.

    So maybe in the Kubernetes world, there's something called database object, and you can give it a database service and it will do all the right things in terms of generically, attaching data, detaching and attaching things, when things crash or come back alive, but it'll never be perfect for every single database. Then you can teach Pulumi to target this Kubernetes database object. And so your Pulumi code shrinks way down because you're dealing with a much cleaner obstruction. Now there's still going to be integration works. They're gonna have to take that database username and give it to another system.

    So Pulumi still adds a lot of other value because you probably don't want the database passing out passwords to other systems. They're still going to be ruined for this second tier orchestration. But then there comes a time where you say, "What happens when the database gets way more complex and should that database then take on the responsibility of having its own API for doing things like backups and self-healing or growing its cluster horizontally versus forcing Kubernetes to do it generically. And in that mode, then we start to get this nice system of flow is when we learn new patterns, we can decide at what layer to put those patterns. And I think to wrap it up is maybe over time, those databases get so powerful in terms of their automation hooks that they expose.

    You might just be able to point Pulumi at the database and say, "Deploy yourself to Kubernetes." Right? That's the extreme side of it. So I think that's where as an industry, we rustle, where do we put these things? And also you gotta be careful, you know, what if you start to put automation hooks for platforms that aren't very popular, do you have automation hooks for Kubernetes, Nomad, Cloud Run and five other systems? That's going to be the biggest challenge? Where do you place your bets? Yep. Yeah. It's interesting working in the infrastructure's code space.

    You know, honestly, when I started down the path that led to Pulumi, I didn't know, I would end up in infrastructure's code. It turned out that, that is a highly programmable way to stitch together the building blocks. But one of the key traits is that it is goal, state driven. You declare what you would like, and then you let an Oracle, IEA and infrastructure's code engine figure out how to converge the current state to your desired state and leave the reliability and all the security elements and everything else to that Oracle so that you don't have to open and code it yourself. Kubernetes was built around this fundamental concept of eventual consistency, goal, state driven configuration, a control loop that can continually converge towards that, even in the case of unexpected failure.

    So self-healing definitely, you know, from what I see, it's a great kind of goalpost for what excellent, you know, infrastructure self-healing systems looks like. Do you think that the Kubernetes control plane is at the end of the day where the dust settles and that is going to be the thing that rules the world of infrastructure management. It's a good checkpoint for all the things we learned before Kubernetes. And I think what people are starting to understand about complexity is it will live somewhere. And when Kubernetes brought to the table was being very explicit about where it lives.

    In the Kubernetes world there's this idea of a controller and for most people and the things that you get out of Kubernetes in the box, out of the box, you know, the ability to configure and manage load balancers, to deploy containerized applications. Those control loops is where the complexity lives 'cause if you look in there, you'll see just how complex it is to support all of these low balancers that is forced to support. But since we encapsulate the complexity, we don't run away from it. We encapsulate it and be very explicit. And by being explicit, we created an API and that API is what we call that Kubernetes resource model.

    And I think from a configuration as management standpoint, you look at that and say, "yes, I can deal with this explicit API versus having to reinvent the stuff that we see in that black box inside of those controllers." So I do think Kubernetes has brought this very clear direction for infrastructure. We too can benefit from control planes that have APIs and intentionality. And then we can put the complexity in a box, but this time a box with an API, I think that pattern, that formula is here to stay and we're going to see that apply to other systems. So whether Kubernetes sticks around or not, that pattern will stay with us.

    I'm curious to hear, I've heard wind of you've really helped to improve the usability of some of the abstractions that your team is shipping at Google through I think you call it empathetic engineering or something along those lines. Could you talk a little bit about that? And maybe some of the lessons learned that the audience might be able to take home with them.

    I read a story about a person who worked on light engines for cars. The person had no driver's license, and this is like a weird scenario. It's like, how do you know that you've built a great engine if you've never driven a car? And so I think there's a little bit of empathy that goes into the thing that I'm working on.

    How do I know it's right? And so I think there's something to be gained from using the thing, so in our industry for a very long time, we have that concept of dogfooding, using your own stuff and then you create this very organic feedback loop. It turns out for the Cloud. That's not enough, actually. It turns out in the Cloud, we have thousands and thousands and 10s of thousands of customers that are all coming at this from a different angle of practice. And they all need something different.

    And to your point, they're all trying to stitch together other systems from other vendors. And so without experiencing that yourself, you could be working on one component, let's call it GKE, you could be doing a really great job, best Kubernetes offering ever. But what is it like to use Kubernetes, plus Spanner, plus CloudFlare, plus this DNS service, that might be so much friction that one way to quickly elevate someone's understanding of that world is to put them in the customer's shoes. So empathetic engineering is really about how do you change the person that's writing the software. Right? We can all get formalized specs of what to build, but how do you do it with empathy, right? I want to know who am I building this for? What will their real experience be like? And so in order to create that, we try to give people opportunities, whether they embed with the customer and build something together, maybe support a system or the pager, or try to solve a problem using the exact same paths available to our customers.

    And what we've seen through that kind of work, this idea of empathetic engineering is when you go back to your keyboard, that becomes permanent. When you say something is done, your definition of done has changed because now it includes the customer's perspective. So that's what empathetic engineering's all about, it's giving people the space and the opportunity and rewarding that discipline of understanding what it's like for real people to use what you're working on in real settings.

    I certainly experienced the dog food culture at, you know, working at Microsoft where sometimes it's painful, right? You're using software that clearly isn't quite there yet, but that's part of the process of helping to get it there. But the point around Cloud, I mean, it's highly fractal.

    You can't even imagine all the ways it's, it's going to be combined and used, thousands of services, you know, customers using it at different scale. It's, it's definitely, you know, a difficult world. So I love the concept of empathetic engineering, I think I'll have to borrow that. So, I'll ask you a potentially dangerous question, but you can, you can take it or not, if you'd like. Prediction, a lot has changed even in the last few years alone.

    Is it clear to you in five years, where we're gonna be? And if so, what does that world look like? Given the history of other areas like electricity, you turn on the light switch, it tends to come on, the light does. That's the type of interfaces that most people want. I want to reduce the number of options I have to make something work. If you wanna get advanced you can get a dimmer. I can turn it down to something, but the interfaces get simpler as we understand the problem space much better.

    When I look at infrastructure and the things we've been talking about today, we don't have a lot of options for people who want to flip up light switches. We're asking everyone to learn how to build power grids right now, and that can't work. That's not going to ever scale to where we want to be, because I think what we want to do is go from, I think there was a time period during my career where the goal was to get the next million developers. At some point, you're going to have a billion developers, right? These are people interfacing and customizing their own tools, right? You customize your budget, you customize your financial apps. All of these new tools are allowing customers to be programmers of their own domains.

    But in order to do that, we cannot ask them to learn the skills set of the people we've been addressing so far. So I think everything will eventually evolve to this ultimate utility that will allow 85%, 95% of people to build and deliver things safely and conform to all those global things. So pick a topic, look at where we are today. Look at the problems preventing mass adoption. And I think that's where the opportunities will lie.

    Absolutely. Yeah. I think there's a lot of regulation conformance, governments being more involved, green energy, I love, you know, a lot of the carbon neutral emission commitments that folks like Google Cloud and other Cloud providers have made. The climate one is interesting because it's one of these things that now, you know, whether you were fearful of floods and forest fires, some people that wasn't enough. But I think now you're starting to see this situation where business interests now are merging with some of these things that should have been the forcing function all along.

    And that businesses are starting to understand if I can get cheap, renewable, sustainable power, then I can actually grow my data center footprint. I can have more powerful machine learning models and keep the cost down. So I think now that these interests aligned, you're starting to see a lot more investment in those areas. And I think that does accelerate some of these technology advances that we've seen. Yeah.

    Well, I could keep talking all day, but I think we should bring it home with one final question. One thing that's amazing that I know you do a lot is help mentor people, help them early in career, later in career, take me into of those mentoring sessions. Like, somebody who's new to the space, that's listening into this talk. What advice would you have for them? So this one like touches the soul because we all remember how we got into tech. And for me, it was really going to a bookstore and on my mom's living room floor, flipping through that book.

    And you got to remember at that time college had the grades, but it wasn't something I saw myself doing. I didn't know a lot of people in other professional roles like doctors, lawyers, software engineers, that wasn't a thing in my viewpoint. So flipping through that book was in some ways, hope that you could learn the things in this book and you can enter this profession that had less gatekeeping than all the other ones and they paid well and you can actually choose to change your own destiny. And so, I remember what it was like going through acquiring that knowledge and then translating that knowledge into a career and the agency that comes from having a career that pays well. But you can change a bunch of things, not just for yourself, your family and the people around you.

    So when I see new people getting into tech, I know that as a possible outcome, look at the demand for people who do this and the way it's looking, it's going to continue to grow. So the other thing that I realized is that this is hard. If it was easy, I don't know if everybody would want to do it. I don't know if they would pay the way. So what I, what I tried to explain to them is realize that they're probably drawn to this area for a reason.

    And the reason why they're drawn to it, maybe it's to make more money or maybe they really liked doing it. But the thing that's going to be sustainable is the discipline that you're going to be learning forever. I don't care if you have a computer science degree, I don't care if you're self-taught and maybe you payed a couple of thousand dollars to go to the local code school. You're going to be learning for the rest of your career. And then I try to make sure that we can demystify that, as a senior software engineer and I'm pretty sure you do it too.

    We just search for the thing we're trying to do. Absolutely. And I have this saying, No shame "Good developers copy, great developers paste." You don't have to learn all this stuff by yourself. There is nothing in human society where typically people learn everything by themselves, that will be incredibly wasteful.

    So I try to teach them the humility of asking a question and think of anyone that takes the time to give you the answer is an investment in that skillset. So you can have agency on your own career and your own life. So when I think about mentoring someone, I think about being responsible for this person, the whole person, not just the engineer that they're inspiring to be, but the whole person who will be someone who can use these skills and everything that comes with it. Well, what a note to end on, thank you, Kelsey Hightower, it's been inspirational and informational and a lot of fun. Thanks for having me. Thanks a lot.
---
