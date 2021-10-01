---
# Name of the webinar.
title: The Future of Cloud Engineering
meta_desc: Pulumi CEO, Joe Duffy, and Chef Co-founder, Adam Jacob share their thoughts on the role Cloud Engineers play in helping organizations innovate faster.

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
url_slug: "the-future-of-cloud-engineering"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "The Future of Cloud Engineering"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "The Future of Cloud Engineering"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/D0xIBOld-i8"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-10-08T10:00:00-07:00
    # Duration of the webinar.
    duration: "43 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Pulumi CEO, Joe Duffy, and Chef Co-founder, Adam Jacob will kick off the full day of talks and panels and share their thoughts on the role Cloud Engineers play in helping their organizations innovate faster.

    # The webinar presenters
    presenters:
        - name: Joe Duffy
          role: CEO, Pulumi
        - name: Adam Jacob
          role: CEO, The System Initiative

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - The past, present, and future of Cloud Engineering.
        - How in many ways the cloud is the world's biggest super computer.

# This section contains the transcript for a video. It is optional.
transcript: |
    **Joe Duffy**

    All right. Hello, everyone, and welcome to the first ever Cloud Engineering Summit. Really excited to have you here. We've got a great lineup of speakers, some awesome content throughout the day. Before diving into that, I want to take a brief moment to thank all the great sponsors that have made today possible. GitLab, JFrog, Jetstack, Chef, AWS, and NSONE. Of course, presented by Pulumi, the company I work for. But really appreciate the support for cloud engineering overall. So with that I wanted to spend just a minute introducing ourselves, getting to know each other before we talk about cloud engineering, why we're excited about this. And to kick it off, I'd like to introduce Adam.

    **Adam Jacob**

    Hi. I'm Adam Jacob. I am the CEO of a company called The System Initiative, which has a website that says The System Initiative with a little blinking cursor on it. And I was formerly the CTO and a co-founder of a company called Chef, which did infrastructure automation. And I'm super stoked to be here. Hi, everybody.

    **Joe Duffy**

    And I'm super stoked to be here also. My name's Joe, founder and CEO of a company, Pulumi, that builds an infrastructure's code platform using your favorite languages for infrastructure's code. And my background leading up to cloud engineering is interesting. I worked at Developer Platforms at Microsoft for many, many years. I really lived and breathed developer productivity day-in and day-out, and really got excited about modern cloud architectures, and that brought me to the world of infrastructure, DevOps and all the great work that's come before us, and really excited about the future of cloud engineering and to tell you a little bit about that story today.

    So to kick off the story I'll start with maybe a controversial position, which is, the cloud really is the world's biggest supercomputer. The cloud is sort of infinite in scale, both in compute and storage, worldwide distributed. Think of really modern architectures are really moving in the direction of distributed applications. And what that means, if you believe that premise, and especially you look at today, the fact that we're not writing client server applications like we did 20 years ago, 15, 10, even five years ago, all software is cloud software. What that means is software's using the cloud for those compute and storage capabilities, but increasingly manage services that add value, and that we don't have to go build all these things by hand. We can leverage these building blocks in the cloud and the leverage them in new ways.

    **Adam Jacob**

    I think it's really important to highlight, "All", here. There's this idea of cloud native software, which has been a pretty big idea, a pretty big concept here in the last couple of years, and it's drawing this distinction between legacy software, which is usually what we mean when we say like, "The stuff that runs all the things that matter most in the world." That's legacy software. Then cloud software, which is like the new stuff that's been written since the cloud has been born. I think the reality is we're now at a place where there isn't any piece of software, regardless of how it's deployed or when it was written, that doesn't have some cloud impact, right? There're some components somewhere probably in what makes it work that lives in the cloud, and ultimately we've sort of already reached the point where every piece of software, regardless of when it was written or how it's deployed, likely interacts with the cloud in some way, and therefore all of it really is cloud software.

    **Joe Duffy**

    Absolutely. And why is that important? Well, it's important because it changes the way we think about software architecture. It also changes the way we think about our teams and how we work with one another. I think of all developers are cloud developers. If all software's cloud software and developers are the ones authoring the applications and designing and implementing them, then that really means all developers are cloud developers and really need to think about the cloud in a first class way. It's not something you think about after you've designed and implemented, but it's really something you think about at every stage of the life cycle.

    **Adam Jacob**

    Yeah, totally. And if you think about all developers today, if there's a part of you that was like, "Ah, not everyone's a cloud developer", if the cloud's a supercomputer there isn't a software developer alive who doesn't think about the computer that their software's going to run on. That's the whole point of running software, right?

    **Joe Duffy**

    Absolutely. I think it's exciting too. Even if you're not directly touching the cloud, maybe you're writing an application that gets packaged up into a Docker Container and run inside of a Kubernetes cluster, well, you can kind of ignore that point, but it's only a matter of time before you need to be aware of that. What happens when you need to debug your application? What happens when you need to do logging and monitoring and understand the performance of your application? All of that means that you will become increasingly aware of the cloud hosting environment. It's not a black box that you can kind of ignore. Related to that is really, okay, think about infrastructure teams. They're really the ones enabling this to happen. I mentioned the Docker and the Kubernetes example.

    The infrastructure teams are the ones providing the infrastructure platforms that developers are going to use to build and deploy their applications, and many infrastructure teams really want to enable this level of innovation within the organization. All of the applications are going to be cloud applications. They're all going to require infrastructure, and the infrastructure team really holds the keys to unlocking all of that application development and software delivery within the team. So that brings us to really the three themes that we're going to talk about today, which is architectures, workflows, and teams. I think architectures are fundamentally changing as we move to these more distributed architectures. The workflows are really how we take those architectures and operationalize them. How do we make sure they're secure? How do we test them and verify them? How do we ship them continuously? How do we debug them after something might go wrong? The teams component fundamentally is different than it used to be.

    It used to be okay that developers didn't really think about the cloud, and the infrastructure team did the heavy lifting there. We're really thinking about teams where cloud engineering teams are taking the best of what everybody has to offer, and making sure that we can collaborate and move fast. We'll talk a little bit about the future in today's talk as well. So I want to spend just a moment motivating where might we be going before we get into a little bit of the details of where we are today and how we got here. If you think about the cloud as the world's biggest supercomputer, it begs some obvious questions. Every computer has an operating system. What is the operating system of the cloud? Where is it? Do we have one today? I think we'll see throughout this that we have a lot of fundamental building blocks for an operating system, but we don't yet have a true operating system.

    **Adam Jacob**

    We both need one and do not have one. I think the most common thing I hear now when people talk about there being an operating system for the cloud, it's usually people talking about Kubernetes as the operating system for the cloud. But I think it's probably not. It's probably easier to think of it as some combination of, is it like a scheduler, is it a kernel? What is it exactly that it's doing? But when you think about operating systems, they're so much bigger than just taking my application and shoving it somewhere, right?

    Everybody who's watching this right now is running an operating system, and you have this window into everything you do that the operating system provides. It's the user experience. It's the developer experience. It's the way the tools are shaped. All of those things are part of the operating system. It's not just running an application. I think we really haven't seen a huge change in the idea that if we have the world's biggest supercomputer, what's the user interface to that supercomputer supposed to be? What's the human experience of using the computer? We've really just extended what the previous experiences were out into being more available in the cloud, which is great, but it's really just a foundation.

    **Joe Duffy**

    Absolutely. And related to UX, which is a great important point, the UX for developers and infrastructure teams interacting with the supercomputer is also still the jury's still out on where that's going to land as well. Certainly YAML is our current programming model interface, and I think we all dream of something a bit richer than that that allows us to build bigger things out of smaller things, and really all the things we know and love about programming models for all these other operating systems, in the future we will have a similar thing for the cloud supercomputer.

    **Adam Jacob**

    Yeah, it helps out, because I think if the model is just YAML I may be out. I might go back and decide that the cloud wasn't for me.

    **Joe Duffy**

    Absolutely. Then finally with the application model, you think of relating to the notion of operating system and what is an operating system, one of the things an operating system provides is an application model. How do I install applications? How do I version those applications? How do I sign them to make sure they're secure? How do I remove them when I want to get rid of them? And today, Docker gives us a nice building block for individual containers, which is great, and there are certainly efforts to go beyond that. Like CNAB and Helm really kind of give us a little bit more of that installation model. But it's really a far cry from, you think of the iOS App Store.

    **Adam Jacob**

    And this goes to speak to almost every piece of that architecture or workflow and team thing that we were talking about just a second ago. Without an application model, what it means is that the only thing we can do to drive this supercomputer is work way down low, right? All we can really do is kind of twist the knobs, a low level in this system, which then results in something we could run. I think when we talk about application models it becomes a little more top-down, right? It becomes a little more like, "Yeah, if you define what this application is and what it needs to run on this giant supercomputer, the giant supercomputer should figure out what that's going to do and where it lives and how it's going to run." And those layers need to be more semantically clearer than they are now.

    **Joe Duffy**

    So that leads you to the conclusion, the cloud kind of broke things, right? We knew what the world looked like in the simple client server model, and as we move to this more distributed model of the cloud as a supercomputer, we're still trying to figure things out. As we were talking about this, a keynote, Adam and I were brainstorming. We really realized that the cloud kind of broke architectures, workflows and teams, and that we're now rebuilding.

    **Adam Jacob**

    Absolutely. I think when you think about the early days of the internet, so I'm 42, and the first time I used the internet was pretty early on, because I love bulletin boards. I ran my first bulletin board when I was eight years old. When the internet started there wasn't like a book you could read or like a best practice to understand how you were going to manage this internet thing you were doing, right? All you really had were like the books that were written about how to run Unix systems in corporations or in university computer labs, right? It was the Dragon Book, or it was AEleen Frisch's Armadillo Book. Those were what you did, and that was the model we all tried to copy when we were running services for the internet.

    It just didn't work, and we had to figure out a whole new way of running things. That was sort of how the 1.0 of the internet worked. But then the cloud comes along. That entire model fundamentally shifted yet again, and it's first pass was really just to take what we had learned in the first part of the internet and automate it some more so that we could hide it behind the APIs. And now we have to go beyond that even and say, "Okay, now that these things, we've dealt with them a little, we've agglomerated ..." Is that a word? I think it is now. "... what it means to do this kind of work. What can we build from here, knowing that this is the status quo, that it's fixed, it's here to stay and that this shape of the universe is what it is."

    **Joe Duffy**

    Absolutely. And I think one of the fundamental things that happen along the way that Adam just mentioned was infrastructure became software, it became programmable. Suddenly there was an API. And this is why all is not lost. We've got a lot of the foundational pieces we need to rebuild something amazing and way better than what we had before. We're still early days. But this is where our cloud engineering comes into the picture. I think it's interesting to look back over the last 10 years, as the cloud was incrementally breaking things, we're having to react in realtime to that and build tools and build automation, and we did a great job. I think the future of cloud engineering could not be possible were it not for DevOps, the last 10 years or so of really practicing DevOps.

    **Adam Jacob**

    Yeah, definitely. Look, DevOPs, I feel like I was lucky enough to be present for the whole evolution of DevOps from its very beginnings to now, and I think it was this really necessary response to these new capabilities that we had. The way that we worked together, the way that we managed things, the architectures we supported, just like now. 10 years ago everything was fundamentally broken and we were trying to figure out how we were going to deal with it. And it started from this place of collaboration and this place of bringing in engineers and operations people closer together so that we understood that it required both of those things in order for the system to really come alive, and it required sort of a holistic understanding of those disciplines in order to adapt to this new world. I think where DevOps landed over time was a little more Ops-y than Dev-y, and the way you know was that when you hire someone to do operations work you hire a DevOps engineer.

    And there were arguments for a long time about whether that was a good or a bad idea, but it doesn't matter now, because it's definitely what it means to be an operations person now. It means you're a DevOps engineer. And if you were to ask a regular software developer who builds applications if they're DevOps engineers, their answer would be, "No", because they're still software engineers. I think where we move from DevOps into cloud engineering, I think cloud engineering is a super set of what we learned from DevOps that's going to take all those lessons about how we needed to work together, all those lessons about the very shape of the organizations and the shapes of the teams, and that need for that holistic understanding of the stack. Then push it into this new paradigm that says, "Okay, but now we need to build systems that were designed for this world instead of just design to cope with the transition from the world we were in to the one we have now.

    **Joe Duffy**

    Totally. So that leads to cloud engineering. What is cloud engineering? And really it's exactly what Adam said, which is taking all those lessons learned from DevOps, really making sure that application developers are leveraging the cloud in a first class way. So infusing the cloud more into application development, especially with modern architectures and services, this is almost an absolutely requirement, but it's exciting as well. The second thing is applying engineering practices to infrastructure. We see that increasingly as infrastructure becomes software it becomes programmable, we're able to actually apply engineering practices. Like testing, like refactoring, like security enforcement, continuous delivery.

    A whole lot of things that we know and love about application development can now apply actually to infrastructure as well. Then the final thing is unlocking collaboration, and this is really where I think DevOps has done an amazing job of really creating a collaborative environment where everybody can come to the table with their own skillsets, contribute them, and move faster and deliver amazing capabilities in a software that we're delivering. To me, this is just a broadening of that approach to developing cloud software, which is to say the entire organization becomes the cloud engineering organization, including app dev, including DevOps, including infrastructure, including security engineering as well.

    **Adam Jacob**

    Absolutely. And the thing that most fires me up about this idea is that it's focused not so much on how do we cope with the change, instead it's saying, "Look, we know how to cope with the change now. We understand what the pieces are. We're coping just fine." This is about, "What can we build? How could it be better? What could be different about the way we interact? How could we really move the state-of-the-art forward in a way that you can't do when you're just trying to stay afloat, when you're just trying to deal with how much has changed." It's really hard to think about what's the new way that we could infuse the cloud into application development, right? What's it mean if the cloud is a giant supercomputer, that it be fused into application development?

    I think it means that the whole paradigm could shift. It could change the way IDEs work. It could change the way application development work. If you think about that applying to engineering practices, if we say engineering practices apply to infrastructure, can we have the same kind of IDE experience that we get when we write code, only in infrastructure? Could we see it across all the different components that exist in the cloud? There's so much potential for the future that cloud engineering really can be this forward-looking idea that says, "How do we become better than what we are?", because now we're standing at a new baseline.

    **Joe Duffy**

    And the most exciting thing of all is we're starting to see a lot of this emerge. So today what we'll do is we'll walk through your architectures, the workflows and the teams that we see comprising modern cloud engineering as it is today, and then we'll spend a little bit of time at the end just talking about, what does the future entail? But if you're excited by this vision, you can start practicing and take some very concrete steps down this road, starting today. When I look at infrastructure, I'll admit my background was more on the developer side for over a decade at Microsoft and even before that. When I got excited about cloud computing with microservices and Docker and serverless, I actually thought infrastructure was boring. I thought it was boring when I came to this space. What I quickly realized is infrastructure's actually essential. Infrastructure is the building block of the cloud.

    Every one of AWS's 200 services, or Azure's 100-something services, or Google Cloud, and SAS providers too, Datadog, New Relic, et cetera, these are all building blocks that we can assemble in unique ways to build new capabilities in the software. I think this is why it's exciting for both infrastructure teams and for application developers. I think of infrastructure building blocks coming in many different flavors. Obviously infrastructure is the essential compute, networking and storage layers that power applications. We see AI and ML services that we can use right off the shelf, right? I think AI and ML are two of the most compute and storage intensive services that you can imagine, and the fact that we can just leverage this huge supercomputer to run them and integrate them into our applications means things like Lyft, Airbnb, and all these companies that are really leveraging the cloud, it's much easier to innovate and build those sorts of applications today, and scale them globally as our workloads scale as well.

    What that means is, infrastructure used to be a tax. We used to think of IT as a cost center that was kind of a necessary evil to run our applications, but that's no longer true. In fact, the exciting thing about this transition is that infrastructure becomes a competitive advantage where you can actually use cloud infrastructure to transform entire business models. I mentioned a few just now. One of my favorite stories is the Zoom CEO who when the pandemic started, COVID started, they saw 10 to 20 X usage almost overnight. And because they architected their application to use the cloud they were able to scale and meet the demand. And of course Zoom is an essential part of our lives because of that. That was all about cloud infrastructure. If the cloud hadn't been there, if we were at even five to 10 years ago, that simply wouldn't have been possible.

    **Adam Jacob**

    As a great example of the evolution from having disrupted technology like EC2, to fully embracing that technology and then using it as a building block of a foundational piece of the entire applications design, one of the most informative things that happens before I started Chef was I had a consulting company, I was working with some friends who ran a company called Zeus, which was one of the first Facebook applications. They were a dating app. And when Facebook launched applications Zeus was the very first thing you could do that allowed you to do dating over Facebook, and it blew all the way up. It went completely insane. Zeus went crazy. iLike was another example where same kind of era. iLike was about music sharing, and you could share music on Facebook and it was a huge deal.

    And the iLike guys, they were literally going around to everyone they knew and asking them if they had spare servers that they could rack to deal with capacity, right? And this wasn't that long ago. When you compare the experience that Zeus had, which was just a little after iLike, where they could use EC2, they could scale elastically, they could do those things. They were using that cloud environment as a competitive advantage and a competitive weapon in a way that even within the span of six or eight months difference, iLike couldn't do. And now you get to something like Zoom where it's a commonplace piece of core infrastructure. When think about this as a massive supercomputer, I think that's one of the reasons that it's the right lens, because that transition over time really is pushing you toward this idea that, "No, we designed it to run on this planet-scale computer, and it does."

    **Joe Duffy**

    It's definitely not easy to accomplish that, but I think really going in with the mindset that cloud infrastructure is a super power and that those who figure out how to harness it to build these new software capabilities really are the ones innovating and creating new experiences, and really it is a testament to, hey, the power of all those building blocks available to us at our fingertips if we can only figure out how to harness them. So I think one of the challenges is how to harness that, but that's really where cloud engineering comes in, which is to say the way to really leverage that is to let developers use cloud capabilities in a first class way, have infrastructure teams empowering the whole organization. So cloud engineering really is all about accomplishing that outcome. So as part of this transition, we're really reshaping the way our applications work. You look back to when Adam was mentioning the early internet days where client server had just become a thing.

    You had a client and a server, there were two moving pieces. Then we started breaking apart the backend services and to NT architectures. Then we lifted and shifted virtual machines in the cloud. These architectures were pretty simple, mostly monolithic. Yeah, there were a few moving pieces, but not many, and very static. So these days we really think of, "Hey, what we're really building are distributed systems." They're complex. They're distributed. So there's RPC mechanisms, its all asynchronous. We need to think about things like service meshes and discoverability. They're dynamic, so oftentimes we're not only provisioning new capacity on a much faster rate, but maybe in realtime in response to demand with some of those serverless architectures. And this just requires us to think in fundamentally new ways about the architecture of these applications. If we have these dynamic elastic distributed architectures, how do we actually build them? How do we test them? How do we deploy them? How do we manage them within our teams? And that's what we're calling workflows.

    And we've been on this infrastructure code journey for quite some time now. So one way of looking at that is, we've kind of treated infrastructure as text, but not software, and I think infrastructure software is an exciting next quantum leap in how we do infrastructure as code, which is to really bring those software engineering techniques to the way we manage infrastructure. That includes architecture so that we've got real patterns and best practices, we're not copy and pasting text all over the place, we actually have a real sharing and reuse package model. We can develop new infrastructure as productively we can develop applications. We can test that infrastructure using all of the tried-and-true techniques that we've learned over the many years of dealing with software, and we can secure the infrastructure using those tried-and-true techniques as well.

    **Adam Jacob**

    I think this idea of infrastructure as text to infrastructure software, it's so compelling. I've spent so much of my life doing infrastructure as code and doing infrastructure as text from the beginning of my systems administrator career, which I still kind of feel like a systems administrator, all the way till now, and this idea that it has to evolve from just text to software, a big piece of that is that right now you don't actually interact with your infrastructure as code systems at all once they're running, right? You write this code, then you run the software, then it reaches out and makes whatever changes it's going to make to the world at large, and then it's finished, right? And maybe you're running it in a loop so that you're doing drift detection and you can reconcile state, but ultimately they're not software that runs like an application runs in its own right. You can't interact with it interactically. You couldn't ask it what it's state is, because it doesn't really have one, because it's only real job is to let you describe what you desire and then make it so hopefully.

    And sure, it can check in every now and again, and [hensible 00:26:24] you can like decide to do something right now. But ultimately it's not really the same as when you think about when we write software. We don't think only about the code that went into writing the artifact. We think about how we interact with the artifact once it's running. We think about the API that we can interact with. We think about all the different pieces that went into that system. I think this is just a really powerful and important frame for thinking about how cloud engineering can be different than what we got with infrastructure as code and what we got with DevOps. There is a place we can go that I think is really exciting and unique and special that lives around this idea that the infrastructure itself is a programmable piece of the puzzle and that we need to treat it like one, not only in the development lifecycle, but also in the runtime lifecycle and across its entire life.

    **Joe Duffy**

    Yeah, and once you get into that frame of thinking a lot of things pop. So one is that the inner loop that we're used to, that this idea that you do all your application development within your editor and then magic happens and suddenly it's running in the cloud and it's not something you had to think about in your editor, that's just not the world we live in anymore. So one of the things, one of the critical pieces of the workflow that the cloud really did break in a sense, is the IDE experience. You think of, "How do I go from writing code to getting it running in production, or even a test environment in the cloud?", and oftentimes there're manual steps, you have to step out of your editor, you have to go maybe into the cloud console point-and-click. Maybe what you're testing locally isn't quite the same as what's going to run once you deploy it to the cloud, and you're often hopping around going into a terminal running some commands. The experience is very disconnected today, so the inner loop of how you work has become not so inner.

    **Adam Jacob**

    Absolutely. I'm so stoked about the idea that we can solve this problem. When you think about what's possible in software, I saw a really cool demo of some ORM code that was written in typescript that when you define the query you want to run, depending on the way you deploy it, it either runs through a lambda that then does a proxy back to the actual data store, or it talks directly to the data store that's running on your laptop and the developer doesn't have to know the difference, it just happens magically by the compiler at deploy time. And that sort of thing is so interesting, and when you think about those possibilities, however you think about it, somebody out there is like, "That's too much magic."

    But forget about the details for a second and just think about what could be possible when we think about, is an IDE as we understood it the right environment? Maybe we need different kinds of tools that run alongside the IDE. Maybe the way that we think about how the system is built could be fundamentally foundationally different than it is right now. But in order to get to that future you have to think holistically about what's possible. If you're focused in on how the world's been constructed so far, then it necessarily constrains you to thinking in terms of terminal windows and code editors as opposed to thinking about it in terms of workflow and collaboration, and how do we get those reusable patterns and practices? We know that there's a way to work together to create these infrastructures, because we're doing it all the time, but could we build better experiences that really take advantage of all of this capability to make that inner loop inner again? It's so cool.

    **Joe Duffy**

    Yes. I'm super excited. I have to laugh when you say, "Is it too magic, is it not?" It's funny, because IDE's really are magic.

    **Adam Jacob**

    Because they're complete magic. Type systems are complete magic, right? Everything about its magic.

    **Joe Duffy**

    Everything about an IDE is magic. I worked on debugging and edit and continue and refactoring support and setting breakpoints for Visual Studio many, many years ago, and if you knew how those things work, they're just crazy. They really are magic.

    **Adam Jacob**

    If you think about that, what's the equivalent of the Chrome Debugger for your cloud infrastructure? That's [infrastructure as software](/what-is/what-is-infrastructure-as-software/), right? That's infrastructure as software, because now we're talking about like, "Oh yeah, could I set a breakpoint that happens right before I launch the EC2 instance, or right after, that tells me whether the AMI was right or wrong?" There's so much potential there, but we haven't even begun to tap it.

    **Joe Duffy**

    Absolutely. If we're lucky somebody watching this will go build that, because we all need that.

    **Adam Jacob**

    Please do.

    **Joe Duffy**

    Related to that, testing is something we do see once you start applying software engineering techniques to your infrastructure. It unlocks a lot of that workflow. So despite everything we said about editors, at least you can edit your infrastructure as code in the editor and get refactoring and all these great go-to-definition things that we know and love, and you can also test. So that's one great thing that we have figured out how to do through some of the great work that Chef has done and some of the work that we've done with Terraform and Pulumi where you can actually test your infrastructure in addition to your application code. The nice thing about that is whether you're testing applications or testing infrastructure, there's a critical part of the software release lifecycle, and it really spans a lot of different possibilities.

    So when somebody comes and asks me, "Hey, how do I test my infrastructure?" The answer's actually quite difficult, because there's many different testing techniques. Some of those include unit testing. That's just for basic code correctness. "Did this function, do the right thing? Given a certain set of inputs, did it produce the right output?" There's integration testing for larger system integration. "Does the composition of all of those functions do the right thing?" But more interestingly these days, we're seeing, especially for cloud architectures, new workflows where people are actually doing ephemeral environment testing. And how that typically works is maybe in a pull request within your GitHub, workflow where you're collaborating with your team and doing code reviews, maybe part of the pre-merge validation is to spin-up an entire environment of your cloud application, run a battery of tests and make sure it works and then tear it back down.

    And treating infrastructure as software actually allows you to do this, and it's game changing. It really changes the way you think about confidently shipping all the time, new innovation, new features, out to your production environment. There's also advanced testing. I think one of the cool things I've seen is people doing chaos testing where they'll actually simulate an outage for an entire region to make sure that maybe the Kubernetes cluster failover works correctly, or even within a region and maybe a single availability zone goes out, and maybe there's some fuzz testing to randomize the environment to make sure that everything works properly. I think it's sort of a renaissance of testing for cloud architectures now that infrastructure can be treated like software.

    Security is also a key component of that, where security is part validation and making sure you're scanning and enforcing that you're not making mistakes unknowingly. Like for example, opening ports to the internet that you didn't mean to, or S3 buckets that are unprotected. But also the practice, the principle of least privilege I think is an important concept. It's always been an important concept, but I think now with the move to the cloud the security perimeter has changed for applications. It's no longer the four walls of the data center, which is a physical perimeter. It's a virtual perimeter of the virtual private cloud that you're deploying into and the firewall rules that protect and govern access to that, and the IAM roles and policies that you put in place. So the idea of principle of least privilege is an application, it doesn't get granted access to perform an action unless it's opt-in and granted that privilege. And that's a real key to being able to move fast with confidence in this cloud engineering world.

    **Adam Jacob**

    Yeah, for sure. And when you think about the cloud as a supercomputer and security not being an afterthought, we haven't really designed that least privileged stack all the way through the system, right? Like when you think about your operating system's security model, it has this whole model ranging from, how do you get into the UI, all the way down to encrypted drives and BIOS boot security. And that chain doesn't exist across this massive supercomputer that we've created. So we really do have to think about security not as an accidental side effect of what we've done, but it has to be this intentional design of what could be possible.

    **Joe Duffy**

    I love when you think of the operating system analogy it just becomes even more clear that security needs to be a fundamental part of how we develop this software. And I think the job isn't done after you've done all of this verification and testing and you think you're ready to ship. Really that's just the start of the game, that's just the beginning. Once it's out in production, now you need to monitor and react to what's going on. So this is really up to each team to figure out their own OODA loop, and what an OODA loop is, it's kind of a term used by the U.S. Air Force for combat operations.

    Basically the idea is observing your surroundings, orienting yourself to your surroundings, deciding based on what you're observing and then acting based on that. I think that's a really good analogy to how we observe our cloud applications in the real world, and how do we figure out when something's wrong, how do we react to the unknown unknowns. And to do that properly really means that you're logging everything. You often can't know in advance what the important bits of data are going to be. The old model of just having very simple performance counters of CPU utilization and memory for example, yes, maybe you need those, but that's seldom the sort of information we need to really detect anomalies and react to them in modern cloud architectures, especially given how distributed they are in their nature.

    **Adam Jacob**

    Exactly, and if you can't see it, you can't orient yourself to it, right? If I can't observe my situation, that orientation step where I try to figure out, "Well, what am I going to do?", given the inputs that I understand about what's happening, now I have to orient myself based on what I know about my mission, what I know about my surroundings, all of those things, so that I can make a good decision as quickly as possible about what the next action is. These loops are really tight, and I think the big change here is going to be about being able to collect all of that data into an observability system that gives you that capacity to orient yourself quickly and to make better decisions about what to do next when things go wrong.

    **Joe Duffy**

    I think the key thing is that all these things that we're talking about from a workflow perspective are all related. This is about, how do we go from idea to actually shipping software in production that our end users are going to benefit from? I think this is where continuous delivery comes in. Continuous delivery, this is not a new idea. We've been practicing this for application deliver for a while now. Continuous integration is sort of running the tests and running the acceptance testing before delivering. But really what we're seeing is moving from just application continuous delivery to also the infrastructure as well. As application development teams and infrastructure teams and the whole cloud engineering organization work closer together, really this is how teams ship early and often.

    This is how the whole team goes from shipping every quarter to shipping every month to shipping every week to daily, and many teams are trying to get to that nirvana of literally shipping features on every git commit. Many people are able to do that, and that's because they're practicing continuous delivery and incorporating all of these cloud engineering or infrastructure software practices into their daily habits. I think the exciting thing is that we're talking about applications and infrastructure, the developers and infrastructure engineers and DevOps teams working together on this. We're talking about all the validation. We talked about testing, security, before, during and after, speaking to the observability importance there. And I think increasingly we hear multi-cloud a lot. I think teams are really trying to centralize on cloud agnostic workflows that work for the team. The workflow is really for the team and has to empower the team to do their best work together and to be agile. So that's a key element also.

    **Adam Jacob**

    Absolutely. I think when you focus in on the idea that continuous delivery is the workflow that gets our software and infrastructure and all those things up into production, it's also one of the bellwethers that tells you that we have so much more to do in terms of thinking about the cloud as a supercomputer, because when I want to deliver software on my computer I don't like build a pipeline that then knows how to take my code from the editor to the running thing. Not like that I don't. And it's not that continuous delivery needs to go away, but the idea that what we're doing is continuously delivering the software, producing these artifacts and then running them on the supercomputer, that needs to become the paradigm by which we see continuous delivery, as opposed to this process of building pipelines or sort of the how. Instead it needs to be more about the what.

    **Joe Duffy**

    Talked about teams, and really workflow is about how the team works. So let's spend a minute just talking how cloud engineering teams work. Really the thing I like to say is, cloud engineering is about taking one plus one equal three. It's about taking application developers and infrastructure teams and DevOps teams and having them work together to do more than they could have otherwise on their own, and that speaks to the DevOps journey that we've been on and to the future, which is that cloud engineering teams are empowered. Everybody collaborates, contributing their own unique skills. Application developers focus on what they're great at. They're great at building applications and delivering functionality to end users. And increasingly now they're doing that with cloud capabilities. But really we want to empower developers to do what they're good at. Similarly, infrastructure teams and DevOps teams are great at engineering scalable reliable cost-effective foundations on top of which the entire organization runs.

    I like to say, application developers might not want to become experts in networking, or how to build scalable Kubernetes clusters that can scale across multiple regions. That's really in the infrastructure domain, and I think it's important that we recognize everybody brings passions and skills and things that they're good at to the table. And really cloud engineering's about empowering everybody to bring their best foot forward, and that includes security engineers also. Really, security's not an afterthought point. The way that we ensure that it's not an afterthought is by making sure the security engineering team is a core part of the cloud engineering team as well. So that's sort of the architectures, workflows and teams, kind of where we're at today. I think it'd be interesting just to spend a minute looking into the future. We've alluded to a number of the key things that still need to happen, but I think it's pretty clear we're on the horizon of a lot of great breakthroughs in cloud engineering.

    I think in fact, if I were to use a baseball analogy, we're still kind of in a third inning of the cloud, whether that's because folks are still moving from on-prem and hybrid into public cloud, people are still making the shift to ... There's a lot of facets in which we're still in the third inning. So a lot of excitement about the future of course, and it all starts with cloud engineering. I think these are all foundational pieces, and in a sense the future is really about just more of this. It's about really that operating system, the programming model, the application model, really coming to fruition. So I think, super optimistic about the future. The good news, we're well on our way and that cloud engineering is the foundation that's going to enable us all to get there. So I want to thank you for coming to talk today. I had a really exciting time telling this story. Thank you, Adam.

    **Adam Jacob**

    Oh, thank you. So nice of you to let me hang out.

    **Joe Duffy**

    Any time. Enjoy the summit. I hope you learned something today. I hope you learned something, a lot of things throughout the day, and we've got a lot of great talks here. And the talks are sort of organized to map back to the themes we talked about today here, architectures, workflows and teams. So have an exciting time. Thanks again for coming. Thanks again for joining us.
aliases:
  - /resources/the-future-of-cloud-engineering
---
