---
title: New in Pulumi IaC: Dependent resource replacements
meta_desc: "You can now use the `replaceWith` property on resources to inform Pulumi of extra dependencies"
authors:
    - tom-harding
tags:
    - features
    - iac
    - releases
---

The magic of Pulumi is that we rarely have to worry about the fine details of *how* our deployment and infrastructure management works, allowing us to focus instead on *what* we want. If our program declares an S3 bucket as part of our infrastructure, Pulumi knows what to do: we don’t have to issue a specific command to create it, and nor do we have to issue a different command to alter some property of it or remove it.

Most of the time, this is exactly what we want. However, sometimes our use cases can be trickier, or more bespoke to our infrastructure. Today, we’d like to announce a new feature to allow finer-grained control over these dependencies between resources: the new `replaceWith` resource option.

## Custom resource dependencies

When we want to replace a particular resource, the Pulumi engine will walk the dependency graph to figure out what else needs to be replaced. However, the answer is not always obvious:

* Some dependencies are not obvious at the infrastructure level. Restarting a database server might mean we also want to restart its consumers so that they can reconnect.

* There are provider-specific challenges. Perhaps we can’t update the properties of a subnet if resources are using it, but there is not necessarily an observable dependency between the subnet and its users. In this case, any change to the subnet that isn’t accompanied by changes to all of its consumers would result in an error: we can’t replace a subnet while it is in use.

* There may be entirely domain-level dependencies that are part of the definition of the application on top of the infrastructure, rather than the infrastructure itself. If I have two services that maintain open connections between one another in the application layer, the replacement of one should also necessitate the replacement of another.

## Declaring our own dependencies

With the new `replaceWith` resource option, we can make these dependencies explicit in user code. Much like `deletedWith`, passing reference to other resources via `replaceWith` defines a relationship: every time one of the target resources is replaced during an operation, the source should also be replaced. There are some less obvious consequences to this:

* We can define a number of resources that all `replaceWith` each other, and so any change to any member of the group will trigger an update to all the others.

* These relationships are transitive: if we organise our resources hierarchically and children all `replaceWith` their parents, any change to an ancestor will trigger a replacement of all descendants.

## In code

As a final example, let’s take a look at one of our earlier use cases using the TypeScript SDK to illustrate the point:

```ts
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const database = new aws.rds.Instance("app-db", { /* ... */ });

// The database location is provided to this instance
// by other means, so there is not an explicit dependency
// linking the two.
const app = new aws.ec2.Instance("app-service", { /* ... */ }, {
    // Here, we explicitly tie the two together: if the
    // database is upgraded, for example, we will need to
    // restart the application instance to ensure that
    // a connection is re-established.
    replaceWith: [database],
});
```

Of course, this is a simple example, but hopefully it illustrates the point: we now have a way to make implicit dependencies between resources more explicit within our programs, and provide hints to Pulumi as to which services depend on others.

## Next steps

This feature is supported as of `v3.207.0` of the Pulumi Engine, and is now available within the Go, Python, and NodeJS SDKs. Thanks for reading, and feel free to reach out with any questions via [GitHub](https://github.com/pulumi/pulumi), [X](https://x.com/pulumicorp), or our [Community Slack](https://slack.pulumi.com/).

