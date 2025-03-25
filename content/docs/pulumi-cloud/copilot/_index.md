---
title_tag: "Pulumi Copilot"
meta_desc: Learn about Pulumi Copilot, a new conversational chat interface integrated
  throughout Pulumi Cloud.
title: Pulumi Copilot
h1: Pulumi Copilot Overview
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Pulumi Copilot
    parent: cloud-home
    weight: 5
    identifier: pulumi-cloud-copilot
aliases:
  - /docs/intro/copilot/
  - /docs/intro/pulumi-cloud/copilot/
search:
  keywords:
    - copilot
    - conversational
    - chat
    - integrated
    - interface
    - learn
    - cloud
---

Pulumi Copilot is a new conversational chat interface integrated throughout Pulumi Cloud, enabling Pulumi Cloud users to quickly accomplish a variety of cloud infrastructure management tasks by leveraging the combination of generative AI and the rich capabilities of Pulumi Cloud.

![Copilot](/images/docs/reference/service/copilot.png)

Through Pulumi Copilot, you can explore your cloud infrastructure and gain insights across an incredible breadth of use cases, including:

![Copilot use cases](/images/docs/reference/service/copilot-use-cases.png)

Pulumi Copilot enables these use cases via the following:

#### Access any data in Pulumi Cloud

* The state of every resource you are managing with Pulumi across _any_ Cloud, _any_ account, and _any_ region.  With [Pulumi Insights'](https://www.pulumi.com/blog/pulumi-insights/) Cloud Supergraph support for 160+ cloud providers, this offers an unprecedented breadth of cloud infrastructure data to explore and interrogate with Pulumi Copilot.
* Pulumi stacks, projects, updates, deployments, environments, policies, audit logs and more - enabling historical understanding of what happened when, by who, and why across all of your cloud engineering systems managed by Pulumi.

#### Pulumi IaC Authoring and Deployment

* The same great Pulumi AI features for authoring IaC are now available inside Pulumi Copilot as well, enabling you to quickly solve new IaC problems within Pulumi Cloud, and even deploy code directly from Pulumi Copilot.

#### Access cloud metadata from the clouds themselves

* Through the use of new skills, Pulumi Copilot can access cloud metadata in real time in AWS, Azure, Kubernetes, and more, allowing it to join Pulumi’s IaC world view with information about usage, costs, and more – as well as infrastructure not yet under the management of Pulumi.

#### Customization via system prompts

* System Prompts allow organization administrators to set default preferences and guidelines for Pulumi Copilot. By configuring these prompts, you can tailor Pulumi Copilot’s behavior to better suit your team’s needs and policies.

## Frequently Asked Questions

### What model does Pulumi Copilot use?

Pulumi Copilot currently uses OpenAI GPT-4o, hosted in Azure OpenAI Service in a Pulumi owned and managed Azure subscription. Over time we expect to use a combination of models to improve the user experience and answer quality.

### Will my data be used to train Pulumi Copilot?

We are not using either a self-fine tuned model or a fine tuning product, therefore today data is not being used to train Pulumi Copilot.

### How does Copilot handle user identities and access permissions?

Pulumi Copilot leverages Pulumi Cloud’s Role Based Access Control model, therefore it only has access to the data that the user using it has access to. Behind the scenes, Pulumi Copilot is making API calls on the user's behalf, meaning it does not expose information the user has no access to.

### Can Copilot also make changes or is it limited to read-only scenarios?

At this time Pulumi Copilot can only perform read operations, such as making GET requests on the user's behalf. If you ask Pulumi Copilot to perform an action, such as making a member an admin, it will confirm it is not able to.

In the near future we plan to expand Copilot functionality to perform actions on your behalf, with confirmation actions to ensure you are aware of the steps it is taking. Controls will be available to disable read-write capabilities at the organization level.

### What data do we send to Azure OpenAI API?

Pulumi Copilot transmits data to Pulumi’s Azure tenant to generate responses, including both contextual data and data about the user’s actions. The transmitted data is encrypted both in transit and at rest; Pulumi Copilot-related data is encrypted in transit using transport layer security (TLS).

### Are my secrets exposed to Pulumi Copilot or third parties?

No. Pulumi Copilot does not have the ability to decrypt [secrets](/docs/concepts/secrets/). Therefore, no secret data is exposed to either users or the Pulumi’s Azure tenant by Pulumi Copilot.

### What data is Pulumi Copilot storing?

We store conversation data, similar to all other product metrics logging in Pulumi Cloud, including the response from Azure’s OpenAI API in order to debug issues and measure model quality. This data is treated sensitively and used only for operational purposes.

### Can I turn Pulumi Copilot off for my organization?

Pulumi Copilot is off by default at public beta launch. Organization admins can turn it on by navigating to organization __Settings > Access Management > Pulumi Copilot__. You can make it available for all members, just admins or no one in your organization. It can be turned off at any point.

### How do I use organization system prompts?

1. Log in to Pulumi Cloud and navigate to your organization’s settings in the left hand navigation.
2. Under the settings menu, select "Access Management".
3. In the Copilot section, you’ll find the edit box titled "Organization system prompts".

The best way to author the prompts is to specify your organization's rules and preferences in a conversational style. For example, if you want Copilot to generate code in Python, you can write it like this:

`Our organization prefers Python.`

You can add other prompts to specify the default cloud provider, compliance guidelines and so on.

### How can I report bugs or provide feedback about Pulumi Copilot?

You can respond “/bug” in the chat and it will be logged to provide us feedback on response quality.
