---
title_tag: "Implement a provider in Python"
meta_desc: "Build a Pulumi provider in Python using the gRPC bindings directly."
title: Implement a provider in Python
h1: Implement a provider in Python
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Python
        parent: iac-guides-provider-implementers
        weight: 20
---

This guide shows how to implement a Pulumi provider in Python using the gRPC bindings directly. This approach gives you full control over provider behavior and works with any Python version that supports gRPC.

{{% notes type="warning" %}}
This is an advanced guide for power users. You'll be working directly with the provider protocol, which requires understanding gRPC, Protocol Buffers, and Pulumi's provider semantics. If you're open to writing Go, the [Pulumi Go Provider SDK](/docs/iac/guides/building-extending/providers/sdks/pulumi-go-provider-sdk/) offers a more ergonomic experience with less boilerplate. [Dynamic providers](/docs/iac/concepts/resources/dynamic-providers/) can be useful for quick prototyping, but aren't suitable for production providers.
{{% /notes %}}

## Prerequisites

You'll need Python 3.8 or later, the `grpcio` and `grpcio-tools` packages, and a basic understanding of the [provider protocol](/docs/iac/guides/building-extending/providers/implementers/protocol-reference/).

## Project structure

```
my-provider/
├── provider/
│   ├── __init__.py
│   ├── __main__.py          # Entry point
│   └── server.py            # gRPC server implementation
├── pulumi-resource-myfiles   # Wrapper script (executable)
├── schema.json               # Provider schema
├── PulumiPlugin.yaml         # Plugin metadata
└── requirements.txt
```

## Step 1: Set up the project

Create your project directory and install dependencies:

```bash
mkdir my-provider && cd my-provider
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install pulumi grpcio
```

Create `requirements.txt`:

```text
pulumi>=3.0.0
grpcio>=1.50.0
```

The Pulumi Python SDK includes the generated Protocol Buffer and gRPC bindings, so you don't need to generate them yourself.

## Step 2: Create the plugin metadata

Create `PulumiPlugin.yaml`:

```yaml
runtime: python
```

## Step 3: Write the schema

Create `schema.json`. This example defines a simple `File` resource:

```json
{
    "name": "myfiles",
    "displayName": "My Files Provider",
    "version": "0.1.0",
    "description": "A provider for managing local files",
    "keywords": ["pulumi", "files"],
    "publisher": "your-org",
    "language": {
        "python": {
            "requires": {
                "pulumi": ">=3.0.0,<4.0.0"
            }
        }
    },
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

## Step 4: Implement the provider

Create `provider/__init__.py`:

```python
# Empty file to make this a package
```

Create `provider/server.py`:

```python
import os
import sys
import grpc
from concurrent import futures
from google.protobuf import struct_pb2, empty_pb2

from pulumi.runtime.proto import plugin_pb2, provider_pb2, provider_pb2_grpc


