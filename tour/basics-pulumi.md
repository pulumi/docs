---
title: Pulumi
---

Every Pulumi program is run and managed by [the `pulumi` command line interface (CLI)](/reference/cli).

Ensure it is installed before proceeding:

```bash
$ pulumi version
v0.12.1
```

If you haven't installed `pulumi` yet, you can do so simply:

```bash
$ curl -fsSL https://get.pulumi.com | sh
```

Most interesting commands will ask you to login to [the Pulumi.com service](https://pulumi.com/dashboard) when you run
them.  The CLI works in tandem with Pulumi.com to deliver a reliable and dependable experience.  It is also how you'll
use Pulumi in team environments safely.

You can log in explicitly using the [`pulumi login`](/reference/cli/pulumi_login.html) command, just as you may log out
using [`pulumi logout`](/reference/cli/pulumi_logout.html) when you are done.

As soon as you've got the `pulumi` CLI ready to go, we can create a <a href="basics-project.html">project</a>.

<div class="tour-nav">
    <a class="tour-button enabled" href="index.html" title="A Tour of Pulumi">◀</a>
    <span class="tour-index"><strong>2</strong>/8</span>
    <a class="tour-button enabled" href="basics-projects.html" title="Projects">▶</a>
</div>
