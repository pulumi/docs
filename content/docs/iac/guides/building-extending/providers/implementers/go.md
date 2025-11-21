---
title_tag: "Implement a provider in Go"
meta_desc: "Build a Pulumi provider in Go using the gRPC bindings directly, without the higher-level SDK."
title: Implement a provider in Go
h1: Implement a provider in Go
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Go
        parent: iac-guides-provider-implementers
        weight: 30
---

This guide shows how to implement a Pulumi provider in Go using the gRPC bindings directly, without the [Pulumi Go Provider SDK](/docs/iac/guides/building-extending/providers/sdks/pulumi-go-provider-sdk/). This approach gives you full control over provider behavior and schema definition.

{{% notes type="info" %}}
For most Go providers, the [Pulumi Go Provider SDK](/docs/iac/guides/building-extending/providers/sdks/pulumi-go-provider-sdk/) provides a more ergonomic experience with schema inference and less boilerplate. Use this direct approach when you need precise control over the protocol or want to understand exactly how providers work.
{{% /notes %}}

## Prerequisites

You'll need Go 1.21 or later, and a basic understanding of the [provider protocol](/docs/iac/guides/building-extending/providers/implementers/protocol-reference/).

## Project structure

```
my-provider/
├── main.go                   # Entry point and gRPC server
├── provider.go               # Provider implementation
├── schema.json               # Provider schema
├── go.mod
└── go.sum
```

## Step 1: Set up the project

Create your project directory and initialize the Go module:

```bash
mkdir my-provider && cd my-provider
go mod init github.com/your-org/pulumi-myfiles
```

Add the required dependencies:

```bash
go get github.com/pulumi/pulumi/sdk/v3
go get google.golang.org/grpc
go get google.golang.org/protobuf
```

## Step 2: Write the schema

Create `schema.json`. This example defines a simple `File` resource:

```json
{
    "name": "myfiles",
    "displayName": "My Files Provider",
    "version": "0.1.0",
    "description": "A provider for managing local files",
    "keywords": ["pulumi", "files"],
    "publisher": "your-org",
    "config": {},
    "provider": {
        "description": "The provider configuration."
    },
    "resources": {
        "myfiles:index:File": {
            "description": "A file managed by Pulumi.",
            "inputProperties": {
                "path": {
                    "type": "string",
                    "description": "The path where the file will be created."
                },
                "content": {
                    "type": "string",
                    "description": "The content of the file."
                },
                "force": {
                    "type": "boolean",
                    "description": "Overwrite existing files.",
                    "default": false
                }
            },
            "requiredInputs": ["path", "content"],
            "properties": {
                "path": {
                    "type": "string",
                    "description": "The path of the file."
                },
                "content": {
                    "type": "string",
                    "description": "The content of the file."
                },
                "force": {
                    "type": "boolean",
                    "description": "Whether existing files are overwritten."
                }
            },
            "required": ["path", "content", "force"]
        }
    }
}
```

## Step 3: Implement the provider

Create `provider.go`:

