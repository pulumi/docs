---
# Name of the webinar.
title: "Toxic Velocity: Speed Kills"
meta_desc: In this talk, we'll discuss the concepts of business pressures on organizations and individuals, the effects, and what "crashing" looks like.

cloud_engineering_summit:
    track: manage

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
url_slug: "toxic-velocity-speed-kills"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Toxic Velocity: Speed Kills"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Toxic Velocity: Speed Kills"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/irUai3eU8Gg"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T10:20:00-07:00
    # Duration of the webinar.
    duration: "15 minutes"
    # Description of the webinar.
    description: |
        In auto racing, the maximum amount of directional force available to a tire is visualized as a traction circle. When force is applied to a tire that is in excess of the size of the traction circle, you lose traction, and the vehicle will skid and, usually, crash. Similarly, there is a maximum amount of stress and pressure available to individuals with an org and within an org itself. When that stress and pressure is exceeded, the individuals and orgs can start to spiral and crash. In this talk, we will discuss the concepts of business pressures on organizations and individuals, the effects on those individuals and organizations, what "crashing" looks like, and some ways to manage the forces to get the best performance our of people and organizations without pushing them over their limits.

    # The webinar presenters
    presenters:
        - name: Tim Banks
          role: Principal Cloud Economist, Duckbill Group

