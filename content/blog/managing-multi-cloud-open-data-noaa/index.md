---
title: "Managing NOAA Open Data across Multiple Clouds with Pulumi"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2022-11-08T21:01:21Z

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
# Max length is 160 characters.
meta_desc: Learn how the North Carolina Institute for Climate Studies manages open
  data for the NOAA on multiple clouds using Pulumi.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
  - denis-willett

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
  - aws
  - azure
  - google-cloud
  - python
  - guest-post
  - infrastructure-as-code
  - community

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
search:
  keywords:
    - NOAA
    - Python
    - multi-cloud infrastructure
    - open data
    - infrastructure as code
---

> Denis Willett is a software engineer at the [North Carolina Institute of Climate Studies](https://ncics.org) who works on the NOAA Open Data Dissemination Program. His work focuses on leveraging cloud technologies for the development of data processing and machine learning pipelines. Denis did his PhD in Entomology and Nematology at University of Florida and his undergraduate and masters work in Earth Systems at Stanford University. You can read his full bio [here](https://ncics.org/people/denis-willet-2/).

[NOAA Open Data Dissemination (NODD)](https://www.noaa.gov/information-technology/open-data-dissemination) makes environmental data freely and publicly accessible across Amazon Web Services (AWS), Microsoft Azure (Azure), and Google Cloud Platform (GCP). These data include near real-time satellite imagery, weather models, radar feeds, drought information, ocean databases, and a suite of climate data records among many others. This program supports more than 220 datasets and over 24PB of open data. Since its inception, the program has been growing rapidly, almost doubling in size over the past year.

<!--more-->

Availability of the petabyte scale environmental data on the cloud is only one aspect of NODD. The program places a premium of performant data delivery and access. NODD data pipelines provide resilient and  low, in many cases near real-time, latencies to NOAA’s core data offerings. In addition, NODD provides performant, parallel access to these data supporting billions of requests per day and accessions of individual datasets exceeding 1PB in a single day.

To support this program, the North Carolina Institute for Climate Studies (NCICS) through the Cooperative Institute for Satellite Earth System Studies (CISESS) engineers infrastructure on all three major public clouds ranging from object stores to messaging platforms, data ingest and transformation pipelines, and monitoring systems. These systems are deployed and managed by a very small team that, by necessity, must be agile, resilient and facilitate low latency data transfers at petabyte scale.  Given the scale and diversity of resources managed through this initiative, we began looking for tools to facilitate multi-cloud management using [infrastructure as code (IAC)](/what-is/what-is-infrastructure-as-code).

## Before Pulumi

Prior to beginning to transition to Pulumi, our team built infrastructure primarily using the Command Line Interface (CLIs) and consoles of each cloud service provider. While this worked well, it required extensive Cloud Service Partner (CSP) specific training to be able to not only navigate the nuances of each provider’s offerings, but also the unique interface to deploy resources. Changing and updating infrastructure in this manner resulted in long development cycles where upgrades were mostly manual and composed of repetitive tasks.

Because of the manual nature of these deployments across three different cloud service providers, infrastructure began to sprawl. A clear snapshot of what resources were deployed where became difficult to compile and management of legacy and deprecated systems depended on manual intervention for clean-up. Infrastructure also began to drift. What started as uniform deployment of resources across multiple cloud platforms morphed as manual updates to each instance resulted in unique environments that were hard to replicate if they had to be deleted and redeployed.

As an example, our program relies on Apache NiFi deployments on AWS, GCP, and Azure to coordinate and manage petabyte scale data transfers while managing data provenance. Drift in these deployments makes it especially difficult to redeploy identical configurations (even though we were using Ansible and Containerization) if they go down.

An additional consequence of this approach is knowledge silos. The team member who deployed a group of resources on AWS had trouble (even with extensive documentation) communicating reusable architectures to another team member who was working on similar situations in Azure. While there are obvious nuances relevant to each cloud environment, our need to replicate similar infrastructure in a multi-cloud environment at scale necessitated extensive detailed communication in a team environment.  Questions like: “What is the ARN of the most recent version of this service?” and “What queues do we have on GCP?” required communication and time taken by the individual responsible to answer those questions.

## How and why we chose Pulumi

As our team grew and our platform scaled (more than doubling in storage size over the past year by more than 10PB), we began to explore tooling to help us better navigate and manage our multi-cloud and multi-account environment. The nature of the NOAA Open Data Dissemination program agreements with each cloud service provider (CSP) meant that we had multiple accounts with different permissions, funding, and configuration on each CSP, resulting in flexible options.

We began looking at infrastructure as code (IAC) solutions and initially considered many of the cloud-specific options: CloudFormation on AWS, Deployment Manager on Google, and Resource Manager on Azure. While these were nice for automation, we quickly discarded these as options because each had an individual learning curve for that environment; they did not translate well in a multi-cloud environment. These tools also did not have the control features of a full-fledged programming language; looping and if-then statements were challenging to implement.

We also considered other Infrastructure as Code providers. While these solutions would meet a lot of our needs, and one of our team members had extensive experience with one of these  tools, the ability to use a common tool seamlessly in a multi-cloud environment was attractive. However, the learning curve associated with a domain specific language was cause for reticence.  In addition, we really wanted to be able to use the features of a full-fledged programming language.

After experimenting with a few IAC options, our research institute began using Pulumi in late 2021 and immediately began implementing it to expand our infrastructure.

## Benefits of using Pulumi for multi-cloud infrastructure as code

Pulumi had all the benefits we were looking for in a multi-cloud infrastructure as code platform. In terms of automation, manual checklists could be converted to code reducing both deployment time and human errors in deployment. This automation with infrastructure as code (and accompanying state management) allowed us to adopt an immutable infrastructure paradigm where old resources are replaced with new updated infrastructure. While these benefits are accessible via other IAC tools, we particularly appreciated the Pulumi interface to be able to quickly access and inspect infrastructure deployments.

We saw immediate wins for our teams in the following areas:

- Drift was eliminated. Single source of truth, version controlled (and tagged) code documented exactly what was deployed where. When updates were needed, the code was updated and redeployed without manually tweaking individual resources through the console.
- Management of legacy and deprecated resources were obviated. With IAC managed deployment that would automatically clean up old resources, we saved many future hours cleaning up unused cloud resources.
- Team collaboration was enhanced. With a single source of truth and a visual snapshot of resources and deployments, the number of ‘What was the ARN of that resource again?” type questions dropped considerably. Team members could simply look at the deployment in one location and see all of the resources across all three major clouds. This type of friction-reduction really enhances team productivity.

In addition to these IAC benefits, we saw a number of key advantages in implementing Pulumi. First and foremost was the ability to use full-featured programming languages to deploy IAC solutions in a multi-cloud environment. This not only allowed us to fully take advantage of programming control structures (e.g., need 100 different rules on AWS? Now you do not have to manually script each one, just put it in a loop), but also flattened the learning curve for adoption. Our team already used Python extensively in our day-to-day work. Adopting Pulumi was almost as simple as importing a package. Accessing Pulumi through Python made it much easier to embrace.

This accessibility through Python also meant that learning how to create, deploy, and share reusable templates was trivial as all team members already knew how to build, share, and import modules in Python. The ability to rapidly share these templates accelerated our development and allowed for standardization around best practices. For example, we use serverless capabilities on all three CSPs. Once we had a template for deploying our function as a service (FAAS) code on one platform, we did not have to reinvent the wheel or remember to go through a checklist; it was as simple as importing our internal FAAS module and pointing it to the correct code to deploy.

## Next steps

Pulumi has become an automation and collaboration tool that is accelerating our ability to provide petabyte scale data to the public in a multi-cloud environment. As we continue to scale our program, Pulumi is allowing us to leverage a small team to manage increasingly larger, more complex deployments in a dynamic environment. In addition, it is rapidly becoming a key player in a cross-cloud fabric that we are building to facilitate working across multiple platforms. By providing a similar, intuitive interface through our language of choice, Python, it is allowing us to more quickly adapt and reproducibly deploy infrastructure across AWS, Azure, and GCP.

Please reach out to us with your thoughts, reactions, and comments at [NODD@NOAA.GOV](mailto:NODD@NOAA.GOV).
