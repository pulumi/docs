---
# Name of the webinar.
title: "Build Panel Discussion"
meta_desc: Join Wesley Faulkner, Ellen Körbes, Rizel Scarlett, and Paul Czarkowski as they discuss a variety of topics related to Cloud Engineering.

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
url_slug: "cloud-engineering-summit-2021-build-panel"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Build Panel Discussion"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Build Panel Discussion"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/uZgnf1iXi6w"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T15:00:00-07:00
    # Duration of the webinar.
    duration: "49 minutes"
    # Description of the webinar.
    description: |
        Join Wesley Faulkner, Ellen Körbes, Rizel Scarlett, and Paul Czarkowski as they discuss a variety of topics related to Cloud Engineering.

    # The webinar presenters
    presenters:
        - name: Wesley Faulkner
          role: Developer Advocate
        - name: Ellen Körbes
          role: Head of Product, Tilt
        - name: Rizel Scarlett
          role: Junior Developer Advocate, Github
        - name: Paul Czarkowski
          role: Managed OpenShift Black Belt, Red Hat

# This section contains the transcript for a video. It is optional.
transcript: |
  Oh, that was fancy.  We've got a little countdown in everything.  Hi, welcome to this bill panel at the Cloud Engineering Summit.  My name is Paul Czarkowski and I am honored to be in the virtual presence of this amazing group of experts.  How about we all take a moment to introduce ourselves. Let's start with Rizel. Yeah, sure.  So, like you said, my name's Rizel.  I currently work at GitHub as a Junior Developer Advocate.  You can follow me on blackgirlbytes.

  I'm probably gonna follow back and interact with you.  So, definitely follow me there.  I have like a background in software engineering, mostly front end.  So, I wouldn't call myself an expert in cloud development, but I'm excited to learn from the other panelists. Awesome, and Wesley, tell us a little bit about yourself.

  Sure, my name is Wesley Faulkner.  I'm currently the Head of Community at a company called SingleStore.  They're a database company that is unifying both column and row store, that's little plug.  And I've been there for about three months, but before that I was a Developer Advocate for a company named Daily, doing WebRTC work.  And even before that, I was the Developer Advocate and The Technical Community Manager for MongoDB.

  So, my foot in the cloud has been in several different buckets.  If that's where we're using brain analogies.  And I'm also on Twitter, I'm Wesley83 there as on many services.  And so please reach out to me as well, 'cause I love talking to people. Now, Wesley, I was told that you also hold the world record for the number, the most amount of soup dumplings eaten in an hour. Is that true?

  I don't know where that information came from.  I've hired a scrubbing agency to remove that from the internet.  So, it should not be found anymore.  But that is not true and so I will, like I said, publicly deny it, officially. Okay, we'll wait, we can just cut that in editing, okay guys? Yeah, please. All right, I've got confirmation, we're cutting it in editing.  Ellen, finally last but not least. Yeah, I'm Ellen.  I work at Tilt.  Head of Product at Tilt.

  Tilt is a development environment as code solution basically.  And I've been in the Kubernetes developer experience side of things, for, I don't know, quite a few years now.  Used to do that for our first.  So, some of you might recognize me from talks and whatever, some of you might recognize me from like Twitter shoot posting.  We were talking earlier about the bios and then people were asking, okay, how far back should I go into bio? And then there were some jokes there.

  So I would just like clarify that my parents met when they were working in the State Data Processing Company that existed in Brazil at the time.  And according to my mom, my father would type a little bit and then look at her and then type a little bit and then look at her.  And yeah, long story short, I'm here now. That's beautiful. Well, I'm glad that he talked a little bit and looked at her and then talked a little bit more because it brought something wonderful into this world. You're too kind men, stop it.

  I guess we should get started.  And one of the things I thought about, we're at this thing called the Cloud Engineering Summit, and I'm gonna be a little bit honest and say, I don't even really fully understand what a cloud engineer is.  Like, I come from an ops background.  And so I do know that from like, from experience that the practical difference between say a CIS admin and a DevOps engineer, is about $ 100,0000 a year.

  But I don't know if that's the same for software engineer or, and cloud engineer, or if there's a little bit more in depth and a little bit more to it.  That's the question, sort of. I will jump on that one.  I would say that the difference is, there's several different specialties and several different varieties.  And so being able to orchestrate different types of environments based on your needs and wants, can be very custom targeted for even verticals.

  Like if you're in finance, if you're in a place where you're dealing with extremely highly regulated industries, it's a variety of different things.  But I would say a cloud engineer is someone who is more versed on how the infrastructure is set up and how it's orchestrated and how it's maintained.  And so, there's a lot more of like, getting what the requirements are and making sure that it works the best as possible, but also being able to troubleshoot different specific types of environments, but have them look almost the same, depending on your needs.

  Yeah, I would agree with you.  I mean, I have a background in software engineering and I've like played around with AWS and Kubernetes a little bit, but I wouldn't say like, I understand every single thing that's going on and why I'm doing it. And I'm not like provisioning and maintaining some of these things.  I sometimes had to do those 'cause I like worked at startups and, you know, there was nobody else to like set up a dynamo DB table, but I don't think I have enough like knowledge and background.  So there is a big difference to me.

  Yeah, to me, it's a bit like, for example, you have a game engine developer, is that a software engineer? I think, whatever the we're talking about is a specialization of software engineering.  And sometimes even you can be working on the thing and not for example, you can be working on cloud stuff, but you're not a cloud engineer. For example, maybe you're doing something and all the cloud stuff is abstracted away and all you have to do is, whatever thing you were a specialist on and you don't really know what you're doing, even though you are doing effectively cloud development.  So, I think it's just.

  Do I, am I a security engineer now? Absolutely, you're now the security engineer and you're now responsible for the security of the entire side going forward. It's just, that's how it works. I will watch for you on LinkedIn for that. Okay, thanks. So, I guess that's probably a really good point.  It feels like we're seeing a lot more of like, the concept of like that full stack engineer that does everything.

  And maybe that is one person wearing many hats, maybe it's like the line blurring between like, what is infrastructure code, what's AppCode.  And like, even like, what's like application lifecycle with like CI/CD and GitOps and stuff like that.  So that line appears to be getting blurry.  Like, is that accurate? And if it is, you'll see it as a good thing or do we, can we take it too far or not far enough? I think that I've seen you come off of mute, Ellen, so you can jump in.  But I think that maybe it's getting a little blurry, but I don't know if that's a good thing.

  'Cause I don't think that everyone should, everyone can't be a generalist or good at every single thing.  So, it almost doesn't make sense.  It's good to like, have like that extra knowledge to be able to like dive in if something's broken, you know how to like try to like, noodle your way around there.  But I don't think that like all software engineers should be doing infrastructure development and all infrastructure engineers should be doing app development 'cause I don't think things will look great.  Like, that's like your backend developer doing CSS. That's not gonna look as great as we hope it would.

  Yeah, I guess I have strong opinions on this.  So at my job, what we do is basically abstract away, Kubernetes and microservices complications so that people can do what their actual job is.  And that's kind of our goal, but also from the companies we work with, for example, sometimes people are complaining oh, doing hacks with Kubernetes as hard.  And then we go like, oh, we can add a few buttons here so that if you just click a button and then Kubernetes does the thing and then we bring it back to them and then they're like, no, no, no, developers should not click on anything Kubernetes, they should just write their code, don't let them touch Kubernetes.

  So, I feel like what I see is a very strong push towards let's keep it separate 'cause when we try to mix it up, everyone is confused.  And I know this opinion is not popular in many circles, but what I can see, like feet on the ground, in the actual people working that day-to-day, definitely the more you try to mix disciplines, the more messy it is.  So, what I would say is have someone who really knows all the cloud stuff, they set it up, they create the automation, the abstractions, and then like, oh yeah, you're a front end developer, a backend developer, you're a security engineer, whatever.  Well, maybe security is different, but all the other developers should like, be really good at your thing and then let the person who's doing the other thing, be really good at their thing.

  I have to say that it kind of reminds me of, I left this out of my bio because, you know, we were constrained on time. But I used to for about a decade, I was a social media manager, like in the very beginning of when social was a thing for companies to start actually doing. That was on LiveJournal, right?

  This was on LiveJournal? This is Friendster actually, I think so a little bit later, yeah.  But when social media marketing was basically, can you post the Facebook? That's basically what it was.  And then it went into, once you post on Facebook, you have to like attach an image.  So, now you have to do a little light image editing, and then you have to do video 'cause video is gonna scale and that's where we're gonna reach people because that's better, so you have to do video editing.

  And then, oh, we need to do metrics, we need to make sure to see if it's working.  And so you need to do some analytics and do some analytics and tied to that.  Oh, but you know, animated gifs are really good too, so you need to do that.  Oh, and we need to do some overlays and some compositing in order to make sure that all the other stuff kind of like really comes together and then, oh, we need to do some like ABM, like some account based marketing.  So, you need to target to make sure our message goes to specific places.

  Oh, and then we also need to buy some ads.  And so we need to do some ad targeting on top of that to make sure that.  It just kept growing and growing and growing as the market became more sophisticated.  And then we started having more tools to actually target the thing that we're trying to do.  And then we had some automation that was brought in to help make it so that you can just post once and it goes everywhere.

  So, I think there are positions where, you want someone to kind of try to do everything and it may not be the best, but it's better than not doing it at all.  But, as you grow into more specialized and more bigger budget, and you've gotten the, all the low-hanging fruit is gone, and you're trying to do optimizations, you're gonna need specializations in every little thing in order to really not just leverage that specific thing, what your advantage is and that one platform, but you also need to make sure that for whatever you're doing that, not just the defaults of what you think is good, but just really tweaking it, doing the testing, look at the numbers and really fine tuning that knob to get it right.  But also, it's good from a, like an employee employer relationship to realize that when talking about the analogy of social media, those roles like entry level, social media roles, and they want you to do everything.  If the employer is not really educated on all the nuance into what our role is, then us in the field will be undervalued because they won't understand all of the things that are on our plates, and that we're responsible for, or also how much better and worse it can go.  Like, there's a huge variability on how you execute.

  You can make it just work, or you could make it like optimize for like, your bills to be lower, or like your downtime to be shorter, or your replication and different regions, to be optimized for where your data lives, as opposed to where it's access to cold storage, to like life management of where things are, you know, there's whole kinds of tierings that you can do.  And it's very complicated and it is getting simpler because it's allowing one person to do a lot of bigger different things by trusting in some of this infrastructure.  But as you get bigger, there's gonna be more nuance.  And even if you see like these large companies that have security breaches, because they don't have people specialized in security, they check a couple of boxes and they think, hey, I'm good.  With more, more users, more visibility, your target becomes bigger.

  And so, and that's gonna be for every link in the chain.  So, yes, it's good that things are getting more complicated, but yes, as you get bigger, you should, in my opinion, become a little bit more specialized. Great, so I feel like, oh, go ahead. Sorry, yeah, let me pick up something that Wesley said.  I think it's important for people to realize that like he said, at different scales, things are different.

  So for example, you have a startup, it's like five people.  Yeah, you're gonna have to do everything or, things that it feels like everything.  'Cause there's no other way.  But the thing is, you're not gonna do a great job at any of them.  And when your company grows to 50 people, people are gonna spend a lot of time fixing all the things you didn't do very well, and that's fine, that's normal.

  But then the thing is at that scale, you shouldn't be looking for more people who can do everything just like the person who was in the five people startup did.  Now you're looking for experts.  And then it's important to have the principals, senior staff, director of something something, sort of like one person who actually is familiar with the whole field to coordinate all the experts, so that's important.  But if you try and get that person, the senior or some director, blah, blah, blah, to actually do all the things that person's gonna go absolutely like, yeah, their head's gonna explode 'cause it's too much.  So at one point, the person who knows everything should do everything 'cause there's no other alternative.

  Later, that person is gonna stop doing the thing, he's gonna start coordinating and letting the people who actually understand all the details, do their jobs. So, I guess in the olden days, we would often like at the enterprise level, call that person, the enterprise architect, is there like a cloud architect, type, role or position that would be different enough from that to be its own thing? Or is that even something we don't necessarily even need now, like a dedicated, like architect type role?

  I think at that level, the person should like, whoever is in that position should be up to date on whatever the industry is.  So, if you're, there's something, something architect in 2021, you need to know cloud stuff, that's my take.  If you don't, then you probably should not be in that position. I've talked a lot.

  So I'm trying not to hog the mic, but I'll just say one little thing.  What you're saying makes sense in terms of the skill, but not necessarily the title, titles come and go and they just get made up.  What's most important is the skillset over whatever you call it.  So, depending on, like we mentioned the scale of a company, you might have all the things.  But as you get bigger, you actually might need more like a specific cloud architect for each cloud maybe or something, I don't know. But yeah, the skill is the big top line, not necessarily the title.

  All right, and then from the, like the difference between like infrastructure and application focus like developers, like, in the past they were super distinct.  We kind of merged them together with DevOps.  We kind of split them out a little bit more with SRE and with some other things, like where do you all feel like that fits? Was it too far when like every dev team had their own DevOps or is it too far when we have a separate DevOps team? Like, how do you all feel like that sort of stuff should work in a healthy, medium size environment?

  I don't think it's too far to have a DevOps team that's dedicated to a software engineering team.  Like I mentioned already, I've been in startups where like, we didn't have that 'cause we weren't at that level yet.

  So, it was kind of just me, like putting up Lambdas and being like, oh, I hope this is right.  And I mean, nothing, nothing broken, I think everything's fine.  But it would have been great to have a DevOps team to make sure everything was going very smoothly, even for like, releases that we did, they were so crazy.  Like, we would like do releases at like nine, 10:00 PM.  And like, it would be very manual 'cause none of us really had those skills.

  So, looking back if we had a DevOps team and if we like through to that point where we could have one, I think that would have been very helpful.  We would have been able to like move faster and understand like how to optimize everything.  So, cloud engineers, DevOps, whatever, if you have like a team of backend, front end and quote and quote full stack developers, like I think a DevOps team is definitely beneficial.

  I think there is a, when we look at the, well, let's call it Caesar Admin like, we going to the roots and then what we have nowadays.  I think the main difference is like back then the developer was separate from whoever would put things in production.

  So I would, here's my binary.  Now you throw, you know, shoot it into the cloud of a canon, I dunno how it works.  And so because of that, the teams are separate, right? And now, people went into DevOps and I think it went too far into wanting every developer to understand the infrastructure.  I think that to me, that's completely wrong.  And you know, the experience, I have seen things in practice reflects that.

  But I think people are arguing, people argue a lot about should developers know all the infra stuff, etc.  And to me, what I see the most interesting in this, this shift is all the automation.  So, before you would like, the developer would give the ops person an artifact and okay now put it there.  Now, the developer gives that artifact to assist him that the ops person has built and then that system puts the artifact in production.  That is different.

  Like the developer, having the mechanism to put things in production is different than the developer understanding all the info behind it.  So, to me, it's a matter what DevOps brought compared to before that was good to me is automation, is good tooling and machinery and abstractions.  That's my opinion.  So, I would not say the developer needs to know infra, I would not say a developer should know infra.  Of course, if you want it cool, but we need to have specialized people who know about the infra and then developers can directly interact with that mechanism without needing a person to handhold. But they should not. It's like I can drive a car, I have no idea how a car works.  Basically to me, ops is the car.

  Right, and at the same time, if that car broke down, even if you knew a little bit enough, how much is it worth your time to sit there and try to fix it? It's better to hand it off to an expert, someone who lives and breathes it every day, rather than you getting up to speed, cracking open the manual and say, I can probably fix it if given enough time, but your time is gonna be more valuable spent on doing the thing that you're best at rather than doing the thing that even though you have the skill and knowledge to figure it out, why, why, yeah. And that's an interesting analogy.

  I immediately thought of like roadside assistance, like your car breaks down, you know, you call roadside assistance, they show up and they kind of have a limited things number of things they can troubleshoot before they'll like put the car on a truck and take it elsewhere.  And I feel like there's probably a super interesting analogy there with like, how you handle, like on call and things like that, where, the developer absolutely doesn't need to know how to fix the car, but they might need to know how to do like some of the smaller, like more well-known troubleshooting kind of things.

  Yeah, I know the problem is the engine and not the tire kind of. Right, exactly, yeah.  So, Ellen, you kind of touched on this a little bit earlier, but like how comfortable should say a web developer be with Kubernetes? Like, not at all, like they should never see the Yammel involved in making that work or should they be intimately involved in it? I mean, I feel like you kind of partially already answered this, but I also feel like you kind of have a lot more answer left in you.

  Okay, yeah, my ideal scenario would be Kubernetes is the operating system, I don't know how Bluetooth drivers work on my computer.  I don't wanna know, I don't care.  Just make it so that I click a button and it works.  To me, Kubernetes and all of infra should be like that.  Someone's sets it up, someone who knows what they're doing, who's like, has the skills.

  Everyone else is a consumer, they don't know, they don't care.  If something breaks, either the thing fixes itself 'cause you know, self-healing mechanisms, etc, that there's a whole topic there or someone else fixes it.  I don't think anyone whose job is something, something Kubernetes for example, or something, something cloud, anyone whose job is not that should have to know or care about it. Yeah, I agree from a developer point of view, if something's broken in Kubernetes or Docker or something like that, I just wanna be able to see the logs and go tell someone like, hey, this is broken.  I need help, you fix it.

  'Cause I don't want to spend my day fixing that part when that's not part of my ticket.  My ticket is to like make a button work or something like that.  So, yeah, I wanna be able to use like Docker and stuff like that.  Maybe to do a deploy, be able to read the logs if something's broken, like you guys were saying with the car analogy, knowing like, okay, my horn is broken, my engine is broken, whatever it is, but I don't know, like under the hood, why it's broken or what to do with that.  And I prefer to be at that level.

  Yeah, Kubernetes should be acting like the operating system.  You put it on there, it should run and it should do it the thing it's supposed to do, as long as it's supporting the program and allocating resources as it needs to, you shouldn't have to worry about it.

  So, it feels like we're at this spot where we should, we still need to have people with distinct skillsets, but the more context they have about what's going on the better.  And so it's not that they need to be able to do, but if they know and understand a little bit, it'll make them a lot more functional in the overall structure of things.  How do we kind of make sure that we balance that? So we don't end up just making, just going back to like, everyone needs to know everything, go back to doing the whole skills creep where we need more, and more like senior people, because we're like out skilling, being able to bring people in and train them up.

  How do we stop ourselves from doing that, so we can still provide like an entry-level for junior people to come in and be able to like really contribute meaningfully without spending three years learning how your particular weird way of doing things works? I got to say that's, to me, it's a false economy.  You can do both.  One thing about technology.  Like, if you just look from when I started to where I ended up, the pie just gets bigger in terms of the amounts of jobs.  So it's not thinking that it's gonna go totally creening to the point where like no one could get started because it's just, you have to be so senior.

  I think for every little thing, it can be tiered and there's an entry path.  And some of it could be just like someone starting, almost doing pure automation, they just hit the button and let it go.  And as they find thing that they like, they can specialize and kind of like strip away those layers until you get towards the bottom.  Ultimately we're all working on computers, right? You have memory of storage and you have, like some sort of engine that runs the operations, like a CPU.  And once you, I mean, if you start there, you can keep piling things on.

  And so, somebody could say, oh, well, I can do code optimization.  Someone says, oh, I can do it in C++ then someone can say, oh, I can do it in assembly.  And then, someone says I can do a machine code.  I mean, you can keep going lower, but at the same time, you can still go up the stack.  And so, I think it's, just because it's getting like more complex and there are more jobs, there still is gonna be an entry way for everyone, because there's gonna be ways that the pie is gonna grow.

  Where if you find your niche, you still gonna be able to get closer to the core if you're starting from further outside of the circle, that's just my opinion. Yeah, and I am very passionate about hiring entry level people.  I agree with you.  Like, I don't see why you can't hire them.  I understand that like the needs are gonna get more and more complex, but like you're saying, everyone will eventually grow up to that point.

  I think to me simply hiring a senior person for that role.  And then also like very quickly after, hiring an entry level person so they can work with them and kind of like grow, get to that spot and then do that same cycle again is maybe a good solution of like making sure that the entry-level person is not feeling like they're underwater, but then also making sure that you're not too top heavy as a team or like a hierarchy.  I think if you do that, it should level out 'cause the entry level person is learning, the higher-up person is continuing to grow higher and higher and you just keep doing that loop over and over again.

  So, what I'm gonna say now is basically a pitch.  So, I'm not gonna say the name of my company in this segment, but it's like what we believe in kind of a thing. So like, if you go back a few decades, can you be a software developer if you can't write machine code? That was a real question.  And the answer was, well, here's the assembly, you don't need to know machine code anymore.  And then a few years later, can you be a software engineer if you can't try assembly? And well, okay, more, more tooling, give me another language.  A few years later, oh yeah, this thing is so complicated.  Here you go, here's an ID, more stuff.

  Okay, now your ID can do magic.  And so it goes, and to me, the difference between there's so much cloud stuff to learn, we can't bombard people quick enough 'cause it's too complicated.  We can only hire seniors, because juniors don't know the first thing about this.  The answer to that, to me, another layer of abstraction, more tooling.  So, my company does tooling, company I worked at before did tooling, before that I was riding tooling internally for a company, and before that, I was like working on tools and complaining that we didn't have all the tooling that then I went on to write in the years after.

  So, I think, oh, Kubernetes is too complicated.  Like we hired the, I don't know, web developer, those who know Kubernetes, they can't work here.  No, just abstract Kubernetes away.  That was not a reality a couple of years ago, maybe but right now it is.  You don't need to deal with the intricacies of Kubernetes anymore to be effective as a front end or like, you know, the API engineer or etc.

  So, if you don't wanna do it, don't, and it's basically the responsibility of whoever is setting up those systems and in larger companies to use the right ways, the right tools, right machinery.  So that all the junior people who come in can be effective at the things they know without having to relearn all the opcode of the 68,000 processor for example. And just to piggyback off of that, that's a really good point.  The tooling helps make this more accessible, but we are also in a place where the education is becoming more accessible.  You had to have a graduate level degree in order to work on computers.

  Then it moved into, you can just have like a bachelor's like a CS degree and you can go in and get started.  And then we have coding boot camps.  And then we have like free code camp, for instance, that you can just be able to start teaching yourself this with YouTube videos and hacking things online or going to a hackathon.  The entry-level to the information, is also becoming way more accessible.  So, if you look at the trends, the trends are that there are gonna be more entry-level jobs, or they're also gonna be people who are gonna be more qualified because they're able to access their certificates or certifications, like all the stuff that they need and be able to do it all themselves for nearly free or close to free as possible.

  So, speaking of abstractions, we're often either building abstractions or we're using someone else's abstractions, right? Usually both on top of each other.  Like, is there a way to tell when you're at that sweet spot of abstraction and also like, how do you know when you've gone too far and where have we not gone far enough? Just blast me about abstractions and like your thoughts on where we're at with them.  If we're doing it right, if we're way off. I would say money.  Are you losing a lot of money? Like, okay, you can only, let's say you can only hire senior people.

  Now, senior developers are extremely expensive, they're very hard to find too.  So like getting a senior person in the door, costs you a lot to find them, it costs you a lot to keep them.  Next year they're gonna do the next shiny thing, you need to spend it all again.  Junior people are a lot easier.  A lot of junior people, they just want a job doing interesting things.

  You can find a lot more of them.  So, but they don't know all the things.  And we kind of know the solution that when something is too complicated, build something abstracted away.  So, to me, it's a matter of money, like at what point did, did it become the case that it was actually cheaper to have all the tooling do the stuff than it was to hire only qualified people that could do it without the tooling.  So, to me money speaks.

  It's like, look at how much it costs, look at how much it would cost to have a solution.  And yeah, that's what I think. Wesley you can go ahead because I'm not sure I have an opinion on this. My, I was thinking of like, we're talking about complexity, but we're also thinking about when everything's automated, you click a button and then it goes down a whole chain.  And if you don't know what it touches or how it interacts and something goes wrong.

  If you automated to the point where you don't know where problems are happening or what's can cause them, and you can't like dig deep enough to actually get to the heart of it.  That's something that means that you've probably over automated.  When you click the button and it doesn't do the thing and then you're like, I don't know why it's not doing the thing.  That probably is where you've gone too far.  And you haven't sorry, go ahead.

  I have, if the whole thing went and it broke and you don't know where it broke, you automated wrongly because you need to have visibility through the automation process.  So, whoever wrote that automation did a bad job. Right, if you automated that person job away and you're like, hey, everything works, so we don't need you anymore.  Like everything works.  So, and like when it does break and then you don't have someone there to like, actually be able to have that knowledge or to take it apart or to re-engineer it or to fix it, then yeah, absolutely.

  Yeah, I feel that that's a real thing.  Like you use a new abstraction and then the, I guess the default way to think from a business perspective is great, we can fire all these people that used to, have to know this stuff.  But the reality is like, at least a couple of like layers of abstraction deep, you still need to have a good grounding in it.  Like, even doing like Kubernetes stuff.  Even if you're using something on top of Kubernetes, you still need to, at some point be able to troubleshoot and discover when like slow IOPS happen, right? It's even harder because that's not something that's easily exposed to you.

  Sometimes like people think everything's going right because nothing goes wrong.  And so when you stop using an umbrella, because you're no longer getting wet and then you decide that you're like, oh, things are going great, we don't need this anymore.  And all the problems happen when you get rid of those people, who've been holding back that tide and making sure that all these fixes are happening and you just haven't heard about them because nothing has broken because they've been doing a really good job.

  Right, right.  it's like a spring. If you just throw out all your, you know, cold weather gear and then get surprised when winter comes back around. I think it's like, if you create the pool automatic machine that does your job, you've automated yourself out of a job.  But the next step of that is, you've automated yourself out of a job and you got yourself a job as a pool automatic consultant. Yes.  And you had to file bugs like this joke is not corny enough, please resubmit.

  Right, we're getting close to time.  Does anyone have, have we, have we not talked about something that like is burning inside of you that you really need to like, just get out there and talk about any final words of wisdom, parting goodbyes. Oh, you're on mute. No, I never gonna say something. Oh, I was gonna say the only thing I wanted to talk about is the question of like, who should touch production systems.

  I was curious about that.  'Cause I like, I wanna touch production systems.  Like, how else am I gonna know, like what broke, what went wrong.  Especially if like, sometimes something works locally for me or on staging and all that, but on production, it doesn't.  So I wanna be able to dive in. So, I'm curious about y'all's opinion on that. I would say if it works in development and it doesn't work in production, you probably don't have a very good development environment. True. Of course, not always but I see that a lot.  And I think more importantly, and this is like an opinion.

  I think more important than a developer, having access to production is a developer having fast feedback towards what they're doing.  So, you'd known that like, okay, sometimes you do stuff and you're only gonna find out if it works in production, no chance to replicate.  And sometimes that's the case.  It's the case a lot less than most people think, in my opinion, there's a lot you can replicate in development environments.  And then I think the important part is, for example, and I'm going very close again to doing a sales pitch, but I'll try to hold myself back.

  For example, you're working on a service that depends on another service.  You spin up both locally on your machine, you make a change, it looks good.  You push the commit, it goes into Kubernetes and it's broken because it runs on local hosts, it doesn't run on Kubernetes.  If you can make a change to your code and it sinks live in half a second with your development environment, your development environment is Kubernetes.  It has the same config, the same policies, the same everything that your development environment does.

  You can see that instantly in the blink of an eye, whether it worked or not.  And when it goes into production, it's very likely that the results you signed developments are gonna be the same in production.  Unless of course, it's one of those exceptions that, for example, if you depend on high traffic to know if a thing works, you're not gonna have as much traffic and development.  But if it's like, does the thing work or not? Like, are the configs rights, do things mesh well with each other? There is a lot you can do in development with instant, like near instant feedback.  And I think a lot of people don't realize that they can have really good dev environment. And then you end up with all sorts of trouble, like people developing local hosts, and then it doesn't work. You're not wrong, I feel like some of my developer environments have sucked.

  Yeah, simulation like you were mentioning before is something that can help with load testing and some of those variables that you can't do in like staging, but also I think if you are a developer and you are pushing to production on your own with great power comes great responsibility, expect like something goes wrong, you're on the hook on it.  You're in that team working to make sure that's done.  And it's the burden on you to like get everyone in the loop and to make sure that you monitor that.

  And if you need help, you get help in that, that structure is in place to support you, if you're pushing the production directly.  I rather like hand it off than have someone monitor, make sure it's good.  But, if you feel that you need to do it, I think you should be empowered to do it, but there should be a system, not just like technology, but like, a policy in place to make sure that you are supported and that everyone knows if something goes wrong that there's a way to make sure that it's taken care of in a timely manner.

  All right, I feel like even from like an old school operations perspective, production should really be a look, but don't touch unless there's a really, really good reason to touch, right? 'Cause the moment you change the smallest bit and in a way, even just logging onto a server, changes things.  You've potentially invalidated what your automation does, and then you've also potentially not captured any changes you make to fix it and brought them back to your automation.

  And so I kind of agree with what Wesley said, which is like, you should be empowered to do all the things that can be done in production, like safely in the scope of your like processes, policies, and tooling.  But like, none of us should be playing around with production for the sake of playing around with production.  Hopefully, that's not a thing we do anymore. Cool, I knew this was like a spicier question for me.  So I was like, I really wanna know your all stats. The tie on the scope of scale.  Yeah, that's very spicy.

  Very spicy.  All right, so let's call it.  I think, I don't know how we, how are we doing? Have we covered everything? Do we need to reach into the people behind the curtain and ask if they want us to talk about anything else? Do we need to spend time talking about favorite foods or anything to take some time? I do wanna say one little thing though.

  We talked about what the future looks like and where we're going, we talked about automation and I think automation and abstraction is like, it's clear that's where that's coming.  What I'd like to see.  And this is a little off topic ish, around technology is the responsibility of one person for each role, instead of it being more equitable in terms of, you know, coming through the pandemic, making sure that we have a strong work-life balance, that we are people we are not machines.  And then also with respect to specialization, that it's impossible to assume that each person is well-rounded as well as specialized.  And sometimes you're gonna be good at one thing and bad at others.

  And hopefully we can move towards a skill based economy where the skillset is where we're trying to really like hone in and do, and not all this other stuff.  Not that it's not important, so think like you are, need to be the person that's implementing it, designing it, writing the report, giving the presentation, and then like that's all considered one part of the job.  Maybe if we can just start splitting those things up as well, and not just looking at the infrastructure and figure out what goes where.  I just wanted to say that, my hope is that we will move beyond just wondering about who are we gonna hire, but like, what are they gonna do and do they really need to do that for us to be successful?

  You see Wesley, now you've set the bar and now we need Rizel and Ellen to also tell us their hopes and dreams about the future of cloud engineering.  If they can choose who's gonna speak first.

  I know we both said, we'll go first.  I'll try, let's see.  I think what I hope for cloud engineering is kind of similar to what all of y'all said so far is that we are moving to a space where I don't have to dig in AWS logs and Kubernetes especially as like a more entry level or early career developer, but there is that push of a button and I still get some insight into why things are happening, but I'm not responsible for all of that.  And when I say I, I mean to be representing all the other early career developers out there.

  Yeah, I was alluding earlier, before we started recording that I could rant about all these things for 10 hours and I'm kind of trying to follow the conversation, but yeah, there's so much we could talk about here like, as the discussion was going back and forth, I was thinking like, how much, for example, like, there's so much stuff you're like, for example, should every developer know how to install Docker? Like you would think that's simple, it's not.

  Or like just install Kubernetes, like kubectl, etc, that's work.  There's so many questions like, for example, I keep talking about development environments and then everyone's like, oh, but I can't run all of Netflix on my laptop.  The experiment doesn't have to be your laptop, it can be depending on the scale or it doesn't have to be sometimes it's both on your laptop and in the cloud and things talk to each other.  Yeah, so I think going forward, we're probably gonna see a lot more, very easy to use solutions that right now are very complicated to implement.  Like there's a lot of stuff, I see it at partner companies that I work with that are like, you just got to stop and really give it to them that, well, that was an idea I would have dared to implement and they did it and it actually works.

  So maybe you should copy that and make it a push button productized, easy to use version.  So, I mean, I'm certainly biased 'cause I'm building this stuff as it happens, but yeah, there are so many elegant solutions to these problems that I think if in the future we can make them very easy to use for everyone without previous training, without anything just here saying default, takes your app, does the thing, there's so much room for growth there.

  Nice, well, look, thank you all so much for joining me.  This has been a really fascinating, enjoyable discussion.  And thanks everyone, at home or in your offices or wherever you're watching this from, for joining us. And everyone say goodbye. I was supposed to do two hand bye waves, bye. Okay, bye. But that's just how you're supposed to end Zoom calls and stuff now, right? Bye, bye. See y'all.
---
