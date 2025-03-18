---
# Name of the webinar.
title: "PASTA and OCTIVE and STRIDE, Oh My!"
meta_desc: Learn how the Threat Modeling Manifesto serves as a guide to define or tailor a methodology that fits enhances software development rather than holding it up.

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
url_slug: "pasta-and-octive-and-stride-oh-my"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "PASTA and OCTIVE and STRIDE, Oh My!"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "PASTA and OCTIVE and STRIDE, Oh My!"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/nAtM4I3v5OA"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T13:40:00-07:00
    # Duration of the webinar.
    duration: "20 minutes"
    # Description of the webinar.
    description: |
        Threat modeling is an extremely valuable tool in the security software development pipeline. Some studies suggest it has greater impact on security posture than other more widely practiced security activities. There are many different frameworks, models, and methodologies that have been developed in an attempt to make threat modeling easier. However, these popular approaches to threat modeling are still too cumbersome, structured, or time consuming to fit into modern DevSecOps

        In 2020, a group of 15 security professional released the Threat Modeling Manifesto to formalize decades of combined experience into a declared vision of what threat modeling truly is and what makes it important. Learn from one of these authors about the values and principles of what threat modeling should be. Discover how this often-over-looked activity can actually make our CI/CD pipelines more efficient while improving overall security of software. Get practical examples of how the manifesto serves as a guide to define or tailor a methodology that fits enhances software development rather than holding it up.

    # The webinar presenters
    presenters:
        - name: Alyssa Miller
          role: Hacker, Security Advocate, and Cyber Security Executive

