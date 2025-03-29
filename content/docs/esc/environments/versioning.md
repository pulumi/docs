---
title: Versioning
title_tag: Environment versioning | Pulumi ESC
h1: Pulumi ESC environment versioning
meta_desc: Pulumi ESC allows you to manage, track and audit changes to your secrets
  and configurations with versioning.

menu:
  esc:
    identifier: esc-versioning
    parent: esc-environments
    weight: 3
search:
  keywords:
    - versioning
    - environment
    - revisions
    - environment versioning
    - version history
    - tagged versions
---

Each time a change is made to an environment, a new immutable revision is created. You can manage and track changes to your secrets and configuration over time with a clear history you can audit, compare, and roll back.  You can assign tags to revisions, such as `production`, `v1.2.1`, or `stable`, to help organize and identify them.

When [importing an environment](/docs/esc/environments/imports/), you can choose to pin it to a specific version using a tag or revision number. This prevents automatic updates from the source environment, making it easier to test and roll out changes gradually. You can also specify which version to use when running commands with `esc run`, allowing you to target different environments for different tasks.

## View and compare version history

You can see the history of revisions using `esc env version history` or in the Pulumi Cloud Console.

```bash
$ esc env version history myorg/test
revision 3 (tag: latest)
Author: <Name> <User-ID>
Date: 2024-04-18 12:42:18.02 -0700 PDT

revision 2
...
```

Compare revisions using `esc env diff`.

```bash
$ esc env diff myorg/test@3 myorg/test@2
 Value

    --- myorg/test@3
    +++ myorg/test@2
...
```

## Tagging versions

You can tag your revisions with meaningful names like `prod`, or `stable`. Each environment has a built-in `latest` tag that always points to the environment’s most recent revision. Use `esc env version tag` to tag a revision.

To tag revision 3 of the `test` environment as `prod` for example, you can use the following command:

```bash
$ esc env version tag myorg/test@prod @3
```

### Using tagged versions

Once you tag a revision, you can use the tag to [open](/docs/esc/environments/working-with-environments/#opening-an-environment) a specific environment version.

```bash
$ esc open myorg/test@prod
```

You can specify the tagged version when importing the environment. This helps you ensure that you are importing a stable environment version that is not affected by changes.

```yaml
# Importing in another ESC Environment
imports:
  - test@prod

# Importing in Pulumi stack Config
# Pulumi.dev.yaml
environment:
  - test@prod
```
