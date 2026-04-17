---
title_tag: "Resource Names and Identity"
meta_desc: A resource in Pulumi has a logical name, physical name, physical ID, and URN. Learn about these four forms of resource identity and when to use each one.
title: Names
h1: Resource names and identity
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Names
        parent: iac-concepts-resources
        weight: 1
    concepts:
        parent: resources
        weight: 1
aliases:
- /docs/intro/concepts/resources/names/
- /docs/concepts/resources/names/
---

Each resource in Pulumi carries four distinct forms of identity that serve different purposes. Understanding when to use each one is essential to reading and writing Pulumi programs correctly:

- **Logical name** — the name you give the resource in your program. Pulumi uses it for state tracking and URN generation.
- **Physical name** — the name Pulumi assigns in the cloud provider, usually derived from the logical name plus a random suffix.
- **Physical ID** — the identifier the cloud provider returns after creating the resource (e.g., an AWS ARN or a GCP self-link). Exposed as `resource.id`.
- **URN** — a Pulumi-internal globally unique identifier derived from the stack, project, resource type, and logical name. Exposed as `resource.urn`.

The sections below explain each form in detail. For a quick reference on which identity form to use in a given context, see the [identity summary table](#identity-summary).

Pulumi [auto-names](#autonaming) most resources by default, using the logical name and a random suffix to construct a unique physical name for a resource. You can provide explicit names to override this default, and you can [customize or disable auto-naming](#autonaming-configuration) globally, per provider, or per resource type.

{{% notes type="warning" %}}
Be careful when you change a resource's name because changing the name of a resource will create a new resource and delete the old/original resource. If you'd like to rename a resource without destroying the old one, refer to the [aliases](/docs/concepts/options/aliases/) resource option.
{{% /notes %}}

## Logical Names {#logicalname}

Every resource managed by Pulumi has a logical name that you specify as an argument to its constructor. For instance, the logical name of this IAM role is `my-role`:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
let role = new aws.iam.Role("my-role");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
role = iam.Role("my-role")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
role, err := iam.NewRole(ctx, "my-role", &iam.RoleArgs{})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var role = new Aws.Iam.Role("my-role");
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var role = new com.pulumi.aws.iam.Role("my-role");
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  my-role:
    type: aws:iam:Role
```

{{% notes type="info" %}}

In Pulumi YAML, you always use the logical name of a resource (e.g., my-role in the above)
to refer to it. There are no distinct variable names, as there are in other languages.

{{% /notes %}}

{{% /choosable %}}

{{< /chooser >}}

The logical name you specify during resource creation is used in two ways:

- As a default prefix for the resource’s physical name, assigned by the cloud provider.
- To construct the [Universal Resource Name (URN)](#urns) used to track the resource across updates.

Pulumi uses the logical name to track the identity of a resource through multiple deployments of the same program and uses it to choose between creating new resources or updating existing ones.

The variable names assigned to resource objects are not used for either logical or physical resource naming. The variable only refers to that resource in the program. For example, in this code:

```typescript
var foo = new aws.Thing("my-thing");
```

The variable name `foo` has no bearing at all on the resulting infrastructure. You could change it to another name, run `pulumi up`, and the result would be no changes. The only exception is if you export that variable, in which case the name of the export would change to the new name.

## Physical Names and Auto-Naming {#autonaming}

A resource’s logical and physical names may not match. In fact, most physical resource names in Pulumi are, by default, auto-named. As a result, even if your IAM role has a logical name of `my-role`, the physical name will typically look something like `my-role-d7c2fa0`. The suffix appended to the end of the name is random.

This random suffix serves two purposes:

- It ensures that two stacks for the same project can be deployed without their resources colliding. The suffix helps you to create multiple instances of your project more easily, whether because you want, for example, many development or testing stacks, or to scale to new regions.
- It allows Pulumi to do zero-downtime resource updates. Due to the way some cloud providers work, certain updates require replacing resources rather than updating them in place. By default, Pulumi creates replacements first, then updates the existing references to them, and finally deletes the old resources.

{{% notes type="info" %}}

The exact format of auto-generated physical names varies by provider. While the general pattern is a logical name followed by a random suffix, individual providers may transform the logical name—for example, by removing hyphens or truncating it—to satisfy platform naming constraints. Consult the [Registry](/registry/) for provider-specific documentation.

{{% /notes %}}

For cases that require specific names, you can override auto-naming by specifying a physical name. Most resources have a `name` property that you can use to name the resource yourself. Specify your name in the argument object to the constructor. Here’s an example.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
let role = new aws.iam.Role("my-role", {
    name: "my-role-001",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
role = iam.Role('my-role', name='my-role-001')
```

{{% /choosable %}}
{{% choosable language go %}}

```go
role, err := iam.NewRole(ctx, "my-role", &iam.RoleArgs{
    Name: pulumi.String("my-role-001"),
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var role = new Aws.Iam.Role("my-role", new Aws.Iam.RoleArgs
{
    Name = "my-role-001",
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var role = new com.pulumi.aws.iam.Role("my-role",
    com.pulumi.aws.iam.RoleArgs.builder()
        .name("my-role-001")
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
    role:
        type: aws:iam:Role
        properties:
            name: my-role-001
```

{{% /choosable %}}

{{< /chooser >}}

If the `name` property is not available on a resource, consult the [Registry](/registry/) for the specific resource you are creating. Some resources use a different property to override auto-naming. For instance, the `aws.s3.Bucket` type uses the property `bucket` instead of name. Other resources, such as `aws.kms.Key`, do not have physical names and use other auto-generated IDs to uniquely identify them.

Overriding auto-naming makes your project susceptible to naming collisions. As a result, for resources that may need to be replaced, you should specify `deleteBeforeReplace: true` in the resource’s options. This option ensures that old resources are deleted before new ones are created, which will prevent those collisions.

Because physical and logical names do not need to match, you can construct the physical name by using your project and stack names. Similarly to auto-naming, this approach protects you from naming collisions while still having meaningful names. Note that `deleteBeforeReplace` is still necessary:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
let role = new aws.iam.Role("my-role", {
    name: `my-role-${pulumi.getProject()}-${pulumi.getStack()}`,
}, { deleteBeforeReplace: true });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
role = iam.Role(
    'my-role',
    name=f'my-role-{ pulumi.get_project() }-{ pulumi.get_stack() }',
    opts=ResourceOptions(delete_before_replace=True),
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
role, _ := iam.NewRole(ctx, "my-role", &iam.RoleArgs{
    Name: fmt.Sprintf("my-role-%s-%s", ctx.Project(), ctx.Stack()),
}, pulumi.DeleteBeforeReplace(true))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var role = new Aws.Iam.Role("my-role", new Aws.Iam.RoleArgs
    {
        Name = string.Format($"my-role-{Deployment.Instance.ProjectName}-{Deployment.Instance.StackName}"),
    },
    new CustomResourceOptions { DeleteBeforeReplace = true }
);
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var role = new com.pulumi.aws.iam.Role("my-role",
    com.pulumi.aws.iam.RoleArgs.builder()
        .name(String.format("my-role-%s-%s", ctx.projectName(), ctx.stackName()))
        .build(),
    CustomResourceOptions.builder()
        .deleteBeforeReplace(true)
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  role:
    type: aws:iam:Role
    properties:
      name: my-role${pulumi.project}-${pulumi.stack}
    options:
      deleteBeforeReplace: true
```

{{% /choosable %}}

{{< /chooser >}}

## Configuring Auto-Naming {#autonaming-configuration}

You can customize how Pulumi generates resource names through the `pulumi:autonaming` configuration setting. This can be set at the stack or project level. And by leveraging [Pulumi ESC](/docs/esc/), autonaming can be managed at the organization level.

{{% notes %}}
When configuring auto-naming in your project configuration (`Pulumi.yaml`), you need to wrap the configuration in a `value` key:

```yaml
config:
  pulumi:autonaming:
    value:
      pattern: ${name}-${project}-${stack}
```

However, when configuring it in a stack configuration file (`Pulumi.<stack-name>.yaml`), you can specify the configuration directly:

```yaml
config:
  pulumi:autonaming:
    pattern: ${name}-${project}-${stack}
```

And when configuring it in an [ESC environment](/docs/esc/guides/integrate-with-pulumi-iac/), you can specify the configuration as such:

```yaml
pulumiConfig:
  pulumi:autonaming:
    # Note the "$$".
    pattern: $${name}-$${project}-$${stack}
```

{{% /notes %}}

Here are the key ways to configure auto-naming:

### Default Auto-Naming

The default behavior adds a random suffix to resource names:

```yaml
config:
  pulumi:autonaming:
    mode: default
```

This is equivalent to having no configuration at all.

### Verbatim Names

To use the logical name exactly as specified, without any modifications:

```yaml
config:
  pulumi:autonaming:
    mode: verbatim
```

No random suffixes will be added to the resource names.

### Disable Auto-Naming

To require explicit names for all resources:

```yaml
config:
  pulumi:autonaming:
    mode: disabled
```

### Custom Naming Pattern

You can specify a template pattern for generating names:

```yaml
config:
  pulumi:autonaming:
    pattern: ${name}-${hex(8)}
```

The following expressions are supported in patterns:

| Expression | Description | Example |
| :---- | :---- | :---- |
| name | Logical resource name | ${name} |
| hex(n) | Hexadecimal random string of length n | ${name}-${hex(5)} |
| alphanum(n) | Alphanumeric random string of length n | ${name}${alphanum(4)} |
| string(n) | Random string of letters of length n | ${name}${string(6)} |
| num(n) | Random string of digits of length n | ${name}${num(4)} |
| uuid | UUID | ${uuid} |
| organization | Organization name | ${organization}_${name} |
| project | Project name | ${project}_${name} |
| stack | Stack name | ${stack}_${name} |
| config.key | Config value of key | ${config.region}_${name} |

{{% notes type="warning" %}}
When an update requires replacing the resource, Pulumi's default behavior is to create the new resource and then deleting the old resource. However, when using verbatim names or patterns without random components, resources that need to be replaced will be deleted before creating the new resource. This can lead to downtime.
{{% /notes %}}

### Provider-Specific Configuration

You can configure auto-naming differently for specific providers or resource types:

```yaml
config:
  pulumi:autonaming:
    mode: default
    providers:
      aws:
        pattern: ${name}_${hex(4)}  # AWS resources use underscore and shorter suffix
      azure-native:
        mode: verbatim  # Azure resources use exact names
        resources:
          azure-native:storage:Account:
            pattern: ${name}${string(6)}  # Storage accounts need unique names
```

### Strict Name Pattern Enforcement

By default, providers may modify the generated names to comply with resource-specific requirements. To prevent this and enforce your exact pattern:

```yaml
config:
  pulumi:autonaming:
    pattern: ${name}-${hex(8)}
    enforce: true
```

### Migration

Changing the autonaming setting on an existing stack doesn't cause any immediate changes. It will only affect any newly created resources on this stack, including resources being replaced for unrelated reasons. To re-create resources with new names, e.g. on a dev stack, you would need to destroy the stack and update it again.

## Resource Types {#types}

Each resource is an instance of a specific Pulumi resource type.  This type is specified by a type token in the format `<package>:<module>:<typename>`.  Concrete examples of this format are:

- `aws:s3/bucket:Bucket`
- `azure-native:compute:VirtualMachine`
- `kubernetes:apps/v1:Deployment`
- `random:index:RandomPassword`

The `<package>` component of the type (e.g. `aws`, `azure-native`, `kubernetes`, `random`) specifies which [Pulumi Package](/docs/using-pulumi/pulumi-packages/) defines the resource.  This is mapped to the package in the [Pulumi Registry](/registry/) and to the underlying [Resource Provider](/docs/concepts/resources/providers/).

The `<module>` component of the type (e.g. `s3/bucket`, `compute`, `apps/v1`, `index`) is the module path where the resource lives within the package.  It is `/` delimited by component of the path.  Per-language Pulumi SDKs use the module path to emit nested namespaces/modules in a language-specific way to organize all the types defined in a package.  For example, the `Deployment` resource above is available at `kubernetes.apps.v1.Deployment` in TypeScript and in the `github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/apps/v1` module in Go.  For historical reasons only, some packages include the type name itself as a final component of the module (e.g. `s3/bucket` for the type name `Bucket`) - in this case, this component is not included in the SDK namespace.  The name `index` indicates that the resource is not nested, and is instead available at the top level of the package.  For example, the `RandomPassword` resource above is available at `random.RandomPassword` in TypeScript.

The `<typename>` component of the type (e.g. `Bucket`, `VirtualMachine`, `Deployment`, `RandomPassword`) is the identifier used to refer to the resource itself.  It is mapped to the class or constructor name in the per-language Pulumi SDK.

Note that because of some of the historical details of how `<module>` is defined, a "simplified" resource type name is accepted or presented in certain places, and mapped into the "full" resource type name specified above.  The simplified resource type name applies the following rules:

1. If the type token is two components instead of three, that is `<package>:<typename>`, it is interpreted as if it was `<package>:index:<typename>`.
2. The repetition of the `<typename>` as part of the module definition is not required, and will be inferred if necessary - that is `aws:s3:Bucket` will be interpreted as referring to `aws:s3/bucket:Bucket`.

This "simplified" type name format is currently used in the following places:

- The [Pulumi YAML](/docs/languages-sdks/yaml/) language allows simple type names to be used as the `type` of a resource.

The examples above can be written in simplified form as:

- `aws:s3:Bucket`
- `azure-native:compute:VirtualMachine`
- `kubernetes:apps/v1:Deployment`
- `random:RandomPassword`

## Resource URNs {#urns}

Each resource is assigned a [Uniform Resource Name (URN)](https://en.wikipedia.org/wiki/Uniform_Resource_Name) that uniquely identifies that resource globally. Unless you are writing a tool, you will seldom need to interact with an URN directly, but it is fundamental to how Pulumi works so it’s good to have a general understanding of it.

The URN is automatically constructed from the project name, stack name, resource name, resource type, and the types of all the parent resources (in the case of [component resources](/docs/concepts/resources/components/)).

The following is an example of a URN:

```text
urn:pulumi:production::acmecorp-website::custom:resources:Resource$aws:s3/bucket:Bucket::my-bucket
           ^^^^^^^^^^  ^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^
           <stack-name> <project-name>   <parent-type>             <resource-type>       <resource-name>
```

The type components of the URN are [resource types](#types) as defined above, and the full type in the URN is a `$` delimited path of the parent chain of resource types that the resource is nested within (up to and excluding the root Stack resource).

The URN must be globally unique. This means all of the components that go into a URN must be unique within your program. If you create two resources with the same name, type, and parent path, for instance, you will see an error:

```bash
error: Duplicate resource URN 'urn:pulumi:production::acmecorp-website::custom:resources:Resource$aws:s3/bucket:Bucket::my-bucket'; try giving it a unique name
```

Any change to the URN of a resource causes the old and new resources to be treated as unrelated—the new one will be created (since it was not in the prior state) and the old one will be deleted (since it is not in the new desired state). This behavior happens when you change the `name` used to construct the resource or the structure of a resource’s parent hierarchy.

Both of these operations will lead to a different URN, and thus require the `create` and `delete` operations instead of an `update` or `replace` operation that you would use for an existing resource.

Resources constructed as children of a component resource must include the component resource's name as part of their names (e.g., as a prefix). This ensures uniqueness across multiple instances of the component resource and ensures that if the component is renamed, the child resources are renamed as well.

## Physical IDs {#physicalid}

In addition to its logical name, physical name, and URN, every resource that Pulumi creates in a cloud provider is assigned a **physical ID** by that provider once creation is complete. This ID is exposed as the `id` output property on every resource.

Unlike the logical name (which you choose) or the URN (which Pulumi derives), the physical ID is assigned by the provider and is specific to that provider's conventions:

- AWS resources use short identifiers such as bucket names (`my-bucket-d7c3a1f`) or resource-specific IDs (`vpc-0abc1234def5678`, `i-0abc1234def5678`). The ARN is typically a separate `arn` output property, not the `id`.
- Azure resources use long ARM IDs (`/subscriptions/<sub>/resourceGroups/<rg>/providers/...`).
- GCP resources use self-link URLs (`https://www.googleapis.com/compute/v1/projects/...`).
- Generic resources often use simple strings or numeric IDs.

Because `id` is an output, it is wrapped in Pulumi's `Output<T>` type and is not known until the resource has been created or updated. You access it just like any other output — by passing it directly to another resource's input or by using `.apply()` when you need to transform the value in code.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("my-bucket");

// bucket.id is an Output<string> — the AWS-assigned bucket name.
const obj = new aws.s3.BucketObject("hello.txt", {
    bucket: bucket.id,   // Pass Output<string> directly — no .apply() needed.
    content: "Hello, Pulumi!",
    key: "hello.txt",
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws

bucket = aws.s3.Bucket("my-bucket")

# bucket.id is an Output[str] — the AWS-assigned bucket name.
obj = aws.s3.BucketObject(
    "hello.txt",
    bucket=bucket.id,   # Pass Output[str] directly — no apply() needed.
    content="Hello, Pulumi!",
    key="hello.txt",
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
bucket, err := s3.NewBucket(ctx, "my-bucket", nil)
if err != nil {
    return err
}

// bucket.ID() returns pulumi.IDOutput — the AWS-assigned bucket name.
_, err = s3.NewBucketObject(ctx, "hello.txt", &s3.BucketObjectArgs{
    Bucket:  bucket.ID(), // Pass IDOutput directly.
    Content: pulumi.String("Hello, Pulumi!"),
    Key:     pulumi.String("hello.txt"),
})
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var bucket = new Aws.S3.Bucket("my-bucket");

// bucket.Id is an Output<string> — the AWS-assigned bucket name.
var obj = new Aws.S3.BucketObject("hello.txt", new()
{
    BucketName = bucket.Id,  // Pass Output<string> directly.
    Content = "Hello, Pulumi!",
    Key = "hello.txt",
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
var bucket = new Bucket("my-bucket");

// bucket.id() returns Output<String> — the AWS-assigned bucket name.
var obj = new BucketObject("hello.txt", BucketObjectArgs.builder()
    .bucket(bucket.id())   // Pass Output<String> directly.
    .content("Hello, Pulumi!")
    .key("hello.txt")
    .build());
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  my-bucket:
    type: aws:s3:Bucket
  hello-txt:
    type: aws:s3:BucketObject
    properties:
      bucket: ${my-bucket.id}
      content: "Hello, Pulumi!"
      key: hello.txt
```

{{% /choosable %}}

{{< /chooser >}}

The physical ID is particularly important when you want to adopt an existing cloud resource into a Pulumi stack. The [`import` resource option](/docs/iac/concepts/resources/options/import/) and the `get` static method both accept a physical ID to look up the resource's current state in the provider.

```python
# Import an existing S3 bucket by its provider-assigned ID.
existing = aws.s3.Bucket.get("existing-bucket", id="my-bucket-name-abc123")
```

See [Importing resources](/docs/iac/adopting-pulumi/import/) for a full discussion of adoption workflows.

## Resource identity summary {#identity-summary}

Pulumi uses four distinct forms of resource identity, each suited to a different purpose. Understanding which form to use in a given context prevents the most common type-mismatch errors.

| Identity form | Where it comes from | Typical value | When to use it |
|---|---|---|---|
| **Logical name** | Your code — the first constructor argument | `"my-bucket"` | Passed to the resource constructor. Drives the URN and often the physical name prefix. |
| **Physical name** | Provider, influenced by your logical name and auto-naming | `"my-bucket-d7c3a1f"` | Used in provider API calls. Read back via provider-specific output properties (e.g., `bucket`, `name`). |
| **Physical ID** | Provider — returned after the resource is created | `"my-bucket-d7c3a1f"` (S3), `"vpc-0abc1234def5678"` (VPC), `"/subscriptions/.../resourceGroups/..."` (Azure) | Pass to `import`, `get`, and provider APIs that accept a resource reference by ID. Access via `resource.id`. |
| **URN** | Pulumi — derived from project, stack, type, and logical name | `"urn:pulumi:dev::app::aws:s3/bucket:Bucket::my-bucket"` | Pulumi CLI commands (`pulumi state`, `pulumi import`). Rarely used in program code. Access via `resource.urn`. |
| **Resource reference** | Your program — the variable holding the resource object | `bucket` (the Python/TS/Go variable) | Pass to [`ResourceOptions`](/docs/iac/concepts/resources/options/) fields (`parent`, `depends_on`, `provider`, `deleted_with`). Never pass a URN or ID here. |

The most frequent source of confusion is the distinction between the physical ID (`resource.id`) and the URN (`resource.urn`). The physical ID is what cloud provider APIs and the Pulumi import system expect. The URN is Pulumi-internal and is almost never needed in application code.

{{% notes type="info" %}}
The `dependsOn` option accepts a list of **resource references** (the variable itself), not URNs or IDs. In Python the field is `depends_on` — pass `depends_on=[bucket]`, not `depends_on=[bucket.urn]`.
{{% /notes %}}
