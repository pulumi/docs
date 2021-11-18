---
# Name of the video.
title: "Introducing the Pulumi AWS Native Provider"
meta_desc: "Pulumi’s AWS Native provider offers a well-defined resource model for AWS that allows developers to build, deploy, and manage AWS infrastructure."

# A featured video will display first in the list.
featured: false

pre_recorded: true
pulumi_tv: true
unlisted: false

# Gated videos will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars

external: false
block_external_search_index: false

# The url slug for the video landing page. If this is an external
# video, use the external URL as the value here.
url_slug: "introducing-the-pulumi-aws-native-provider-powered-by-aws-cloud-control-api"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Introducing the Pulumi AWS Native Provider Powered by AWS Cloud Control API"

# Content for the left hand side section of the page.
main:
    # Video title.
    title: "Introducing the Pulumi AWS Native Provider Powered by AWS Cloud Control API"
    # URL for embedding a URL for ungated videos.
    youtube_url: "https://www.youtube.com/embed/oKxaZCyu2OQ"
    # Sortable date. The datetime Hugo will use to sort the videos in date order.
    sortable_date: 2021-09-30T10:00:00-07:00
    # Duration of the video.
    duration: "4 minutes"
    # Description of the video.
    description: |
        Pulumi’s AWS Native provider offers a robust, reliable and well-defined resource model for AWS that allows infrastructure teams and developers to build, deploy, and manage AWS infrastructure with languages like TypeScript, Python, Go and C#.

        The AWS Native provider builds on the work done by service teams at AWS to define the resource model for their services.  This ensures a rock solid provisioning lifecycle for resources deployed with the AWS Native provider and same-day support for all new features in the AWS Cloud Control API.

    # The video presenters
    presenters:
        - name: Laura Santamaria
          role: Developer Advocate, Pulumi

# This section contains the transcript for a video. It is optional.
transcript: |
    Hi there, Laura from Pulumi here. Today, we're going to go check out the new native provider for AWS, that you can use with Pulumi. Native providers work directly with the cloud providers resource model. In this case, we're working with AWS's Cloud Control API, which directly accesses AWS's resource model. That means you get direct access to the resource model as well. Built only by AWS. You can rely on everything that they have, and you're not really relying on any kind of a bridge.

    But what does that really mean for you as the user? Well, you get same-day updates. If you see something really cool at re:Invent, as long as it's on AWS, it's out for Pulumi. In addition, you get a solid and reliable provisioning experience, just like you're using the console.

    Finally, of course, you can use any programming language that works with Pulumi, just like you've come to know and love. Enough about the high level stuff though. Let's go code.

    All right. Now, we have the code. First things first, let's take a quick look at what the classic provider was for anybody who's not familiar with the AWS classic provider. This is a simple Lambda function that is going to have our state machine running. It's pretty basic. We just have this little file archive that's running this hello.api. Nothing too exciting when it comes to a Lambda, but it should give you a rough idea. The IAM that's being imported here is just the IAM. You see this one here on line six IAM.Lambda_role.ARN. That is calling to a actual separate file that we've written up that abstracts away all of the IAM role creation and role binding all the role policy information that isn't in the provider just yet, because this is a beta release. That's coming, but we didn't really want to get everything a little too confused with the that. This is just what the classic provider looks like. Let's see what the native provider looks like.

    Basically the same, the native provider is really just couple of little things that we've abstracted out one or two, like this definition string, instead of definition, for this same exact code. If you wanted to actually have definition, you just changed the code up a little bit, but I wanted to show just how similar all of this is. It's not that much different, but you're going to get all of those benefits of using the native provider by being able to do this. So let's go ahead and we are going to deploy this. Just the simple quick the Pulumi me up and through the magic of movie, we're going to zoom ahead until we're all ready to go. And there we have it. So this is all deployed. Let's just double check. I have a little command here, just running AWS. The step functions feature from the CLI, just to see we use a quick stack output to the state machine saying here, give me that information.

    There it is. It ran perfect. It's up and running. Now we'll just do a quick little 'pulumi destroy' here to take down that stack real quick. While that's running, just something to know is we also have the new cf2pulumi tool. The cf2pulumi tool is taking any CloudFormation set up and converting it to Pulumi. The tool is coming out as part of this preview. So please do go check it out. It allows us to migrate any configure really. And if it's deprecated right now, if it's not exactly ready just yet with the cloud control API, there is a little note saying that we're not ready just yet for you.

    Thanks for joining me today to check out the new AWS native cloud provider with Pulumi. I hope that gave you a sense of what's possible and what's next with cloud engineering with Pulumi. Give it a try and let us know what you think. See you soon. Bye.

---