class MyFilesProvider(provider_pb2_grpc.ResourceProviderServicer):
    """A Pulumi provider for managing local files."""

    def __init__(self, schema_path: str):
        with open(schema_path, 'r') as f:
            self._schema = f.read()
        self._configured = False

    # -------------------------------------------------------------------------
    # Plugin info and configuration
    # -------------------------------------------------------------------------

    def GetPluginInfo(self, request, context):
        """Return plugin metadata."""
        return plugin_pb2.PluginInfo(version="0.1.0")

    def GetSchema(self, request, context):
        """Return the provider schema."""
        return provider_pb2.GetSchemaResponse(schema=self._schema)

    def Configure(self, request, context):
        """Initialize the provider with configuration."""
        # Store any configuration values here
        # For this simple provider, we don't need any configuration
        self._configured = True
        return provider_pb2.ConfigureResponse(
            acceptSecrets=True,
            supportsPreview=True,
            acceptResources=False,
            acceptOutputs=False,
        )

    def CheckConfig(self, request, context):
        """Validate provider configuration."""
        return provider_pb2.CheckResponse(inputs=request.news)

    def DiffConfig(self, request, context):
        """Diff provider configuration."""
        return provider_pb2.DiffResponse(changes=provider_pb2.DiffResponse.DIFF_NONE)

    # -------------------------------------------------------------------------
    # Resource operations
    # -------------------------------------------------------------------------

    def Check(self, request, context):
        """Validate resource inputs and set defaults."""
        inputs = self._struct_to_dict(request.news)

        # Validate required fields
        failures = []
        if 'path' not in inputs:
            failures.append(provider_pb2.CheckFailure(
                property='path',
                reason='path is required'
            ))
        if 'content' not in inputs:
            failures.append(provider_pb2.CheckFailure(
                property='content',
                reason='content is required'
            ))

        # Set defaults
        if 'force' not in inputs:
            inputs['force'] = False

        return provider_pb2.CheckResponse(
            inputs=self._dict_to_struct(inputs),
            failures=failures,
        )

    def Diff(self, request, context):
        """Compute differences between current and desired state."""
        olds = self._struct_to_dict(request.olds)
        news = self._struct_to_dict(request.news)

        diffs = []
        detailed_diff = {}
        replaces = []

        # Check each property for changes
        if olds.get('content') != news.get('content'):
            diffs.append('content')
            detailed_diff['content'] = provider_pb2.PropertyDiff(
                kind=provider_pb2.PropertyDiff.UPDATE
            )

        if olds.get('force') != news.get('force'):
            diffs.append('force')
            detailed_diff['force'] = provider_pb2.PropertyDiff(
                kind=provider_pb2.PropertyDiff.UPDATE
            )

        if olds.get('path') != news.get('path'):
            diffs.append('path')
            replaces.append('path')
            detailed_diff['path'] = provider_pb2.PropertyDiff(
                kind=provider_pb2.PropertyDiff.UPDATE_REPLACE
            )

        has_changes = provider_pb2.DiffResponse.DIFF_SOME if diffs else provider_pb2.DiffResponse.DIFF_NONE

        return provider_pb2.DiffResponse(
            changes=has_changes,
            diffs=diffs,
            replaces=replaces,
            detailedDiff=detailed_diff,
            hasDetailedDiff=True,
            deleteBeforeReplace=True,
        )

    def Create(self, request, context):
        """Create a new file resource."""
        inputs = self._struct_to_dict(request.properties)
        path = inputs['path']
        content = inputs['content']
        force = inputs.get('force', False)

        # During preview, don't actually create the file
        if request.preview:
            return provider_pb2.CreateResponse(
                id=path,
                properties=self._dict_to_struct(inputs),
            )

        # Check if file exists
        if os.path.exists(path) and not force:
            context.abort(
                grpc.StatusCode.ALREADY_EXISTS,
                f"File already exists at {path}. Set force=true to overwrite."
            )

        # Create parent directories if needed
        parent_dir = os.path.dirname(path)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

        # Write the file
        with open(path, 'w') as f:
            f.write(content)

        return provider_pb2.CreateResponse(
            id=path,
            properties=self._dict_to_struct(inputs),
        )

    def Read(self, request, context):
        """Read the current state of a file resource."""
        path = request.id

        if not os.path.exists(path):
            # Resource no longer exists
            return provider_pb2.ReadResponse(
                id='',
                properties=struct_pb2.Struct(),
                inputs=struct_pb2.Struct(),
            )

        with open(path, 'r') as f:
            content = f.read()

        state = {
            'path': path,
            'content': content,
            'force': self._struct_to_dict(request.inputs).get('force', False),
        }

        return provider_pb2.ReadResponse(
            id=path,
            properties=self._dict_to_struct(state),
            inputs=self._dict_to_struct(state),
        )

    def Update(self, request, context):
        """Update an existing file resource."""
        inputs = self._struct_to_dict(request.news)
        path = inputs['path']
        content = inputs['content']

        # During preview, don't actually update the file
        if request.preview:
            return provider_pb2.UpdateResponse(
                properties=self._dict_to_struct(inputs),
            )

        # Write the updated content
        with open(path, 'w') as f:
            f.write(content)

        return provider_pb2.UpdateResponse(
            properties=self._dict_to_struct(inputs),
        )

    def Delete(self, request, context):
        """Delete a file resource."""
        path = request.id

        if os.path.exists(path):
            os.remove(path)

        return empty_pb2.Empty()

    # -------------------------------------------------------------------------
    # Optional methods (minimal implementations)
    # -------------------------------------------------------------------------

    def Invoke(self, request, context):
        """Handle function invocations."""
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Invoke not implemented")

    def Call(self, request, context):
        """Handle method calls on component resources."""
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Call not implemented")

    def Construct(self, request, context):
        """Construct component resources."""
        context.abort(grpc.StatusCode.UNIMPLEMENTED, "Construct not implemented")

    def Cancel(self, request, context):
        """Handle cancellation requests."""
        return empty_pb2.Empty()

    def Attach(self, request, context):
        """Attach to a running provider."""
        return empty_pb2.Empty()

    def GetMapping(self, request, context):
        """Get provider mappings."""
        return provider_pb2.GetMappingResponse()

    def GetMappings(self, request, context):
        """Get all provider mappings."""
        return provider_pb2.GetMappingsResponse()

    # -------------------------------------------------------------------------
    # Utility methods
    # -------------------------------------------------------------------------

    def _struct_to_dict(self, struct):
        """Convert a protobuf Struct to a Python dict."""
        from google.protobuf.json_format import MessageToDict
        return MessageToDict(struct)

    def _dict_to_struct(self, d):
        """Convert a Python dict to a protobuf Struct."""
        struct = struct_pb2.Struct()
        struct.update(d)
        return struct