# This section contains the transcript for a video. It is optional.
transcript: |
    This is Fernando Alonso's crash in the 2018 Belgian Grand Prix F1 race. You may be able to see how close Fernando Alonso's car is to Charles Leclerc's head. Fortunately, no one was seriously injured in this crash. The use of the halo, and the extension of the car's frame in front of and over the driver's head was credited with Leclerc still being here with us today. However, this crash did destroy a $14 million car and damaged several others.

    These are arguably the best drivers in the world, operating the most meticulously designed machines ever created. However, even these can be overwhelmed by physics and the results of split-second decisions made at extreme velocity. Every day, developers, engineers, product and project managers, engineering and company leadership are making decisions at speed. Business speed may not be the 200 plus miles per hour scene on an F1 track, but nevertheless, they're oftentimes making decisions that their business is moving too fast for them to adjust or react to properly. And they can crash.

    These crashes can often cost millions of dollars, as well as people's livelihoods, careers and mental or physical health. I'm Tim Banks. I'm an engineer, a former chef and international Brazilian Jiu-Jitsu champion and a former amateur auto racer and tireless petrol head, as like they say across the pond. I used to build cars, race cars, teach folks high-performance driving. And most importantly, wreck cars because of myself or others pushing our cars past their limits.

    Let's talk about the traction circle. This is a traction circle. This circle is used in racing schools to represent the amount of traction available to a car. And there's a fair amount of complex math used to determine the actual coefficient of traction, which is used to calculate the exact point at which a vehicle will break traction. But for instructional purposes in race schools, this is used so drivers can visualize the demands they're placing on their tires.

    Any combination of these forces added to a particular vector can cause traction to break. We've often felt this. If we've taken a turn too sharply and spun or skidded through a turn, doing a burnout or powerslide also demonstrates this. And while it can be fun to experience these in a controlled manner, most of the time when these happen, the results can be catastrophic, especially at high speed. Speed vastly reduces the amount of time that you have to react to a situation and make the right decision to avoid crashing.

    Speed also greatly increases the consequences of the wrong decision. More than anything else, speed makes it difficult to maintain control and safety. The thing that makes race car drivers so good, is their ability to control a car by feeling how far they can push a vehicle without losing control. And also being able to react properly when things go literally sideways. Much of this ability comes from a lot of track time and a lot of sometimes costly mistakes.

    So what forces do we encounter in engineering organizations and businesses that can cause us to break traction? What things are pushing us to go faster and faster, making our margin of error smaller and smaller? Let's look at a few. In short, money. This is why we're here after all, right? Making money is always gonna be a force in an engineering organization. Whether it's directly creating the product, directly supporting the product or supporting the larger business. Are you making enough money? Are you making money fast enough? How much money do you have left? Development velocity.

    This is often coupled with sales and growth and can often be the main driver behind crashing. When we aren't taking the time we need around making good decisions here, the results, which we will get to in a bit, will seem pretty familiar. One thing I do wanna point out here, is a decision to accrue technical debt. Many times the decision to create or continue to accumulate technical debt is a business decision, in order to preserve speed. We will make a decision that's expedient to a short-term goal, and then tell ourselves and others that we will fix or redo it later.

    See also to-do comments in code. The longer this debt goes unaddressed, the more likely it is to become, as we see at the Duckbill Group, load bearing. Load bearing technical debt is much harder and more expensive to pay off, because of the other systems and processes built on top of it. You've built something, now you have to keep it up. After all, your customers aren't paying for something that doesn't run.

    And unless you're Facebook, you can't just suck up hours and hours of downtime with no consequences. The resources necessary to keep the lights on and the 200s OK, will always pull on a business organization. As part of growth, recruiting and onboarding is expensive, both in raw dollars and in engineering cost. Phone screens, interview panels, onboarding and training, and working with folks until they get up to speed and your team must also be taken to account when you're determining the overall capacity for your organization. What are some signs that may indicate that your organization is going too fast? Whether you're making a character phase through a wall or causing a rocket to explode, trying to land it on a barge in the middle of the ocean, bugs are gonna happen.

    That's a given. But when bugs are becoming more commonplace and more apparent, it maybe an indication that you're not taking the time to put out quality code or that you're testing and QA cycles, aren't being given time to catch and remediate them. Bugs can be costly in money and reputation. And we all understand outages. They can take a business down in one fell swoop.

    Outages can have several causes and can be out of your direct control. However, if you're not taking the time to build resilience into your architecture, test your failovers, your runbooks and backups. Outages can be more widespread and last longer than they needed to. If you're not taking the time to sufficiently investigate outages and act on the findings of those investigations, outages can then be reoccurring. Look, we've all been in a rush and forgotten to lock the door, right? Same applies here.

    Building a secure application infrastructure takes time. Developing secure development and engineering practices also takes time. And frankly, sometimes it can seem like a pain in the ass, but even now we can still find open S3 buckets, default passwords on data stores, wide open ACL or unpatched software that is susceptible to known exploits, running in production. And those are just the basics. Your app is slow.

    You keep throwing errors. You're losing data. You're losing users. Putting features over stability can lead to these and other performance problems. And users are incredibly unforgiving when something they are relying on, is slow.

    How are your support interactions? What are your support NPS scores? What is your customer retention like? Are you having to issue credits or refunds? All of these can suffer or be indicators that your organization is not taking the time to fully resolve customer issues, train support personnel on products and new features or that your support metrics are prioritizing speed over quality. Good support and user experience is a leading factor in customer retention. If you can't retain customers, building a successful business is pretty difficult. How about us? What are some telltale signs that we as individuals are going too fast? There can be a lot of indications on this, but let's talk about a few. Now, this is a difficult topic for a lot of us, but it's important.

    I once worked with a sales person that was so focused on getting numbers for the quarter that he was working long hours, seven days a week. During a one-on-one, I asked him how his family was doing and he told me that his partner was pretty upset with him for ignoring his family, even to the point of working through a vacation that they all took together. I remember at one point when I was working at operations, that I had to take a SevOne call from the delivery room of one of my children. Look, everyone's family and relationship dynamics are different, certainly, but if they're starting to deteriorate and boundaries are being crossed, that's a red flag that you may be pushing too hard. Anxiety, depression, imposter syndrome, eating disorders, and other mental health problems are also an indicator that you may be pushing yourself too hard and too fast.

    We've all experienced these to some extent I believe, but we still must make sure that we are taking the time that we need for self-care and we're taking care of our mental health. Burnout. We've seen it, we've experienced it. Especially during the pandemic, as we're all spending time working from home and having a hard time stepping away from work, we're seeing more and more cases of burnout. Some folks are quitting and taking some, what they call, funemployment time.

    Some folks are just leaving the industry altogether. Burnout is preventable, but it's hard to stop when you're not taking the time to let your people recover. Crashing. What does crashing look like? It can be retention problems. It can be loss of business.

    It can be your business closing. For personal, for folks, for individuals crashing can be mental health breakdowns. It can be rage quitting. It can be relationship problems. It can be substance abuse problems.

    Whatever it is, crashing can be detrimental to business, it can be detrimental to individual's careers, it can be detrimental to their livelihoods and their personal relationships. Crashing is a situation that is avoidable, if we're making sure we're taking the time to relax, and we're also paying attention to our safety mechanisms. So what are some safety mechanisms that we can utilize to make sure that we're making good decisions and that we have the time to examine all the factors that go into making those decisions? First and foremost, slowing down. Having smaller sprints, having longer timelines, taking more time for testing and QA. Take the time for retrospectives and making the necessary changes to fix organizational issues that are brought up.

    Checking in. Check in with your team, check in with your leaders, check in with each other to see how we're doing. If you notice that someone is seeming down or seeming a little off or having a hard time, it may be time just to step in and make sure that they're taking care of themselves. These things may not seem like they're important, but over time, they will build up and they can cause us to crash. Time off.

    When we're factoring time to complete a project, complete a build, do a sprint, if we're factoring time for who's gonna be on call, make sure you're budgeting, so that your people can take time off. Do you know when the last time your folks have taken time off? If you don't, you may wanna check in, especially if you're one of those folks that have the unlimited PTO. Unlimited PTO is great, but if you're not taking it, it's pointless. Make sure you're not only budgeting that time for your folks to take the time off, but encouraging them to do so and lead by example. Finally, I wanna talk about humility.

    You may be a startup founder or a CEO or a hotshot engineering leader, but chances are, you're not the engineering leadership equivalent of an F1 driver. You need to accept your own fallibility and listen to others inside and outside your organization, regardless of their role, when they have criticism. All of you collectively, have more experience than any of you. This should be leveraged, not ignored. If you're a developer, operations, SRE, QA, or any other IC, acknowledge and accept that you don't know at all, take the time to relax and recover.

    It's better for you, it's better for your code. It's better for those that depend on you inside and outside of work. In the end, velocity can be toxic. It can cause us to crash. It can cause us to make bad decisions, which can make things worse.

    But if we take the time to slow down, we can make good decisions and we can recover. We can recover before we crash and we can recover as we start to crash. But once we've crashed, it's a little too late. Please everyone, take some time, check in with each other and make sure that you're not going too fast. Thank you.
---
