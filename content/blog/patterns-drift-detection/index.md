---
title: "Patterns for Drift Detection with Pulumi"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2022-06-16T09:26:46-05:00

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
# Max length is 160 characters.
meta_desc: Curious about how to handle drift? Developer Advocate David shows a couple of patterns for detecting and reconciling drift with your Pulumi programs.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
    - david-flanagan

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - continuous-delivery

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
---

Let's face it, at some point someone is going to modify your carefully-crafted and automated infrastructure without updating your Pulumi program. These changes cause the desired state of our Pulumi program's to be inconsistent with the state of the world. These inconsistencies are often referred to as "drift". In this article, I want to cover a couple of patterns for detecting and reconciling this drift with your Pulumi programs.

<!--more-->

## Why is Drift Detection Important?

Reconciling drift as quickly as possible is very important in the infrastructure as code (IaC) space because the longer drift is left unattended, the harder it becomes for automation to reconcile in a manner that can be considered safe for your organization, SLAs, and customers happiness. Imagine this as if it were your car. If a single tyre needs replaced, you might be OK for a while and not notice any problems driving. If you leave that unattended and another tyre runs flat, then you've got a slightly more serious problem. As these smaller problems accumulate you're applying a multiplier of risk to your overall infrastructure, especially during reconciliation. The more resources Pulumi needs to handle during this step, the more likely for some collateral damage.

It's important that you build a system that can tolerate a nominal amount of drift but actively works to repair that as quickly as possible.

Let's see how.

## Refreshing the World

When you run a `pulumi up`, Pulumi will create a directed-acyclic graph (DAG) from your Pulumi program. This graph is then compared to your state file, and any changes that need to happen to have the DAG match the state file are applied. Pulumi does not reach out to "the world" to detect if what is in your state file is actually still up to date, at-least not without adding the `--refresh` option.

That's the secret sauce to ensuring that we can begin to detect and reconcile drift. Of course, this comes with a couple of caveats that you need to be aware of before adopting `--refresh` as your default behavior.

Firstly, it's slower. The `--refresh` option will take longer because the Pulumi program needs to reach out to all of the providers and fetch information on the resources in your state file.

Secondly, the refresh will sync potentially "untracked" fields within your resources and could trigger more updates to your resources than you've had previously. This isn't a bad thing and Pulumi's defaulting will hopefully ensure that resources aren't needlessly updated, but it's definitely worth keeping in mind.

With that being said, let's take a look at two common strategies for updating Pulumi programs.

### Workflow Approach

The most common approach is to use your CI/CD / build system to run Pulumi whenever your source code changes. This works quite well, but it means that any drift isn't detected and reconciled until someone pushes some changes. If nobody commits to the repository for 2 days, a week, or even longer - then a few problems can arise. The longer the gap, the more chance of drift causing more problems during the next run. Drift can cause resources to be recreated, which may be unexpected, and if left long enough, the "drift" might become expected behavior within your system and the next reconcile becomes a "break".

When using the workflow approach for your Pulumi program's, I highly encourage you to schedule builds as frequently as you can. Whether that's hourly or daily, the more you run your Pulumi and handle drift, the easier and more comfortable you'll be with the automation.

If you want to do this with GitHub Actions, you can use the `cron` settings on your workflow. This is an example of my own production infrastructure:

```yaml
name: infrastructure

on:
  workflow_dispatch: {}
  push:
    branches:
      - main
  schedule:
    - cron: "6 6 * * *"
```

CircleCI also makes this rather easy too:

```yaml
 daily-run-workflow:
   triggers:
     - schedule:
         cron: "6 6 * * *"
         filters:
           branches:
             only:
               - main
```

### Operator Approach

Now, scheduled executions are great, but if you want to take that to the next level - using the Pulumi Kubernetes Operator is the next step. The operator can be configured to run every few minutes, ensuring that your world is always consistent with your Pulumi program. Here's an example YAML representation of a Pulumi stack:

```yaml
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: some-repo-production
spec:
  stack: production
  projectRepo: https://github.com/some/repo
  branch: "refs/heads/main"
  destroyOnFinalize: true
  continueResyncOnCommitMatch: true
  refresh: true
  resyncFrequencySeconds: 60
```

The last three settings are the most important part of this configuration. Unfortunately, these are not the defaults - but there's an [issue tracking this change](https://github.com/pulumi/pulumi-kubernetes-operator/issues/283).

`continueResyncOnCommitMatch` is a setting that tells Pulumi to run even though the code itself hasn't changed, which when used with `refresh: true` means we'll always update the state of the world and reconcile any drift. `resyncFreqeuncySeconds` is the number of seconds between each reconcile.

## Making Refresh Your Default

Before you go updating all your workflow files, or adopting the operator, for all the benefits of continuous reconciliation and drift detection, let's cover a few safety tips.

Always run a `pulumi up --refresh` locally / manually first and inspect the changes. Pulumi may wish to replace some resources and if you don't want that to happen - you need to prepare those resources for your new continuous reconciliation.

### Protect

If you have a resource that should NEVER be deleted, make sure you protect it. You can do this by adding a `ResourceOption` to the resource in your Pulumi program.

{{< chooser language "typescript,go,python,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
{
    protect: true
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
opts=ResourceOptions(protect=True)
```

{{% /choosable %}}

{{% choosable language go %}}

```python
pulumi.Protect(true)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
new CustomResourceOptions { Protect = true }
```

{{% /choosable %}}

{{% choosable language java %}}

```java
CustomResourceOptions.builder()
        .protect(true)
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
options:
  protect: true
```

{{% /choosable %}}

{{% /chooser %}}

### Ignore Changes

If Pulumi wants to replace a resource that you don't believe needs to be updated, you can ask Pulumi to `ignoreChanges` on certain properties. Of course, it might be best to have your code match those properties, but in the event that you can't - you can use the code below to ignore:

{{< chooser language "typescript,go,python,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
{
    ignoreChanges: ["prop"]
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
opts=ResourceOptions(ignore_changes=["prop"])
```

{{% /choosable %}}

{{% choosable language go %}}

```python
pulumi.IgnoreChanges([]string{"prop"})
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
new CustomResourceOptions { IgnoreChanges = { "prop" } }
```

{{% /choosable %}}

{{% choosable language java %}}

```java
CustomResourceOptions.builder()
        .ignoreChanges("prop")
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
options:
    ignoreChanges:
    - prop
```

{{% /choosable %}}

{{% /chooser %}}

### Delete Before Replace

If you have any resources that don't use auto-naming, you'll also need to ensure they have the `deleteBeforeReplace` option enabled.

{{< chooser language "typescript,go,python,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
{
    deleteBeforeReplace: true
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
opts=ResourceOptions(delete_before_replace=["prop"])
```

{{% /choosable %}}

{{% choosable language go %}}

```python
pulumi.DeleteBeforeReplace(true)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
new CustomResourceOptions { DeleteBeforeReplace = true }
```

{{% /choosable %}}

{{% choosable language java %}}

```java
CustomResourceOptions.builder()
        .deleteBeforeReplace(true)
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
options:
    deleteBeforeReplace: true
```

{{% /choosable %}}

{{% /chooser %}}

Once you've run a couple of `pulumi up --refresh` and you're comfortable with the proposed executions, you can adopt the automation and sleep easier, knowing that you're handling drift and keeping your infrastructure up to date.

## Want to See More?

Watch me demo some of these features live, on YouTube, on my PulumiTV series: Modern Infrastructure.

{{< youtube "7nJBFEtqTl8?rel=0" >}}
