---
# Name of the webinar.
title: "Beyond Prod: Don't Let Your Data Fail You"
meta_desc: This talk will deep-dive into how whylogs fits into the infrastructure as a whole and how it can enable end-to-end observability for your data stack.

cloud_engineering_summit:
    track: deploy

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
url_slug: "beyond-prod-dont-let-your-data-fail-you"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Beyond Prod: Don't Let Your Data Fail You"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Beyond Prod: Don't Let Your Data Fail You"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/OjCBDRDe9IA"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T09:00:00-07:00
    # Duration of the webinar.
    duration: "27 minutes"
    # Description of the webinar.
    description: |
        In the era of microservices, decentralized ML architectures and complex data pipelines, data quality has become a bigger challenge than ever. While infrastructure-as-code and DevOps frameworks such as Pulumi enable best practices in managing and testing the infrastructure and software, much is left to be desired for managing data quality. As data becomes more entangled in software-based decisions, it’s critical for companies to start treating data with similar rigor to what the DevOps world has. In this talk, we will address this challenge through whylogs, an open source standard for data logging. We’ll deep-dive how whylogs fit into the general infrastructure as a whole and how it can enable end-to-end observability and monitoring for your data stack. This shift in paradigm will enable companies that operate with data to move faster and safer by building discipline and processes around data.

    # The webinar presenters
    presenters:
        - name: Andy Dang
          role: Co-Founder and Engineering Lead, WhyLabs

