---
# Name of the webinar.
title: "Day-two Operation of Multi-cloud Kubernetes and Vault"
meta_desc: In this session you learn how Snowflake worked towards implementation and the day-2 experience of using Pulumi to manage Kubernetes and Vault.

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
url_slug: "day-two-operation-of-multi-cloud-kubernetes-and-vault"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Day-two Operation of Multi-cloud Kubernetes and Vault"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Day-two Operation of Multi-cloud Kubernetes and Vault"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/0iAwwtjQvhw"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T10:50:00-07:00
    # Duration of the webinar.
    duration: "20 minutes"
    # Description of the webinar.
    description: |
        Snowflake is multi-cloud. So is its infrastructure. For two years, Snowflake’s platform team has been building and operating 100 (and growing) Kubernetes clusters on AWS, Azure, and GCP. Today, we run on average a total of 60k Pods to unlock $7M annual savings.

        We use Pulumi to provision cloud resources and manage HashiCorp Vault. In this talk, I will present how Pulumi has enabled Snowflake’s scale and growth:
        * How we leverage Pulumi Automation API to build custom rollout strategy for all Pulumi stacks
        * How we achieve blue-green upgrades for Kubernetes node pools
        * How we manage HashiCorp Vault using Pulumi:
            - rotating issuing certs (that signs Istio private gateway TLS cert)
            - static secrets (such as Teleport join-root token so k8s users could use one CLI to access all clusters and nodes)
            - cloud-provider secret engine (to generate scoped and short-lived tokens for services and automation)
        * How we generate and manage cloud-agnostic Kubernetes manifests by integrating with Pulumi stack outputs
        * How we use Pulumi Operator in CICD for auto-apply and audit

        This talk differs from the one my colleagues did in the Cloud Engineering Summit 2020. They focused on the container platform design (logging, monitoring, networking, etc). I will lean more towards implementation and the day-2 experience of using Pulumi.

    # The webinar presenters
    presenters:
        - name: Charles Xu
          role: Senior Software Engineer, Snowflake

