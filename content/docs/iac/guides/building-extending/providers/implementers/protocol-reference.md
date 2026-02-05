---
title_tag: "Provider protocol reference"
meta_desc: "Complete reference for the Pulumi provider gRPC protocol, including all RPC methods and their semantics."
title: Provider protocol reference
h1: Provider protocol reference
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Protocol reference
        parent: iac-guides-provider-implementers
        weight: 10
---

This document describes the gRPC protocol that all Pulumi providers implement. Understanding this protocol is essential for [implementing providers directly](/docs/iac/guides/building-extending/providers/provider-architecture/#layer-2-generated-language-bindings) without a higher-level SDK.

The complete protocol definition is in [`provider.proto`](https://github.com/pulumi/pulumi/blob/master/proto/pulumi/provider.proto). Additional protocol documentation is available at [pulumi-developer-docs.readthedocs.io](https://pulumi-developer-docs.readthedocs.io/latest/proto/README.html).

## Overview

Pulumi providers are gRPC servers. When a Pulumi program runs, the engine starts provider processes and communicates with them over gRPC. The provider implements the `ResourceProvider` service, which defines methods for managing resources throughout their lifecycle.

### How it works

The Pulumi engine starts your provider as a subprocess and connects to it via gRPC. It then calls `Configure` with credentials and settings to initialize the provider. For each resource operation, the engine calls the appropriate method such as `Check`, `Diff`, or `Create`. Your provider executes the operation and returns results, while the engine manages state and orchestrates the overall deployment.

## Essential methods

These methods are required for a functional provider:

### GetSchema

Returns the provider's schema, which defines all resources, their properties, and configuration options.

```protobuf
rpc GetSchema(GetSchemaRequest) returns (GetSchemaResponse)
```

**Request fields:**

- `version` (int32): Schema version to retrieve (use 0 for current)
- `subpackage_name` (string): Optional subpackage name
- `subpackage_version` (string): Optional subpackage version

**Response fields:**

- `schema` (string): JSON-encoded [package schema](/docs/iac/guides/building-extending/packages/schema/)

The schema is critical—it tells Pulumi what resources your provider offers, what inputs they accept, and what outputs they produce. Without a valid schema, Pulumi cannot generate SDKs or validate programs.

### Configure

Initializes the provider with configuration values like credentials and region settings.

```protobuf
rpc Configure(ConfigureRequest) returns (ConfigureResponse)
```

**Request fields:**

- `variables` (map<string, string>): Environment variables
- `args` (Struct): Configuration values from the Pulumi program
- `acceptSecrets` (bool): Whether the provider can accept secret values
- `acceptResources` (bool): Whether the provider can accept resource references

**Response fields:**

- `acceptSecrets` (bool): Confirm secret handling capability
- `supportsPreview` (bool): Whether the provider handles preview operations correctly
- `acceptResources` (bool): Confirm resource reference capability
- `acceptOutputs` (bool): Whether the provider can accept output values

Store configuration values for use in subsequent resource operations. Most providers use this to set up API clients with the provided credentials.

### Check

Validates resource inputs and optionally sets defaults.

```protobuf
rpc Check(CheckRequest) returns (CheckResponse)
```

**Request fields:**

- `urn` (string): The resource's uniform resource name
- `olds` (Struct): Previous input values (if updating)
- `news` (Struct): New input values to validate
- `randomSeed` (bytes): Seed for deterministic random generation

**Response fields:**

- `inputs` (Struct): Validated/transformed inputs
- `failures` (repeated CheckFailure): Validation errors

Check is called before any create or update operation. Use it to validate that inputs are well-formed, set default values for optional properties, normalize inputs such as lowercasing strings, and return detailed error messages for invalid inputs.

Return the (potentially modified) inputs in the response. These become the inputs for subsequent `Diff`, `Create`, and `Update` calls.

### Diff

Computes what changes are needed between current state and desired inputs.

```protobuf
rpc Diff(DiffRequest) returns (DiffResponse)
```

**Request fields:**

- `id` (string): The resource's ID
- `urn` (string): The resource's URN
- `olds` (Struct): Current state
- `news` (Struct): Desired inputs
- `ignoreChanges` (repeated string): Properties to ignore
- `oldInputs` (Struct): Previous inputs

**Response fields:**

- `replaces` (repeated string): Properties requiring replacement
- `stables` (repeated string): Properties guaranteed unchanged
- `deleteBeforeReplace` (bool): Whether to delete before creating replacement
- `changes` (DiffChanges): Whether any changes exist
- `diffs` (repeated string): Changed property names
- `detailedDiff` (map<string, PropertyDiff>): Detailed per-property changes
- `hasDetailedDiff` (bool): Whether detailedDiff is populated

The diff response tells Pulumi whether any changes are needed via the `changes` field, which specific properties changed via `diffs` and `detailedDiff`, whether changes require resource replacement via `replaces`, and whether to delete before replace or create before delete via `deleteBeforeReplace`.

**Detailed diff format**:

```protobuf
message PropertyDiff {
    Kind kind = 1;      // ADD, ADD_REPLACE, DELETE, DELETE_REPLACE, UPDATE, UPDATE_REPLACE
    bool inputDiff = 2; // Whether this is an input diff vs output diff
}
```

### Create

Provisions a new resource.

```protobuf
rpc Create(CreateRequest) returns (CreateResponse)
```

**Request fields:**

- `urn` (string): The resource's URN
- `type` (string): The resource type token (e.g., `myfiles:index:File`)
- `name` (string): The resource's logical name
- `properties` (Struct): Input properties (from Check)
- `timeout` (double): Operation timeout in seconds
- `preview` (bool): Whether this is a preview operation

**Response fields:**

- `id` (string): The created resource's unique identifier
- `properties` (Struct): Output properties (state)

The `id` must uniquely identify the resource for subsequent Read, Update, and Delete calls. When `preview` is true, don't actually create anything—return expected outputs instead. Return all output properties, not just inputs, and handle errors gracefully with meaningful error messages.

### Read

Fetches the current state of an existing resource.

```protobuf
rpc Read(ReadRequest) returns (ReadResponse)
```

**Request fields:**

- `id` (string): The resource's ID
- `urn` (string): The resource's URN
- `type` (string): The resource type token
- `name` (string): The resource's logical name
- `properties` (Struct): Last known state
- `inputs` (Struct): Last known inputs

**Response fields:**

- `id` (string): The resource's ID (may change if resource was replaced externally)
- `properties` (Struct): Current state
- `inputs` (Struct): Current inputs that would produce this state

Read is called during `pulumi refresh` and `pulumi import`. It should query the external system for current state, return an empty response if the resource no longer exists, and compute what inputs would produce the current state.

### Update

Modifies an existing resource.

```protobuf
rpc Update(UpdateRequest) returns (UpdateResponse)
```

**Request fields:**

- `id` (string): The resource's ID
- `urn` (string): The resource's URN
- `type` (string): The resource type token
- `name` (string): The resource's logical name
- `olds` (Struct): Current state
- `news` (Struct): New desired inputs
- `timeout` (double): Operation timeout in seconds
- `ignoreChanges` (repeated string): Properties to ignore
- `preview` (bool): Whether this is a preview operation
- `oldInputs` (Struct): Previous inputs

**Response fields:**

- `properties` (Struct): New state after update

Update is called when Diff indicates changes that don't require replacement. Apply the changes and return the new state.

### Delete

Removes a resource.

```protobuf
rpc Delete(DeleteRequest) returns (google.protobuf.Empty)
```

**Request fields:**

- `id` (string): The resource's ID
- `urn` (string): The resource's URN
- `type` (string): The resource type token
- `name` (string): The resource's logical name
- `properties` (Struct): Current state
- `timeout` (double): Operation timeout in seconds

Delete should be idempotent—if the resource is already gone, succeed silently.

### GetPluginInfo

Returns metadata about the provider plugin.

```protobuf
rpc GetPluginInfo(google.protobuf.Empty) returns (PluginInfo)
```

**Response fields:**

- `version` (string): Provider version (e.g., "1.2.3")

## Additional methods

These methods are optional but enable advanced functionality:

### Invoke

Calls a provider function (not a resource operation).

```protobuf
rpc Invoke(InvokeRequest) returns (InvokeResponse)
```

Use this for data sources and utility functions that don't create resources.

### Construct

Creates a component resource (a resource composed of other resources).

```protobuf
rpc Construct(ConstructRequest) returns (ConstructResponse)
```

Component resources are implemented in the provider but create child resources. This is advanced functionality.

### CheckConfig / DiffConfig

Validate and diff provider configuration itself (not resource configuration).

```protobuf
rpc CheckConfig(CheckRequest) returns (CheckResponse)
rpc DiffConfig(DiffRequest) returns (DiffResponse)
```

### Cancel

Signals that the current operation should be canceled.

```protobuf
rpc Cancel(google.protobuf.Empty) returns (google.protobuf.Empty)
```

Providers should attempt to cancel in-progress operations when this is called.

## Data types

### Property values

Properties use a structured format that supports primitives like strings, numbers, and booleans, complex types like arrays and objects, and special values including secrets, resource references, and unknowns.

Unknown values appear during preview when a value depends on a resource that hasn't been created yet. Your Check and Diff implementations must handle unknowns gracefully.

### Secrets

Secret values are marked specially in the protocol. When `acceptSecrets` is true in Configure, you may receive secret-wrapped values. Preserve the secret wrapper in outputs to maintain secret propagation.

### Resource references

When `acceptResources` is true, you may receive references to other resources instead of their resolved values. This enables tracking dependencies.

## Error handling

Return gRPC errors with appropriate status codes:

- `INVALID_ARGUMENT`: Invalid inputs (prefer CheckFailure in Check)
- `NOT_FOUND`: Resource doesn't exist
- `ALREADY_EXISTS`: Resource already exists
- `FAILED_PRECONDITION`: Operation prerequisites not met
- `INTERNAL`: Unexpected provider error

Include descriptive error messages—they're shown directly to users.

## Implementation checklist

A minimal provider needs:

1. [ ] `GetPluginInfo` returning your version
1. [ ] `GetSchema` returning valid JSON schema
1. [ ] `Configure` storing credentials/settings
1. [ ] `Check` validating inputs
1. [ ] `Diff` computing changes
1. [ ] `Create` provisioning resources
1. [ ] `Read` fetching current state
1. [ ] `Update` modifying resources
1. [ ] `Delete` removing resources

## Example: Method call sequence

For a typical `pulumi up` creating a new resource:

1. `GetPluginInfo` → Engine gets provider version
1. `Configure` → Provider receives credentials
1. `GetSchema` → Engine gets resource definitions
1. `Check` → Validate and default inputs
1. `Diff` → Compute changes (none, since new)
1. `Create` → Provision the resource

For updating an existing resource:

1. `Check` → Validate new inputs
1. `Diff` → Compute what changed
1. `Update` or `Delete`+`Create` → Apply changes

## Next steps

For language-specific implementation guides, see [Direct implementation in Python](/docs/iac/guides/building-extending/providers/implementers/python/) or [Direct implementation in Go](/docs/iac/guides/building-extending/providers/implementers/go/). For schema details, see the [Schema reference](/docs/iac/guides/building-extending/packages/schema/). You can also [view the complete proto file](https://github.com/pulumi/pulumi/blob/master/proto/pulumi/provider.proto) on GitHub.
