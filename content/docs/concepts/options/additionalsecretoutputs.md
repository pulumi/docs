---
title_tag: "additionalSecretOutputs | Resource Options"
meta_desc: The additionalSecretOutputs resource option specifies a list of named output properties that should be treated as secrets.
title: "additionalSecretOutputs"
h1: "Resource option: additionalSecretOutputs"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    identifier: additionalSecretOutputs
    parent: options
    weight: 1
aliases:
- /docs/intro/concepts/resources/options/additionalsecretoutputs/
---

The `additionalSecretOutputs` resource option specifies a list of named output properties that should be treated as [secrets](/docs/concepts/secrets/), which means they will be encrypted. It augments the list of values that Pulumi detects, based on secret inputs to the resource.

This example ensures that the password generated for a database resource is an encrypted secret:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let db = new Database("new-name-for-db", { /*...*/ },
    { additionalSecretOutputs: ["password"] });
```

{{% /choosable %}}
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

{{% notes type="warning" %}}
The `additionalSecretOutputs` resource option does not apply to component resources, and will not have the intended effect.
{{% /notes %}}
