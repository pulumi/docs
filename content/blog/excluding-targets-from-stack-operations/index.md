---
title: "Excluding targets from stack operations"
date: 2025-04-30
meta_desc: "You can now exclude targets from up, preview, refresh, and destroy operations"
authors:
    - tom-harding
---

Pulumi provides a set of top level commands for managing stack deployments. We can use commands like `up` and `destroy` to spin up and tear down production environments, or `refresh` to update our understanding of the stack’s resources.

These work great, but sometimes you want to perform these operations on a subset of your infrastructure. In these cases, the `--target` flag allows you to specify the precise resources on which you want to perform your updates. On top of this, the `--target-dependents` flag can be used to select all the children of these `--target` resources automatically. This makes it easy to say, for example, “deploy this particular AWS bucket” without affecting the rest of your infrastructure.

Today, we’re going to talk about an update to address the complementary feature request. While `--target` allows us to specify a subset of our infrastructure, it can be cumbersome if we want to include almost all of our resources. For this use case, we’ve introduced two new flags: `--exclude` and `--exclude-dependents`.

## An example: blog post drafts

Let’s imagine we want to deploy our static blog website. As part of this process, we have a bunch of HTML pages we’d like to deploy:

{{% chooser language "javascript, python" %}}

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

for file_path in glob("posts/**/*.html"):
    aws.s3.BucketObject(file_path,
        source = pulumi.FileAsset(file_path),
        ....
    )

...
```
{{% /choosable %}}

This works well, but what if we have a list of draft articles that we don’t want to include in the deployment? We can optimistically assume we’ve finished more articles than we’ve started, so using `--target` to specify every article, as well as supporting resources (CSS, JavaScript, ownership controls, et cetera), would quickly become unmanageable.

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

{{% chooser language "javascript, python" %}}

{{% choosable language javascript%}}
```javascript
...

// A stub resource to group all our drafts
const draftGroup = new pulumi.ComponentResource('ComponentResource', 'drafts')

for (const file in await glob('drafts/**/*.html')) {
  new aws.s3.BucketObject(`draft-${file}`, {
    source: new pulumi.asset.FileAsset(`drafts/${file}`),
    ...
  }, { parent: draftGroup })
}

...
```
{{% /choosable %}}

{{% choosable language typescript%}}
```typescript
...

// A stub resource to group all our drafts
const draftGroup: pulumi.ComponentResource =
  new pulumi.ComponentResource('ComponentResource', 'drafts')

for (const file in await glob('drafts/**/*.html')) {
  new aws.s3.BucketObject(`draft-${file}`, {
    source: new pulumi.asset.FileAsset(`drafts/${file}`),
    ...
  }, { parent: draftGroup })
}

...
```
{{% /choosable %}}

{{% choosable language python %}}
```py
...

# A stub resource to group all our drafts
draft_group = pulumi.ComponentResource(t="ComponentResource", name="drafts")

for file_path in glob("posts/**/*.html"):
    aws.s3.BucketObject(file_path,
        source = pulumi.FileAsset(file_path),
	 opts = pulumi.ResourceOptions(parent = draft_group),
        ....
    )

...
```
{{% /choosable %}}

In this setup, we now have a parent resource for all drafts. Using `--exclude-dependents`, we can now exclude everything under this parent resource without having to enumerate all of them individually:

```shell
pulumi up --exclude <URN>::ComponentResource::drafts --exclude-dependents
```

This command will exclude all drafts from the `up` operation, regardless of how many we have or how they’re named. We now have a nice, scalable way to manage our drafts across production and development environments\!

## Next steps

With these flags now available in the command line, expect to see them introduced in the automation APIs and GitHub action soon. Thanks for reading, and feel free to share any feedback on [GitHub](https://github.com/pulumi/pulumi), [X](https://twitter.com/pulumicorp), or our [Community Slack](https://slack.pulumi.com/).

