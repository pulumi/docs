---
# Name of the webinar.
title: "Migrating a monolith to Cloud-Native"
meta_desc: In this talk you will learn how to migrate a large monolith codebase to Cloud-Native and learn a few gotchas along the way.

cloud_engineering_summit:
    track: deploy

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
url_slug: "migrating-a-monolith-to-cloud-native"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Migrating a monolith to Cloud-Native"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Migrating a monolith to Cloud-Native"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/0Jnq-M_7se0"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T15:30:00-07:00
    # Duration of the webinar.
    duration: "24 minutes"
    # Description of the webinar.
    description: |
        So your company has finally decided to move to the Cloud Native ecosystem. You’ve landed on containerization as your first step. You heard that all you needed to do was containerize your first app and then push it to Kubernetes/OpenShift/Nomad, and the cost savings just come. You’ve done this, and well, things have gone not as planned. Some of the tech didn’t do what you expected, and wait, what do you mean our OpEx has gone up?

        Simply said: the promise of containerization or migrating to the Cloud Native ecosystem can be a lie if you don’t do your homework. Sadly most companies don’t. In this talk, I’ll explain a few gotchas that a “few” enterprises, in the guise of AsgharLabs, hit moving towards the Cloud Native world, and hopefully, you’ll learn from their mistakes, so you’re trip down this path will be more comfortable and closer to the promise.

    # The webinar presenters
    presenters:
        - name: JJ Asghar
          role: Developer Advocate, IBM cloud

