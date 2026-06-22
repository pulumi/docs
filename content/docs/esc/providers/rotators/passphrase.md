---
title: passphrase
title_tag: passphrase Pulumi ESC Rotator
meta_desc: The `passphrase` rotator enables you to rotate any user-defined key by generating memorable passphrases.
h1: passphrase
menu:
  esc:
    identifier: passphrase-rotator
    parent: esc-providers-rotators
    weight: 1
aliases:
  - /docs/esc/integrations/rotated-secrets/passphrase/
  - /docs/esc/concepts/providers/rotators/passphrase/
---

The `passphrase` rotator enables you to rotate any user-defined key in your ESC environment by generating memorable passphrases.

{{% notes "info" %}}
If you want to generate _random passwords_ use the [password rotator](/docs/esc/providers/rotators/password/)
{{% /notes %}}

## Inputs

| Property     | Type    | Description                                                                |
|--------------|---------|---------------------------------------------------------------------------|
| `separator`  | string  | A single character used as the word separator. (default: `-`)             |
| `capitalize` | boolean | If `true`, each generated word is capitalized. (default: `false`)         |
| `length`     | int     | The number of words the generated passphrase will contain. (default: `5`) |

## Example

The `passphrase` rotator can be configured for any user-defined key.

```yaml
values:
  mypassphrase:
    fn::rotate::passphrase:
      inputs:
        separator: "%"
        capitalize: true
        length: 4
```

This configuration will generate passphrases like `Mouth%Purebred%Headstone%Plausibly`.

When you open the environment, you should see output similar to the following:

```json
{
  "mypassphrase": {
    "current": "[secret]",
    "previous": "[secret]"
  }
}
```

<!-- TODO(SME): verify the passphrase rotator output schema — confirm the current/previous shape and whether the generated value is nested under a property. -->

## State (Optional)

| Property   | Type   | Description                                                                                    |
|------------|--------|------------------------------------------------------------------------------------------------|
| `current`  | string | Current generated passphrase. This is the newest and recommended value.                        |
| `previous` | string | Previous generated passphrase. This value is still valid, but will be phased out next rotation. |

## Outputs

| Property   | Type   | Description                                                                                    |
|------------|--------|------------------------------------------------------------------------------------------------|
| `current`  | string | Current generated passphrase, stored as a secret.                                              |
| `previous` | string | Previous generated passphrase, stored as a secret.                                             |

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Rotation fails with an invalid input error | `length` is set below the minimum or `separator` is more than a single character. | Set `length` to a positive integer and `separator` to a single character, then rotate again. |
| The generated passphrase is shorter or longer than expected | `length` counts words, not characters. | Adjust `length` to the desired number of words; the character count varies with the words chosen. |

<!-- TODO(SME): verify exact validation error strings and input bounds for the passphrase rotator. -->

## Related

- [Rotators](/docs/esc/concepts/rotators/) - How credential rotation works in Pulumi ESC
- [password rotator](/docs/esc/providers/rotators/password/) - Generate random passwords instead of memorable passphrases
- [Rotators reference](/docs/esc/providers/rotators/) - Catalog of all ESC rotators
