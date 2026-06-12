---
title: imports
title_tag: imports
h1: imports
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
aliases:
  - /docs/reference/esc-syntax/top-level-keys/imports/
  - /docs/esc/reference/top-level-keys/imports/
menu:
  esc:
    parent: esc-syntax-top-level-keys
    identifier: esc-syntax-imports
    weight: 1
---

The `imports` top-level key is a list of other environments that this environment imports. Imported environments are evaluated and merged to form the basis for the current environment, which is then evaluated and merged with the imported values. Merging is performed using the [JSON Merge Patch](https://www.rfc-editor.org/rfc/rfc7396) algorithm.

## Environment names

Each entry in the `imports` list names an environment to import. Environment names should be qualified with a project (e.g. `my-project/dev`). If no project name is given, the default project is assumed (e.g. the unqualified name `foo` refers to `default/foo`):

```yaml
imports:
  - auth-core          # Imports the "auth-core" environment in the "default" project
  - network-infra/dev  # Imports the "dev" environment in the "network-infra" project
```

## Import options

To control the behavior of an import, specify an object with options instead of a plain string:

```yaml
imports:
  - auth-core: { merge: false } # Import "default/auth-core", but don't add it to the merge stack
```

### Available options

| Option  | Type    | Default | Description |
|---------|---------|---------|-------------|
| `merge` | boolean | `true`  | Whether to add the imported environment to the merge stack. When `false`, the environment is evaluated but its values are not automatically merged into the current environment. Unmerged imports are still accessible via the [`imports` built-in property](/docs/esc/environments/syntax/builtin-properties/imports). |
