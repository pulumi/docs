---
title: Pulumi YAML Reference
linktitle: Pulumi YAML Reference
meta_desc: Specification for the Pulumi YAML format and built-in functions
---

Pulumi programs can be defined in many languages, and the Pulumi YAML dialect offers an additional language for authoring Pulumi programs.

The Pulumi YAML provider supports programs written in YAML or JSON.  In both cases, the programs (`.yaml` or `.json` files) follow a simple schema, including four top level sections:

| Property        | Type | Required           | Expression  | Description |
| ------------- |---|-------------| -----|---|
| `configuration`      | map[string]Configuration | No | No | Configuration specifies the [Pulumi config]({{< relref "/docs/intro/concepts/config" >}}) inputs to the deployment. |
| `resources`      | map[string]Resource | No | No | Resources declares the [Pulumi resources]({{< relref "/docs/intro/concepts/resources/" >}}) that will be deployed and managed by the program |
| `variables`      | map[string]Expression | No | Yes | Variables specifies intermediate values of the program, the values of variables are expressions that can be re-used. |
| `outputs`      | map[string]Expression | No | Yes | Outputs specifies the [Pulumi stack outputs]({{< relref "/docs/intro/concepts/stack#outputs" >}}) of the program and how they are computed from the `resources` is a value of the appropriate type for the template to use if no value is specified. |

In many locations within this schema, values may be expressions which computed a value based on the `configuration`, `variables`, or outputs of `resources`.  These expressions can be provided in two ways:

* If an object is provided as a value, and has a key that has the prefix `Fn::`, the object is treated as an expression, and the expression will be resolved to a new value that will be used in place of the object.
* Any string value is interpreted as an interpolation, with `${...}` being replaced by evaluating the expression in the `...`.

The supported expression forms for each of these is detailed below.

### Configuration

The value of `configuration` is an object whose keys are logical names by which the config input will be referenced in expressions within the program, and whose values are elements of the schema below.  Each item in this object represents an independent config input. Either `type` or `default` is required.

| Property        | Type | Required           | Expression  | Description |
| ------------- |---|-------------| -----|---|
| `type`      | string | No | No | Type is the (required) data type for the parameter. It can be one of: `String`, `Number`, `List<Number>`, or `List<String>`. |
| `default`      | any | No | No | Default is a value of the appropriate type for the template to use if no value is specified. |

### Resources

The value of `resources` is an object whose keys are logical resource names by which the resource will be referenced in expressions within the program, and whose values which are elements of the schema below.  Each item in this object represents a resource which will be managed by the Pulumi program.

