---
# Name of the webinar.
title: "Anomaly Detection with AWS GuardDuty and Slack"
meta_desc: "In this episode, Lee Zen walks you through anomaly detection with Amazon GuardDuty + Slack using TypeScript and Pulumi."

aliases:
  - /resources/aws-anomaly-detection-guardduty-slack
  - /webinars/aws-anomaly-detection-guardduty-slack

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: true

# The preview image will be shown on the list page.
preview_image: "https://img.youtube.com/vi/PF7KnOB3fLk/hqdefault.jpg"

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
url_slug: "aws-anomaly-detection-guardduty-slack"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Anomaly Detection with AWS GuardDuty and Slack"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Anomaly Detection with AWS GuardDuty and Slack"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/PF7KnOB3fLk"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-04-01T10:00:00-07:00
    # Duration of the webinar.
    duration: "13 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        In this episode, Lee Zen walks you through anomaly detection with Amazon GuardDuty + Slack using TypeScript and Pulumi.

    # The webinar presenters
    presenters:
        - name: Lee Zen
          role: VP of Engineering, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - Setting up AWS GuardDuty and CloudWatch Events
        - Creating a Lambda function using a callback
        - Enable anomaly alerting with Slack

transcript: |
    Hello, and welcome to another episode of Modern Infrastructure Wednesday. Today, we're going to be talking about anomaly detection, in particular, looking for anomalies in your infrastructure and looking for oddities that might be occurring in your metrics. We'll have two parts of this, today, we'll cover GuardDuty and next time we'll cover looking for anomalies via CloudWatch Metrics.

    So in this particular episode, we'll be using Amazon GuardDuty to look for anomalies, particularly against cloud trail events and other things like that, and then we'll be connecting that with CloudWatch Events to notify us. We could define a callback that becomes a serverless function so we can use that to actually alert us in Slack, as the watch event is hooked up to Slack via Webhooks. If at any point, you want to follow along with the code, you can check it out. It's on [github.com/pulumi/pulumitv](https://github.com/pulumi/pulumitv/tree/master/modern-infrastructure-wednesday/2020-04-01).

    All right, let's get started. Let's start a new Pulumi project and we'll use TypeScript today. Oops, sorry, let me make a directory first, we'll call it `guard-duty`. We'll take the default `guard-duty` name, we'll call this "Detect Anomalies via GuardDuty", we'll go with the `dev` stack and let's go with `us-east-2` today. So while this is installing our Node dependencies, I'll fire up Visual Studio in a separate window. All right, and here we go, we'll open up Visual Studio code here. We're ready to rock and roll. All right, let's make this a little bit bigger, and we want to create some GuardDuty stuff. I don't remember how to do that off the top of my head, so let's look at some documentation. We'll go to the AWS docs, look for the GuardDuty package module right here, and I'll bump this up in case you can't see, and we want the detector. So let's look at what we can do here. All Right, that's going to copy and paste this actually, this looks pretty straight forward.

    Give this a better name, let's call it a Detector. And what else do we need to do? Finding publishing frequency. Okay, I think, probably don't need anything there, and in addition to that, we also want to set up a CloudWatch. So now we have the detector, we also want to set up a CloudWatch event, and this, I happen to know off the top of my head, I do. So we'll do a new CloudWatch event and we want an event rule, actually, so we'll call this our GuardDuty rule and we'll look for an event pattern and we'll look for, in particular, the source of AWS GuardDuty. Pretty sure that's our limit, let's actually double check that. Let's Google for GuardDuty events, and this is probably it.
    Yeah, so we want to, we want to look for this particular format of the source. So this CloudWatch event rule, that we're creating here will match on any events that match this particular source type, which is the source type here in this particular event, that's going to fire. And so now we'll actually have this CloudWatch event rule that we can work against. So this will generate notifications, or CloudWatch events rather from that detector. And now we can actually create a callback to work against this. So one way to do this, we could do a rule on the event, so we named this `guard-duty-callback`, and we can actually just give it our handlers right here, so we can actually have this be our event.

    And this could be, if you, look at the typing, this is actually what we expect it to be, it's the event rule event, but we can actually declare what we're going to do with it here. And we actually want to post this to Slack. So we're going to actually import `axios` and actually need to see us. So we actually need to make a post call here to do this and in our code, we, what we want to do is we would like to actually, anytime we have an event notify ourselves that something happened. We can do something like this and realize we need a URL here. So let's put in a temporary placeholder here, let's call it URL and we'll figure that out later. We'll have some text, `Amazon GuardDuty has detected new findings!`. Let's actually wrap this up so we can actually see what happens if anything bad happens.

    And that's it. Actually, this is pretty simple. And so now the question is, how do we get this URL? So what we really want to do is pass in a Slack, WebHook Url, so we can post to Slack. And so if I go back to my browser, you can see, I have this handy dandy, incoming Webhooks thing set up, and that can create a web pocket. I can copy it and post it into a post into a channel. So you can see here, I'm actually going to post it into this `#ops-security` channel. So to do that, I probably actually want this to be an environment variable. So just putting our secret in here, right? So let's actually configure this as a secret. So we will do this. Which will give us a config object to work with, and then we'll call a `slackWebhookUrl` and require the secret.

    We'll call it. You know we won't be too creative here and call this `slackWebhookUrl`. And so what you would do here is you would do `$ pulumi config`, make this a little bit bigger in case you can't see. See `$ pulumi config` and you can see actually I had my handy little helper here. It just tells me what stack I'm on. That's a custom thing you can add. Shoutout to [Community Slack](https://slack.pulumi.com/) for telling me how to do this. Pulumi config and we'll set the `slackWebhookUrl` to for now is put in a placeholder here and we'll say secret. So now we have this URL that would be in our application. I would actually normally get that from this page, but don't really want to copy and paste something that you're going to see that actually POSTs into our Slack channel. So I'll just put that placeholder there for now. And since we want this to be, so we can't actually pass that into here because if you look at this, this is an output and we're not going to do that here. So what we do want to do is instead I'm going to actually create a callback function so we can pass in.

    So we can actually pass in the URL as an environment variable. So that's actually better for, from a security perspective as well. So let's do that. Okay this callback function and it takes this event type, which if I recall correctly, I'll need to look at my types again. So it's a AWS CloudWatch event rule event. Did I misread the type? Is it an AWS CloudWatch, dependable event? Ah, sorry, this is, this is not type safe. Actually it might be, let's see. So we give it some arguments, so we give it a callback. So it'd be our events to the actual code I had earlier. Oh, already have that.

    Now we can actually say, give it our event and we can pass in our environment variables. Now I can give it the thing from up there. So what this will do, let's see, let me see what's going on here. Oh, it's because I need this variable. So now we have this probably just auto complete in general. So yeah. Okay. And what's it’s complaining about here? Ah, it could be undefined. So while we know this is defined, so I'm just going to cheat a little here and just do that. And actually I think that's pretty much all we need to do. So at this point, what we've got is we created our little detector and we have this event rule that actually this looks for these particular events. And then we hooked up this callback function to this rule. So that every time this rule fires, we will basically post to our WebHook URL that we have new findings. And, then we finally hook up this callback to that particular rule at the very, at the very end. So we can actually run Pulumi preview here, see what it tells us.

    And there we go. We'll create all these different resources, and yeah, and then we'll, we'll be alerting on, on any anomalies that Amazon GuardDuty has detected. Cool. So that pretty much sums up this episode. In next week's episode, we'll actually talk about how to use CloudWatch alarms for anomaly detection, as well as using GuardDuty to detect anomalous behavior in your AWS accounts. Thanks for watching. I hope you enjoyed this episode, please like, and [subscribe](https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw?sub_confirmation=1) also interested in what you want to see for the next episode after the, after the next one, obviously. So feel free to leave some comments, follow us on [Twitter](https://twitter.com/PulumiCorp). And yeah, as I mentioned the beginning, if you want to check out the code it's available on [GitHub](https://github.com/pulumi/pulumitv/tree/master/modern-infrastructure-wednesday/2020-04-01). Thanks very much.

---
