---
title: "The New Generation of Pulumi Components"
date: 2025-03-26
draft: false
meta_desc: Pulumi Components enable you to create, share, and consume reusable infrastructure building blocks across your organization and the broader community.
meta_image: meta.png
authors:
    - mikhail-shilkov
    - meagan-cojocar
tags:
    - releases 
    - platform-teams
    - features
    - iac
    - components
social:
    twitter: "Introducing enhanced Pulumi Components: Create in one language, consume in any other—even YAML! Perfect for platform teams building reusable infrastructure that developers can easily adopt."
    linkedin: "We're excited to announce significant enhancements to Pulumi Components! Now platform teams can build sophisticated infrastructure abstractions in their preferred language, while developers can easily consume these components using simpler interfaces or YAML. It's a more intuitive, more secure way to codify organizational standards while giving developers straightforward access to rock-solid abstractions—without worrying about the underlying details. A true win-win that accelerates innovation and drives productivity across your organization."
---

Pulumi Components enable you to create, share, and consume reusable infrastructure building blocks across your organization and the broader community. Today, we're excited to announce significant enhancements to Pulumi Components that make them more powerful, accessible, and easier to use than ever before.

<!--more-->

With this release, we've made it possible to author components in one language and consume them in any other Pulumi language—including Pulumi YAML. This breakthrough enables platform teams to build sophisticated infrastructure abstractions in their preferred programming language while application developers can easily consume these components using simpler interfaces or even YAML, all without sacrificing type safety or functionality.

For platform teams, the new Pulumi Components offer a more intuitive, more secure way to codify organizational standards. For developers, it's a straightforward way to pull in rock-solid abstractions without having to worry about all the underlying details. It's a win-win that drastically accelerates innovation and drives productivity across your teams.

"Pulumi's reusable components have transformed our infrastructure collaboration," said Kevin Keeler, Vice President - DevOps, QA, and Architecture at A+E Networks. "Our developers interact with Pulumi YAML to provision infrastructure quickly and easily, while our platform team leverages Pulumi's programming capabilities to build robust, reusable components. This ensures compliance with organizational standards and best practices without burdening developers with complexity. By streamlining this workflow, we've enhanced productivity and focused more on delivering customer value."

## Understanding Component Resources

At their core, Component Resources in Pulumi are logical groupings of resources that encapsulate infrastructure patterns and best practices. Unlike standard resources that map directly to cloud provider resources, component resources are higher-level abstractions that can contain multiple child resources working together to implement a specific capability. While similar in concept to Terraform modules, Pulumi Components offer significantly more power through full programming language capabilities, stronger typing, inheritance patterns, and now, cross-language support.

For example, a `WebService` component might include a load balancer, compute instances, security groups, and networking configuration—all bundled together as a single, reusable unit.

## What's New with Pulumi Components

Our latest enhancements focus on making components more accessible and easier to share:

1. **Cross-language consumption**: Components authored in one language can now be consumed in any Pulumi language, including Pulumi YAML.

2. **Simplified sharing**: Share components by simply pushing code to a git repository - no need to manually publish SDKs.

3. **Streamlined consumption**: Use the `pulumi package add` command with any git URL (like `github.com/org/repo`) to easily incorporate any components into your projects.

## How It Works

### Creating Components

Creating a component remains the same as before—define a class that extends `ComponentResource`:

```ts
TODO
```

### Sharing Components

Pulumi's new Components capability is designed to make sharing infrastructure building blocks as easy as possible, whether you're publishing them to a Git repository or referencing them from a local folder in a monorepo.

#### Publishing to Git

Once you've authored your component, sharing it is as simple as pushing your code to a Git repository and optionally tagging a release. From there, anyone (including you) can pull it down and use it in their own Pulumi projects.

For example, after pushing your S3BucketComponent to GitHub and tagging it as v1.0.0, others can consume it by running:

```ts
TODO
```

Under the hood, Pulumi:

1. Fetches your code from GitHub
2. Auto-generates a local SDK from the component's schema
3. Makes it available to your Pulumi program in your chosen language

#### Referencing Components Locally

For scenarios when you're not wanting to publish components publicly, you can reference local source code directly:

```ts
TODO
```

Pulumi will identify the folder as a Pulumi component project, generate a local SDK, and make it available for import in your program—even if your consumer program is in a different language.

### Consuming Components Across Languages

The real power comes in how these components can now be consumed in any Pulumi language:

**TypeScript:**

```ts
TODO
```

**Python:**

```ts
TODO
```

**Pulumi YAML:**

```ts
TODO
```

## Pro Tips

- **Tagging Releases**: If you're working with Git-based components, you can tag stable releases. This ensures downstream users can easily choose specific versions without chasing a moving target.

- **Managing Dependencies**: Once you've run `pulumi package add <repo-url>`, Pulumi will generate a local SDK in your project. Check in these files if you want fully reproducible builds; or add them to `.gitignore` if you prefer to regenerate them on each checkout.

- **Leveraging Private Repos**: If you need to keep your components private, you can still point to a Git source in a private repository. Just make sure your CLI environment has the right credentials (for example, an SSH key or a personal access token).

## Conclusion

The ability to author components in one language and consume them in any other Pulumi language—including YAML—provides unprecedented flexibility and collaboration opportunities between platform teams and application developers.

We're excited to see what you build with Pulumi Components! Share your feedback with us on the [Pulumi Community Slack](https://slack.pulumi.com/) or open an issue in the [pulumi/pulumi GitHub repository](https://github.com/pulumi/pulumi).
