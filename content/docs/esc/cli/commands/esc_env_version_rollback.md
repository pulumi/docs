---
title: "esc env version rollback | CLI commands"
aliases:
  - /docs/reference/cli/esc_env_version_rollback/
meta_desc: "Learn about the esc env version rollback command."
---



Roll back to a specific version

## Synopsis

Roll back to a specific version

This command rolls an environment's definition back to the specified
version. The environment's definition will be replaced with the
definition at that version, creating a new revision.


```
esc env version rollback [<org-name>/][<project-name>/]<environment-name>@<version> [flags]
```

## Options

```
      --draft string[="new"]   set flag without a value (--draft) to create a draft rather than saving changes directly. --draft=<change-request-id> to update an existing change request.
  -h, --help                   help for rollback
```

## Options inherited from parent commands

```
      --env string   The name of the environment to operate on.
```

## SEE ALSO

* [esc env version](/docs/esc/cli/commands/esc_env_version/)	 - Manage versions

###### Auto generated by spf13/cobra on 1-Aug-2025
