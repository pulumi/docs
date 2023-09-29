---
title_tag: "Pulumi YAML Reference | Languages & SDKs"
meta_desc: Specification for the Pulumi YAML format and built-in functions
title: Reference
h1: Pulumi YAML reference
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  languages:
    parent: yaml-language
    weight: 1
aliases:
- /docs/reference/yaml/
---

Pulumi programs can be defined in many languages, and the Pulumi YAML dialect offers an additional language for authoring Pulumi programs.

The Pulumi YAML provider supports programs written in YAML or JSON.  In both cases, the programs (`.yaml` or `.json` files) follow a simple schema, including four top level sections:

| Property | Type | Required | Expression | Description |
| - | - | - | - | - |
| `config` | [config options](/docs/reference/pulumi-yaml/#config-options) | No | No | Config specifies the [Pulumi config](/docs/concepts/config/) inputs to the deployment. |
| `resources` | map[string]Resource | No | No | Resources declares the [Pulumi resources](/docs/concepts/resources/) that will be deployed and managed by the program |
| `variables` | map[string]Expression | No | Yes | Variables specifies intermediate values of the program, the values of variables are expressions that can be re-used. |
| `outputs` | map[string]Expression | No | Yes | Outputs specifies the [Pulumi stack outputs](/docs/concepts/stack#outputs) of the program and how they are computed from the `resources` is a value of the appropriate type for the template to use if no value is specified. |

In many locations within this schema, values may be expressions which computed a value based on the `config`, `variables`, or outputs of `resources`.  These expressions can be provided in two ways:

* If an object is provided as a value, and has a key that has the prefix `fn::`, the object is treated as an expression, and the expression will be resolved to a new value that will be used in place of the object.
* Any string value is interpreted as an interpolation, with `${...}` being replaced by evaluating the expression in the `...`.

The supported expression forms for each of these is detailed below.

### Config

`config` is a map of config property keys to either values or structured declarations ([see here](/docs/reference/pulumi-yaml/#config-options)).

In beta, Pulumi YAML projects used the `configuration` key. This will eventually be deprecated; switching from `configuration` to `config` will not break existing projects.

The value of `configuration` is an object whose keys are logical names by which the config input will be referenced in expressions within the program, and whose values are elements of the schema below.  Each item in this object represents an independent config input. Either `type` or `default` is required.

| Property | Type | Required | Expression | Description |
| - | - | - | - | - |
| `type` | string | No | No | Type is the (required) data type for the parameter. It can be one of: `String`, `Number`, `List<Number>`, or `List<String>`. |
| `default` | any | No | No | Default is a value of the appropriate type for the template to use if no value is specified. |
| `secret` | bool | No | No | Secret specifies if the config value should be encrypted as a secret. |

### Resources

The value of `resources` is an object whose keys are logical resource names by which the resource will be referenced in expressions within the program, and whose values which are elements of the schema below.  Each item in this object represents a resource which will be managed by the Pulumi program.

| Property  |  Type | Required | Expressions | Description |
|- | - | - | - | - |
| `type` | string | Yes | No | Type is the Pulumi type token for this resource. |
| `defaultProvider` | bool | No | No | DefaultProvider specifies if a provider should be used for resources without an explicit one set. Set only on provider resources. |
| `properties` | `map[string]Expression` | No | Yes | Properties contains the primary resource-specific keys and values to initialize the resource state. |
| `options` | [Resource Options](#resource-options) | No | No | Options contains all resource options supported by Pulumi. |
| `get` | [Resource Getter](#resource-getter) | No | Yes | A getter function for the resource. Supplying `get` is mutually exclusive to `properties`. |

#### Resource Options

The value of the `options` property of a Resource is an object whose keys are [resource option names](/docs/concepts/options/) and whose values are elements of the schema below. No resource options are required.

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

| Property | Type | Description |
| - | - | - |
| `additionalSecretOutputs` | string[] | AdditionalSecretOutputs specifies properties that must be encrypted as secrets |
| `aliases` | string[] | Aliases specifies names that this resource used to have, so that renaming or refactoring doesn’t replace it |
| `customTimeouts` | [Custom Timeout](#custom-timeout) | CustomTimeouts overrides the default retry/timeout behavior for resource provisioning |
| `deleteBeforeReplace` | bool | DeleteBeforeReplace  overrides the default create-before-delete behavior when replacing |
| `dependsOn` | Expression[] | DependsOn makes this resource explicitly depend on another resource, by name, so that it won't be created before the dependent finishes being created (and the reverse for destruction). Normally, Pulumi automatically tracks implicit dependencies through inputs/outputs, but this can be used when dependencies aren't captured purely from input/output edges.|
| `ignoreChanges` | string[] | IgnoreChanges declares that changes to certain properties should be ignored during diffing |
| `import` | string | Import adopts an existing resource from your cloud account under the control of Pulumi |
| `parent` | Expression | Parent specifies a parent for the resource |
| `protect` | bool | Protect prevents accidental deletion of a resource |
| `provider` | Expression | Provider specifies an explicitly configured provider, instead of using the default global provider |
| `providers` |  map[string]Expression | Map of providers for a resource and its children. |
| `version` | string | Version specifies a provider plugin version that should be used when operating on a resource |
| `pluginDownloadURL` | string | PluginDownloadURL specifies a provider plugin download URL  |
| `replaceOnChanges` | string[] | ReplaceOnChanges specifies if changes to certain properties on a resource should force replacement instead of an in-place update. |
| `retainOnDelete` | bool | RetainOnDelete causes a resource to be preserved in the cloud even when it is deleted from the Pulumi state. |

#### Resource Getter

Supplying a `get` key turns the resource declaration into a [Getter Function](/docs/concepts/resources/get/).

| Property | Type | Required | Description |
| - | - | - | - |
| `id` | string | Yes | The ID of the resource to import |
| `state` | map[string]Expression | No | Known properties (input & output) of the resource. This assists the provider in figuring out the correct resource. |

#### Custom Timeout

The optional `customTimeouts` property of a resource is an object of the following schema:

| Property | Type | Required | Expression | Description |
| - | - | - | - | - |
| `create` | string | No | No | Create is the custom timeout for create operations. |
| `delete` | string | No | No | Delete is the custom timeout for delete operations. |
| `update` | string | No | No | Update is the custom timeout for update operations. |

### Providers and provider versions

There are at least two reasons to explicitly define providers in YAML, or explicitly set their versions while creating resources.

1. Using explicit versions enables pinning the dependencies used, a technique used to improve build reliability.
2. Using explicit providers enables controlling the options for providers used by each resource, as described in [Unlock Programmatic Control by Disabling Default Providers](/blog/disable-default-providers/).

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

### Outputs and Stack References

The value of [`outputs`](https://www.pulumi.com/docs/concepts/stack/#outputs) is an object whose keys are the logical names of the outputs that are available from outside the Pulumi stack (via [`pulumi stack output`](https://www.pulumi.com/docs/cli/commands/pulumi_stack_output/)), and whose values are potentially computed expressions that resolve to the values of the desired outputs.

```yaml
outputs:
  outputName: ${resource.id}
```

Stack references can be used to access the outputs of one stack from within another stack. A stack reference requires the fully qualified name of the stack as an argument in the format of `<organization>/<project>/<stack>`.

```yaml
resources:
  reference:
    type: pulumi:pulumi:StackReference
    properties:
      name: org/project/stack

outputs:
  secondOutputName: ${reference.outputs["outputName"]}
```

The above output will have the value of the `outputName` output from the stack `org/project/stack`.

### Expressions

Expressions can be used in several contexts:

* the properties of `properties` of `resources`
* the properties of `options` of `resources` that take references to other resources: `parent`, `dependsOn`, `provider`, and `providers`
* the values of `variables` and `outputs`
* some or all values provided to built-in functions, as specified below

Generally speaking, most values permit an expression and exceptions will be documented as not permitting an expression, as above.

In these contexts, any JSON/YAML value may be provided.  If that value is a string, it is interpolated.  If that value is an object, and the object has a key with a prefix of `fn::`, it is evaluated as an expression.

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

In any expression location, an object containing a single key beginning with `fn::` calls a built-in function.

##### `fn::toBase64`

Converts a UTF-8 string into a Base64 encoded string using the [standard encoding](https://pkg.go.dev/encoding/base64#pkg-variables).

```yaml
variables:
  greeting:
    fn::toBase64: "Hello, world!"
```

The expression `${greeting}` will return `SGVsbG8sIHdvcmxkIQ==`

##### `fn::fromBase64`

Converts a Base64 encoded string into a UTF-8 string. **This will fail if the result is not a valid UTF-8 string**

```yaml
variables:
  greeting:
    fn::fromBase64: SGVsbG8sIFdvcmxkIQ==
```

The expression `${greeting}` will return `Hello, World!`

##### `fn::toJSON`

Converts a value into its JSON representation.

```yaml
variables:
  item:
    fn::toJSON:
      key1: value1
      key2: 123
```

The expression `${item}` will return a JSON value `{ "key1": "value1", "key2": 123 }`.

##### `fn::invoke`

Calls a function from a package and returns either the whole object or a single field if given the `return` property. The schema is:

| Property | Type | Required | Expression | Description |
| - | - | - | - | - |
| `function` | string | Yes | No | Name of a function to call. |
| `arguments` | map[string]Expression | Yes | Yes | Arguments to pass to the expression, each key is a named argument. |
| `options` | [Invoke Options](#invoke-options) | No | No | Options for the provider calling the function. |
| `return` | string | No | No | Return the value of the field with this name. |

```yaml
variables:
  AmazonLinuxAmi:
    fn::invoke:
      function: aws:getAmi
      arguments:
        filters:
          - name: name
            values: ["amzn-ami-hvm-*-x86_64-ebs"]
        owners: ["137112412989"]
        mostRecent: true
      options:
        version: 5.9.0
      return: id
```

The expression `${AmazonLinuxAmi}` will return the AMI ID returned from the [`aws:getAmi`](/registry/packages/aws/api-docs/getami/) function.

#### Invoke Options

The value of the `options` property of an fn::invoke is an object with the following properties.

The  `parent` and `provider` values permit expressions which must use interpolation syntax to reference resources by name. For example:

```yaml
    options:
      provider: ${myEksProvider}
      parent: ${someParentResource}
```

| Property | Type | Description |
| - | - | - |
| `parent` | Expression | Parent specifies a parent for the resource |
| `provider` | Expression | Provider specifies an explicitly configured provider, instead of using the default global provider |
| `version` | string | Version specifies a provider plugin version that should be used when operating on a resource |
| `pluginDownloadURL` | string | Version specifies a URL that should be used when to download the provider plugin |

##### `fn::join`

Joins strings together separated by a delimiter. Arguments are passed as a list, with the first item being the delimiter, and the second item a list of expressions to concatenate.

```yaml
variables:
    banana:
        fn::join:
            - 'NaN'
            - - Ba
              - a
```

The expression `${banana}` will have the value `"BaNaNa"`.

##### `fn::split`

Splits a string on a delimiter. Arguments are passed as a list, with the first item being the delimiter, and the second item the string to split.

```yaml
variables:
    fruits:
        fn::split:
            - ", "
            - "apple, orange, banana"
```

The expression `${fruits}` will be a list containing the values `["apple", "orange", "banana"]`.

##### `fn::select`

Selects one of several options given an index. Arguments are passed as a list, with the first item being the index, 0-based, and the second item a list of expressions to select from.

```yaml
variables:
    policyVersion:
        fn::select:
            - 1
            - - v1
              - v1.1
              - v2.0
```

The expression `${policyVersion}` will have the value `v1.1`.

##### `fn::*Asset` and `fn::*Archive`

[Assets and Archives](/docs/concepts/inputs-outputs/assets-archives/) are intrinsic types to Pulumi, like strings and numbers, and some resources may take these as inputs or return them as outputs. The built-ins create each kind of asset or archive. Each takes all take a single string value.

| Built-In | Argument Type | Description |
| - | - | - |
| `fn::fileAsset` | string | The contents of the asset are read from a file on disk. |
| `fn::stringAsset` | string | The contents of the asset are read from a string in memory. |
| `fn::remoteAsset` | string | The contents of the asset are read from an http, https or file URI. |
| `fn::fileArchive` | string | The contents of the archive are read from either a folder on disk or a file on disk in one of the supported formats: .tar, .tgz, .tar.gz, .zip or .jar. |
| `fn::remoteArchive` | string | The contents of the asset are read from an http, https or file URI, which must produce an archive of one of the same supported types as FileArchive. |
| `fn::assetArchive` | map | The contents of the archive are read from a map of either Asset or Archive objects, one file or folder respectively per entry in the map.

```yaml
variables:
  aFile:
    fn::fileAsset: ./file.txt
  aString:
    fn::stringAsset: Hello, world!
  aRemoteAsset:
    fn::remoteAsset: http://worldclockapi.com/api/json/est/now

  aFileArchive:
    fn::fileArchive: ./file.zip
  aRemoteArchive:
    fn::remoteArchive: http://example.com/file.zip
  anAssetArchive:
    fn::assetArchive:
      file:
        fn::stringAsset: Hello, world!
      folder:
        fn::fileArchive: ./folder
```

##### `fn::secret`

Constructs a [Secret](/docs/concepts/secrets/) from an existing value.

``` yaml
variables:
  secret:
    fn::secret:
      fn::invoke:
        function: my:pkg:GetSecretValue
```

##### `fn::readFile`

Reads a file from disk and returns the contents as a string, must be utf-8. This function has
special rules for its behavior.

``` yaml
variables:
  someText:
    fn::readFile: ./README.md
```

Any subpath of the Pulumi project directory is allowed, whether it is absolute, relative, constant,
or an expression:

* `fn::readFile: ./README.md`, a relative subpath
* `fn::readFile: ${pulumi.cwd}/example.txt`, an absolute subpath
* `fn::readFile: /opt/project-dir/example.json`, an absolute subpath if the program is in /opt/project-dir

Absolute paths to any location are allowed if they are constants:

* `fn::readFile: /etc/lsb-release`
* `fn::readFile: /usr/share/nginx/html`
* `fn::readFile: /var/run/secrets/kubernetes.io/serviceaccount/token`

Relative paths that escape the project directory and absolute paths that are non-constant are
forbidden to prevent path traversals.

* `fn::readFile: ../../etc/shadow`, a relative path that escapes the project
* `fn::readFile: ${pulumi.cwd}/../../.ssh/id_rsa.pub`, an expression that returns an absolute path
   that escapes the project

#### Built-in variables

Built-in variables accessible within any Pulumi YAML program.

##### `pulumi`

The built-in `pulumi` variable contains three properties, which can be useful for retrieving information
about your current workspace.

```yaml
    variables:
      cwd: ${pulumi.cwd}
      project: ${pulumi.project}
      stack: ${pulumi.stack}
```

* `${pulumi.cwd}` retrieves the current working directory
* `${pulumi.project}` retrieves the current project
* `${pulumi.stack}` retrieves the current stack
