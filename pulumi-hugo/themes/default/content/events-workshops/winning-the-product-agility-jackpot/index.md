---
# Name of the webinar.
title: "Winning the Product Agility Jackpot"
meta_desc: "Learn ways to use infrastructure-as-code to build product stacks that not only deliver business value but also make engineers excited to work on them."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars

# External webinars will link to an external page instead of a webinar
# landing/registration page. If the webinar is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the webinar page created.
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "winning-the-product-agility-jackpot"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Winning the Product Agility Jackpot"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Winning the Product Agility Jackpot"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/QrdNIhCWW2A"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-10-08T10:00:00-07:00
    # Duration of the webinar.
    duration: "28 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Learn how a social gaming company from Australia builds their product stacks to maximize product agility and engineering efficiency. The talk covers effective ways to leverage containers, infrastructure-as-code and the cloud to build product stacks that not only deliver business value but also make engineers excited to work on them.

    # The webinar presenters
    presenters:
        - name: Luke Mundy
          role: Senior Site Reliability Engineer, Virtual Gaming Worlds

# This section contains the transcript for a video. It is optional.
transcript: |
    What's up, everybody? Thanks for tuning in to my presentation. I hope you've been enjoying the summit so far. My name is Luke and for the last 14 or so months, I've been having an absolute blast working at a place called V-G-W. V-G-W is a social gaming company founded in Perth, Western Australia, which is also where I live and we have a couple of pretty cool game products on the market. I'm lucky enough to be a Site Reliability Engineer for one of them, called Chumba Casino. Chumba Casino is an online social casino currently serving customers in the U-S-A and Canada and what I'll be talking about today is how I've been working with the team at Chumba to, to do this. So these are two metrics we use of a handful of different metrics to track our software, development, delivery performance.

    We got these metrics out of a book called Accelerate. I'm sure some of you have probably heard of, and or, read this book, but I will give a quick, brief summary just to get everybody on the same page. Like it says on the cover of the book is about building and scaling high-performing tech organizations. And in the book, it explores the various factors that impact software delivery. Their research suggests that if you can optimize these four metrics, you will deliver faster and more reliably than your competitors. Now, I've only got two of the four up at the moment and that's largely because pretty much everything I'm going to talk about today is pretty directly related to these particular two metrics. So the things I'm going to cover today are, infrastructure as code.

    I'm going to talk about some principles we use at Chumba when writing infrastructure as code, going to talk about some deployments stuff. So, principles we use for deployment and how we kind of unpacked our, our existing deployments infrastructure. And lastly, I'm going to touch a little bit on how, when you get the these first two parts, right, you can start to really reap the benefits of docker and everything that docker provides. So let's get started on infrastructure as code. So I'm a big fan of infrastructure as code. I've been working with it a lot over the last several years of my career. So when I started in July of last year at Chumba Casino, I was pretty keen to see what they had.

    I knew they were on A-W-S so I was expecting probably CloudFormation, maybe some Terraform, but, in my first few days they mentioned that they actually had a custom in-house built Python code that a handful of architects had built quite awhile back, but were no longer at the company. So I did start to get a little bit curious and that did raise a few red flags. Eventually at some point that week, I checked out this infrastructure as code and I was pretty mortified to say the least.

    It was a massive 15,000-line, Python code-base and the more I kind of looked into it and tried to see how it worked, I Identified a huge number of issues straight away, which you can see on the screen there. The biggest issues were just how highly abstracted it was, the fact that it was unmaintained, and the the infrastructure that it was deploying was very rigid and very standardized. This code base was kind of intended to define all of the infrastructure across V-G-W, not just for Chumba Casino and so as a result, it was highly standardized and very difficult to change. It was a big ball of mud, but in infrastructure as code terms.

    So, I pretty quickly identified and worked with the, the seniors and an engineering lead for Chumba, to say that yeah, look it was pretty clear, we need a real infrastructure as code tool, pretty quickly. Now, as you probably guessed already, that's all eventually was Pulumi for us, but I did want to take a brief moment to talk about how Pulumi wasn't actually my first choice originally. So as I mentioned, I've got quite a bit of experience writing infrastructure as code, but all of that experience has been using declarative languages. So YAML or H-C-L when I've used a bit of Terraform and I've always considered that to be the real man's infrastructure as code.

    And, and why would you sort of do it, anywhere, any other way? When I first found out about Pulumi, I was pretty skeptical and my, my assumption was that using imperative languages to write infrastructure as code would be a catalyst to writing similar things to the the giant Python code-base that I had just seen. Really, highly abstracted complex code-bases. But as I used it some more, I started to like it and very quickly changed my tune, and so did the rest of the squad leads in Chumba Casino. Some of the main reasons we chose it over everything else was we were pretty deep into typescript already.

    So 90% of all the active development in Chumba Casino happens on typescript. So, being able to write typescript with Pulumi kind of fit right into our workflows and toolchains. The I-D-E integration was great, the, the typing the auto-complete and the intellisense, and probably my favorite thing about imperative languages and infrastructure as code, is actually being able to use real looping constructs. So for-loops, for example, or, or other kinds of loops to really just cut down on the, the amount of code you have to write. But as much as vendors may want us to believe it, new tools don't just make all your problems just magically disappear.

    We still needed some good principles to follow and we still needed to make sure that we weren't going to end up with another massive code-base monstrosity like we already had. So let's talk about some of those briefly. Now as software engineers we tend to have, we're prone to taking abstraction a little bit too far sometimes. So something I've tried to ensure that we do with our infrastructure as code moving forward is to just keep a handle on that abstraction and not go overboard. It's really important, I think to keep it simple.

    Even if it's just so that when you onboard new engineers, particularly juniors or associate engineers, that they don't need to kind of wade through four or five levels of abstraction before they can understand the various cloud provider resources that are being provisioned by the infrastructure as code. I think it's very easy to go too far with abstraction. And like I said, it just it just muddies the water, but it's also not necessarily ideal to not go far enough with abstraction.

    If you don't abstract enough, it means there's lots of duplicated code, lots of re-work and things of that nature. So it really is something you've got to find the right balance form. One of the other biggest problems with the old infrastructure One of the other biggest problems with the old infrastructure as code was it was highly standardized and what that meant was we were, the engineering teams were kind of put into a, confined in a box with with how they could architect the infrastructure that ran their services. With the new code, I've chosen I need to standardize some of the really basic building-block style resources.

    So for example, I've got a Fargate web service module that we use across Chumba at the moment, but it only really defines just an E-C-S service. Some task definitions and some roles and things like that. And that's it. We've also got a couple of other small standardized modules, but these are mainly for utility things. So things like lambdas to send log-streams to our log aggregation tools and things of that nature. I think, like I said standardize, too much standardization just limits Innovation, and if, if I was hoping for the, the engineering squads to be owning their infrastructure as code, I needed to be able to let them do what they needed to do and solve the problems in the best way they could come up with.

    So the other thing standards sometimes try and do is to enforce policy. So as an example, let's say you need to ensure that all S-3 buckets in your organization are encrypted. What the old infrastructure as code, at Chumba would have done, is kind of provided you a bunch of pre-built infrastructure components that only had encrypted buckets, but I think the the better way to achieve that same outcome, while still kind of unshackling your engineers is to use policy as code for that. So there's a number of different policy as code tools with Pulumi. Obviously we use CrossGuard, but they have Sentinel available for Terraform and Open Policy Agent can be used in another of other contexts.

    I think when you define constraints and let your engineers just fill in the blanks, that's when you get the best result. If you, like I said, if you're giving pre-built infrastructure components to engineer's they'll very quickly find the limitations of those standards and find it difficult to to move around them. It's much better instead to just write policies. Tell them where the, where the constraints are and, and let them fill in the gaps. So these are just a couple of the principles. I've started following with our infrastructure as code, but after getting started migrating a lot of this stuff to Pulumi, I quickly found that it wasn't just infrastructure as code that was holding our deployment performance back. And that kind of brings me on to the next topic of the talk and that's deployments.

    So like a lot of companies, we, we had Jenkins, a Jenkins install. And while I don't really have a huge problem with Jenkins in and of itself, I think there's probably really nothing worse than a Jenkins install that you inherit from from other people particularly when you started a new job. Now the Jenkins install at Chumba was, was a particularly bad case of this. Again, it was just a sprawling mess of scripts, or what I like to call script hell. Bash scripts that link to other Bash scripts that link to Python scripts that had various different control flows and configuration in them. It was largely unmaintained an unpatched as well. So it hadn't been patched in God knows how long, it was running a very old Jenkins version.

    The pipelines were very brittle. So there were very frequently pipeline failures that you know required an engineer. Sometimes just a senior engineer, because they had most of the previous experience troubleshooting things to fix it. So it took a lot of time and it just wasn't fun for everyone. It was a giant dumpster fire to use an overused analogy in software engineering. So one of the main issues I ran into, or one of the main decisions we had to make then were are we going to stick with Jenkins and try and clean it up and fix things or were we going to pivot completely and move to a different tool.

    In our particular case, making changes to Jenkins were just super high-risk. There was no easy way to test things in isolation without sort of replicating a large number of different scripts that were somewhere in source control, some weren’t. So it became a very risky operation, if we broke things, if we broke a certain pipeline or if we accidentally, you know, took out Jenkins for a day or two, that would be a day or two where we couldn't do any deployments which is a pretty big deal as you can imagine. So, we pretty quickly made the decision, we were going to migrate to something else and it was likely not going to be Jenkins.

    Chumba Casino doesn't really have a lot of engineers with operations experience. So we tend to shy away from, from managing our own servers and our own deployments and definitely prefer managed services. So that's what we started looking for in a new tool. So we ended up choosing Codefresh and there are a couple of reasons for that, the first being the the feature set is quite balanced as far as C-I-C-D tools go. What I find is that a lot of tools are either really good at C-I and not so good at C-D or vice-versa.

    Codefresh seemed to be kind of the best of both worlds. There's still sort of a handful of features that are missing, but are on the road-map, but overall it was a really good fit for what we were looking for. We needed both C-I and C-D features. The other cool thing that attracted us to Codefresh was its focus on containers. Pretty much our entire stack is now running on containers. So some of the extra container focus we get from Codefresh was always super beneficial. But again, like I mentioned before, tooling isn't just going to solve all your problems immediately. And this was no different for Codefresh.

    We needed to approach our deployments differently and we needed to unpack some of the poor design decisions we had we had made in the existing stuff. So most of what I've learned about making deployments work really well has come from The Twelfve-Factor App. This isn't anything particularly new, and, and again, I'm sure a lot of you have already heard of it. But for those that don't know The Twelfve-Factor App goes into detail on 12 factors of app develop, development, particularly for cloud-based apps. Now, I'm not going to touch on all these because we don't have time. I'm really just going to talk about the one that I feel the most strongly about and is configuration. So Twelve-Factor defines configuration is everything that's likely to change between deployments. So things that change between your local environment versus the staging environment versus production.

    Code is or should always be the same across those environments. So the things that change are things like the U-R-Ls of that environment potentially, the instance sizes you use in that environment, or maybe database secrets, that kind of thing. Twelve-Factor then goes on to say apps sometimes store configs as constrants in the code and we did this a lot in Chumba. But this is a violation of Twelve-Factor, which requires strict separation of config from code. Now, it may, it's probably not immediately apparent why this is a bad thing. So I'm going to go through a handful of examples of mixing and config in code and why it leads to some problems and why it kind of limits your flexibility. So this is one that's particularly common or was particularly common.

    It's also something I've seen, not just a Chumba, but at a number of different code-bases I've worked on where, certain behavior that you don't want to occur in non-production environments gets wrapped in, in an if-statement like this, but it's keyed on, on just the value of the environment variable called environment where obviously it matches the, the type of environment it is. Now, to kind of illustrate why this is bad I'll ask a few sort of rhetorical questions to help illustrate the problems I'm trying to identify. So one problem with this code is how do you how do you test the production of, do production behavior function in a non-production environment? You can't really, I mean if, if this if statement was just in one place in your entire code-base and this was the only place that this environment variable was used, I guess you probably could.

    You’d just change the value of that environment variable, but what's typically the case is this is littered all throughout the code-base and there's tens and sometimes hundreds of different places where this same method is used. So when you run this app in non-production and you set environment to production you really don't necessarily know what other behavior you're switching on and it could definitely be other behavior that you really don't want to have occur. So another good question that kind of arises out of this example is why is the app actually behaving differently in prod in the first place? Which is also another really good question. I think there's some sort of small examples where this is desirable when you're using sort of feature flags for either in development or, or new features, but for the most case behavior between test and production should be identical.

    In most of the cases I've seen this implemented it's usually, it's a wrap, things like e-mail functionality or purchasing functionality where you don't necessarily want a real e-mail to go out or you don't necessarily want a real purchase to go through. In these cases, I feel like the behavior should still be the same across all different environments, but to prevent real e-mails or real purchases to go they should be connected to mock services instead, instead of doing this this weird branching. The next example I'm going to go into is, I guess the most explicit case of hard-coding configuration into code and this again was another pretty common one throughout services in Chumba Casino.

    We have many of our, of our applications obviously need to know the base U-R-L that they're operating on and so there was, the easiest way in a lot of cases was to write this kind of function where again keying off the environment, environment variable, and just returning a very unchanging list of U-R-Ls, but again to ask some questions, what if I wanted to run this app locally on a different port, one that's not 80-99. What if I wanted to deploy this app into a temporary ephemeral environment? Let's say as the result of a P-R build. How would I deploy this to a temporary host name? You can't really do that with this code.

    It requires you to actually make code changes first and rebuild and artifacts which is obviously going to revol—, involve a pull request, potentially some new unit tests. There will need to be a review that kind of thing which is quite a lot of overhead for just being able to sort of spin-up a different environment to test something very specific out. And so this, this concept of being able to deploy without changing artifacts or something Twelve-Factor goes into a lot as well. It's kind of phrased as being, build once, deploy many times and it sort of looks a little bit like this.

    So regardless of the, the build artifacts that come out of your build process, whether they're docker containers, maybe they're tarballs or executables, the idea that Twelve-Factor tries to promote is you should be able to just build your application once and then deploy that to any environment that it needs to go to. So again, using the ephemeral stack example, I should be able to take the artifact from a P-R build. I should be able to deploy that to a temporary host-name with temporary configuration. I should be able to run that exact same instance locally and configure it so it will run properly on the right ports with the right host-names and things of that nature.

    The other cool benefit of this is if you're having a problem in production, you can pull down a copy, an exact copy of the build artifact running in production and troubleshoot that locally with just you know, a few changes of config. Now one, I guess disadvantage that I've heard talked about when we're talking about the separation of config and code is that it removes the actual values of config a bit further away from the developer when they're writing code, but I think although Twelve-Factor doesn't really go into specific detail on this. I think when we're talking about separating config and code it's really talking about separating config from the build artifacts and not necessarily the code.

    I think starring config in source control right next to the code is often the best place to put it. So I just wanted to point that out a little bit as well because it sometimes can get misinterpreted. So there's, to achieve this, I guess good separation, there's two small things that I try and get the the engineers in Chumba to do. The first is to use environment variables for very specific, discrete things. There's no longer an environment variable called environment. That's quite a very ambiguous into what it enables. Instead, it's very specific environment variables like database host-name or maybe enable this particular feature flag. That kind of thing. The second thing is to have a configuration object built in a central location and I'll show you an example of that now.

    So in our apps, I've started to encourage our engineers to, in a single file, generate this configuration object. And, and this is the only place in the code. That should really be reaching into environment variables. As you can see this is a pretty contrived example just with two fields, but you can add sort of as many as you want and it allows you to kind of set docstrings, set up any appropriate defaults if you want to. You can also do validation of configuration and the other cool thing is it lets you properly type all the different configuration items.

    So in this case, I've got two strings so it's not really a good example, but if you have got more complex configuration types coming from environment variables, instead of having to always manipulate a string type, you can convert that into whatever type you need to make things a little bit safer for the engineer. Then to use this you just need to obviously grab that config and have that happen at a very nice an early point in the bootstrap of your apps. Again, this is a very small example just running an express service, but once it's, it's been included nice and early here, the rest of your app can just refer to the config and not have to worry about manipulating strings in environment variables.

    Something else I'm going to try and Implement soon is a linting rule. So once this is set up we can have a lint rule that checks for access to environment variables outside of configuration just to kind of drive that home. So when you're able to achieve this separation of configuration in code you get kind of a lot of benefits. So the first one is as we saw before, you're able to kind of take any artifact deployed anywhere and, and test out very specific things under very specific configuration, which is really good for testing and verification. But the other cool thing you get out of it is you can start to sort of really reap more of the benefits of docker. Now, there's a lot to really talk about for docker particularly around best practices.

    Again, I'm only going to go into a small amount, but here's some links to some other resources that I've personally used to help level-up how we use docker files and docker at V-G-W. So next I'm going to show you this pretty basic example of a docker file, but a lot of our docker files are sort of starting to take a very similar shape at V-G-W. So the first thing to point out is we're now making use of multi-stage builds and largely to ensure that we can build the code in the same execution environment as the resulting image, but also stop building and installing dependencies on the host image and then copying them through. The other thing you will see is we’re linting, building, and running unit tests all inside that docker build.

    This is really handy because it kind of helps us ensure that we can we can build the app and build an artifact pretty much on any workstation we want, provided it's running docker. The other thing I generally recommend to people is if they've got quite a lot of different stages in their multi-stage docker builds, is to enable build kit. It's surprisingly a not that well-known feature, but it's a new build engine that docker has. I think it's close to being the default or being generally available, but it's still something you need to enable within an environment variable. But what it does is allows better paralyz—, paralyzation of different docker stages. And so even though this is a basic docker file, we do have four stages, but these two, first stages have no dependencies.

    So what build kit will do, will run and build these two stages simultaneously. The next two obviously depend on each other so they need to be run serially but serially, but you can sort of see the benefits you might get for a more complex docker file. The other thing, that good use of environment variables and docker allows you to do is, really make the most out of things like docker compose. Being able to spin-up a full copy of your application with all its dependencies, the things like demo-ing to other developers running integration tests, and also having those integration tests run in an ephemeral environment during your build pipelines. Again, this is another basic example of a docker file. Sorry a docker compose file that I've got in a small personal project that I use for testing out some stuff.

    We've got a simple postgres database, a flyway container that sets up the schema and contains all our database migrations and then an A-P-I image which is built from the local docker file. Now, you can see we've obviously got good use of environment variables here. So this is able to be run with whatever configuration it needs. Once you've set this up locally, then again, like I said, becomes very easy to run integration tests, particularly if your integration tests are running inside a container also.

    Something I've used at least in this hobby project is running Postman in a docker container to run a handful of A-P-I calls across those apps, but arguably one of the more powerful things is being able to spin-up that docker compose as part of your build pipeline and running build test. So this is just a quick screen cap of the build pipeline for the docker compose image you saw, and what this step here does is it spins-up that docker compose file,, runs the integration test and this happens on every build. It happens quite quickly, as you can see the only sort of took 43 seconds to spin-up the app, boot-strap the database and run through a pretty big, heavy suite of postman tests.

    And then after this, obviously you can then push the it image, push it through a handful of real environments if you need to, or put it in front of real testers. So once you get a good handle on this, that's when you sort of start to see your deployment frequency kicking off, and when you make good use of testing, unit testing and integration testing, using, you know, the advantages of docker, your change failure rate should hopefully go down as problems get exposed earlier and earlier in the build, build process.

    That's all I've really got time for. Thanks so much for tuning in. It's been a pleasure to present at the summit. So big thanks to Pulumi for giving me the opportunity. Also wanted to give a quick shout out to Lee Campbell who helps immensely, helped me immensely put this together. Like I said, this is the first time I've presented externally, so I'd really like to hear your feedback if you can hit that link on the slide there. Other than that, I hope you enjoy the rest of the summit. I'll see you later.
aliases:
  - /resources/winning-the-product-agility-jackpot
---
