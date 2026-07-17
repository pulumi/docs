---
title_tag: "Deploy with Pulumi button"
meta_desc: The "Deploy with Pulumi" button lets you easily create new Pulumi projects from the browser. Learn how to create this deployment button in this guide.
title: Deploy with Pulumi button
h1: Deploy with Pulumi button
menu:
  idp:
    name: Deploy with Pulumi button
    parent: idp-integrations
    weight: 10
    identifier: idp-integrations-pulumi-button
aliases:
- /docs/deployments/pulumi-button/
- /docs/pulumi-cloud/pulumi-button/
- /docs/reference/service/pulumi-button/
- /docs/console/extensions/pulumi-button/
- /docs/intro/console/extensions/pulumi-button/
- /docs/intro/console/pulumi-button/
- /docs/intro/pulumi-service/pulumi-button/
- /docs/intro/pulumi-cloud/pulumi-button/
---

The "Deploy with Pulumi" button lets you easily create new Pulumi projects from the browser. You can embed the button in README files within GitHub repositories or gists, blog posts, or other web pages.

For example, select the `Deploy` button to configure and create a new empty JavaScript project:

[![Deploy](/images/deploy-with-pulumi/dark.svg)](https://app.pulumi.com/new?template=https://github.com/pulumi/templates/javascript)

Rather than right-clicking the button to recover its image URL, copy the Markdown snippet below and drop it straight into a README, gist, or blog post:

```markdown
[![Deploy](https://www.pulumi.com/images/deploy-with-pulumi/dark.svg)](https://app.pulumi.com/new?template=https://github.com/pulumi/templates/javascript)
```

Swap the `template` query parameter for the URL of your own project template to point the button at your repository instead. See [Creating a Pulumi Button](#creating-a-pulumi-button) below for the full Markdown and HTML forms, plus the complete set of button image variants.

To create a _Deploy with Pulumi_ button:

 1. Include optional template metadata in your `Pulumi.yaml`.
 2. Create a button in Markdown or HTML.

## Preparing your Template

The "Deploy with Pulumi" button works with project templates hosted in public or private GitHub repositories or gists.

A template is a Pulumi project that has the required `Pulumi.yaml` file describing the project. The project template can be in the root of the GitHub repository, or within a subdirectory. Multiple projects can be hosted within subdirectories of a single repository.

A large number of templates are provided by Pulumi in [https://github.com/pulumi/examples](https://github.com/pulumi/examples) and [https://github.com/pulumi/templates](https://github.com/pulumi/templates).

To learn more about building your own custom templates, see [Custom Templates](/docs/idp/concepts/templates).

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
[![Deploy](https://www.pulumi.com/images/deploy-with-pulumi/dark.svg)](https://app.pulumi.com/new?template=https://github.com/pulumi/examples/aws-js-s3-folder)
```

Or, the equivalent HTML:

```html
<a href="https://app.pulumi.com/new?template=https://github.com/pulumi/examples/aws-js-s3-folder">
  <img src="https://www.pulumi.com/images/deploy-with-pulumi/dark.svg" alt="Deploy">
</a>
```

Use the fully qualified image URL rather than a relative path — a relative path only resolves on pulumi.com and renders as a broken image once the snippet is pasted into a README hosted elsewhere.

### Button Image

Pulumi provides both SVG and PNG versions of the button image at the following URLs in both light and dark themes:

**Dark Theme**

- `https://pulumi.com/images/deploy-with-pulumi/dark.svg`
- `https://pulumi.com/images/deploy-with-pulumi/dark.png`

**Light Theme**

- `https://pulumi.com/images/deploy-with-pulumi/light.svg`
- `https://pulumi.com/images/deploy-with-pulumi/light.png`

## Custom Git Branches

You can use a fully qualified GitHub URL with the `template` parameter to reference the template at a specific Git branch, tag, or commit:

```
https://github.com/pulumi/examples/tree/master/aws-js-s3-folder
```
