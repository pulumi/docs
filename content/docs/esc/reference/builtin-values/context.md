---
title: context
title_tag: context
h1: context
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-ref-builtin-values
    identifier: esc-ref-builtin-context
    weight: 1
---

The `context` built-in value provides information about the user evaluting an ESC environment.

## Properties

| Property | Type                              | Description                                                       |
|----------|-----------------------------------|-------------------------------------------------------------------|
| `pulumi` | [PulumiContext](#pulumicontext)   | Information about the Pulumi user that requested evaluation

### PulumiContext

| Property       | Type                              | Description                                                       |
|----------------|-----------------------------------|-------------------------------------------------------------------|
| `user`         | [UserOrOrgInfo](#userororginfo)   | Information about the user
| `organization` | [UserOrOrgInfo](#userororginfo)   | Information about the user's organization

### UserOrOrgInfo

| Property | Type    | Description                                                       |
|----------|---------|-------------------------------------------------------------------|
| `login`  | string  | The name of the user or organization

## Example

```yaml
values:
  greeting: Hello, ${context.pulumi.organization.login}/${context.pulumi.user.login}!
```

### Evaluated result

```json
{
  "greeting": "Hello, org/user!"
}
```
