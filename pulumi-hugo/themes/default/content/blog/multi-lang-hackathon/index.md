---
title: "Demos from the Multi-Language Component Hackathon"
date: 2021-06-24
meta_desc: "Pulumi successful multi-lang package hackathon showed how to build multi-lang components and yielded demos exploring new concepts and capabcilities"
meta_image: hackathon.png
authors:
    - lee-zen
tags:
    - multi-language component
    - hackathon
---

At Pulumi, we have a tradition of hosting hackathons every so often to play with concepts and ideas that we may not typically encounter in our day-to-day product building activities. This past week, we’ve had two separate back-to-back hackathons. Our first hackathon, which was open to the community, focused on using our new [multi-language component capabilities]({{< relref "/blog/pulumiup-pulumi-packages-multi-language-components" >}}). Multi-language components allow developers to author reusable infrastructure abstractions in one language and make them available to others in all the languages that Pulumi supports. We were really excited to see what everyone would build!

<!--more-->

We had a kickoff meeting on Tuesday morning where Lee Briggs walked participants through the [basic steps for bringing up a multi-language component](https://www.youtube.com/watch?v=_RXvNS5N8A8). If you’re interested in seeing the kickoff meeting, we’ve recorded it and have made it available for viewing on [Pulumi TV](https://youtu.be/Ogg5cs6vPfc). After the walk-through, teams got down to business!

We had some great ideas, including but not limited to components for a simplified Google Cloud project setup, an Azure web app service container, and an Amazon SageMaker model with a frontend for serving it.

As part of the hackathon, we received some great feedback from all the participants on improving the multi-language authoring experience, including reducing boilerplate code, ways to improve on the schema authoring experience, and documentation suggestions. We’re keen to continue to refine the experience.

Thank you to all the participants! If you’d like to see some of the components in action, you can [watch our demo session](https://youtu.be/U7-eYSpB4o8). We saw the following component demos:

- "Run my d#!n container” which demonstrated a component to run a container on any of the major cloud providers.
- A component that brings up a new Google Cloud Project.
- A component for creating an AWS Lambda function fronted by API Gateway
- A component for creating an Amazon CloudFront distribution backed by an S3 bucket
- A component that runs an AWS Lambda function as a cron.
- API Gateway component that simplifies creating Amazon API Gateway resources
- A serverless component that consumes Serverless configuration
- Replicated S3 Bucket component to simplify cross-region object replication
- Miniflux component that deploys the Miniflux service
- .NET Boilerplate for multi-language components

Stay tuned for our next post on our general hackathon results. In our general hackathon, the Pulumi team tried out new ideas and investigated ways to improve upon the Pulumi experience!

You can watch the hackathon including the intro multi-lang components, the hackathon kickoff, and the demo session.

### Introduction to Building Multi-lang Components

{{< youtube "_RXvNS5N8A8?rel=0" >}}

### Multi-lang Hackathon Kick-Off

{{< youtube "Ogg5cs6vPfc?rel=0" >}}

### Hackathon Demos!

{{< youtube "U7-eYSpB4o8?rel=0" >}}
