---
title: Learning Machine
type: page
layout: case-study

meta_desc: |
    Learn how Learning Machine used Pulumi and TypeScript to streamline its devops processes
    and eliminate several hundred thousand lines of configuration code.

exec_summary: |
    Learning Machine provides a secure platform, using the blockchain, to issue records in
    a format that is tamper proof, recipient owned, and independently verifiable.  They
    are witnessing opportunities in several key industries – Public Sector, Healthcare and
    Education – and need to maximize their resources in order to quickly capitalize on the
    explosive growth opportunities in front of them.  Pulumi offered them a solution which
    would allow them to target new environments with minimal changes to their core
    solution, allowing them to increase their cloud footprint without increasing their
    engineering investment.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: Challenges
      anchor: challenges-faced
    - label: Results
      anchor: results
    - label: Conclusion
      anchor: new-opportunities
---

## Learning Machine Corporate Overview

Learning Machine partners with governments, companies, and school systems to deploy secure
credentialing systems that leverage the blockchain as a secure anchor of trust.  To ensure
the longevity and interoperability of these records, they are leading  contributors to
standards communities, including Blockcerts, IMS Global, and the W3C.

## Challenges Faced

Like many Software as a Service companies, Learning Machines started off with a basic
infrastructure and a simple development process.  They selected Amazon Web Services as
their public cloud partner, and began using Cloud Formation to specify their
infrastructure.  Most of the development team was focused on higher level business logic,
and very quickly, the task of infrastructure specification became specialized, since few
folks on the development team had the time to jump in and understand the hundreds of lines
of JSON used to get their SaaS up and running.  The team was able to make progress for
several months, before it was clear that there were some showstopper issues with their
initial approach.

First, the template files were growing at an alarming rate!  What had started as a few
hundred lines of JSON quickly grew to thousands; in fact, at its peak, the Cloud Formation
specification grew to over 25,000 lines of templates.  In part, this was because of
inherent limitations in the technology itself.  The technology was missing basic control
flow, and worse, there was no way to create reusable components.  Of course, this made the
resulting specification even harder to understand, and so even less of the team was able
to contribute, and infrastructure specification became a bottleneck for the team.  This
was compounded by the fact that when the team did need to make changes, they often did so
using the AWS console, creating “drift” between the specification they thought they were
running and the actual infrastructure that was provisioned in production.

Second, the company was growing.  The CEO of Learning Machine, Chris Jagers, realized that
much of their growth for the next few years would come from international clients, which
would necessitate their core product being replicated in data centers across multiple
geographies.  He huddled with his COO, Chris Hughes, and his CTO, Kim Hamilton to
brainstorm about how to solve the dilemma they were facing.

## Moving From Complicated to Simple

Both Hughes and Hamilton realized that they needed to transition away from their first
generation tooling to a more sophisticated offering.  While they researched some of the
existing cloud management companies, they realized that none of them really offered them a
full solution.  They wanted their development team to be immediately productive, using
their existing skill sets and they needed a solution that could be adopted incrementally,
rather than shutting down with a full “lift and shift.”  Fortunately, they were able to
meet with the Pulumi team and describe the issues facing them and what they wanted to see
in a next generation solution.

Together Learning Machine and Pulumi worked together to develop a solution.  Learning
Machine chose JavaScript and TypeScript as their key programming language and decided to
keep their infrastructure on AWS.  Once they realized that they would be able to stamp out
copies of their infrastructure on demand, they also decided to enhance their CI/CD
pipeline, in order to give their engineers the freedom to try new approaches, while
maintaining engineering discipline with their core staging and production roll out
processes.

The prototype was developed in just a few weeks, and transformed thousands of lines of
templates into just a few hundred lines of code.  Everyone on the team was able to clearly
see the resources that their solution was using, why they were being used and who was
responsible for their maintenance and configuration.  Pulumi truly delivered a new way for
the team to work.

<img class="block mx-auto max-w-2xl my-8" src="/images/case-studies/learning-machine-loc.png">

## Results

“Pulumi is the foundational technology that allowed us to transform our organization,”
said Hughes.  The entire DevOps process was streamlined and in addition to realizing
better productivity and higher quality, the team has new insight into their SaaS offering
that they never thought possible.

## New Opportunities

With the adoption of Pulumi, Learning Machine created new opportunities not just for the
Technical Staff, but for the business as a whole.  In addition to supporting new
geographies for their public cloud, they now have the option to offer private cloud
support as well, since they finally have an abstraction that allows them to deliver their
products across multiple architectures.  “Initially, we focused on cost and developer
efficiency,” said Hughes, “Now, we realize that this is in fact a strategic choice, and
that we can use this work to deliver the speed, flexibility, value and business outcomes
that are so vital to our company.”

Hamilton offers this advice to her peers in key CTO roles.  “Jump in with both feet – the
sooner the better.  The payback is immediate and the confidence you gain from having a
predictable development pipeline is immeasurable.  Our industry moves with incredible
speed and using tools like Pulumi are absolutely essential to providing teams with the
agility that they require.”
