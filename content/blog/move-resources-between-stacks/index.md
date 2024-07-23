---
title: "Move Resources Between Stacks Or Projects"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2024-07-11T15:47:21+02:00

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Introducing the new pulumi state move command that allows moving resources between stacks and projects

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - thomas-gummerer

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - announcement
    - CLI


# The social copy used to promote this post on Twitter and Linkedin. These
# properties do not actually create the post and have no effect on the
# generated blog page. They are here strictly for reference.

# Here are some examples of posts we have made in the past for inspiration:
# https://www.linkedin.com/feed/update/urn:li:activity:7171191945841561601
# https://www.linkedin.com/feed/update/urn:li:activity:7169021002394296320
# https://www.linkedin.com/feed/update/urn:li:activity:7155606616455737345
# https://twitter.com/PulumiCorp/status/1763265391042654623
# https://twitter.com/PulumiCorp/status/1762900472489185492
# https://twitter.com/PulumiCorp/status/1755637618631405655

social:
    twitter:
    linkedin:

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

Today we're announcing the [`pulumi state move`](/docs/cli/commands/pulumi_state_move/) command, which can be used to move resources that are managed by Pulumi between different stacks and/or projects.  No matter in which stack/project the resource was created in, it can now be moved with a single commmand.

<!--more-->

