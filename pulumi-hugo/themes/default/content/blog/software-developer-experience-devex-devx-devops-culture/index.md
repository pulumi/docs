---
title: "Beyond Productivity: Developer Experience is Business Critical"
allow_long_title: true

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2024-02-20T20:47:44Z

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Improving developer experience does more than increase productivity and efficiency. It is crucial for business success. Here's what you need to know.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: developer-experience-devex-business-value-business-critical.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - sara-huddleston

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - developer-experience-devex
    - devops
    - platform-engineering
    - developer-portals
    - software-development

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

"Developer experience is hard to sell," said Cleve Littlefield, Engineering Manager at Pulumi, during a casual meeting. With experience as both an end-user developer and a lead in self-service platform implementation, Cleve's observation stuck with me.

Though I have expertise in leading implementations and upgrades for internal platforms, none were specifically for developers. However, experience remains vital across departments, addressing tools, processes, systems, and best practices, aiming to reduce cognitive load, increase productivity, enhance collaboration, boost communication and much more. 

Intriguingly, engineering teams may perceive its value differently. Therefore, we will dive into the concept of developer experience, aka DevEx, which, in truth, should translate into a competitive advantage.

<!--more-->

## In this DevEx article

- [What is developer experience?](/blog/software-developer-experience-devex-devx-devops-culture/#what-is-developer=experience)
- [Is developer experience important?](/blog/software-developer-experience-devex-devx-devops-culture/#is-developer-experience-important) (Spoiler alert: it's business-critical)
- [The GitHub developer experience (DevEx) formula](/blog/software-developer-experience-devex-devx-devops-culture/#the-github-developer-experience-devex-formula)
- [What does a great developer experience look like?](/blog/software-developer-experience-devex-devx-devops-culture/#what-does-a-great-developer-experience-look-like)
- [How does DevEx intersect with DevOps?](/blog/software-developer-experience-devex-devx-devops-culture/#how-does-devex-intersect-with-devops)
- [Organizational culture is a predictor of outcome success](/blog/software-developer-experience-devex-devx-devops-culture/#organizational-culture-is-a-predictor-of-outcome-success)
- [How do you implement a great developer experience?](/blog/software-developer-experience-devex-devx-devops-culture/#how-do-you-implement-a-great-developer-experience)
- [What DevEx is not](/blog/software-developer-experience-devex-devx-devops-culture/#what-devex-is-not)
- [Frequently asked questions](/blog/software-developer-experience-devex-devx-devops-culture/#frequently-asked-questions)

## What is developer experience

Developer experience (DevEx), also referred to as DevX or DX, encompasses systems, technology, processes, and culture that collectively impact the effectiveness of software development. It looks at all components of a developer's ecosystem—from environment to workflows to tools—and evaluates how they contribute to developer productivity, satisfaction, and operational impact.

Developer experience revolves around the ease or difficulty of executing essential tasks. **A positive developer experience means those tasks are relatively easy to perform, translating into higher performance.**

The quality of the experience is equally vital for developers building and managing internal software as it is for those involved in developing customer-facing software products.

## Is developer experience important

It is not just important. **It's business critical.** If your company is in the business of creating and selling software or relies on critical internal software, developers are vital internal stakeholders to your business foundation.

Greg Mondello, director of product at GitHub, said, "In most contexts, software development capacity is the limiting factor for innovation. Therefore, improvements to the effectiveness of software development are inherently valuable [...] companies with better DevEx outperform their competitors, regardless of vertical."

{{< figure alt="Platform Engineering Forrester Opportunity Snapshot - DevEx impacts overall business performance. Credit: Humanitec" src="/blog/software-developer-experience-devex-devx-devops-culture/what-impact-are-you-experiencing-resulting-of-improving-developer-experience.jpg" width=70%  caption="Platform Engineering Forrester Opportunity Snapshot - DevEx impacts overall business performance. Credit: Humanitec" >}}

As per [McKinsey's report](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/tech-forward/why-your-it-organization-should-prioritize-developer-experience), an enhanced developer experience (DevEx) can yield significant advantages for organizations, including enhanced talent hiring and retention, improved security, and increased developer productivity- this makes DevEx important for all companies, not just tech.

A positive developer experience can yield numerous business advantages, which can include:

1. **Improvement in collaboration across departments**
2. **Higher attraction and retention top talent**
3. **Increase developer productivity and developer velocity**
4. **Reduction in operational costs**
5. **Accelerate time-to-market**
6. **Support innovation**
7. **Elevate customer attraction and retention**
8. **Increase bottom line through revenue growth**

To this end, let's look into what goes into developer experience and how to achieve it.

## The GitHub developer experience (DevEx) formula

GitHub's DevEx formula takes into consideration the following:

- Productivity: The speed and simplicity of implementing changes to a codebase
- Impact: The seamless transition from idea to production without obstacles
- Satisfaction: The environment, workflows, and tools influence developer happiness

Optimizing DevEx involves fostering a collaborative environment where developers can be most productive, impactful, and satisfied.

{{< figure alt="DevEx formula. Credit: GitHub" src="/blog/software-developer-experience-devex-devx-devops-culture/github-developer-experience-formula.png" width=100%  caption="DevEx formula. Credit: GitHub" >}}

Noah Gift, the founder of Pragmatic AI Labs and a professor at Duke University specializing in machine learning, MLOps, AI, data science, and cloud architecture, noted that with the right platform, there could be:

- A 75% increase in productivity
- A sustained 22% productivity increase three years later
- An 80% reduction in onboarding time

Merely having skilled developers is insufficient. Developers also require the appropriate tools and processes to excel in their work. Top-tier developers anticipate the availability of such resources, influencing the hiring and retention of talent.

## What does a great developer experience look like

Engineering teams that have good developer experiences are more productive and efficient. Great DevEx is often enabled by a platform where the end-users are the developers.

- Developer-first readily available [internal developer platform](https://www.pulumi.com/product/internal-developer-platforms/), infrastructure, and development tooling, with well-organized and explicit documentation, including tutorials, demo environments, and curated learning paths.
- A unified hub for all developer requirements eliminates the need for developers to navigate through numerous tools, saving valuable time.
- Simplified workflows emerge when developers can swiftly select app patterns, such as API microservices or front-end journeys, and deploy them within minutes. This includes all-encompassing elements like environments, pre-integrated DevSecOps pipelines, monitoring, and fully automated change and release procedures.
- Centralized tracking of software, API, and infrastructure status and versions promotes asset transparency. A real-time view supports adherence to architectural standards, security controls, and patching status, with bots offering automatic suggestions for code enhancements related to issues.
- Integrated analytics and KPIs such as developer velocity, tech debt, error rate, mean time to recovery, and infrastructure cost can be automatically pulled by standard organizational tools, including backlog, pipeline, and monitoring tools.

{{< figure alt="Survey by GitHub on a typical experience for developers. Credit: GitHub" src="/blog/software-developer-experience-devex-devx-devops-culture/github-study-what-developers-spend-themost-time-on-daily.png" width=60%  caption="Survey by GitHub on a typical experience for developers. Credit: GitHub" >}}

Without the proper tools, progress may slow down the development process and hinder developer productivity. It becomes crucial to implement appropriate measures to avoid disruptions that could impact everyone involved, including the developers themselves. Although not often mentioned, [DevOps](https://www.pulumi.com/what-is/what-is-devops/) and [Platform Engineering](https://www.pulumi.com/what-is/what-is-platform-engineering/) also aim to enhance the developer experience and achieve the associated benefits.

## How does DevEx intersect with DevOps

DevOps is about developers and operations working together and sharing values, assumptions, and responsibility for the software they build and maintain.

According to Vilas Veeraraghavan, VP of Engineering at Truckstop, "Developer experience (DevEx) is the investment you make to enable solid DevOps practices, reduce developer burnout, and improve retention. The need for this investment is more pronounced as companies grow and the tech stack gets more diverse."

Watch Jowanza Joseph, Head of Engineering at StreamFT, below as he discusses how the right tool empowered developers, improved DevEx, reduced bottlenecks, increased productivity, and helped DevOps be a culture, a practice, not a person.

{{< youtube "I-GQ1xpyV0E?rel=0" >}}

Let's address a strong indicator of success or failure - culture.

Culture is not something you are—it's something you do. Software companies often focus on DevOps practices and culture, but all would benefit from adopting a DevOpsAll since the entire company should strive for the same thing. The diversity of perspectives, ideas, and insights can spark creativity and innovation and even ensure product-market alignment.

## Organizational culture is a predictor of outcome success

Why it matters? Organizational culture encompasses everyone, from the development team and operations to product management teams, sales, marketing, and more.

According to George Spafford, Senior Director Analyst at Gartner, "Infrastructure & Operations leaders embarking on DevOps initiatives and struggling to address organizational change and the value they will provide to the larger enterprise [...] people-related factors tend to be the greatest challenges — not technology."

According to a Harvard study encompassing 200 companies over 11 years, companies that focused on shaping their culture outperformed their competitors:

- Revenue growth was 4.1 times higher
- The stock price was 12.2 times higher
- [Net income](https://www.investopedia.com/terms/n/netincome.asp) was 756% vs. 1%
- [Return on investment (ROI)](https://www.investopedia.com/terms/r/returnoninvestment.asp) was 15 times higher

The driving force behind this exceptional financial performance is that engaged employees are prone to increased productivity, fostering superior innovation and more effective problem-solving.

{{< figure alt="Slide from a New York Atlassian Community Group presentation. Credit: Mark Cruth, principal modern work coach / advocate at Atlassian" src="/blog/software-developer-experience-devex-devx-devops-culture/employee-developer-experience-focus-areas.jpeg" width=80%  caption="Slide from Mark's New York Atlassian Community Group presentation. Credit: Mark Cruth, principal modern work coach/advocate at Atlassian" >}}

Based on decades of research on employee engagement, [Gallup has established that engaged employees consistently yield superior business outcomes compared to their counterparts](https://www.gallup.com/workplace/285674/improve-employee-engagement-workplace.aspx#ite-357638). This holds true across various industries, company sizes, and nationalities and remains consistent in prosperous and challenging economic conditions.

If it is not yet clear, then I will spell it out. Developer experience impacts employee engagement. A better developer experience can boost the engagement of the engineers and developers in the organization, and more engaged people are more likely to go the extra mile.

{{< figure alt="How developer experience supports better business outcomes. Credit: Swarmia" src="/blog/software-developer-experience-devex-devx-devops-culture/developer-experience-more-engaged-developers.png" width=100%  caption="How developer experience supports better business outcomes. Credit: Swarmia" >}}

If organizations invest in cultural values centered on human-first factors, then even the choices made in tools, processes, and systems will also be with the end-user in mind.

## How do you implement a great developer experience?

There isn't a bulletproof checklist, but there are several aspects to consider, and you can see the outline below. But first, you need to view the developers as the customers.

You will need to understand how developers work, the developer workflow, what the onboarding process looks like for a new developer, the developer teams' pain points, what developers love and hate about their day-to-day work, where they are spending most of their time, where they wish they spent most of their time, and so much more, that boils down to communication, and asking the right questions, and deep diving into analytics.

### Cultivate a DevOps culture

- **Shared responsibility**: Encourage a culture of shared responsibility where developers, operations, and other stakeholders work collaboratively
- **Continuous learning**: Promote a culture of continuous learning and improvement to adapt to evolving technologies and methodologies
- **Open communication**: Foster open communication channels to enhance collaboration and transparency among team members
- **Company-wide collaboration tools**: It's essential to encourage communication among developers and cross-functional teams to stimulate creativity, spark innovation, and enhance productivity and the speed of decision-making. Cross-functional collaboration contributes to successful business outcomes

### Define clear objectives

- **Alignment with business goals**: Ensure DevEx objectives align with business goals to drive meaningful outcomes
- **User-centric approach**: Prioritize user needs and feedback, shaping the DevEx strategy around the actual experiences of developers

### Leverage developer-first tools

- [**Internal developer portals (IDPs)**](https://www.pulumi.com/blog/building-developer-portals/): IDPs enable developers to quickly provision approved infrastructure, boosting productivity with pre-configured architectures, automated testing, and deployment adhering to organizational standards
- **CI pipelines**: usually, pipelines can be made faster and more unified. If they have a microservice architecture, they are likely duplicating pipeline code for every service
- [**Software development kits (SDKs)**](https://www.pulumi.com/docs/languages-sdks/): SDKs are integral components of a positive DevEx and provide developers with tools that facilitate crafting applications tailored to specific platforms or frameworks. Offering easy-to-access, well-designed, functional SDKs can make a meaningful difference in helping engineers quickly prototype ideas and refine their creations
- [**Infrastructure as code (IaC)**](https://www.pulumi.com/docs/pulumi-cloud/): Developers like to write code, particularly in their preferred programming language, provision infrastructure, ensuring consistency and reproducibility
- **Monitoring and observability**: Implement effective monitoring and observability tools (e.g., Prometheus, [New Relic](https://www.pulumi.com/resources/observability-as-code-with-new-relic/), Grafana) to gain insights into application performance and proactively address issues
- **Collaborative documentation platforms**: Use collaborative documentation platforms to document code, processes, and best practices, ensuring knowledge sharing and reducing onboarding friction

{{< figure alt="Platform Engineering Forrester Opportunity Snapshot - which of the following steps has your org take to improve the developer experience? Top 43% internal developer platform or platform engineering Credit: Humanitec" src="/blog/software-developer-experience-devex-devx-devops-culture/steps-to-improve-developer-experience.jpg" width=70%  caption="Platform Engineering Forrester Opportunity Snapshot - Which of the following steps organizations are taking to improve DevEx? Credit: Humanitec" >}}

### Prioritize developer-friendly workflows

- **Fast feedback loops**: Minimize feedback loops by integrating quick feedback mechanisms, allowing developers to identify and resolve issues early in the development cycle
- **Self-service environments**: Provide developers with self-service environments to facilitate experimentation, testing, and debugging without unnecessary dependencies on other teams
- **Version control best practices**: Enforce version control best practices to maintain a clean and organized codebase, allowing for easier collaboration and tracking of changes

### Continuous integration of feedback

- **Developer surveys**: Conduct regular surveys to gather feedback on the DevEx, ensuring continuous improvement based on real user experiences
- **Rapid iteration**: Encourage a culture of rapid iteration, where feedback is quickly incorporated into the development process to enhance the overall developer experience

### Measure and optimize

- **Key performance indicators (KPIs)**: Define and track key metrics such as deployment frequency, lead time, and mean time to recovery to measure the effectiveness of the DevEx strategy
- **Iterative optimization**: Continuously iterate and optimize DevEx based on performance metrics and user feedback

Implementing developer experience requires a holistic approach that blends cultural aspects with powerful DevOps and platform engineering tools. Watch Daniel Tao, Head of Engineering at [Atlassian](https://www.pulumi.com/case-studies/atlassian/), and Sven Peters, developer evangelist, discuss how to build a great developer experience through culture and an integrated approach to developer tools.

{{< youtube "xriRD7ugX20?si=LurTGLx1KfgRGIQZ&t=192?rel=0" >}}

## What DevEx is not

Now that DevEx has been defined let's address some common misconceptions about developer experience.

### DevEx is not the same as User Experience (UX)

Developer experience may sound similar to user experience (for developers), but it's different, although user experience is a component. For example, a platform engineer [building an internal developer platform](https://www.pulumi.com/blog/developer-portal-platform-teams/) must view the developers as their customers and create a good user experience by making it intuitive and easy to use.

### DevEx is not about enabling lazy developers

Part of the DevEx strategy is to retain talent. Companies that invest in DevEx don't do it to pamper developers. The true reason behind it is that they want their developers to stay "in the zone," also known as "deep work." When in this state, they are immersed in writing code and solving problems they enjoy working on, and their creativity is higher, it sparks innovative ideas, and the quality and speed of their output are also higher.

{{< youtube "NbhpII8DIKA?rel=0" >}}

### DevEx is not about implementing AI and cool tools

Technology impacts developer experience, [a robust generative AI tool can help create code faster](https://www.pulumi.com/ai), and internal developer platforms can help reduce cognitive load on developers. But again, tooling is only one aspect of it. Tools can't fix culture or replace processes. Many DevEx considerations should be considered to ensure that when the development teams adopt a tool, it addresses their pain points and enables developers.

### DevEx is not a one-person decision

DevEx should be a joint effort from the entire team. One needs to be aware of the issues to plan to fix them, so open communication and team collaboration are vital to developing and implementing a DevEx strategy, intersecting DevOps and platform engineering initiatives. Many large organizations already have DevEx teams or professionals with a bird's-eye view of what happens within the engineering team. They are internal advocates for software engineers. They consider the developer's journey from being new developers and their 'Time to First Contribution' to day-to-day activities. They work with engineers to learn which problems are a priority and identify misconceptions and bottlenecks that may slow the development process.

## Conclusion

Developer experience (DevEx) is essential for creating maximum output while increasing developer satisfaction. The appropriate technology tools, workflows, and a supportive development community can help foster progress and innovation while promoting high-quality software engineering results that can become a competitive advantage and ultimately benefit the business's bottom line.

By dedicating attention to improving the DevEx, companies will also be able to bring more talent aboard, reduce their "Time to First Contribution," enable developers to provide higher output contributions and improve talent retention. It's time to start focusing on superior developer experiences.

- Join the [Developer Infrastructure workshop with Pulumi and Okteto](https://www.pulumi.com/resources/developer-infrastructure-with-pulumi-and-okteto/). Perfect for those looking to streamline their development process and foster better team collaboration
- Read [The Pulumi 'Push to start' GitOps Experience](https://www.pulumi.com/blog/pulumi-developer-workflow/)
- Discover [Pulumi for Platform Teams: New Features for Developer Portals, Policy and Deployments](https://www.pulumi.com/blog/developer-portal-platform-teams/)

---

## Frequently asked questions

### What does business critical mean?

Business critical means essential for a business to operate and be successful. It refers to business processes, systems, or activities that are considered essential for proper functioning, success, or survival. If these elements are disrupted or compromised, the impact can significantly affect its operations, financial health, or overall business objectives. Business-critical components are often prioritized for attention, protection, and resource allocation to ensure the organization's continued effectiveness and stability, and to remain competitive.

### What is the role of a Developer Experience Engineer (DXE)?

Developer Experience Engineers are internal advocates indispensable to making life easier for developers by making workflows more efficient, implementing the same processes across the development team, and assisting in choosing tools to lighten their load. Some companies do not necessarily have engineers with that job title, and it's instead seen as part of DevOps or Platform Engineering initiatives. Other times, the internal developer advocate natural rises from the developer community to help form an integral part of the developer team's unity. They also champion communication and work with cross-function coworkers and feel safe means of providing constructive feedback.

### How do we cultivate a positive developer community?

The importance of DevEx's human element is now in focus. A productive and effective developer community could be seen as a flourishing habitat, strengthening cooperation and maximizing productivity through collaboration. Such an atmosphere also sustains morale among the developers, resulting in job satisfaction and contentment.

Here are some steps to build a developer community: open communication needs to become standard, successes should consistently be recognized, and avenues for growth need to exist. Diversity and acceptance are significant. Task expectations should be attainable goals and set high enough not to compromise quality but not realistic so they can be achieved without burnout and unbalanced life routines.

### How does technology impact developer experience?

Technological advancements continue to change software development and impact the Developer experience. AI, ML, TDD, and internal developer platforms are some of these technologies that help reduce developers' cognitive load. They automate complex tasks for more accuracy and enable intelligent decision-making. Besides this, generative AI has come into play in creating higher-quality code faster. At the same time, GitOps is a management approach based on one source of truth - Git, which makes collaboration smoother & boosts productivity by allowing automation. All these things undoubtedly improve the DX substantially for any developer out there!
