---
title_tag: "Dynamic Resource Providers"
meta_desc: Dynamic resource providers are providers that can be written inside your
  Pulumi program. Learn how to use dynamic providers and use cases for them.
title: Dynamic providers
h1: Dynamic resource providers
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    name: Dynamic providers
    parent: iac-concepts-resources
    weight: 6
  concepts:
    parent: resources
    weight: 6
aliases:
  - /docs/intro/concepts/resources/dynamic-providers/
  - /docs/concepts/resources/dynamic-providers/
search:
  keywords:
    - providers
    - resource
    - dynamic providers
    - resource provider
    - custom resource
---

The dynamic resource provider construct can be used to build a local provider for simple APIs and use-cases. Dynamic resource providers are only able to be used in Pulumi programs written in the same language as the dynamic resource provider. But, they are lighter weight than custom providers and for many use-cases are sufficient to leverage the Pulumi state model. For more sophisticated APIs, one can create a [bridged or native provider](/docs/iac/packages-and-automation/pulumi-packages/).

{{% notes type="info" %}}
**Note:** The Pulumi registry includes the [Command Provider](https://www.pulumi.com/registry/packages/command/) as an even lighter weight solution and can be used in place of a dynamic resource provider in some cases.
{{% /notes %}}

There are several reasons why you might want to write a dynamic resource provider. Here are some of them:

- You want to create some new custom resource types.
- You want to use a cloud provider that Pulumi doesn’t support.

All dynamic providers must conform to certain interface requirements. You must at least implement the `create` function but, in practice, you will probably also want to implement the `read`, `update`, and `delete` functions as well.

For example, if creating a dynamic resource provider for WordPress, you would probably want to create new blogs, update existing blogs, and destroy them. The mechanics of how these operations happen would be essentially the same as if you used one of the standard resource providers. The difference is that the calls that would've been made on the standard resource provider by the Pulumi engine would now be made on your dynamic resource provider and it, in turn, would make the API calls to WordPress.

Dynamic providers are defined by first implementing the `pulumi.dynamic.ResourceProvider` interface. This interface supports all CRUD operations, but only the create function is required. A minimal implementation might look like this:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
const myProvider = {
    async create(inputs) {
        return { id: "foo", outs: {}};
    }
}
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const myProvider: pulumi.dynamic.ResourceProvider = {
    async create(inputs) {
        return { id: "foo", outs: {}};
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi.dynamic import ResourceProvider, CreateResult

class MyProvider(ResourceProvider):
    def create(self, inputs):
        return CreateResult(id_="foo", outs={})
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// Dynamic Providers are currently not supported in Go.
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Dynamic Providers are currently not supported in .NET.
```

{{% /choosable %}}
{{% choosable language java %}}

```java
// Dynamic Providers are currently not supported in Java.
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# Dynamic Providers are currently not supported in YAML.
```

{{% /choosable %}}

{{< /chooser >}}

This dynamic resource provider is then used to create a new kind of custom resource by inheriting from the `pulumi.dynamic.Resource` base class, which is a subclass of `pulumi.CustomResource`:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
class MyResource extends pulumi.dynamic.Resource {
    constructor(name, props, opts) {
        super(myProvider, name, props, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
class MyResource extends pulumi.dynamic.Resource {
    constructor(name: string, props: {}, opts?: pulumi.CustomResourceOptions) {
        super(myProvider, name, props, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi import ResourceOptions
from pulumi.dynamic import Resource
from typing import Any, Optional

class MyResource(Resource):
    def __init__(self, name: str, props: Any, opts: Optional[ResourceOptions] = None):
         super().__init__(MyProvider(), name, props, opts)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// Dynamic Providers are currently not supported in Go.
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Dynamic Providers are currently not supported in .NET.
```

{{% /choosable %}}
{{% choosable language java %}}

```java
// Dynamic Providers are currently not supported in Java.
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# Dynamic Providers are currently not supported in YAML.
```

{{% /choosable %}}

{{< /chooser >}}

We can now create instances of the new `MyResource` resource type in our program with `new MyResource("name", args)`, just like we would any custom resource. Pulumi understands how to use the custom provider logic appropriately.

Specifically:

1. If Pulumi determines the resource has not yet been created, it will call the create method on the resource provider interface.
1. If another Pulumi deployment happens and the resource already exists, Pulumi will call the diff method to determine whether a change can be made in place or whether a replacement is needed.
1. If a replacement is needed, Pulumi will call create for the new resource and then call delete for the old resource.
1. If no replacement is needed, Pulumi will call update.
1. In all cases, Pulumi first calls the check method with the resource arguments to give the provider a chance to verify that the arguments are valid.
1. If Pulumi needs to read an existing resource without managing it directly, it will call read.

See below for details on each of these functions.

## How Dynamic Providers Work

Dynamic providers are a flexible and low-level mechanism that allow you to include arbitrary code directly into the deployment process. While most code in a Pulumi program runs while the desired state of the resources is constructed (in other words, as the resource graph is built), the code inside a dynamic provider’s implementation, such as `create` or `update`, runs during resource provisioning, while the resource graph is being turned into a set of CRUD operations scheduled against the cloud provider.

In fact, these two phases of execution actually run in completely separate processes. The construction of a `new MyResource` happens inside the JavaScript, Python, or Go process running in your Pulumi program. In contrast, your implementations of create or update are executed by a special resource provider binary called `pulumi-resource-pulumi-nodejs`. This binary is what actually implements the Pulumi resource provider gRPC interface and it speaks directly to the Pulumi engine.

Because your implementation of the resource provider interface must be used by a different process, potentially at a different point in time, dynamic providers are built on top of the same [function serialization](/docs/iac/concepts/miscellaneous/function-serialization/) that is used for turning callbacks into AWS Lambdas or Google Cloud Functions. Because of this serialization, there are some limits on what can be done inside the implementation of the resource provider interface. You can read more about these limitations in the function serialization documentation.

## The Resource Provider Interface

Implementing the `pulumi.dynamic.ResourceProvider` interface requires implementing a subset of the methods listed further down in this section. Each of these methods can be asynchronous, and most implementations of these methods will perform network I/O to provision resources in a backing cloud provider or other resource model. There are several important contracts between a dynamic provider and the Pulumi CLI that inform when these methods are called and with what data.

Though the input properties passed to a `pulumi.dynamic.Resource` instance will usually be [Input values](/docs/concepts/inputs-outputs/), the dynamic provider’s functions are invoked with the fully resolved input values in order to compose well with Pulumi resources. Strong typing for the inputs to your provider’s functions can help clarify this. You can achieve this by creating a second interface with the same properties as your resource’s inputs, but with fully unwrapped types.

{{% notes type="warning" %}}
There are nuances to how data is passed between the core Pulumi program and your dynamic provider. Learn more here: https://github.com/pulumi/pulumi/issues/16582.
{{% /notes %}}

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
// Exported type.
export interface MyResourceInputs {
    myStringProp: pulumi.Input<string>;
    myBoolProp: pulumi.Input<boolean>;
    ...
}

// Non-exported type used by the provider functions.
// This interface contains the same inputs, but as un-wrapped types.
interface MyResourceProviderInputs {
    myStringProp: string;
    myBoolProp: boolean;
    ...
}

class MyResourceProvider implements pulumi.dynamic.ResourceProvider {
    async create(inputs: MyResourceProviderInputs): Promise<pulumi.dynamic.CreateResult> {
        ...
    }

    async diff(id: string, oldOutputs: MyResourceProviderOutputs, newInputs: MyResourceProviderInputs): Promise<pulumi.dynamic.DiffResult> {
        ...
    }
    ...
}

class MyResource extends pulumi.dynamic.Resource {
    constructor(name: string, props: MyResourceInputs, opts?: pulumi.CustomResourceOptions) {
        super(new MyResourceProvider(), name, props, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi import Input, Output, ResourceOptions
from pulumi.dynamic import *
from typing import Any, Optional

class MyResourceInputs(object):
    my_string_prop: Input[str]
    my_bool_prop: Input[bool]

    def __init__(self, my_string_prop, my_bool_prop):
        self.my_string_prop = my_string_prop
        self.my_bool_prop = my_bool_prop

class _MyResourceProviderInputs(object):
    """
    MyResourceProviderInputs is the unwrapped version of the same inputs
    from the MyResourceInputs class.
    """
    my_string_prop: str
    my_bool_prop: bool

    def __init__(self, my_string_prop: str, my_bool_prop: bool):
        self.my_bool_prop = my_bool_prop
        self.my_string_prop = my_string_prop

class MyResourceProvider(ResourceProvider):
    def create(self, inputs: _MyResourceProviderInputs) -> CreateResult:
        ...
        return CreateResult()

    def diff(self, id: str, oldInputs: _MyResourceProviderInputs, newInputs: _MyResourceProviderInputs) -> DiffResult:
        ...
        return DiffResult()

class MyResource(Resource):
    def __init__(self, name: str, props: MyResourceInputs, opts: Optional[ResourceOptions] = None):
        super().__init__(MyResourceProvider(), name, {**vars(props)}, opts)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// Dynamic Providers are currently not supported in Go.
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Dynamic Providers are currently not supported in .NET.
```

{{% /choosable %}}
{{% choosable language java %}}

```java
// Dynamic Providers are currently not supported in Java.
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# Dynamic Providers are currently not supported in YAML.
```

{{% /choosable %}}

{{< /chooser >}}

### configure(ConfigureRequest)

The `configure` method is invoked after a dynamic resource provider is loaded. This method is optional and is called exactly once for each provider instance. The `configure` method receives a `ConfigureRequest` object as its argument, which contains the configuration of the current stack. This method can be used to perform any necessary setup for the provider, and allows you to read configuration values and store them for later use in other provider methods.

### check(olds, news)

The `check` method is invoked before any other methods. The resolved input properties that were originally provided to the resource constructor by the user are passed to it. The operation is passed both the old input properties that were stored in the *state file* after the previous update to the resource, as well as the new inputs from the current deployment. It has two jobs:

1. Verify that the inputs (particularly the news) are valid or return useful error messages if they are not.
1. Return a set of checked inputs.

The inputs returned from the call to `check` will be the inputs that the Pulumi engine uses for all further processing of the resource, including the values that will be passed back in to `diff`, `create`, `update`, or other operations. In many cases, the news can be returned directly as the checked inputs. But in cases where the provider needs to populate defaults, or do some normalization on values, it may want to do that in the `check` method so that this data is complete and normalized prior to being passed in to other methods.

### create(inputs)

The `create` method is invoked when the URN of the resource created by the user is not found in the existing state of the deployment. The engine passes the provider the checked inputs returned from the call to `check`. The `create` method creates the resource in the cloud provider. It then returns two pieces of data:

1. An id that can uniquely identify the resource in the backing provider for later lookups, and
1. A set of outputs from the backing provider that should be returned to the user code as properties on the CustomResource object. These outputs are stored in the checkpoint file. If an error occurs, an exception can be thrown from the create method that should be returned to the user.

### diff(id, olds, news)

The `diff` method is invoked when the URN of the resource created by the user already exists. Because the resource already exists it will need to be either updated or replaced. The `diff` method is passed the `id` of the resource, as returned by `create`, as well as the old outputs from the checkpoint file, which are values returned from a previous call to either `create` or `update`. The checked inputs from the current deployment are passed to the diff method.

It returns four optional values:

- `changes: true` if the provider believes there is a difference between the olds and news and wants to do an update or replace to effect this change.
- `replaces`: An array of property names that have changed that should force a replacement. Returning a non-zero length array tells the Pulumi engine to schedule a replacement instead of an update. Replacements might involve downtime, so this value should only be used when a diff requested by the user cannot be implemented as an in-place update on the cloud provider.
- `stables`: An array of property names that are known not to change between updates. Pulumi will use this information to allow some [`apply`](/docs/concepts/inputs-outputs/#apply) calls on [`Output[T]`](/docs/concepts/inputs-outputs/#outputs) to be processed during `previews` because it knows that the values of these property names will stay the same during an update.
- `deleteBeforeReplace`: true if the proposed replacements require that the existing resource be deleted before creating the new one. By default, Pulumi will try to create the new resource before deleting the old one to avoid downtime. If an error occurs, an exception can be thrown from the diff method to return this error to the user.

### update(id, olds, news)

The `update` method is invoked if the call to diff indicates that a replacement is unnecessary. The method is passed the `id` of the resource as returned by `create`, and the old outputs from the checkpoint file, which are values returned from a previous call to either `create` or `update`. The new checked inputs are also passed from the current deployment. The `update` method is expected to do the work in the cloud provider to update an existing resource to the new desired state. It then returns a new set of `outputs` from the cloud provider that should be returned to the user code as properties on the [`CustomResource`](/docs/concepts/resources/) object, and stored into the checkpoint file. If an error occurs, an exception can be thrown from the `update` method to return this error to the user.

### delete(id, props)

The `delete` operation is invoked if the URN exists in the previous state but not in the new desired state, or if a replacement is needed. The method is passed the `id` of the resource as returned by `create`, and the old outputs from the checkpoint file, which are values returned from a previous call to either `create` or `update`. The method deletes the corresponding resource from the cloud provider. Nothing needs to be returned. If an error occurs, an exception can be thrown from the `delete` method to return this error to the user.

### read(id, props)

The `read` method is invoked when the Pulumi engine needs to get data about a resource that is not managed by Pulumi. The method is passed the `id` of the resource, as tracked in the cloud provider, and an optional bag of additional properties that can be used to disambiguate the request, if needed. The `read` method looks up the requested resource, and returns the canonical `id` and output properties of this resource if found. If an error occurs, an exception can be thrown from the `read` method to return this error to the user.

## Dynamic Resource Inputs

The inputs to your `pulumi.dynamic.ResourceProvider`’s functions come from subclasses of `pulumi.dynamic.Resource`. These inputs include any values in the input arguments passed to the `pulumi.dynamic.Resource` constructor. This is just a map of key/value pairs however, in statically typed languages, you can declare types for these input shapes.

For example, `props`, in the `MyResource` class shown below, defines the inputs to the resource provider functions:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
class MyResource extends pulumi.dynamic.Resource {
    constructor(name, props, opts) {
        super(myprovider, name, props, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
interface MyResourceInputs {
    myStringProp: pulumi.Input<string>;
    myBoolProp: pulumi.Input<boolean>;
    ...
}

class MyResource extends pulumi.dynamic.Resource {
    constructor(name: string, props: MyResourceInputs, opts?: pulumi.CustomResourceOptions) {
        super(myprovider, name, props, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi import Input, ResourceOptions
from pulumi.dynamic import Resource
from typing import Any, Optional

class MyResourceInputs(object):
    my_string_prop: Input[str]
    my_bool_prop: Input[bool]
    def __init__(self, my_string_prop, my_bool_prop):
        self.my_string_prop = my_string_prop
        self.my_bool_prop = my_bool_prop

class MyResource(Resource):
    def __init__(self, name: str, props: MyResourceInputs, opts: Optional[ResourceOptions] = None):
         super().__init__(MyProvider(), name, {**vars(props)}, opts)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// Dynamic Providers are currently not supported in Go.
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Dynamic Providers are currently not supported in .NET.
```

{{% /choosable %}}
{{% choosable language java %}}

```java
// Dynamic Providers are currently not supported in Java.
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# Dynamic Providers are not supported in YAML.
```

{{% /choosable %}}

{{< /chooser >}}

## Dynamic Resource Outputs

Any outputs can be returned by your create function in the outs property of `pulumi.dynamic.CreateResult`.

{{% notes "info" %}}
The following only applies to statically typed languages.
{{% /notes %}}

If you need to access the outputs of your custom resource outside it with strong typing support, declare each output property returned in the `outs` property by your `create` function as a class member of the `pulumi.dynamic.Resource` itself. For example, in TypeScript, these outputs must be declared as `public readonly` class members in your `pulumi.dynamic.Resource` class. These class members must also have the type `pulumi.Output<T>`.

The name of the class member must match the names of the output properties as returned by the `create` function.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
JavaScript does not support types.
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
...

interface MyResourceProviderOutputs {
    myNumberOutput: number;
    myStringOutput: string;
}

class MyResourceProvider implements pulumi.dynamic.ResourceProvider {
    async create(inputs: MyResourceProviderInputs): Promise<pulumi.dynamic.CreateResult> {
        ...
        // Values are for an example only.
        return { id: "...", outs: { myNumberOutput: 12, myStringOutput: "some value" }};
    }
}

export class MyResource extends pulumi.dynamic.Resource {
    public readonly myStringOutput!: pulumi.Output<string>;
    public readonly myNumberOutput!: pulumi.Output<number>;

    constructor(name: string, props: MyResourceInputs, opts?: pulumi.CustomResourceOptions) {
        super(new MyResourceProvider(), name, { myStringOutput: undefined, myNumberOutput: undefined, ...props }, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi import ResourceOptions, Input, Output
from pulumi.dynamic import Resource, ResourceProvider, CreateResult
from typing import Any, Optional

...
...

class MyProvider(ResourceProvider):
    def create(self, inputs):
        return CreateResult(id_="foo", outs={ 'my_number_output': 12, 'my_string_output': "some value" })

class MyResource(Resource):
    my_string_output: Output[str]
    my_number_output: Output[str]

    def __init__(self, name: str, props: MyResourceInputs, opts: Optional[ResourceOptions] = None):
         super().__init__(MyProvider(), name, { 'my_string_output': None, 'my_number_output': None, **vars(props) }, opts)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// Dynamic Providers are not yet supported in Go.
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Dynamic Providers are currently not supported in .NET.
```

{{% /choosable %}}
{{% choosable language java %}}

```java
// Dynamic Providers are currently not supported in Java.
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# Dynamic Providers are not supported in YAML.
```

{{% /choosable %}}

{{< /chooser >}}

## Dynamic Provider Examples

### Example: Random number generator

This example generates a random number using a dynamic provider. It highlights using dynamic providers to run some code only when a resource is created, and then store the results of that in the state file so that this value is maintained across deployments of the resource. Because we want our random number to be created once, and then remain stable for subsequent updates, we cannot use a random number generator in our program; we need dynamic providers. The result is a provider similar to the one provided in `@pulumi/random`, just specific to our program and language.

Implementing this example requires that we have a provider and resource type:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let pulumi = require("@pulumi/pulumi");
let crypto = require("crypto");

let randomprovider = {
    async create(inputs) {
        return { id: crypto.randomBytes(16).toString('hex'), outs: {}};
    },
}

class Random extends pulumi.dynamic.Resource {
    constructor(name, opts) {
        super(randomprovider, name, {}, opts);
    }
}

exports.Random = Random;
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as crypto from "crypto";

const randomprovider: pulumi.dynamic.ResourceProvider = {
    async create(inputs) {
        return { id: crypto.randomBytes(16).toString('hex'), outs: {}};
    },
}

export class Random extends pulumi.dynamic.Resource {
    constructor(name: string, opts?: pulumi.CustomResourceOptions) {
        super(randomprovider, name, {}, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi import ResourceOptions
from pulumi.dynamic import Resource, ResourceProvider, CreateResult
from typing import Optional
import binascii
import os

class RandomProvider(ResourceProvider):
    def create(self, inputs):
        return CreateResult(id_=binascii.b2a_hex(os.urandom(16)), outs={})

class Random(Resource):
    def __init__(self, name: str, opts: Optional[ResourceOptions] = None):
         super().__init__(RandomProvider(), name, {}, opts)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// Dynamic Providers are currently not supported in Go.
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
// Dynamic Providers are currently not supported in .NET.
```

{{% /choosable %}}
{{% choosable language java %}}

```java
// Dynamic Providers are currently not supported in Java.
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# Dynamic Providers are not supported in YAML.
```

{{% /choosable %}}

{{< /chooser >}}

Now, with this, we can construct new `Random` resource instances, and Pulumi will drive the right calls at the right time.

### Example: GitHub Labels REST API (Credentials via Pulumi Config)

This example highlights how to make REST API calls to a backing provider to perform CRUD operations. In this case, the backing provider is the GitHub API.

A fundamental requirement for a dynamic provider that calls an API is managing the credentials needed for the API calls. One approach is to just pass the necessary creds as inputs when declaring resources using the dynamic resource provider. But passing provider credentials when declaring resources is an antipattern, to say the least. Therefore, other mechanisms that allow the dynamic resource provider to consume the needed credentials outside of the resource declaration are preferred. This example uses [Pulumi Config](/docs/concepts/config) to get the credential.

Because the resource provider method implementations will be serialized and used in a different process, we keep all the work to initialize the REST client and to make calls to it, local to each function.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let pulumi = require("@pulumi/pulumi");
let Octokit = require("@octokit/rest");

class githubLabelProvider {
    // Set a stack config variable named githubToken (e.g. pulumi config set githubToken <VALUE> --secret)
    async configure(req) {
        this.auth = req.config.require("githubToken")
    }
    async create(inputs) {
        const octokit = new Octokit({this.auth});
        const label = await octokit.issues.createLabel(inputs);
        return { id: label.data.id.toString(), outs: label.data };
    }
    async update(id, olds, news) {
        const octokit = new Octokit({this.auth});
        const label = await octokit.issues.updateLabel({ ...news, current_name: olds.name });
        return { outs: label.data };
    }
    async delete(id, props) {
        const octokit = new Octokit({this.auth});
        await octokit.issues.deleteLabel(props);
    }
}

class Label extends pulumi.dynamic.Resource {
    constructor(name, args, opts) {
        super(new githubLabelProvider, name, args, opts);
    }
}

exports.Label = Label;
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import { Octokit } from "@octokit/rest";

export interface LabelResourceInputs {
    owner: pulumi.Input<string>;
    repo: pulumi.Input<string>;
    name: pulumi.Input<string>;
    color: pulumi.Input<string>;
    description?: pulumi.Input<string>;
}

interface LabelInputs {
    owner: string;
    repo: string;
    name: string;
    color: string;
    description?: string;
}

class githubLabelProvider implements pulumi.dynamic.ResourceProvider {
    private auth: string = ""

    async configure(req: pulumi.dynamic.ConfigureRequest): Promise<void> {
        // Set a stack config variable named githubToken (e.g. pulumi config set githubToken <VALUE> --secret)
        this.auth = req.config.require("githubToken")
    }
    async create(inputs: LabelInputs) {
        const octokit = new Octokit({this.auth});
        const label = await octokit.issues.createLabel({
            owner: inputs.owner,
            repo: inputs.repo,
            name: inputs.name,
            color: inputs.color
        });
        return { id: label.data.id.toString(), outs: label.data };
    }
    async update(id: string, olds: LabelInputs, news: LabelInputs) {
        const octokit = new Octokit({this.auth});
        const label = await octokit.issues.updateLabel({
            owner: news.owner,
            repo: news.repo,
            current_name: olds.name,
            name: news.name,
            color: news.color
        });
        return {outs: label.data};
    }
    async delete(id: string, props: LabelInputs) {
        const octokit = new Octokit({this.auth});
        await octokit.issues.deleteLabel({owner: props.owner, repo: props.repo, name: props.name});
    }
}

export class Label extends pulumi.dynamic.Resource {
    constructor(name: string, args: LabelResourceInputs, opts?: pulumi.CustomResourceOptions) {
        super(new githubLabelProvider, name, args, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
from pulumi import ComponentResource, export, Input, Output
from pulumi.dynamic import Resource, ResourceProvider, CreateResult, UpdateResult, ConfigureRequest
from typing import Optional
from github import Github, GithubObject

class GithubLabelArgs(object):
    owner: Input[str]
    repo: Input[str]
    name: Input[str]
    color: Input[str]
    description: Optional[Input[str]]
    def __init__(self, owner, repo, name, color, description=None):
        self.owner = owner
        self.repo = repo
        self.name = name
        self.color = color
        self.description = description

class GithubLabelProvider(ResourceProvider):
    auth: str
    def configure(self, req: ConfigureRequest):
        # Set a stack config variable named githubToken (e.g. pulumi config set githubToken <VALUE> --secret)
        self.auth = req.config.require("githubToken")

    def create(self, props):
        auto_secret = True
        g = Github(self.auth)
        l = g.get_user(props["owner"]).get_repo(props["repo"]).create_label(
            name=props["name"],
            color=props["color"],
            description=props.get("description", GithubObject.NotSet))
        return CreateResult(l.name, {**props, **l.raw_data})
    def update(self, id, _olds, props):
        auto_secret = True
        g = Github(self.auth)
        l = g.get_user(props["owner"]).get_repo(props["repo"]).get_label(id)
        l.edit(name=props["name"],
               color=props["color"],
               description=props.get("description", GithubObject.NotSet))
        return UpdateResult({**props, **l.raw_data})
    def delete(self, id, props):
        g = Github(self.auth)
        l = g.get_user(props["owner"]).get_repo(props["repo"]).get_label(id)
        l.delete()

class GithubLabel(Resource):
    name: Output[str]
    color: Output[str]
    url: Output[str]
    description: Output[str]
    def __init__(self, name, args: GithubLabelArgs, opts = None):
        full_args = {'url':None, 'description':None, 'name':None, 'color':None, **vars(args)}
        super().__init__(GithubLabelProvider(), name, full_args, opts)

label = GithubLabel("foo", GithubLabelArgs("lukehoban", "todo", "mylabel", "d94f0b"))

export("label_color", label.color)
export("label_url", label.url)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// Dynamic Providers are not currently supported in Go.
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Dynamic Providers are currently not supported in .NET.
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# Dynamic Providers are not supported in YAML.
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// Dynamic Providers are currently not supported in Java.
```

{{% /choosable %}}
{{< /chooser >}}

### Example: Pulumi Cloud REST API (Creds via Environment Variables)

This example highlights how to make REST API calls to a backing provider to perform CRUD operations. In this case, the backing provider is the [Pulumi Cloud API](/docs/pulumi-cloud/cloud-rest-api).

A fundamental requirement for a dynamic provider that calls an API is managing the credentials needed for the API calls. One approach is to just pass the necessary creds as inputs when declaring resources using the dynamic resource provider. But passing provider credentials when declaring resources is an antipattern, to say the least. Therefore, other mechanisms that allow the dynamic resource provider to consume the needed credentials outside of the resource declaration are preferred. This example uses environment variables to pass the credentials. A big advantage of this approach is that if the credentials change before `pulumi destroy` is run, there is no need to first run a `pulumi up` to update the credentials used by the dynamic provider.

Because the resource provider method implementations will be serialized and used in a different process, we keep all the work to initialize the REST client and to make calls to it, local to each function.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
const pulumi = require("@pulumi/pulumi");
const axios = require('axios');

// Use user-specified API URL if provided. Otherwise, use default Pulumi cloud URL.
const basePulumiApiUrl= process.env.PULUMI_CLOUD_API_URL || "https://api.pulumi.com"

// NOTE: When Pulumi Environments is GAed, the API path will no longer include "preview".
const basePulumiEnvApiUrl= `${basePulumiApiUrl}/api/preview/environments`

const PulumiEnvironmentProvider = {

  //*** CREATE ***//
  async create(inputs) {
  
    // It is important to set up the headers in the action as opposed to outside of the provider so that the environment variable reference is
    // stored in state instead of the actual credential value.
    const headers = {
      'Authorization': `token ${process.env.PULUMI_ACCESS_TOKEN}`,
      'Content-Type': 'application/json'
    }

    const createEnvUrl = `${basePulumiEnvApiUrl}/${inputs.orgName}/${inputs.environmentName}`

    let envId = "unassigned"
    await axios.post(createEnvUrl, {},
      {
          headers: headers
      }).then((response) => {
        // Pulumi Cloud does not return a unique ID for an environment. So create one using the org and environment name.
        envId = `${inputs.orgName}/${inputs.environmentName}`
      }).catch((reason) => {
        console.log("ERROR: ", `${reason.status} - ${reason.response?.statusText}`)
        process.exit(10)
      })

      const envOuts = {id: envId, envName: inputs.environmentName, orgName: inputs.orgName}
      return { id: envId, outs: envOuts }
  },

  //*** DELETE ***//
  async delete(id, props) {

    // It is important to set up the headers in the action as opposed to outside of the provider so that the environment variable reference is
    // stored in state instead of the actual credential value.
    const headers = {
      'Authorization': `token ${process.env.PULUMI_ACCESS_TOKEN}`,
      'Content-Type': 'application/json'
    }

    const deleteEnvUrl = `${basePulumiEnvApiUrl}/${id}`
    await axios.delete(deleteEnvUrl, {
          headers: headers
    })
    .then((response) => {
    })
    .catch((reason) => {
      console.log("ERROR: ", `${reason.response?.status} - ${reason.response?.statusText}`)
      process.exit(20)
    })
  }
}

class PulumiEnvironment extends pulumi.dynamic.Resource {

  constructor(name, args, opts) {
    super(PulumiEnvironmentProvider, name, args, opts);
  }
}

exports.PulumiEnvironment = PulumiEnvironment;
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import { Input, Output } from "@pulumi/pulumi";
import { CreateResult } from "@pulumi/pulumi/dynamic";
import axios from 'axios'
import { AxiosResponse, AxiosError } from 'axios'

export interface PulumiEnvironmentArgs {
  orgName: string;
  environmentName: string;
}

export interface PulumiEnvironmentProviderArgs {
  orgName: string
  environmentName: string;
}

// Use user-specified API URL if provided. Otherwise, use default Pulumi cloud URL.
const basePulumiApiUrl= process.env.PULUMI_CLOUD_API_URL || "https://api.pulumi.com"

// NOTE: When Pulumi Environments is GAed, the API path will no longer include "preview".
const basePulumiEnvApiUrl= `${basePulumiApiUrl}/api/preview/environments`

const PulumiEnvironmentProvider: pulumi.dynamic.ResourceProvider = {

  //*** CREATE ***//
  async create(inputs: PulumiEnvironmentProviderArgs): Promise<CreateResult> {
  
    // Use environment variable for authentication.
    // This keeps the actual PULUMI_ACCESS_TOKEN value out of state and instead only the env variable reference is kept in state.
    // Therefore, if the token is changed between the create and the destroy, the destroy will use the new creds.
    const headers = {
      'Authorization': `token ${process.env.PULUMI_ACCESS_TOKEN}`,
      'Content-Type': 'application/json'
    }

    const createEnvUrl = `${basePulumiEnvApiUrl}/${inputs.orgName}/${inputs.environmentName}`

    let envId:string = "unassigned"
    await axios.post(createEnvUrl, {},
      {
          headers: headers
      }).then((response: AxiosResponse) => {
        // Pulumi Cloud does not return a unique ID for an environment. So create one using the org and environment name.
        envId = `${inputs.orgName}/${inputs.environmentName}`
      }).catch((reason: AxiosError) => {
        console.log("ERROR: ", `${reason.status} - ${reason.response?.statusText}`)
        process.exit(10)
      })

      const envOuts = {id: envId, envName: inputs.environmentName, orgName: inputs.orgName}
      return { id: envId, outs: envOuts }
  },

  //*** DELETE ***//
  async delete(id, props) {
    // Use environment variable for authentication.
    // This keeps the actual PULUMI_ACCESS_TOKEN value out of state and instead only the env variable reference is kept in state.
    // Therefore, if the token is changed between the create and the destroy, the destroy will use the new creds.
    const headers = {
      'Authorization': `token ${process.env.PULUMI_ACCESS_TOKEN}`,
      'Content-Type': 'application/json'
    }

    const deleteEnvUrl = `${basePulumiEnvApiUrl}/${id}`
    await axios.delete(deleteEnvUrl, {
          headers: headers
    })
    .then((response: AxiosResponse) => {
    })
    .catch((reason: AxiosError) => {
      console.log("ERROR: ", `${reason.response?.status} - ${reason.response?.statusText}`)
      process.exit(20)
    })
  }
}

export class PulumiEnvironment extends pulumi.dynamic.Resource {

  constructor(name: string, args: PulumiEnvironmentArgs, opts?: pulumi.CustomResourceOptions) {
    super(PulumiEnvironmentProvider, name, args, opts);
  }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
from pulumi import Input, Output
from pulumi.dynamic import ResourceProvider, CreateResult, Resource
import requests
import os

class PulumiEnvironmentArgs:
    def __init__(self, org_name: str, environment_name: str):
        self.org_name = org_name
        self.environment_name = environment_name

class PulumiEnvironmentProviderArgs:
    def __init__(self, org_name: str, environment_name: str):
        self.org_name = org_name
        self.environment_name = environment_name

# Use user-specified API URL if provided. Otherwise, use default Pulumi cloud URL.
base_pulumi_api_url = os.getenv("PULUMI_CLOUD_API_URL", "https://api.pulumi.com")

# NOTE: When Pulumi Environments is GAed, the API path will no longer include "preview".
base_pulumi_env_api_url = f"{base_pulumi_api_url}/api/preview/environments"

# Set up the headers using the environment variable.
headers = {
    'Authorization': f"token {os.getenv('PULUMI_ACCESS_TOKEN')}",
    'Content-Type': 'application/json'
}

class PulumiEnvironmentProvider(ResourceProvider):
    def create(self, inputs: PulumiEnvironmentProviderArgs) -> CreateResult:

        create_env_url = f"{base_pulumi_env_api_url}/{inputs['org_name']}/{inputs['environment_name']}"

        env_id = "unassigned"
        response = requests.post(create_env_url, headers=headers)
        if response.status_code == 200 or response.status_code == 201:
            env_id = f"{inputs['org_name']}/{inputs['environment_name']}"
        else:
            print(f"ERROR: {response.status_code} - {response.text}")
            os._exit(10)

        env_outs = {"id": env_id, "envName": inputs['environment_name'], "orgName": inputs['org_name']}
        return CreateResult(id_=env_id, outs=env_outs)

    def delete(self, id: str, props):

        # The id provides the "org/environment-name" path for the environment
        delete_env_url = f"{base_pulumi_env_api_url}/{id}"

        response = requests.delete(delete_env_url, headers=headers)
        if response.status_code != 200:
            print(f"ERROR: {response.status_code} - {response.text}")
            os._exit(20)

class PulumiEnvironment(Resource):
    def __init__(self, name, args: PulumiEnvironmentArgs, opts=None):
        super().__init__(PulumiEnvironmentProvider(), name, vars(args), opts)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// Dynamic Providers are not currently supported in Go.
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Dynamic Providers are currently not supported in .NET.
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# Dynamic Providers are not supported in YAML.
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// Dynamic Providers are currently not supported in Java.
```

{{% /choosable %}}
{{< /chooser >}}

### Additional Examples

- [Add a Custom Domain to an Azure CDN endpoint](https://github.com/pulumi/examples/tree/846811de2c7faa4694454c64edc9bbcdb31d533e/classic-azure-ts-dynamicresource)
    Similar to the previous example, this is another example of a shortcoming of the regular Azure resource provider available in Pulumi. However, due to the availability of a REST API, we can easily add a custom domain to an Azure CDN resource using a dynamic provider.