| Property        | Type | Required           | Expressions  | Description |
| ------------- |---|-------------| -----|---|
| `type`      | string | Yes | No | Type is the Pulumi type token for this resource. |
| `properties`      | map[string]Expression | No | Yes | Properties contains the primary resource-specific keys and values to initialize the resource state. |
| `options`         | [Resource Options](#resource-options) | No | No | Options contains all resource options supported by Pulumi. |

#### Resource Options

The value of the `options` property of a Resource is an object whose keys are [resource option names]({{< relref "/docs/intro/concepts/resources/options/" >}}) and whose values are elements of the schema below. No resource options are required.

The `dependsOn`, `parent`, `provider`, and `providers` values permit expressions which must use interpolation syntax to reference resources by name. For example:

```yaml
    options:
      provider: ${myEksProvider}
      providers:
        aws: ${myAwsProvider}
      dependsOn:
        - ${otherResource}
      parent: ${someParentResource}
```

| Property                  | Type         | Description |
| ------------------------- |--------------|-------------|
| `additionalSecretOutputs` | string[]     | AdditionalSecretOutputs specifies properties that must be encrypted as secrets |
| `aliases`                 | string[]     | Aliases specifies names that this resource used to have, so that renaming or refactoring doesn’t replace it |
| `customTimeouts`          | [Custom Timeout](#custom-timeout) | CustomTimeouts overrides the default retry/timeout behavior for resource provisioning |
| `deleteBeforeReplace`     | bool         | DeleteBeforeReplace  overrides the default create-before-delete behavior when replacing |
| `dependsOn`               | Expression[] | No | Yes | DependsOn makes this resource explicitly depend on another resource, by name, so that it won't be created before the dependent finishes being created (and the reverse for destruction). Normally, Pulumi automatically tracks implicit dependencies through inputs/outputs, but this can be used when dependencies aren't captured purely from input/output edges.|
| `ignoreChanges`           | string[]     | IgnoreChanges declares that changes to certain properties should be ignored during diffing |
| `import`                  | string       | Import adopts an existing resource from your cloud account under the control of Pulumi |
| `parent`                  | Expression   | No | Yes | Parent specifies a parent for the resource |
| `protect`                 | bool         | Protect prevents accidental deletion of a resource |
| `provider`                | Expression   | No | Yes | Provider specifies an explicitly configured provider, instead of using the default global provider |
| `providers`               | map[string]Expression | No | Yes | Map of providers for a resource and its children. |
| `version`                 | string       | Version specifies a provider plugin version that should be used when operating on a resource |

#### Custom Timeout

The optional `customTimeouts` property of a resource is an object of the following schema:

| Property        | Type | Required           | Expression  | Description |
| ------------- |---|-------------| -----|---|
| `create`      | string | No | No | Create is the custom timeout for create operations. |
| `delete`      | string | No | No | Delete is the custom timeout for delete operations. |
| `update`      | string | No | No | Update is the custom timeout for update operations. |

### Providers and provider versions

There are at least two reasons to explicitly define providers in YAML, or explicitly set their versions while creating resources.

1. Using explicit versions enables pinning the dependencies used, a technique used to improve build reliability.
1. Using explicit providers enables controlling the options for providers used by each resource, as described in [Unlock Programmatic Control by Disabling Default Providers]({{< relref "/blog/disable-default-providers/index" >}}).

#### Resource version

To create a resource with a specific provider version use the `version` option as described in [Resource Options](#resource-options):

```yaml
resources:
  something:
    type: aws:s3:Bucket
    properties:
      ...
    options:
      version: 5.6.0
```

#### Explicit provider

To create an explicit provider instance, preferably with a specific version, use the [`resources`](#resources) section and prefix the name of the provider with `pulumi:providers` which will the value of the `type` property.

```yaml
provider:
    type: pulumi:providers:azure
    options:
      version: 5.1.0
```

The provider instance can than be used as described in section [Resource Options](#resource-options) by setting the `provider` option:

```yaml
resources:
  provider:
    type: pulumi:providers:azure
    options:
      version: 5.1.0
  rg:
    type: azure:core:ResourceGroup
    properties:
      location: WestEurope
    options:
      provider: ${provider}
```

### Outputs

The value of `outputs` is an object whose keys are the logical names of the outputs that are available from outside the Pulumi stack (via `pulumi stack output`), and whose values are potentially computed expressions the resolve to the values of the desired outputs.

### Expressions

Expressions can be used in several contexts:

* the properties of `properties` of `resources`
* the properties of `options` of `resources` that take references to other resources: `parent`, `dependsOn`, `provider`, and `providers`
* the values of `variables` and `outputs`
* some or all values provided to built-in functions, as specified below

Generally speaking, most values permit an expression and exceptions will be documented as not permitting an expression, as above.

In these contexts, any JSON/YAML value may be provided.  If that value is a string, it is interpolated.  If that value is an object, and the object has a key with a prefix of `Fn::`, it is evaluated as an expression.

#### Interpolation

In expression locations, strings are evaluated as interpolations and any nested `${...}` expressions within the string value are replaced by the value of the expression `...`.  The syntax of expressions within interpolations permits [property access](#property-access) only.

To use `${}` in a string literal, escape `$` with `$$` like so:

```yaml
variables:
  plainString: $${value}
```

A string like `Hello, ${foo}` will convert the expression `foo` to a string.

If a string contains only an `${...}` expression, it's considered a [substitution](#substitution).

#### Property Access

Within an expression denoted by `${...}` property access is permitted according to the forms below. Config, variables, and resource keys all exist in a single namespace, and in the examples, `root` or equivalent must be the name of one of these items, and it must be valid to access the `foo` property of that item if it's a map or object, or if it's an array, the index must be valid.

* `${root}`
* `${root.foo}`
* `${root["foo"]}`
* `${root.bar.quux}`
* `${root["bar"].quux}`
* `${root["bar"]["quux"]}`
* `${root[0]}`
* `${root[100]}`
* `${root[0].foo}`
* `${root[0][1].foo}`
* `${root.foo.items[0].bar[1]}`
* `${root["key with \"escaped\" quotes"]}`
* `${root["key with a ."]}`
* `${["root key with \"escaped\" quotes"].foo}`
* `${["root key with a ."][100]}`

We have not discussed types until now, but implicitly every expression has a type, such as number, string, map, array, or even resource. When interpolated, these values must become strings, otherwise they are substituted in. Additionally:

* maps must have string keys and expression values
* arrays have non-negative integer indices and expression values
* property access on a Resource retrieves outputs

#### Substitution

Expressions denoted by `${...}` are only converted to strings when interpolated into a string with surrounding text. If a resource property takes a list or a map for example, that can be provided by a variable whose value can be substituted in. In the example below, the `httpPort` variable is used to reduce repetition in the two Kubernetes Service resources.

```yaml
name: kubernetes-port-example
variables:
  httpPort:
    protocol: TCP
    port: 80
    targetPort: 8000
resources:
  serviceOne:
    type: kubernetes:core/v1:Service
    properties:
      spec:
        selector:
          app: "MyApp"
        ports:
          - ${httpPort}
  serviceTwo:
    type: kubernetes:core/v1:Service
    properties:
      spec:
        selector:
          app: "OtherApp"
        ports:
          - ${httpPort}
```

The last two lines are equivalent as if the variable were substituted for its value:

```yaml
        ports:
          - protocol: TCP
            port: 80
            targetPort: 8000
```

#### Built-in Functions

In any expression location, an object containing a single key beginning with `Fn::` calls a built-in function.

##### `Fn::ToBase64`

Converts a UTF-8 string into a Base64 encoded string using the [standard encoding](https://pkg.go.dev/encoding/base64#pkg-variables).

```yaml
variables:
  greeting:
    Fn::ToBase64: "Hello, world!"
```

The expression `${greeting}` will return `SGVsbG8sIHdvcmxkIQ==`

##### `Fn::FromBase64`

Converts a Base64 encoded string into a UTF-8 string. **This will fail if the result is not a valid UTF-8 string**

```yaml
variables:
  greeting:
    Fn::FromBase64: SGVsbG8sIFdvcmxkIQ==
```

The expression `${greeting}` will return `Hello, World!`

##### `Fn::ToJSON`

Converts a value into its JSON representation.

```yaml
variables:
  item:
    Fn::ToJSON:
      key1: value1
      key2: 123
```

The expression `${item}` will return a JSON value `{ "key1": "value1", "key2": 123 }`.

##### `Fn::Invoke`

Calls a function from a package and returns either the whole object or a single key if given the "Return" property. The schema is:

| Property        | Type | Required           | Expression  | Description |
| ------------- |---|-------------| -----|---|
| `Function`    | string | Yes | No | Name of a function to call. |
| `Arguments`   | map[string]Expression | Yes | Yes | Arguments to pass to the expression, each key is a named argument. |
| `Return`      | string | No | No | If the function returns an object, a single key may be selected and returned instead with its name. |

```yaml
variables:
  AmazonLinuxAmi:
    Fn::Invoke:
      Function: aws:getAmi
      Arguments:
        filters:
          - name: name
            values: ["amzn-ami-hvm-*-x86_64-ebs"]
        owners: ["137112412989"]
        mostRecent: true
      Return: id
```

The expression `${AmazonLinuxAmi}` will return the AMI ID returned from the [`aws:getAmi`](https://www.pulumi.com/registry/packages/aws/api-docs/getami/) function.

##### `Fn::Join`

Joins strings together separated by a delimiter. Arguments are passed as a list, with the first item being the delimiter, and the second item a list of expressions to concatenate.

```yaml
variables:
    banana:
        Fn::Join:
            - 'NaN'
            - - Ba
              - a
```

The expression `${banana}` will have the value `"BaNaNa"`.

##### `Fn::Select`

Selects one of several options given an index. Arguments are passed as a list, with the first item being the index, 0-based, and the second item a list of expressions to select from.

```yaml
variables:
    policyVersion:
        Fn::Select:
            - 1
            - - v1
              - v1.1
              - v2.0
```

The expression `${policyVersion}` will have the value `v1.1`.

##### `Fn::*Asset` and `Fn::*Archive`

[Assets and Archives]({{< relref "/docs/intro/concepts/assets-archives" >}}) are intrinsic types to Pulumi, like strings and numbers, and some resources may take these as inputs or return them as outputs. The built-ins create each kind of asset or archive. Each takes all take a single string value.

| Built-In      | Argument Type | Description |
| ------------- |---|------|
| `Fn::FileAsset` | string | The contents of the asset are read from a file on disk. |
| `Fn::StringAsset` | string | The contents of the asset are read from a string in memory. |
| `Fn::RemoteAsset` | string | The contents of the asset are read from an http, https or file URI. |
| `Fn::FileArchive` | string | The contents of the archive are read from either a folder on disk or a file on disk in one of the supported formats: .tar, .tgz, .tar.gz, .zip or .jar. |
| `Fn::RemoteArchive` | string | The contents of the asset are read from an http, https or file URI, which must produce an archive of one of the same supported types as FileArchive. |
| `Fn::AssetArchive` | map | The contents of the archive are read from a map of either Asset or Archive objects, one file or folder respectively per entry in the map.

```yaml
variables:
  aFile:
    Fn::FileAsset: ./file.txt
  aString:
    Fn::StringAsset: Hello, world!
  aRemoteAsset:
    Fn::RemoteAsset: http://worldclockapi.com/api/json/est/now

  aFileArchive:
    Fn::FileArchive: ./file.zip
  aRemoteArchive:
    Fn::RemoteArchive: http://example.com/file.zip
  anAssetArchive:
    Fn::AssetArchive:
      file:
        Fn::StringAsset: Hello, world!
      folder:
        Fn::FileArchive: ./folder
```

##### `Fn::StackReference`

[Stack References]({{< relref "/docs/intro/concepts/stack#stackreferences" >}}) allow accessing the outputs of a stack from a YAML program. Arguments are passed as a list, with the first item being the stack name and the second argument the name of an output to reference:

```yaml
variables:
  reference:
    Fn::StackReference:
      - org/project/stack
      - outputName
```

The expression `${reference}` will have the value of the `outputName` output from the stack `org/project/stack`.

##### `Fn::Secret`

Constructs a [Secret]({{< relref "/docs/intro/concepts/secrets" >}}) from an existing value.

``` yaml
variables:
  secret:
    Fn::Secret:
      Fn::Invoke:
        Function: my:pkg:GetSecretValue
```

##### `Fn::ReadFile`

Reads a file from disk and returns the contents as a string, must be utf-8. This function has
special rules for its behavior.

``` yaml
variables:
  someText:
    Fn::ReadFile: ./README.md
```

Any subpath of the Pulumi project directory is allowed, whether it is absolute, relative, constant,
or an expression:

* `Fn::ReadFile: ./README.md`, a relative subpath
* `Fn::ReadFile: ${pulumi.cwd}/example.txt`, an absolute subpath
* `Fn::ReadFile: /opt/project-dir/example.json`, an absolute subpath if the program is in /opt/project-dir

Absolute paths to any location are allowed if they are constants:

* `Fn::ReadFile: /etc/lsb-release`
* `Fn::ReadFile: /usr/share/nginx/html`
* `Fn::ReadFile: /var/run/secrets/kubernetes.io/serviceaccount/token`

Relative paths that escape the project directory and absolute paths that are non-constant are
forbidden to prevent path traversals.

* `Fn::ReadFile: ../../etc/shadow`, a relative path that escapes the project
* `Fn::ReadFile: ${pulumi.cwd}/../../.ssh/id_rsa.pub`, an expression that returns an absolute path
   that escapes the project
