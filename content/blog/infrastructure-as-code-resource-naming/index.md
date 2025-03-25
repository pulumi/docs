---
title: Infrastructure as Code Resource Naming
canonical_url: https://www.pulumi.com/blog/autonaming-configuration/
date: 2019-09-10
updated: 2025-03-03
meta_desc: "Understand Pulumi resource naming—eliminate confusion, customize auto-naming,
  and simplify updates. Discover how to take full control."
meta_image: meta.png
authors:
  - eric-rudder
tags:
  - features
search:
  keywords:
    - naming
    - customize
    - infrastructure
    - resource
    - confusion
    - auto
    - eliminate
---

{{% notes %}}
We've introduced a new way to customize or disable auto-naming with a configuration option. See [Auto-naming Configuration](/blog/autonaming-configuration/) for more information about all the ways you can customize auto-naming.
{{% /notes %}}

"What's in a name? That which we call a rose by any other name would smell as sweet."  William Shakespeare's oft repeated quote was used to help Juliet explain that a "Montague" is worthy of love.  Juliet may have underestimated the importance of a name, however, since things didn't work out so well for everyone in Verona!  Many customers have questions about "names" in Pulumi -- and in an effort to make sure that things work out better for them than they did for Romeo, here's a quick note on naming!

<!--more-->

Usually, folks ask, "Why are resources created with funny characters at the end?"  And more often than not, their next question is, "Can I use my own names instead?"  Fear not!  There are good reasons for Pulumi's naming strategy and ultimately, you have complete control over naming.

## Logical vs. Physical Names

Cloud resources typically have both a logical and a physical name, and given this level of abstraction, these names may not always match.  More often than not, the [physical resource names](/docs/iac/concepts/resources/names/#autonaming) in Pulumi are "auto-named," and it's this auto-naming that appends a few random characters to end of the physical name.

Say that you have IAM role with a logical name of `role-friar`.  Pulumi will choose a physical name for this that looks something more like: `role-friar-3742fb`, for several good reasons.

First and foremost, Pulumi Stacks are often instanced multiple times.  Choosing a random suffix ensures that there are no naming collisions, and teams can stand up projects multiple times, for example, in a rapid create/test development cycle, or even in production, where you may want to stand up your Pulumi Stack in different regions for availability and scale.

Second, physical names are used in important ways when we update our resources.  Sometimes, updates can happen in place, however, often updates require a resource to be replaced.  Auto-naming helps ensure that Pulumi can stand up the new resource first and update any references to the new name, before deleting the old resource.  This allows for zero-downtime updates, which is something we usually want to take advantage of.  Indeed, customers often start to override auto-naming, only to realize that it's much easier to let the platform manage this for you, and then revert back to auto-naming.

## Controlled Naming

{{% notes %}}
We've introduced a new way to customize or disable auto-naming with a configuration option. See [Auto-naming Configuration](/blog/autonaming-configuration/) for more information about all the ways you can customize auto-naming.
{{% /notes %}}

There are times, however, where precise naming is important.  You might need to match an existing environment, or want to explicitly control other behavior.  If you know for certain that you want to control the naming yourself, you can indeed override auto-naming.  Simply specify the physical name on your resource during creation. Most resources expose a `name` property that may be specified in the argument object to the constructor:

```typescript
const role = aws.iam.Role("role-friar", {
    name: "friar-lawrence",
});
```

Sometimes, the "name" property isn't called name -- just to keep you on your toes.  For example, the AWS S3 Bucket requires setting the `bucket` property.  So, you may have to scan the documentation for the specific resource you are creating to help you with your construction.  There are also a few resources (like `aws.kms.Key`) that don't have physical names and instead use other auto-generated IDs to uniquely identify them.

## A Happy Ending

Eventually the Montagues and Capulets made peace.  I'm sure you too will find peace with a naming strategy that works for you, whether it's fully automatic, fully manual or a combination of both.