```go
package main

import (
	"context"
	_ "embed"
	"os"

	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource/plugin"
	rpc "github.com/pulumi/pulumi/sdk/v3/proto/go"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
	"google.golang.org/protobuf/types/known/emptypb"
	"google.golang.org/protobuf/types/known/structpb"
)

//go:embed schema.json
var schema string

type myFilesProvider struct {
	rpc.UnimplementedResourceProviderServer
}

func (p *myFilesProvider) GetPluginInfo(ctx context.Context, req *emptypb.Empty) (*rpc.PluginInfo, error) {
	return &rpc.PluginInfo{
		Version: "0.1.0",
	}, nil
}

func (p *myFilesProvider) GetSchema(ctx context.Context, req *rpc.GetSchemaRequest) (*rpc.GetSchemaResponse, error) {
	return &rpc.GetSchemaResponse{
		Schema: schema,
	}, nil
}

func (p *myFilesProvider) Configure(ctx context.Context, req *rpc.ConfigureRequest) (*rpc.ConfigureResponse, error) {
	return &rpc.ConfigureResponse{
		AcceptSecrets:   true,
		SupportsPreview: true,
	}, nil
}

func (p *myFilesProvider) CheckConfig(ctx context.Context, req *rpc.CheckRequest) (*rpc.CheckResponse, error) {
	return &rpc.CheckResponse{Inputs: req.News}, nil
}

func (p *myFilesProvider) DiffConfig(ctx context.Context, req *rpc.DiffRequest) (*rpc.DiffResponse, error) {
	return &rpc.DiffResponse{}, nil
}

func (p *myFilesProvider) Check(ctx context.Context, req *rpc.CheckRequest) (*rpc.CheckResponse, error) {
	inputs := req.News.AsMap()
	failures := []*rpc.CheckFailure{}

	if _, ok := inputs["path"]; !ok {
		failures = append(failures, &rpc.CheckFailure{
			Property: "path",
			Reason:   "path is required",
		})
	}

	if _, ok := inputs["content"]; !ok {
		failures = append(failures, &rpc.CheckFailure{
			Property: "content",
			Reason:   "content is required",
		})
	}

	// Set defaults
	if _, ok := inputs["force"]; !ok {
		inputs["force"] = false
	}

	result, err := structpb.NewStruct(inputs)
	if err != nil {
		return nil, err
	}

	return &rpc.CheckResponse{
		Inputs:   result,
		Failures: failures,
	}, nil
}

func (p *myFilesProvider) Diff(ctx context.Context, req *rpc.DiffRequest) (*rpc.DiffResponse, error) {
	olds := req.Olds.AsMap()
	news := req.News.AsMap()

	var diffs []string
	var replaces []string
	detailedDiff := map[string]*rpc.PropertyDiff{}

	if olds["content"] != news["content"] {
		diffs = append(diffs, "content")
		detailedDiff["content"] = &rpc.PropertyDiff{Kind: rpc.PropertyDiff_UPDATE}
	}

	if olds["force"] != news["force"] {
		diffs = append(diffs, "force")
		detailedDiff["force"] = &rpc.PropertyDiff{Kind: rpc.PropertyDiff_UPDATE}
	}

	if olds["path"] != news["path"] {
		diffs = append(diffs, "path")
		replaces = append(replaces, "path")
		detailedDiff["path"] = &rpc.PropertyDiff{Kind: rpc.PropertyDiff_UPDATE_REPLACE}
	}

	changes := rpc.DiffResponse_DIFF_NONE
	if len(diffs) > 0 {
		changes = rpc.DiffResponse_DIFF_SOME
	}

	return &rpc.DiffResponse{
		Changes:             changes,
		Diffs:               diffs,
		Replaces:            replaces,
		DetailedDiff:        detailedDiff,
		HasDetailedDiff:     true,
		DeleteBeforeReplace: true,
	}, nil
}

func (p *myFilesProvider) Create(ctx context.Context, req *rpc.CreateRequest) (*rpc.CreateResponse, error) {
	inputs := req.Properties.AsMap()
	path := inputs["path"].(string)
	content := inputs["content"].(string)
	force, _ := inputs["force"].(bool)

	// During preview, don't create the file
	if req.Preview {
		result, _ := structpb.NewStruct(inputs)
		return &rpc.CreateResponse{
			Id:         path,
			Properties: result,
		}, nil
	}

	// Check if file exists
	if _, err := os.Stat(path); err == nil && !force {
		return nil, status.Errorf(codes.AlreadyExists,
			"file already exists at %s; set force=true to overwrite", path)
	}

	// Write the file
	if err := os.WriteFile(path, []byte(content), 0644); err != nil {
		return nil, status.Errorf(codes.Internal, "failed to write file: %v", err)
	}

	result, _ := structpb.NewStruct(inputs)
	return &rpc.CreateResponse{
		Id:         path,
		Properties: result,
	}, nil
}

func (p *myFilesProvider) Read(ctx context.Context, req *rpc.ReadRequest) (*rpc.ReadResponse, error) {
	path := req.Id

	data, err := os.ReadFile(path)
	if os.IsNotExist(err) {
		// Resource no longer exists
		return &rpc.ReadResponse{}, nil
	}
	if err != nil {
		return nil, status.Errorf(codes.Internal, "failed to read file: %v", err)
	}

	oldInputs := req.Inputs.AsMap()
	force, _ := oldInputs["force"].(bool)

	state := map[string]interface{}{
		"path":    path,
		"content": string(data),
		"force":   force,
	}

	result, _ := structpb.NewStruct(state)
	return &rpc.ReadResponse{
		Id:         path,
		Properties: result,
		Inputs:     result,
	}, nil
}

func (p *myFilesProvider) Update(ctx context.Context, req *rpc.UpdateRequest) (*rpc.UpdateResponse, error) {
	inputs := req.News.AsMap()
	path := inputs["path"].(string)
	content := inputs["content"].(string)

	// During preview, don't update the file
	if req.Preview {
		result, _ := structpb.NewStruct(inputs)
		return &rpc.UpdateResponse{
			Properties: result,
		}, nil
	}

	// Write the updated content
	if err := os.WriteFile(path, []byte(content), 0644); err != nil {
		return nil, status.Errorf(codes.Internal, "failed to write file: %v", err)
	}

	result, _ := structpb.NewStruct(inputs)
	return &rpc.UpdateResponse{
		Properties: result,
	}, nil
}

func (p *myFilesProvider) Delete(ctx context.Context, req *rpc.DeleteRequest) (*emptypb.Empty, error) {
	path := req.Id

	if err := os.Remove(path); err != nil && !os.IsNotExist(err) {
		return nil, status.Errorf(codes.Internal, "failed to delete file: %v", err)
	}

	return &emptypb.Empty{}, nil
}

func (p *myFilesProvider) Cancel(ctx context.Context, req *emptypb.Empty) (*emptypb.Empty, error) {
	return &emptypb.Empty{}, nil
}
```

