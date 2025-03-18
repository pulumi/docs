---
title: How to Create and Share a Pulumi Template
date: 2022-12-12
meta_desc: Learn how to design and build Pulumi project templates and share them with others on GitHub.
meta_image: meta.png
authors:
    - christian-nunciato
tags:
    - templates
    - yaml
    - aws
---

Last month, we released our first set of [architecture templates](/templates/) --- configurable Pulumi projects designed to make it easy to bootstrap new stacks for common cloud architectures like [static websites](/templates/static-website/), [containers](/templates/container-service/), [virtual machines](/templates/virtual-machine/), and [Kubernetes clusters](/templates/kubernetes/). Architecture templates are a great way to get a new project up and running quickly, and they've already grown quite popular with our users, several of whom have asked if whether it's possible to create templates of their own.

It's not only possible, it's surprisingly easy! So in this post, I'll show you how. It all starts with a Pulumi project --- a template is really just a Pulumi project with a few extra lines of config --- so we'll start with one of those, add a few resources, and turn the project into a template. When it's ready to go, we'll test it out locally, and then finally, we'll publish it so that anyone with Pulumi can use our template to kickstart their own projects.

We'll do this in five steps:

1. [Create a new project](#create)
2. [Design and build the program](#write)
3. [Turn the project into a template](#templatize)
4. [Test-drive the template locally](#test)
5. [Publish the template](#publish) to share it with the world

Let's get to it.

## Step 1: Create a new project {#create}

If you haven't already, make sure you've [installed Pulumi](/docs/install/) and [configured your AWS credentials](/registry/packages/aws/installation-configuration/). For this example, we'll be using [AWS](/registry/packages/aws/installation-configuration/), but the process is the same for any cloud provider, so if you aren't set up on AWS, you should still be able to follow along anyway.

Create a new project in the usual way using one of our starter templates. The YAML template is a good choice for this walkthrough, as YAML projects are simple and lightweight (no runtime dependencies!), and because they combine both project and program into one file, they're especially conducive to sharing:

```bash
$ mkdir my-template-project && cd my-template-project
$ pulumi new aws-yaml
```

Step through the prompts, choosing whichever AWS region works best for you. When the new-project wizard finishes, open the generated `Pulumi.yaml` project file in your editor of choice to start building.

## Step 2: Design and build the program {#write}

I'm a static-website person, myself --- I think pretty much everyone should have one. So in order to realize my grand vision of home page for every human, you and I are going to build a Pulumi project template that lets anyone with the Pulumi CLI deploy a super-simple website of their own on AWS.

As Pulumi template authors, our general goal is twofold:

* Make it easy for our users to create deployable projects that address an infrastructural need.
* Make it easy to customize and extend those projects after they've been created.

A good template, in other words, is one that not only takes you from `pulumi new` to `pulumi up` in as few steps as possible, but that also leaves you with an open, extensible program you can use as a foundation to build upon. For us, the goal is to create a template that can be used to provision the minimal set of cloud resources one needs to run a static website on AWS. And done well, our template will also lend itself easily to further development --- custom domains, serverless functions, edge caching, and so on.

To that end, let's start by replacing the contents of `Pulumi.yaml` with the following program, which defines the core resources we need: an [S3 bucket](/registry/packages/aws/api-docs/s3/bucket/) to hold the files of the website and an [S3 bucket object](/registry/packages/aws/api-docs/s3/bucketobject/) (`index.html`) to serve as its home page. We'll also export the computed URL of the website as a Pulumi [stack output](/docs/concepts/stack/#outputs) to give us something to navigate to after deployment:

```yaml
name: my-template-project
description: A simple static website on Amazon S3
runtime: yaml
resources:

  # Create an S3 bucket and configure it as a website.
  bucket:
    type: aws:s3:Bucket
    properties:
      acl: public-read
      website:
        indexDocument: index.html

  # Create a home page for the website.
  index.html:
    type: aws:s3:BucketObject
    properties:
      bucket: ${bucket.id}
      acl: public-read
      contentType: text/html
      content: |
        <html>
          <meta name="content" charset="utf-8">
          <title>My Awesome Website</title>
          <body>
            <h1>My Awesome Website</h1>
            <p>Hello, internet person! 👋</p>
          </body>
        </html>

# Export the URL of the website.
outputs:
  url: http://${bucket.websiteEndpoint}
```

Try running this program now, just to make sure everything works. In a few seconds, you should see that the new resources were created and be able to browse to the new website at the exported `url`:

```
$ pulumi up
...

Updating (dev)

     Type                    Name                        Status
 +   pulumi:pulumi:Stack     my-s3-website-template-dev  created (3s)
 +   ├─ aws:s3:Bucket        bucket                      created (2s)
 +   └─ aws:s3:BucketObject  index.html                  created (0.37s)

Outputs:
    url: "http://bucket-f1bb181.s3-website-us-west-2.amazonaws.com"

Resources:
    + 3 created

Duration: 5s
```

Good --- we have a working program. And looking back at our design goals, you'll see that this program already meets them pretty well:

1. It works out of the box. Deployed now, it produces a running website on AWS.
2. It's open and extensible. To build onto it --- add more pages, attach a custom domain, etc. --- you'd simply add more resources alongside those already defined.

Now let's turn this program into a template.

Before moving on, though, let's quickly destroy and remove this stack, as we'll be making a few changes to the project's settings in the next step, and it'd be better to begin from a clean slate:

```bash
$ pulumi destroy --yes --remove
```

## Step 3: Turn the project into a template {#templatize}

The next thing to do is decide which parts of the program should be configurable. Earlier, when you ran `pulumi new aws-yaml`, you probably noticed you were prompted for an optional AWS region:

```
$ pulumi new aws-yaml
...

This command will walk you through creating a new Pulumi project.
...

aws:region: The AWS region to deploy into: (us-west-2)
```

You got this prompt because the authors of the [`aws-yaml` template](https://github.com/pulumi/templates/tree/master/aws-yaml) knew that not every user would want to deploy into the same hard-coded AWS region, so they defined an `aws:region` setting to make it both configurable and optional, falling back to `us-west-2` by default. Users of this template are free to change this value if they like or leave it alone and accept the default.

This is all made possible by the existence of the [`template` block](/docs/reference/pulumi-yaml/#template-options) in `Pulumi.yaml`:

```yaml
# The `template` block from the aws-yaml template.
template:
  description: A minimal AWS Pulumi YAML program
  config:
    aws:region:
      description: The AWS region to deploy into
      default: us-west-2
```

Indeed, this block is all that defines `aws-yaml` as a template; without it, the `aws-yaml` project would be a regular ol' Pulumi YAML program like any other.

The `template` block defines two properties:

* An optional `description` property to give new projects created from the template
* A `config` block that lists the names, descriptions, and default values of any settings that should be configurable for new projects

The `template` block is essentially where all the new-project magic happens. Any settings you define in this block will prompt users for their values and apply those settings to the project's initial stack (for example, the `dev` stack we created in Step 1). By default, these values are captured and applied as plain-text strings, but you can also capture them [as encrypted Pulumi secrets](/docs/reference/pulumi-yaml/#config) by adding `secret: true` --- an appropriate choice for prompting for sensitive data like passwords, API keys, and the like.

Our super-simple website template doesn't need much in the way of configurability --- but let's define some anyway just to see how it's done. While we're at it, we'll make a few adjustments to make project names and descriptions configurable as well.

Make the changes below to `Pulumi.yaml` to use the project `name` and `description` supplied by the CLI, add a `template` section to let users configure a home-page title and greeting, and interpolate those values into the body of the home page itself. Here's the full content of the program for reference:

```yaml
# Configure project names and descriptions with values obtained from `pulumi new`.
name: ${PROJECT}
description: ${DESCRIPTION}
runtime: yaml

# Define the template's configuration settings.
template:
  description: A simple static website on Amazon S3
  config:
    aws:region:
      description: The AWS region to deploy into
      default: us-west-2
    title:
      description: A title to use for the home page
      default: My Awesome Website
    greeting:
      description: A greeting to show on the home page
      default: Hello, internet person! 👋

resources:

  # Create an S3 bucket and configure it as a website.
  bucket:
    type: aws:s3:Bucket
    properties:
      acl: public-read
      website:
        indexDocument: index.html

  # Create a home page for the website.
  index.html:
    type: aws:s3:BucketObject
    properties:
      bucket: ${bucket.id}
      acl: public-read
      contentType: text/html
      content: |
        <html>
          <meta name="content" charset="utf-8">
          <title>${title}</title>
          <body>
            <h1>${title}</h1>
            <p>${greeting}</p>
          </body>
        </html>

# Export the URL of the website.
outputs:
  url: http://${bucket.websiteEndpoint}
```

That's all there is to it! The template's complete and ready to be published. However, before we do that, let's first give it a try locally just to make sure it delivers the new-project experience we're looking for.

## Step 4: Test-drive the template locally {#test}

Back in your terminal (and assuming you're still in the `my-template-project` folder), create a new folder alongside `my-template-project`, then run `pulumi new` to create a new project, pointing Pulumi to the folder containing your template:

```bash
$ cd ..
$ mkdir my-test-website && cd my-test-website
$ pulumi new ../my-template-project
```

Step through the prompts, which should include each of the configurable settings we defined in the `template` block earlier, along with their default values:

```
$ pulumi new ./my-template-project

project name: (my-test-website)
project description: (A simple static website on Amazon S3)
...

aws:region: The AWS region to deploy into: (us-west-2)
greeting: A greeting to show on the home page: (Hello, internet person! 👋) Hi, world!
title: A title to use for the home page: (My Awesome Website) Hey look, it's my website!

Your new project is ready to go! ✨
To perform an initial deployment, run `pulumi up`
```

Go ahead and deploy the new project with `pulumi up`, then navigate to the newly deployed website in your favorite web browser:

```bash
$ pulumi up --yes
$ open $(pulumi stack output url)
```

Well done! You've written your first Pulumi template.

Let's finish things off by publishing your template so others can use it. As before, tidy up with `pulumi destroy` before moving on:

```bash
$ pulumi destroy --yes --remove
```

## Step 5: Publish the template {#publish}

A moment ago, when you tested your first template, you did so by pointing Pulumi to the template's path on your local filesystem. Before that, when you ran `pulumi new aws-yaml`, you instructed Pulumi (implicitly) to fetch the source of the template over HTTPS from the official [pulumi/templates repository on GitHub](https://github.com/pulumi/templates). So to make your template available to others, all you have to do publish it to a file path or Git URL that's accessible by the Pulumi CLI.

You _could_ create a new GitHub repository for this project, then pass the fully-qualified URL of the path containing `Pulumi.yaml` to `pulumi new`, like so:

```bash
$ pulumi new https://github.com/{your-org}/{your-repo}/tree/main
```

But since our project consists of just one file, you don't even need to do that much: you can just paste the contents of the file into a new [GitHub gist](https://gist.github.com/) (since a gist is [also a Git repository](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists)), name the gist `Pulumi.yaml`, and point Pulumi to the gist's URL.

Go ahead and [create a gist of your own](https://gist.github.com/), then use it to create a new project:

```bash
$ mkdir ../my-second-test-website && cd ../my-second-test-website
$ pulumi new https://gist.github.com/cnunciato/b331efae6a4740c237a0364d17fe220f
$ pulumi up
```

Be sure to tidy up as before with `pulumi destroy` when you're done.

## Bonus step: Add a Deploy with Pulumi button

In addition to the CLI, your users can also create new projects in the Pulumi Service with the [Deploy with Pulumi button](/docs/pulumi-cloud/pulumi-button/). This is a great option for making your project installable from GitHub READMEs and other team docs. Here, for example, is a Deploy button that creates a new project using my version of the gist we created above:

[![Deploy with Pulumi](/images/deploy-with-pulumi/dark.svg)](https://app.pulumi.com/new?template=https://gist.github.com/cnunciato/b331efae6a4740c237a0364d17fe220f)

Embedding these buttons yourself is easy --- just use one of the snippets below, swapping the values of `{template-url}` for the URL of your template's gist or Git repository:

```html
<a href="https://app.pulumi.com/new?template={template-url}">
    <img src="/images/deploy-with-pulumi/dark.svg" title="Deploy with Pulumi">
</a>
```

```markdown
[![Deploy with Pulumi](/images/deploy-with-pulumi/dark.svg)](https://app.pulumi.com/new?template={template-url})
```

Project creators who go down this path will be prompted in the browser for the same configuration values as they would with the CLI, and afterward, they'll be able to deploy the project either with the Pulumi CLI or with [Pulumi Deployments](https://www.pulumi.com/docs/pulumi-cloud/deployments/).

## See it in action

You can watch this [Modern Infrastructure video](https://www.youtube.com/playlist?list=PLyy8Vx2ZoWloyj3V5gXzPraiKStO2GGZw) to see another example of creating and sharing a Pulumi template:

{{< youtube "-jbZ_LZz31M?rel=0" >}}

## Wrapping up

As you can see, creating a template is both simple and powerful, and I hope this post encourages you to experiment with a few of your own. Feel free to peruse the following links for inspiration:

* [Pulumi Templates](/templates/)
* The [pulumi/templates repository](https://github.com/pulumi/templates) on GitHub
* [Pulumi project file reference](/docs/reference/pulumi-yaml)
* [`pulumi new` reference](/docs/cli/commands/pulumi_new/)
* [Deploy with Pulumi button reference](/docs/pulumi-cloud/pulumi-button/)

And as always, be sure to stop by [Pulumi Community Slack](https://slack.pulumi.com/) to let us know know how it goes.

Happy templating!
