---
title_tag: "Implement a provider in TypeScript"
meta_desc: "Build a Pulumi provider in TypeScript using the gRPC bindings directly."
title: Implement a provider in TypeScript
h1: Implement a provider in TypeScript
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: TypeScript
        parent: iac-guides-provider-implementers
        weight: 40
---

This guide shows how to implement a Pulumi provider in TypeScript using the gRPC bindings directly. This approach gives you full control over provider behavior and works with Node.js.

{{% notes type="warning" %}}
This is an advanced guide for power users. You'll be working directly with the provider protocol, which requires understanding gRPC, Protocol Buffers, and Pulumi's provider semantics. If you're open to writing Go, the [Pulumi Go Provider SDK](/docs/iac/guides/building-extending/providers/sdks/pulumi-go-provider-sdk/) offers a more ergonomic experience with less boilerplate.
{{% /notes %}}

## Prerequisites

You'll need Node.js 20 or later, and a basic understanding of the [provider protocol](/docs/iac/guides/building-extending/providers/implementers/protocol-reference/).

## Project structure

```
my-provider/
├── src/
│   └── index.ts              # Provider implementation
├── schema.json               # Provider schema
├── pulumi-resource-myfiles   # Wrapper script (executable)
├── package.json
└── tsconfig.json
```

## Step 1: Set up the project

Create your project directory and initialize:

```bash
mkdir my-provider && cd my-provider
npm init -y
```

Install dependencies:

```bash
npm install @pulumi/pulumi @grpc/grpc-js google-protobuf@3.21.4
npm install -D typescript @types/node @types/google-protobuf
```

{{% notes type="info" %}}
Use google-protobuf version 3.21.4 to match the version bundled with the Pulumi SDK. Version 4.x has incompatible API changes.
{{% /notes %}}

Create `tsconfig.json`:

```json
{
    "compilerOptions": {
        "target": "ES2020",
        "module": "commonjs",
        "lib": ["ES2020"],
        "outDir": "./dist",
        "rootDir": "./src",
        "strict": true,
        "esModuleInterop": true,
        "skipLibCheck": true,
        "forceConsistentCasingInFileNames": true,
        "declaration": true
    },
    "include": ["src/**/*"]
}
```

Update `package.json` to add build scripts:

```json
{
    "scripts": {
        "build": "tsc"
    }
}
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

Create `src/index.ts`:

```typescript
import * as fs from "fs";
import * as path from "path";
import * as grpc from "@grpc/grpc-js";

// Import generated proto types from Pulumi SDK
const providerProto = require("@pulumi/pulumi/proto/provider_pb");
const providerGrpc = require("@pulumi/pulumi/proto/provider_grpc_pb");
const pluginProto = require("@pulumi/pulumi/proto/plugin_pb");
const structProto = require("google-protobuf/google/protobuf/struct_pb");
const emptyProto = require("google-protobuf/google/protobuf/empty_pb");

// Load schema
const schema = fs.readFileSync(path.join(__dirname, "..", "schema.json"), "utf-8");

// Helper to convert Struct to plain object
function structToObject(struct: any): Record<string, any> {
    return struct ? struct.toJavaScript() : {};
}

// Helper to convert plain object to Struct
function objectToStruct(obj: Record<string, any>): any {
    return structProto.Struct.fromJavaScript(obj);
}

