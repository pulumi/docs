---
title: "Future of the Cloud: 10 Trends Shaping 2024 and Beyond"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2023-12-19T15:56:40Z

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: "The year of Cloud Optimization is here! Explore the top 10 trends, including IaC, AI/ML, Kubernetes, platform engineering, security, FinOps, data, and more."

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: cloud-computing-forecast-2024.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - sara-huddleston
# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - ai
    - cloud-native
    - iac
    - cloud-computing
    - multi-cloud
    - forecast
    - devops

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

In 2024, several trends will dominate cloud computing, driving innovation, efficiency, and scalability. From Infrastructure as Code (IaC) to AI/ML, platform engineering to multi-cloud and hybrid strategies, and security practices, let's explore the 10 biggest emerging trends.

<!--more-->

## 1. Cloud Will Become a Business Necessity by 2028

According to [Gartner](https://www.gartner.com/en/newsroom/press-releases/2023-11-29-gartner-says-cloud-will-become-a-business-necessity-by-2028), cloud adoption will move from being a technology disruptor to a necessity for maintaining business competitiveness. In 2024, worldwide end-user spending on public cloud services is forecast to total $679 billion and is projected to **exceed $1 trillion in 2027**.

{{< figure alt="The future of cloud computing. Credit: Gartner" src="https://media.licdn.com/dms/image/D4E12AQElUBX5yuTQKA/article-inline_image-shrink_1500_2232/0/1701900870466?e=1708560000&v=beta&t=kuCJujRb-C3eeP7u4hGnXmy2DQrY1YYUzEI4ed9P-P0" caption="The future of cloud computing. Credit: Gartner" width=100% >}}

According to McKinsey & Company's "[In search of cloud value](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/in-search-of-cloud-value-can-generative-ai-transform-cloud-roi)" report:

- Cloud enables businesses to innovate, which is worth more than x5 what is possible by simply reducing costs.
- The anticipated increase in EBITDA (Earnings Before Interest, Taxes, Depreciation, and Amortization) attributable to cloud adoption is projected to range between 20% and 30% by the year 2030 - but it's expected to vary across different sectors.
- Asian companies have the most to gain from the cloud, with $1.2 trillion in EBITDA. American institutions stand to capture about $1.1 trillion in cloud value, while European institutions are at $773 billion due to regulatory constraints.
- Companies that have captured the most ROI consistently do 3 things well: 1/ work closely with business leaders to focus on high-value business cases, 2/ build a robust cloud foundation, and 3/ adopt a product-oriented operating model.

## 2. Large Organizations with Multi-Cloud and Hybrid Environments

Multi-cloud and Hybrid (mixing cloud and on-premise infrastructure) environments are a trend that is here to stay. According to Forbes, by **2024, 85% of large-sized companies will have a multi-cloud strategy**. Organizations recognize the importance of leveraging multiple cloud providers and on-premises infrastructure to optimize performance, enhance redundancy, and mitigate risks.

{{< figure alt="Why organizations are using multiple clouds chart. Credit: Cisco Systems" src="https://media.licdn.com/dms/image/D4E12AQEs9JuY5rKdGg/article-inline_image-shrink_1500_2232/0/1701900695659?e=1708560000&v=beta&t=Dvt6x86Vb5yqtpWviHwxn5Vraq30UlbcA-AfRXyzytU" caption="Credit: Cisco Systems" width=100% >}}

The following trends also relate to this multi-cloud and hybrid approach as companies seek ways to balance flexibility and cost while increasing overall productivity with security and compliance in mind.

## 3. Infrastructure as Code (IaC) Crucial for Scalability

IaC in general-purpose languages is gaining prominence as organizations seek to automate and streamline their infrastructure management processes and reduce the divide between application development and cloud infrastructure development.

[Infrastructure as Code](https://www.pulumi.com/what-is/what-is-infrastructure-as-code/) is maturing beyond taming the complexity of the cloud:

- Facilitating the adoption and configuration standardization of multi-cloud and hybrid strategies
- Better integration with multiple cloud providers, like [AWS](https://www.pulumi.com/docs/clouds/aws/), [Azure](https://www.pulumi.com/docs/clouds/azure/), and [Google Cloud](https://www.pulumi.com/docs/clouds/gcp/), data stores, and third-party services like [Cockroach Labs db](https://www.pulumi.com/registry/packages/cockroach/), [Confluent cloud](https://www.pulumi.com/registry/packages/confluentcloud/), [Kafka](https://www.pulumi.com/registry/packages/kafka/), and more.
- Deeper validation on parameters that people are passing in, checking all critical components, ensuring they are configured correctly before deployment
- More [efficient resource management](https://www.pulumi.com/docs/pulumi-cloud/insights/)
- Robust security and [Policy as Code](https://www.pulumi.com/docs/using-pulumi/crossguard/core-concepts/) to enforce security practices, guardrails, compliance, cost policies, and more
- Intelligent automation, including [automated tests](https://www.pulumi.com/docs/using-pulumi/testing/) and [remediation policies](https://www.pulumi.com/blog/remediation-policies/)
- [AI-driven automation and insights](https://www.pulumi.com/blog/pulumi-insights/)

## 4. Rise of Security-First (DevSecOps)

Security is no longer a separate consideration but a top priority in the cloud landscape - **integrating security into the DevOps process, known as DevSecOps, will be a key trend in 2024**. Organizations will emphasize building security measures in every development lifecycle stage. [Policy as Code](https://www.pulumi.com/crossguard/) will be an indispensable pillar in many security aspects:

- Use off-the-shelf rules or define your best practices for security, cost, compliance, and reliability
- Maintain security across all cloud infrastructure assets
- Ensure cost-conscious deployments requiring specific cost allocation tags.
- Catch policy violations before they escape using CI/CD.
- Automate governance using programmable libraries and REST APIs, easily integrating with external services such as web services, asset tracking databases, pricing lists, and more.

{{< figure alt="A live dashboard of organizational violations in Pulumi Cloud." src="https://www.pulumi.com/images/screens/pac-in-action.png" caption="A live dashboard of organizational violations in Pulumi Cloud. Credit: Pulumi" width=100% >}}

## 5. Platform Engineering – Internal Developer Portals (IDP) for Better Developer Experience

**By 2026, 80% of large software engineering organizations will establish platform engineering teams** as internal providers of reusable services, components, and tools for application delivery. Platform engineering will ultimately solve the central problem of cooperation between software developers and operators (source: [Gartner](https://www.gartner.com/en/articles/what-is-platform-engineering)).

Mid-size to large companies will begin or [continue to invest in implementing platform engineering practices](https://www.pulumi.com/product/internal-developer-platforms/), with large tech companies as first adopters. They will provide [Internal Developer Portals (IDP)](https://www.pulumi.com/blog/building-developer-portals/) to elevate the Developer Experience (DX, sometimes referred to as DE or DevEx), helping them work faster, like abstracting the complexities of configuring, testing, and validation, deploying infrastructure, and scanning their code for security.

{{< figure alt="Internal developer platform-in-a-box. Credit: Pulumi" src="https://www.pulumi.com/blog/developer-portal-platform-teams/platform-teams.png" caption="Internal developer platform-in-a-box. Credit: Pulumi" width=100% >}}

## 6. AI/ML Continues to Rise

Many AI-based systems are built around cloud-native tools, practices, and managed services. The extensive use of cloud-native primitives means that AI is fundamentally a cloud adoption story, and Cloud and AI are consequently interconnected.

[Artificial Intelligence (AI) and Machine Learning (ML)](https://www.pulumi.com/blog/tag/ml/) applications will continue to drive innovation across various industries. This trend will increase the focus on machine learning algorithms, data collection, and preprocessing, inference and deployment.

{{< youtube "i09F14yc0l4?rel=0" >}}

**By 2027, AI will dramatically increase developer velocity by automatically generating code** to meet functional business requirements for 70% of new digital solutions in production (source: [IDC](https://www.digitalnewsasia.com/business/idc-reveals-its-top-predictions-cloud-2023-and-beyond)). Despite the concerns regarding AI and job security, AI job posts on the global work marketplace Upwork increased more than 1,000% in the second quarter of 2023 compared to the same period last year, showing a significant increase in new employment opportunities related to AI and ML.

In fact, [BizReport](https://www.bizreport.com/business/ai-influence-on-us-workforce-salaries) estimates that **by 2024, there will be an additional 131,000 AI-related jobs within computer science**. This figure currently stands at 30.3% of roles, supporting the [World Economic Forum’s prediction](https://www.weforum.org/press/2020/10/recession-and-automation-changes-our-future-of-work-but-there-are-jobs-coming-report-says-52c5162fce/) that **by 2025, 97 million new jobs will have been established thanks to AI**.

## 7. Investment in Data and Data Streaming

Data streaming is a buzzword set to go up in the maturity curve:

- **Data Sharing for faster innovation.** Collaboration within and beyond organizational boundaries is facilitated through data sharing, utilizing streaming protocols like Kafka, APIs like REST/HTTP, and adhering to open standards like AsyncAPI.
- **Data Contracts** for better data governance include enforcing policies for structure, integrity constraints, metadata, rules, and other specifications.
- **Serverless Stream Processing** will make building scalable and elastic streaming apps easier. The focus shifts towards deriving business value by leveraging a fully managed, integrated, and secure infrastructure.
- **Multi-Cloud Deployments** for cost-efficient delivery value, addressing the need for seamless data movement across cloud providers, organizations invest in data bridge creation, migrations, and disaster recovery solutions.
- **Reliable Generative AI**. This encompasses activities such as model training, real-time model scoring, and integration with third-party services, such as GenAI LLMs or Software as a Service (SaaS) offerings, to enhance the capabilities of artificial intelligence.

Event streaming technology can be transformative but often difficult to adopt. Watch Collin James, Engineering Leader and Software Architect at Dutchie, describe how [a small team has enabled Kafka adoption by creating a monorepo of Pulumi projects](https://www.pulumi.com/resources/enabling-kafka-adoption-pulumi-and-confluent-cloud/) that manage resources on Confluent Cloud.

## 8. Kubernetes Dominance and Increased Complexity

Kubernetes, the open-source container orchestration platform, will continue its ascent in 2024. According to [Markets N Research](https://marketsnresearch.com/report/1649/global-kubernetes-market), the global Kubernetes market size was valued at USD 1.8 billion in 2022 and is projected to be **USD 7.8 billion by 2030, exhibiting a CAGR of 23.40%** during the forecast period.

The "growing pains" will also increase with rising concerns in security, networking, deployment, scalability, cost, and impact on developer productivity. Read the previous LinkedIn Newsletter article [From Complexity to Simplicity: Streamlining Kubernetes with Infrastructure as Code](https://www.linkedin.com/pulse/from-complexity-simplicity-streamlining-kubernetes-infrastructure?lipi=urn%3Ali%3Apage%3Ad_flagship3_pulse_read%3BHF6x7jyoRWSmk9POeHy0TA%3D%3D).

## 9. Cost Transparency and Governance

As cloud environments become more complex, ensuring cost transparency and governance will be a priority. In 2024, businesses will invest in Cloud Optimization and/or cost management tools and processes to monitor and control cloud spending effectively. This includes implementing policies, [managing resource allocation](https://www.pulumi.com/blog/property-search/), and utilizing cost analytics to make informed decisions about resource utilization.

As a result, [IDC](https://www.netapp.com/media/93564-operationalize-fin-ops-for-continuous-cloud-and-cost-efficiency.pdf) predicts that complexities and IT budget pressures will drive **70% of Global 1000 companies to [increase FinOps maturity](https://www.pulumi.com/blog/finops-with-pulumi/)** with granular chargebacks, benchmarking, and multiple-cloud optimization by 2024.

## 10. Talent Shortage

Over 150,000 technology industry workers have been laid off in the US since the beginning of 2023, and yet the Korn Ferry report finds that **by 2030, more than 6 million jobs could go unfilled** because there aren't enough skilled people to take them.

Previous research by [McKinsey Global Institute](https://www.mckinsey.com/featured-insights/future-of-work/jobs-lost-jobs-gained-what-the-future-of-work-will-mean-for-jobs-skills-and-wages) has shown that **as many as 375 million tech workers globally might have to change occupations** and skills in the next decade to meet companies' needs and that automation could free employees to spend as much as 30% of their time on new work-acquiring new work experience.

{{< figure alt="AI Influence on US workforce salaries Credit: Bizreport" src="./Bizreport.png" caption="AI Influence on US workforce salaries Credit: Bizreport" width=100% >}}

The skill gaps have appeared in many of the previously stated trends. For organizations, it means that they need to look closer at their existing knowledge and prioritize skill-building, reskilling, and upskilling efforts. These programs face other obstacles, most at the cultural level.

Since 72% of US companies struggle to find tech talent, now’s a great time to upskill for the cloud. [Check out our upcoming workshops](https://www.pulumi.com/resources/#upcoming) - topics range from introduction level to IaC, taking AI apps to production, and more.

## Keeping up with the Future Cloud Trends

From advanced technologies like AI/ML and Kubernetes to practices like FinOps and Security, the cloud of 2024 is set to redefine best practices for enhanced efficiency, security, and scalability. You may have noticed that many trends overlap, and a holistic view will be crucial for organizations aiming to stay ahead.
