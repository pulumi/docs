---
title_tag: "Deploy with Pulumi Button"
meta_desc: The “Deploy with Pulumi” button lets you easily create new Pulumi projects from the browser. Learn how to create this deployment button in this guide.
title: Deploy with Pulumi Button
h1: Deploy with Pulumi Button
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumicloud:
    weight: 10
aliases:
- /docs/reference/service/pulumi-button/
- /docs/console/extensions/pulumi-button/
- /docs/intro/console/extensions/pulumi-button/
- /docs/intro/console/pulumi-button/
- /docs/intro/pulumi-service/pulumi-button/
- /docs/intro/pulumi-cloud/pulumi-button/
---

The "Deploy with Pulumi" button lets you easily create new Pulumi projects from the browser. You can embed the button in README files within GitHub repositories or gists, blog posts, or other web pages.

For example, select the `Deploy` button to configure and create a new empty JavaScript project:

[![Deploy](https://get.pulumi.com/new/button.svg)](https://app.pulumi.com/new?template=https://github.com/pulumi/templates/javascript)

To create a _Deploy with Pulumi_ button:

 1. Include optional template metadata in your `Pulumi.yaml`.
 2. Create a button in Markdown or HTML.

## Preparing your Template

The "Deploy with Pulumi" button works with project templates hosted in public or private GitHub repositories or gists.

A template is a Pulumi project that has the required `Pulumi.yaml` file describing the project. The project template can be in the root of the GitHub repository, or within a subdirectory. Multiple projects can be hosted within subdirectories of a single repository.

A large number of templates are provided by Pulumi in [https://github.com/pulumi/examples](https://github.com/pulumi/examples) and [https://github.com/pulumi/templates](https://github.com/pulumi/templates).

To learn more about building your own custom templates, see [Custom Templates](/docs/pulumi-cloud/developer-portals/templates).

### Testing

You can test your template via the [Pulumi CLI](/docs/install/) or a web browser.

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
