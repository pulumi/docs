---
title: "esc env version | CLI commands"
aliases:
  - /docs/reference/cli/esc_env_version/
meta_desc: "Learn about the esc env version command."
---



Manage versions

## Synopsis

Manage versions

This command describes the referenced environment version.

Subcommands exist for viewing revision history and managingtagged versions.

```
esc env version [<org-name>/][<project-name>/]<environment-name>@<version> [flags]
```

## Options

```
  -h, --help   help for version
      --utc    display times in UTC
```

## Options inherited from parent commands

```
      --env string   The name of the environment to operate on.
```

## SEE ALSO

* [esc env](/docs/esc/cli/commands/esc_env/)	 - Manage environments
* [esc env version history](/docs/esc/cli/commands/esc_env_version_history/)	 - Show revision history.
* [esc env version retract](/docs/esc/cli/commands/esc_env_version_retract/)	 - Retract a specific revision of an environment
* [esc env version rollback](/docs/esc/cli/commands/esc_env_version_rollback/)	 - Roll back to a specific version
* [esc env version tag](/docs/esc/cli/commands/esc_env_version_tag/)	 - Manage tagged versions

###### Auto generated by spf13/cobra on 1-Aug-2025
