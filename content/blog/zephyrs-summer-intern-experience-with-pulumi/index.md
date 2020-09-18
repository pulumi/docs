---
title: "Zephyr's Summer Intern Experience with Pulumi"
date: "2020-09-18"
meta_desc: "Zephyr's internship experience in Summer 2020, personal growth, skills learned and reflection"
meta_image: zephyr-pulumi.png
authors: ["zephyr-zhou"]
tags: ["pulumi","intern"]
---

Hi, I am [Zephyr Zhou](https://www.linkedin.com/in/zephyr-zhou-a17741196/), a senior Computer Science student at the University of Washington. I spent this past summer interning at Pulumi. This is my first internship ever in my life. Thanks to Pulumi for providing this opportunity even in this difficult time of the Covid-19 epidemic. Despite the sad truth that I couldn't get in touch offline, I believe this will be one of my most precious memories.

Time goes by so fast, but before saying goodbye to my internship, I would like to share the story.

<!--more-->

## Personal Growth

Honestly, before my internship started, I was so nervous that I couldn't sleep. Previously, I had taken only one data management course that contains a tutorial about setting up Azure SQL Database. Other than that, I knew nothing about the cloud. Although I have read the [Getting Started documentation](https://www.pulumi.com/docs/get-started/aws/) and learned Go, I was worried that my understanding was not good enough. Also, I transferred from a community college to the University of Washington as a junior student and was admitted to the Computer Science major after that. Therefore, I felt relatively new to programming than my peers and less confident working in the industry, even less so working remotely.

However, I am glad that I was brave enough to make the first step out of my comfort zone to learn about new things and improve my understanding while practicing. That was one of the important reasons for choosing to intern at Pulumi, a startup with great potential. Also, due to the nature of startups, Pulumi has smaller but more connected teams. Personally, I felt more comfortable discussing issues and thoughts in small groups. Also, I was able to work with different teams and people. I was also able to broaden my horizons and improve my collaboration skills.

I found that the more familiar I got with the company and the job, the more confident I was. My confidence was boosted in large part from the support of team members. The warm greetings and kind help gave me a lot of powers and courage. Working remotely with Pulumi was much more interactive than I thought. The one-to-one meeting with my mentor and site supervisor has boosted my working efficiency because I could compile my questions and updates, talk about them all together, and get informed about if I am on the right path. I also loved the fact that I was able to join other team meetings so I could learn about the different projects other people are working on.

In addition, I absolutely loved the various team-building games, especially the virtual escape room and the pair-up chatting with other engineers in the team. These interesting events and relaxed atmosphere made me feel more welcomed and less stressful. I've been moved and realized it is okay to be imperfect and improve step by step. Despite having less coding experience, I was still welcomed and cared for by everyone at Pulumi.

Moreover, I am so glad that I could work on my individual internship project: building the content management system (CMS) for Pulumi's website. I took control of the whole development phase of the Content Management System project. I was able to research and write up proposals, implement the project, plan the next steps, and improve. In the end, the CMS was published and running. I have contributed back to the Netlify CMS, the underlying technology for the CMS. I have built an [open-source example](https://github.com/pulumi/examples/tree/master/aws-ts-netlify-cms-and-oauth) and written blog posts on deploying the [CMS application]({{< relref "/blog/deploying-netlify-cms-on-aws" >}}) and its [OAuth Access Token Server]({{< relref "/blog/deploying-the-infrastructure-of-oauth-server-for-cms-app" >}}) to AWS.

When I heard the CMS project would be a great help for the marketing team during our meetings, I felt indescribable happiness and proud of myself. Although far from perfect, I was finally able to prove myself with this unforgettable experience.

Confidence is the greatest gift that Pulumi gave me during this Summer internship. I felt a lot more confident in entering the technology industry and pursue my career goal as a software engineer. Thanks to this internship experience, I have grown braver and stronger than before.

## Technology Skills

I have learned a lot of skills that I have never learned in the classrooms.

- First of all, I learned a lot about Pulumi and cloud technology.
  - Before my internship, I read about how Pulumi provides a platform for building infrastructure. At first, I thought the benefit would be to reduce the amount of work to click through different settings on the provider's website. However, during the CMS development process, I found writing infrastructure as code can do many more things than that. For example, I have implemented Github Actions, which automatically deploys the infrastructure when I push or merge a pull request. It saves time to upload and deploy again and prevent any manual error by automating the process. Also, if we want to remove the cloud resources completely, Pulumi enables us to do a simple `pulumi destroy` rather than manually going through and worrying about missing any resources.
  - I also learned to build the cloud infrastructure for a static website by configuring AWS S3 bucket, Route 53, CloudFront, and Certificate Manager. I also learned to configure AWS Fargate Service and create a Dockerfile.
  - I learned more concepts, including assume role, CDN (Content Delivery Network), target groups, and load balancers.

- Besides cloud technology, I also got to work with the Continuous Integration/Continuous Delivery concept and have practiced it with GitHub to work with the team.
  - I learned more details about git command including, the difference between `git rebase` and `git merge`.
  - I learned to create GitHub projects, issues, and pull requests and link them for better references.
  - I got to know about GitHub Actions and Workflow and implemented one for my internship project to increase efficiency in deploying.
  - I learned about GitHub OAuth Applications and more about GitHub API while working on the OAuth Server for the CMS application.

- I learned to create a static website using plain HTML and CSS in the classroom. During my internship, I was able to get in touch with modern front-end technology including Netlify CMS, Hugo, Markdown, and React, while building CMS and the website's preview.

## Reflection and Next Steps

Although the CMS application's basic infrastructure is working and provides a content management interface for updating the webinars and events pages, there are more things I want to improve. During the last meeting with the marketing team, we discussed creating a [custom widget](https://www.netlifycms.org/docs/custom-widgets/#header) for shortcodes and image storage system. I created the necessary GitHub issues and added them to a GitHub project but didn't have the time to implement it.

I realized I should have had a clearer time schedule of development when writing the proposal and coming up with a priority list of the features I wanted to develop initially. During my meeting with the marketing team in the beginning we only discussed the potential improvement but failed to count the time it takes to develop each feature and the priority of them. If I could communicate about that better and write a better-timed plan, I would be able to implement more new features.

Also, my mentor and manager taught me to dig deeper into the problem to understand the issue better. It also helped me organize my time better when looking into issues.

In general, these lessons and experience will benefit me a lot, especially after I enter the industry after graduation in Spring 2021. I feel more prepared now. I have been fascinated by the concept of cloud and cloud infrastructure as code. I feel the potential of cloud technology and believe I will develop my career goal in this direction.

Soon I will return to my senior year's schoolwork. However, please feel free to keep in touch with me via my [Linkedin](https://www.linkedin.com/in/zephyr-zhou-a17741196/).

## Special Thanks!

First of all, I offer my sincere appreciation to Pulumi leaders, Joe Duffy and Luke Hoban, for offering this internship opportunity despite their busy schedules in the middle of our internship.

Words can't express my thanks to Praneet Loke, my mentor, who spent every day having sync meetings with me to guide my internship pathway and help me move forward, step by step. I can't count how many times he saved me from daunting problems and patiently explained obscure knowledge.

I cannot express enough thanks to Lee Zen, our manager, for organizing this internship, ensuring our internship experience, entrusting me with the exciting CMS project, and guiding me towards the correct path during our weekly meeting.

Moreover, my completion of the internship could not have been accomplished without:

- Chris Smith. Thank you for helping me to understand the concept of assuming a role and setting up the credentials and domains for my CMS project.

- Sophia Parafina. Thank you for proofreading my three blog posts and carefully fixing my expression errors.

- Isaac Harris, Lindsay Marolich, and Jay Wampold. Thank you for spending time learning and trying out the CMS and sharing suggestions for improvement.

- Zack Chase. Thank you for informing me about the components of Pulumi's website and trying out my CMS application.

- Freddy Hernandez. Thank you for ensuring our compensation and organizing various team building games, which made my life in quarantine fascinating.

- Everyone at Pulumi. Thank you all for helping my fellow interns and me out and contributing to my wonderful internship experience!
