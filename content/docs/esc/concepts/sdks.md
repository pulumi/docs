---
title: SDKs
title_tag: Pulumi ESC SDKs
h1: Pulumi ESC SDKs
meta_desc: Learn what the Pulumi ESC SDKs are for, when to use them at runtime, and when to use config in a Pulumi IaC program instead.
menu:
  esc:
    parent: esc-concepts
    identifier: esc-concepts-sdks
    weight: 13
---

The Pulumi ESC SDKs are language libraries that let you work with [environments](/docs/esc/concepts/) from your own code. They provide a programmatic interface to create, read, update, and delete environment definitions, and to open environments so you can read their evaluated configuration and resolved secrets.

{{< esc-sdk-config-note >}}

## When to use the SDK

The SDK is designed for two primary use cases:

- **Retrieving environment values from workloads at runtime.** An application or service opens an environment with the SDK and reads its resolved configuration and secrets while the workload runs. Because environments are evaluated when they are opened, dynamic values—such as short-lived cloud credentials—are generated fresh each time, rather than being baked into the workload.
- **Managing environments programmatically.** Automation and tooling can use the SDK to create, update, tag, decrypt, and delete environment definitions, list environments and revisions, and check definitions for errors—the same operations you can perform with the `esc` CLI or the Pulumi Cloud console.

## When not to use the SDK

Do not use the ESC SDK to consume environments from inside a Pulumi IaC program. In an IaC program, list the environment in the `environment` block of your `Pulumi.<stack>.yaml` stack configuration so its values flow into the stack as configuration and secrets. See [Use ESC with Pulumi IaC](/docs/esc/guides/integrate-with-pulumi-iac/) for details.

## Supported languages

The ESC SDK is available for the following languages. See each page for installation instructions and examples.

- [TypeScript](/docs/esc/languages-sdks/javascript/)
- [Python](/docs/esc/languages-sdks/python/)
- [Go](/docs/esc/languages-sdks/go/)
- [.NET](/docs/esc/languages-sdks/dotnet/)

## Related integrations

- [Automation API](/docs/esc/integrations/automation-api/) drives ESC from orchestration code.
- [Pulumi Service Provider](/docs/esc/integrations/pulumi-service-provider/) manages ESC resources from inside a Pulumi program.