# This section contains the transcript for a video. It is optional.
transcript: |
    Well hello everyone, thank you so much for joining me today.  My name is Charles and today I would love to tell you more about our multi-cloud experience building a multi tenant Container platforms on Kubernetes and Vault.  A bit more about me.  I work on the Container Platform team at Snowflake.  About more than a year-and-a-half ago my team started to build and operate a cloud agnostic container platforms based on Kubernetes.

    And today's talk is mostly about our experience and lessons of doing so.  I am excited about cloud native infrastructure as well as ecosystem.  So I think the contributor to several open-source projects in this domain.  Previously I work at Cruise, a self-driving car startup.  And my job was to design and implement a hyper cloud Kubernetes platform spanning GCP as well as on premise infrastructure.

    And before that I was working at Google on the Istio team the infamous open source service mesh.  You can learn more about me at my personal website as well as by scanning the QR code.  I would like to begin my presentations by sharing with you the key takeaways of this talk.  I want you to take this message with you before I dive into the stories and analysis behind them.  And then I will explain what Snowflake is.

    What is the data cloud? And what is the implications for the Snowflake infrastructure? And then I'll give an overview of the our Container platforms.  What are its current scales? What are some technologies that we use? And what are the applications that we run on this platform? And then I'll dive right into the cloud agnostic Abstractions and explain to you how this strategy has enabled us to expand our support into the three major cloud provider so efficiently.  And Pulumi has been a very important tool to unlock the projects success.  I will share examples of our experience using Pulumi to provision cloud resources as well as managing vaults.  And from this experience I want to point you at some of the key characteristics or features that you should be looking for in your next provision tools.

    And lastly I will discuss some open questions with multi-cloud that my team is still actively working on.  So takeaways.  Cloud-agnostic abstractions prevents fragmentation's and proliferation of identities, policies, and toolings but is not always possible.  Proliferation right here means that you have to use different accounts and different user account and service accounts to access comparable services on different cloud.  And it's even harder to manage policies because the IM boundaries and IM policies are totally different in concepts and different API objects.

    And the toolings that you use to access those cloud services or the client libraries are all so different.  So essentially you have the problem of fragmentation's where you're doing one thing for Azure and totally different things for Amazon.  And another different kind of set up for GCP.  And that's just not scalable.  And how do you assign different identities in different clouds that belongs to the essentially the same pre sequels? And governing the policies around that identity association? That's a challenge, and cloud-agnostic abstraction's definitely help in this case.

    But we will also discuss what are the cases that such abstraction is not possible yet? Secondly declarative infrastructure is insufficient to solve life cycle management.  Invest in a tool that allows orchestration.  Life cycle management right here refers to a cluster of version upgrades or stepping out additional clusters by some predefined configurations.  Orchestration becomes a key right here and we are operating at a scale of hundreds of clusters.  The best in provisioning tools that has the melting point that supports this complicated orchestration, because your infrastructure might be integrated with application on boarding and appointments as well as non cloud native infrastructure.

    And thirdly your infrastructure provisioner is either your metadata store or orchestrated by a metadata store.  And this store must be queryable.  We use to store this metadata within an internal wiki page.  Or this metadata is standard around the remits across our co ports.  Those are very hard to query and has been a number one headache in terms of implementing orchestrations where automations on top of different sets of tools that provisions the infrastructure and apps.

    So make sure that your infrastructure provides the interface that allows them to be queryable and orchestrate it.  Or you define this metadata within your provisioner itself that expose an API to make it queryable.  So the Snowflake overview.  Snowflake presents itself as the data cloud that sits on top of the three biggest public cloud providers regardless of where our customer data sits.  Snowflake provides one uniform execution platforms that unlocks all the data related functionalities such as data engineering, data warehousing, and data sharing.

    And because the Snowflake products are multi-cloud by nature so are our infrastructure.  Like I alluded to earlier, our continued platform has experienced tremendous growth in the recent months.  Currently we are running 110 Kubernetes clusters and my team's still building a lot more because of the business in it.  All the clusters averaged about 3,000 nodes in total, and that's about 60,000 Containers.  Because the cluster all the scales those are the average numbers.

    We built the continued platforms on top of the managed Kubernetes sovereigns to reduce operational overhead for the control prompts, but we do a lot more customizations and also add-ons on the clusters to make them a Container platforms that supports multi tenants.  All the clusters original clusters or multi AZ's and is deployed around the world.  The clusters are multi-tenant.  We support many different teams at Snowflake for their applications.  And meta teams share the same clusters and oftentimes many apps share the same node.

    Multi-tenancy has unlocked around seven million dollars savings in last year and we expect a lot more savings this year.  And our continual platform is integrated with the legacy VM-based infrastructure.  Snowflake was founded in 2012 and that's before Kubernetes was available.  So many of the infrastructure are still VM-based.  We have to integrate with the infrastructure to make sure there's network line of sight.

    There is privatizing nets resolution.  We're able to deliver the platform of this scale and scope because of the cloud native abstractions.  We've put a lot of thought into the sub systems that we use to reduce the customizations that we had to make for each individual clouds.  We use Okta to reduce the proliferation of identity.  Every users are assigned one Okta identity and assigned to several group membership.

    Each name space is granted access to exactly one group.  And Okta combined with Teleport ensured that users will only use one Teleport CLI to access all the different clusters and VM's on all different clouds.  One lessons we learn from this project is that we should try as much as possible to push up the policies into cloud native components such as pushing up network policies and mesh external traffic Policies, authorization policies, and routing rules, firewall rules, or OPA gatekeeper policies.  To further enhance multi-tenancies we developed in house custom resource definitions that abstract away the provisioning of Blob Storage buckets and objects as well as KMS services by different clouds.  Also for Vault policies for different tenants.

    So each tenant running in the name space will have the dedicated sub half on vault that they could use as the secret engine to store any kind of secrets that is secret.  And lastly for logging and monitoring we're relying on the core it Snowflake offering by itself kinda like dog food-ing our own products where we are streaming all the Container logs to Snowflakes using a product called Snowpipe.  Snowflake allows us to eventually write SQL to query our logs.  Like I mentioned before Pulumi has been a great fit for my team to provision cloud resources because Plumi enables automation toolings and hence rapid infra scaling.  We use Pulumi micro stacks or multi-stacks where we divided up the provisioning of each cluster into three separate chunks.

    The network, compute, and SQL.  And doing so drastically reduced Pulumi preview time which is sorta similar to Teraform plan.  Pulumi also makes cross stack referencing really easy.  So all the dependencies on multi-stack can be properly captured.  The Pulumi automation API is really powerful.

    There are at least four new cases that I have seen in our internal code leveraging this feature.  I'll focus on covering the first two where we implemented blue-green upgrades from Kubernetes node pools to minimize any kinds of disruptions as well as instant during the upgrades.  We also generate cloud specific Kubernetes manifests from Pulumi outputs.  And I'll explain why we decided to define Kubernetes manifest outside of Pulumi and how Pulumi still makes any kinds of custom toolings really easy.  In addition to those two we have implemented custom roll out strategies for Pulumi stacks which is important because we have hundreds of clusters that we operate and we want to do some kind of preliminary testing before we roll out the code changes to all the clusters.

    And lastly we leverage Pulumi operator which is a sort of agent-pull CICD solutions so that we don't have to manually apply hundreds of stacks.  Blue-green upgrades for node pools.  Blue-green upgrades for node pools is very similar for blue-green upgrades for say any services where we provision a new version of the backing service.  And then after you validate it the new service is healthy and ready.  We redirect all the traffic to the new version of the server and retire the old version.

    The blue-green upgrades for node pools allows fast revert and there's no chance for stuck between different versions.  The upgrade steps are creating new node pools, cordon and drain the old pools, and delete the old node pools after workloads has been migrated to the new pools and are running healthily.  The problems with implementing blue-green upgrades is that manual upgrades on hundreds of clusters is just error-prone and doesn't scale, especially because we expect to do a lot more in the future.  Moreover we cannot rely on the cloud providers on the upgrade feature because we have a really special Istio ingress setup which is prompted by the product requirements that we must preserve the client source by P in every IP packets.  Combined with the fact that Azure doesn't have a cloud-native load balancer where the Azure load balancer is using the nodes as the back ends instead of the pods.

    So the traffic has to be routed to the nodes, and then its IP tabled to the ingress gateway paths.  And we do value consistency cross different clouds.  And we do want to have a consistent architecture across cloud.  And therefore we arrived at this special architecture where we're running Istio ingress in a dedicated node pool that doesn't follow scale.  And we're running the Istio ingress gateway as a deem of set pods.

    This kind of set up requires special coordination's to include in upgrades because when the Istio ingress pods are shifted or migrated to new sets of nodes the old Istio networks are still the back hands of the load balancer receiving client traffic.  However there's no more Istio ingress pods on that node to handle such client traffic.  Essentially that means the load balancer is routing the client traffic into a black hole.  And that's some kind of down time that we cannot tolerate.  Therefore for the Istio pool upgrade we kinda have to de-register the backing nodes from the load balancer and then coordinate and drain the Istio gateway pods over to the new pools.

    We are able to automate the entire blue-green upgrade procedures using the Pulumi Automation API.  We built some custom toolings around this API that allows us to add it and apply the Pulumi stacks according to the upgrade steps that I just described.  And we proceed one step at a time with some pre-imposed condition checks in between the steps to make sure that the steps are healthy and executed correctly.  And unlike other infrastructure's code systems Pulumi requires no DSL.  It expose the full flash firm language distractions directly to the user which is so powerful when we are trying to integrate with additional custom toolings and orchestration systems.

    The bottom line is that declarative infrastructure is insufficient to solve life cycle management.  Invest in a tool that allows orchestration.  And automation and orchestration are so important to sustain at the scale that we operate.  Another tool that we built around Pulumi is to solve the cloud-specific Kubernetes manifests issue.  Our application users need to customize their Kubernetes manifests to be able to run on multiple clusters or clouds.

    The reason is that the Container image hosts with the load balancer labels with a pod identity annotations are usually different across clouds.  The problem is that we were managing Kubernetes manifests outside of Pulumi.  The reason is mostly because A, most open source projects that we use only released an installation yaml.  And is non trivial work to translate that to the Pulumi set up.  And second the cluster stays almost always digress from infrastructure as code sets because of the dynamic nature of the cluster due to reasons like different controllers or a horizontal pod out of scale.

    And lastly we run the multi-tenant platform where we want our users to self manage their own Kubernetes manifests.  We don't want to be the bottom act where we have to approve every configuration changes related to applications.  But we also don't want to grant all the users equivalent access to Pulumi's and our configuration platforms.  Given the fact that we're building the Kubernetes manifest outside of Pulumi the clusters specific values are still stored in Pulumi because the cloud resources in the cluster itself is provisioned by Pulumi.  So we need to build a tool that allows us to generate those Kubernetes manifests, customize given the cloud's specific values.

    And that's why we built Overlaymgr, a yaml rendering engine.  The Overlaymgr will read the Pulumi stack outputs using the API and generating the overlays that feeds into Kustomize, which renders the final Kubernetes manifests that was applied by ArgoCD.  In the cloud native community we also saw alternative solution such as using the DSL.  Doing so still needs the input data from that framework to manage the Kubernetes configuration.  The infrastructure provisioning tool.

    Some of the examples of this DSL approach includes isopod or cue.  The bottom line is that your infrastructure provisioner is either your metadata store or orchestra by a metadata store where the store must be queryable.  In addition to Kubernetes and in cloud resources we also use Pulumi to provision and manage Vault deployments.  Vault or HashiCorp Vault is a critical piece in our secret net service and also private EKI.  We use Pulumi to initialize and configure Vault.

    For example we use Vault to issue and rotate the issue in Casert for Cert Manager.  And Cert Manager or assigned the TLS cert used to terminate our private HTTPS traffic.  We also replicates data secrets cross deployments and regions using Pulumi to orchestrate this.  And lastly we enabled the cloud providers secret engine so that clients or applications can obtain from vault short lived tokens to talk to cloud providers instead of having to store long lived data tokens which is less secure.  The tenant onboarding is outside of Pulumi.

    Recall our platform is multi-tenant so we implemented this Vault policy custom resource definition where the platform user can define this vault policy so that they combined a list of Vault paths to a specific Kubernetes service account.  And their applications could just use such service account when interacting with the Vault that's deployed in a cluster.  An example of such Vault policy is showing on the right hand side.  My team has made some progress with multi-cloud, but some open questions remain.  For example applications still have to be cloud aware.

    They need to use cloud specific client libraries to interact with cloud services and requiring code changes for each cloud providers we want to support.  For example if the application needs to read a file from the Blob Storage bucket or write to a message cue or pop sub topic, path identity that translates a Kubernetes service account into a cloud service account only solves the authorization and authentication problems.  The CRD's that we described earlier only resolves the resource provisioning aspect, hence the interaction between the applications and the cloud providers remain cloud specific.  Essentially you have to write the same code many times and ones for each cloud providers.  And secondly cloud agnostic abstractions often terminates at Kubernetes.

    Cloud resources and policies that cannot bet pushed up remains heterogeneous across clouds.  One example is when we used Cert Manager and acme protocols to automatically renew our cluster public certificates that terminates the public HTTPS traffic.  In order to solve the acme DNS oh one challenge we have to make some DNS tax record.  So we want to reduce the cloud DNS permissions for Cert Manager to only making tax records.  However we could not do so on GCP at least because there's no record lever permission control.

    And the IM boundary is the entire GCP project.  So essentially we have to configure the permissions and security boundary controls per cloud.  And this is the end of my talk.  Thank you so much for being with me for the past 20 minutes.  And if you are also excited about multi-cloud and distributive systems, continued platforms, and open-source software, my team is hiring aggressively. And please scan the QR code on the left and get in touch with us.  Thank you so much.
---