# This section contains the transcript for a video. It is optional.
transcript: |
    Good morning, everyone. My name is Andy Dang. I'm a co-founder and a tech lead at WhyLabs. Today, I'm gonna talk about the problem of monitoring data once it's deployed to prod beyond the normal DevOps monitoring pipeline. So when AI is deployed everywhere and not just AI, any data pipeline applications, we, organization nowadays have adopted various stacks to deploy machine learning as well as analytics to production environment. And once in production, these data flows can fail in unanticipated way and can prove to be very difficult to operate.

    For example, as of today, over 100,000, AI failures have been recorded by the partnership on AI in an AI incident database. So if your team run data and AI in production, you probably have a story of how it failed and upset your customers or affected your business. Just like Andreas here, who got recommended a pepper as a substitute for roses by the whole foods' algorithm. Luckily it's a harmless failure in this case, but that's not always the case. So in the data centric world, machine learning or AI application is just one of the many uses of data centric applications. We have analytics software, we have traditional decision tree making software, so all of these pieces are creating a complex flow of data pipelines and they come with their own scaling challenges and they are fighting complex business decisions.

    Unfortunately, the traditional DevOps monitoring that revolves around application performance monitoring is insufficient to really address the quality control as well as ensuring this data centric architecture can work effectively in the real world. Another thing is that when it comes to data, it has a very different characteristic from traditional DevOps signals. We have the massive volume of data points. And so when things fail, it's really hard to detect. Even when things work, it's also hard to manually configure all these possible dimensions. And by what I mean dimensions is because data tend to contain many fields. Each of them might fail independently of each other. And oftentimes what the operators at the moment are doing, are writing complex queries and extracting complex metrics to detect these issues.

    These are expensive mechanisms and it creates a lot of friction in the development and deployment process for data centric applications. And sometimes it creates this culture of fear because when it's hard to process and detect failures, it's harder to deploy to make changes. In most of the time, we often say that companies are flying blind without data monitoring in production. And a lot of the existing DevOps are not designed around these characteristics. So some mitigations in the DataOps and the machine learning world have done, have applied like retrofitting DevOps culture into the MLOps culture like you've seen solutions around GitLab and GitHub based deployment, Git based operations. And then you also have solutions where they retrofit the prometheus and grafana to monitor data pipelines.

    As I mentioned, those are insufficient to really address the characteristic of a complex real-world pipeline. The landscape itself is still very early and very immature. So what are the gaps here? I want to recap a bit. Here first of all, data itself is highly dimensional, at the moment when it comes to data monitoring, we tend to couple them with the data warehousing solution, because we would run query analysis using this existing technology. Most oftentimes SQL, which are powerful. However, because there's this coupling, it limits the ability to monitor this architecture in places where data warehousing is not available. And that comes to the next part where we have data being deployed to the small devices like smartphones or ILT devices.

    And these are very different from traditional data warehouses, where you have everything in one single location with a massive processing engine. And finally, the explosion of configurations. When you have tons of data, it's harder to tell what to monitor, monitor what matters is hard. And this is where observability and zero config monitoring philosophy can come to rescue and solve the problem. So you just don't just deploy data to prod, beyond that you want to monitor these pipelines and data flow continuously. Taking a step back, I want to introduce myself a bit more in depth.

    I am the tech lead at WhyLabs.ai And what we're building is we are a team here, set out to build a solution for continuously tracking data and machine learning models to help companies and teams measure what matters in their machine learning system. We take the expertise of, I spent six years at Amazon building massive data pipelines and data warehouse solutions before entering the machine learning infrastructure and tooling world. So my background is bring together this kind of knowledge around operating real world massive data systems versus running machine learning in production, both of which are kind of separate fields at the moment, but they are converging into what we call MLOps. At WhyLabs we built an open source solution called whylogs as a standard to track data quality and we believe that every team must have access for continuous machine learning monitoring.

    And I'll talk about whylogs in the next part of my talk. And this solution can allow team to track and measure data quality regardless of where it is in the pipeline, whether it's on your mobile phone device, on ILT device, to where you're running it in a massive real-time data processing systems, such as Kafka. This philosophy of log way statistic collection allow us to integrate with many points in the data flow and allow you to treat data monitoring problem in a very similar manner as DevOps monitoring problem. So here's the agenda. I'll try to discuss in a little bit further about specific kind of data challenges around monitoring for data itself, the science behind it, and then I'll discuss data observability and what that means in the context of data deployment.

    And then I'll go in depth about whylabs and how to get started with whylabs. So data monitoring challenges, this is a very, very high level overview of a machine learning system. I'm taking machine learning system as an example of a data architecture here, just to highlight the increasing complexity of how we operate data. DevOps was coined in 2009 and our software architecture has evolved significantly then. Obviously nowadays we have infrastructures code like Pulumi, where we deploy software as part of our pipeline, and we can monitor and test our infrastructure. However, when it comes to data, ML pipelines involves a lot of data and metadata, but there's a huge gap in the tooling space to really talk about what it means to do checks at each of the step for these boxes in the diagram, it's not, and the data comes in a complex form. It's just not just pure numbers.

    They come in high dimensional, they can be embedding, they can be images. So we require a solution that is slightly more that provides more insights than traditional DevOps solution and with highly complex data that can support a large number of features and various machine learning use cases, as well as traditional data use cases. And the data volume is one of the things that we want to focus on because we recognize that the pipeline is, first of all, is constantly evolving. Sometimes you don't, you can't keep every record of the data that your system sends or process, because data also can be ephemeral simply because of cost, privacy or security you can't store every single data point sometimes.

    But you still want to monitor that data flow somehow to make sure that it doesn't look too different from the data flow you've seen yesterday, for example. Existing philosophy around this tend to be expensive by storing all the data in a warehouse, tedious because you need to run SQL query on top of that warehouse. And that requires writing SQL query, which some people are a fan of, but I don't think a lot of machine learning scientists or software engineers are excited about doing that as a day job. And it can be very time consuming because these queries get expensive, running against a massive data warehouse. Now and then with the infrastructure changes, it's a lot easier to build terabyte scale pipelines now. In minutes, you can spin up a massive spark job cluster in database for example, or snowflake and process tons of data at the same time.

    If you look at all the core steps of machine learning pipeline or data pipeline, each of these steps involves data transformation and moving massive amount of data. And you can, once you start operating this sort of stat, you quickly learn that each step can introduce a data bug in production and can completely derail the whole system. Even though the software is sound, data systems of very sensitive to data bugs and data changes, especially machine learning one and the majority of machine learning failures stem from data and not the code itself. So this slide, we talked to 150 data science team, and we just ask about the recent failures they have to deal with. And this is just a sample of the issues. And as you see, typically, when we think about software failures, we think about either bugs in the code, lack of you know, testing, lack of integration testing, or infrastructure deployment failures, but when it comes to data, everything can be correct.

    And the data itself is still just different because data reflects the real world. And when COVID happened for example, it changes how customer behave and therefore changed the data's shape. DevOps, traditional DevOps for testing validation does not transfer well due to again, the data issues, dimensionality and volume issues, I mentioned before. Also, especially with machine learning system, a fluctuation of distribution itself can disrupt the whole system. And that is different from what the problem that DevOps systems like prometheus or grafana are are trying to solve. So here's the quick list of data logging versus software logging and different ways how we can monitor the problems in these metrics.

    And just to call out that if you look at the metrics that we have to collect to effectively monitor data stream, the number of metrics in, if you map that back to the traditional DevOps solution, it increases significantly and it increases the cost. So this is why traditional software lab monitoring is insufficient for data monitoring. And on top of that, we really want to talk about observability. It's not about monitoring, it's about providing insights, because lot of the time you find problems by looking at metrics or chart rather than setting up individual monitors all the time.

    So what that means is that machine learning, we can learn a few things from quality control in traditional DevOps. We have canary, we have constant monitoring for system in production, by emitting metrics, we can do something similar with data. So data systems are not deploying nice pipeline into snowflake everywhere. They run in live system, they run on devices. So we are proposing this technique called data profiling, thinking about collecting lightweight, simple lightweight statistics that are meaningful, that will allow user to detect data quality in production without having to actually store the data.

    So here let's say we want to design such data lab with the sort of, kind of quality we would want from our experience working with both machine learning and data warehouse problems, there are key five core categories. First one is metadata, like just simple things like when it was produced. And then the count of data points. These are simple. And more advanced ones are statistics like standard deviation, distribution, like histogram of the data, and then stratified Sam and then building stratified sampling on top of this is something that is not really at risk by by how traditional software monitoring works because using these statistics and distribution, and you can decide smartly what data points to collect, like only collecting the outliers or the long tail data points rather than randomly sample your data stream to try to debug a data issue, for example.

    And since logging to be a part of every ML step or data pipeline step, we need to be thoughtful about the runtime footprint. What are the key properties? Here's some, taking some lesson from the DevOps best practices, a good solution should be lightweight, should be portable, should be configurable. And we're working with statistics in massive datasets. The last one it should be mergeable. So you can build a global view of the distribution of your, for example, when you run data on 20 machines, you can see the global view across 20 machines, rather than, rather than having to run again, SQL analysis in order to collect global statistics.

    And then finally, when you have these properties, you can enable a deployment everywhere for this solution. And this is what we were trying, what we are building with whylogs and build in terms of the kind of properties that allows whylogs to be infrastructure agnostic and can run in multiple environments. So what is Whylogs? It is a data centric logging library. What it does is it log all key statistics of your data over intervals of time, instead of producing log files for example, you get a summary statistic file and there are multiple open source library that actually try to tackle the problem of testing data quality or evaluating drift. But whylogs tech is a very different approach where it doesn't require you to store the full data set, to run such analysis.

    It decouples the process of producing distributions and metrics from the step of generating drift and analysis, because the drift and analysis and data quality checks might happen way downstream. When say you compare data between your production system against your training system. It can, it provides the foundation for profiling the data, testing data quality, and mark and continuously monitor data after production deployment. And thanks to these properties, it works elegantly for big data systems, such as a Apache spark, which is a Scala. We have a Scala library that is actually wraps around our Java library. It can work on terabytes of data taking full advantage of spark raw processing power. It doesn't require double passing over the data and because the logs are so lightweight, the cost of any IO bandwidth is minimized.

    And because whylogs also tries to tackle the machine learning and all the data engineering steps in Python, we have a Python version as well. And in this example, you're looking at whylogs integration with ML flow. It allows user to track data, associate data, fingerprints with every step of the experiment. And this is a very powerful feature when you can visualize these statistics all the time, too. And then you can ideally build, monitor and debug data issues by running through this exploratory data analysis in a black white manner. So you don't have to run it against say a whole SQL database.

    Here's just a very example of how whylogs does it. It takes in the key statistics per feature. So without zero, without any configuration from user, these statistics that are automatically captured. The type of metrics Whylogs that captures is configurable and would love the community contribute new metrics and ideas. Our GitHub and slack community are very active and you're welcome to chime in and look at our roadmap and directions. And once you collect this statistic over time across different step, in this example, we ran the example for 20 batches of data, and we capture the whylogs property for every feature in the batch.

    And we take, we can visualize distribution, for example, free sulphur dioxide across different batches here and visualizing this sort of distribution over time, allow user to understand drifts and data blocks, even without any automated monitoring on top of this. You can see here, there's a spike in the middle of the graph. And if when given that this feature is an important feature to the model, I probably want to take a look and make sure that that batch does not have any problem associated with the data like user input for example. Now the most important property of a logging setup is the cost. Capturing data statistics should not involve massive amount of data or processing it, post-processing it. So whylogs uses to cast its streaming algorithms to capture remarkably the lightweight data statistics, this ensured that constant memory footprint and the ability to log terabytes of data without breaking the bank.

    Furthermore, whylogs is mergeable so streaming pipeline can capture micro batches like every 5 minutes and aggregate them into hourly batches. And then you can even aggregate them further to create a global view or daily view, the ability to slice and dice is there for you and again, the result is very lightweight, and doesn't contain raw data So very privacy friendly. And the ability to store this using these algorithms, like Kappa lambda allow us to capture much, much more accurate data distribution than traditional method of sampling, for example.

    So once with this, you are going back to the initial conundrum of monitoring after you deploy to production. This is why we developed Whylogs, to capture data every step of your pipeline in production and in development. And this allows you users to visualize, to detect data quality issues and take action, like meaningful actions. When we open source the library, the AI community actually and the data community actually found additional ways of using whylogs' output. For example, whylogs can also be used to test data, you can take the distribution in production and test it against your development data set to make sure that what you're doing in development, the transformation doesn't cause deviation from the actual data and in production, for example, or the sample that you're using in development is representative of production data set.

    And then you can also extract constrain from whylogs so that you can assert things like data points should be within this distribution or data points should not have X amount of missing value every batch. These become unit tests as well as canary, we call them canary data validation for post deployment of machine learning and data pipelines. So how do you get started with whylogs? It is an open source library. It is available in Python and Java. So you can check out our whylogs GitHub repo and our example. We would love to have some feedback.

    And if you are curious about the WhyLabs platform, where we provide free monitoring for your models, check and sign up from this form and you can get an account to experience the workflow of visualizing and going through the flow of pushing and logging and monitoring data on for your real time or for your batch models. Fine to conclude, I would like to invite everyone who's thinking about AI governance and transparency and data for quality, for data center infrastructure to join the effort, to develop an open standard for data monitoring with whylogs.

    We have a slack community to discuss the tooling and the future direction of the standard and the extensibility of it to make sure that it works from multiple use cases. And also check out the link on the right for the GitHub package. Again, you can pip in story very easily in a Jupiter notebook environment, and also try out how to see how easy it is to log data as part of your machine learning and data operation. Would love to hear your feedback, your contribution and feature requests that will help us drive the direction and the integration into your favorite data and machine learning tooling, and to extend the concept of logging to new data types, like images, audio. And so, yeah, and also join our slack if you want, just to talk to us. Thank you very much for listening.
---
