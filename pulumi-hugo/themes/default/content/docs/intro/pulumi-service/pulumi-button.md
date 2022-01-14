---
title: "Deploy with Pulumi Button"
meta_desc: An overview of how to use the "Deploy with Pulumi" button to easily
           create new projects directly from the browser.
menu:
  intro:
    parent: pulumi-service
    weight: 10
aliases:
 - /docs/reference/service/pulumi-button/
 - /docs/console/extensions/pulumi-button/
 - /docs/intro/console/extensions/pulumi-button/
 - /docs/intro/console/pulumi-button/
---

The "Deploy with Pulumi" button lets you easily create new Pulumi projects from the browser. You can embed the button in README files within GitHub repositories or gists, blog posts, or other web pages.

For example, select the `Deploy` button to configure and create a new empty JavaScript project:

[![Deploy](https://get.pulumi.com/new/button.svg)](https://app.pulumi.com/new?template=https://github.com/pulumi/templates/javascript)

To create a _Deploy with Pulumi_ button:

 1. Include optional template metadata in your `Pulumi.yaml`.
 2. Create a button in Markdown or HTML.

## Preparing your Template

The Pulumi button works with project templates hosted in public GitHub repositories or gists. A template is a Pulumi project that has the required `Pulumi.yaml` file describing the project. The project template can be in the root of the GitHub repository, or within a subdirectory. Multiple projects can be hosted within subdirectories of a single repository.

The `Pulumi.yaml` file can optionally contain a `template` section, which typically includes a `config` section for specifying required config values for the project. Each config value can have a `description` and a `default` value. Config values can also have a `secret` property, which can be set to `true` to indicate that it is a
[secret]({{< relref "/docs/intro/concepts/config#secrets" >}}).

```yaml
name: my-aws-project
runtime: nodejs
description: My AWS project description
template:
  config:
    aws:region:
      description: The AWS region to deploy into
      default: us-west-2
    myAccessToken:
      description: My access token
      secret: true
```

The above snippet includes an `aws:region` config value with a default value of `us-west-2`, as well as a `myAccessToken` config value that is a secret without a default value.

### Testing

You can test your template via the [Pulumi CLI]({{< relref "/docs/get-started/install" >}}) or a web browser.

#### CLI

```bash
$ pulumi new https://github.com/pulumi/examples/aws-js-s3-folder
```

#### Browser

```
https://app.pulumi.com/new?template=https://github.com/pulumi/examples/aws-js-s3-folder
```

![New Project](/images/docs/reference/service/new-project.png)

## Creating a Pulumi Button

After you've verified your project template works as expected, you can add a button to the README in your repository or gist. You will need to specify a `template` parameter that points to the project.

Here's an example in Markdown:

```markdown
[![Deploy](https://get.pulumi.com/new/button.svg)](https://app.pulumi.com/new?template=https://github.com/pulumi/examples/aws-js-s3-folder)
```

Or, the equivalent HTML:

```html
<a href="https://app.pulumi.com/new?template=https://github.com/pulumi/examples/aws-js-s3-folder">
  <img src="https://get.pulumi.com/new/button.svg" alt="Deploy">
</a>
```

### Button Image

Pulumi provides both SVG and PNG versions of the button image at the following URLs:

- `https://get.pulumi.com/new/button.svg`
- `https://get.pulumi.com/new/button.png`

## Custom Git Branches

You can use a fully qualified GitHub URL with the `template` parameter to reference the template at a specific Git branch, tag, or commit:

```
https://github.com/pulumi/examples/tree/master/aws-js-s3-folder
```
