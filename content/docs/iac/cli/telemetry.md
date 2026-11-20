---
title: Pulumi CLI telemetry
h1: Pulumi CLI telemetry
meta_desc: "Learn how the pulumi CLI collects and uses telemetry"
menu:
  iac:
    parent: iac-cli
    identifier: iac-cli-telemetry
    weight: 75
---

Since pulumi v3.376.0, pulumi started collecting anonymous telemetry in the CLI.  This telemetry is used to improve the product and to be able to better understand usage patterns from our users, and spot potential problems ahead of time. Each installation of pulumi is identified with a random UUID, and so is each operation. None of data is identifiable by design.

Telemetry is optional and can be turned off at any time, either using `pulumi telemetry disable` or by setting the `PULUMI_TELEMETRY=0` or `DO_NOT_TRACK=1` environment variables.

## What we collect and why

### The data we collect

| Data             | Why we collect it                                                                             |
|------------------|-----------------------------------------------------------------------------------------------|
| `command`        | What commands are being run                                                                   |
| `flags`          | Which flags are being used (flag names only, never the values)                                |
| `env-vars`       | Which env vars are being used (var names only, never the values)                              |
| `exit-code`      | Patterns of user errors that we can help with                                                 |
| `duration-ms`    | Measure performance over time, spot regressions and see if any improvements have been helpful |
| `ci`             | See whether a command was run in CI or not                                                    |
| `ci-system`      | Which CI systems our users are using, and how that affects the experience                     |
| `interactive`    | How does interactivity influence how users use the tool                                       |
| `automation-api` | How much is automation API used to drive pulumi                                               |
| `using-ai`       | How much is AI used to drive pulumi                                                           |
| `os`             | Which operating system should we focus on                                                     |
| `arch`           | Which architectures are important to our users                                                |
| `backend`        | Are users using Pulumi Cloud or the DIY backend                                               |
| CLI version      | So we can spot issues in specific versions                                                    |

The schema for this data can be found in [`pkg/telemetry/schema.json`](TODO: add link). Each fact that is sent is validated against the schema first, so this file will always be the authoritative source of what the CLI can send to the backend.

### What we never collect

We never collect any personal data, such as stack, project organization or resource names, no flag/argument values, no environment variable values, error messages or account identity. We don't collect any variable strings, only the fixed strings as they are defined in the schema. This makes it easy to validate what is being sent, and makes it easy to validate that that's safe.

### Identifiers

Telemetry data carries two unique, randomly generated identifiers. The installation ID is unique per installation and stored in `$PULUMI_HOME/telemetry.json`.  We store it so we can correlate telemetry events from a single installation. E.g. 10 errors from a single installation is different from 10 errors from 10 different installations. This installation can be reset any time by deleting `$PULUMI_HOME/telemetry.json`, or removing the UUID from the file.

Additionally, each command invocation has unique, randomly generated identifier as well. This is so we can correlate multiple telemetry events that come from a single command.

## Who is affected

Telemetry events are emitted for both Pulumi Cloud and DIY backend users. Telemetry is not emitted for self hosted Pulumi instances, and the EU Cloud currently.

## Turn telemetry off

Telemetry can be turned off through various methods.  `pulumi telemetry disables` disables telemetry permanently for the installation. There are also two environment variables to disable telemetry, `PULUMI_TELEMETRY=0` and `DO_NOT_TRACK=1` (from https://donottrack.sh/).  Note that if `DO_NOT_TRACK=1` is set, but telemetry is explicitly enabled using `PULUMI_TELEMETRY=1`, or through running `pulumi telemetry enable`, telemetry will be enabled.

## See what is sent

You can see for yourself what is sent by either running `pulumi telemetry log enable`, to log all telemetry that's being sent (or would be sent if telemetry is turned off) to `$PULUMI_HOME/telemetry/log`. Each log contains a marker whether it is sent to the service or not. The same can be achieved using the `PULUMI_TELEMETRY_LOG=1` environment variable.
