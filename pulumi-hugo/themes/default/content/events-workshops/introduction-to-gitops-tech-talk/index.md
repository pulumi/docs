---
# Name of the webinar.
title: "Introduction to GitOps Tech Talk"
meta_desc: "In this lightning talk, you'll learn how to take DevOps best practices used for application development and apply them to infrastructure automation."

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
url_slug: "introduction-to-gitops-tech-talk"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Introduction to GitOps Tech Talk"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Introduction to GitOps Tech Talk"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/Tqy8ZMxy57s"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-10-08T10:00:00-07:00
    # Duration of the webinar.
    duration: "14 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        In this lightning talk, you'll learn how to take DevOps best practices used for application development such as version control, collaboration, compliance, and CI/CD, and apply them to infrastructure automation.

    # The webinar presenters
    presenters:
        - name: William Chia
          role: Sr. Product Marketing Manager, GitLab

# This section contains the transcript for a video. It is optional.
transcript: |
    Hello, my name is William Chia. I serve on the Product Marketing Team at GitLab. In the next 15 minutes I'm going to show you how to manage E-K-S kubernetes clusters on A-W-S with GitLab and Pulumi using GitOps principles for collaboration and compliance. At the end, I'll walk you through all of the code that I'm using to make it all happen so that you can try it out yourself. To get started let me go ahead and share my screen. This is an introduction to GitOps and I'm happy to be here at the Cloud Engineering Summit.

    As I mentioned, my name is William. You can find me on Twitter, LinkedIn and I would love to connect with you all. And as I mentioned all of the code and links, I'll be showing today, are in this GitLab repository. GitLab dot come slash William Chia slash A-W-S dash P-Y dash E-K-S. I’ve mirrored all the code here so you can check it out yourselves. And if there's anything interesting or you have any questions, please do go ahead and tweet it out. You can tweet me at @TheWilliamChia. Use the hashtag #Cloud EngineeringSummit or hashtag #GitOps.

    So I wonder how many of you have ever run into this scenario. Might be a little familiar. You are logged into the A-W-S console and you need to do some type of infrastructure management, but it's not exactly designed for collaboration. For example, here I have an E-K-S node group that's part of a kubernetes cluster and I can see that it's got a four node maximum with three node desire state. And I've heard from my dev team that this is— this is kind of a bit large. Really this should be smaller or really I only need two nodes. This is a small service doesn't get a lot of traffic.

    So can you please go and update the node size? So we're not using as many resources. Well, one way to do it is I can just click around in a GUI and edit and make the changes and go ahead and save those, but the problem is, who knows about it. How did I know I made the right changes? What kind of review did it go through? Where's the record of the actions taken? And is that record in context of all of my other infrastructure changes? You can see— and for that matter if somebody else wants to do the same thing again, you have the same problem arise, or the same situation arise, and you want to modify the infra to match that, where's the record of that? How do I understand any of those things?

    I don't get any of that if I just go in and click around. So instead what I want to do is, I want to use GitOps, I want to use infrastructure as code using Pulumi to manage this. So let me show you what that looks like. Here I have a repo and I've taken this repo as a sample from Pulumi’s examples. They're all here in this GitHub repo. I happen to use the Python E-K-S one, but if you look at this example, you can find almost any cloud and any language, there's a lot to start with there. Additionally, I've set it up for GitLab’s C-I-C-D and that instruction is here. I'll walk you through this code at the end.

    And I've even set up something that's new, this Pulumi-Gitlab integration. And with this webhook, you get some cool interaction that I’ll show a bit later on in the demo. So let me show you a GitOps workflow to go ahead and update that cluster. The first thing is, let's say someone on our dev team is going to log a new issue in GitLab and they're going to say reduce the node size, using too much power, need less power. Usually we need more power. But in this case we need less power. We want to slim it down.

    So what's nice about this is now we can collaborate on this project. I can leave comments and this sort of thing. And let's say in this case this is a comment bot, but let's just imagine it's someone on the dev team or perhaps a— an engineering manager and they're going to assign the task to me to go pick it up. Maybe send me a note with a tag so that I get a notification. Can you pick this one up? And then if we look at the view from my own GitLab, I can see I probably got a to-do here. And I can see hey, can you pick this one up? So I'll go ahead and take a look at that and I can say @cbot2000, yeah, no prob.

    So I'm— I'm picking this one up and the first thing I want to do is from this issue, I want to create a merge request and what that's going to do is create a new branch for me, so that I can start working on this request and it's going to start a merge request to merge that branch back into master and it's going to tie this to the issue so that when this gets merged it's going to go ahead and close this. Last thing it's going to do is going to mark it as a draft, so people know I'm still working on this and they don't don't merge it automatically.

    All of this is set up really nice and automatically with that one button. So the next thing is, I might check out the branch and work on it locally, but I'm going to go ahead and open this up in my web I-D-E. Here I have my all of my YAML and code set up. I'll walk through this in a little bit when you can see how it works and then I'll show you what it's doing. But in this case, I'm using this Pulumi Python to set the size with infrastructure as code rather than a manual click. So for example, let's set this down to a node size of two, and I'm going to say reduce nodes to two. And go ahead and commit that.

    This isn't the GitLab— GitLab web I-D-E, but you could, like I said, you could do this locally as well. So now I can see that a few things have happened since I've committed that code. It's kicked off a pipeline to go ahead and test that out. So I think this is probably ready. I'm going to mark it is ready and I'm going to go ahead and tag for review @cbot2000 How does this look to you? And even though I'm using a kind of trivial example here, I'm just changing a few nodes.

    I wanted the change to be simple to understand. What's important here is this collaboration. This is how as platform engineers, infrastructure and operations engineers, you can collaborate with each other or collaborate with your dev teams so that you have collaboration between developers, a security team, the operations team, all in one place. So if we look now back at our comment box view of the— of the issue they see, okay here is this related merge request.

    And they can now go to the changes and they can see oh okay, I've put it to two and maybe they might make a comment, you know, looks good, or maybe if there's a question they could provide an in-line suggestion, you know, maybe to make it three instead of two, not 23, but in this case we think that two looks good. We're going to add that comment. And others can add those kind of in-line comments, and what that does is creates an unresolved thread here. So this is really nice because when we go through, we can look at the merge request. And see all of our feedback from our peers.

    So for example, in this case, we see there's an unresolved thread. We're going to jump to that thread. In this case we're just being told this looks good, but maybe it might be something to address and when we address that problem, then we can resolve the thread so we can see, we'll go ahead and resolve the thread. And that'll make the change ready to merge. We can also see that our pipeline passed and it all looks good. What I can do now is, go ahead and merge the code because it's been reviewed and what's really nice about this is in my Git— Git commit history, I have a history of what exact changes were made.

    I have a history of who participated in this. I have the discussion that took place. I was able to collaborate. So even with this small trivial change, I've been able to have a lot of collaboration and even have some compliance capabilities. For example, let's say you might want a lot of people to be able to suggest changes to your infrastructure. Anybody could make a merge request to suggest a change, but you could lock down the permission so that maybe only a few people have that ability to merge or approve. And so this allows you to stay compliant as well with your internal compliance policies, or if you have regulatory compliance.

    And it's a lot faster and a lot more automated than, you know, having that change management meeting. This is a much more modern way to do it. What I can see here is as I've merged, it’s gone and kicked off a pipeline to go ahead and do my master pipeline where I have a build and an infrastructure update. And the last thing that I want to show that's really neat is, here is the Pulumi integration. So even though this comment was left by the comment bot, you can see I didn't leave it. This was done via the integration and what it's done is set the Pulumi plan output directly as a comment.

    So one way I could review this, is I could go to the pipeline and look at the actual job. And I can see the job that's run. I can even go to the permalink which is really nice. I can open this up inside of Pulumi console. I get a lot of nice changes here. I can see what was updated, but instead of having to make all of those clicks and all of those steps, with that one webhook that we set up, we get a comment here to show us what the update and what the change was made from Pulumi.

    So as it runs the master pipeline, it's going to go ahead and make those changes, update those in my cluster. We’ll take a look at those in just a moment. Let me walk you through some of the code. So as I mentioned, I started with the basic A-W-S Python E-K-S example that I just downloaded off the repository and I just made a few changes. One of the changes was I added the GitLab C-I-C-D configuration and this added three scripts here. A setup script, which basically just logs into Pulumi. So when this setup script runs, it's going to log me in.

    There is a preview script and there is a run script, and you can see these are exactly the same. The only difference is this one runs Pulumi Preview. So it's going to show me the changes, but not actually enact them, and this one actually runs Pulumi Up and go ahead— go ahead and make the changes. And this is my GitLab C-I YAML file. So this is the file that is configuring these pipelines that are running. You can see I've got two stages here, a build an infrastructure update.

    The build phase is just a stub but this could be where you set up your U-I, your service, and the infrastructure update is the one we care about. So what we're doing here is on the master branch we are running the Run Pulumi, or the Pulumi Up script, to enact the changes. And on the merge request we're running the preview. So when we have a merge request, this is the test, I just want to see the preview. I don't, you know, every time I make a change in a merge request, I don't want it to actually go in and enact those changes, I just want to preview them.

    But when it all looks good and I actually merge to master, then I'm actually going to run the Pulumi Up and enact those changes on A-W-S. And the last thing I'll point out, a really nice feature, is that in order to make this really easy is I've just pulled the Pulumi Python image off of Docker Hub, so that it already has Pulumi installed when it goes to run my C-C-D. It just pulls in this image and it can just start executing these commands. That's a— that's the basic setup.

    This is the main Python, we can see that it's got the old info there, but if I do a Git pull, it'll— it'll pull my changes and I can see, there we go, now it's updated. And let's go take a look at that master branch. It looks like it has finished running. It's completed successfully and in theory, if it's all goes well, and we look at our A-W-S cluster, we can see we now have two nodes. It's the same change. But in this case, we've done it in a way that's collaboration. We've done it through compliance. We call this GitOps. Operations by Git request. Thanks a lot for watching. Please do reach out to me on Twitter and have an excellent day. Cheers.
aliases:
  - /resources/introduction-to-gitops-tech-talk
---
