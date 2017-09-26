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

<h2 class="title f2">Lifecycle of a Pulumi Application</h2>

When we update an application, Pulumi does not need to recreate all of the infrastructure.  Instead, Pulumi understands
the minimal set of changes it needs to make by diffing the current state with a new desired state.

For some resources, changes can be made directly in place with no interruption to your infrastructure.  For
others, a resource may need to be replaced, and Pulumi will create the new resource first, then update any other
resources dependent on this, before finally removing the no longer needed original resource.  This is handled by
Pulumi automatically and this behavior is dependent on the kind of resource being updated.

Pulumi tracks the state of the infrastructure in a __checkpoint__ file, stored inside the `.pulumi` folder.  This
checkpoint file file is needed to make updates to the infrastructure.  In future releases, Pulumi will support
additional methods for managing infrastructure state across updates, including a reliable deployment service.

<h2 class="h2" style="font-weight: bold" markdown="1">Next Up: [Programming AWS](./aws)</h2>