# This section contains the transcript for a video. It is optional.
transcript: |
    Hello, everyone. I hope you're really enjoying the Cloud Engineering Summit. We've got lots of great content we've already seen today and lots more coming your way. But right now we are talking about this thing we know as threat modeling. That probably sent a little bit of a shiver up your spine.

    It does when I talked to a lot of people. We think about these big heavyweight frameworks and long design cycles and things that are always a part of threat modeling and it really makes threat modeling this thing that just doesn't seem like it's gonna fit with our DevOps and our cloud native world. So I'm here to tell you that that's not the case. In fact, I wanna share with you how we can make threat modeling one of the enablers, one of the things that makes our pipelines move even faster. I know it sounds crazy, right? But stay with me.

    So if any of you travel like me you know this idea of layovers and what that can mean. Why am I talking about traveling? We'll get there in a minute. So when I travel, I constantly look at how long my layovers are gonna be. If I'm flying through Detroit, I know it's a huge terminal, I could end up landing on one end and have to be down a mile and a half on the other end in 40 minutes or less, that might not work so I usually look for longer layovers. Or in a case where I fly into Salt Lake City, airport I've never been to before.

    And so this happened to me recently and I made sure that I got an extra long layover just in case 'cause I really didn't know what that airport was like. Well, when we landed, this is where we landed. We were about a mile from the terminal and we had to take a bus into the terminal and then I had to go catch my other flight. If I hadn't had a longer layover, I'd have missed my connection. So this whole thought process, this idea of, hey, I wanna think about what's going on here and make plans, that lies at the heart of what threat modeling is.

    So let's dig in. Now, who am I first of all? My name's Alyssa Miller, I'm a hacker and a researcher first and foremost. I have been a hacker all my life, bought my first computer at 12, hacked into Prodigy and I've been doing it pretty much ever since. However, today I find myself as the Business Information Security Officer or BISO for S&P Global Ratings. Now, what is that? Well, I don't have any time to get into that right now, but you can check out this blog and it will share more information with you about what that is.

    I'm also an author and a blogger, gonna be releasing my first book. It's already available for pre-order, "Cyber Defenders' Career Guide" if you're interested check it out. Should be in print by the end of the year. And then finally I am a former software developer. I taught myself how to program when I bought that computer at 12.

    I worked in financial technologies as a programmer for a number of years. I come from the world of software development. So as I said before, when we think about threat modeling, we think about all of these different STRIDE and DREAD and OCTAVE and PASTA, all these different frameworks. And we think about all these complexities where we have to have a long design cycle, we have to map out an entire system and figure out where the threats are. But the problem with that is that's so 2008 thinking because in 2008, 2009, DevOps showed up on the scene.

    And suddenly it was a whole different world, right? We were looking at how do we make our development pipelines quicker, how do we get Devs and Ops working together and create this culture where we can deploy faster and faster and more dynamically. But the problem is threat modeling kind of gets left out in the cold. However, when I look at this 2019 state of DevOps report, one of the things they looked at were the common security practices, how often we do them versus the impact they have on security posture. And what you see in the upper left here are all the usual suspects, static code analysis, penetration testing and so forth. Those are the things we do a lot but they don't impact our security posture a whole lot.

    But down here in the lower right we see security and development teams collaborating on threat models as something that has a huge importance, but we don't do it very often. So I got to thinking, how do we bring threat modeling into this DevOps space? And I figured we got to get back to basics first of all. I'm gonna solve this problem. I got to just get back to the basics of what even is threat modeling. And why in the heck do we do threat modeling? So I set out to find an answer to that first question, just what is threat modeling? I wanna answer this.

    And so I did a Google search as we all would do. I went to OWASP first, Open Web Application Security Project. They seem to know everything about application security. They'll know what threat modeling is. But this was their definition and look at how complex this is.

    I mean, if I'm trying to get back to basics, a long difficult explanation like this is not gonna get me there. So okay, OWASP isn't gonna help me out, what about Wikipedia? Well, it didn't get much better, right? This is still not that simple back to basics approach that I was looking for. All right, well, Microsoft has the SDL and Adam Shostack wrote the book on threat modeling so many years ago when he worked at Microsoft so what does Microsoft have to say? Well, it's better, it's shorter. It's a little more to the point but it's still filled with a lot of security jargon and things that just really don't help. So I had to really just dig into this and try to figure it out and finally it hit me one day.

    When it comes right down to it, the core of what threat modeling is, is simply asking that question, what could possibly go wrong? Just like I mentioned before with that flight and planning out my layovers and things, threat modeling is something we all do every day. We do it in all phases of our life. It's just when we talk about software development and deploying into our cloud environments through our DevSecOps pipelines and our CI/CD pipelines and we want that to move faster and faster, when we apply it there, it's just we gotta think about it a little differently. But it's something we always do, it's something natural. So that's when I came up with this definition.

    Threat modeling is simply identifying the likely threats to a system to inform the design of security countermeasures. So shortly after I came up with this, I found out I wasn't the only one asking the question and wanting to get back to basics. In fact, there was a group of 13 other security professionals who wanted to do the same thing. And last year we formed a working group that created the threat modeling manifesto. And here you see the definition we came up with as part of that manifesto.

    You'll notice it mimics really closely to the definition I had. We were all kind of on the same page that threat modeling is really just looking at a system and figuring out what could possibly go wrong with that particular system. But why, why do we do threat modeling? So we went on in that working group and we defined the why. The output of threat modeling informs decisions, that sound familiar? That you might make in your subsequent design development testing and post deployment phases. But they don't need to be these big heavy design cycles.

    When I say design there, it doesn't mean, oh, we have this whole complete system design and we're gonna do DFD diagrams and everything else. No, we can do this much simpler. And that's what I wanna share with you today. So when we wrote the threat modeling manifesto, one thing we didn't do was defined yet another framework or methodology. The goal of the threat modeling manifesto was to lay out the values, the principles and patterns and anti-patterns for what makes for good threat modeling.

    So let's talk about how you build your methodology because at the end of the day we want a methodology that fits your organization. Now, a value in threat modeling is just something that has relative worth or importance. It's basically this is the core of what threat modeling is. It speaks to the heart of threat modeling. And so we defined six values and I'm gonna walk through those with you and help you understand what we saw as most important to threat modeling.

    So our first value. Threat modeling values a culture of finding and fixing design issues over checkbox compliance. Now, I think a lot of us will agree with that, right? Checkbox compliance is not something we wanna do. Instead, what we're looking for is a culture where we're actually finding and fixing things. There's a lot of things that it feels like we do in security or that security makes our developers do, that just feels like it's checkbox compliance, kind of like this image here.

    Okay, great, you've created this handicap space so you maybe you're compliant now with requirements, but yet you haven't fixed the issue. There is a major design flaw here that hasn't been addressed. This is what we need to avoid. And that's what threat modeling is there to help us with. It's to help us see where those design issues lie and make sure that as we're designing things, we don't end up with a situation like this.

    So that's our first value in threat modeling, moving away from just checking the boxes, hey, we did the thing, okay, we can move on, now we can promote our code or we can push this particular new deployment into our environment. But it's really making sure that we're making meaningful fixes because we found the flaws in our designs. And that's whether we had a big design or we were working in true CI/CD and we're just pulling things off the backlog and design is just something that happens in our heads. So our next value is the idea of people and collaboration over process, methodologies and tools. So you saw that little quadrant graph I put up there before, where it said that collaboration between security and Dev teams was what drove the value insecurity posture.

    So that's what we want from threat modeling. We want our Devs, our business people, our SREs, our Ops folks, our security people, all working together. Do your security people come to your Scrum teams, your daily standups, do they come to your sprint planning, are they there for the retrospectives? How much time do you all spend working together? Threat modeling is something that can enable that collaboration and it doesn't necessarily have to be face to face. When we think about threat modeling, we think about these big meetings where everybody gets together and they talk through the design of the system and yeah, that works but obviously as pipelines get faster and faster, we move towards CI/CD and we're deploying our cloud native technologies into things like functions or even containers. A lot of times that whole idea of is huge design review just falls apart.

    So we wanna look for other ways to focus on collaboration and get away from things like you be slave to something like PASTA and STRIDE or yo, having tools that we have to leverage for this. Let's focus on the people working together. Now, our third value is a journey of understanding over security or privacy snapshot. Threat modeling should be a journey. It's not something we do once we take a snapshot, we say, okay, we know what this is, these are our threats, we're all good to go.

    Threat modeling has to constantly be evolving. It needs to be something that we take a system and our threat model for that system is constantly growing and changing over time because we're constantly making changes to it. As we leverage our cloud native environments and we've got that CI/CD pipeline going, you all understand how this works. Our deployments are happening faster and faster and our threat models need to keep up with that. So again, once again, those big design cycle heavy duty threat modeling sessions just aren't gonna work for us anymore.

    Now, our fourth value, threat modeling values doing threat modeling over talking about it. Sitting around and talking about threat modeling is great, but it doesn't get us anywhere. There are so many organizations that sit down and try to figure out how they're gonna implement threat modeling but they never actually get around to doing it. It's that whole analysis or paralysis by analysis cliche you've heard before. We get to the door of the airplane but we never jump out.

    It's time to make that jump. When we talk about threat modeling the value is in doing it. We don't need it to be a perfect methodology the first time. We can evolve that methodology over time, but we need to get out and start doing it no matter how basic, no matter how simple we start off with that threat modeling, it's still better than not doing anything at all. So forget about being perfect, forget about talking about how we're gonna do it for months and months and months.

    Forget about trying to decide what frameworks and what outcomes we're gonna have and what artifacts we're gonna create but instead just jump out of the damn plane. Talk about threat modeling and do the threat model. Just talk about what could possibly go wrong and how we can design around that. That's where we need to start. Because ultimately threat modeling values continuous refinement over a single delivery.

    Think about it, how many times is threat modeling that thing that's just required as part of a development pipeline. We do it once and it's done. And we don't really think about it in terms of that journey that we talked about before. We wanna be continuously refining our threat model. We're not looking to solve all of the problems in our system today.

    We just want that system to get better over time, to continually improve it from a security posture perspective. The same way a sculptor is going to constantly continue working on that sculpture. Maybe I need to make a change to the highlight in this eye or, oh, I've noticed a little something imbalanced over here. And that artist is gonna come back over and over again and make those little tweaks. That's what we wanna be doing with the security of our applications and threat modeling is there to help us do it.

    So those are our five, I think I might've said six before, five values, excuse me. Now, let's talk about the principles of threat modeling. And these are just fundamental truths about what makes threat modeling threat modeling. So the first is that the best use of a threat modeling is to improve the security and privacy of a system through early and frequent analysis. So again, doing it in multiple iterations but doing it early.

    That whole idea we've talked about forever with push left. The second, is that threat modeling must align with an organization's development practices and follow design changes in iterations that are scoped to manageable portions of the system. Okay, so I like the sound of this. The third, is that the outcomes of threat modeling must be meaningful when they are a value to the stakeholders. In other words if what we create doesn't mean anything to the people who are gonna consume those artifacts, it's worthless.

    And then finally dialogue is the key. The documentation is just there to record the understandings and then to enable measurement of our threat modeling efforts. So how do we do this? How do we do this in DevSecOps? How do we bring security away from being a gate between the different phases and make it part of it? How do we push left? How do we get as early as we can? How do we do it in manageable steps? We make our threat model a part of the user story. How can you push any farther left than the user's story? But what does this look like? Well, consider your typical user story, right? The simple narrative that we often throw out there. As a some persona I want to do this thing so that I can accomplish this task.

    But what if we added another statement from that persona that says I want you to protect this from this threat. Now, all of a sudden we understand our critical assets and what we need to protect them from. So let's consider an example, as a car driver I want to enter a destination name so I can navigate without an address. But I want you to protect my search history from being accessed attackers. That seems like a pretty simple and obvious idea, right? So let's get that in the user story.

    So when we take that off the backlog, our Devs can address that quickly and easily. But it's not just the devs. They're gonna grab that and they're gonna take it from the backlog, they might work with an architect or maybe a security champion on what those security requirements look like. And then from those security requirements, they can figure out how to build security controls. But it doesn't end there.

    That information if we persist that, that now moves into our test cases. And we can now leverage that threat modeling information and the subsequent security controls designs to drive our test cases. But now that we've captured those in test cases, think about this, we can leverage that to build our monitoring. Now, we can do this in a lot of different ways but imagine for a minute if we took that information and we put it into something like YAML. Now, I know this is probably the sloppiest YAML you've ever seen.

    It is valid YAML but this is just there for an example, right? This is oversimplified but imagine for a moment you define the name of your asset. You describe what it is. Then you define the threats that it faces and specific counter measures that are being designed to address those threats. You can now leverage this YAML to build out your test cases in a semi-automated fashion. You can use this information to build the monitoring in your post-deployment environment.

    This is how we bring threat modeling into the context of DevSecOps and cloud native deployments. Using the same tools we do today, getting away from those heavyweight architectures and frameworks and things that we've used for threat modeling for years and getting back to the basics because as Albert Einstein said, the genius comes in making complex ideas simple, not making simple ideas complex. So unfortunately that's all the time I have but I thank you so much for joining me. Here's my social media information. I certainly invite you to continue the conversation.

    Thank all of you for being here. Thank you Pulumi for having me at the Cloud Engineering Summit. Thank you to my organization for allowing me to be here today. Thank all of you, I hope you enjoy the rest of the summit. And think about that threat modeling and how we can use that to get better in our cloud environments. Take care.
---
