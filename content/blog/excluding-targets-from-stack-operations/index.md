---
title: "New in Pulumi IaC: Support for skipping a resource"
date: 2025-05-14
meta_desc: "Pulumi now supports excluding specific resources from stack operations, giving you more control and efficiency in managing your infrastructure"
meta_image: meta.png
authors:
    - tom-harding
tags:
    - features
    - iac
    - releases
---

Managing large-scale infrastructure can be challenging, especially when you need to perform operations on specific subsets of your resources. Pulumi's stack operations like `pulumi up` and `pulumi destroy` are powerful for deploying and tearing down environments, but sometimes you need more fine-grained control over which resources are affected.

Today, we're excited to announce a [highly requested feature](https://github.com/pulumi/pulumi/issues/9346) that will save you time and reduce complexity in your workflows: the ability to exclude specific resources from stack operations using the new `--exclude` and `--exclude-dependents` flags.

These new flags complement the existing `--target` functionality, giving you powerful options whether you want to focus on a small subset of resources or exclude just a few from larger operations. No more workarounds or custom scripts to achieve selective deployments!

<!--more-->

## The challenge: partial operations on large stacks

When managing infrastructure at scale, you often want to operate on most—but not all—resources in your stack. For example:

- Deploying all resources except a database that requires a maintenance window
- Refreshing most resources while skipping those with known differences
- Updating production infrastructure while leaving critical services untouched
- Testing changes to most components while preserving test data in development

Pulumi already has the `--target` flag to specify which resources to include in an operation. This works well when you want to target a small number of resources, but becomes unwieldy when you want to operate on most of your stack while excluding only a few resources.

## The solution: introducing `--exclude` and `--exclude-dependents`

Our new `--exclude` flag solves this problem by letting you specify which resources to omit from stack operations. When paired with `--exclude-dependents`, you can also exclude all child resources of the specified resources, making it easy to exclude entire branches of your resource tree.

These flags are now available for all major stack operations:

```shell
pulumi up --exclude <URN>::resource-to-skip
pulumi preview --exclude <URN>::resource-to-skip
pulumi refresh --exclude <URN>::resource-to-skip
pulumi destroy --exclude <URN>::resource-to-skip
```

Each of these commands can also use the `--exclude-dependents` flag to exclude child resources.

## An example: selective deployment of blog content

Let's imagine you're managing a static blog website with Pulumi. As part of your deployment, you have multiple HTML pages you'd like to deploy:

{{% chooser language "javascript,typescript,python,go,csharp" %}}

{{% choosable language javascript%}}

```javascript
...

for (const file in await glob('posts/**/*.html')) {
  new aws.s3.BucketObject(`post-${file}`, {
    source: new pulumi.asset.FileAsset(file),
    ...
  })
}

...
```

{{% /choosable %}}

{{% choosable language typescript%}}

```typescript
...

for (const file in await glob('posts/**/*.html')) {
  new aws.s3.BucketObject(`post-${file}`, {
    source: new pulumi.asset.FileAsset(file),
    ...
  })
}

...
```

{{% /choosable %}}

{{% choosable language python %}}

```python
...

for file in glob("posts/**/*.html"):
    aws.s3.BucketObject(file,
        source = pulumi.FileAsset(file),
        ....
    )

...
```

{{% /choosable %}}

{{% choosable language go %}}

```go
...

files, err := filepath.Glob("posts/**/*.html")
if err != nil { return err }

for _, file := range files {
  _, err := s3.NewBucketObject(ctx, file, &s3.BucketObjectArgs{
    Source: pulumi.FileAsset(file),
    ...
  })

  if err != nil { return err }
}

...
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
...

var files = Directory.GetFiles("posts", "*.html");

foreach (var file in files)
{
    var bucketObject = new BucketObjectv2(file, new BucketObjectv2Args
    {
        Source = new FileAsset(file),
        ...
    });
}

...
```

{{% /choosable %}}

{{% /chooser %}}

