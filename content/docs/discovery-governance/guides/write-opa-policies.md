---
title: Write OPA policies
title_tag: Write OPA policies | Pulumi Policies
h1: Write OPA policies
meta_desc: Write Pulumi policies in Rego with Open Policy Agent (OPA), including rule naming, the input document, metadata, configuration, testing, and enforcement.
menu:
  discovery-governance:
    name: Write OPA policies
    parent: dg-guides
    weight: 85
---

Pulumi Policies can run policies written in [Rego](https://www.openpolicyagent.org/docs/latest/policy-language/), the policy language of [Open Policy Agent (OPA)](https://www.openpolicyagent.org/). If your team already writes Rego, for example for OPA Gatekeeper or Conftest, you can use the same language to check Pulumi resources. An OPA policy pack also doesn't need Node.js or Python installed on the machines that run Pulumi.

This guide builds a small OPA policy pack and runs it against a Pulumi program. The example uses the `random` provider, so you can run it without any cloud credentials. To write policies in TypeScript or Python instead, see [Write a policy pack](/docs/discovery-governance/guides/write-a-policy-pack/).

OPA policies have a few limits compared with TypeScript and Python policies:

- They can validate resources but can't [remediate](/docs/discovery-governance/guides/write-a-policy-pack/#remediating-policy-violations) them. A policy pack set to `remediate` reports violations without fixing them.
- They can't read [stack tags](/docs/discovery-governance/guides/write-a-policy-pack/#using-stack-tags-in-policies).
- They support a smaller set of [policy fields](/docs/discovery-governance/reference/policy-fields/#opa). There's no `severity`, `remediationSteps`, `url`, `tags`, `framework`, or configuration schema.

## Prerequisites

- [Pulumi CLI](/docs/install/) v3.227.0 or later.
- The OPA language plugin. Install it with:

    ```bash
    pulumi plugin install language opa
    ```

- Optional: the [OPA CLI](https://www.openpolicyagent.org/docs/latest/#running-opa), to [test your policies](#test-your-policies).

## Create a policy pack

An OPA policy pack is a directory that contains a `PulumiPolicy.yaml` file and one or more `.rego` files.

To start from a template, run `pulumi policy new` with one of the OPA templates: `aws-opa`, `azure-opa`, `gcp-opa`, or `kubernetes-opa`:

```bash
mkdir policy-pack && cd policy-pack
pulumi policy new aws-opa
```

To follow this guide, create the files by hand instead. Create a `PulumiPolicy.yaml` file:

```yaml
runtime: opa
version: 0.1.0
description: Example OPA policy pack for random resources.
```

Always set `version`. Pulumi uses it to identify the pack in the output of `pulumi preview` and when you [publish](#publish-and-enforce) the pack, and warns with `warning[opa/missing-version]` if it's missing. For every field, see the [project file reference](/docs/discovery-governance/reference/policy-project-file/).

Every `.rego` file in the pack must declare the same package. The package name becomes the policy pack's name.

## Write rules

Create a file named `random.rego` with two rules:

```rego
package random

import rego.v1

deny_short_strings contains msg if {
    input.__type == "random:index/randomString:RandomString"
    input.length < 12
    msg := sprintf("RandomString '%s' has length %d; the minimum is 12", [input.__name, input.length])
}

warn_special_chars contains msg if {
    input.__type == "random:index/randomString:RandomString"
    input.special == true
    msg := sprintf("RandomString '%s' includes special characters", [input.__name])
}
```

Each rule produces a set of messages. The rule is evaluated once for each resource, with the resource as `input`. Every message the rule produces is reported as a violation. If a rule produces no messages, the resource complies.

{{% notes type="info" %}}
Include `import rego.v1` in every file and use the `contains` and `if` keywords, as shown here. The Pulumi analyzer and the OPA CLI both accept this syntax. Without the import, the analyzer fails to compile rules written with `contains` and `if`, and the OPA CLI rejects rules written in the older syntax, such as `deny_short_strings[msg] {`.
{{% /notes %}}

### Rule names and enforcement levels

A rule's name tells Pulumi what it checks and how strictly to enforce it:

| Prefix | Evaluated against | Enforcement level |
|--------|-------------------|-------------------|
| `deny` or `violation` | Each resource | Mandatory: the deployment is blocked |
| `warn` | Each resource | Advisory: a warning is reported |
| `stack_deny` or `stack_violation` | All the stack's resources at once | Mandatory |
| `stack_warn` | All the stack's resources at once | Advisory |

A rule name is either a prefix on its own, such as `deny`, or a prefix followed by an underscore and a descriptive suffix, such as `deny_short_strings`. Prefixes are case-sensitive. Rules with any other name are treated as helpers: they aren't evaluated as policies, but other rules can use them.

If a rule looks like a policy but doesn't match a prefix, such as `denySpecial` or `require_versioning`, Pulumi warns that it won't be evaluated:

```output
warning[opa/unrecognized-rule]: rule "denySpecial" in module "p" will NOT be evaluated because its name does not match a recognized rule prefix, so it is being treated as a helper routine.
```

If no rule in the pack matches a prefix, Pulumi also reports `warning[opa/zero-rules]`, because the pack enforces nothing.

You can override a rule's enforcement level with [configuration](#configuration).

## The input document

When Pulumi evaluates a resource rule, `input` holds the resource. Here's the `input` for the `api-token` resource in the [example program](#run-the-policy-pack), trimmed slightly:

```json
{
  "__name": "api-token",
  "__type": "random:index/randomString:RandomString",
  "__urn": "urn:pulumi:dev::opa-demo::random:index/randomString:RandomString::api-token",
  "__options": {
    "protect": false,
    "parent": "urn:pulumi:dev::opa-demo::pulumi:pulumi:Stack::opa-demo-dev",
    "deleteBeforeReplace": null,
    "ignoreChanges": null,
    "aliases": null,
    "additionalSecretOutputs": null,
    "customTimeouts": {"create": 0, "delete": 0, "update": 0}
  },
  "__provider": {
    "name": "default",
    "type": "pulumi:providers:random",
    "urn": "urn:pulumi:dev::opa-demo::pulumi:providers:random::default",
    "properties": {}
  },
  "__properties": {"length": 8, "special": true},
  "length": 8,
  "special": true
}
```

| Field | Contents |
|-------|----------|
| `__type` | The resource's full type token, such as `random:index/randomString:RandomString`. |
| `__name` | The resource's logical name. |
| `__urn` | The resource's URN. |
| `__options` | The resource's options, such as `protect`, `parent`, and `ignoreChanges`. |
| `__provider` | The provider resource's name, type, URN, and properties. |
| `__properties` | The resource's properties, as an object. `__props` is an alias. |
| Each property | The resource's properties are also copied to the top level of `input`, such as `input.length`. |

Each field is also available without the `__` prefix, such as `input.type` and `input.name`. Prefer the `__` forms: a resource property with the same name, such as a property called `type`, can collide with the unprefixed field.

Keep these details in mind when you match resources:

- **Use the full type token.** Rules compare `__type` against the full token, such as `random:index/randomString:RandomString`. The `pulumi preview` output shows a shorter form, `random:index:RandomString`, which never matches. To find a resource's full type token, see its API documentation in the [Pulumi Registry](/registry/).
- **Only the properties your program sets are present during a preview.** Provider defaults and output properties aren't in `input` until after the resource is created. A rule that checks for a property your program doesn't set sees it as undefined.

## Stack-level rules

Rules with a `stack_` prefix run once for the whole stack. `input.resources` holds every resource in the stack, each in the same shape as the resource `input` above. Add these rules to `random.rego`:

```rego
stack_deny_too_many_passwords contains msg if {
    passwords := [r | some r in input.resources; r.__type == "random:index/randomPassword:RandomPassword"]
    count(passwords) > 1
    msg := sprintf("Stack has %d RandomPassword resources; the maximum is 1", [count(passwords)])
}

stack_warn_unprotected contains msg if {
    some r in input.resources
    startswith(r.__type, "random:")
    not r.__options.protect
    msg := sprintf("Resource '%s' is not protected", [r.__name])
}
```

`input.resources` also contains the stack itself (`pulumi:pulumi:Stack`) and provider resources such as `pulumi:providers:random`. Filter by type, as these rules do, so that a rule only checks the resources you mean it to.

## Metadata annotations

To describe a rule in Pulumi Cloud, add a [`# METADATA` annotation](https://www.openpolicyagent.org/docs/latest/policy-reference/#annotations) directly above it:

```rego
# METADATA
# title: Minimum string length
# description: Random strings must be at least 12 characters long.
# custom:
#   message: Increase the length property to at least 12.
deny_short_strings contains msg if {
    ...
}
```

| Annotation | Purpose |
|------------|---------|
| `title` | The policy's display name in Pulumi Cloud. Defaults to the name of the `.rego` file, without its extension. |
| `description` | A short description of what the policy checks. |
| `custom.message` | A message shown with the policy's violations in Pulumi Cloud, such as how to fix them. |

To set a display name for the whole pack, add a `title` annotation with `scope: package` above the `package` line:

```rego
# METADATA
# title: Random resource policies
# scope: package
package random
```

The `pulumi preview` output identifies violations by rule name and shows the message the rule produced. The annotations appear in Pulumi Cloud after you [publish](#publish-and-enforce) the pack. For how these annotations map to other languages' policy fields, see the [policy fields reference](/docs/discovery-governance/reference/policy-fields/#opa).

## Configuration

Configuration lets people who apply your policy pack adjust its behavior without changing the code. A rule reads its configuration from `data.config.<rule_name>`. Change `deny_short_strings` to read the minimum length from configuration instead of hard-coding it:

```rego
deny_short_strings contains msg if {
    input.__type == "random:index/randomString:RandomString"
    min_length := data.config.deny_short_strings.minLength
    input.length < min_length
    msg := sprintf("RandomString '%s' has length %d; the minimum is %d", [input.__name, input.length, min_length])
}
```

Provide the values in a JSON file, with each rule's values directly under its name:

```json
{
    "deny_short_strings": {
        "minLength": 12
    }
}
```

A rule that reads a configuration value doesn't fire when the value isn't set, because the lookup is undefined. When no configuration is provided at all, `data.config` itself is undefined, so `object.get(data.config, ...)` with a default value doesn't help. If a rule must always run, read the value through a helper rule with a `default`:

```rego
default min_length := 12

min_length := data.config.deny_short_strings.minLength

deny_short_strings contains msg if {
    input.__type == "random:index/randomString:RandomString"
    input.length < min_length
    msg := sprintf("RandomString '%s' has length %d; the minimum is %d", [input.__name, input.length, min_length])
}
```

The same file can also override enforcement levels, either for every rule with the `all` key or for individual rules. An `enforcementLevel` key sits alongside a rule's other values and isn't passed to the rule:

```json
{
    "all": "advisory",
    "deny_short_strings": {
        "enforcementLevel": "mandatory",
        "minLength": 12
    },
    "warn_special_chars": "disabled"
}
```

OPA policy packs don't currently support configuration schemas.

## Test your policies

Because OPA policies are plain Rego, you can unit test them with the OPA CLI. Create `random_test.rego` in the policy pack directory. Use `with` to supply the `input` and configuration for each test:

```rego
package random

import rego.v1

test_short_string_denied if {
    count(deny_short_strings) == 1 with input as {
        "__type": "random:index/randomString:RandomString",
        "__name": "token",
        "length": 8,
    }
        with data.config.deny_short_strings.minLength as 12
}

test_long_string_allowed if {
    count(deny_short_strings) == 0 with input as {
        "__type": "random:index/randomString:RandomString",
        "__name": "token",
        "length": 16,
    }
        with data.config.deny_short_strings.minLength as 12
}

test_short_string_ignored_without_config if {
    count(deny_short_strings) == 0 with input as {
        "__type": "random:index/randomString:RandomString",
        "__name": "token",
        "length": 8,
    }
}

test_two_passwords_denied if {
    count(stack_deny_too_many_passwords) == 1 with input as {"resources": [
        {"__type": "random:index/randomPassword:RandomPassword", "__name": "a"},
        {"__type": "random:index/randomPassword:RandomPassword", "__name": "b"},
    ]}
}
```

Run the tests:

```bash
opa test -v .
```

```output
data.random.test_short_string_denied: PASS
data.random.test_long_string_allowed: PASS
data.random.test_short_string_ignored_without_config: PASS
data.random.test_two_passwords_denied: PASS
--------------------------------------------------------------------------------
PASS: 4/4
```

Test files can stay in the policy pack directory. Pulumi ignores `test_` rules.

To see exactly what a rule receives, add a temporary rule that reports the whole `input` as its message, then run `pulumi preview`:

```rego
warn_debug_input contains msg if {
    input.__name == "api-token"
    msg := json.marshal(input)
}
```

## Run the policy pack

To try the policy pack, create a Pulumi program in a separate directory. This Pulumi YAML program declares four `random` resources, several of which violate the policies:

```yaml
name: opa-demo
runtime: yaml
resources:
  api-token:
    type: random:RandomString
    properties:
      length: 8
      special: true
  bucket-suffix:
    type: random:RandomString
    properties:
      length: 16
      special: false
      upper: false
    options:
      protect: true
  db-password:
    type: random:RandomPassword
    properties:
      length: 32
  admin-password:
    type: random:RandomPassword
    properties:
      length: 32
```

Save the configuration from the [Configuration](#configuration) section as `policy-config.json`, then run a preview with the policy pack:

```bash
pulumi preview --policy-pack ../policy-pack --policy-pack-config policy-config.json
```

```output
Policies:
    ❌ random@v0.1.0 (local: .../policy-pack)
        - [mandatory]  deny_short_strings  (random:index:RandomString: api-token)
          RandomString 'api-token' has length 8; the minimum is 12
        - [mandatory]  stack_deny_too_many_passwords  (pulumi:pulumi:Stack: opa-demo-dev)
          Stack has 2 RandomPassword resources; the maximum is 1
        - [advisory]  stack_warn_unprotected  (pulumi:pulumi:Stack: opa-demo-dev)
          Resource 'admin-password' is not protected
        - [advisory]  stack_warn_unprotected  (pulumi:pulumi:Stack: opa-demo-dev)
          Resource 'api-token' is not protected
        - [advisory]  stack_warn_unprotected  (pulumi:pulumi:Stack: opa-demo-dev)
          Resource 'db-password' is not protected
        - [advisory]  warn_special_chars  (random:index:RandomString: api-token)
          RandomString 'api-token' includes special characters

Diagnostics:
  pulumi:pulumi:Stack (opa-demo-dev):
    error: preview failed
```

The mandatory violations fail the preview, and the command exits with a non-zero status, which fails a CI job. Violations of stack-level rules are reported against the `pulumi:pulumi:Stack` resource. If you run the preview without `--policy-pack-config`, `deny_short_strings` doesn't fire, because its configuration is missing.

## Publish and enforce

{{< pulumi-cloud "custom-policy-packs" />}}

To apply the policy pack across your organization without passing `--policy-pack` on each command, publish it to Pulumi Cloud from the policy pack directory:

```bash
pulumi policy publish
```

Then add the pack to a [policy group](/docs/discovery-governance/concepts/policy-as-code/policy-groups/). Every machine that runs Pulumi against a stack in that group, including CI runners, needs the OPA language plugin installed with `pulumi plugin install language opa`. A preventative policy group checks stacks during `pulumi preview` and `pulumi up`, and an audit policy group checks discovered cloud resources. For the full workflow, see [Enforce policy as code](/docs/discovery-governance/get-started/enforce-policy-as-code/).

## Reuse OPA Gatekeeper policies

If you have Rego policies written for [OPA Gatekeeper](https://open-policy-agent.github.io/gatekeeper/), you can run them against Pulumi's Kubernetes resources without changing them. Set `inputFormat: kubernetes-admission` in `PulumiPolicy.yaml`, and Pulumi presents each resource in the admission review structure that Gatekeeper policies expect. A pack uses one input format for all its rules, so keep Gatekeeper policies in their own pack. For the details, see [`inputFormat`](/docs/discovery-governance/reference/policy-project-file/#inputformat).

## Troubleshooting

If a rule never reports a violation:

- **Check the rule's name.** Look for `warning[opa/unrecognized-rule]` in the `pulumi preview` output. See [Rule names and enforcement levels](#rule-names-and-enforcement-levels).
- **Check the type token.** Compare against the full token, such as `random:index/randomString:RandomString`, not the short form shown in `pulumi preview` output.
- **Check that the property is present.** During a preview, `input` contains only the properties your program sets.
- **Check the configuration.** A rule that reads `data.config` doesn't fire without its configuration value. Configuration values go directly under the rule's name, not under a `properties` key.
- **Inspect the input.** Add a temporary rule that reports `json.marshal(input)`, as shown in [Test your policies](#test-your-policies).

If the pack fails to load with `rego_parse_error: var cannot be used for rule name`, add `import rego.v1` to each `.rego` file.
