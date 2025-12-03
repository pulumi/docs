---
title: password
title_tag: password Pulumi ESC Rotator
meta_desc: The `password` rotator enables you to rotate any user defined key by generating random passwords.
h1: password
menu:
  esc:
    identifier: password-rotator
    parent: esc-rotated-secrets
    weight: 1
---

The `password` rotator enables you to rotate any user defined key by generating random passwords.

{{% notes "info" %}}
If you want to generate _memorable passphrases_ use the [passphrase rotator](../passphrase)
{{% /notes %}}

## Inputs

- **length**: The length of the generated passwords. (default `16`)
- **lower**: If `true` the generated passwords will contain lowercase characters. (default: `true`)
- **upper**: If `true` the generated passwords will contain uppercase characters. (default: `true`)
- **special**: If `true` the generated passwords will contain special  characters. (default: `true`)
- **minUpper**: The minimum number of uppercase characters that the generated passwords will contain. (default: `0`)
- **minLower**: The minimum number of lowercase characters that the generated passwords will contain. (default: `0`)
- **minSpecial**: The minimum number of special characters that the generated passwords will contain. (default: `0`)
- **overrideSpecial**: a string containing all the special characters that can be used to generate passwords. (default: `!@#$%&*()-_=+[]{}<>:?`)

## Example

The `password` rotator can be configured for any random user defined key.

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
