---
# Name of the webinar.
title: "Azure Cosmos DB Serverless Preview"
meta_desc: "In today's episode, we explore the next generation Microsoft Azure provider for Pulumi. We take it for a spin on Azure's Cosmos DB serverless preview."

aliases:
  - /resources/azure-cosmos-serverless-db-preview
  - /webinars/azure-cosmos-serverless-db-preview

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: true

# The preview image will be shown on the list page.
preview_image: "https://img.youtube.com/vi/U13FC3_eOh4/hqdefault.jpg"

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
url_slug: "azure-cosmos-serverless-db-preview"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Azure Cosmos DB Serverless Preview"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Azure Cosmos DB Serverless Preview"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/U13FC3_eOh4"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-09-23T10:00:00-07:00
    # Duration of the webinar.
    duration: "4 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        In today's episode, we explore the next generation Microsoft Azure provider for Pulumi. We take it for a spin on Azure's Cosmos DB serverless preview and show how easy it is to create a database and wire up the connection string information to a client. Code for the episode can be found [here](https://github.com/pulumi/pulumitv/tree/master/modern-infrastructure-wednesday/2020-09-23).

    # The webinar presenters
    presenters:
        - name: Lee Zen
          role: VP Engineering, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - Create a Cosmos DB account.
        - Provision a database and container.
        - Setup a client to interact with that container.

transcript: |
    Hello, and welcome to another episode of Modern Infrastructure Wednesday. I'm your host, Lee Zen, and today we're going to be covering the Azure Cosmos DB Serverless Preview along with Pulumi's new Azure Next-Gen Provider. So, what are we going to do today? We're going to be covering creation of a Cosmos DB account, provisioning a database container, and then also setting up a client to interact with that container. So, very basic stuff, but really just excited to show off the new next-gen provider that we've built that really covers the full surface area of all those Azure resources that you want to use. And really, the ability to use any feature on day one, once it's announced because we're compiling our provider based on the actual Azure REST API specs. So, let's get started.

    I have a [TypeScript program here](https://github.com/pulumi/pulumitv/tree/master/modern-infrastructure-wednesday/2020-09-23), so you can see we're importing from our new Azure next-gen provider here. Then, I'm also importing from the Azure Cosmos Client. I already have everything prebuilt because I don't want to spend any time on the provisioning steps. So, you can see this looks and behaves very similar to the previous Azure provider. You create a resource group, you create a document DB database account. We give it the parameters we want. In particular of note here is that you can actually, again, because we're reflecting the full surface area of that resource model in the Azure REST API, we can give this a capabilities property with the name EnableServerless, and this will enable the serverless preview for Cosmos DB.

    Everything else after that is fairly standard. We create a SQL database in that Cosmos DB account, and then we create a container to interact with it as always. Then, finally, you could do a number of things with these outputs now, so at the end of this, we'll have created that account, the database, and then the container, and then you can then get back to the connection string. So, you can see here, again, using the new provider, we can actually make a call to list database account connection strings, which is again, part of that REST API surface area that we've modeled. So, we can actually get back those connection strings. You could totally imagine taking that and passing that on to something else. So, passing those connection strings onto, for example, a function or something like that, or storing it as a sequence so you can use it later on in your web app.

    In our particular case here, I'm just doing something super simple. I'm using the Cosmos Client that I've imported from above, and then I'm just going to insert a single item here with just some key and some value. So, if we run this program, we've already gone ahead and all these resources were already created, so there's really not too much to show there. As you can see, there's no changes. But if I say yes, this particular `apply` will actually run and we should see an additional item in our data store. So, if we go here and this is the items, this is the serverless DB that I created, and if I refresh my items here, you can see that I have a third item now, and that has that timestamp inserted in.

    So, really just wanted to go through the basics of using the new next-gen provider with Pulumi and how easy it is to use it and how easy it is to actually wire things in and get your applications up and running on the new preview for Azure Cosmos DB. I hope you enjoyed today's episode of Modern Infrastructure Wednesday. Please make sure to [subscribe to PulumiTV](https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw?sub_confirmation=1) for future updates and leave your comments below and like the video, if you enjoyed today's episode and I hope to see you next week on PulumiTV. Thanks very much.
---
