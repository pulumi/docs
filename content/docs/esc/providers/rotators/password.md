---
title: password
title_tag: password Pulumi ESC Rotator
meta_desc: The `password` rotator enables you to rotate any user-defined key by generating random passwords.
h1: password
menu:
  esc:
    identifier: password-rotator
    parent: esc-providers-rotators
    weight: 1
aliases:
  - /docs/esc/integrations/rotated-secrets/password/
  - /docs/esc/concepts/providers/rotators/password/
---

The `password` rotator enables you to rotate any user-defined key by generating random passwords.

{{% notes "info" %}}
If you want to generate _memorable passphrases_ use the [passphrase rotator](/docs/esc/providers/rotators/passphrase/)
{{% /notes %}}

## Inputs

| Property          | Type    | Description                                                                                          |
|-------------------|---------|-----------------------------------------------------------------------------------------------------|
| `length`          | int     | The length of the generated passwords. (default: `16`)                                              |
| `lower`           | boolean | If `true`, the generated passwords will contain lowercase characters. (default: `true`)             |
| `upper`           | boolean | If `true`, the generated passwords will contain uppercase characters. (default: `true`)             |
| `special`         | boolean | If `true`, the generated passwords will contain special characters. (default: `true`)               |
| `minUpper`        | int     | The minimum number of uppercase characters the generated passwords will contain. (default: `0`)     |
| `minLower`        | int     | The minimum number of lowercase characters the generated passwords will contain. (default: `0`)     |
| `minSpecial`      | int     | The minimum number of special characters the generated passwords will contain. (default: `0`)       |
| `overrideSpecial` | string  | The set of special characters that can be used to generate passwords. (default: `!@#$%&*()-_=+[]{}<>:?`) |

## Example

The `password` rotator can be configured for any user-defined key.

```yaml
values:
  mypassword:
    fn::rotate::password:
      inputs:
        minLower: 2
        minUpper: 3
        minSpecial: 5
        overrideSpecial: "!@#$%&*()-_=+[]{}<>:"
        length: 15
```

The previous example will generate passwords like: `wn#ZQH}z$[H_&h*`

When you open the environment, you should see output similar to the following:

```json
{
  "mypassword": {
    "current": "[secret]",
    "previous": "[secret]"
  }
}
```

<!-- TODO(SME): verify the password rotator output schema — confirm the current/previous shape and whether the generated value is nested under a property. -->

## State (Optional)

| Property   | Type   | Description                                                                                   |
|------------|--------|-----------------------------------------------------------------------------------------------|
| `current`  | string | Current generated password. This is the newest and recommended value.                         |
| `previous` | string | Previous generated password. This value is still valid, but will be phased out next rotation. |

## Outputs

| Property   | Type   | Description                                        |
|------------|--------|----------------------------------------------------|
| `current`  | string | Current generated password, stored as a secret.    |
| `previous` | string | Previous generated password, stored as a secret.   |

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Rotation fails with an invalid input error | The sum of `minLower`, `minUpper`, and `minSpecial` exceeds `length`. | Increase `length` or lower the minimum-count inputs so they fit within the password length. |
| Generated passwords are missing a character class | The class is disabled (`lower`, `upper`, or `special` set to `false`) or its minimum is `0`. | Enable the character class and set its corresponding minimum to require at least one character. |

<!-- TODO(SME): verify exact validation error strings and input bounds for the password rotator. -->

## Related

- [Rotators](/docs/esc/concepts/rotators/) - How credential rotation works in Pulumi ESC
- [passphrase rotator](/docs/esc/providers/rotators/passphrase/) - Generate memorable passphrases instead of random passwords
- [Rotators reference](/docs/esc/providers/rotators/) - Catalog of all ESC rotators
