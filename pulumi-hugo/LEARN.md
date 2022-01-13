# Learn Pulumi

So you're interested in writing some Learn Pulumi content? Great! Follow these
steps to make it happen.

## Setting up your development environment

If you haven't done so already, clone this repository and
[follow the instructions in the README](https://github.com/pulumi/pulumi-hugo)
to set up your `pulumi/pulumi-hugo` development environment and run the development web server.

Once you're able to run:

```zsh
$ make serve
```

... you can browse the site locally at http://localhost:1313/, and any changes you make to the pages of the site will be reloaded automatically in your browser.

## How Learn content is organized

All content lives under `./themes/default/content/learn`. Modules, which appear as cards on the Learn home page, sit at the top level of the `learn` folder, and each of the topics that comprise a given module live as siblings underneath their parent module. There are only these two levels in the hierarchy; no further nesting is supported as of today.

Both modules and topics can have their own meta images as well.

```
$ tree ./content/learn

./content/learn
├── _index.md
└── pulumi-101-aws
    ├── projects-and-stacks
    │   ├── index.md
    │   └── meta.png
    ├── configuration-and-secrets
    │   ├── index.md
    │   └── meta.png
    │   ...
    ├── meta.png
    └── _index.md
```

You can control the order in which modules appear on the Learn home page by adjusting the value of the `index` property in the module's YAML frontmatter:

```
---
title: "Pulumi 101 on AWS"
layout: module
...

# The order in which the module appears on the home page.
index: 0
...
```

Similarly, you can control the sort order of topics within a given module by adjusting their `index` properties as well:

```
---
title: "Projects and Stacks"
layout: topic
...

# The order in which the topic appears in the module.
index: 0
...
```

## Creating new modules or topics

We have a couple of helpers that make it easy to create new modules and topics. Please use them! **Please don't copy and paste content from other modules or topics to create new ones.** If (er, when) you have trouble with one of the helpers, [file an issue](issues) so we can address it and make the authoring process better for everyone.

### Creating a new module

When you know what you want to call the new module, make sure you're at the root of the `pulumi-hugo` repository, then run the new-module helper as below. (You can do this anytime; you don't have to be running the development server first.)

```
$ make new-learn-module
```

The helper will prompt you for a _slug_ -- a URL-friendly name that'll be used as the path to the module under `/learn`. Enter a name, such as `pulumi-101-aws` or `pulumi-101-azure`, and hit Enter. (You can always rename the folder of the module later, so don't worry if you don't pick the perfect thing on the first try.)

```
$ make new-learn-module
...

Module name (e.g., pulumi-101-aws): pulumi-101-azure
themes/default/content/learn/pulumi-101-azure created
```

Hugo will do its best to convert the slug to a proper title -- e.g., `pulumi-101-aws` becomes `Pulumi 101 Aws`. If you find that the conversion looks a bit weird, or if you just want to change it to something else, you can do that by editing the module file's YAML frontmatter directly.

Since a module should have at least one topic, the generator will then prompt you for a new topic as well. Give it a URL-friendly name, in the same way you did with the module, and it'll be created as a folder with that name under the module.

```
$ make new-learn-module
...

Module name (e.g., pulumi-101-aws): pulumi-101-azure
themes/default/content/learn/pulumi-101-azure created

...
Topic name (e.g., basics): basics
themes/default/content/learn/pulumi-101-azure/basics created
```

When you want to create a topic for a module that already exists, use the topic-specific helper:

```
$ make new-learn-topic
```

The new-topic helper will ask what module your new topic should belong to, so you'll need to give it the name of the folder that contains is -- for example, to create a new topic for the `pulumi-101-azure` module, enter `pulumi-101-azure`:

```
$ make new-learn-topic
...

Module name (e.g., pulumi-101-aws): pulumi-101-azure
Topic name (e.g., basics): advanced-basics
themes/default/content/learn/pulumi-101-azure/advanced-basics created
```

At this point, your new topic is created and you're ready to start writing. Each file should contain annotated frontmatter explaining how each property works, and if you find you don't have something you need, feel free to reach out in the #docs channel.

## What's a module? What's a topic?

A topic is a single focused lesson aimed at teaching someone how to do something -- ideally, something that can be completed in a relatively short period of time, like 30 minutes or less.

A module is a collection of topics that share a common theme and that are organized (usually linearly) in the interest of teaching a subject that's not easily covered in a standalone tutorial, example, or blog post.

### How do they differ from tutorials and examples?

These definitions aren't perfect, but they should hopefully help clarify the differences.

* An **example** is a single Pulumi program (possibly expressed in multiple languages) with a concise README and a maybe a [Deploy with Pulumi button](https://www.pulumi.com/docs/intro/pulumi-service/extensions/pulumi-button/). Examples are meant to serve as references; they're like snapshots of a finished product. Most of the programs in the [examples repo](https://github.com/pulumi/examples) today fall into this category.

* A **tutorial** is a guided walkthrough that often ends with a finished example. Like a blog post (and unlike an example), it's written in a familiar tone, generally in the second person ("you/your"), and it's aimed at having the reader learn by doing. Whereas an example might say, _Here's a finished thing you can look at and use_, a tutorial says, _Let's build a thing together_, from start to finish.

* A **module** is more like a chapter in a book, its topics like are sections within that chapter. Stylistically, a topic may be written like a tutorial, but it may not always end with a concrete result; instead, a topic might just tell you how to do something, or walk you through how something works. By the end of a module, though, you should have a fairly thorough understanding of whatever it is the module set out to communicate at the start.

It might help to think about the differences with some sample titles:

| Content Type    | Sample Title                                                 |
| --------------- | ------------------------------------------------------------ |
| Example         | S3 Static Website, or S3 Bucket with Cross-Region Replcation |
| Tutorial        | Building a video-processing service with Pulumi and AWS      |
| Module & topics | Strategies for testing your infrastructure code              |

Again, these may not be perfect, but should hopefully help you decide on the right form for whatever it is you're thinking about writing.

## Conventions to keep in mind

* Please keep to vanilla Markdown and [Hugo shortcodes](https://gohugo.io/content-management/shortcodes/). If you find you need more than you can express with these, let us know, and we'll do our best to get you what you need. This'll help us keep a good separation between content and layout.

* Don't try to do too much with a single module or topic. Small modules, and short, focused topics are great. People are busy -- respect their time. Also, in general, opt for provider-specific modules as opposed to higher-level ones; for example, make a module for `pulumi-101-aws` and another one for `pulumi-101-azure`, rather than just a single `pulumi-101` that tries to cover both providers.

* Keep it simple and maintainable. Multiple languages represented within a single topic is fine, of course. Multiple languages, within multiple clouds, within a single topic is going to be painful for you to write and even more painful for others to maintain.

## Questions?

Ping Christian or anyone in the #docs channel on [Pulumi Community Slack](https://slack.pulumi.com).

Thank you!
