---
title: "Improved pnpm support for Node.js projects"
date: 2026-07-17
meta_desc: Pulumi now supports pnpm 11 and reliably serializes Node.js functions in pnpm and symlinked workspaces.
authors:
    - julien-poissonnier
---

If you manage your Node.js Pulumi projects with pnpm, our latest releases make the experience a lot smoother:

* Pulumi now supports [pnpm 11](https://pnpm.io/blog/releases/11.0), including its stricter handling of post-install scripts, so `pulumi new` works out of the box with the latest pnpm ([#23815](https://github.com/pulumi/pulumi/pull/23815))
* [Serialized functions](/docs/iac/concepts/functions/function-serialization/) no longer embed pnpm's versioned store paths in `require` calls, so upgrading a dependency no longer produces spurious diffs in serialized code, or errors when a dynamic provider loads its dependencies during `pulumi refresh` or `pulumi destroy` ([#23767](https://github.com/pulumi/pulumi/pull/23767))
* Magic functions, callbacks written inline in your program and deployed as cloud functions, like an [`aws.lambda.CallbackFunction`](/docs/iac/concepts/functions/function-serialization/), now work in pnpm projects. Symlinked workspace and `file:` dependencies are fixed the same way ([#23866](https://github.com/pulumi/pulumi/pull/23866))

After you upgrade to an SDK with these fixes, expect a one-time diff on previously serialized functions as their `require` paths switch to the new version-independent form.

For more on how Pulumi serializes functions in Node.js, see the [function serialization docs](/docs/iac/concepts/functions/function-serialization/).
