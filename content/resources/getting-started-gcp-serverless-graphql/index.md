---
# Name of the webinar.
title: "Getting Started with Serverless GraphQL on GCP"
meta_desc: "In this episode, Lee Zen walks you through building a serverless GraphQL API using Apollo GraphQL and GCP Functions with the help of Pulumi."

aliases:
  - /webinars/getting-started-gcp-serverless-graphql

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: true

# The preview image will be shown on the list page.
preview_image: "https://img.youtube.com/vi/mU5_aclyQR8/hqdefault.jpg"

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
url_slug: "getting-started-gcp-serverless-graphql"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Getting Started with Serverless GraphQL on GCP"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Getting Started with Serverless GraphQL on GCP"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/mU5_aclyQR8"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-05-19T10:00:00-07:00
    # Duration of the webinar.
    duration: "10 minutes"
    # Datetime of the webinar.
    datetime: "MAY 19, 2020"
    # Description of the webinar.
    description: |
        In this episode, Lee Zen walks you through building a serverless GraphQL API using Apollo GraphQL and GCP Functions with the help of Pulumi. The code for this episode is [available on GitHub](https://github.com/pulumi/pulumitv/tree/master/modern-infrastructure-wednesday/2020-05-20).

    # The webinar presenters
    presenters:
        - name: Lee Zen
          role: VP Engineering, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - Deploy an Apollo Server to GCP
        - Learn about callbacks and callback factories

transcript: |
    Hello, and welcome to another episode of Modern Infrastructure Wednesday. I'm your host Lee Zen. And today, we're going to be talking about serverless GraphQL API. It's kind of a lot to unpack. What we're talking about is really how to build a GraphQL API using the function in GCP. And you can see, I'm wearing my new super Pulumipus t-shirt, so let's get started. In this episode we'll be covering a way to modify an existing example. It's an Apollo Server example. Apollo is one of the GraphQL API implementations and then we'll learn about callbacks and callback factories, and seeing how we can actually modify the example to work with callbacks in Pulumi. You can follow along on [github.com/pulumi/pulumitv](https://github.com/pulumi/pulumitv). All the example code will be there, as well as all the previous episodes example code. And of course, if you enjoy this episode, please like and [subscribe](https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw?sub_confirmation=1) to the channel for future videos. We're publishing one every week, please comment if you have any feedback.

    Let's take a look at what this looks like. I already have a skeleton project set up for GCP and Pulumi on TypeScript and if I go look at the example I was talking about, this is in the [Apollo GraphQL repo](https://github.com/apollographql/apollo-server/tree/main/packages/apollo-server-cloud-functions). I've already installed the two dependencies they talk about. So now we're just going to copy and paste the code they have around implementing the API handler as a Google function. This is really what the function should be in the Google function itself, but for now, we're just going to drop it into our Pulumi program and then add some things here to get this to deploy. This handler is really what we want to deploy, so we can make an API. Well actually, we'll call it a function. We'll call this API function and this is a GCP cloud functions callback function. We'll call this API function and this could really just be the `server.createHandler` here. The reason, as you can see, it takes a callback, which is exactly what this creates. That's pretty much all we would technically need.

    In addition to that, we will want to actually create a invoker so that we can actually invoke a role, rather, a member, so that we can actually invoke this from anywhere. So let's go ahead and do that. We'll call this the API invoker, and this is a cloud functions member. We'll call this API invoker. We can see here, this takes a function, so this will be the function above, there's an underlying function, and there's the ID. Then it also requires a member, and this will be all users. So we'll let anyone invoke this, even just random internet users. We'll give it a role, which is the cloud functions invoker role and then finally, we'll export the URL of the function that we're creating.

    Cool. So let's try running Pulumi up and see what happens. This should actually fail and the reason for that is because, and you'll see quickly, when we try to serialize the function, it doesn't really work because we try to capture this Apollo Server class that we instantiate up here, this object. We really don't like this and stuff like that and part of that is because we're kind of crossing this boundary between instantiating this here and then trying to use it as a full fledged thing in our function. So we could fix this up, and let's do that, by wrapping this. So we'll call this a callback, and we'll make a callback up here. And actually, let's clean this up and make this look more TypeScripty here. We'll do import `from`. Let's do that.

    We'll have this function callback and callback actually... Let's look at the type signature for this. Actually, looks like this. So it's an `express` request response to avoid. Let's just copy this here and we'll use that signature in our callback. We'll just indent all this. Earlier, we had `server.createHandler`, and this is our callback function. Right? So we can just invoke this with the request response and so we've basically... Oh, we need to import `express`, of course. Let's try this. So what we've done is we've wrapped all that code we had previously, into the callback itself and we're just calling the callback as if that's what we're doing. So let's say yes. So instead of just passing off the function itself, instead of just passing this, we're also doing all of this other work that we were doing before in our Pulumi program, and now doing it as part of the callback itself.

    So let me fix the invitation here while that's running and while this is running, actually, let's also take a quick look at the example here. You can see what this is really doing is... It's very simple. We're just creating a simple schema, where we have a single query type with a parameter, `hello`. These queries just return, `"Hello world."` So we're not doing anything complicated. Obviously, if you want to get into this, you can go learn more about GraphQL or if you're already a GraphQL user or knowledgeable GraphQL, you can pretty easily modify the example we're doing to work with your needs. This is still deploying. You can see the function created, the IAM Member created, so everything worked. Let's try to execute it. We can curl Pulumi... Oops. Let's wait to curl at post. We'll take the `stack output` of the URL, and we probably need to give it a content type `application/json`. We'll give it some data, it'll be `query`, and we'll give it the query of `hello`.

    So, let's try that. And so now this is actually executing the function, and we get back the result we expect. So life is good. You can see it was kind of a little bit slow, but that's some of the startup time. But also, some of that's because every time we invoke the function, actually, it's going to run all this code. This is all part of our callback. It's going to instantiate a new Apollo Server and do all this stuff, and then finally invoke the callback. So how can we avoid all this stir up overhead? Well, that's where a callback factories come in. So let's take a quick look at the cloud functions documentation for Pulumi. You can see, we have this concept of a callback factory. It's a signature that actually produces an entry point, but it allows us to initialize expensive state. The whole point is that this factory lets us create a callback. So let's do that. How do we do that? Let's modify our example here, so instead of just giving it the callback, we can actually give it a callback factory.

    We'll give this a factory, which we haven't declared yet. Let's go back up here, and let's change this to be a factory and as we will post, the implementation for a factory is actually fairly simple. It's a function that takes no parameter, and it returns a callback. So we can actually, instead of doing this, we can just return this. Now we're not wrapping the whole thing. Now what's going to happen, is all of this code, all of this, is going to act as initialization code and then this callback is actually the handler that will be called on each function invocation. But the remaining stuff up here is only called one time, when the function is first created. Let's update this, and we should see this still work. We can see it's going to replace the function with... The bucket object is the source code and then also replace the... Since we've changed some of the other stuff here. Let's do this. You can see the URL. We don't know what it's going to be now, since we're going to have a new invocation URL.

    Let's run this. It's a couple of minutes for us to update. So just a quick recap of what we changed. Before, we were just invoking the whole thing as its own callback. Now, this factory function is basically just... It's just returning the callback instead. And all this stuff becomes initialization code. Actually, if you were to go into the console and look at how it's set up, you would actually see that happening. There's the initialization followed by using the handler as just this, as opposed to the entire handler being all of this code. So that would be the difference. Okay, great. So our update is done, and you can see we updated and replaced the object. Now let's go back to run our `curl` command. We should see that this will return the same thing, but without having to do all of that startup cost. So that's it actually. Those are the two things I wanted to run through today. Hope you had a good time following along. As always, please like and [subscribe](https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw?sub_confirmation=1). Please leave any comments in the video, and we'll see you next week.

---