// Provider implementation
const providerImpl = {
    getPluginInfo(
        call: grpc.ServerUnaryCall<any, any>,
        callback: grpc.sendUnaryData<any>
    ) {
        const response = new pluginProto.PluginInfo();
        response.setVersion("0.1.0");
        callback(null, response);
    },

    getSchema(
        call: grpc.ServerUnaryCall<any, any>,
        callback: grpc.sendUnaryData<any>
    ) {
        const response = new providerProto.GetSchemaResponse();
        response.setSchema(schema);
        callback(null, response);
    },

    configure(
        call: grpc.ServerUnaryCall<any, any>,
        callback: grpc.sendUnaryData<any>
    ) {
        const response = new providerProto.ConfigureResponse();
        response.setAcceptsecrets(true);
        response.setSupportspreview(true);
        callback(null, response);
    },

    checkConfig(
        call: grpc.ServerUnaryCall<any, any>,
        callback: grpc.sendUnaryData<any>
    ) {
        const response = new providerProto.CheckResponse();
        response.setInputs(call.request.getNews());
        callback(null, response);
    },

    diffConfig(
        call: grpc.ServerUnaryCall<any, any>,
        callback: grpc.sendUnaryData<any>
    ) {
        const response = new providerProto.DiffResponse();
        callback(null, response);
    },

    check(
        call: grpc.ServerUnaryCall<any, any>,
        callback: grpc.sendUnaryData<any>
    ) {
        const inputs = structToObject(call.request.getNews());
        const failures: any[] = [];

        if (!inputs.path) {
            const failure = new providerProto.CheckFailure();
            failure.setProperty("path");
            failure.setReason("path is required");
            failures.push(failure);
        }

        if (!inputs.content) {
            const failure = new providerProto.CheckFailure();
            failure.setProperty("content");
            failure.setReason("content is required");
            failures.push(failure);
        }

        // Set defaults
        if (inputs.force === undefined) {
            inputs.force = false;
        }

        const response = new providerProto.CheckResponse();
        response.setInputs(objectToStruct(inputs));
        failures.forEach(f => response.addFailures(f));
        callback(null, response);
    },

    diff(
        call: grpc.ServerUnaryCall<any, any>,
        callback: grpc.sendUnaryData<any>
    ) {
        const olds = structToObject(call.request.getOlds());
        const news = structToObject(call.request.getNews());

        const diffs: string[] = [];
        const replaces: string[] = [];
        const detailedDiff: Record<string, any> = {};

        if (olds.content !== news.content) {
            diffs.push("content");
            const diff = new providerProto.PropertyDiff();
            diff.setKind(providerProto.PropertyDiff.Kind.UPDATE);
            detailedDiff["content"] = diff;
        }

        if (olds.force !== news.force) {
            diffs.push("force");
            const diff = new providerProto.PropertyDiff();
            diff.setKind(providerProto.PropertyDiff.Kind.UPDATE);
            detailedDiff["force"] = diff;
        }

        if (olds.path !== news.path) {
            diffs.push("path");
            replaces.push("path");
            const diff = new providerProto.PropertyDiff();
            diff.setKind(providerProto.PropertyDiff.Kind.UPDATE_REPLACE);
            detailedDiff["path"] = diff;
        }

        const response = new providerProto.DiffResponse();
        response.setChanges(
            diffs.length > 0
                ? providerProto.DiffResponse.DiffChanges.DIFF_SOME
                : providerProto.DiffResponse.DiffChanges.DIFF_NONE
        );
        diffs.forEach(d => response.addDiffs(d));
        replaces.forEach(r => response.addReplaces(r));
        Object.entries(detailedDiff).forEach(([k, v]) => {
            response.getDetaileddiffMap().set(k, v);
        });
        response.setHasdetaileddiff(true);
        response.setDeletebeforereplace(true);
        callback(null, response);
    },

    create(
        call: grpc.ServerUnaryCall<any, any>,
        callback: grpc.sendUnaryData<any>
    ) {
        const inputs = structToObject(call.request.getProperties());
        const filePath = inputs.path as string;
        const content = inputs.content as string;
        const force = inputs.force as boolean;

        // During preview, don't create the file
        if (call.request.getPreview()) {
            const response = new providerProto.CreateResponse();
            response.setId(filePath);
            response.setProperties(objectToStruct(inputs));
            callback(null, response);
            return;
        }

        // Check if file exists
        if (fs.existsSync(filePath) && !force) {
            callback({
                code: grpc.status.ALREADY_EXISTS,
                message: `File already exists at ${filePath}. Set force=true to overwrite.`,
            });
            return;
        }

        // Create parent directories if needed
        const parentDir = path.dirname(filePath);
        if (parentDir) {
            fs.mkdirSync(parentDir, { recursive: true });
        }

        // Write the file
        fs.writeFileSync(filePath, content);

        const response = new providerProto.CreateResponse();
        response.setId(filePath);
        response.setProperties(objectToStruct(inputs));
        callback(null, response);
    },

    read(
        call: grpc.ServerUnaryCall<any, any>,
        callback: grpc.sendUnaryData<any>
    ) {
        const filePath = call.request.getId();

        if (!fs.existsSync(filePath)) {
            // Resource no longer exists
            const response = new providerProto.ReadResponse();
            callback(null, response);
            return;
        }

        const content = fs.readFileSync(filePath, "utf-8");
        const oldInputs = structToObject(call.request.getInputs());

        const state = {
            path: filePath,
            content: content,
            force: oldInputs.force || false,
        };

        const response = new providerProto.ReadResponse();
        response.setId(filePath);
        response.setProperties(objectToStruct(state));
        response.setInputs(objectToStruct(state));
        callback(null, response);
    },

    update(
        call: grpc.ServerUnaryCall<any, any>,
        callback: grpc.sendUnaryData<any>
    ) {
        const inputs = structToObject(call.request.getNews());
        const filePath = inputs.path as string;
        const content = inputs.content as string;

        // During preview, don't update the file
        if (call.request.getPreview()) {
            const response = new providerProto.UpdateResponse();
            response.setProperties(objectToStruct(inputs));
            callback(null, response);
            return;
        }

        // Write the updated content
        fs.writeFileSync(filePath, content);

        const response = new providerProto.UpdateResponse();
        response.setProperties(objectToStruct(inputs));
        callback(null, response);
    },

    delete(
        call: grpc.ServerUnaryCall<any, any>,
        callback: grpc.sendUnaryData<any>
    ) {
        const filePath = call.request.getId();

        if (fs.existsSync(filePath)) {
            fs.unlinkSync(filePath);
        }

        callback(null, new emptyProto.Empty());
    },

    cancel(
        call: grpc.ServerUnaryCall<any, any>,
        callback: grpc.sendUnaryData<any>
    ) {
        callback(null, new emptyProto.Empty());
    },
};

