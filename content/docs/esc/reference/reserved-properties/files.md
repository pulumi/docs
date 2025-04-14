---
title: files
title_tag: files
h1: files
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-ref-reserved-properties
    identifier: esc-ref-reserved-files
    weight: 2
---

The `files` reserved property contains values that should be written to temporary files. For example, [`esc run`](/docs/esc/cli/commands/esc_run) writes the contents of each property in the `files` property to a temporary file and exports the file's path in the named environment variable that is accessible to the command to run.

## Properties

| Property | Type              | Description                                                       |
|----------|-------------------|-------------------------------------------------------------------|
| name     | `string | binary` | The contents of the temporary file whose path will be exported in the environment variable `name`

## Example

```yaml
values:
  files:
    GREETING: Hello, ${context.pulumi.user.login}!
    BINARY:
     fn::fromBase64: ...
```

### Evaluated result

```json
{
  "files": {
    "GREETING": "Hello, user!",
    "BINARY": ...
  }
}
```

### Using `esc run`

```console
$ esc run default/greet -- sh -c 'echo ${GREETING} & cat ${GREETING}'
/tmp/tmp.iBApHfcsJ1
Hello, user!
```