This works well, but what if we have a list of draft articles that we don't want to include in the deployment? We can optimistically assume we've finished more articles than we've started, so using `--target` to specify every article, as well as supporting resources (CSS, JavaScript, ownership controls, et cetera), would quickly become unmanageable.

```shell
pulumi up --target <URN>::style.css --target <URN>::post-hello.html ...
```

With the `--exclude` flag, this becomes much more manageable:

```shell
pulumi up --exclude <URN>::post-draft-1.html --exclude <URN>::post-draft-2.html ...
```

With this command, everything *not* specified using an `--exclude` tag will be included in the `up` operation, and thus we can avoid the hassle of naming every resource that *isn’t* a draft.

## Next step: a draft group

This is fine for a personal blog site, but can still become unmanageable when we’re dealing with multiple authors, each with multiple drafts. In this case, we might want to group our drafts under a common parent:

{{% chooser language "javascript,typescript,python,go,csharp" %}}

{{% choosable language javascript%}}

```javascript
...

// A parent component for all drafts
const drafts = new pulumi.ComponentResource('ComponentResource', 'drafts')

for (const file in await glob('drafts/**/*.html')) {
  new aws.s3.BucketObject(`draft-${file}`, {
    source: new pulumi.asset.FileAsset(`drafts/${file}`),
    ...
  }, { parent: drafts })
}

...
```

{{% /choosable %}}

{{% choosable language typescript%}}

```typescript
...

// A parent component for all drafts
const drafts: pulumi.ComponentResource =
  new pulumi.ComponentResource('ComponentResource', 'drafts')

for (const file in await glob('drafts/**/*.html')) {
  new aws.s3.BucketObject(`draft-${file}`, {
    source: new pulumi.asset.FileAsset(`drafts/${file}`),
    ...
  }, { parent: drafts })
}

...
```

{{% /choosable %}}

{{% choosable language python %}}

```python
...

# A parent component for all drafts
drafts = pulumi.ComponentResource(t="ComponentResource", name="drafts")

for file_path in glob("posts/**/*.html"):
    aws.s3.BucketObject(file_path,
        source = pulumi.FileAsset(file_path),
        opts = pulumi.ResourceOptions(parent = drafts),
        ....
    )

...
```

{{% /choosable %}}

{{% choosable language go %}}

```go

drafts := &DraftGroupComponent{}
err = ctx.RegisterComponentResource("ComponentResource", "drafts", drafts)
if err != nil { return err }

...

files, err := filepath.Glob("posts/*.html")
if err != nil { return err }

for _, file := range files {
  _, err := s3.NewBucketObject(ctx, file, &s3.BucketObjectArgs{
    Key: pulumi.String(file),
    ...
}, pulumi.Parent(drafts))

  if err != nil { return err }
}

...
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp

public class MyComponentResource : ComponentResource { ... }

...

var files = Directory.GetFiles("posts", "*.html");
var drafts = new MyComponentResource("drafts");

foreach (var file in files)
{
    var bucketObject = new BucketObjectv2(file, new BucketObjectv2Args
    {
        Source = new FileAsset(file),
        ...
    }, new CustomResourceOptions
    {
        Parent = drafts
    });
}

...
```

{{% /choosable %}}

{{% /chooser %}}

In this setup, we now have a parent resource for all drafts. Using `--exclude-dependents`, we can now exclude everything under this parent resource without having to enumerate all of them individually:

```shell
pulumi up --exclude <URN>::ComponentResource::drafts --exclude-dependents
```

This command will exclude all drafts from the `up` operation, regardless of how many we have or how they’re named. We now have a nice, scalable way to manage our drafts across production and development environments!

## Next steps

With these flags now available in Pulumi CLI v3.158.0., expect to see them introduced in the automation APIs and GitHub action soon. Thanks for reading, and feel free to share any feedback on [GitHub](https://github.com/pulumi/pulumi), [X](https://twitter.com/pulumicorp), or our [Community Slack](https://slack.pulumi.com/).
