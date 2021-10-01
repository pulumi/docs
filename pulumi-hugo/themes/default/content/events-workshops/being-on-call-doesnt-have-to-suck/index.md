---
# Name of the webinar.
title: "Being On-Call Doesn't Have to Suck!"
meta_desc: "In this session we will explore how we got to this point and how we can adopt Chaos Engineering to help us wake up less and sleep better."

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
url_slug: "being-on-call-doesnt-have-to-suck"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Being On-Call Doesn't Have to Suck!"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Being On-Call Doesn't Have to Suck!"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/fFDo_o3XM0k"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-10-08T10:00:00-07:00
    # Duration of the webinar.
    duration: "17 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Companies rely on key services to be available nearly 100 percent of the time in order to make revenue. A consequence of this situation is that it has become natural for Engineers to get woken up late at night or early in the morning to resolve incidents. But whether you rise to the occasion or not, it eventually becomes a very taxing experience. Unfortunately our industry has accepted this as the norm. There is a better way. Chaos Engineering. In this session we will explore how we got to this point and how we can adopt Chaos Engineering to help us wake up less and sleep better.

    # The webinar presenters
    presenters:
        - name: Jacob Plicque
          role: Sr. Solutions Architect, Gremlin

# This section contains the transcript for a video. It is optional.
transcript: |
    I loved being on call. The fact that a company, much less a multi-billion dollar company, relied on me to save the day felt incredible. Is this how it feels to be Spider-Man maybe? Of course! In the context of getting woken up at 4am to save the day. Hundreds of instances resolved by little old me. I remember the day that things changed. Cyber Monday was the best year-over-year best day in company history leading into a particularly memorable one on November 27, 2017. We scaled up our instances in advance, pre-warmed our load balancers, even went through this large launch readiness checklist.

    We felt ready and personally, I was super excited. Then later in the afternoon we started seeing some nxdomain errors which even started looking at our D-N-S cluster and couldn't find anything. Everything looked healthy. Then the panic started to kind of set in a little bit. Felt like the walls began to close in. I remember specifically that the person talking to me on the call was our V-P of Infrastructure as well as our C-T-O asking me what was going on through all the kind of white noise. I had no idea what was going on and every minute thousands of dollars were going down the drain. Of course, this is also the same week as A-W-S re:Invent.

    So people are popping in from Las Vegas, the Venetian in the background, to try to jump in escalate and figure out what was going on. We eventually looked at our console cluster for service discovery and saw that are EV--S volumes couldn't handle the— the I-O load. So it essentially fell over. We didn't realize later on that our E-V-S volumes that we load test— that we load tested in our staging environments were actually a different size than they were in production. Which completely invalidates the test. Of course this came from post-mortem several days and unfortunately a few million dollars later.

    On call can suck, but it doesn't have to. So good evening. My name is Jacob Plicque or if it's morning or afternoon. Good morning and afternoon as well. I'm a Senior Solutions Architect at Gremlin. I helpeour customers across a variety of different industries including, finance, commerce, airlines, retail, and insurance. Help build out their chaos engineering practice, In case you didn't know, Gremlin is a hosted SaaS platform that lets you run chaos engineering experiments simply, safely, and securely.

    Actually been at Gremlin for just over two years and previously worked at a large sports e-commerce company that I alluded to called Fanatics where I served as both a cloud operations and senior site reliability engineer for about a little over four years. So there I was responsible for providing a reliable e-commerce experience to process upwards of over 1,100 orders a minute, all while training junior S-R-E’s. So reliability has been sort of the bread and butter for a long time, especially on days such as Cyber Monday and Black Friday.

    So this on-call situation, how did we get here? So especially if we zoom in to right now in our current living situation, this recent move to working from home, shopping purely online has put a lot of strain on different companies across every industry. Many of them not being prepared for this level of demand during this pandemic. But if we actually zoom all the way out of it, we can actually see that this has been a problem for years in our crazy, rapid, Innovation digital world.

    We see things on Twitter of companies running issues, #HugOps and whether that's regular e-commerce failures on Black Friday, breakdowns at banks and financial institutions, and in some cases life-threatening incidents on airlines, the cost of these major technological breakdowns goes far beyond just the billions lost in company revenue. But of course more transactions at a business are performed online than ever. We have our network speeds that are constantly increasing and users that are getting more and more demanding.

    So we're looking for new ways constantly to satisfy that demand quickly and cost-effectively. This may mean breaking up monolithic systems for performance reasons, of distributed systems for ease of management, and the promise of reduced infrastructure costs, as well as the need for tracking all of these services wherever they are. So, but frankly with more complexity, comes more risk that things will break. So in order to keep up with the speed of innovation, we've adopted new technologies and approaches. So your team or your company's journey is likely somewhere on this slide, but of course this added complexity comes at a cost.

    So, of course, we're increasing this rate of change, which then increases the complexity of our systems, which increases the numbers of— the numbers of— of failures unless we're investing in both velocity and reliability. This is what allows us to shift the curve to achieve both reliability at the speed that we want to. However, as this trend continues, we start to think about the definition of operational maturity. So the majority of the industry considers being operational mature from this perspective as being ready to fight incidents. So this is a major component in the maturity of a compnay by I’d argue it's only half the picture.

    Actually I like to think about operational maturity as being proactive. So we can interpret this as architecting for failure in development, and then testing our assumptions about our systems early and often. But of course, we have dependencies on networks that we don't own, infrastructure that we don't control, orchestrators that are black— black boxes, open-source or legacy dependencies and the people operating the systems testing the code of, or just the code I should say, isn't enough. So we need a new way to test the other parts of the application stack so we make sure that we configured everything right and that all of our processes are in place. So so far, we're just looking at a small piece of this proverbial iceberg.

    And on top of that, to make matters even more fun, we’re responsible for the reliability of systems that we just don't understand. So how do we efficiently test and operate these new complex and distributed systems? Well, that's where chaos engineering comes in. So what is it and how does it fit? So if you remember nothing else from this particular presentation, remember these these four words. Thoughtful and plan. The term chaos is actually more of a misnomer. I've heard it more referred to as like a marketing jargon, but the truth is— is we're trying to validate or disprove a hypothesis. And then as we reveal weakness, the ultimate goal of chaos engineering is to shine a light on latent issues that are already exist.

    One of my favorite analogies I've heard is around the fact that if you take a flashlight or— or you know, your phone, in the case 2020, and shine a light into a basement, or, you know, if you're in Florida like me and don't have a basemen,t maybe more of an attic, you have all these like spiders and stuff. And in this particular area if you turn off the— the flashlight, it doesn't mean that the spiders are suddenly gone, right? So there's a concept called the blast radius. We always recommend starting small and carefully and purposely increasing the blast radius. So this typically means experimenting with a single or a few host, not your entire fleet, but this also can mean starting in your development environments and expanding outward.

    Speaking of extending outward. So this typically starts over as you escalate up your environments. So you can adopt the practice in your development phase so that your engineers are thinking about and validating that they’ve architected for failure early, and then what you can— once you’re confident with a particular failure mode, you could begin testing that and staging on a subset of your— of your environment and then expand from there. And then you simply rinse and repeat on your way to production. But what's great is chaos engingeering brings two crucial benefits. So first we can proactively identify and fix bugs that can produce an outage rather than waiting for system failure to show us where the weakness is. Secondly by running proactive gamedays our engineers grow more familiar with systems behavior and makes them more effective during an incident.

    Not to mention, this also helps us too in our monitoring and detection systems so that we can detect issues earlier. Now a quick note on fire drills. So I think in my younger grade school years I have to admit I took fire drills for granted. I thought they were a colossal waste of time. But now that you know, I'm an adult, and we can actually use fire drills to train for incidents, it makes a lot more sense to me now. So we actually are able to use these fire drills to train ourselves to stay calm and know exactly what to do. So many of us, if you think back, you’ve probably been placed on call for the first time given an on-call phone or pager and have been pointed out the run-books that are covered in cobwebs. They haven't been updated in a long time and essentially been told good luck. That's pretty common, unfortunately. Including myself.

    I've been responsible for systems that I didn't have a runbook or even in architecture diagram on, but liability and incident management fell to me. So we can actually make on-call less painful by running these fire drill scenarios as part of either onboarding a new engineer, as well as ongoing training exercises. Then even when run-books and solutions do exist, they're a great way to make sure that they make sense. For example, I once ran through an exercise where everything was going perfectly, alert striggered to the right people, they responded promptly, no issues logging in and getting into things and getting things working. But when we got to the actual run-book itself, to fix the issue, the run-book simply just said, wait for 15 minutes.

    Not great. So there's actually plenty of places where folks tend to get started. Whether you're moving to the cloud, migrating to microservices, adopting kubernetes, or actually figuring out your monitoring gaps. A pretty common example here is, if you're evaluating a new monitoring tool and you're trying to figure out how to decide between one or another, you can actually do chaos engineering experiments and see what responds first. So to dive in a little bit deeper, so there's a few experiments in which are really common for folks to get started, around verifying monitoring just to avoid those missed alerts and prolonged outages because of the fact that there was an issue that wasn't responded to.

    A pretty common one is around slow response from your application to your database. So that's a really great way to get started. As well as, and we’ll get into auto-scaling here in a second, which I'll admit the very first time that I knew that I fell in love with cloud was when I found out that auto-scaling was even a thing. So it was really cool. Then as we start thinking about incidence response, this becomes a kind of the level two. So you wanna start thinking about, perhaps you had an incident and a pain— a particular pain point you wanted to re-implement and see either as part of a post-mortem or much later just to verify that you've— that you and your team have— have gotten better. This is a great way to get started.

    I actually remember a story about a cloud architect that I worked with and we we're talking about this large, confluent stock which had all the different dependencies that we had as well as all of these different failure modes. And at the time, I was kind of the low man on the totem pole from a cloud operations team perspective and I asked when are we going to test these. They— this is a long list. We should probably get started on it, but we didn't have time and so it just kind of stood there. But also we didn't even know the chaos engineer existed back then so we actually have a really easy way to to get started now.

    And then from a cloud architecture perspective specifically, we can actually make sure that our auto-scaling is tuned. Our teams are prepared and able to handle those degraded or lost networks. As well as we can actually invest in doing region evacuation and make sure that that doesn't knock us offline. What's really great is that A-W-S Azure, and Google Cloud all have design principles used internally for their own systems that they publish for other companies to leverage. So these actual design principles include chaos engineering practices such as running gamedays to test out your workloads and train your teams.

    So that way you can simulate failures in an automated fashion. Just like that. So what can you do if you're on call this Spring? Run some experiments in your lower environments, of course, making sure that you're communicating this, but have a bit of a chaos hour during that sprint. Worst-case scenario is you validate an assumption that you had about your system that you're responsible for, and you learn something. The best case that you might find some surprises that they happen upstream in production, you'd be running that incident. So that's where you get started.

    But where are we headed? What's next? So there's no need for us to wait until something bad happens and then post-mortem. So let's start small in our dev environment with a hypothesis. Slow down or black hole that dependency and learn more about our systems. So also we can stop reading those post-mortems and start sharing these pain points with each other. Imagine if there's a world where we are all talking to each other about what we've learned about our systems. Then we can understand the need for our on-call by sharing these stories and doing chaos engineering to help it make— help us make it not suck.

    We've got to get better at telling these stories to each other. Frankly, it's why we're all here to learn and to get better. So chaos engineering actually creates this really interesting forced function that causes us to ask these questions about our systems and just as if not more important to our people. So a few links before you go. So right now while you’re watching this there is the largest, you know, no big deal, the largest chaos engineering event happening right now at Chaosconf dot I-O. And by the time you're watching this it’s almost over, but you can sign up and make sure that you get all the recordings from those from those talks.

    So those are— that's awesome way for you to really kind of jump-start your chaos engineering new journey. Secondly, everyone asks about swag stickers. We have some really, really awesome ones. So if you go to Gremlin dot com slash talk slash duval just as a short thank you for joining me on this this crazy journey. You can absolutely grab some of those stickers. They're— they're pretty, they're pretty cool. Main point Gremlin dot com slash community, thos conversations that I mentioned are already happening in our community Slack.

    There's some more, over 5,000 different engineers with a bunch of different places in which to get started. This also will link you to several tutorials as well. Test on being an on-call hero a little bit. My compatriot Vince wrote an awesome blog about not being an all-call hero— or not being just an on-call hero. So check that out. And lastly. There's something I actually just wrapped up yesterday, the first half of two webinars about planning and architecting for reliability. So right now you can actually watch the recording of part on and part two will go live on October 22nd. So just in a few weeks.

    So amazing amazing time I had putting this together. Thank you for listening. I hope it was helpful. Tweet at me. Add me on LinkedIn. Email me. Slack me. I’ll actually be available right after this for a bit of Q&A. Always happy to chat. And as one of the best teachers, Miss Frizzle of The Magic School Bus once said, take chances, make mistakes, and get messy. Just not in prod, just yet. Thanks again.
aliases:
  - /resources/being-on-call-doesnt-have-to-suck
---