# This section contains the transcript for a video. It is optional.
transcript: |
    Hello. My name is JJ Asghar and I'm a developer advocate for IBM cloud. You're here to see migrating a monolith to Cloud-Native and the stumbling blocks you may have not heard about. So let me go ahead and switch over to my slides. Hopefully you can see an IBM slide here now and there we go.

    So here we go. Again, hi. JJ developer advocate for the IBM cloud. You can find me @jjasghar on Twitter or I really do have the address or email address of awesome@ibm.com.

    So your company has finally decided to move to the Cloud-Native ecosystem. You've landed on containerization as your first step and you've heard all you need to do is containerize your first app and push the Kubernetes or OpenShift or Nomad. And the cost savings will just come. You've done this and well, honestly things haven't really gone as well as planned. Some of the tech didn't go, do what you expected and wait, what do you mean our opex has gone up? Simply said the promise of containerization or the migrating to the Cloud-Native ecosystem can be a lie if you don't do your homework.

    Sadly, most companies don't, they just don't. In this talk I'll explain a few gotchas that a few enterprises in the guise of AsgharLabs hit towards moving to the Cloud-Native world and hopefully you learn from those mistakes And so you don't trip down those, those stumbling blocks as you go passed them yourself. So what is AsgharLabs? It's a multi-tech multi-national tech conglomerate that bought hard into the VM ecosystem. They make ones and zeros like no other company but notice that they were falling behind. In all seriousness AsgharLabs is just a collection of different companies that I've seen and the stories I've taken from the different ones that have the same issues.

    Honestly. So I don't say, you know, random airline or random bank, I just say, AsgharLabs. It makes classes so much easier. And yes, it is a fake company and no they're not hiring. So what did AsgharLabs think they needed to do? They only thought they could take their migration from the physical data center or co-location to the VM ecosystem right? Using that exact same technique where they could just move their monolithic applications to Cloud-Native.

    Bare metal is the same or bare metal to VMs is the same as VMs to containers, right? I mean that's, that's a promise, right? Well, obviously it's not, that's the whole point of this talk. I came into this conversation normally with AsgharLabs when they've had a few of those successful migrations. Which honestly I beg to differ that they work. They're nowhere near where they thought they could have been for the amount of time and effort and money they've spent. I'm the Cloud-Native expert that comes in and asks some very simple yet very tough questions that believe it or not, are deceptively hard to answer.

    So let's ask, let's ask these questions now so you can kind of see that conversation that kind of peer and hopefully, make your life a little bit easier. Let me go ahead and fix my screen real quick. It seems a little weird with me, chopped off, doesn't it? There we go. So here we go. Let's ask those questions now.

    So first question. Who containerized your app? Honestly? Was it developers or the operations team? Was it a dev ops team? Was it the COE? The center of excellence? Was there more than a couple of status meetings? The cough AsgharLabs cough, between the project teams and who shipped it? Like wasn't actual like communication back and forth? It's really important to know who actually containerized it. Followed up with, why? Honestly. Like why did we containerize this app? AsgharLabs containerized it because they were told to. Somebody read a magazine in an airplane and said, "Hey, we need to containerize this app now.

    We need to beat Cloud-Native, so go do it." Is it no other reason than some executive wanted to be next gen? I've seen this happen with the cloud where people move from in the black with physical hardware, moving you to the Cloud-Native into just VMs and they went into the red because the amount of effort they had to spend on migrating from bare metal to VMs. That conversation happens with VMs to containerization now. It's a really important thing to ask. Why did we actually containerize this thing? Next question is where? Where do you plan on deploying this? Or where have you deployed this to? Disperse from the conversation in which cloud are you using? Was it because of choice or was it because of some ELA? Is the best, is the best one for our company the one we're actually using? Or is it the one that we're forced to use? It's important question to ask, because if you do a lot of ML, maybe a cloud that isn't IBM cloud.

    Some would think different out there. Or maybe you are really bought into the AWS ecosystem, but you're forced to use Azure for some reason. You really need to really look at where you're planning on deploying your application. And finally. What did we actually containerize? This comes from the actual architecture of what you containerized.

    The actual conversation around it. Like one of AsgharLabs' subsidiaries just took a WAR file, could have actually honestly been an EAR file, I don't really know and they think they could just shove it into the Docker container and call it a day. It's opened up so many conversations about why going down this path they did. So let's actually look at some very specific container, some architectural changes that you'll have to do when you move down this path. Just before, oops, I'm actually in the way.

    So let me move myself up here, make myself a little bit smaller. There we go. And transition, there we go. So this is that first step, right? The replatform example. They took that EAR file, they took that you know that WAR file and shoved it into container and made that happen.

    They thought this was as far as they needed to go. I beg to differ. I beg to say that this is just the first step. When you just shove a container into, shove a WAR file into a container. You don't take advantage of the scheduling or any parts of OpenShift or Kubernetes in the Cloud-Native ecosystem.

    A lot of that time, for instance, cause I work for IBM, of course I say WebSphere. WebSphere exists, there's a lot of things around it that take care of a lot of your application. OpenShift and Kubernetes don't have that by standards. You have to start thinking about how to build those things. So let's talk about the next step.

    You need to start looking into repackaging into microservices where you take that WAR file, now you break it up or if it's an EAR file, we break up all the WAR files into different small little applications. So you can start having their own histories, their own speed to deploy things. So now all of a sudden you don't have this one big WAR file that deploys everything. Again, it doesn't have to be a WAR file. It can be a Python app.

    It can be whatever. I'm just using that as an example here, and you start cutting it all up into small different pieces. So then you start repackaging to allow for the different levels and different velocities you want to be able to add to deploy your application, but this is only the, the second step to regarding to true Cloud-Native. The third and probably the final step, which actually is the longest one to get to is refactoring into something called the strangler pattern. And I'm using refactor as the actual term here, because you're going to have to refactor your application to work into Cloud-Native.

    Strangler pattern if you don't know, is the ability to slowly but surely take bits and pieces your application out and not just microservices, but even smaller portions of it. So you can start creating functions and things like that, where everything now has a bunch of different widgets to be able to be successful. Obviously it depends on the different applications out there and the way that your applications are ran so I can't actually give you a great example off the bat here but take a few moments and look into the strangler pattern, refactoring your application to it. It's a journey to get to this point. It's very important to recognize.

    So let me go ahead and bring myself back down into the corner here so we can start talking about some architectural advantages and disadvantages of going down to this path. The first of all, going spending your time in the space, velocity becomes the most important value prop. Now people are starting to bring out applications so quickly that if you have to spend any time not doing the Cloud-Native way of deploying something, you will be left behind. The ability to focus on your own histories and scoping your clusters for what you actually need, which will help you save a significant amount of money will only benefit you in the long-term. Having one big pod is not as good as having multiple smaller pods.

    So when you start building out that strangler pattern application refactoring it, you start building different services with different pods, so you can scale out what you need and when you don't need it, which in turn allows you to actually optimize for the hardware you have. But on the flip side, this all requires such a higher level of cooperation. You need to build out more advanced integration tests, along with likely most likely a completely different deployment policy system. I didn't realize at the time that this, the concept of CCB was not considered an industry standard, but when I was working in a place at an AsgharLabs company, they had something called the CCB or the change control board where traditionally a bunch of middle managers would literally get into a room every Thursday afternoon and give a thumbs up to say, yes. Let's do the deploy this weekend.

    I was actually part of that at one point where I would, when I saw those thumbs up in that meeting, that means I was waking up at three in the morning on that Saturday to deploy the application. Now that just does not work inside of the Cloud-Native ecosystem. Imagine the hundreds of possible deployments you could doing during the day with microservices. That whole change control board is something of the past. It just doesn't work.

    So then imagine the cultural change that you're gonna have to make happen with all that. All of a sudden those middle managers don't have that level of control or understand it. So you're gonna have to work and have a collaboration between all these different people to be successful. Hey JJ are we doubling up on things like, as we move down this path, why is there another load balancer inside of Kubernetes or OpenShift, or why is there a scheduler there when I have a schedule written to my app? Well of course you're going to need to audit and verify your application. As you refactor and move down this path, you're going to have to do your homework.

    There will be a time where you're going to see, you know, basically an application where you might have a scheduler built into it that you're not leveraging the scheduler for, for instance Kubernetes. A great example is that I saw this one AsgharLabs company, that has a scheduler built into the job application, and whenever it spun out trial processes, it would spin it out and it would sit inside that pod. Now inside of the Cloud-Native ecosystem or instead of Cloud-Native, at least Kubernetes and OpenShift, you can't spin out child services outside of the pod. So when all the sudden these child processes would start, they had come to me and was like JJ, why do we see all this usage spike on this one specific node when we have three nodes, shouldn't it leverage it across? I'm like well no, because you're running everything inside of one pod. So it's all just staying on that one cluster one note.

    They're like oh. So we should just make one really big note. And I'm like no, don't do that. That's a horrible idea. What you need to do is leverage Kubernetes for what it is and create a way to have a service that has those child services so when it needs to spin out and do that, it spins it out and loads it across the whole cluster.

    Like oh, I get it now. Well, I mean they're still in the process of getting to it because they had to refactor their application to get there but now they're actually leveraging the cluster for what it was. It's no longer just one VM, if you will, it's now an actual, like clustered application. There's also the challenge of load balancing, right? Where you have a built-in load balancer inside of Kubernetes and OpenShift. And with that, you might not need that F5 anymore because you're going to use the ingress and the way that the networking's done.

    So if you have that, that hardware sitting in your data center, you're gonna have to have some real conversations around this so keep that in mind. So wait, isn't automation good here now? There we go. I'll move out of the way so you can see it. And why is everything so complicated? Well, I rebut by saying it's probably always been this complicated. You just probably haven't noticed to have the complication.

    You've probably had a enterprise engineer or architect who actually knows how everything is done and kept that visibility minimal. But now that you're breaking things out to microservices, now you're actually seeing the complexity of your application and yes of course, automation is good here. Yes. I mean, humans are error prone. So you're going to absolutely need to build that pipeline and to be able to do that work, you need to take the human error out of that complication.

    A great friend of mine said this as I was talking about the this presentation and he really did say this, which was like when you have a monolithic app, you have an ornery bull mastiff, but as you move to the, the Cloud-Native microservices based architecture, you now have 13 yipping chihuahuas. They're both dogs. You both have to care and feed for them, but you're gonna have to deal with like walking one bull mastiff instead of 13 yipping chihuahuas. At the same time having 13 yipping chihuahuas you'll be able to just take one care of one smaller dog, which believe it or not is less overhead when you start thinking about it. it's a great visual representation of it.

    You take it one step farther. And I stole this from a good friend of mine Ken, who stole it from someone else who stole it from someone else. And if something does go wrong, you need to really understand that it does become a murder mystery. Need to take a moment and think about that. No longer unless you have really good aggregated log monitoring.

    You'll have no way to be able to understand what something where something went wrong. You'll have to be Sherlock Holmes, digging through the logs to understand where the different services happened. So you will have to create a standardized way standardized contracts between your applications or your microservices to be able to talk to one another. And this is challenging. It becomes a huge cultural change inside of a lot of companies.

    I mentioned the CCB earlier, and then here's some questions you should really ask yourself about the cultural shift that's going to happen because you will change your culture. The CCB when I first saw it at this one AsgharLabs, it really was something like something out of the Phoenix project if you ever read that book. People stopped coming at one point because it was just useless. With moving to Cloud-Native you naturally start allowing for self-orchestration and rollouts. You really do start empowering the different teams to be successful.

    And eventually you will build that pipeline. And yes, you will, as I say, build that pipeline. And I've said this is the third time now, because you need to trust CI and CD. You'll need to leverage the standards of linting and always make sure that there's standardization for your code. One reason why Go is so easy to read is Go came along standard outside the box with the Go format command.

    So imagine at 3:00 AM, when you have a bunch of microservices things going wrong and you got woken up and having to deal with it because of the Go format command and everything now looking the exact same, the engineer who has to sit there, the operations person or SRE or whatever, they can actually read it and know without having to leverage that cognitive overhead of where that semi-colon or that curly brace is. They could just read the code like a book. That is so important for when that murder mystery happens. So you leverage pipelines to enforce these policies and in shared contracts. Yes people are going to argue about tabs and spaces.

    It's the same thing with Emacs and VI. But honestly, when it comes down to your business, you create a standard, you stick to it, and you will only see ROI in the long term. You'll have to learn to collaborate with the other teams too. The hardest thing I saw AsgharLabs deal with was the actual collaboration between the teams. They had some great propaganda around having a scrum teams and tribes and whatnot, but people still wanted to do things the old way.

    Collaboration isn't just about status meetings. It's more than that. It's really truly creating, declared contracts and responsibilities with a constant communication between teams. Your tickets will only get you so far. One of the most successful things AsgharLabs did, was at every sprint they switched out one person from one tribe to another, for the portion of that global app.

    This took a lot of buy-in from executives above but imagine every two weeks you had a brand new person on your team who had to know how to run part of your application Before you know it, tribal knowledge doesn't exist anymore because you know that Jane DOE and John DOE come over and you have to train them and they have to be useful within two weeks because they'll be gone. And then all of a sudden they know that it turns out that third contractor of that team over there, it turns out this person's really good at X, Y, and Z. So then it builds better cohesion between the different works. Collaboration's unbelievably powerful. Asghar has something you could just buy one product and call it a day when it came to visibility and monitoring and any talk you need to really mention this because there's a lot of companies out there.

    I have friends who work at these companies too, but honestly Nagios is just not going to cut it anymore. When you start moving into the Cloud-Native ecosystem, you're going to need to have different slices of visibility and monitoring because different teams are going to care about different things. You're not going to just have one size fits all. As badly as AsgharLabs wanted that single pane of glass, it's unrealistic. There's just too many moving parts.

    It's a huge cultural shift one of the AsghardLab companies had and they're still dealing with this but you will have to spend some time and effort with that. And to recognize also that we actually have to pay for the economics of this. The ALPEX yes, will now go up. You will have to pay most of this by a credit card. CFOs go back and forth about these things because some love it because assuming your team can keep control of the work and you could control get control of your spend, it's very predictable and the costs are easy to project, but on the flip side, some CFOs hate this stuff because it's really hard to depreciate or it's impossible to depreciate OPEX.

    It has to be CapEx. So those data centers and the hardware they used to buy, there's some interesting economics out there with, with, sorry, accounting practices that allow for depreciation that turns some really interesting stories around. So hopefully your management team at least acknowledges this and wants to spend time to talk through these problems. So hey JJ, what do you mean all our support is on stack overflow now. Well honestly, a few places it is, but there are companies out there, IBM cloud that leverage, open source, and have offerings for some of these things.

    But yes, if you're going to layer on top of it, you're going to have to be part of the community. You're going to have to spend time in the open source community to understand where it's coming and what it's doing. And you know you'll be able to be successful that way but if you do want enterprise ready Kubernetes, OpenShift is a great offering. I had to say it. So let's talk about some really tangible things at the very end of this talk to make sure that you understand where you can get going from the get-go.

    There's a ton of technology out there to help you get going. The best thing is really to just take a moment and figure out when you containerized your app, did you really need to, or did you just wrap your app in a pod and wash your hands of it? Have a large on conversation on why you did this, because honestly, if it's just because you're being left behind, that's not a good reason to. It's good to be in the black. It's not good to be in the red, or is it because you thought you could leverage some software to make your business move forward. That's great.

    Have a larger conversation about it but don't just do it because it's what the cool kids are doing nowadays. Ideally with masking all these corporations I've had exposure to as AsgharLabs, I've helped highlight a few of the consistent issues I've seen which nine out ten times it's just having conversations on why we're doing this technology. The best thing I can do is ask if you really need to. And if you're really committed, or if you've already started down this path, you should probably take a beat and look for optimizations instead of features, which is probably what you're gonna have to do because you have to start learning how to use build that microservices and whatnot. But the remember the more you pay up front, the more you do your homework and use the correct tool for the job, the better you'll get.

    To quote a great friend of mine and I'll make myself small here so you can see his name, Thomas Cate. You wouldn't use a saw when you needed a hammer or you wouldn't use a hammer when you needed to saw right? And it's true. Take a moment to think about that. You can use a saw to hammer in a nail. It's going to take you some time.

    It'd be weird but it'll work. And you can use a hammer if you need to break a piece of saw, a piece of wood apart. It's going to be weird but it'll work. So take a moment and recognize using the correct tool for the job is the best thing you could do. And thank you.

    My name is JJ Asghar and again, I'm a developer advocate for the IBM cloud. Let's see if I can make myself big again. There we go. And thank you. You're more than welcome to reach me @jjasghar on Twitter or awesome@ibm.com and I hope you learned something. Take it easy y'all.
---
