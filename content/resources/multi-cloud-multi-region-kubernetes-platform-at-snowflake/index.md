---
# Name of the webinar.
title: "Shipping a Multi-Cloud Kubernetes Platform at Snowflake"
meta_desc: "Learn how the Snowflake team shipped a truly multi-region, multi-cloud, global-scale service in a few months using Kubernetes."

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
url_slug: "multi-cloud-multi-region-kubernetes-platform-at-snowflake"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Shipping a Multi-Cloud, Multi-Region Kubernetes Platform at Snowflake"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Shipping a Multi-Cloud, Multi-Region Kubernetes Platform at Snowflake"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/oD9m6e3Bo2o"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-10-08T10:00:00-07:00
    # Duration of the webinar.
    duration: "15 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Learn how the Snowflake team shipped a truly multi-region, multi-cloud, global-scale service in a few months using Kubernetes.

    # The webinar presenters
    presenters:
        - name: Jonas-Taha El Sesiy
          role: Senior Software Engineer, Snowflake
        - name: Raman Hariharan
          role: Director of Cloud Platform Engineering, Snowflake

# This section contains the transcript for a video. It is optional.
transcript: |
    **Raman Hariharan**

    Hi, today's topic is multi-cloud, multi-region kubernetes at snowflake. My name is Raman Hariharan, at snowflake. My name is Raman Hariharan, I'm the Director of Cloud Platform Engineering here at Snowflake. We at Snowflake are building cloud data platform to break down data silos and enabling data collaboration capabilities while leveraging the near endless performance and scale of the cloud. The experience I'm going to talk about is one of the flagship products that we were working on at the beginning of the year. The solution itself was developed on top of kubernetes for a lot of you know reasons.

    It's— becoming the de-facto platform for developing containerized applications and which in turn allows for faster innovation and roll-out across different cloud providers. The challenge me and my team faced at the beginning of the year as we were looking for a new tool, was we needed a solution that can build, deploy, manage kubernetes, you know, clusters at scale, right? Across different cloud providers in 20-plus regions worldwide. This was a problem that's not easily solved and probably limited to only the cloud providers. The traditional approach for solving this problem did not work for us. We are a software engineering organization. So the tool that we were looking for was— had to meet some certain key criteria. One of them being, you know, it had to support our standard programming language which was Golang. We wanted the ability to kind of treat the infrastructure as code, have testing capabilities and make it seamlessly integrate our C-I pipelines. So we also we're faced with a very aggressive deadline.

    So from— when we were innovating rapidly, so we had just three months. On one end we were supporting the product and efforts in terms of rapidly innovating and developing, you know, the prototypes and iterating through it. and on the other end we had to actually think about rolling it out at scale. That's where we're looking for a tool that could actually help solve our challenges. At this time, I'm going to hand it off to my colleague Jonas who's going to talk more about our journey and how we leveraged Pulumi to solve our objectives.

    **Jonas-Taha El Sesiy**

    Yeah. thanks Raman. I'm Jonas. I'm a software engineer here at Snowflake. Before that I worked at I-B-M and Mercedes Benz R&D. My primary area of focus is infrastructure and automation. So as Raman mentioned let's dive into the solution overview a little bit. This is the high-level architecture of how we were setting up our new kubernetes infrastructure co-located to regional Snowflake deployments. As we can see we have A-W-S, Azure, and G-C-P-S and major cloud providers with multiple regional deployments. And each of them has a kubernetes delployment. What are the components that constitutes our solution, and how we were able to embark on this journey in the first place? As Snowflake values customer security, we had to really look into private networking, restrict egress and ingress controls.

    For that we use security groups, Calico and Istio. We use postgreSQL for our two major applications, which is Snowsight and DataExchange. This is what you see when you go to app dot snowflake dot com. For mission critical infrastructure, we wanted to make sure we have good monitoring components in place. For that we use Telegraf and Wavefront. All of our application logs make their way into blob storage accounts on the respective cell providers and are then imported into our internal Snowflake deployment, which helps our developers to trace issues and look at certain events. On top of that, we want to make sure that all of our developers have a unified experience accessing all these deployments for which we use Teleport.

    In order to have a seamless deployment in place, we use a GitOps workflow using ArgoCD that takes care of deploying our manifest off of the Git branch and ensures that the state is reconciled at all times. Now, let's dive a little bit into how an actual single regional department looks like. I know it's a lot to unpack here, but bear with me. We have two public load-balancers. One is for ArgoCD that is used by our developers to actually access Argo and get a glimpse into how the application state looks like. For customers, we have a public load balance, for which traffic is directed to the respective applications. We use Istio for M-T-L-S and we have a layered network security model in place where we have security groups on the kubernetes V-P-Cs, we have Calico rules for strict egress controls and Istio for— service communication and authorization policies.

    This is all done in a multi A-Z fashion, where if a certain node goes down, you can make sure that the application stays responsive. On top of that, we do have the postgreSQL database deployed to it. Now, let's look into the networking architecture a bit more, and how we ensure that there's connectivity to the existing Snowflake deployments. As mentioned before Snowflake’s focus on security is high. So we need to make sure that the traffic does not traverse the internet. We started out with having a big co-located kubernetes V-P-C that uses V-P-C peering to the region of Snowflake deployments using an internal load balancer on the Snowflake side and a core V-P-C that hosts shared services.

    For monitoring we use Telegraf as a Daemon Set running on each node forwarding StatsD metrics to Wavefront proxy, which end up in Wavefront. Wavefront reall is our view into what's happening live in over 30 clusters today. We do use Pingdom for our time checks. So we get alerted on that and we use PagerDuty for incident response. For logging, we use FluentD as a Daemon Set on each node that tells the docker logs and forwards them to the respective storage location based on the cluster.

    So for A-W-S our logs go to S-3 and for Azure they go to Azure blob. Down here you see a small glimpse of our Snowflake U-I and how our developers are able to retrieve the logs. So now let's talk about how we were able to manage all these deployments and how we were able to create reliable and repeatable automation. For infrastructure deployments. We use Pulumi. All of our platform components reside in Git. We use ArgoCD, that is managed by Git cluster-autoscaler, logging and monitoring components, and a bunch of custom kubernetes controllers that helps us automating even further. In these repos a mix of Kustomize resources and Helm charts reside.

    ArgoCD reconciles the state that it’s based on. Our internal customers have their own repos where they host the application manifest. Let's look how the deployment pipeline helps our developers to get the applications deployed. We have a developer pushing a commit to Git and the specific branch of that application is picked up by ArgoCD. ArgoCD then goes ahead and deploys all the application components into the respective customers namespace. The clusters itself are deployed by Pulumi. Now, let's have a look at a small demo of how that could look like using Pulumi. What I'm about to show you is a setup that uses micro stacks to separate infrastructure layers from each other so they can evolve independently similar to the notion of micro services.

    We’ll also be using the Next Generation Azure provider that has access to a broad and extensive list of Azure A-P-Is using the Go S-D-K by using automation A-P-I. We are able to have an easy orchestration layer for stack updates across multiple stacks. We also make sure that we use a custom secrets provider to keep our state secure, using our own provider key. I switched over to my terminal here. So let me give you a quick overview of what the code does. We have two projects network and kubernetes. Network provides a shared layer of networking resources that are going to be used by kubernetes. Let's have a look.

    As it's customary for Azure, first we create a resource group. Next we create a virtual network as seen here, with the sider annotation and the private I-P space. We then go ahead and create a subnet as seen here. That does not span the full v-net. Last we're going to export certain properties that are needed by kubernetes. Now let's switch over to kubernetes and see how that looks. First we create a stack reference to read off of the remote stack. And retrieve our properties that we need for our cluster. We then go ahead and create an S-S-H key pair that is needed to access the worker and notes and then we create a kubernetes cluster.

    As you can see, we also limit the access to the A-P-I server to a certain I-P, which already shows the power of using a real programming language. We’re calling another go function here. All that is doing is retrieve the public I-P of the host running it. We create an agent poll three nodes. Create a user profile using kubernetes 1-16-13, and lastly we're going to export to kubeconfig. So now, let's look at the automation A-P-I. What the automation A-P-I does is allow us to iteratively go over stacks. First, we're going to retrieve the passphrase that is going to be exported on the environment and then we dynamically create stacks and run Pulumi Up.

    Lastly we're going to export the kubeconfig write it out to the file system so we can attack with it. Let's see how that looks. First I got to export the passphrase and now I'm going to run my program just like any other program. Ss you can see the huge benefits to using this approach. We have static typing, we have I-D-E support and auto-complete. This is going to take awhile. All right, great. Our stack has been deployed. Now that we have validated access to the cluster let's have a quick look at how it looks in the Azure portal. We created our resource group, we have our cluster and the v-net with our custom tags on it.

    So, working with Pulumi helped us get to our goal fast. First, we were able to use a standardized language and framework. We have full I-D-E support, that includes debugging, we have out-of-band operations such as making A-P-I calls as we just see, we can use custom stack encryption to store secrets in the state. We have static typing. And ultimately, the tight feedback loop that we had with the team over at Pulumi really helped us to get to our goal. Our team was also involved in design reviews for new features to Pulumi that will benefit the whole community. What's next? We hope to broadly adopt the automation A-P-I once it gets out of alpha.

    We will set up C-I systems to drive that automation even further, and ultimately we're going to be putting crossguard policies in place. Right now, we’re up and running and over 20 regions in a very short time span covering all major cloud providers and we’re super happy with the result. Thanks for watching my demo, now, let's throw it back to Ramen. Thank you Jonas. So to summarize, like, we were very successful in the launch of the product and we had great adoption, you know, for the product, and you know, I want to just give a huge shout-out to the Pulumi engineering and the support team who are a trusted partner along the way.

    We couldn't have done it, you know, without them. And we feel like, you know, this is just a start of the partnership and as we continue to innovate, you know, we're going to continue to leverage, you know, the platform to even greater possibilities. Thank you.
---
