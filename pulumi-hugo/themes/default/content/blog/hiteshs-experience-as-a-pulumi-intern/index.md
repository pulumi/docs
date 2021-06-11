---
title: "Hitesh's Intern Experience at Pulumi"
date: 2021-06-11T09:53:45-07:00
meta_desc: A reflection on Hitesh's experience as a Pulumi Intern, including what he worked on and learned.
meta_image: pulumi_mascot_3.0.png
authors:
    - hitesh-boinpally
tags:
    - pulumi-interns

---

Hi everyone, I’m [Hitesh Boinpally](https://www.linkedin.com/in/hitesh-boinpally), a junior studying Computer Science at the University of Washington. I was offered the opportunity to intern for Pulumi over the past three months, and here’s how it looked!

<!--more-->

## Technical Work

My overall project was to build a test harness for Pulumi’s converter tools such as [`arm2pulumi`](https://github.com/pulumi/arm2pulumi) and [`tf2pulumi`](https://github.com/pulumi/tf2pulumi). The project involved several pieces, all of which meant learning about technologies I hadn’t encountered before.

1. A program that ran the test itself and generated results in a program readable way, which I wrote in Go.
2. Running that program to  generate historical data over time through GitHub Actions consistently.
3. The cloud infrastructure part, which was uploading the test results into an AWS Redshift table for human-accessible analysis. Here was where I got to utilize Pulumi and better understand infrastructure as code.

All of these were fascinating to learn about and stretched my knowledge in directions I hadn’t previously explored.

I began with setting up the harness for [`arm2pulumi`](https://github.com/pulumi/arm2pulumi). The Go program had already been written, so I needed to focus on the GitHub Actions for CI and cloud infrastructure aspects. I set up the CI quickly, but the cloud infrastructure took some time. Wrangling with AWS’s different IAM roles, cross-account permissions, and how to utilize the different tools was complex and challenging. However, I learned a lot about these different spaces and gained valuable experience. Further, I appreciated the advantages of Pulumi, as I could quickly undo/redo changes incrementally, rather than making manual changes in the AWS Console.

Once I built the arm2pulumi coverage tracker end-to-end, I shifted to [`tf2pulumi`](https://github.com/pulumi/tf2pulumi). Unlike `arm2pulumi`, there was no code to inherit, and I had to write out the entire workflow from scratch. The Go program was the real challenge, as the CI work and cloud infrastructure I had written was reusable. I got a much better hang of Go as a language and the advantages that came with it. I also got to leverage Pulumi’s [Automation API](https://www.pulumi.com/docs/guides/automation-api/) and the power of having multiple, configurable stacks through Pulumi to significantly simplify the process of deploying `tf2pulumi`’s (and any other converter’s) coverage report cloud infrastructure. Overall, I explored various new technologies, many of which I’ve used in personal projects since, and plan to continue to do so.

## Day to Day Work

Due to the ongoing pandemic, my internship was done fully remote. Having come from 4 quarters of remote learning in college, I wasn’t particularly ecstatic about more remote work. Pulumi completely exceeded my expectations, though!  It was hard to meet new people, and I missed out on the daily interactions you might expect in a traditional office environment. Regardless, efforts were made to overcome that, and they were pretty successful, with biweekly random 1:1s and fun team events to better integrate with the team. On the other hand, I work better at night and am a bit of a late sleeper, so I could adjust my schedule to my strengths more than I would if I were going into an office each day. Additionally, Pulumi has adapted nicely to the remote environment and made my experience much better than I thought possible.

The team itself was great, with everyone being super friendly and supportive. It took me longer than I expected to get the confidence to ask questions in general Slack channels, but each time I did, I was met with a helpful response and got the assistance I needed to succeed. Despite being the only intern, I never felt cast aside and was guided throughout my project in a balanced way, still allowing for some independence. Everyone is also so knowledgeable that I would learn something new perusing Slack every day, whether internal to Pulumi or an article about some new way of doing things.

Thanks to the high level of transparency at Pulumi, I also got to see many different levels of the company, rather than just the work that I was doing. As a result, I learned more about how a company works fundamentally, and a typical development process.

## Closing Thoughts

Pulumi was my first ever internship, and I couldn’t have asked for a better experience. I learned about a ton of new technologies, some of which I may not have explored yet but at least am aware of for future projects. In addition, I met some truly incredibly talented, hardworking, and interesting people. I’m stoked to continue using Pulumi and am excited to see how the company evolves and grows!

## Thank Yous

First off, a huge shout out to the leadership at Pulumi for offering this opportunity to begin with! Thanks to [Lee](https://github.com/leezen), especially for organizing the internship and your help throughout it!

Thank you to [Levi](https://github.com/lblackstone) for being an awesome, approachable mentor and always willing to help out! I asked a ton of -- oftentimes pretty random -- questions, and you helpfully answered each of them.

Thank you to [Vivek](https://github.com/viveklak) for guiding me through many technical details and approving my PRs. Your guidance was really useful, and I appreciate it a lot!

Lastly, thanks to all those who helped me out along the way and the rest of the team for building such a friendly, helpful environment!
