---
title: files
title_tag: files
h1: files
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-ref-well-known-properties
    identifier: esc-ref-well-known-files
    weight: 1
---

The `files` well-known property contains values that should be written to temporary files. For example, [`esc run`](/docs/esc/cli/commands/esc_run) writes the contents of each property in the `files` property to a temporary file and exports the file's path in the named environment variable that is accessible to the command to run.

## Properties

| Property | Type   | Description                                                       |
|----------|--------|-------------------------------------------------------------------|
| name     | string | The contents of the temporary file whose path will be exported in the environment variable `name`

## Example

```yaml
values:
  files:
    GREETING: Hello, ${context.pulumi.user.login}!
```

### Evaluated result

```json
{
  "files": {
    "GREETING": "Hello, user!"
  }
}
```

### Using `esc run`

```console
$ esc run default/greet -- sh -c 'echo ${GREETING} & cat ${GREETING}'
/tmp/tmp.iBApHfcsJ1
Hello, user!
```
