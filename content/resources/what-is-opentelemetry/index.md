---
# Name of the webinar.
title: "What is OpenTelemetry?"
meta_desc: In this session you will learn how OpenTelemetry helps you understand your distributed system and the performance of individual services within it.

cloud_engineering_summit:
    track: build

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
url_slug: "what-is-opentelemetry"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "What is OpenTelemetry?"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "What is OpenTelemetry?"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/2Dg2m5a-RHo"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T14:30:00-07:00
    # Duration of the webinar.
    duration: "20 minutes"
    # Description of the webinar.
    description: |
        Microservices have broken monitoring tools and practices. Traditional methods of application logging and host-based metrics can’t provide accurate and timely signals for issues impacting production. OpenTelemetry solves this dilemma by providing a single set of APIs, SDKs, and automatic instrumentation tools that give you the ability to understand your distributed system and the performance of individual services within it.

    # The webinar presenters
    presenters:
        - name: Liz Fong-Jones
          role: Principal Developer Advocate, Honeycomb

# This section contains the transcript for a video. It is optional.
transcript: |
    Hello, and thank you for coming to my talk about OpenTelemetry and observability. One of the problems that we have on our plate as software developers is that we waste a lot of time on break fix work work that is reactive rather than proactive and doesn't necessarily move the business forward. We waste over 17 hours out of every single week because of technical debt and bad code, according to the Stripe Developer Coefficient report from 2018, why is this? It's because we're tasked with doing three different things all at the same time, and it can feel really, really overwhelming. We want to both shift features, more of them, faster, scale to meet user demand, and decrease downtime all at the same time. And we're really afraid that things are not going to work correctly in production, that things are going to break and that we're not going to be able to figure out why.

    And when we have slow feedback loops, the problem gets even worse because when you've forgotten about what you've developed because you turned it over to another team to do integration testing on, and it didn't actually release production until two weeks later bundled with a hundred other people's changes, you'll have no idea why the release was broken. You'll have no choice, but to roll it back. But the good thing is that progressive delivery culture and DevOps have solved a lot of these challenges by enabling people to have faster feedback cycles, and get code deployed to production faster. But that doesn't necessarily solve the problem of what to do once your code reaches production. How do you keep your code running successfully in production? This is the problem that we still struggle with.

    We struggle with a lot of technical complexity, where different microservices are releasing at different rates, faster and faster, creating end known failure modes that we couldn't have predicted in advance. Caused by interactions between users and services, including noisy neighbors and multi-tenant situations and our traditional monitors no longer work. So this is where observability and OpenTelemetry can come to our rescue and help solve the problem. Hi, my name is Liz Fong-Jones, and I'm the Principal Developer Advocate at Honeycomb, but the hat I'm wearing today is actually that of an OpenTelemetry Governance Committee member. I am part of a vendor neutral body that is aiming to standardize how we measure and report data from our production systems to enable developers to move faster in production.

    I'm an elected member of that governance committee and I act on behalf of all of OpenTelemetry rather than just my particular employer. So today we're going to have covered what's painful in software development? What observability is, and how it can help? And how OpenTelemetry plays into the observability picture? And then finally, I'll give you some starting points as to how you can get started with OpenTelemetry to advance your observability journey so that you can get back to shipping code with confidence faster. So let's talk about what observability is and isn't. Observability helps us answer questions about our systems. Questions that the previous generation of technology did not allow us to answer.

    Things like what are the common characteristics about the queries that timed out taking more than 500 milliseconds and not just the dimensions that we thought to break down by previously, but new combinations of dimensions, things like language pack, browser plugin, software version, data center, and to combine all of these things together, along with the full execution path of the request. Rather than being confined to measuring only by predefined dimensions. In order to achieve observability, we need to have both instrumentation data and the capability to query it. And I'll tell you more about that in a minute. So there's research done by independent researchers that shows the impact that monitoring and observability have when you advance to observability and not just have monitoring.

    The accelerate state of DevOps report, reports at 26% of teams are elite in the year 2021. And those teams are 4.1 times as likely to integrate observability in how they run their services, rather than just attempting to passively monitor their services. Solving that problem with the 17 wasted hours per week, teams with good observability practices spend more time coding according to the DORA research groups, Accelerate State of DevOps report. Additionally, open-source technologies such as OpenTelemetry is part of the journey towards becoming the elite team.

    Elite performers that meet reliability targets are 2.4 times more likely to use open-source technologies, according to the DORA reports, Accelerate State of DevOps report. And what do they mean by an elite team? They mean a team for which they're able to deploy multiple times per day on demand. And that the lead time from writing a change to having it running in production is measured in hours, not days or months. So you may have heard this before that observability has something to do with logs, traces, and metrics.

    The answer is that telemetry data is part of the picture, but it's not the entire picture. Observability is about our socio technical systems. It's about the ability of our people together with the systems to answer important business questions and to get back to doing proactive work. This means that our developers have to be able to write high quality code that's instrumented correctly from the beginning, to measure its progress through the systems, to debug it in production, and then to understand how users are actually utilizing the feature, and finally to manage and eliminate tech debt so that we can make sure that our systems are scalable and maintainable into the future. So yes, we do need instrumentation in our code in order to produce that data.

    We need to be able to store it. But most importantly, we need to be able to query it, answer questions such as why is our bill taking 15 minutes rather than 10 minutes? Or why is this particular set of user seeing HB five hundreds? That's what really matters to our business and not necessarily having a Pokemon situation of collecting all of the different telemetry types just because we can. So let's talk about those data signals though, because they are important to consider. Your data comes in many different formats. In particular, you may be used to measuring metrics which are aggregate summary statistics that tell you data points such as how many requests did you have in the past five minutes that took between 500 and 600 milliseconds.

    You also may be used to diagnostic logs which contain detailed debugging information emitted by processes. But what distributed tracing aims to do is to provide a causal relationship to give you insights into the full life cycle of a request, tying together the relationship between different bits of your code that are running at different points in the request workflow. Regardless of how you will wind up with data in the end state, the reality is your systems are executing code in order to execute user workflows of some form. And you can have those workflows emit structured data corresponding to those units of work, and then we're able to synthesize metrics, logs, or distributed traces out of those pieces of structured data. So that's how I encourage you to think about it, is that you can choose to make data in the format of metrics, or in the format of logs, or in form of distributed trace, or maybe potentially in the future to utilize new things like continuous profiling everywhere.

    So you have to be able to generate the data, send the data somewhere, store it, and then visualize it. And that's where OpenTelemetry comes in as a vendor neutral solution that enables you to correlate multiple types of telemetry together. So OpenTelemetry arose as a vendor neutral project, whose goal is to make telemetry simple for end users. So you don't need to change or re-instrument your code every time you decide to change backings or change vendors. It's also the combination of two previous open standards, OpenCensus and OpenTracing that were both trying to achieve the same thing and realize that they would be better off if and the ecosystem would be better off if we joined forces together.

    So OpenTelemetry supports tracing, context propagation, and metrics today, and has emerging work around logs as well as continuous profiling signals. These projects have been in the works for awhile. OpenTracing was founded over five years ago in 2016 and OpenTelemetry is formed as the merger of OpenTracing and OpenCensus in 2018. As of when I record this in October of 2021, OpenTelemetry's specification has reached general availability and OpenTelemetry is available in some of the most popular languages as a generally available product. So OpenTelemetry consists of a number of moving parts that I think are all important and all work together to produce an optimal result.

    The most important part about OpenTelemetry is that it's a cross-language specification that no matter how many different languages you use in your project, you can use OpenTelemetry as one seamless set of APIs that work consistently together and transmit data in a consistent manner in order to measure the properties of your system and get the debugging data that you need. Additionally, there's also the OpenTelemetry collector, which is a Swiss Army knife that enables you to ingest telemetry in any format, whether it's produced by OpenTelemetry libraries or not. And to emit it in a variety of different supported formats. Third, for every language, there is an implementation with a specification, both in terms of an API that code can call by end-users or by library authors, as well as an SDK that actually takes those incoming API calls and turns it into pieces of telemetry that gets sent out over the wire. Finally, there's automatic instrumentation libraries that make it very easy to get data flowing without writing very much code.

    So referring back to that earlier diagram, OpenTelemetry creates all of the necessary data so that you can understand your systems, understand where they're going wrong or where they're working correctly, but we're relatively agnostic about what you do with that data once you've produced it. And that way we preserve interoperability and flexibility for our end users. So OpenTelemetry also works regardless of what language or technology you use. Not only do we support like everything from Java and .NET, to Node and Python, but we also even have emerging things such as a CLI integration, so you can wrap your shell scripts with OpenTelemetry and that'll enable you to understand the performance of your shell scripts and performance of any applications that are called via shelling out.

    So what do I mean by the APIs? Well, let's demonstrate what the OpenTelemetry APIs look like in Golang, for instance, what OpenTelemetry provides is a mechanism for you to say, I want to trace this particular library and I don't need to care whether or not the end user has set up OpenTelemetry or not. If any user hasn't set up OpenTelemetry it's still safe to call the API and it won't do anything. But if someone has configured the SDK, then they'll immediately start getting useful data from my library. So within one of the functions of my library, I could take the languages standard context object, and then I can, say I want to create a span and close the trace span when this function terminates. And I might set parameters and attributes in order to provide instrumentation that lets people know what function calls were made and what their attributes were that were passed along when you initialized that call.

    This enables people to have a fine-grain understanding of what your library is doing and what it's spending its time doing in case it gets slower, starts submitting errors. OpenTelemetry also implements the W3C TraceContext standard, which is a World Wide Web Consortium standard that says, this is how we define what a trace ID is or a request ID and what a individual trace span ID is and how do we transmit that information from process to process and from web server to web server, API server to API server, so we can understand the full flow of execution and not just that, we're also able to understand things that we want to pass along all the way down to individual end points. For instance, where did this request come from? So that we can make smarter decisions about routing along the way. So distributed context propagation is a crucial part of OpenTelemetry because it enables us to correlate requests no matter where in the system they're happening. So that when we collect that data in the end, we're able to understand and retroactively figure out what happened.

    But you don't necessarily have to manually write instrumentation if you're an end user because OpenTelemetry aims to make instrumentation ubiquitous, so we've written wrappers or directly integrated with common frameworks in each language to make sure that you're able to always have an active trace context if you're using for instance, Express in node JS or the HTTP libraries in Go. So we're able to just say, hey, by the way, wrap this function with this automatic instrumentation handler and we'll take care of the rest. We'll take care of recording the HTTP status code, the duration, the mecha name, these are all things that will just automatically record, but if you have something additional you want to add on, we're always happy to give you direct access to the trace bands so you can add in your own attributes. So when you define the API calls, that doesn't necessarily mean that you're admitting OpenTelemetry data right off the bat. That way it's safe for anyone to compile into their binary, but the SDK implements trace and span collection, and actually starts collecting that data.

    And then you can configure exporters to send data wherever you like. And that can be anything from an existing format or the new OpenTelemetry format, which is a common language that OpenTelemetry speaks, regardless of whether it's the collector or a supporting backend, or whether it's the SDK producing the code. And the collector is important because it, as I said, it's a Swiss Army knife, it proxies data between the instrument code and the backend services. And that means it's just a config change, not a code change to recompile, if you want to try out a different backend. So in terms of export, as I said, the OpenTelemetry protocol is our native protobuf or JSON format that enables people to have one common way to import and export telemetry data.

    But we're also cross-compatible with things like Jaeger, which has an established tracing product, or Prometheus, which is an established metrics product. The collector is able to receive things in whatever format. Potentially enhance it with information about the current resource and it can even do things like drop personally identifying information or key the data to multiple different backends in order to make it as easy as possible for you to have data portability. You can also run it as a sidecar in order to collect local information about the currently running container or pod. So what do I do knowing about OpenTelemetry's components? Well, let's talk about what the journey of an OpenTelemetry adopter looks like.

    If you choose to adopt OpenTelemetry, the first place I encourage you to start, is to start with OpenTelemetry's automatic instrumentation, especially if you're using a language like Java, you can go ahead and install the OpenTelemetry agent, which will automatically hook into your server and will automatically start measuring your gRPC server or your HTTP server. So attach the agent to a few tightly connected services within your infrastructure. You don't have to employ it everywhere. And configure the exporter to send data somewhere immediately useful. For instance, you can send that data to an OpenTelemetry collector that's located on as a sidecar on your local host and then you can immediately route that data to a backend.

    For instance, you could choose to use Jaeger and Prometheus, which are open-source software, or you can use the generous free tiers of a large number of vendors that support OpenTelemetry. And it's just a config file option in your collector to choose where to route the data. And you can try out multiple providers as your needs grow because it's just adding additional stance to say, hey! I want to try out LightStep or I want to try out Honeycomb. And then after that, the thing that I recommend, is adding custom attributes that are relevant to your business to start measuring smaller units of work. If you discover the request is taking a while and you don't have visibility into why, you may want to add a trace span, covering part of that unit of work to understand where is it spending its time and how can I optimize it? You can also start implementing across multiple services beyond your initial seed set of services and potentially do conics propagation for everything ranging from your Amazon load balancer or Google cloud balancer, all the way down to things like event driven services, Kafka, or even use OpenTelemetry's newly adopted project SQL commenter which enables you to correlate your application traces to the slow query log in your database server.

    So there's a wide number of ways you can go with OpenTelemetry because it's so extensible. And as you evolve, you'll be able to use observability data to make your systems run better and to make your teams function better. Use observability data to level up with things like service level objectives so you can measure the impact to end users as measured by real user monitoring, and then to be able to use distributed tracing to debug those issues all the way down to the service admitting errors. You can also graph the chart of services to understand, do I have dependency cycles? Do I have single points of failure? And then finally, telemetry data can be useful in order to understand, should I potentially automatically remediate and drain from a bad availability zone or roll back a problematic relates? So that's what I have to share with you today, is how OpenTelemetry relates to observability and how observability can make your life easier by making it possible to understand who is impacted and why they're impacted in the event that you're having unexpected or turbulent conditions in production. If you're interested in learning more about observability, you can go and visit the CNCF Observability Technical Advisory Group on the Cloud Native Computing Foundation, Slack.

    You can also check out OpenTelemetry on Cloud Native Computing Foundation, Slack, or visit our website, OpenTelemetry.io I also encourage people getting into service-level objectives to check out OpenSLO, which is a new standard being developed to use telemetry data to measure service-level objectives. Finally, if you're interested in seeing me speak more about OpenTelemetry, you can go and look at my Twitter or the OpenTelemetry Twitter or Twitch. And I'm always happy to meet people over video conference. If you'd like to spend 30 minutes pairing or asking questions about how to adopt OpenTelemetry and how to make your life as a developer more productive and to sleep better at night.

    Thank you very much and I look forward to taking your questions and to conduct the fireside chat. You can find me at hny.co/liz and I'm @lizthegrey on Twitter. Thanks.
---
