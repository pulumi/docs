---
# Name of the webinar.
title: "Testing Configuration with Open Policy Agent"
meta_desc: "In this talk multiple techniques for testing different configuration formats, including showing how to use Open Policy Agent to test Pulumi."

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
url_slug: "testing-configuration-with-open-policy-agent"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Testing Configuration with Open Policy Agent"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Testing Configuration with Open Policy Agent"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/SpiT-Xq1cAk"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-10-08T10:00:00-07:00
    # Duration of the webinar.
    duration: "28 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        As developers, we’re writing more and more configuration to power increasingly powerful services and applications. But how do we ensure that the configuration we write meets community best practices and our internal policies?

        In this talk we will:

        - Introduce Open Policy Agent, an open source policy engine
        - Discuss the Rego language used to write policies for Open Policy Agent
        - Show how Open Policy Agent based tools can be applied at different stages of development, from local testing, CI/CD and through to auditing production
        - Touch on policy as a tool for assisting with tool portability
        - Talk about why reuse and sharing are critical to scaling the use of policy based testing
        - We’ll also show lots of demos of testing different configuration formats, including showing how to use Open Policy Agent to test Pulumi
        - The audience should come away with some useful ideas and tools they can use, whatever configuration formats they are writing and whatever software they are trying to configure.

    # The webinar presenters
    presenters:
        - name: Gareth Rushgrove
          role: Director of Product, Snyk

