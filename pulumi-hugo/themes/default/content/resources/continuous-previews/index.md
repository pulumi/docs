---
# Name of the webinar.
title: "Continuous Previews"
meta_desc: Attendees will leave this session ready to take control of their development process in ways they may not have known were possible.

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
url_slug: "continuous-previews"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Continuous Previews"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Continuous Previews"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/n2T_6RqCxMQ"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T15:00:00-07:00
    # Duration of the webinar.
    duration: "17 minutes"
    # Description of the webinar.
    description: |
        Continuous Integration and Continous Deployments have been part of our application lifecycle for some time now but what about Continuous Previews? The ability to easily share new features and changes to a wide audience within your organization is a game changer for accelerating the delivery of features your users need. In this talk we will walk you through everything you need to know to deploy a Continuous Previews pipeline. Starting with containerizing your application, deploying to a cluster and connecting the results back to a GitHub Pull Request. Attendees will leave this session ready to take control of their development process in ways they may not have known were possible.

    # The webinar presenters
    presenters:
        - name: Peter McKee
          role: Head of Developer Relations, Docker
        - name: Josh Thurman
          role: Developer Relations at Uffizzi

# This section contains the transcript for a video. It is optional.
transcript: |
    Hello everybody, my name is Peter McKee.  I'm the head of developer relations at Docker, and today, Josh and I are gonna talk about how continuous previews is a game changer for accelerating and delivering new features and development to your end users.  So, I'm gonna hand it over to Josh, he's gonna walk through some concepts of continuous previews and then we'll quickly jump back and I'll go through a quick demo and then we'll wrap things up.  All right Josh, over to you. Yeah, thanks Peter.

    I'm Josh Thurman, head of developer relations for Uffizzi.  I'm gonna jump right into explaining the why, what and how of the continuous previews methodology.  Share my screen here.  Okay, so, let's start with why.  So, why CP? So, what? So, teams that follow a CP method will be able to begin testing earlier in the development process.

    So, with CP, you're effectively removing any gaps between the developer writing the code, and the approver who's testing the feature that they're working on.  Second, teams that use this will accelerate their iterative feedback loops which means they will be able to speed up how quickly an issue can be reviewed, feedback provided and adjustments made.  And third, teams that adopt the CP method will simplify their overall testing process.  The CP features can easily be tested independently and feature testing can be separated from integration testing.  So, I wanna frame this a little bit in the overall software production process.

    So, every team that develops software has four hurdles they've gotta overcome.  One, the development of new code, two, the integration of that new code with existing code, three, acceptance testing and four, delivery to end users.  So, I would venture to say that everyone tuning in can easily think of numerous tools and processes that support development, integration, and delivery.  But what about tools and processes that improve how software is accepted and tested? We're all just probably scratching our heads on that.  So, this is where CP comes in.

    CP is a method that fundamentally improves how your team collaboratively tests new software.  So, let's talk about the foundation of the continuous preview process.  There's eight principles behind it.  One, continuous collaboration, two, empower Devs with production-like test environments, three, tight integration between your ticketing, repositories, and infrastructure.  No additional burdens placed on the Dev Team, limit context switching, we all know that's costly.

    Confirming functionality prior to integration, reliance on automation and support for full stack.  So, front end, back end, microservices, APIs, anything else you can think of.  So, how does CP fit within Agile? So, if Agile is the overall umbrella that drives how we build software CP is a method or a best practice that is nested within agile.  So, the big loop here represents a typical agile workflow.  New requirement is designed and ticketed, developer picks that up and begins their work.

    When they're finished, that branch is merged, it goes through an integration step and then your acceptance testing begins.  So, the problem with this model is there's too much of a gap between the individual developer writing new code and the person approving that feature.  So, CP is an add-on method to the overall agile workflow, it enables feedback loops to beginning earlier and happen faster.  So, you see the little continuous preview piece that happens in the development section there.  So, it's a tighter loop and it's a loop between, again the developer writing the code and the person approving it.

    So, next I'll talk about a little compare and contrast.  What does a non-CP process look like versus a CP process? I'm just gonna be descriptive here.  So, in a non-CP, testing does not begin until post-integration.  You have a delayed feedback loop between the person writing the code and the approver.  Feature and integration testing are done in batches, so they're all coupled together.

    You have persistent QA/test environments.  There's more context switching and you're at a higher risk of bricking or bricking at your QA environments.  So, in a CP workflow, testing begins pre-integration.  You have a continuous feedback loop between the person writing the code and the approver.  Feature and integration testing are decoupled.

    So, you have a separation of concerns.  And you have, instead of persistent environments, you have on-demand test environments that have a purpose-driven life cycle, and you have as many as you need.  You also have limited context switching and you've got a lower risk of bricking or bricking your QA.  Let's talk about CP and branching.  So, I'm showing a GitHub flow here.

    And so in this case, a developer has checked out a topic branch, and when you're following the CP method, it can easily be deployed to an on-demand environment that has a purpose-driven lifecycle.  This again enables the developer and approver to quickly iterate through feedback loops until the feature is approved.  So, in this case, the developer has checked out a topic branch, begun work, and because it's being continuously previewed, an approver is reviewing the work in progress and providing feedback.  So, in this scenario, we see two thumbs downs, there's two feedback iterations that did not pass.  On the third iteration, they accepted the feature and it was approved.

    So, now the feature can be merged.  So, we've been able to test and accept the feature in isolation.  And later, if and when we were tracing root cause issues in a post-merge review, we can have confidence that any issues are most likely related to integration and are not functionality issues.  So, that reduces our time spent debugging.  So, let's look at the CP loop.

    And, I previously mentioned one of the principles, which is tight integration between ticketing, repository, and infrastructure, and that is displayed here.  So, issue starts as a ticket, and then developer begins working on it again, in a Git Workflow.  So, CP is the automation step that occurs.  So, from a Git Workflow, you should be able to kick off a preview deployment without breaking context.  That deployment is then gonna go to your infrastructure and then to close the loop, once you have a preview URL, that shows back up in your ticketing system.

    And so that signals to the, whoever's QA-ing or approving this feature, that it is ready to be reviewed.  And of course the process continues through as many loops as required until the new feature is approved.  So, in summary, on the process, continuous previews make it easy to collaboratively review and test in-progress feature development for full-stack applications.  So, our acceptance testing can happen earlier in the development process, we can accelerate our iterative feedback loops, and overall testing process has been simplified.  We can feature test in isolation.

    We can also separate feature testing from integration testing.  And so all of this results in improvements against our key performance indicators.  Some common ones are lead time, cycle time, team velocity, and code stability.  And of course, that all leads to happy end users.  So, enough about concept, let's get going with seeing a technical implementation of this.

    So, I'm gonna pass it back to Peter, who's gonna share what he's got. All right, thanks Josh.  So, let me go ahead and share my screen and let's take a look at little demo application that I have.  So, first, I have a small, little continuous preview server that I wrote and it's running on a remote machine.  And now I have a little application I have running locally.

    You could see it here on port 3000.  It's just a small crud app.  And I'm gonna go ahead and make a change.  We've got a ticket that came into our queue.  I'm a developer on a team, so they wanna get rid of these continuous previews in the title.

    So, we're just gonna call it Widgets Application.  Let me save that and then I'm gonna come over to my command line.  I'm gonna stop this from running inside of containers and then I'm gonna restart it.  So, I'm doing docker-compose up and I'm giving it a dash dash build, so it'll rebuild my containers.  And this should run relatively quickly and then start everything up with the changes.

    Give this a second to run.  I'm running this in local on my machine.  And I wanted to run it in composed so I can do my dependent services and my application at once.  Okay, so, now it's up and running, let's jump over here to the web, give it a quick F5 refresh, and there we go.  We have the title's been updated, looks good to me.

    Let's go back on our command line, and I'm gonna do a Git Commit and I'm gonna say update the title, and then I'm gonna do a Git Push.  So, that's gonna run.  And typically, you would have your continuous preview server connected into your GitHub, or Bitbucket, or whatever that is and whenever you cut a PR or do a push, that can send a webhook into your server.  So, I'm gonna simulate a webhook here.  I just have a little bar script that makes a call out to the web, into the continuous preview server.

    And here it is running here, we get back, everything's been built, everything's fine and it's done working.  So, that is updated.  So, now we're gonna come over here and you can see I'm running on my CP server.  Let's give that a refresh, and now I have Widgets Application.  I can give this URL out to anybody on my team in the business, peers, business analysts, and you know, product owners.

    They can come take a look at the application, go, "Yep, that looks great. " Or they might say, "You know what? No, change that back, we don't care. " So, let's pretend that that happened.  So, let me run in back into my application.  Just gonna do an undo, put the title back.

    I'm gonna save that and then I'm gonna do another commit and I'm gonna say revert title.  And I'm gonna do a commit, and a push, that's been pushed, and I'm gonna update, send a message into my continuous preview server.  There we go, everything's been updated.  If I come back into my continuous preview server and hit refresh, there we go, it's been updated.  Now this URL again can be passed around to all your teammates, they can take a look at it, and then you can continue on with the process once it gets signed off.

    All right Josh, let me kick it back over to you. Yeah, great, Peter.  Thank you for sharing that.  So, let me share my screen again.  And I'm gonna show a continuous preview with Uffizzi. So, first let's look at the app that I'm gonna employ.  So this is a six-container microservices application.  And I'm gonna work on a couple of these components.  So, I've got three off-the-shelf Docker official images here Nginx, Reddis and of course, a Postgres container.  And then I've got three custom elements that I'm working on.

    So, I've got the voting app, the results app component and the work component.  And so, I'm gonna work on a couple of those.  And let me go following the CP loop, let's start with ticketing on a new feature that has been designed.  So, here's my ticket, I'm gonna need to change the voting function.  I'm gonna double the dog.

    So, every time every vote for a dog gets doubled.  So, I've been working on that and let me show you, I already have this branch, I've already committed to it and what I'm gonna do, now that this is ready to be reviewed or previewed by the approver, I'm gonna open my pull request, create and create.  Okay, so, that pull request has been opened.  Now, bear with me, I'm gonna do one more pull request, and then we'll see why I'm doing that.  So, this was for the example voting worker component.

    Let's say also that I was working on the results component and I was working on a change color branch.  Okay, so, again, to save time for the demo, I've already committed my changes and I'm gonna open a pull request here.  Create and create.  The importance of the pull request is I'm the developer working in my Git Workflow and without doing anything extra, I actually kicked off a preview deployment for each of those branches that I've been working on.  And so I can go to Uffizzi here and watch, when I did that pull request, both of these deployments kicked off.

    So, again, this first one is gonna preview the double dog's change that I made and the second one is gonna preview the color change that I made.  So, once those go live, I will have a preview URL and to finish the CP loop, and I already had this one running just to save time on the bill process here, but I'm gonna finish the loop by going back into my ticketing system, in this case, I've got JIRA.  And so this was the ticket I started with.  And Uffizzi went in here and placed this preview URL right here.  So, whoever is approving this knows that it's available there, they can go take a look at it.

    If they need to make any comments, they can say, "No, not quite right. " Of course, that's gonna go to the developer working on it and they're gonna go back through the loop and try to make the changes until the approver has indicated that it does meet the requirements.  And let me show you this in a little bit more detail.  So, what we've done on the backside is deployed six containers all to Kubernetes.  And this works with any cluster.

    This happens to be an EKS cluster, but you can run it on Azure, on GKE, you can also do it on prem, but I have all these containers running.  If I need to, if I have any issues, I can go in and actually, I can look at the logs and these are filterable.  So, I can see my build process was done and I can see the container's up 'cause I can see the logs are running here.  And so now, this one's up and then it'll take maybe another 30 seconds or so, and I'll be able to review those changes here.  So, that's it.

    That is a continuous preview in action leveraging Uffizzi's automation.  And Peter, don't know if you have any final comments, but I appreciate everyone tuning in and yeah, please come check out continuous previews.  I wanted to reference, a lot of my talk was from the CP manifesto.  You can go view that at cpmanifesto.org to learn more about this process.

    It's open source, so, you can also check out the repo and then go, and we'd love to have feedback there and more collaboration.  So, please check it out. Yeah, great.  Thanks Josh.  Yeah, the only thing I will say is make sure we get out the manifesto. I think it's really important.  Yeah, like you said, give some feedback and we'd love to hear people's thoughts about it.  Thanks everybody, really appreciate it.
---