When refactoring a Pulumi project from a [monolithic](https://www.pulumi.com/docs/using-pulumi/organizing-projects-stacks/#monolithic) structure to [micro stacks](https://www.pulumi.com/docs/using-pulumi/organizing-projects-stacks/#micro-stacks), you might need to move resources between different projects or stacks, without recreating them. While this has been possible with some major surgery (our users came up with [automated solutions](https://github.com/pulumi/pulumi/issues/3389#issuecomment-679020482)), it's fairly error prone and difficult.  This makes refactoring Pulumi programs quite cumbersome, and having a simpler, integrated solution for this problem was a [much requested feature](https://github.com/pulumi/pulumi/issues/3389).

The `pulumi state move` command works as follows:

```
$ pulumi state move --help
Move resources from one stack to another

This command can be used to move resources from one stack to another. This can be useful when
splitting a stack into multiple stacks or when merging multiple stacks into one.

Usage:
  pulumi state move [flags] <urn>...

Flags:
      --dest string       The name of the stack to move resources to
  -h, --help              help for move
      --include-parents   Include all the parents of the moved resources as well
      --source string     The name of the stack to move resources from
  -y, --yes               Automatically approve and perform the move
```

Both `dest` and `source` can be either stacks in the current project, or stacks in a different project, using the fully qualified stack names.  Note that this works only for stacks within the same backend, it is currently not possible to move a resource between different backends.

The resources being moved have to be specified by their full [URN](/docs/concepts/resources/names/#urns), and multiple URNs can be passed at once.  For each resource being moved, all the children of that resource will also be moved, and the relationships between all resources being moved is preserved.  Resources with other types of dependencies will however not be moved to the target stack by default.  The easiest way to get the full URN of the resources is to use `pulumi stack --show-urns`.  Note that URNs can contain characters that get interpreted by the shell, so it is always a good idea to wrap them in single quotes when passing them as arguments.

The command will make no attempt to adjust the users program.  Inputs and outputs from broken dependencies will have to be adjusted in the program where the resource is being managed after being moved.  This can be done either by using [stack references](https://www.pulumi.com/docs/concepts/stack/#stackreferences), or recreating the inputs in the program.

The `pulumi state move` command is available in Pulumi v3.126.0 and later.

# Example

To demonstrate how the command works in practice, let's go through an example.  Let's assume we have the following program:

```typescript
const randomPet = new random.RandomPet("a-random-pet");

const b = new aws.s3.Bucket("b");

const index = new aws.s3.BucketObject("index.html", {
    bucket: b.bucket,
    content: "Thanks for using Pulumi!",
}, {
    parent: b,
});

const randomSite = new aws.s3.BucketObject("random.html", {
    bucket: b.bucket,
    content: randomPet.id,
}, {
    parent: b,
});
```

We create a bucket, and two bucket objects, both of them having the bucket as their parent.  One of the objects has a random pet name as its content.  At some point we decide we'd rather group all the AWS resources in a separate program, because this one grew too large.  We can do that using the `pulumi state move` command, and then adjusting the code.

First we can find out which stacks already exist and we can move the resources to:

```shell
$ pulumi stack ls --all
NAME                                            LAST UPDATE     RESOURCE COUNT  URL
v-thomas-pulumi-corp/pulumi-demo-move-aws/dev   23 minutes ago  0               <url>
v-thomas-pulumi-corp/pulumi-demo-move/dev       6 minutes ago   7               <url>
```

Next we can find the URN of the resources using `pulumi stack --show-urns`:

```shell
$ pulumi stack --show-urns
Current stack is dev:
    Owner: v-thomas-pulumi-corp
    Last updated: 13 seconds ago (2024-07-23 13:52:17.58884965 +0200 CEST)
    Pulumi version used: 3.125.1-dev.0
Current stack resources (7):
    TYPE                                    NAME
    pulumi:pulumi:Stack                     pulumi-demo-move-dev
    │  URN: urn:pulumi:dev::pulumi-demo-move::pulumi:pulumi:Stack::pulumi-demo-move-dev
    ├─ random:index/randomPet:RandomPet     a-random-pet
    │     URN: urn:pulumi:dev::pulumi-demo-move::random:index/randomPet:RandomPet::a-random-pet
    ├─ aws:s3/bucket:Bucket                 b
    │  │  URN: urn:pulumi:dev::pulumi-demo-move::aws:s3/bucket:Bucket::b
    │  ├─ aws:s3/bucketObject:BucketObject  random.html
    │  │     URN: urn:pulumi:dev::pulumi-demo-move::aws:s3/bucket:Bucket$aws:s3/bucketObject:BucketObject::random.html
    │  └─ aws:s3/bucketObject:BucketObject  index.html
    │        URN: urn:pulumi:dev::pulumi-demo-move::aws:s3/bucket:Bucket$aws:s3/bucketObject:BucketObject::index.html
    ├─ pulumi:providers:random              default_4_16_3
    │     URN: urn:pulumi:dev::pulumi-demo-move::pulumi:providers:random::default_4_16_3
    └─ pulumi:providers:aws                 default_6_45_0
          URN: urn:pulumi:dev::pulumi-demo-move::pulumi:providers:aws::default_6_45_0
```

Next we can actually move the resources.  Since we're moving the resources from the currently selected stack, we can omit the `--source` argument:

```shell
$ pulumi state move --dest v-thomas-pulumi-corp/pulumi-demo-move-aws/dev 'urn:pulumi:dev::pulumi-demo-move::aws:s3/bucket:Bucket::b'
Planning to move the following resources from dev to dev:

  - urn:pulumi:dev::pulumi-demo-move::aws:s3/bucket:Bucket::b
  - urn:pulumi:dev::pulumi-demo-move::aws:s3/bucket:Bucket$aws:s3/bucketObject:BucketObject::index.html
  - urn:pulumi:dev::pulumi-demo-move::aws:s3/bucket:Bucket$aws:s3/bucketObject:BucketObject::random.html

The following resources being moved to dev have dependencies on resources in dev:
  urn:pulumi:dev::pulumi-demo-move::random:index/randomPet:RandomPet::a-random-pet has a dependency on urn:pulumi:dev::pulumi-demo-move::random:index/randomPet:RandomPet::a-random-pet
  urn:pulumi:dev::pulumi-demo-move::random:index/randomPet:RandomPet::a-random-pet (content) has a property dependency on urn:pulumi:dev::pulumi-demo-move::random:index/randomPet:RandomPet::a-random-pet

If you go ahead with moving these dependencies, it will be necessary to create the appropriate inputs and outputs in the program for the stack the resources are moved to.

Do you want to perform this move? yes
Successfully moved resources from dev to dev
```

There's a few things worth explaining above:
- We're moving the resources to a different project, so we need to use the fully qualified stack name.  If the resources are being moved between different stacks in the same project, the argument can be only the stack name.
- Before actually moving the resources, the command gives a list of resources that is being moved.  Since the bucket objects are children of the bucket, they will be included in the move.  However the random pet is not a child resource, so it will not be moved.
- The command also warns us about dependencies that will not be transferred to the destination stack.  Since we didn't want to include the pet, but the bucket has a dependency on it, pulumi will warn us about that.
- Before going ahead with the move, we get prompted to confirm whether we want to go ahead with it.  In this example we do want to go ahead with the move, so we confirm the move, and the resources will be moved for us.

Now that the resources are moved, we need to adjust the program to take advantage of that.  The source program will now look as follows:

```typescript
const randomPet = new random.RandomPet("a-random-pet");
export const randomPetName = randomPet.id;
```

Only the random pet remains here.  We also export its name, so we can continue using it in the destination program.  Meanwhile the destination program is mostly just a copy of the original AWS resources, but there is an important change:

```
const stackRef = new pulumi.StackReference(`v-thomas-pulumi-com/pulumi-demo-move/dev`)

const b = new aws.s3.Bucket("b");

const index = new aws.s3.BucketObject("index.html", {
    bucket: b.bucket,
    content: "Thanks for using Pulumi!",
}, {
    parent: b,
});

const randomSite = new aws.s3.BucketObject("random.html", {
    bucket: b.bucket,
    content: stackRef.getOutput("randomPetName"),
}, {
    parent: b,
});
```

Note how we now need to specify the content of `random.html`, since we no longer have the random pet in the same program.  In this case we use a [stack reference](https://www.pulumi.com/learn/building-with-pulumi/stack-references/) to reference the output from the source program.  It is of course up to the user how to re-create the output.  It could also come from config, or be hardcoded depending on the use-case.

As always, we would love to hear your feedback in the [community slack](https://www.pulumi.com/community/).  If you encounter any issues with the command, please open an [issue](https://github.com/pulumi/pulumi/issues).