## Step 4: Create the entry point

Create `main.go`:

```go
package main

import (
	"fmt"
	"net"
	"os"

	rpc "github.com/pulumi/pulumi/sdk/v3/proto/go"
	"google.golang.org/grpc"
)

func main() {
	// Listen on a random available port
	listener, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		fmt.Fprintf(os.Stderr, "failed to listen: %v\n", err)
		os.Exit(1)
	}

	// Create gRPC server
	server := grpc.NewServer()
	rpc.RegisterResourceProviderServer(server, &myFilesProvider{})

	// Print the port for Pulumi to connect
	port := listener.Addr().(*net.TCPAddr).Port
	fmt.Printf("%d\n", port)

	// Serve
	if err := server.Serve(listener); err != nil {
		fmt.Fprintf(os.Stderr, "failed to serve: %v\n", err)
		os.Exit(1)
	}
}
```

## Step 5: Build the provider

Build the provider binary:

```bash
go build -o pulumi-resource-myfiles .
```

The binary name must follow the pattern `pulumi-resource-<provider-name>`.

## Step 6: Test the provider

Create a test Pulumi program:

```bash
mkdir ../test-myfiles && cd ../test-myfiles
pulumi new yaml
```

Update the `Pulumi.yaml`:

```yaml
name: test-myfiles
runtime: yaml

plugins:
  providers:
    - name: myfiles
      path: ../my-provider

resources:
  testFile:
    type: myfiles:index:File
    properties:
      path: ${pulumi.cwd}/test.txt
      content: |
        Hello from my Go provider!
```

Run the program:

```bash
pulumi up
```

You should see the file created at `test.txt`.

## Dispatching to multiple resources

The example above shows a single resource type. Real providers typically have many resources and need to dispatch to the correct implementation based on the type token extracted from the URN.

The URN format is `urn:pulumi:<stack>::<project>::<type>::<name>`, where `<type>` is the resource type token like `myfiles:index:File`.

```go
func getTypeFromURN(urn string) string {
	// URN format: urn:pulumi:<stack>::<project>::<type>::<name>
	parts := strings.Split(urn, "::")
	if len(parts) >= 3 {
		return parts[2]
	}
	return ""
}

func (p *myFilesProvider) Create(ctx context.Context, req *rpc.CreateRequest) (*rpc.CreateResponse, error) {
	resourceType := getTypeFromURN(req.Urn)

	switch resourceType {
	case "myfiles:index:File":
		return p.createFile(ctx, req)
	case "myfiles:index:Directory":
		return p.createDirectory(ctx, req)
	default:
		return nil, status.Errorf(codes.Unimplemented, "unknown resource type: %s", resourceType)
	}
}
```

Apply the same pattern to Check, Diff, Read, Update, and Delete.

## Working with property bags

Resource inputs and outputs are untyped property bags (`map[string]interface{}`). In production providers, you'll often want to deserialize these into typed structs for safer code, and serialize typed structs back to property bags for responses.

```go
type FileInputs struct {
	Path    string `json:"path"`
	Content string `json:"content"`
	Force   bool   `json:"force"`
}

func fileInputsFromMap(m map[string]interface{}) FileInputs {
	inputs := FileInputs{}
	if v, ok := m["path"].(string); ok {
		inputs.Path = v
	}
	if v, ok := m["content"].(string); ok {
		inputs.Content = v
	}
	if v, ok := m["force"].(bool); ok {
		inputs.Force = v
	}
	return inputs
}

func (f FileInputs) toMap() map[string]interface{} {
	return map[string]interface{}{
		"path":    f.Path,
		"content": f.Content,
		"force":   f.Force,
	}
}
```

The [Pulumi Go Provider SDK](/docs/iac/guides/building-extending/providers/sdks/pulumi-go-provider-sdk/) handles both dispatching and property bag serialization automatically based on Go struct definitions and tags.

## Advantages of Go

Go providers compile to standalone binaries with no runtime dependencies, making them easy to distribute. Users of your provider can consume it from any Pulumi language without installing Go or any other runtime.

## Next steps

For detailed method documentation, see the [Protocol reference](/docs/iac/guides/building-extending/providers/implementers/protocol-reference/). For the complete schema specification, see the [Schema reference](/docs/iac/guides/building-extending/packages/schema/). When you're ready to distribute your provider, see [Publishing packages](/docs/iac/guides/building-extending/packages/publishing-packages/).