def serve(schema_path: str):
    """Start the gRPC server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    provider_pb2_grpc.add_ResourceProviderServicer_to_server(
        MyFilesProvider(schema_path), server
    )
    # Use port 0 to let the OS assign an available port
    port = server.add_insecure_port('127.0.0.1:0')
    server.start()
    # Write the port to stdout as bytes - Pulumi reads this to connect
    sys.stdout.buffer.write(f'{port}\n'.encode())
    sys.stdout.buffer.flush()
    server.wait_for_termination()
```

Create `provider/__main__.py`:

```python
import sys
import os

# Add the parent directory to the path so we can import the provider
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from provider.server import serve

if __name__ == '__main__':
    # Find the schema.json file
    provider_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    schema_path = os.path.join(provider_dir, 'schema.json')

    serve(schema_path)
```

## Step 5: Test the provider

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
        Hello from my Python provider!
```

Run the program:

```bash
pulumi up
```

You should see the file created at `test.txt`.

## Dispatching to multiple resources

The example above shows a single resource type. Real providers typically have many resources and need to dispatch to the correct implementation based on the type token.

Since Pulumi SDK v3.132.0, the type token is available directly in the request via `request.type`:

```python
def Create(self, request, context):
    """Create a new resource, dispatching based on type."""
    if request.type == "myfiles:index:File":
        return self._create_file(request, context)
    elif request.type == "myfiles:index:Directory":
        return self._create_directory(request, context)
    else:
        context.abort(
            grpc.StatusCode.UNIMPLEMENTED,
            f"Unknown resource type: {request.type}"
        )
```

Apply the same pattern to Check, Diff, Read, Update, and Delete.

## Working with property bags

Resource inputs and outputs are untyped property bags (dictionaries/maps). In production providers, you'll often want to deserialize these into typed structures for safer code, and serialize typed structures back to property bags for responses.

```python
from dataclasses import dataclass

@dataclass
class FileInputs:
    path: str
    content: str
    force: bool = False

    @classmethod
    def from_dict(cls, d: dict) -> "FileInputs":
        return cls(
            path=d.get("path", ""),
            content=d.get("content", ""),
            force=d.get("force", False),
        )

    def to_dict(self) -> dict:
        return {"path": self.path, "content": self.content, "force": self.force}
```

The [Pulumi Go Provider SDK](/docs/iac/guides/building-extending/providers/sdks/pulumi-go-provider-sdk/) handles both dispatching and property bag serialization automatically based on Go struct definitions and tags.

## Handling secrets and unknowns

The example above is simplified. Production providers need to handle secrets and unknown values properly.

### Secrets

Properties may be wrapped in a secret marker:

```python
def _unwrap_secret(self, value):
    """Unwrap secret values while preserving the marker for outputs."""
    if isinstance(value, dict) and value.get('4dabf18193072939515e22adb298388d') == 'secret':
        return value.get('value'), True
    return value, False
```

### Unknowns

During preview, some values are unknown:

```python
def _is_unknown(self, value):
    """Check if a value is unknown (not yet computed)."""
    if isinstance(value, dict):
        return value.get('4dabf18193072939515e22adb298388d') == 'unknown'
    return False
```

Handle unknowns in your Diff implementation by skipping comparison for unknown values.

## Packaging for distribution

To distribute your provider, you need to create a wrapper script that Pulumi can execute. Create a shell script named `pulumi-resource-myfiles`:

```bash
#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"
source venv/bin/activate
exec python -m provider "$@"
```

Make it executable with `chmod +x pulumi-resource-myfiles`. This script activates the virtual environment and runs the provider module. Package everything including the `venv` directory into a distributable archive, or install dependencies system-wide and adjust the script accordingly.

See [Publishing packages](/docs/iac/guides/building-extending/packages/publishing-packages/) for full details.

## Debugging

Add logging to stderr since stdout is reserved for the port number:

```python
import sys
print("Debug message", file=sys.stderr)
```

You can also test individual methods with a gRPC client, or use the `PULUMI_DEBUG_PROVIDERS` environment variable:

```bash
PULUMI_DEBUG_PROVIDERS="myfiles" pulumi up
```

## Complete example

A complete working example is available at: [pulumi/examples/python-provider](https://github.com/pulumi/examples) (TODO: Add link when example is published)

## Next steps

For detailed method documentation, see the [Protocol reference](/docs/iac/guides/building-extending/providers/implementers/protocol-reference/). For the complete schema specification, see the [Schema reference](/docs/iac/guides/building-extending/packages/schema/). When you're ready to distribute your provider, see [Publishing packages](/docs/iac/guides/building-extending/packages/publishing-packages/).
