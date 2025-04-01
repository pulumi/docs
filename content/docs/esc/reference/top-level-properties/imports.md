---
title: imports
title_tag: imports
h1: imports
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-ref-top-level-properties
    identifier: esc-ref-imports
    weight: 1
---

The `imports` top-level property is a list of other environments that this environment imports. Imported environments are evaluated and merged to form the basis for the current environment, which is then evaluated and merged with the imported values. Merging is performed using the [JSON Merge Patch](https://www.rfc-editor.org/rfc/rfc7386) algorithm.

## Environment names

Each entry in the `imports` list names an environment to import. Environment names should be qualified with a project (e.g. `my-project/dev`). If no project name is given, the default project is assumed (e.g. the unqualidied name `foo` refers to `default/foo`):

```yaml
imports:
  - auth-core          # Imports the "auth-core" environment in the "default" project
  - network-infra/dev  # Imports the "dev" environment in the "network-infra" project
```

## Import options

It is sometimes desirable to control the behavior of an import. This can be done using import options:

```yaml
imports:
  - auth-core: { merge: false } # Import "default/auth-core", but do add it to the merge stack
```

There is currently a single option, `merge`, which controls whether or not an imported environment is added to the merge stack. Unmerged imports are still available via the `imports` built-in property.