# This section contains the transcript for a video. It is optional.
transcript: |
    Welcome to Testing Configuration with Open Policy Agent. I'm Gareth Rushgrove. I'm currently the Director of Product Management at Snyk as well as that the curator of the Devops Weekly Newsletter. I'm also one of the maintainers of the Conftest Project which is part of Open Policy Agent. You can find me on the internet as GarethR. I thought I'd say hi before we kick the talk off and I'll mainly be talking to slides and showing some demos, but it's nice to hopefully see who's talking behind that.

    In this talk, I'm going to talk about policy. What is policy? Why do we care? And I'll introduce the open policy agent project too. I'm also going to talk about why is that relevant to a developer workflow? Why is that relevant in the context of cloud engineering? I'm going to touch on the importance of sharing and then we'll round up with a few conclusions. Okay, let's get the talk started. Why policy? Well, what do we mean when we say policy? Because it’s definitely an overloaded term.

    I'm fond of dictionaries, aren't we all? So, one says it’s a set of ideas or a plan of what to do in particular situations that have been agreed to officially, by a group of people, a business, organization, government, or a political party. And obviously, we're not necessarily a government or political party, though we might be, we’re mainly around this agreement— an official agreement. So what might be some examples in the context of, I guess, software. And well you might be saying, okay, all of our Go projects should be have been updated to a specific version of Go.

    Obviously doesn't have to be Go, it doesn't have to be 1.13, but you might have a policy around keeping up to date with the versions of frameworks or compilers. Maybe it's cloud infrastructure and you're saying well all of our E-C-2 instances should have tags showing which team owns them. Or, maybe it's in the context of Docker filesl, like we're saying, okay none of them should be using latest. They should all be using shards. Whatever it might be.

    These are all examples of policies, maybe their informally agreed and enforced. Maybe they're very official in your organization. Open policy agent is a— an attempt to really build a library to help service policy. And it provides a the underlying components. I sort of think— I think of it as, it's really the sort of open-source equivalent in a mature sense to the sort of half-baked policy engine we'd all make without really talking about as an engine if we didn't have something like this. It can take some data, some policy, and give you a response— give you an answer.

    Does this— does the data you're putting in match the policy? And it provides a declarative language called Rego that we’ll show some examples of to sort of describe that policy in. And it's very much optimized for, I guess, modern data structures. It's also now a Cloud Native Compute Foundations or C-N-C-F first-class project and there are a number of sub-projects as well under that, one of which I'll talk about a bit later. Coftest is a tool that originally started as something built on top of open-policy agent.

    We've recently moved this under the same project banner into C-N-C-F. And this really provides a more end-user, like, command  line interface while OPA provides a daemon and does provide a command line tool, Conftest is very focused on end-users. It's very focused on taking any sort of form of input in and providing outputs that are useful locally and— and in C-I-C-D environments. Vincent, a good friend of mine, sort of describes Open Policy Aagent in another way and this definitely resonates with me. It's my new favorite hammer. Policy is abstract, it is quite general.

    This is an advantage. This means we can apply it in lots of different places. Hopefully, we'll show you a number of examples throughout this talk. Here's one. Let's take a— the sort of ubiquitous kubernetes configuration file. Again, this doesn't have to be kubernetes, but it— we’ll use that for this example. We can write a policy against that. Maybe we're saying that in this case containers here must not run as root. We're skipping over some details, but really what we're saying here is input is the document where— is under test. Spec template. Spec security context, if you're familiar with kubernetes, is that path to, in this case, the RunAsNonRoot flag. And what we're saying is this should not be true.

    Also saying this applies to deployments. That's Rego. That's the policy language we're using to, in this case, deny something that matches it. Conftest just provides you a nice command line tool to running that policy against arbitrary input files. So here we can do Conftest test, point it at deployment YAML file, and in this case, we're failing that policy and we're getting a clear indication of that. We could send that file in via standard in, we could actually address multiple files. Conftest is quite powerful and provides that, just, good user experience over the top of the policies.

    Here the policies have been automatically picked up from the policy folder in there, but you could also point that anywhere else. And we can output that in different ways too. So maybe you prefer a sort of table view. You can also output to JUnit X-M-L or TAP for C-I-C-D integration. We also have a Json format if you're interested in doing some sort of glue integration or want to pass things out with J-Q. Let's see a quick demo of that in action. We have lots of examples in the Conftest repository, it comes with a load of different sort of tools, a lot of them relevant to that sort of cloud space.

    And I showed a kubernetes example there. So let's show a quick Docker example. So here I have a docker file, fairly standard, nothing overly clever about it, And I've got some policies. One of them is saying, okay, let's pass out the command instructions and look for FROM. Within saying— well, actually, let's get the value of the FROM instruction and we're saying, does it contain anything from our denial list? In this case our denial is just has open J-D-K. And if we match all of those things we're going to deny. So Conftest test. Docker file. And there we see, we've got an unallowed image.

    We've got a banned image in our Docker file. So if I go change my image, rerun, we're good. Again simple example, but Conftest really, it doesn't care about the inputs. We support a lot of different inputs. So docker file, X-M-L, Json, YAML, V-C-L, HOCON, Queue. I can't even remember them all off the top off— the top my head. There are a lot of inputs. If you've got a config file, we probably support it, or someone's working on a passer for it. Let's see it another quick example. The simplest framework is sort of again a popular way of deploying cloud applications.

    Here I've got a serverless configuration file and it actually has a couple of problems. Let's see what Conftest thinks they are. So Conftest test again. File. Well actually in this case, we appear to have prohibited the Python 2.7 runtime, sounds sensible, givien it's out of date. We're also insisting people provide ome tags and we can have a look at the policies there. Yeah, again examples of Rego, like saying, well if the runtime is Python 2.7, then basically deny. You can see here we're also able to build up functions in Rego that can be reused across multiple things.

    We've even got a set of utility functions. Here, has field, to make it easier to write policies. Rego is a language. It's just— it's that, it's a logic programming language rather than a more familiar, maybe object-oriented language. It's powerful and allows you to express really any arbitrary policy. Rego even has its own built-in unit testing framework. So you can write tests against those policies because you're always going to come up to that conversation of well, yes, we've written a policy, but other bugs in it. Well now you can write tests for those policies to catch those bugs.

    And sure you're testing your policies and then use your policies to test things. You've got that extra assurance. This is very much a software development too. The documentation for Open Policy Agent and learning the Rego language is also really strong. Here you can go to Open Policy Agent dot org slash docs. You'll find a lot of wealth of examples really of using it for different use cases. I'm mainly here talking about using this for sort of policy and infrastructure as code related cases, but you can apply this to all sorts of other problems as well. Authorization is a great example.

    Open Policy Agent also provides the Rego playground. This is an interactive web application. You don't have to download anything and you can just go and play around with the language. And this is also a great learning tool. Often in the community when people have questions about how to do something in Rego, people can post it here and share an example, share a worked example with input data and showing the outputs. It's a great way to get started if you prefer just to dive into trying something. Okay, so we've introduced Open Policy Agent and the Rego language and we've talked a little bit about what we mean by policy.

    But how do we fit that really into a workflow? As we talked about really we can test any configuration file or structured data with this tool set. And when you start thinking about, I guess, the both the inputs and the outputs that are surrounding us as cloud engineers, you start to find lots of places to apply this. So maybe it's your Pulumi code. Maybe it's as a resource manager. Maybe it's varnish configurations or Docker files we just saw. We saw serverless configurations, but maybe you also have envoy configurations or Circle C-I configurations or Tekton.

    Like nearly all of the tooling we're deploying is configurable and some of that configuration might just be somewhat arbitrary, but something that you might want to standardize policies around. If you're— if it's in any of the supported formats, or can be converted into those formats, you can use Conftest to test it. Anything that outputs or takes as input structured data. It's fair game. I showed you— you I was using Conftest locally there, but we also provide a number of C-I-C-D integrations. So there are GitHub Actions, Tekton Tasks in the official Tekton C-D catalogue.

    There's also— a community member wrote a Conftest of Circle C-I and there's examples with GitLab’s C-I as well and lots of other— and as a devops and really that long range of C-I systems. Any of them are definitely— whether there's a first party integration or a community one or it's just using the C-L-I, or Docker images provided. Conftest is easy to integrate into your C-I-C-D system. If you're testing with any other tools, this should be easy to add in additional tests for your configuration. Let's take an example of that by looking at Pulumi. So as a lot of people will know attending this event Pulumi is a infrastructure as code tool.

    You can write typescript, Python Go or dot net, possibly other languages later, who knows? And use that to configure and stand up and manage cloud infrastructure. So here's a typescript example creating a small stack on E-C-2. But this applies to really any cloud— really any A-P-I driven infrastructure. This definitely sounds like the type of thing that would be useful to enforce policy around. Luckily Pulumi has CrossGuard which also supports Open Policy Agent. You can actually write that test here in other languages. I'll focus on Open Policy Agent really because of the portability.

    We can use those pol— same policies with Rego and with all the tools that provides a really interesting sort of portability story. But also we can even use those policies to maybe test things direct from the A-P-I. We've got a lot more reuse out of the same policies because we're applying them to a generic toolset. It's a really nice way of Pulumi supporting something that's becoming widely used in other surrounding use cases. So, let's write some policies for our Pulumi provider. Here we are again. We're back to the kubernetes example and we’re— we're looking at metadata.

    We're wanting to say that all of our kubernetes applications should have the recommended— recommended labels. So we're setting a name, instance version, component, part of, all of these are now required based on this policy. You can see we define the set of labels and then we deny things that are not labels, that basically don't have those labels. And again, we're saying this must be a deployment. There's nothing specific to Pulumi here. This would apply exactly the same to a raw kubernetes configuration file that you wrote yourself by hand or one being output by another tool as well.

    Again, that's— that policy is portable. Pulumi has a built-in feature for us to apply that, called Policy Packs. So Pulumi Up which would normally just actually just create that infrastructure by using dash F, Policy Pack and pointing out our policy folder. Again, that folder could be named anything, that's just the default that Conftest happens to use. Before applying we see here that actually it's run that policy and failed. This deployment obviously didn't have those recommended— the label set and we've caught an error well before even, in this case, touching an A-P-I, nevermind actually provisioning that infrastructure.

    Pulumi also provides the ability in Beta to output to YAML files. So if you're— whichever the providers you're using, a few examples here with Python and Typescript like you might use it instead of talking to the A-P-Is to 0utput the files. In this case, you can use the same policy packs or you could just use Conftest against those outputted files. There's quite a lot of sort of like reuse and portability built into this tool chain. Let’s see a quick demo of that. So here I have a small Python application and a bunch of this— our policies. Let's have a look. This is the policy we saw before.

    It's enforcing the— whether we have labels on our kubernetes objects. And we have our Pulumi code in this case in Python creating a deployment. Again, you can probably— if you are familiar with Pulumi you'll see well I'm definitely not adding the relevant labels. I'm adding app, NGINX, and that's all. So I can run Pulumi Up, Policy Pack, policy. And again we’ll see it fail. Okay. Conftest is also useful for checking outputs. So maybe you have a lot of sort of files you’re writing, but you probably also have tools that will output to structured data.

    So any tool that outputs to Json or YAML or any of the other supported tools is also fair game for applying policy too. We could look at kube C-T-L is a good example here. Kube C-T-L is a tool that will allow you to output to Json or is the cloud provider C-L-Is. Most of those will also as well as give you a nice by default sort of human-friendly view. They’ll generally give you data behind the scenes. I'm going to be cheeky and show you an example using Snyk. But really this is applicable to any tool that gives you structured app output.

    So the Snyk container C-L-I allows you to test an image for vulnerabilities, again, that's not specific to any of this talk. And it allows you to output that information, that list of vulnerabilities, as a Json document. Well, we can write policies against that as well. So here I'm saying that let's get all of the vulnerabilities. Let's— and then let's say, well for each of them, let's check if the severity is high. When— if there's a high severity vulnerability, let's basically again like fail the bill, let’s deny that document from passing. We can also be a lot more specific and this is a— this is the real power of Rego and having a programming language that allows you to describe policy. We can get arbitrarily complex.

    Even these are simple examples compared to some of them that you would be able to build after a little bit of experience of Rego. Like with any D-S-L there's always a learning curve. But the simple things are reasonably straightforward once you get the model. And if you've ever done prolog before that's going to be easier or the logic programming languages. If not, try it for long enough that you get it and then try and build from there is definitely the advice I would give.

    Here we're saying that, well again, like get the list of it— get the individual issues, get the list of issues and we're looking for identifiers of a C-W-E. C-W-E, these are types of vulnerabilities in this case 3-2-7 is cryptographic issues and so here is a policy that’s saying actually, well fail on any high severity cryptographic issues. But also let's warn on any others. This is a new concept that we haven't talked about up to now, where we— where as well as just denying and saying nope, this is blocked, we can also warn. This is a Conftest idea that really like allows you to build a sort of nuanced U-I for users.

    So here is an example of something I mentioned before, but didn't show, of using Conftest to take a document on standard in. So anything that outputs Json or any other structured document format can just be piped straight into Conftest. In this case we run Conftest test, the dash saying for standard in and we get the output. So as well as thinking about writing policies for again like documents, you might write, think about outputs. It's a very flexible toolset in that sense. So we've now introduced what policy is and we've shown some examples of how you might fit that into a workflow.

    But they were generally sort of local or even in C-I. But you might have lots of projects, lots of teams, and policy is definitely one of those things that often spans those types of organizations. It's often global even, policy, Maybe it's to do with a specific regulatory regime or company-wide rules. So sharing becomes really fundamental to adopting policy at scale. So how can you reuse the things you write? The good news is we've built tools into  Conftest to really sort of help facilitate that.

    Conftest supports downloading policies from a number of different sort of remote services so you can download it directly just from Git, including downloading individual folders as shown in example here. You can download just from an H-T-T-P server. So if you want to, if you have a file stored somewhere or anything that's downloading that— allowing you to upload files and directories over FTP or it natively supports S-3 as well. So you can very easily pull down policies from different places. If you want everything into a Git repository that will work. If you want to have releases somewhere and package them up that will work too.

    We also support for that workflow and O-C-I images. So if you have a container registry or you're using one of the like globally distributed container registries from the cloud providers, you can generally pull that— store policies there and pull them down using  Conftest. And  Conftest also supports pushing policies there that packages up to the OPA bundle, which is how policies are shared. And it adds a bunch of metadata that means the registries can index and install that correctly. This is all powered by the new O-C-I artifact specification that opens up registries to sharing really arbitrary content but in a structured way.

    Open Policy Agent and Conftest were one of the first implementers of that on the client side and increasingly a lot of the registries are starting to support that. This is really opening up. It's sort of like being able to reuse how we share container images for other tooling, in this case the policy agent. Definitely worth checking out. And last but not least that Pulumi itself has a sharing mechanism built in, really sculpted to organizations. So the example we share before where I could specify the policy locally. Maybe it's not up to me. Maybe it's up to a central security team about which policies I need to adhere to. And if I can skip out of those by simply pointing that at different directory or not doing dash dash policy path. That's not good.

    So with Pulumi we can do Pulumi Policy Publish that will publish things centrally. We can then Pulumi Policy enable that policy and that will affect all runs of Pulumi Up. Whether they're running with Policy Pack or not centrally. You can't work around that then. So built into the Pulumi service is a useful tool for sharing Pulumi based policies that are using open policy. Okay, so rounding up, like if all you take away from this I guess is that configuration needs tests too. We write a lot of configuration. We write a lot of infrastructure as code. And it definitely benefits from everything we've learned from software development.

    And that's not just down to testing and in this case using sort of policies. It is true of other software— the other aspects of software development as well. So introduction C-I, thinking about refactoring. Thinking about code quality and repetition and refactoring. But definitely like adding test into your configuration and your infrastructure as code, helps you go faster by making you safer. Looking at OPA specifically as a approach to solving some of those problems, I think it's useful to think about the fact that that's useful for lots of different cases. Lots of tools historically have come with a testing approach. They've come with built-in testing tools or community provided ones.

    But then when you move to a different tool, it's a different testing tool and— and the reality on the ground for most cloud environments is you're not just using one tool. You're using all of them. OPA opens up that idea that maybe we can standardize in a different way. The policies we write can be portable between different tools that are doing the same thing. Again, that could be a huge time-saver later as well as making it easier to move between different tools and lowering the cost of adoption. Ultimately, conversations around policy of generally being in meeting rooms and with documents and really the implementation of that has been left as a separate thing later to maybe never happen. I think policy needs to shift left.

    We need that conversation about policy to be part of what we talk about as engineers building cloud environments or ultimately building applications. Thank you for listening. If you did like this talk do feel free to sign up for Snyk for free over at Snyk dot IO slash sign up. And if you do have any questions about this, I'm @GarethR pretty much everywhere on the internet. Thanks for listening.
aliases:
  - /resources/testing-configuration-with-open-policy-agent
---
