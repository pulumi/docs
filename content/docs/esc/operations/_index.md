---
title: Operations
title_tag: Pulumi ESC operations
h1: Operations
meta_desc: Run Pulumi ESC day-to-day — manage secrets, rotate credentials, deploy rotation connectors, and inject environment values into commands and CI jobs.
menu:
  esc:
    identifier: esc-operations
    parent: esc-home
    weight: 5
---

Operational guides for running Pulumi ESC day-to-day: managing secrets in existing environments, rotating credentials, deploying rotation connectors into private networks, and injecting environment values into commands and CI pipelines.

If you are looking for *what* ESC is rather than *how to run it*, start with [Concepts](/docs/esc/concepts/). For reference on the YAML syntax that defines an environment, see [Environments](/docs/esc/concepts/environments/).

## Working with environments

- [Manage secrets](/docs/esc/operations/managing-secrets/) — add, read, and organize secrets inside an environment.
- [Approvals](/docs/esc/concepts/approvals/) — require explicit review and sign-off before applying changes to environments.

## Rotation

- [Rotating secrets](/docs/esc/operations/rotation/) — best practices for rotation, and deploying connectors so rotators can reach databases and services in private networks.

## CI/CD

For continuous integration, the [GitHub Actions integration](/docs/esc/guides/integrate-with/github-actions/) wires ESC short-lived credentials into your workflows. See also the [`gh-login` provider](/docs/esc/providers/login/gh-login/) for ESC-issued GitHub App credentials.
