---
title: "esc env rotate | CLI commands"
aliases:
  - /docs/reference/cli/esc_env_rotate/
meta_desc: "Learn about the esc env rotate command."
---



Rotate secrets in an environment

## Synopsis

Rotate secrets in an environment

Optionally accepts any number of Property Paths as additional arguments. If given any paths, will only rotate secrets at those paths.


```
esc env rotate [<org-name>/][<project-name>/]<environment-name> [path(s) to rotate] [flags]
```

## Options

```
  -h, --help   help for rotate
```

## Options inherited from parent commands

```
      --env string   The name of the environment to operate on.
```

## SEE ALSO

* [esc env](/docs/esc/cli/commands/esc_env/)	 - Manage environments

###### Auto generated by spf13/cobra on 1-Aug-2025
