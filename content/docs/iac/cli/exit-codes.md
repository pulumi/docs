---
title: Pulumi CLI Exit Codes
h1: Pulumi CLI Exit Codes
meta_desc: Learn how the Pulumi CLI maps internal failures to stable exit codes you can use in CI/CD pipelines, tools, and automations.
menu:
  iac:
    parent: iac-cli
    identifier: iac-cli-exit-codes
    weight: 70
aliases:
  - /docs/iac/cli/error-codes/
meta_image: /images/docs/meta-images/docs-meta.png
---

The Pulumi CLI returns numeric exit codes that indicate the result of a command. Scripts, CI/CD systems, and tools can use these codes to distinguish between different kinds of failures.

> The global CLI exit code mapping described here was introduced in Pulumi CLI **v3.226.1**. Earlier versions may behave differently and do not guarantee the same mapping.

This page explains how Pulumi exit codes work and how to consume them safely in automation. A zero exit code means the operation was **successful**, and any other code means **failure**.

## Error Categories

The exact non-zero value of a failing exit code gives us some information about what went wrong.

| Category                          | Exit code | When it occurs |
|-----------------------------------|----------:|----------------|
| Success                           | 0         | The command completed successfully. |
| Generic error                     | 1         | A failure occurred that does not fit a more specific category. |
| Configuration and validation error | 2         | The CLI cannot run or complete the command because of invalid or missing arguments, configuration, or schema validation, or because required confirmation flags (such as `--yes`) are not provided in non-interactive mode. |
| Authentication or authorization error | 3         | The CLI cannot authenticate or is not authorized to perform the requested operation, for example when login is required, credentials are missing, or access is forbidden. |
| Resource or deployment error      | 4         | A resource operation fails during deployment, preview, refresh, destroy, or import. This includes errors returned by resource providers and underlying cloud platforms. |
| Policy failure                    | 5         | A [policy pack](/docs/iac/policy/policy-as-code/) or organization policy blocks the operation even though the program and providers succeeded. |
| Stack not found                   | 6         | The requested stack does not exist, cannot be found, or no stack is selected. |
| No changes                        | 7         | An expectation about changes is not met, such as when `--expect-no-changes` is used but changes are detected. |
| Canceled run                      | 8         | The operation is canceled before completion, for example due to `pulumi cancel`, a user interrupt (such as Ctrl+C), or cancellation initiated through the Automation API. |
| Timeout                           | 9         | The operation fails because it does not complete within an expected time window. |
| Internal CLI error                | 255       | An unexpected internal condition occurs inside the Pulumi CLI itself that does not fit another category. |
