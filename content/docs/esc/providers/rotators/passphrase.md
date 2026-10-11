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

{{% notes type="info" %}}
If you want to generate _random passwords_ use the [password rotator](/docs/esc/providers/rotators/password/)
{{% /notes %}}

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

## Schema reference

{{< esc-schema-updated >}}

### Inputs

{{< esc-schema type="rotator" name="passphrase" section="inputs" >}}

### State

{{< esc-schema type="rotator" name="passphrase" section="state" >}}

### Outputs

{{< esc-schema type="rotator" name="passphrase" section="outputs" >}}

## Troubleshooting

| Symptom | Likely cause | Resolution |
|---------|--------------|------------|
| Rotation fails with an invalid input error | `length` is outside 3–15, or `separator` is not a single character. | Set `length` within range and `separator` to a single character, then rotate again. |
| The generated passphrase is shorter or longer than expected | `length` counts words, not characters. | Adjust `length` to the desired number of words; the character count varies with the words chosen. |

## Related

- [Rotators](/docs/esc/concepts/rotators/) - How credential rotation works in Pulumi ESC
- [password rotator](/docs/esc/providers/rotators/password/) - Generate random passwords instead of memorable passphrases
- [Rotators reference](/docs/esc/providers/rotators/) - Catalog of all ESC rotators
