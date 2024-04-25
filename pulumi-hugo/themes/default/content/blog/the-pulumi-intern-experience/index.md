---
title: "The Pulumi Intern Experience"
date: "2020-09-16"
meta_desc: "A glimpse into my work and experiences at Pulumi as a summer intern"
meta_image: intern.png
authors: ["sashu-shankar"]
tags: ["pulumi-interns"]
---

What is the cloud? Three months ago, that one word simply meant a bunch of water suspended in the atmosphere, but now it means more than that.

Hi, I’m [Sashu Shankar](https://www.linkedin.com/in/sashushankar/), a second-year computer science student at the University of Washington, and this is my life as a Pulumi intern!

<!--more-->

## My Pulumi Experience

### Getting to Know the Team

Let’s be real, onboarding with a new team in a remote situation was tough; the world was quite literally in a state of chaos, and each day was filled with talking to faces on the screen, but everyone was in the same situation, and that made it just a little more bearable. Coming into my first full software engineering internship, I was a nervous wreck, and I had millions of questions. What is the remote culture of the company going to be like? What is their standard for the quality and timeline of work, and am I going to be able to meet them? However, the team was always supportive, and it didn’t take long for me to feel like I was integrated with them and comfortable with the people around me. No matter the time of day, someone was always available to talk!

### Asking Questions

“There is no such thing as a dumb question” was a phrase I heard a lot, but it never fully registered until recently. The “cloud” as we know it is quite vast. Setting it up takes hours, and fully understanding what is going on could take tenfold. Pulumi simplifies the process; however, there is still so much going on even when doing a single thing. This experience truly taught me that there really is no such thing as a dumb question and searching the internet to find answers is an expectation! Nobody knows all the answers, and that is completely okay.

### Remote Lifestyle

I’m definitely not a fan of the [remote environment](/blog/coronavirus-plan/), however, I’m the kind of person that is more productive at night, so it allowed me to shift my work to times when I knew I would get things done. That said, face to face interaction was something I missed a lot, as it’s understandably harder to get to know people over a computer. However, since Pulumi already has many remote engineers, it was a very smooth process to get set up and start working right away.

## The Project Experience

### Introduction to the Pulumi Model

I worked on the Platform team for the last 3 months, and they focused their work on the Pulumi SDK. The first few weeks were a huge learning curve, as the interns were tasked with converting Pulumi deployment examples from Typescript to Python, C#, and Go. This intro project taught me a lot about cloud resources, how they are deployed, and introduced me to helpful debugging tools through this process. I also learned how to write [tests](/docs/using-pulumi/testing/) to validate output for a deployment which proved helpful as I learned how the entire process was working.

### kube2pulumi Tooling

I built a CLI tool, and an open-source library to convert Kubernetes YAML manifests to Pulumi in a user-defined language [check out kube2pulumi!](/blog/introducing-kube2pulumi). This was done so that Kubernetes users could easily migrate to Pulumi, and use familiar programming languages to tame YAML's complexity. I truly learned a lot from this experience as it was my first time designing and implementing a project end to end in a set time frame. Utilizing existing open-source libraries, code generation techniques, and compilers theory were just some of the many things I got to delve into.

### UI Interface

Another feature that came out of this was a UI layer to access it directly on the web; this forced me to think about different error scenarios and how they would be handled to make it a polished experience. Additionally, this really exposed the programmatic usage of kube2pulumi when writing the web service. It allowed me to further improve the overall experience in whichever form the user decides to use. To top it all off, going through a feature launch with the team was extremely exciting! It's one thing to consistently work on an internal tool, but it's another ball game when you are shipping your work directly to the community.

## Final Thoughts

Coming into industry work right out of my freshman year of college was a daunting task; however, I wouldn’t have wanted to intern at any other place other than Pulumi! The mentorship, team camaraderie, and, most importantly, the exposure to new technologies and learning made this the best possible experience I could’ve imagined. I’m super proud of what I could	accomplish with the team, and I’m excited to see what the future holds for the company!

What is the cloud? Three months later, I can say that the cloud, to me, is a vast tool for people to build their visions and dreams, and Pulumi is the place I would come to help me get that started :)

## Shoutouts :)

Thank you [Albert](https://github.com/albert-zhong), [Zephyr](https://github.com/zephyrz73), and [Vova](https://github.com/jetvova) for being incredible, kind, and helpful intern buddies!

Thank you [Evan](https://github.com/evanboyle) for being an amazing mentor by being so approachable, and always being there everyday. You were always so patient with me and answered virtually any question I threw at you :)

Thank you [Lee](https://github.com/leezen) and and [Luke](https://github.com/lukehoban) for being such organized, motivating, and empathetic managers!

Thank you to [Levi](https://github.com/lblackstone), [Lee Briggs](https://github.com/jaxxstorm), [Komal](https://github.com/komalali), [Pat](https://github.com/pgavlin), and [Mikhail](https://github.com/MikhailShilkov) for being so open and friendly and always being available and sharing your experience when I needed anything at all!

And finally, thank you to everyone at Pulumi and the whole platform team for giving me this opportunity!
