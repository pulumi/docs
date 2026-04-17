---
title_tag: "Resource Identity in Python | Languages & SDKs"
meta_desc: How to work with resource identity in Python — logical names, physical IDs, URNs, and resource references — with common pitfalls and troubleshooting guidance.
title: Resource identity
h1: Resource identity in Python
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Resource identity
        parent: iac-languages-python
        weight: 4
    languages:
        parent: python
        weight: 6
aliases:
- /docs/languages-sdks/python/resource-identity/
---

Pulumi resources carry [four distinct forms of identity](/docs/iac/concepts/resources/names/#identity-summary): a logical name, a physical name, a physical ID, and a URN. Each form serves a different purpose, and passing the wrong one to an argument is the most common source of type-mismatch errors in Python Pulumi programs. This page explains how each form works in Python and how to diagnose problems when something looks wrong.

## How resource identity maps to Python

The first positional argument you pass to a resource constructor is the **logical name** — Pulumi uses it for state tracking, URN generation, and as the prefix for the auto-generated physical name. After the resource is created, you can access the remaining identity forms as output properties:

```python
# Physical ID: the AWS-assigned VPC ID (e.g., "vpc-0abc123def456789").
# This is an Output[str], not a plain string.
vpc_id: pulumi.Output[str] = vpc.id

# URN: Pulumi-internal identifier.
# Format: urn:pulumi:<stack>::<project>::<type>::<logical-name>
vpc_urn: pulumi.Output[str] = vpc.urn
```

Both `id` and `urn` are `Output[str]` values — they are not available as plain strings at program definition time because the cloud provider does not assign them until the resource is actually created or updated.

## Passing identity to other resources

The most common operations — wiring resources together and setting options — each expect a specific form of identity.

### Physical ID: wiring resource inputs

When one resource needs to reference another resource (for example, placing a subnet inside a VPC), pass the upstream resource's **`id` output** to the downstream resource's input:

```python
subnet = aws.ec2.Subnet(
    "main-subnet",
    vpc_id=vpc.id,          # Output[str] — the VPC's AWS-assigned ID
    cidr_block="10.0.1.0/24",
    availability_zone="us-east-1a",
)
```

Pulumi automatically resolves `Output[str]` values and establishes the correct creation order between the two resources. You do not need to call `.apply()` for simple pass-through cases like this.

### Resource references: ResourceOptions fields

Fields in [`ResourceOptions`](/docs/iac/concepts/resources/options/) — `parent`, `depends_on`, `provider`, `deleted_with` — accept the **resource object itself**, not a URN or ID:

```python
# CORRECT: pass the resource variable to parent and depends_on.
subnet = aws.ec2.Subnet(
    "main-subnet",
    vpc_id=vpc.id,
    cidr_block="10.0.1.0/24",
    opts=pulumi.ResourceOptions(
        parent=vpc,         # Resource object — NOT vpc.urn, NOT vpc.id
        depends_on=[vpc],   # List of resource objects — NOT [vpc.urn]
    ),
)
```

```python
# INCORRECT — a common mistake.
subnet = aws.ec2.Subnet(
    "main-subnet",
    vpc_id=vpc.id,
    cidr_block="10.0.1.0/24",
    opts=pulumi.ResourceOptions(
        parent=vpc.urn,     # Wrong — urn is a string output, not a resource
        depends_on=[vpc.id], # Wrong — id is a string output, not a resource
    ),
)
```

### Importing existing resources

To adopt an existing cloud resource into your Pulumi stack, use the `import` resource option with the resource's **physical ID**:

```python
# The id= argument is the provider-assigned ID, not the Pulumi URN.
existing_bucket = aws.s3.Bucket(
    "existing-bucket",
    opts=pulumi.ResourceOptions(import_="my-bucket-name-abc123"),
)
```

The static `.get()` method on a resource class also takes a physical ID:

```python
# Look up an existing resource by its provider-assigned ID.
existing_vpc = aws.ec2.Vpc.get("imported-vpc", id="vpc-0abc123def456789")
```

For a complete walk-through of the import workflow, see [Importing resources](/docs/iac/adopting-pulumi/import/).

## Common type-mismatch errors

### Passing a URN where a physical ID is expected

```python
# WRONG: vpc.urn is Pulumi's internal URN, not the AWS VPC ID.
subnet = aws.ec2.Subnet("main-subnet", vpc_id=vpc.urn, ...)

# RIGHT: use vpc.id, which holds the AWS-assigned VPC ID.
subnet = aws.ec2.Subnet("main-subnet", vpc_id=vpc.id, ...)
```

The URN looks like `urn:pulumi:dev::app::aws:ec2/vpc:Vpc::main-vpc`. Cloud provider APIs never accept a URN — they accept provider-specific IDs such as `vpc-0abc123def456789`.

### Passing a plain string where an Output is needed

If you hard-code a resource ID that you retrieved out-of-band (e.g., from the Pulumi CLI or the cloud console), wrap it in `pulumi.Output.from_input` or just pass the string directly. Pulumi accepts both plain strings and `Output[str]` for inputs:

```python
# Both of these are valid:
subnet = aws.ec2.Subnet("main-subnet", vpc_id="vpc-0abc123def456789", ...)
subnet = aws.ec2.Subnet("main-subnet", vpc_id=pulumi.Output.from_input("vpc-0abc123def456789"), ...)
```

However, passing a plain string for `parent` or `depends_on` in `ResourceOptions` is not valid — those fields require resource objects.

### Confusing the logical name with the physical name

The logical name you pass to the constructor is **not** the same as the physical name the resource gets in the cloud. Pulumi appends a random suffix to the logical name to generate the physical name (unless you override it). Do not rely on the logical name to equal the cloud resource name.

```python
# Logical name: "my-function"
# Physical name (auto-named): "my-function-3a8b7f2" (random suffix added by Pulumi)
fn = aws.lambda_.Function("my-function", ...)

# If you need the actual Lambda function name as known to AWS, use fn.name:
pulumi.export("function_name", fn.name)  # Output[str] — the physical name
```

### Using .apply() unnecessarily for pass-through IDs

A common over-use of `.apply()` is extracting an ID just to pass it directly to another resource:

```python
# UNNECESSARY — Pulumi accepts Output[str] directly.
subnet = aws.ec2.Subnet(
    "main-subnet",
    vpc_id=vpc.id.apply(lambda value: value),  # No-op apply
    ...
)

# CORRECT — pass Output[str] directly.
subnet = aws.ec2.Subnet("main-subnet", vpc_id=vpc.id, ...)
```

Reserve `.apply()` for cases where you need to transform the value or embed it in a string. Passing a resource ID directly never requires `.apply()`.

## Debugging state mismatches

### Checking what Pulumi has recorded for a resource

After a deploy, you can inspect a resource's recorded URN and ID using `pulumi stack`:

```bash
pulumi stack --show-urns
```

Or query the state file directly:

```bash
pulumi stack export | python3 -c "import sys,json; [print(r['urn'], r.get('id','')) for r in json.load(sys.stdin)['deployment']['resources']]"
```

### A resource is being replaced unexpectedly

If Pulumi creates a new resource and deletes the old one when you expected an in-place update, the most common cause is that the logical name, parent, or type changed — any of which changes the URN and forces a replacement. Check whether you unintentionally:

- Changed the first constructor argument (logical name).
- Moved the resource inside or outside a component.
- Changed the resource type.

Use [`aliases`](/docs/iac/concepts/resources/options/aliases/) to preserve the old URN when you need to refactor without replacing resources.

### `get()` returns stale state

The `.get()` static method reads the resource's current state from the cloud provider, not from the Pulumi state file. If the Pulumi state file and the provider are out of sync, use `pulumi refresh` to reconcile them before calling `.get()`.

### `import` fails with "resource already exists"

When using `import` via `ResourceOptions(import_=...)`, if Pulumi says the resource already exists in the stack, you may already have a resource with the same logical name in state. Check `pulumi stack` to see if the resource is already tracked. If it is, remove the `import_` option — the resource is already managed.

## Quick reference: identity in Python

| What you need | Where to get it | Python expression |
|---|---|---|
| Logical name | Your code | The first argument you passed: `"main-vpc"` |
| Physical name | Provider output | `resource.name` (resource-specific; not all resources expose this) |
| Physical ID | Provider output | `resource.id` — always an `Output[str]` |
| URN | Pulumi output | `resource.urn` — always an `Output[str]` |
| Resource reference | Your program variable | `resource` (the variable itself) |

For the full conceptual explanation of these four identity forms and a cross-language reference table, see [Resource names and identity](/docs/iac/concepts/resources/names/).
