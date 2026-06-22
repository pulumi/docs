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
| `length`          | int     | The length of the generated password (8–100). (default: `16`)                                       |
| `lower`           | boolean | Whether to include lowercase characters. (default: `true`)                                          |
| `upper`           | boolean | Whether to include uppercase characters. (default: `true`)                                          |
| `numeric`         | boolean | Whether to include numbers. (default: `true`)                                                       |
| `special`         | boolean | Whether to include special characters. (default: `true`)                                            |
| `minLower`        | int     | The minimum number of lowercase characters to include (0–100). (default: `0`)                       |
| `minUpper`        | int     | The minimum number of uppercase characters to include (0–100). (default: `0`)                       |
| `minNumeric`      | int     | The minimum number of numeric characters to include (0–100). (default: `0`)                         |
| `minSpecial`      | int     | The minimum number of special characters to include (0–100). (default: `0`)                         |
| `overrideSpecial` | string  | The set of special characters to choose from. (default: `!@#$%&*()-_=+[]{}<>:?`)                    |

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

## State (Optional)

| Property   | Type   | Description                            |
|------------|--------|----------------------------------------|
| `current`  | string | The most recently generated password.  |
| `previous` | string | The prior generated password.          |

## Outputs

| Property   | Type   | Description                                            |
|------------|--------|--------------------------------------------------------|
| `current`  | string | The most recently generated password, stored as a secret. |
| `previous` | string | The prior generated password, stored as a secret.      |

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Rotation fails with an invalid input error | `length` is outside 8–100, or the sum of `minLower`, `minUpper`, `minNumeric`, and `minSpecial` exceeds `length`. | Set `length` within range and lower the minimum-count inputs so they fit within the password length. |
| Generated passwords are missing a character class | The class is disabled (`lower`, `upper`, `numeric`, or `special` set to `false`) or its minimum is `0`. | Enable the character class and set its corresponding minimum to require at least one character. |

## Related

- [Rotators](/docs/esc/concepts/rotators/) - How credential rotation works in Pulumi ESC
- [passphrase rotator](/docs/esc/providers/rotators/passphrase/) - Generate memorable passphrases instead of random passwords
- [Rotators reference](/docs/esc/providers/rotators/) - Catalog of all ESC rotators
