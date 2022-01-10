---
title: "Pulumi and LocalStack — beyond the basics"
date: 2022-01-10T11:10:06-06:00
draft: false
canonical_url: https://delitescere.medium.com/pulumi-and-localstack-beyond-the-basics-d993f3b94d17
meta_desc: A review of using Pulumi to spin up a LocalStack environment using good engineering practices.
meta_image: meta.png
authors:
    - josh-graham

tags:
    - aws
    - community

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
---
Recently, Pulumi community member Josh Graham decided to bootstrap a simple application using a serverless approach, with a focus on using good engineering practices and being able to run the application locally. Given that Josh is the (OG) SaaS architect of Atlassian and an AWS user, [LocalStack](https://github.com/localstack/localstack#overview) was a natural choice.

<!--more-->

## Introduction

I first encountered [Pulumi](https://www.pulumi.com/) a few years ago when I was getting a little frustrated at the lack of some expressibility in [Terraform](https://www.terraform.io/). I've been using Terraform from almost day 1 and it really does the job well --- providing you really grok its declarative nature, are very good at modularisation, and never need an escape hatch to non-declarative instructions. At the time, though, Pulumi wasn't ready for me to use, so I watched from a distance.

Recently, I decided to bootstrap a simple application using a serverless approach, making it a good opportunity to try Pulumi again. I still wanted to use good engineering practices and be able to run the application locally. As I was the (OG) SaaS architect of Atlassian and am an AWS user, [LocalStack](https://github.com/localstack/localstack#overview) was a natural choice.

Pulumi has come a long way since I first saw it. I am super happy with it so far and I'm using it for real infrastructure work at the startups I'm working with. It seems the software engineers have less cognitive load using a more familar language to express infrastructure definitions. It is worth noting that Pulumi uses Terraform in various ways under the covers and I'm still a big fan of Terraform and Hashicorp in general.

## The Application and its Infrastructure

The application I've based the following sample on is a website with a simple form to capture a visitor's email address, responding with a cookie to set so the site knows not to bother showing them a form the next time they visit.

In keeping with a serverless goal, I use AWS DynamoDB to store the information. I also want to be able to query for the latest new contacts. In order to try out Pulumi more thoroughly (and although I'm no fan of NodeJS), I decided to do the backend on NodeJS in an AWS Lambda so as to try out the Pulumi Cloud API. Both the backend and the infrastructure-as-code with Pulumi are coded using TypeScript.

There's lots more to the application, but the extract in the following sample is sufficient to showcase #Pulumi and #LocalStack using a #TDD approach to #IaC for #serverless apps.

## The Sample

Unlike every sample or blog I found for either Pulumi or LocalStack, I wanted to organize the code properly. Inevitably, most samples did nothing other than return a simple string as a repsonse (a distributed "hello world"). Otherwise, everything I found was one big file with no cohesion and no separation of concerns. Even worse, the samples mix the IaC "deploy/provision-time" code with the application "runtime" code in the same file. Exactly zero had any tests, let alone ones that were written to specify the expected behaviour.

I've divided this article into various sections depending on what you're wanting to focus on.

- Modularized Pulumi
- Running Pulumi locally with LocalStack
- TDD infrastructure code and an AWS Lambda calling DynamoDB

If you'd like to follow along or use parts as a template, you can fork the [repository](https://bitbucket.org/delitescere/contact).

### Acknowledgements

Grazie mille to my former ThoughtWorks colleague [Toni Terreno](https://twitter.com/javame) for reviewing the article and the code to help smooth out some wrinkles.

## Modularized Pulumi

As with any Pulumi project, it is defined by a [Pulumi.yaml](https://bitbucket.org/delitescere/contact/src/main/Pulumi.yaml) file. I've split the "infrastructure code" --- the code that drives Pulumi --- apart from the application code. This infrastructure code is in the [infra](https://bitbucket.org/delitescere/contact/src/main/infra/) directory. So, the [package.json](https://bitbucket.org/delitescere/contact/src/main/package.json) also specifies a `main` (even though this app isn't a module for others to include) for `pulumi` CLI to find the Pulumi entry point.

## Outputs / Inputs

There's probably a good reason most samples that show how to use Pulumi are one big file. That's because it can be initially difficult to grok the concept of provision-time "output" and "input" values. This isn't isolated to Pulumi --- I've seen similar problems with examples (and real code) with other IaC tools like Terraform, Puppet, and Chef. It's not a big surprise, either. When thinking imperatively or defining infrastructure manually we tend to have a different mindset to the one required to think declaratively.

Despite the documentation, it can be quite confusing and becomes even more so when you deviate from the "one big file". It can become positively baffling when, as this application does, the infrastructure code is aware of the application code and performs the deployment of the application as part of the infrastructure update. I wanted to test the application logic separately from having to run Pulumi, so that separation of code was essential.

The big thing to remember is that a Pulumi "output" value [is not known until after the infrastructure has been fully provisioned](https://www.pulumi.com/docs/intro/concepts/inputs-outputs/). They are a promise of a future value. If you want to refer to the value in other infrastructure code, Pulumi creates a dependency graph to be able to resolve the value at the right time. If, however, you want to refer to the value at runtime and you want to define that runtime code in a modular way, you have to be very clear about how that value is presented by Pulumi to that runtime code.

Our infrastructure code provisions a DynamoDB table and an AWS Lambda. That Lambda needs to know the name of that table at runtime in order to query it. Because the *actual* name of the table isn't known until provisioning is underway (Pulumi creates many infrastructure resources based on the logical name but with suffixes to avoid naming collisions), we need a way to get the "output" table name from Pulumi's `aws.dynamodb.Table` [API](https://www.pulumi.com/docs/reference/pkg/aws/dynamodb/table/#example-usage) to the Lambda we'll create with the "simpler" way to create a Lambda using Pulumi's `cloud.API` [API](https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/cloud/#API).

You'll see in the [ContactApi](https://bitbucket.org/delitescere/contact/src/main/infra/contact/api.ts) infrastructure resource an `Inputs` class with `static` members. This is the key to transferring, in the simplest way I've found, values from provision-time infrastructure code to runtime application code. This class is only available in that file, so for each resource that needs to pass provision-time values to runtime code, you can create one specifically for the values you want to pass.

In the case of `ContactApi` we receive a `Table` as an "input", convert it to an "output" and store it in a static variable. This variable is then used in the constructor for our `Lambda` application class when wiring up the integration between the API Gateway route / method and the Lambda. The way the `Lambda` constructor is called in the infrastructure code is the same as we'd do from a test or any other application code that wanted to call it.

I played with various ways to transfer Pulumi inputs to runtime code but this was the most intentional, most decoupled, and least convoluted.

### Resources

As mentioned above, we provision a DynamoDB table, an API Gateway, and a Lambda.

We could (and indeed I originally did) provision the table with the "simpler" `cloud.Table` [API](https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/cloud/#Table) but I wanted specific control over the attributes and secondary indexes for DynamoDB (so I could, for example, query for new records since a particular date). The `cloud.Table` abstraction works across cloud platform providers, and there may be mechanisms to offer finer-grained / platform-specific options (but I haven't found them yet).

We do provision a Lambda, *but with the actual simplicity of this application's needs, we could dispense with the Lambda and have the API Gateway do a non-proxy integration straight to DynamoDB's HTTP API*. Given many applications would include a Lambda somewhere along the way, I thought it was worth showing Pulumi provisioning a Lambda and integrating it to an API Gateway using it's `cloud.API` abstraction.

### AWS tags

Because we're using AWS, we can set default tags on taggable resources. These can be put into the configuration file (`Pulumi.<stack>.yaml`) which is great for static / non-computed, optional tags.

If we want to ensure certain tags are applied, even if they were omitted from the stack-specific configuration, or the tag keys or values are computed, then we can use the `registerStackTransformation` method of Pulumi runtime. Our `[registerAutoTags](https://bitbucket.org/delitescere/contact/src/main/infra/registerAutoTags.ts)` (based on some code by Joe Duffy) function does this nicely for us, while including resource-specific tags and overrides.

## Pulumi + LocalStack

Using LocalStack to emulate AWS services on your local machine is a great way to get faster feedback, isolate errors, and reduce costs. It's obviously not a perfect emulation but for most purposes, it is more than sufficient.

### Stack templates

Because Pulumi doesn't ([yet](https://github.com/pulumi/pulumi/issues/2307)!) support project-wide configuration, I have a project-wide template `stack.template.yaml` (for any stack) and a local stack template `local-stack.template.yaml` (just for stacks targeting LocalStack).

These templates are merged and interpolated with shell environment variables in the `init-local-stack` script. Keys in the local template override keys in the non-local template.

You may wish to use a similar technique to the `concatAndInterpolateTemplates` function for non-local stacks. Perhaps each engineer has their own stack, but you have configuration keys that everyone should set, that either have common values or machine-specific values. In combination with various `.env` files (including `.env` files per-stack), this could be quite useful for those of you, like [Tony](https://twitter.com/javame), with many engineers (who have a stack each) and also many shared stacks.

In a subsequent article, I'll write about how to set things up if you're using multiple AWS accounts, across multiple regions, each with multiple VPCs.

### Dockerized Lambdas

One issue I encountered was because the Lambda I wrote uses the NodeJS runtime, LocalStack will create a Docker container to run it in. While much of the necessary environment was copied to that container, a subtle bug in LocalStack's Lambda executor failed to include the AWS credentials in the environment. This meant that any other resources the Lambda needs to access (like a DynamoDB table) would fail to authorize as the requests could not be authenticated. I fixed the bug, added some tests, and the behavior is now correct from LocalStack version `0.12.16` (available since 1 Aug, 2021.

Using the included [docker-compose](https://bitbucket.org/delitescere/contact/src/main/docker-compose.yml) file, when you `docker compose up --detach` you will have a LocalStack container running with the requisite faked AWS services for this application.

If you ever want to get a shell into that container, you can either use standard `docker compose exec` commands if you didn't install `localstack`, or use `MAIN_CONTAINER_NAME=$(basename $PWD)_localstack_1 localstack ssh` if you did install it (you don't *have* to install it because Docker Compose is handling it for you).

The docker-compose file also mentions what to change if you're going to be doing lots of tests / Lambda invocations. In this case, you pay the price of a slower `pulumi up`---because the Lambda creation is writing lots of files, particularly `node_modules`--- to the file system. If that is being synchronized to the host file system, in my single Lambda case, the infrastructure creation time goes from about 20 seconds to about 50 seconds. However, you get back time in Lambda invocations when `LAMBDA_REMOTE_DOCKER` is falsey which takes off roughly 1/3 of the time to execute a Lambda.

## TDD Infra + Lambda + DB

This test set up might not look like many JavaScript projects you've encountered. We have "unit" tests segregated from "functional" tests. If we had more things to test, I might have "integration" tests, too.

If you're curious about the different approaches to unit testing I've employed here, please read the excellent (now almost two decades old!) ["Mocks aren't Stubs" article](https://martinfowler.com/articles/mocksArentStubs.html) by my friend and [Thoughtworks](https://medium.com/u/8075bdd73dd9?source=post_page-----d993f3b94d17-----------------------------------) Chief Scientist, [Martin Fowler](https://twitter.com/martinfowler).

### Unit tests

These are "pure" logic tests requiring just the JavaScript class under test and test-doubles for infrastructure dependencies.

In the case of our contact `Table` class, we mock the DynamoDB SDK and stub responses from its `getItem` and `putItem` methods to match the case we want to test. In the case of our contact `Lambda` class, we mock its`Table` class and stub responses from its `findOne` and `insert` methods, and we also need to mock the Pulumi Cloud API's `Request` and `Response` classes.

Although the infrasructure-as-code in our project driving Pulumi is fairly declarative and therefore doesn't really need testing, we do have a little logic that should be tested. In those cases, Pulumi provides the capability set mocks for testing purposes so you don't have to be running the Pulumi engine for unit tests.

Unit tests can be run with `npm test unit`.

### Stack class

We've abstracted the notion of a "stack" into something that is useful in the context of having using LocalStack or a real AWS region, and having "production" and non-production environments. *As mentioned earlier, things can get a lot more complicated than that for more sophisticated AWS users, which I'll write about in a subsequent article.*

In the jest config we include `tests/env.ts` as a setup file. This sets the environment variables before imports and static initialization, allowing us to test things like `aws.config.region` having been set from the environment. You can also set this value in the `Pulumi.<stack>.yaml` file.

We use the `pulumi.runtime.setMocks` function so that we can mock the parts of Pulumi called by our `Stack` class (`getProject` and `getStack`). We now specify the logic for when a resource is qualified by the stack name (e.g. `contact-sandbox` for the sandbox stack versus `contact` for the production stack), and also for when a DNS record is qualified by the stack name (e.g. `www.example.com` for the production environment record but `www.test.example.com` for the test environment record).

### Result type

I don't particularly like the JavaScript approach to Promises and [its many flaws](https://avaq.medium.com/broken-promises-2ae92780f33). However, as this exercise is for a fairly simple function-as-a-service, I didn't want to go down the path of using a replacement approach like [Fluture](https://github.com/fluture-js/Fluture). I did, however, want to work with the results of promises using a something approximating a sum type and be able to transform exceptions and rejected promises into the "not right" side of that type.

The `Result` type uses lightweight type checking and convenience methods. All the Promises we are working with end up resolving to a `Result` which is either an `Error` or a non-error value. We're careful to catch rejected Promises or exceptions and turn them into a resolved `Promise<Error>`or `Error`.

### Table class

The `Table` class in `contact` only has two methods so far, `findOne` and `insert`, because that's all the application needs right now. You can imagine other applications might need other typical methods like `find`, `findOneByEmail`, `delete`, and so on.

To use this class in a unit test, we need to mock the `DynamoDB` client and provide various stubs for its `getItem` and `putItem` methods. Each of these stubs tests a different code path in how `Table` handles responses from the database.

If we had more than one table to interact with, there'd probably be an interface and perhaps an abstract class or other mechanism of providing behavior common to all tables.

### Lambda class

Given the combination of inputs to the lambda and processing issues that may arise, we want to be able to test the lambda behaves in the expected way and handles those issues as specified.

We provide stub responses on the `Table` class methods to stimulate successful and unsuccessful operations. We also stub the input to the lambda (because we're using the Pulumi Cloud API this is a `pulumi.cloud.Request`) to initiate different logic in the lambda.

The result of the lambda is a `pulumi.cloud.Response` which we mock to capture the HTTP status code generated, which is sufficient to verify almost all of the behavior of this lambda. The other thing we need to verify is that a HTTP cookie is set when either a new item is created or a matching previously created item is found.

### AbstractLambda class

Here are some convenience methods that lambdas might generally use. We have two for dealing with when the lambda is running on LocalStack and two for working with HTTP request headers and JSON entities.

Normally, the "endpoint" for AWS is left undefined, which is interpreted bu the AWS SDK as "use the default for the region". When running in LocalStack, however, we set it to the URL that LocalStack is listening to on our local machine.

When running locally, we also include error information in the HTTP Response to help make diagnosing issues during development easier. *(I'm still shocked that the NodeJS*`Error`*has non-enumerable properties that mean*`*JSON.stringify*`*is useless on instances of it).*

To handle the situation where, depending on the HTTP client's approach and because the NodeJS libraries don't normalize for us, the same HTTP request header may either be repeated in the request or have been concatenated with multiple values (with some delimiter, usually a comma), we have a convenience method to deal with that.

To avoid lots of conditionals and error checking when parsing the request entity, we have a convenience method to parse it as JSON. I hope you like the Easter Egg in the test [Tommy Hall](http://www.thattommyhall.com/) and Dave Coombes 😆

### Functional tests

These test the application as it would be used in production. The infrastructure must be set up, the application must be running, and the tests interact with the application like a user or integrating system would.

The `[bin/test](https://bitbucket.org/delitescere/contact/src/main/bin/test)` script does the heavy-lifting of starting LocalStack, initializing a Pulumi stack for testing, running the Jest tests, and pulling everything down again, all handily invoked directly or more likely just with `npm test`.

If something goes wrong with the tests, or you use `KEEP_TEST_STACK=1 npm test`, the Pulumi test stack and LocalStack container stays around for diagnostic purposes.

I have found that this test can be "brittle" due to timeouts when the LocalStack container is low on resources, or your computer is running slow and the Pulumi automation API results are slow (it seems exec'ing a `pulumi stack outputs` command from the test is more efficient, albeit clumsier).

Use `docker compose down --volumes` to totally clear out the LocalStack environment.

### Contact resource

Given everything else has been tested in unit tests, this functional test doesn't need to do much. However, it gives us confidence of the following:

- that Pulumi has hooked up the API Gateway and Lambda properly
- that LocalStack is emulating the AWS services we need sufficiently well
- and most importantly, that our Lambda actually does talk to DynamoDB correctly at runtime (as the unit tests have mocked this out)

That's it, I hope this has given you some hope that your Pulumi code doesn't have to be a big ball of mud, and that using LocalStack to try it out before hitting AWS is straightforward.

*This article was originally posted at [https://delitescere.medium.com/pulumi-and-localstack-beyond-the-basics-d993f3b94d17](https://delitescere.medium.com/pulumi-and-localstack-beyond-the-basics-d993f3b94d17). Reposted here with permission.*
