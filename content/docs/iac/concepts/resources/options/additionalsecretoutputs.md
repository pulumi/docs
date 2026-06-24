---
title_tag: "additionalSecretOutputs | Resource Options"
meta_desc: The additionalSecretOutputs resource option specifies a list of named output properties that should be treated as secrets.
title: "additionalSecretOutputs"
h1: "Resource option: additionalSecretOutputs"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    identifier: additionalSecretOutputs
    parent: options-concepts
    weight: 10
aliases:
  - /docs/intro/concepts/resources/options/additionalsecretoutputs/
  - /docs/concepts/options/additionalsecretoutputs/
  - /docs/iac/concepts/options/additionalsecretoutputs/
---

The `additionalSecretOutputs` resource option specifies a list of named output properties that should be treated as [secrets](/docs/concepts/secrets/), which means they will be encrypted. It augments the list of values that Pulumi detects, based on secret inputs to the resource.

{{< resource-option-scope "additionalSecretOutputs" >}}

This example ensures that the password generated for a database resource is an encrypted secret:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
let db = new Database("new-name-for-db", { /*...*/ },
    { additionalSecretOutputs: ["password"] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database('db',
    opts=ResourceOptions(additional_secret_outputs=['password']))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, err := NewDatabase(ctx, "db", &DatabaseArgs{ /*...*/ },
    pulumi.AdditionalSecretOutputs([]string{"password"}))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Database("new-name-for-db", new DatabaseArgs(),
    new CustomResourceOptions { AdditionalSecretOutputs = { "password" } });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var db = new Database("new-name-for-db",
    DatabaseArgs.Empty,
    CustomResourceOptions.builder()
        .additionalSecretOutputs("password")
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  db:
    type: Database
    options:
      additionalSecretOutputs:
        - password
```

{{% /choosable %}}

{{< /chooser >}}

Only top-level resource properties can be designated secret. If sensitive data is nested inside of a property, you must mark the entire top-level output property as secret.

{{% notes "warning" %}}
A resource's [physical ID](/docs/iac/concepts/resources/names/#physicalid) (the `id` output property) cannot be included in `additionalSecretOutputs`. The `id` is a special property, not a regular output, so it is always stored in plain text in the state file. See [The resource ID cannot be made secret](/docs/concepts/secrets/#the-resource-id-cannot-be-made-secret) for the implications and a workaround.
{{% /notes %}}