// Start gRPC server
const server = new grpc.Server();
server.addService(providerGrpc.ResourceProviderService, providerImpl);

server.bindAsync(
    "127.0.0.1:0",
    grpc.ServerCredentials.createInsecure(),
    (err, port) => {
        if (err) {
            console.error(`Failed to bind: ${err}`);
            process.exit(1);
        }

        // Print the port for Pulumi to connect
        console.log(port);

        server.start();
    }
);
```

## Step 4: Build and create wrapper script

Build the TypeScript:

```bash
npm run build
```

Create a wrapper script `pulumi-resource-myfiles`:

```bash
#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
node "$DIR/dist/index.js"
```

Make it executable:

```bash
chmod +x pulumi-resource-myfiles
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
        Hello from my TypeScript provider!
```

Run the program:

```bash
pulumi up
```

You should see the file created at `test.txt`.

## Dispatching to multiple resources

The example above shows a single resource type. Real providers typically have many resources and need to dispatch to the correct implementation based on the type token.

Since Pulumi SDK v3.132.0, the type token is available directly in the request via `getType()`:

```typescript
create(
    call: grpc.ServerUnaryCall<any, any>,
    callback: grpc.sendUnaryData<any>
) {
    const resourceType = call.request.getType();

    switch (resourceType) {
        case "myfiles:index:File":
            return this.createFile(call, callback);
        case "myfiles:index:Directory":
            return this.createDirectory(call, callback);
        default:
            callback({
                code: grpc.status.UNIMPLEMENTED,
                message: `Unknown resource type: ${resourceType}`,
            });
    }
}
```

Apply the same pattern to Check, Diff, Read, Update, and Delete.

## Working with property bags

Resource inputs and outputs are untyped property bags (`Record<string, any>`). In production providers, you'll often want to deserialize these into typed interfaces for safer code, and serialize typed objects back to property bags for responses.

```typescript
interface FileInputs {
    path: string;
    content: string;
    force: boolean;
}

function fileInputsFromMap(m: Record<string, any>): FileInputs {
    return {
        path: m.path ?? "",
        content: m.content ?? "",
        force: m.force ?? false,
    };
}

function fileInputsToMap(inputs: FileInputs): Record<string, any> {
    return {
        path: inputs.path,
        content: inputs.content,
        force: inputs.force,
    };
}
```

The [Pulumi Go Provider SDK](/docs/iac/guides/building-extending/providers/sdks/pulumi-go-provider-sdk/) handles both dispatching and property bag serialization automatically based on Go struct definitions and tags.

## Considerations

TypeScript providers require Node.js to be installed on the user's system, which adds friction compared to Go providers that compile to standalone binaries. However, if your team is more productive in TypeScript and has access to the Node.js ecosystem, this tradeoff may be worthwhile—especially for internal providers.

## Next steps

For detailed method documentation, see the [Protocol reference](/docs/iac/guides/building-extending/providers/implementers/protocol-reference/). For the complete schema specification, see the [Schema reference](/docs/iac/guides/building-extending/packages/schema/). When you're ready to distribute your provider, see [Publishing packages](/docs/iac/guides/building-extending/packages/publishing-packages/).
