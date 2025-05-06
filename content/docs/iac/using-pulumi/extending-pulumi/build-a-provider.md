---
title_tag: "Build a Provider"
meta_desc: "Learn the process for building a Pulumi Provider that can be packaged and published in the Pulumi Registry."
title: Build a Provider
h1: Build a Provider
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Build a Provider
        parent: iac-extending-pulumi
        weight: 4
---

## When to use a provider

A Pulumi Provider allows you to define new resource types, enabling integration with virtually any service or tool. Pulumi providers are ideal when you need to manage resources that are not yet supported by existing Pulumi providers or when you require custom behavior for managing external systems or APIs. Providers are a powerful extension point, but before building a full provider consider if your use case can be covered by [building a component](/docs/iac/using-pulumi/extending-pulumi/build-a-component/) or using [dynamic provider functions](/docs/iac/using-pulumi/extending-pulumi/build-a-dynamic-provider/).

## What’s needed to implement a provider?

### The provider interface

The Pulumi [Provider](https://pkg.go.dev/github.com/pulumi/pulumi-go-provider#Provider) interface implments the following core methods which form the foundation of Pulumi's resource lifecycle management:

- **Create** – provisions a new resource
- **Read** – fetches the resource
- **Update** – updates an existing resource
- **Delete** – removes a resource
- **Diff** – computes the differences between the current resource and desired updates to the resource
- **Check** – validates the input parameters
- **Configure** – initializes provider-wide settings (e.g. credentials)

### How a provider runs

Pulumi providers are [gRPC](https://grpc.io/) servers that respond to commands from the Pulumi engine. When a Pulumi program runs (e.g. `pulumi up`), the engine connects to the provider process and sends instructions to create, update, or delete resources via calls to the provider interface implementation.

### Configuration, secrets, outputs, and state

Beyond the core functions involved with managing resources, there are a number of other aspects to a Pulumi provider. It is necessary to configure the provider, pass secrets, return output values, and store the state of resources. The Pulumi provider interface has built-in facilities for all of those concerns:

- **Configuration and Secrets**: Set via [Pulumi ESC](/docs/esc/) [environments](/docs/esc/environments/) and/or `pulumi config`. Encrypted secrets and configuration values are passed to the provider at runtime.
- **Outputs**: Providers return outputs from resources, which can be referenced by other resources.
- **State**: Pulumi maintains resource state to track dependencies and detect changes.

### Handling errors and failures

Providers should report meaningful error messages. It’s important to handle transient failures and make operations [idempotent](https://en.wikipedia.org/wiki/Idempotence) to avoid inconsistent states.

### The provider schema

A provider schema defines the resources, their input and output properties, data sources, and configuration options. This schema enables Pulumi to generate SDKs for multiple languages and ensures consistency across them, as well as providing documentation.

{{% notes type="info" %}}

Historically it was necessary to hand-author and maintain the `schema.json` file that accompanied your provider implementation, however, now most of this is handled on-the-fly by the [Pulumi Provider SDK](/docs/iac/using-pulumi/extending-pulumi/pulumi-provider-sdk/) and the file is no longer necessary.

{{% /notes %}}

## Language support and the Pulumi Provider SDK

Pulumi providers can be written in Go, TypeScript, .NET, and Java, and used in any Pulumi program, in any supported language. The [Pulumi Provider SDK](/docs/iac/using-pulumi/extending-pulumi/pulumi-provider-sdk/) is a framework for building providers in Go. We strongly recommend using the SDK, as it is the most full-featured and streamlined way to create a new provider.

Some advantages of using the Pulumi Provider SDK:

- **Minimal Code Required**: You define your resource types and implementation using Go structs and methods, and the SDK handles the rest (RPC, auto-generated schema for multi-language support, etc).
- **Includes a Testing Framework**: Testing custom providers is made much easier with the SDK's built-in testing framework.
- **Middleware Support**: Enhances providers with layers like token dispatch, schema generation, and cancellation propagation.

## Example: Build a custom `file` provider

Let's walk through the implementation of an example provider using the Pulumi Provider SDK. The [`file` provider](https://github.com/pulumi/pulumi-go-provider/blob/main/examples/file/main.go) will demonstrate how to manage local files as resources within Pulumi. It is a minimal but powerful illustration of the provider development process.

### Features of the `file` provider

The `file` provider can be used to create and modify a local file. Here's an example of how to use it in a Pulumi program:

```yaml
resources:
  managedFile:
    type: file:File
    properties:
      path: ${pulumi.cwd}/managed.txt
      content: |
        An important piece of information
```

In this example, we create a new resource called `managedFile` of type `file:File`. We can specify the path to write it to, and the contents that should be in it. During an update, Pulumi will use the `file` provider to ensure the file exists and has the specified contents.

Now let's create the `file` provider that implements this.

### Set up the project

Since the provider is a separate code project from your Pulumi programs, the first step is to create a new directory for the provider code.

```sh
$ mkdir file-provider
$ cd file-provider
```

#### Create `go.mod` file

The `go.mod` file defines the Go project. It sets up the name of the Go module, the runtime requirements, and the module dependencies. We need the Pulumi Provider SDK (aka `github.com/pulumi/pulumi-go-provider`) as well as the standard Pulumi SDK (aka `github.com/pulumi/pulumi/sdk/v3`).

***Example**: `go.mod`*

```go
module example.com/file-provider

go 1.24

toolchain go1.24.0

require (
	github.com/pulumi/pulumi-go-provider v1.0.0
	github.com/pulumi/pulumi/sdk/v3 v3.167.0
)
```

Once that file is created, download the dependencies using `go get`:

```sh
$ go get example.com/file-provider
```

#### Create `PulumiPlugin.yaml` file

The only other file you'll need is the `PulumiPlugin.yaml` file. This tells Pulumi two things: that this code can be loaded as a provider plugin, and what runtime environment to use for that.

***Example:** `PulumiPlugin.yaml`*

```yaml
runtime: go
```

### Implement the interface

To implement the provider, first create a file called `main.go` with the following contents:

***Example:** `main.go`*

```go
package main

import (
	"context"
	"fmt"
	"os"

	p "github.com/pulumi/pulumi-go-provider"
	"github.com/pulumi/pulumi-go-provider/infer"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"
	"github.com/pulumi/pulumi/sdk/v3/go/property"
)

func main() {
	err := p.RunProvider("file", "0.1.0", provider())
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: %s", err.Error())
		os.Exit(1)
	}
}

func provider() p.Provider {
	return infer.Provider(infer.Options{
		Resources: []infer.InferredResource{infer.Resource[*File]()},
		ModuleMap: map[tokens.ModuleName]tokens.ModuleName{
			"file": "index",
		},
	})
}

type File struct{}

var _ = (infer.CustomDelete[FileState])((*File)(nil))
var _ = (infer.CustomCheck[FileArgs])((*File)(nil))
var _ = (infer.CustomUpdate[FileArgs, FileState])((*File)(nil))
var _ = (infer.CustomDiff[FileArgs, FileState])((*File)(nil))
var _ = (infer.CustomRead[FileArgs, FileState])((*File)(nil))
var _ = (infer.ExplicitDependencies[FileArgs, FileState])((*File)(nil))
var _ = (infer.Annotated)((*File)(nil))
var _ = (infer.Annotated)((*FileArgs)(nil))
var _ = (infer.Annotated)((*FileState)(nil))

func (f *File) Annotate(a infer.Annotator) {
	a.Describe(&f, "A file projected into a pulumi resource")
}

type FileArgs struct {
	Path    string `pulumi:"path,optional"`
	Force   bool   `pulumi:"force,optional"`
	Content string `pulumi:"content"`
}

func (f *FileArgs) Annotate(a infer.Annotator) {
	a.Describe(&f.Content, "The content of the file.")
	a.Describe(&f.Force, "If an already existing file should be deleted if it exists.")
	a.Describe(&f.Path, "The path of the file. This defaults to the name of the pulumi resource.")
}

type FileState struct {
	Path    string `pulumi:"path"`
	Force   bool   `pulumi:"force"`
	Content string `pulumi:"content"`
}

func (f *FileState) Annotate(a infer.Annotator) {
	a.Describe(&f.Content, "The content of the file.")
	a.Describe(&f.Force, "If an already existing file should be deleted if it exists.")
	a.Describe(&f.Path, "The path of the file.")
}

func (*File) Create(ctx context.Context, req infer.CreateRequest[FileArgs]) (resp infer.CreateResponse[FileState], err error) {
	if !req.Inputs.Force {
		_, err := os.Stat(req.Inputs.Path)
		if !os.IsNotExist(err) {
			return resp, fmt.Errorf("file already exists; pass force=true to override")
		}
	}

	if req.Preview { // Don't do the actual creating if in preview
		return infer.CreateResponse[FileState]{ID: req.Inputs.Path}, nil
	}

	f, err := os.Create(req.Inputs.Path)
	if err != nil {
		return resp, err
	}
	defer f.Close()
	n, err := f.WriteString(req.Inputs.Content)
	if err != nil {
		return resp, err
	}
	if n != len(req.Inputs.Content) {
		return resp, fmt.Errorf("only wrote %d/%d bytes", n, len(req.Inputs.Content))
	}
	return infer.CreateResponse[FileState]{
		ID: req.Inputs.Path,
		Output: FileState{
			Path:    req.Inputs.Path,
			Force:   req.Inputs.Force,
			Content: req.Inputs.Content,
		},
	}, nil
}

func (*File) Delete(ctx context.Context, req infer.DeleteRequest[FileState]) (infer.DeleteResponse, error) {
	err := os.Remove(req.State.Path)
	if os.IsNotExist(err) {
		p.GetLogger(ctx).Warningf("file %q already deleted", req.State.Path)
		err = nil
	}
	return infer.DeleteResponse{}, err
}

func (*File) Check(ctx context.Context, req infer.CheckRequest) (infer.CheckResponse[FileArgs], error) {
	if _, ok := req.NewInputs.GetOk("path"); !ok {
		req.NewInputs = req.NewInputs.Set("path", property.New(req.Name))
	}
	args, f, err := infer.DefaultCheck[FileArgs](ctx, req.NewInputs)

	return infer.CheckResponse[FileArgs]{
		Inputs:   args,
		Failures: f,
	}, err
}

func (*File) Update(ctx context.Context, req infer.UpdateRequest[FileArgs, FileState]) (infer.UpdateResponse[FileState], error) {
	if !req.Preview && req.State.Content != req.Inputs.Content {
		f, err := os.Create(req.State.Path)
		if err != nil {
			return infer.UpdateResponse[FileState]{}, err
		}
		defer f.Close()
		n, err := f.WriteString(req.Inputs.Content)
		if err != nil {
			return infer.UpdateResponse[FileState]{}, err
		}
		if n != len(req.Inputs.Content) {
			return infer.UpdateResponse[FileState]{}, fmt.Errorf("only wrote %d/%d bytes", n, len(req.Inputs.Content))
		}
	}

	return infer.UpdateResponse[FileState]{
		Output: FileState{
			Path:    req.Inputs.Path,
			Force:   req.Inputs.Force,
			Content: req.Inputs.Content,
		},
	}, nil

}

func (*File) Diff(ctx context.Context, req infer.DiffRequest[FileArgs, FileState]) (infer.DiffResponse, error) {
	diff := map[string]p.PropertyDiff{}
	if req.Inputs.Content != req.State.Content {
		diff["content"] = p.PropertyDiff{Kind: p.Update}
	}
	if req.Inputs.Force != req.State.Force {
		diff["force"] = p.PropertyDiff{Kind: p.Update}
	}
	if req.Inputs.Path != req.State.Path {
		diff["path"] = p.PropertyDiff{Kind: p.UpdateReplace}
	}
	return infer.DiffResponse{
		DeleteBeforeReplace: true,
		HasChanges:          len(diff) > 0,
		DetailedDiff:        diff,
	}, nil
}

func (*File) Read(ctx context.Context, req infer.ReadRequest[FileArgs, FileState]) (infer.ReadResponse[FileArgs, FileState], error) {
	path := req.ID
	byteContent, err := os.ReadFile(path)
	if err != nil {
		return infer.ReadResponse[FileArgs, FileState]{}, err
	}
	content := string(byteContent)
	return infer.ReadResponse[FileArgs, FileState]{
		ID: path,
		Inputs: FileArgs{
			Path:    path,
			Force:   req.Inputs.Force && req.State.Force,
			Content: content,
		},
		State: FileState{
			Path:    path,
			Force:   req.Inputs.Force && req.State.Force,
			Content: content,
		},
	}, nil
}

func (*File) WireDependencies(f infer.FieldSelector, args *FileArgs, state *FileState) {
	f.OutputField(&state.Content).DependsOn(f.InputField(&args.Content))
	f.OutputField(&state.Force).DependsOn(f.InputField(&args.Force))
	f.OutputField(&state.Path).DependsOn(f.InputField(&args.Path))
}
```

We'll go through this code in detail in a moment, but for now, let's give it a try in a Pulumi program.

### Use the provider in a Pulumi program

First, create a Pulumi program that uses our new provider:

```sh
$ cd ..
$ mkdir use-file-provider
$ cd use-file-provider
$ pulumi new yaml
```

This will initiatize a minimal YAML program. Let's modify the default YAML file:

***Example:** The `Pulumi.yaml` file*

```yaml
name: use-file-provider
runtime: yaml

plugins:
  providers:
    - name: file
      path: ../file-provider

resources:
  managedFile:
    type: file:File
    properties:
      path: ${pulumi.cwd}/managed.txt
      content: |
        An important piece of information
```

Save that and then run `pulumi up`:

```sh
$ pulumi up
...

     Type                 Name                   Status
 +   pulumi:pulumi:Stack  use-file-provider-dev  created (2s)
 +   └─ file:index:File   managedFile            created (0.06s)

Resources:
    + 2 created
```

If all went well, you should see a new file created called `managed.txt` with the contents `An important piece of information`.

You can verify this using `cat`:

```sh
$ cat managed.txt
An important piece of information
```

### Detailed breakdown of provider implementation

#### Preample and dependencies

Like any other Go langauge module, you start with a `package` declaration and and `import` block. Here we are adding a few important packages from the base library (`context`, `fmt`, and `os`) which will help us with file operations, and a selection of imports from the Pulumi Provider SDK.

```go
package main

import (
	"context"
	"fmt"
	"os"

	p "github.com/pulumi/pulumi-go-provider"
	"github.com/pulumi/pulumi-go-provider/infer"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"
	"github.com/pulumi/pulumi/sdk/v3/go/property"
)
```

#### Provider entrypoint and indentity definitions

The next section involves defining the `main()` entrypoint function and the `provider()` constructor.

The entry point uses `p.RunProvider(...)` to launch the provider process. It takes as arguments the name of the provider, version, and the provider instance itself. The provider instance is returned from the `provider()` constructor. Note that the name and version here will be what your end-user sees in the Pulumi program and should be unique to avoid confusion.

The constructor uses `infer.Provider(...)` with an options struct that lists the types of the new Pulumi resources that this provider will export. The `ModuleMap` defines the namespace for these resource types. Note that the `index` portion of this definition isn't used when the user declares a resources. In this example, we're exporting only one resource type: `file:File`.

```go
func main() {
	err := p.RunProvider("file", "0.1.0", provider())
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: %s", err.Error())
		os.Exit(1)
	}
}

func provider() p.Provider {
	return infer.Provider(infer.Options{
		Resources: []infer.InferredResource{infer.Resource[*File]()},
		ModuleMap: map[tokens.ModuleName]tokens.ModuleName{
			"file": "index",
		},
	})
}
```

#### Define the `File` resource and implement the provider interface

Next, lets define the `File` resource. Start with a simple empty struct to define the type. Then add the `infer` declarations that will allow the provider SDK to work with the resource.

Here we are letting the SDK know that we have implemented `Check`, `Read`, `Update`, `Delete`, and `Diff`. The `ExplicitDependencies` call lets the SDK know we have defined our own `WireDependencies`. Finally, we add a description to the resource using `Annotate`.  

```go
type File struct{}

var _ = (infer.CustomDelete[FileState])((*File)(nil))
var _ = (infer.CustomCheck[FileArgs])((*File)(nil))
var _ = (infer.CustomUpdate[FileArgs, FileState])((*File)(nil))
var _ = (infer.CustomDiff[FileArgs, FileState])((*File)(nil))
var _ = (infer.CustomRead[FileArgs, FileState])((*File)(nil))
var _ = (infer.ExplicitDependencies[FileArgs, FileState])((*File)(nil))
var _ = (infer.Annotated)((*File)(nil))
var _ = (infer.Annotated)((*FileArgs)(nil))
var _ = (infer.Annotated)((*FileState)(nil))

func (f *File) Annotate(a infer.Annotator) {
	a.Describe(&f, "A file projected into a pulumi resource")
}
```

#### Define the resource arguments

Every resource needs to define the arguments used to configure it. These are done in a separate arguments type. Here we define the file path, contents, and if an existing file should be overwritten or not.

In the struct we use tags prefixed with `pulumi:` to define the language-neutral argument names. This is an important part of the Pulumi developer experience for the users of your provider. We advise using [camelCase](https://en.wikipedia.org/wiki/Camel_case) naming to provide a consistent experience across all of Pulumi's authoring languages. This is also where you can indicate if an argument is optional.

After defining the arguments, describe them using the `Annotator` from the `infer` library. This will provide context-sensitive information to developers when authoring in Pulumi with your provider.

```go
type FileArgs struct {
	Path    string `pulumi:"path,optional"`
	Force   bool   `pulumi:"force,optional"`
	Content string `pulumi:"content"`
}

func (f *FileArgs) Annotate(a infer.Annotator) {
	a.Describe(&f.Content, "The content of the file.")
	a.Describe(&f.Force, "If an already existing file should be deleted if it exists.")
	a.Describe(&f.Path, "The path of the file. This defaults to the name of the pulumi resource.")
}
```

#### Define the resource state

A resource needs to declare and manage its own state within Pulumi, so that Pulumi knows when to perform the create or update operations. Here we define a `FileState` type that indicates the necessary fields to manage. In this case, the state is very similar to the creation arguments, but this may not always be the case.

As before, the tags in the struct specify the language-neutral property name to store, and we provide descriptions via annotations.

```go
type FileState struct {
	Path    string `pulumi:"path"`
	Force   bool   `pulumi:"force"`
	Content string `pulumi:"content"`
}

func (f *FileState) Annotate(a infer.Annotator) {
	a.Describe(&f.Content, "The content of the file.")
	a.Describe(&f.Force, "If an already existing file should be deleted if it exists.")
	a.Describe(&f.Path, "The path of the file.")
}
```

#### Implement the resource CRUD operations

Here's where the business logic of the resource operations happens. In this example, we are going to implement the full interface, with custom implementations for `Create`, `Read`, `Update`, `Delete`, `Check`, and `Diff`. However, the Pulumi Provider SDK provides default implementations for all of these functions other than `Create`, so in many cases, you may only need to implement one or two of these functions to meet your business goals.

##### The `Create` operation

The `Create` operation handles the logic of determining if the resource exists or not, and if not, it creates it using the provided argument context. In many providers this is where you would interact with external cloud APIs, databases, and other systems. In this example, we're going to interact with our local filesystem using calls to Go's `os` library.

First, we check to see if the user configured the `force` option. We can access that through the `req.Inputs` collection, which is will be an instance of `FileArgs`. If `force` is true, we don't need to check to see if the file exists, otherwise, use `os.Stat` and `os.IsNotExist` to see if the specified directory and filename already exist. If it does, we exist early with an error. This will let Pulumi know that the create operation failed, and it will be propogated up to the end user via the console/log output.

To return an error, we return a null `CreateResponse` instance with an error string. The Provider SDK functions use a request and response pattern for each operation, parameterized by the argument and state types. The next piece of logic checks `req.Preview` to see if we are in a *preview* mode or an *update* mode. If we are in preview mode, don't take any actions that would mutate the state and just return early.

Now we can implement the core logic of writing to the filesystem using the base library functions.

Finally, the last thing to do is construct the response object for the Create operation, setting the unique ID for the resource, and the new resource state values as outputs. Returning that response object without errors lets the Pulumi engine know that this operation was successful. Recording the state will be handled by the Pulumi engine.

```go
func (*File) Create(ctx context.Context, req infer.CreateRequest[FileArgs]) (resp infer.CreateResponse[FileState], err error) {
	if !req.Inputs.Force {
		_, err := os.Stat(req.Inputs.Path)
		if !os.IsNotExist(err) {
			return resp, fmt.Errorf("file already exists; pass force=true to override")
		}
	}

	if req.Preview { // Don't do the actual creating if in preview
		return infer.CreateResponse[FileState]{ID: req.Inputs.Path}, nil
	}

	f, err := os.Create(req.Inputs.Path)
	if err != nil {
		return resp, err
	}
	defer f.Close()
	n, err := f.WriteString(req.Inputs.Content)
	if err != nil {
		return resp, err
	}
	if n != len(req.Inputs.Content) {
		return resp, fmt.Errorf("only wrote %d/%d bytes", n, len(req.Inputs.Content))
	}
	return infer.CreateResponse[FileState]{
		ID: req.Inputs.Path,
		Output: FileState{
			Path:    req.Inputs.Path,
			Force:   req.Inputs.Force,
			Content: req.Inputs.Content,
		},
	}, nil
}
```

##### The `Delete` operation

The `Delete` operation removes a resource safely. This operation follows a similar pattern to `Create`, but instead of a `CreateRequest`/`CreateResponse` we have `DeleteRequest`/`DeleteResponse`.

One new concept inroduced in this example function is the use of the Pulumi logger. Calling `p.GetLogger(ctx)` gets you a logger with a familiar interface. This is how you might pass informational messages and warnings to the user without throwing an error.

```go
func (*File) Delete(ctx context.Context, req infer.DeleteRequest[FileState]) (infer.DeleteResponse, error) {
	err := os.Remove(req.State.Path)
	if os.IsNotExist(err) {
		p.GetLogger(ctx).Warningf("file %q already deleted", req.State.Path)
		err = nil
	}
	return infer.DeleteResponse{}, err
}
```

##### The `Check` operation

The `Check` operation is used to validate the inputs to a resource, including logic for setting sensible defaults or otherwise mutating the inputs before they are passed to the other functions.

```go
func (*File) Check(ctx context.Context, req infer.CheckRequest) (infer.CheckResponse[FileArgs], error) {
	if _, ok := req.NewInputs.GetOk("path"); !ok {
		req.NewInputs = req.NewInputs.Set("path", property.New(req.Name))
	}
	args, f, err := infer.DefaultCheck[FileArgs](ctx, req.NewInputs)

	return infer.CheckResponse[FileArgs]{
		Inputs:   args,
		Failures: f,
	}, err
}
```

##### The `Update` operation

The `Update` operation modifies the resource with new values. After checking to see if we are in a preview mode of not, and that the input contents are different than the recorded state of the content, we overwrite the file with the new contents.

```go
func (*File) Update(ctx context.Context, req infer.UpdateRequest[FileArgs, FileState]) (infer.UpdateResponse[FileState], error) {
	if !req.Preview && req.State.Content != req.Inputs.Content {
		f, err := os.Create(req.State.Path)
		if err != nil {
			return infer.UpdateResponse[FileState]{}, err
		}
		defer f.Close()
		n, err := f.WriteString(req.Inputs.Content)
		if err != nil {
			return infer.UpdateResponse[FileState]{}, err
		}
		if n != len(req.Inputs.Content) {
			return infer.UpdateResponse[FileState]{}, fmt.Errorf("only wrote %d/%d bytes", n, len(req.Inputs.Content))
		}
	}

	return infer.UpdateResponse[FileState]{
		Output: FileState{
			Path:    req.Inputs.Path,
			Force:   req.Inputs.Force,
			Content: req.Inputs.Content,
		},
	}, nil

}
```

##### The `Diff` operation

The `Diff` operation compares a resource's recorded state (if any) to the current input values for the resource, to determine what kind of changes need to be made. The `diff` object is a map of property names to the kind of diff operation (if any) that a property needs to have made. The logic of this function is straightforward: compare `req.Inputs.<propertyName>` to `req.State.<propertyName>` and if they aren't equal, add to the diff that this property needs to be updated using `p.PropertyDiff{Kind: p.Update}`. Only include the properties that need to change in the `diff` map. Finally return a `DiffResponse` containing the `diff` map, and set a few other options to configure the update behavior.

```go
func (*File) Diff(ctx context.Context, req infer.DiffRequest[FileArgs, FileState]) (infer.DiffResponse, error) {
	diff := map[string]p.PropertyDiff{}
	if req.Inputs.Content != req.State.Content {
		diff["content"] = p.PropertyDiff{Kind: p.Update}
	}
	if req.Inputs.Force != req.State.Force {
		diff["force"] = p.PropertyDiff{Kind: p.Update}
	}
	if req.Inputs.Path != req.State.Path {
		diff["path"] = p.PropertyDiff{Kind: p.UpdateReplace}
	}
	return infer.DiffResponse{
		DeleteBeforeReplace: true,
		HasChanges:          len(diff) > 0,
		DetailedDiff:        diff,
	}, nil
}
```

#### The `Read` operation

The `Read` operation fetches the resource. The `ReadRequest` has a `ID` property that can be used, in this case, to determine the path to the file, and the base library functions can be used to read the file from disk, populating the `Content` field.

```go
func (*File) Read(ctx context.Context, req infer.ReadRequest[FileArgs, FileState]) (infer.ReadResponse[FileArgs, FileState], error) {
	path := req.ID
	byteContent, err := os.ReadFile(path)
	if err != nil {
		return infer.ReadResponse[FileArgs, FileState]{}, err
	}
	content := string(byteContent)
	return infer.ReadResponse[FileArgs, FileState]{
		ID: path,
		Inputs: FileArgs{
			Path:    path,
			Force:   req.Inputs.Force && req.State.Force,
			Content: content,
		},
		State: FileState{
			Path:    path,
			Force:   req.Inputs.Force && req.State.Force,
			Content: content,
		},
	}, nil
}
```

#### Managing resource output fields

Finally, `WireDependencies` defines the outputs that are made available on the resource, logically connecting the inputs and stored state values.

```go
func (*File) WireDependencies(f infer.FieldSelector, args *FileArgs, state *FileState) {
	f.OutputField(&state.Content).DependsOn(f.InputField(&args.Content))
	f.OutputField(&state.Force).DependsOn(f.InputField(&args.Force))
	f.OutputField(&state.Path).DependsOn(f.InputField(&args.Path))
}
```

<!-- TODO: write this section

### Testing with the SDK

 -->

### Multi-language support

In our above example, we created a provider in Go and used it in YAML. This "just works" by default. However, if you would like to use your provider from the other Pulumi authoring langauges (e.g. TypeScript, Python, Java, Go, C#) it will be necessary to generate SDKs for each target language.

That is a very streamlined process with the Pulumi Provider SDK. The following command will generate language SDKs for all supported languages:

```sh
pulumi package gen-sdk <path-to-provider>
```

See [`pulumi package gen-sdk --help`](/docs/iac/cli/commands/pulumi_package_gen-sdk/) for more options.

{{% notes type="info" %}}

Historically, Pulumi providers required a `schema.json` file. This is now generated on the fly by the Pulumi Provider SDK and so you don't need to have this file on disk to use the provider. If you would like to do so, e.g., for debugging purposes, you can use [`pulumi package get-schema <path-to-provider>`](/docs/iac/cli/commands/pulumi_package_get-schema/).

{{% /notes %}}

<!-- TODO: Add example of using the file provider in all target languages in a chooser. -->

## Packaging and publishing

Using a provider from another directory on your local filesystem is the easiest way to develop a new custom provider. However, once you're ready to share with others at your company, or with the world, you'll need to explore how to publish and package your provider for consumption. There are many ways to accomplish this, from hosting either publicly or privately in GitHub and GitLab, using a private registry within Pulumi Cloud, or publishing to the public Pulumi registry.

See the [Pulumi package authoring guide](/docs/iac/using-pulumi/pulumi-packages/authoring/) for full details.

<!-- TODO: write this section

## Considerations, Gotchas, and FAQs

 -->
