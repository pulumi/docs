---
title: passphrase
title_tag: passphrase Pulumi ESC Rotator
meta_desc: The `passphrase` rotator enables you to rotate any user defined key by generating memorable passphrases.
h1: passphrase
menu:
  esc:
    identifier: passphrase-rotator
    parent: esc-rotated-secrets
    weight: 4
---

The `passphrase` rotator enables you to any user defined key in your ESC environment generating memorable passphrases.

{{% notes "info" %}}
If you want to generate _random passwords_ use the [password rotator](../password)
{{% /notes %}}

## Inputs

- **separator**: Specifies a single character to be used as word separator. (default: `-`)
- **capitalize**: if `true` will capitalize each generated word. (default: `false`)
- **length**: The number of words that the generated passphrase will contain. (default: `5`)

## Example

The `passphrase` rotator can be configured for any random user defined key.

```yaml
values:
   fn::rotate::passphrase:
      inputs:
        separator: "%"
        capitalize: true
        length: 4

```

This configuration will genrate passphrases like `Mouth%Purebred%Headstone%Plausibly`.
