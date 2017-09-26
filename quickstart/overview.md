---
layout: default 
nav_section: "quickstart"
---

<p><a href="/quickstart">Quickstart</a> &gt; <b>Overview</b></p>

<h1 class="title f1">Overview</h1>

With Pulumi, you write **programs** in your favorite language, with your favorite tools, that describe your cloud
application and its infrastructure needs.  We just call these **Cloud Applications**.  You'll quickly notice that with
Pulumi there is less of a striking distinction between infrastructure and application code.  In fact, we like to blur
this line and think of these simply as distributed programs.

Cloud Applications are built out of **package**, just like your favorite language, and some of these packages provide
cloud primitives that are responsible for creating and managing infrastructure on your behalf.  You can also build new
custom packages and share and reuse them with other Cloud Applications in your team or with the open source community.

In a Pulumi Cloud Application, you allocate objects that correspond to cloud resources and application artifacts.
For example, you will see things like `new cloud.Table("customers")`, rather than a bunch of configuration code.
Pulumi figures out what is necessary and will make any changes required for your program to run.

Cloud Applications are not ordinary programs.  Instead of running them directly, you will run them using the **`pulumi`
command-line tool** (CLI).  This tool deploys them to the cloud and updates them anytime you make a change.  The CLI
understands how to do all of this for you, so that you're not manually editing configuration or touching cloud consoles.

<h2 class="title f2">Languages</h2>

In the current release, Cloud Applications can be authored in [JavaScript](
https://developer.mozilla.org/en-US/docs/Web/JavaScript) or [TypeScript](https://www.typescriptlang.org/), run in
[Node.js](https://nodejs.org/en/), and use [NPM](https://www.npmjs.com/) for package management.  We recommend using
TypeScript to get the most development time productivity support, especially when paired with [Visual Studio Code](
https://code.visualstudio.com/), but this is by no means a requirement.

We will support additional languages in the future, and would [love to hear from you](/contact) if you have a special
request!

<h2 class="title f2">Packages</h2>

Pulumi's current Cloud SDK includes three packages to use as building blocks for your Cloud Applications.

The following three packages are included in the Pulumi Cloud SDK by default.  Before using any of them, please
remember to run `npm link <package>` or `yarn link <package>` in the consuming Cloud Application's root directory.

For example, to get ready for a Pulumi Cloud Application to use the AWS and Pulumi Cloud packages, run this:

    $ cd myapp
    $ yarn link pulumi
    $ yarn link @pulumi/pulumi-cloud
    $ pulumi preview

Except for the core runtime package, `pulumi`, packages are scoped underneath the `@pulumi` namespace.  Anytime you
see a `@pulumi/...` package, you can expect some reusable cloud goodness that only Pulumi can deliver!

<h3 class="title f3">pulumi</h3>

[Documentation](/packages/pulumi)

The `pulumi` package contains the core primitives for interacting with the Pulumi Fabric and Cloud Runtime.  Most Cloud
Applications can ignore this package altogether, although for some advanced scenarios it may be necessary.  For the most
part, this is there only to support building the other packages you will soon encounter below.

<h3 class="title f3">@pulumi/aws</h3>

[Documentation](/packages/pulumi-aws)

The `@pulumi/aws` package contains the full suite of over 250 AWS resources.  Any AWS resource that is available from
the AWS console or CloudFormation, along with its full set of properties, is available using this library.  Using this
library, you can provision and connect low level infrastructure, VMs, databases, containers, and more.

<h3 class="title f3">@pulumi/cloud</h3>

[Documentation](/packages/pulumi-cloud)

The `@pulumi/cloud` package is the recommended way to program the cloud using Pulumi.  It is a highly productive,
cloud-neutral library for building Cloud Applications rapidly and productively.  Programs built using this library are
inherently capable of running on any cloud -- or even on-premises -- and you will find that the APIs are built with
ease of use in mind.  Using this library is the easiest way to program the cloud and leverage all it has to offer.

*Note*: We expect to introduce additional cloud providers and cloud components in future releases.

<h2 class="title f2">How Pulumi Works</h2>

To see how Pulumi works, let's look at a very simple Pulumi Cloud Application:

```typescript
import * as cloud from "@pulumi/cloud";

let votes = new cloud.Table("votes");

let app = new cloud.HttpEndpoint("api");
app.get("/", async (req, res) => {
    res.json(await votes.get());
})
app.post("/{vote}", async (req, res) => {
    await votes.insert({ vote: req.vote });
    res.end();
});

app.publish();
```

This simple program does several important and powerful things:

* It imports the cloud package, `@pulumi/cloud`, which gives us a simple and lovable cloud programming model.
* It creates a `votes` table, which is a hosted NoSQL cloud database table that auto-scales to meet demand.
* It creates a new `api` cloud endpoint, which is a hosted API Gateway that is secure and handles infinite scale.
* It registers a serverless HTTP `GET` route at `/` which dumps the contents of `votes` as JSON.
* It registers a serverless HTTP `POST` route at `/{vote}` which records each vote for `{vote}` in `votes`.
* It calls `publish` to listen for incoming requests at these new endpoints.  At this point, the API is live.

Notice that there is absolutely no `XML`, `JSON`, or `YAML` configuration code that must be written.  *This is the
entire Cloud Application!*  This is the power of what Pulumi offers and a major reason why it's so easy to use.

To understand how this works, however, we must return to a point made above: Pulumi programs are not run like
ordinary programs.  You don't simply run the program on your machine.  Instead, you give the program to Pulumi, and it
analyzes it to determine how to activate the program in your target cloud environment.  It then makes it so.

A Pulumi Cloud Application is essentially an eternal program runs continuously in your cloud environment, is updated
incrementally from time to time, but logically never exits.  This is a subtle distinction, and a new and innovative
concept that is key to Pulumi's magic.  Understanding this is essentially to really leveraging Pulumi to its fullest.

To explore this further, let's just look at a single line from that program:

```typescript
let votes = new cloud.Table("votes");
```

It wouldn't make sense to recreate the `votes` NoSQL database table over and over again.  Instead, we want a single
instance of this table to get created for each unique instance of our Cloud Application -- say, dev, stage, and prod --
and, as we update our code, we don't want to perturb that table.  This is precisely what Pulumi does.  It will create
that table once, when we first create an instance, and then incrementally update the pieces around it as needed.

In fact, Pulumi understands the minimal set of changes it needs to make by diffing the current state with a new desired
state.  When we update an application, Pulumi does not need to recreate all of the infrastructure.

For some resources, changes can be made directly in place with no interruption to your Cloud Application's availability.
For others, a resource may need to be replaced, and Pulumi will create the new resource first, then update any other
resources dependent on this, before finally removing the no longer needed original resource.  Although the behavior
depends on the kind of resource being updated, Pulumi handles this automatically to minimize application downtime.

Pulumi tracks the state of the infrastructure in a *checkpoint* file, stored inside the `.pulumi` folder.  This
checkpoint file file is needed to make updates to the infrastructure.  In future releases, Pulumi will support
additional methods for managing infrastructure state across updates, including a reliable deployment service.

<h2 class="h2" style="font-weight: bold" markdown="1">Next Up</h2>

If you would like to program AWS resources directly, see [Programming AWS](./aws.html).

If you would prefer to program against Pulumi's Cloud Framework, see [Programming the Cloud](./cloud.html).

Please note that you can even mix both styles in the same application.

