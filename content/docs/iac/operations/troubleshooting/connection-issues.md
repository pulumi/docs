---
title_tag: "Resolving Pulumi Cloud Connection Issues"
meta_desc: "Learn how to resolve connection issues when using Pulumi Cloud, including network proxy problems."
title: Connection issues
h1: Connection issues
aliases:
  - /docs/support/troubleshooting/common-issues/connection-issues/
  - /docs/iac/troubleshooting/common-issues/connection-issues/
menu:
    iac:
        name: Connection Issues
        parent: iac-operations-troubleshooting
        weight: 40
---

## Cannot connect to Pulumi Cloud

If your network blocks external traffic and you're using Pulumi Cloud to manage your state, your security team may need the following details to allow the Pulumi CLI to connect to Pulumi Cloud:

- The URL that the Pulumi CLI uses to connect to Pulumi Cloud is `https://api.pulumi.com`. (It does not use `https://app.pulumi.com`, so if you want to view the console from a web browser, you will need to enable that as well.)
- All access goes over HTTPS via port 443.

## Nothing happens due to a network proxy

You run Pulumi and nothing happens, with output resembling this:

```
$ pulumi up
Previewing update (<stack name>):

Resources:

$
```

If you have a system-wide proxy server running on your machine, it may be misconfigured. The [Pulumi architecture](/docs/iac/guides/basics/how-pulumi-works/) has three different components, running as separate processes that talk to each other using a bidirectional gRPC protocol on IP address `127.0.0.1`. Your proxy server should be configured **NOT** to proxy these local network connections. Add both `127.0.0.1` and `localhost` to the exclusion list of your proxy server.

## Cannot access a DIY backend

If you're using a [DIY backend](/docs/iac/concepts/state-and-backends/#using-a-diy-backend) and see an error like `read ".pulumi\\meta.yaml": blob (key ".pulumi/meta.yaml") ... AccessDenied` when running `pulumi login` or other commands, the CLI reached your storage provider but couldn't authenticate or wasn't configured correctly. See [Error reading `.pulumi/meta.yaml`](/docs/iac/guides/basics/using-a-diy-backend/#error-reading-pulumimetayaml) for common causes and fixes.
