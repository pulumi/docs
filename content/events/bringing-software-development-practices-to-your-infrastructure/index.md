---
# Name of the webinar.
title: "Bringing software development practices to infrastructure"
meta_desc: Learn how to use practices from software development like test driven development and CI/CD to manage complexity at each stage of cloud development.

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
url_slug: "bringing-software-development-practices-to-your-infrastructure"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Bringing software development practices to your infrastructure"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Bringing software development practices to your infrastructure"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/PgmsiIfbC64"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T14:30:00-07:00
    # Duration of the webinar.
    duration: "20 minutes"
    # Description of the webinar.
    description: |
        The cloud makes it easier and quicker to provision infrastructure at scale, but there is added complexity with that scale. By bringing practices from software development like test driven development, automated testing, and continuous integration/deployment to manage complexity at each stage of the pipeline, you can build and manage your cloud resources more effectively, consistently, and more securely.

    # The webinar presenters
    presenters:
        - name: Jenna Pederson
          role: technical entrepreneur with a passion for community and equity-building

# This section contains the transcript for a video. It is optional.
transcript: |
    Hi everyone.  Thank you for joining me today at cloud engineering summit.  My name is Jenna Pederson, and I'm a software engineer, turned developer advocate at Amazon web services.  I've been writing software for over 20 years.  And today I'm excited to talk to you about one of my favorite topics, software development best practices, or more specifically automated testing.

    So let's just level set a little bit.  Infrastructure as code lets you automate deployments of your infrastructure to facilitate scaling and quicker repeatable deployments and it's code.  So because infrastructure as code is actually code.

    This means that you can version control it, code review it, test it, push it through the different stages of a CICB pipeline.  But what happens when something goes wrong? So it might work on your machine or your account or your region.  And you've probably already gotten this works on my machine badge, but when it's broken, it's broken at scale, the blast radius is much wider and it impacts more resources, regions, customers, and dollars.  So in the next 20 minutes, we'll talk about treating your infrastructure as code, as code and minimizing that blast radius.  We'll talk about the different types of testing using test driven development, to make sure you're building what you need and only what you need.

    We'll talk about testing your infrastructure directly.  So what's provisioned, to make sure it was created correctly.  And then we'll talk about integrating all of this into a CIC pipeline.  So we know that the cloud makes it easier and quicker to provision infrastructure, but there's complexity with that scale.  Infrastructure as code is one way that we manage that complexity, automated testing is another way we can manage it by building quality in from the start, just like we do with our application code.

    We can have confidence in our infrastructure at scale and at velocity.  So when we talk about bringing testing to our infrastructure, it's still really important to consider the different kinds of testing to use.  Just like we do when we build a test strategy for our application code.  So this is a variation of the testing pyramid that's been around for years.  Tests at the bottom of this pyramid are cheaper and easy, easier to create and they give us quicker feedback as to when something has gone wrong.

    They're more finely grained and generally should be testing only one thing or a unit.  Test at the top of the pyramid are more expensive to write, to run.  And they're more brittle and harder to maintain.  In the case of infrastructure testing test towards the top of the pyramid are more complex because it involves spinning up and tearing down cloud resources and tests that have to query that infrastructure.  So we really want to balance fast and cheap tests with those that are closer to the real infrastructure and production environment and therefore reflect reality.

    So if you're test driving your application code, why wouldn't you do the same for your infrastructure code? So remember some of the benefits of test-driven development are that we have reduced defect rates.  We can improve the overall design of what we're building.  We can test in development.  It keeps you focused on requirements.  So you only implement what you need and nothing more.

    It keeps you focused on small chunks.  So you make sure that just those chunks work and it can also serve as documentation.  So communicating requirements to your team.  And then finally it gives you confidence in what you're building.  So this is the flow for test driven development.

    You can follow the same red, green refactor that you do.  When you write your application code.  First, you write a failing test.  Then you write only enough production code to make it pass.  And then you make it better.

    In the examples that I show, in just a little bit, we'll follow this approach.  So let's talk a little bit about those cheap and fast unit tests.  A unit test exercises, a small part of your application or one unit.  And it verifies that it's correct.  Unit tests are quick.

    They can be run frequently and they help us get feedback early on.  So we can shorten that feedback loop.  They help us communicate requirements to our team as well.  They can also be run in your CICB tool.  And then finally, traditionally unit tests are isolated from other resources like external APIs and databases.

    And this reduces the scope and the number of variables that can affect the results.  We can also apply the same process to infrastructure code.  We don't need to provision all of our infrastructure or even a little part of it to test that our code configures it correctly.  Now a unit test checks, if a resource will be created with the correct configuration.  It checks that the number of resources is created.

    The correct number of resources is created.  It checks if the dependencies between resources are correct and then a chapter of interpolated values are correct.  So let's see it as an action for this first demo.  I want to show you that it's possible to test drive your infrastructure code.  For context, this is an AWS cloud development kit or CDK, and we want to create a private S3 bucket with encryption enabled by default, we're going to write a failing unit test with the adjust framework.

    We'll write our infrastructure code, which is our CDK code, and then we'll make sure that our test passes.  So the first thing that we're going to do is write our test.  So we've already got this stubbed out.  I'm going to add a code to create the S3 bucket stack that we're going to write in just a minute.  So I give it an identifier, as three buckets stack, and then I'm going to add some expectations on this stack.

    I want to make sure that the stack creates S3 bucket, and then I want to make sure that this bucket has a bucket name.  And I want to make sure that bucket encryption is enabled by default.  And then lastly, what we're going to add this import for the stack that we're going to write in just a minute.  So if we go back to the terminal and run our test, we can see that there's actually a compilation error here.  And that has to do with this import that I just added.

    It's failing because we haven't created our production code yet.  So I'm going to go ahead and create the S3 bucket stack file.  We'll create the class and we'll implement some of the boilerplate code specifically around the constructor.  And then inside of this constructor, we're actually going to, this is where we're going to create our resources.  So we're going to create a new S3 bucket.

    We'll give it an identifier.  And that identifier is for how we reference it in this code.  We give it a bucket name and we'll block all public access.  And now that we have our test, we can go back and run that again to see if it passes and it turns out it doesn't pass.  We can see that it's missing bucket encryption.

    We forgot to do that.  So now we're going to add that encryption back in to fix our test.  So we add properties to indicate that we want bucket encryption to be enabled by default.  And then we'll rerun our test and we can see that it's passing now.  Now that we have our infrastructure code and it's tested, we can apply it to create our resources in the cloud.

    We could go into the AWS console to check on the state of those resources and manually verify that they were created correctly.  But how do we know that it's really correct? And how do we know that it's what we wanted to create.  And more importantly, how do we do that at scale? Can you imagine having to manually check a hundred as three buckets, across, across different regions and accounts to make sure that they're set up properly, that's a lot of manual work.  And if you remember our test pyramid manual tests are expensive and time consuming.  So if we want to limit them, and this is where integration tests come in.

    So integration testing is a form of testing where we test the India interactions across different units or modules, or in the case of infrastructure testing.  we're testing across different cloud resources.  They allow you to verify that your provisioned cloud resources are created and configured as you expect them to be.  So, as I mentioned earlier, the cloud makes it easier to scale, but it adds complexity.  So integration tests can give you confidence in your infrastructure at scale and at velocity.

    `So in the next example that I'm going to show you we'll use chef InSpec, which is an open source framework for testing and auditing your infrastructure.  You can execute and write tests with an easy to read domain specific language or DSL on remote systems like servers, containers, and cloud resources.  These tasks can be used on any machine or resource, regardless of whether it's managed by chef, the AWS CDK polo me, or even manually by a human.  They can be used across teams too.  So for instance, your security team can set up their own rules and impact levels.

    And if tests path can fail or pass based on that impact level.  So in this demo, I want to show you that its possible to test your infrastructure directly, and you can even test drive those tests along with your unit tests.  For context, this is another AWS CDK app.  There's an easy two instance and some related resources already tested and provisioned.  And now we want to add a database to the app.

    We're going to write a failing test with the inspect framework, we'll update the infrastructure code, and then we'll make sure both our unit tests and infrastructure test pass.  And if you're familiar with our spec unit tests from Ruby, these Inf inspect tests will be familiar because InSpec is built on top of our spec.  So the first thing that we'll look at here is the unit test that we've already written.  We are making sure that we have an easy two instance configured correctly in the stack and elastic IP configured correctly in the stack.  And then we're also making sure that we have an RDS database and it's configured correctly.

    The last test that we have here is to make sure that we have outputs from our staff that we can use in our inspect tests.  So we go back to the terminal, we run our unit tests.  And we do have a failure specifically on the RDS database instance.  And that's because we haven't implemented that in our production code yet.  So if we go back and look at our production code, the stack out, we've configured our easy two instance in here and there related infrastructure, we've added a web app security group with different ingress rules, the elastic IP address.

    And we've also added some outputs, instance ID.  And we've also added a web security group idea that we'll use in our inspect house later.  So we've already created the inspect control and here we're setting the impact to one we've given it a title we're importing those outputs from our stack so that we can use them in this test.  So I mentioned instance ID in web security group idea before, and then we're also making sure our ECE two instance is running.  It's the right image ID and instance type we've.

    We're also making sure that the security group has the right, allows the right traffic in.  So we'll update this inspect test to add our database verification.  And we've added the instance identifier and database security group ID from the outputs.  We're going to make sure that our database security group allows the right traffic in.  So Poststress expects traffic on port 5, 4, 3, 2, and then we'll also add a test to make sure that the RDS instance is set up and configured correctly.

    We want to make sure, that in this case, we're just going to verify that the engine is correct.  The engine version is a specific version, and then we've used the right instance class.  So we'll go back to the command line.  We will run our inspect tests and we can see that we have one failure.  And again, this is because we don't have our production code implemented specifically.

    It doesn't know where those parameters are to use in our test.  So we import the AWS RDS library.  And we're going to add some code in here to actually create our database instance in our, in our stack.  So we've set up the sub-net, we've given it an instance identifier, we've set the engine and engine version.  We've allocated some storage.

    We've given, given it a tag.  And then we're going to set up the connections or the security groups so that it allows traffic on a specific port 5, 4, 3, 2 is what we're expecting here.  And then we also want to add an output for this database instance identifier so that we can run our tests.  Our inspect test specifically, and addition to the database identifier, we'll also do the database security group ID so that we can run some tests against that as well, to verify that that's set up correctly.  So now that we have our infrastructure code actually written, we'll go back to the terminal and we're going to run our unit tests to make sure that we've implemented our production code correctly.

    And it looks like we have, and then we're going to synthesize, synthesize the CDK app and deploy the CDK app stack.  And we'll pass in a couple of parameters here, and then we're going to set the outputs file to be a specific file that our inspect tasks will be able to read from later on.  And this takes a little bit, so it's sped up.  And when it's done here, we'll see that it's successful.  It's created our full stack app, its output that information, and now we can run our inspect test.

    So this test again, it's going directly against our AWS resources and we can see that RDS database, it now exists.  It's configured correctly.  You might be wondering Jenna, we've built all these infrastructure tests now, what do I do with them? That's a great question.  Today your process might look like this.  If you're not doing any sort of infrastructure testing.

    You find your issues in production or maybe you don't find them at all, And your customers find them.  Infrastructure as code plays a key role in CICB and it relies on infrastructure automation to create consistent environments.  So you can be confident that what you built works in each environment and for your customers.  When you automate your infrastructure tests, you can also put your infrastructure code through the same CICB pipeline.  You can iteratively develop, run these automated tests and deploy your infrastructure through each environment.

    Just like you would your application code by moving our infrastructure testing earlier in the pipeline, by shifting it left and doing it at every stage, you're going to find bugs earlier in the process when they're cheaper and easier to fix.  Now, I just want to leave you with a few parting thoughts.  First of all, infrastructure is code.  We should be treating it as such.  We code review it, version control it, test it, push it through the CICB pipeline.

    Second.  Even if you're not testing in production, your customers certainly are.  And last the earlier you catch bugs, the cheaper its going to be to fix.  Thank you all for joining me today.  If you have any feedback, please take the survey at this QR code or send me a message on social media.

    I appreciate any questions and a follow there as well.  And I'm looking forward to the fireside chat next.  Thank you.
---
