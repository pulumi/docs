---
title_tag: "Unit Testing Pulumi Programs"
meta_desc: "Guide to unit testing of Pulumi programs: mock-based tests across Node.js, Python, Go, .NET, and Java."
title: Unit Testing
h1: Unit Testing Pulumi Programs
weight: 1
menu:
    iac:
        name: Unit testing
        parent: iac-guides-testing
        weight: 1
aliases:
    - /docs/guides/testing/unit/
    - /docs/using-pulumi/testing/unit/
    - /docs/iac/concepts/testing/unit/
---

Pulumi programs are authored in a general-purpose language like TypeScript, Python, Go, .NET, or Java. The full power of that language is available to you, including its tooling, libraries, and testing frameworks.

When running an update, your Pulumi program talks to the Pulumi CLI to orchestrate the deployment. The idea of _unit tests_ is to cut this communication channel and replace the engine with mocks. The mocks answer those commands from within the same OS process, returning placeholder data for each call your program makes.

Because mocks don't do any real work, unit tests run fast. They're also deterministic, since nothing about them depends on the behavior of an external system.

## Get started

This guide builds a sample test suite against AWS resources, but the same capabilities and workflow apply to any Pulumi provider. To follow along, complete the [Get Started with AWS](/docs/iac/get-started/aws/) guide to set up a Pulumi program in the language of your choice.

Unit tests are supported in every [Pulumi language runtime](/docs/iac/languages-sdks/).

## Sample program

Throughout this guide, you'll test a program that creates an AWS EC2 web server. The tests check that:

- Instances have a `Name` tag.
- Instances must not use an inline `userData` script. They must use a virtual machine image instead.
- Instances must not have SSH open to the internet.

{{% notes type="info" %}}
Mock-based unit testing needs a general-purpose language runtime, so for declarative Pulumi programs written in YAML or HCL, see [integration testing](/docs/iac/guides/testing/integration/) instead.
{{% /notes %}}

{{< example-program path="unit-testing-webserver" languages="typescript,python,go,csharp,java" >}}

The program allocates a security group and an instance, and it looks the instance's AMI up with `getAmi` rather than hard-coding one. It also breaks all three of those rules, and the tests you write next catch each one.

## Install the unit testing framework

Use whichever test framework and assertion library you prefer.

{{% choosable language "typescript" %}}

This guide uses [Mocha](https://mochajs.org/) as the test framework, run through [tsx](https://tsx.is/) so that it executes your TypeScript directly. Install both as development dependencies of your program:

```bash
npm install --save-dev mocha @types/mocha tsx
```

{{% /choosable %}}

{{% choosable language python %}}

This guide uses Python's built-in [`unittest`](https://docs.python.org/3/library/unittest.html) framework, so there's nothing to install.

{{% /choosable %}}

{{% choosable language go %}}

This guide uses the built-in `go test` command, along with [testify](https://github.com/stretchr/testify) for assertions:

```bash
go get github.com/stretchr/testify
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

This guide uses the [NUnit](https://nunit.org/) test framework to define and run the tests, and [FluentAssertions](https://github.com/fluentassertions/fluentassertions) for assertions. The mocks themselves come from the `Pulumi.Testing` namespace in the Pulumi SDK, so there's no mocking library to add.

Install the corresponding NuGet packages to your program:

```bash
dotnet add package NUnit
dotnet add package NUnit3TestAdapter
dotnet add package FluentAssertions
dotnet add package Microsoft.NET.Test.Sdk
dotnet add package Pulumi
dotnet add package Pulumi.Aws
```

{{% /choosable %}}
{{% choosable language "java" %}}

This guide uses [JUnit 5](https://junit.org/junit5/) as the testing framework. Add the following dependencies to your `pom.xml`:

```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter-api</artifactId>
    <version>5.10.0</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter-engine</artifactId>
    <version>5.10.0</version>
    <scope>test</scope>
</dependency>
```

{{% /choosable %}}

## Add the mocks

Mocks stand in for the Pulumi CLI, answering your program from inside the same process. They have two handlers: `newResource` for each resource your program registers, and `call` for each provider function it invokes, which includes the sample program's AMI lookup.

Here is the whole file, followed by a breakdown of each handler.

{{% choosable language "typescript" %}}

{{< code-filename file="ec2tests.ts" />}}

```typescript
import * as pulumi from "@pulumi/pulumi";

pulumi.runtime.setMocks({
    newResource: function(args: pulumi.runtime.MockResourceArgs): {id: string, state: any} {
        switch (args.type) {
            case "aws:ec2/securityGroup:SecurityGroup":
                return {
                    id: "sg-12345678",
                    state: {
                        ...args.inputs,
                        // Mock output properties that may be used in tests
                        arn: "arn:aws:ec2:us-west-2:123456789012:security-group/sg-12345678",
                        name: args.inputs.name || args.name + "-sg",
                    },
                };
            case "aws:ec2/instance:Instance":
                return {
                    id: "i-1234567890abcdef0",
                    state: {
                        ...args.inputs,
                        // Mock output properties that may be used in tests
                        arn: "arn:aws:ec2:us-west-2:123456789012:instance/i-1234567890abcdef0",
                        instanceState: "running",
                        primaryNetworkInterfaceId: "eni-12345678",
                        privateDns: "ip-10-0-1-17.ec2.internal",
                        publicDns: "ec2-203-0-113-12.compute-1.amazonaws.com",
                        publicIp: "203.0.113.12",
                    },
                };
            default:
                return {
                    id: args.inputs.name + "_id",
                    state: {
                        ...args.inputs,
                    },
                };
        }
    },
    call: function(args: pulumi.runtime.MockCallArgs) {
        switch (args.token) {
            case "aws:ec2/getAmi:getAmi":
                return {
                    id: "ami-0eb1f3cdeeb8eed2a",
                    architecture: "x86_64",
                };
            default:
                return args.inputs;
        }
    },
},
  "project", // Project name. Mocked resources get it in their URNs.
  "stack",   // Stack name. Also part of the URN.
  false,     // Sets the flag `dryRun`, which indicates if pulumi is running in preview mode.
);
```

{{% /choosable %}}

{{% choosable language python %}}

{{< code-filename file="test_ec2.py" />}}

```python
import pulumi

class MyMocks(pulumi.runtime.Mocks):
    def new_resource(self, args: pulumi.runtime.MockResourceArgs):
        return [args.name + "_id", args.inputs]

    def call(self, args: pulumi.runtime.MockCallArgs):
        if args.token == "aws:ec2/getAmi:getAmi":
            return {
                "id": "ami-0eb1f3cdeeb8eed2a",
                "architecture": "x86_64",
            }
        return {}
```

{{% notes type="warning" %}}
When returning explicit output properties from `new_resource`, property names must use camelCase (e.g., `"publicIp"`, `"instanceState"`) rather than snake_case. This is because Pulumi uses camelCase for its internal property serialization regardless of the programming language. For example, use `"publicIp"` rather than `"public_ip"`.
{{% /notes %}}

{{% /choosable %}}

{{% choosable language go %}}

{{< code-filename file="main_test.go" />}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type mocks int

func (mocks) NewResource(args pulumi.MockResourceArgs) (string, resource.PropertyMap, error) {
	return args.Name + "_id", args.Inputs, nil
}

func (mocks) Call(args pulumi.MockCallArgs) (resource.PropertyMap, error) {
	if args.Token == "aws:ec2/getAmi:getAmi" {
		return resource.NewPropertyMapFromMap(map[string]interface{}{
			"id":           "ami-0eb1f3cdeeb8eed2a",
			"architecture": "x86_64",
		}), nil
	}
	return args.Args, nil
}
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

{{< code-filename file="Testing.cs" />}}

```csharp
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Testing;

namespace UnitTesting
{
    class Mocks : IMocks
    {
        public Task<(string? id, object state)> NewResourceAsync(MockResourceArgs args)
        {
            var outputs = ImmutableDictionary.CreateBuilder<string, object>();

            outputs.AddRange(args.Inputs);

            if (args.Type == "aws:ec2/instance:Instance")
            {
                outputs.Add("publicIp", "203.0.113.12");
                outputs.Add("publicDns", "ec2-203-0-113-12.compute-1.amazonaws.com");
            }

            args.Id ??= $"{args.Name}_id";
            return Task.FromResult<(string? id, object state)>((args.Id, (object)outputs));
        }

        public Task<object> CallAsync(MockCallArgs args)
        {
            if (args.Token == "aws:ec2/getAmi:getAmi")
            {
                return Task.FromResult<object>(new Dictionary<string, object>
                {
                    { "id", "ami-0eb1f3cdeeb8eed2a" },
                    { "architecture", "x86_64" },
                });
            }

            return Task.FromResult((object)ImmutableDictionary<string, object>.Empty);
        }
    }

    public static class Testing
    {
        public static Task<ImmutableArray<Resource>> RunAsync<T>() where T : Stack, new()
        {
            return Deployment.TestAsync<T>(new Mocks(), new TestOptions { IsPreview = false });
        }

        public static Task<T> GetValueAsync<T>(this Output<T> output)
        {
            var tcs = new TaskCompletionSource<T>();
            output.Apply(v =>
            {
                tcs.SetResult(v);
                return v;
            });
            return tcs.Task;
        }
    }
}
```

{{% /choosable %}}
{{% choosable language "java" %}}

{{< code-filename file="Ec2Tests.java" />}}

```java
package myproject;

import com.pulumi.test.Mocks;
import com.pulumi.test.Mocks.CallArgs;
import com.pulumi.test.Mocks.ResourceArgs;
import com.pulumi.test.Mocks.ResourceResult;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.CompletableFuture;

class MyMocks implements Mocks {
    @Override
    public CompletableFuture<ResourceResult> newResourceAsync(ResourceArgs args) {
        var state = new HashMap<>(args.inputs);
        return CompletableFuture.completedFuture(
            ResourceResult.of(Optional.of(args.name + "_id"), state)
        );
    }

    @Override
    public CompletableFuture<Map<String, Object>> callAsync(CallArgs args) {
        if ("aws:ec2/getAmi:getAmi".equals(args.token)) {
            return CompletableFuture.completedFuture(Map.of(
                "id", "ami-0eb1f3cdeeb8eed2a",
                "architecture", "x86_64"
            ));
        }
        return CompletableFuture.completedFuture(Map.of());
    }
}
```

{{% /choosable %}}

The full mocks interface is defined on the [Node.js runtime API reference page](/docs/reference/pkg/nodejs/pulumi/pulumi/runtime/#Mocks).

### Mocking resources

`newResource` is handed one resource registration at a time, and returns the ID and state the engine would have returned. Two kinds of property pass through it:

- **Input properties**, such as `tags`, `userData`, and `ingress`, are set by your program and arrive on the mock's arguments. Returning them unchanged is usually what you want.
- **Output properties**, such as `arn`, `publicIp`, and `instanceState`, are computed by the cloud provider. The mock has to return them explicitly, or they come back undefined.

The tests later in this guide read both kinds, which is why the mock branches on the resource type: each type needs its own set of output properties.

### Mocking provider functions

Provider functions, such as `aws.ec2.getAmi` or `aws.getAvailabilityZones`, don't create anything. They query the provider, so the mocks answer them in `call` rather than in `newResource`. Mocking one pins the value the lookup returns, which is what keeps a test that depends on a live cloud query deterministic.

Each function is identified by a token of the form `<package>:<module>/<function>:<function>`, so `getAmi` in the AWS provider's `ec2` module is `aws:ec2/getAmi:getAmi`. You'll find the token for any function on its page in the [Pulumi Registry](/registry/), and in the provider's schema. Match on it to decide what to return.

The `call` handler also receives the arguments the program passed to the function, in `args.inputs` (`args.Args` in Go), so a single mock can answer different queries with different results. A test that exercises both an Amazon Linux lookup and an Ubuntu one can return a different AMI for each, keyed on the filters the program supplied.

The snippets below come from a compact, self-contained project rather than from the web server this guide builds, so that the mock and the assertion it enables sit side by side.

{{% choosable language "typescript" %}}

Match on the token in `call`, and fall through to the default for every other function:

```typescript
{{< example-program-snippet path="unit-testing-function-mock" language="typescript" file="test/index.spec.ts" from="4" to="22" >}}
```

The test can then assert that the mocked value reached the resource that consumed it:

```typescript
{{< example-program-snippet path="unit-testing-function-mock" language="typescript" file="test/index.spec.ts" from="24" to="43" >}}
```

{{% /choosable %}}
{{% choosable language "python" %}}

Match on the token in `call`, and fall through to the default for every other function:

```python
{{< example-program-snippet path="unit-testing-function-mock" language="python" file="test_function_mock.py" from="7" to="17" >}}
```

The test can then assert that the mocked value reached the resource that consumed it:

```python
{{< example-program-snippet path="unit-testing-function-mock" language="python" file="test_function_mock.py" from="20" to="38" >}}
```

{{% /choosable %}}
{{% choosable language "go" %}}

Match on the token in `Call`, and fall through to the default for every other function:

```go
{{< example-program-snippet path="unit-testing-function-mock" language="go" file="main_test.go" from="12" to="26" >}}
```

The test can then assert that the mocked value reached the resource that consumed it:

```go
{{< example-program-snippet path="unit-testing-function-mock" language="go" file="main_test.go" from="28" to="50" >}}
```

{{% /choosable %}}
{{% choosable language "csharp" %}}

Match on the token in `CallAsync`, and fall through to the default for every other function:

```csharp
{{< example-program-snippet path="unit-testing-function-mock" language="csharp" file="Testing.cs" from="7" to="31" >}}
```

The test can then assert that the mocked value reached the resource that consumed it:

```csharp
{{< example-program-snippet path="unit-testing-function-mock" language="csharp" file="AmiTests.cs" from="5" to="18" >}}
```

{{% /choosable %}}
{{% choosable language "java" %}}

Match on the token in `callAsync`, and fall through to the default for every other function:

```java
{{< example-program-snippet path="unit-testing-function-mock" language="java" file="src/test/java/myproject/AmiTest.java" from="17" to="36" >}}
```

The test can then assert that the mocked value reached the resource that consumed it:

```java
{{< example-program-snippet path="unit-testing-function-mock" language="java" file="src/test/java/myproject/AmiTest.java" from="38" to="62" >}}
```

{{% /choosable %}}

The mock only needs the fields your test actually reads. Anything you leave out comes back empty, exactly as it does for an unmocked resource output.

These five projects, one per language, are runnable and run in this site's CI. They live under [static/programs](https://github.com/pulumi/docs/tree/master/static/programs), named `unit-testing-function-mock-<language>`.

### Mocking stack references

If your program uses [StackReference](/docs/iac/concepts/stacks/#stackreferences) to read outputs from another stack, you need to handle them in your mocks. When a `StackReference` resource is created, the mock's `newResource` function receives it with type `pulumi:pulumi:StackReference`. You can return mock outputs that simulate the referenced stack's outputs.

{{% choosable language "typescript" %}}

```typescript
pulumi.runtime.setMocks({
    newResource: function(args: pulumi.runtime.MockResourceArgs): {id: string, state: any} {
        // Handle StackReference resources
        if (args.type === "pulumi:pulumi:StackReference") {
            return {
                id: args.inputs.name + "_id",
                state: {
                    ...args.inputs,
                    outputs: {
                        // Mock the outputs from the referenced stack
                        vpcId: "vpc-12345678",
                        subnetIds: ["subnet-11111111", "subnet-22222222"],
                        clusterName: "my-cluster",
                    },
                },
            };
        }
        // Handle all other resources
        return {
            id: args.inputs.name + "_id",
            state: args.inputs,
        };
    },
    call: function(args: pulumi.runtime.MockCallArgs) {
        return args.inputs;
    },
});
```

In your program, you can then use a `StackReference` as usual:

```typescript
// Example: Program that reads from a StackReference
const networkStack = new pulumi.StackReference("organization/network/prod");
const vpcId = networkStack.getOutput("vpcId");

// In tests, vpcId will resolve to "vpc-12345678" based on the mock above
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi

class MyMocks(pulumi.runtime.Mocks):
    def new_resource(self, args: pulumi.runtime.MockResourceArgs):
        # Handle StackReference resources
        if args.typ == "pulumi:pulumi:StackReference":
            return [
                args.name + "_id",
                {
                    **args.inputs,
                    "outputs": {
                        # Mock the outputs from the referenced stack
                        "vpcId": "vpc-12345678",
                        "subnetIds": ["subnet-11111111", "subnet-22222222"],
                        "clusterName": "my-cluster",
                    },
                },
            ]
        # Handle all other resources
        return [args.name + "_id", args.inputs]

    def call(self, args: pulumi.runtime.MockCallArgs):
        return {}
```

In your program, you can then use a `StackReference` as usual:

```python
network_stack = pulumi.StackReference("organization/network/prod")
vpc_id = network_stack.get_output("vpcId")

# In tests, vpc_id will resolve to "vpc-12345678" based on the mock above
```

{{% /choosable %}}

{{% choosable language go %}}

```go
type mocks int

func (mocks) NewResource(args pulumi.MockResourceArgs) (string, resource.PropertyMap, error) {
	// Handle StackReference resources
	if args.TypeToken == "pulumi:pulumi:StackReference" {
		outputs := resource.NewPropertyMapFromMap(map[string]interface{}{
			"vpcId":       "vpc-12345678",
			"subnetIds":   []interface{}{"subnet-11111111", "subnet-22222222"},
			"clusterName": "my-cluster",
		})
		// Copy inputs and add outputs
		state := args.Inputs.Copy()
		state["outputs"] = resource.NewObjectProperty(outputs)
		return args.Name + "_id", state, nil
	}
	// Handle all other resources
	return args.Name + "_id", args.Inputs, nil
}

func (mocks) Call(args pulumi.MockCallArgs) (resource.PropertyMap, error) {
	return args.Args, nil
}
```

In your program, you can then use a `StackReference` as usual:

```go
networkStack, err := pulumi.NewStackReference(ctx, "organization/network/prod", nil)
if err != nil {
    return err
}
vpcId := networkStack.GetStringOutput(pulumi.String("vpcId"))

// In tests, vpcId will resolve to "vpc-12345678" based on the mock above
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

```csharp
class Mocks : IMocks
{
    public Task<(string? id, object state)> NewResourceAsync(MockResourceArgs args)
    {
        var outputs = ImmutableDictionary.CreateBuilder<string, object>();
        outputs.AddRange(args.Inputs);

        // Handle StackReference resources
        if (args.Type == "pulumi:pulumi:StackReference")
        {
            outputs.Add("outputs", new Dictionary<string, object>
            {
                // Mock the outputs from the referenced stack
                { "vpcId", "vpc-12345678" },
                { "subnetIds", new[] { "subnet-11111111", "subnet-22222222" } },
                { "clusterName", "my-cluster" },
            });
        }

        args.Id ??= $"{args.Name}_id";
        return Task.FromResult<(string? id, object state)>((args.Id, (object)outputs));
    }

    public Task<object> CallAsync(MockCallArgs args)
    {
        return Task.FromResult((object)ImmutableDictionary<string, object>.Empty);
    }
}
```

In your program, you can then use a `StackReference` as usual:

```csharp
var networkStack = new StackReference("organization/network/prod");
var vpcId = networkStack.GetOutput("vpcId");

// In tests, vpcId will resolve to "vpc-12345678" based on the mock above
```

{{% /choosable %}}
{{% choosable language "java" %}}

```java
import java.util.List;

class MyMocks implements Mocks {
    @Override
    public CompletableFuture<ResourceResult> newResourceAsync(ResourceArgs args) {
        var state = new HashMap<>(args.inputs);
        // Handle StackReference resources
        if ("pulumi:pulumi:StackReference".equals(args.type)) {
            state.put("outputs", Map.of(
                "vpcId", "vpc-12345678",
                "subnetIds", List.of("subnet-11111111", "subnet-22222222"),
                "clusterName", "my-cluster"
            ));
        }
        return CompletableFuture.completedFuture(
            ResourceResult.of(Optional.of(args.name + "_id"), state)
        );
    }

    @Override
    public CompletableFuture<Map<String, Object>> callAsync(CallArgs args) {
        return CompletableFuture.completedFuture(Map.of());
    }
}
```

In your program, you can then use a `StackReference` as usual:

```java
var networkStack = new StackReference("organization/network/prod",
    StackReferenceArgs.builder().build());
var vpcId = networkStack.getOutput(Output.of("vpcId"));

// In tests, vpcId will resolve to "vpc-12345678" based on the mock above
```

{{% /choosable %}}

This approach lets you test how your program uses outputs from other stacks without needing those stacks to actually exist. You can mock different scenarios by returning different outputs in your test setup.

## Write the tests

{{% choosable language "typescript" %}}
The structure and scaffolding look like any ordinary Mocha test:

{{< code-filename file="ec2tests.ts" />}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import "mocha";

pulumi.runtime.setMocks({
    // ... mocks as shown above
});

describe("Infrastructure", function() {
    let infra: typeof import("./index");

    before(async function() {
        // It's important to import the program _after_ the mocks are defined.
        infra = await import("./index");
    })

    describe("#server", function() {
        // TODO(check 1): Instances have a Name tag.
        // TODO(check 2): Instances must not use an inline userData script.
    });

    describe("#group", function() {
        // TODO(check 3): Instances must not have SSH open to the internet.
    });
});
```

{{% /choosable %}}
{{% choosable language "python" %}}
Pulumi's Python runtime requires an asyncio event loop. Subclass `unittest.IsolatedAsyncioTestCase` to create and close a separate event loop for each test. In `setUp`, initialize the mocks and run the Pulumi program:

{{< code-filename file="test_ec2.py" />}}

```python
import runpy
import unittest
import pulumi

# ... MyMocks as shown above

class TestingWithMocks(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        pulumi.runtime.set_mocks(
            MyMocks(),
            preview=False, # Sets the flag `dry_run`, which is true at runtime during a preview.
        )
        # Run the program fresh for each test *after* setting the mocks.
        program = runpy.run_path("__main__.py")
        self.group = program["group"]
        self.server = program["server"]

    # TODO(check 1): Instances have a Name tag.
    # TODO(check 2): Instances must not use an inline userData script.
    # TODO(check 3): Instances must not have SSH open to the internet.
```

{{% /choosable %}}
{{% choosable language "go" %}}

The structure and scaffolding look like any ordinary Go test:

{{< code-filename file="main_test.go" />}}

```go
package main

import (
	"sync"
	"testing"

	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/stretchr/testify/assert"
)

// ... mocks as shown above

func TestInfrastructure(t *testing.T) {
	err := pulumi.RunErr(func(ctx *pulumi.Context) error {
		infra, err := createInfrastructure(ctx)
		assert.NoError(t, err)

		var wg sync.WaitGroup
		wg.Add(3)

		// TODO(check 1): Instances have a Name tag.
		// TODO(check 2): Instances must not use an inline userData script.
		// TODO(check 3): Instances must not have SSH open to the internet.

		wg.Wait()
		return nil
	}, pulumi.WithMocks("project", "stack", mocks(0))) // Project and stack names; they end up in the mocked resources' URNs.
	assert.NoError(t, err)
}
```

{{% /choosable %}}
{{% choosable language "csharp" %}}
The structure and scaffolding look like any ordinary NUnit test:

{{< code-filename file="WebserverStackTests.cs" />}}

```csharp
using System.Linq;
using System.Threading.Tasks;
using FluentAssertions;
using NUnit.Framework;
using Pulumi.Aws.Ec2;

namespace UnitTesting
{
    [TestFixture]
    public class WebserverStackTests
    {
        // TODO(check 1): Instances have a Name tag.
        // TODO(check 2): Instances must not use an inline userData script.
        // TODO(check 3): Instances must not have SSH open to the internet.
    }
}
```

{{% /choosable %}}
{{% choosable language "java" %}}

The structure and scaffolding look like any ordinary JUnit 5 test class. Call `PulumiTest.cleanup()` after each test to reset the Pulumi runtime state:

{{< code-filename file="Ec2Tests.java" />}}

```java
package myproject;

import com.pulumi.test.PulumiTest;
import com.pulumi.test.TestOptions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

class Ec2Tests {
    @AfterEach
    void cleanup() {
        PulumiTest.cleanup();
    }

    // TODO(check 1): Instances have a Name tag.
    // TODO(check 2): Instances must not use an inline userData script.
    // TODO(check 3): Instances must not have SSH open to the internet.
}
```

{{% /choosable %}}

Now implement the first check: instances have a `Name` tag. Take hold of the EC2 instance object and inspect the property:

{{% choosable language "typescript" %}}

```typescript
// check 1: Instances have a Name tag.
it("must have a name tag", function(done) {
    pulumi.all([infra.server.urn, infra.server.tags]).apply(([urn, tags]) => {
        if (!tags || !tags["Name"]) {
            done(new Error(`Missing a name tag on server ${urn}`));
        } else {
            done();
        }
    });
});
```

{{% /choosable %}}
{{% choosable language "python" %}}

```python
class TestingWithMocks(unittest.IsolatedAsyncioTestCase):
    # ... setUp as shown above

    # check 1: Instances have a Name tag.
    @pulumi.runtime.test
    def test_server_tags(self):
        def check_tags(args):
            urn, tags = args
            self.assertIsNotNone(tags, f"server {urn} must have tags")
            self.assertIn("Name", tags, f"server {urn} must have a name tag")

        return pulumi.Output.all(self.server.urn, self.server.tags).apply(check_tags)
```

{{% /choosable %}}
{{% choosable language "go" %}}

```go
// check 1: Instances have a Name tag.
pulumi.All(infra.server.URN(), infra.server.Tags).ApplyT(func(all []interface{}) error {
	urn := all[0].(pulumi.URN)
	tags := all[1].(map[string]string)

	assert.Containsf(t, tags, "Name", "missing a Name tag on server %v", urn)
	wg.Done()
	return nil
})
```

{{% /choosable %}}
{{% choosable language "csharp" %}}

```csharp
// check 1: Instances have a Name tag.
[Test]
public async Task InstanceHasNameTag()
{
    var resources = await Testing.RunAsync<WebserverStack>();

    var instance = resources.OfType<Instance>().FirstOrDefault();
    instance.Should().NotBeNull("EC2 Instance not found");

    var tags = await instance.Tags.GetValueAsync();
    tags.Should().NotBeNull("Tags are not defined");
    tags.Should().ContainKey("Name");
}
```

{{% /choosable %}}
{{% choosable language "java" %}}

```java
// check 1: Instances have a Name tag.
@Test
void instanceMustHaveNameTag() {
    var result = PulumiTest
        .withMocks(new MyMocks())
        .withOptions(TestOptions.builder()
            // Project and stack names; they end up in the mocked resources' URNs.
            .projectName("project").stackName("stack").preview(false)
            .build())
        .runTest(App::stack);

    var instances = result.resources().stream()
        .filter(r -> r instanceof Instance)
        .map(r -> (Instance) r)
        .toList();

    assertFalse(instances.isEmpty(), "EC2 Instance not found");
    for (var instance : instances) {
        var urn = PulumiTest.extractValue(instance.urn());
        var tags = PulumiTest.extractValue(instance.tags());
        assertNotNull(tags, "Server " + urn + " must have tags");
        assertTrue(tags.containsKey("Name"), "Server " + urn + " must have a Name tag");
    }
}
```

{{% /choosable %}}

This looks like a normal test, with a few noteworthy pieces:

- The test queries resource state without running a deployment, so many properties are undefined. That includes every output property your cloud provider computes and the mocks don't return explicitly. These checks only read inputs, so none of that matters here.
- Every Pulumi resource property is an [output](/docs/iac/concepts/inputs-outputs/), because so many of them are computed asynchronously. Reach the underlying values with `apply` (see the `GetValueAsync` function in `Testing.cs`).
- Since outputs resolve asynchronously, the test relies on the framework's built-in support for asynchronous tests.

Past that setup, the raw inputs are available as plain values. The tags property is a map, so the check confirms that it's defined and that it holds an entry for the `Name` key. That's a small assertion, but the same approach reaches any property on any resource.

The second check asserts that the `userData` property is empty:

{{% choosable language "typescript" %}}

```typescript
// check 2: Instances must not use an inline userData script.
it("must not use userData (use an AMI instead)", function(done) {
    pulumi.all([infra.server.urn, infra.server.userData]).apply(([urn, userData]) => {
        if (userData) {
            done(new Error(`Illegal use of userData on server ${urn}`));
        } else {
            done();
        }
    });
});
```

{{% /choosable %}}
{{% choosable language "python" %}}

```python
class TestingWithMocks(unittest.IsolatedAsyncioTestCase):
    # ... setUp as shown above

    # check 2: Instances must not use an inline userData script.
    @pulumi.runtime.test
    def test_server_userdata(self):
        def check_user_data(args):
            urn, user_data = args
            self.assertFalse(user_data, f"illegal use of user_data on server {urn}")

        return pulumi.Output.all(self.server.urn, self.server.user_data).apply(check_user_data)
```

{{% /choosable %}}
{{% choosable language "go" %}}

```go
// check 2: Instances must not use an inline userData script.
pulumi.All(infra.server.URN(), infra.server.UserData).ApplyT(func(all []interface{}) error {
	urn := all[0].(pulumi.URN)
	userData := all[1].(string)

	assert.Emptyf(t, userData, "illegal use of userData on server %v", urn)
	wg.Done()
	return nil
})
```

{{% /choosable %}}
{{% choosable language "csharp" %}}

```csharp
// check 2: Instances must not use an inline userData script.
[Test]
public async Task InstanceMustNotUseInlineUserData()
{
    var resources = await Testing.RunAsync<WebserverStack>();

    var instance = resources.OfType<Instance>().FirstOrDefault();
    instance.Should().NotBeNull("EC2 Instance not found");

    var tags = await instance.UserData.GetValueAsync();
    tags.Should().BeNull();
}
```

{{% /choosable %}}
{{% choosable language "java" %}}

```java
// check 2: Instances must not use an inline userData script.
@Test
void instanceMustNotUseInlineUserData() {
    var result = PulumiTest
        .withMocks(new MyMocks())
        .withOptions(TestOptions.builder()
            // Project and stack names; they end up in the mocked resources' URNs.
            .projectName("project").stackName("stack").preview(false)
            .build())
        .runTest(App::stack);

    var instance = result.resources().stream()
        .filter(r -> r instanceof Instance)
        .map(r -> (Instance) r)
        .findFirst().orElse(null);

    assertNotNull(instance, "EC2 Instance not found");
    var urn = PulumiTest.extractValue(instance.urn());
    var userData = PulumiTest.extractValue(instance.userData());
    assertNull(userData, "Illegal use of userData on server " + urn);
}
```

{{% /choosable %}}

The third check takes a few more lines, because a security group may carry many ingress rules, and each of those rules may carry many CIDR blocks. The test walks all of them:

{{% choosable language "typescript" %}}

```typescript
// check 3: Instances must not have SSH open to the internet.
it("must not open port 22 (SSH) to the internet", function(done) {
    pulumi.all([infra.group.urn, infra.group.ingress]).apply(([ urn, ingress ]) => {
        if (ingress.find(rule =>
            rule.fromPort === 22 && (rule.cidrBlocks || []).find(block => block === "0.0.0.0/0"))) {
                done(new Error(`Illegal SSH port 22 open to the internet (CIDR 0.0.0.0/0) on group ${urn}`));
        } else {
            done();
        }
    });
});
```

{{% /choosable %}}
{{% choosable language "python" %}}

```python
class TestingWithMocks(unittest.IsolatedAsyncioTestCase):
    # ... setUp as shown above

    # check 3: Test if port 22 for ssh is exposed.
    @pulumi.runtime.test
    def test_security_group_rules(self):
        def check_security_group_rules(args):
            urn, ingress = args
            ssh_open = any(
                rule["from_port"] == 22
                and "0.0.0.0/0" in rule["cidr_blocks"]
                for rule in ingress
            )
            self.assertFalse(
                ssh_open,
                f"security group {urn} exposes port 22 to the internet (CIDR 0.0.0.0/0)",
            )

        return pulumi.Output.all(self.group.urn, self.group.ingress).apply(check_security_group_rules)
```

{{% /choosable %}}
{{% choosable language "go" %}}

```go
// check 3: Test if port 22 for ssh is exposed.
pulumi.All(infra.group.URN(), infra.group.Ingress).ApplyT(func(all []interface{}) error {
	urn := all[0].(pulumi.URN)
	ingress := all[1].([]ec2.SecurityGroupIngress)

	for _, i := range ingress {
		openToInternet := false
		for _, b := range i.CidrBlocks {
			if b == "0.0.0.0/0" {
				openToInternet = true
				break
			}
		}

		assert.Falsef(t, i.FromPort == 22 && openToInternet, "illegal SSH port 22 open to the internet (CIDR 0.0.0.0/0) on group %v", urn)
	}

	wg.Done()
	return nil
})
```

{{% /choosable %}}
{{% choosable language "csharp" %}}

```csharp
// check 3: Test if port 22 for ssh is exposed.
[Test]
public async Task SecurityGroupMustNotHaveSshPortsOpenToInternet()
{
    var resources = await Testing.RunAsync<WebserverStack>();

    foreach (var securityGroup in resources.OfType<SecurityGroup>())
    {
        var urn = await securityGroup.Urn.GetValueAsync();
        var ingress = await securityGroup.Ingress.GetValueAsync();
        foreach (var rule in ingress)
        {
            (rule.FromPort == 22 && rule.CidrBlocks.Any(b => b == "0.0.0.0/0"))
                .Should().BeFalse($"Illegal SSH port 22 open to the internet (CIDR 0.0.0.0/0) on group {urn}");
        }
    }
}
```

{{% /choosable %}}
{{% choosable language "java" %}}

```java
// check 3: Instances must not have SSH open to the internet.
@Test
void securityGroupMustNotHaveSshOpenToInternet() {
    var result = PulumiTest
        .withMocks(new MyMocks())
        .withOptions(TestOptions.builder()
            // Project and stack names; they end up in the mocked resources' URNs.
            .projectName("project").stackName("stack").preview(false)
            .build())
        .runTest(App::stack);

    for (var resource : result.resources()) {
        if (resource instanceof SecurityGroup group) {
            var urn = PulumiTest.extractValue(group.urn());
            var ingress = PulumiTest.extractValue(group.ingress());
            if (ingress != null) {
                for (var rule : ingress) {
                    var fromPort = PulumiTest.extractValue(rule.fromPort());
                    var cidrBlocks = PulumiTest.extractValue(rule.cidrBlocks());
                    boolean sshOpen = fromPort != null && fromPort == 22
                        && cidrBlocks != null && cidrBlocks.contains("0.0.0.0/0");
                    assertFalse(sshOpen, "Illegal SSH port 22 open to the internet "
                        + "(CIDR 0.0.0.0/0) on group " + urn);
                }
            }
        }
    }
}
```

{{% /choosable %}}

That's all three checks. Now run the tests.

## Run the tests

{{% choosable language "typescript" %}}

Run the Mocha tests with:

```bash
npx mocha --require tsx ec2tests.ts
```

{{% /choosable %}}
{{% choosable language "python" %}}
Run the Python tests with:

```bash
python -m unittest
```

{{% /choosable %}}
{{% choosable language "go" %}}
Run the Go tests with:

```bash
go test
```

{{% /choosable %}}
{{% choosable language "csharp" %}}
Run the C# tests with:

```bash
dotnet test
```

{{% /choosable %}}
{{% choosable language "java" %}}
Run the Java tests with:

```bash
mvn test
```

{{% /choosable %}}

All three tests fail, exactly as planned.

{{% choosable language "typescript" %}}

```output
  Infrastructure
    #server
      1) must have a name tag
      2) must not use userData (use an AMI instead)
    #group
      3) must not open port 22 (SSH) to the internet

  0 passing (454ms)
  3 failing
```

{{% /choosable %}}
{{% choosable language "python" %}}

```output
======================================================================
FAIL: test_security_group_rules (test_ec2.TestingWithMocks)
----------------------------------------------------------------------
...
======================================================================
FAIL: test_server_tags (test_ec2.TestingWithMocks)
----------------------------------------------------------------------
...
======================================================================
FAIL: test_server_userdata (test_ec2.TestingWithMocks)
----------------------------------------------------------------------
...
----------------------------------------------------------------------
Ran 3 tests in 0.034s

FAILED (failures=3)
```

{{% /choosable %}}
{{% choosable language "go" %}}

```output
--- FAIL: TestInfrastructure (0.00s)
...
        	Error:      	Should be false
        	Test:       	TestInfrastructure
        	Messages:   	illegal SSH port 22 open to the internet (CIDR 0.0.0.0/0) on group urn:pulumi:stack::project::aws:ec2/securityGroup:SecurityGroup::web-secgrp
...
        	Error:      	Expected nil, but got: (*string)(0xc000217390)
        	Test:       	TestInfrastructure
        	Messages:   	illegal use of userData on server urn:pulumi:stack::project::aws:ec2/instance:Instance::web-server-www
...
        	Error:      	"map[]" does not contain "Name"
        	Test:       	TestInfrastructure
        	Messages:   	missing a Name tag on server urn:pulumi:stack::project::aws:ec2/instance:Instance::web-server-www
FAIL	testing-unit-go	0.501s
```

{{% /choosable %}}
{{% choosable language "csharp" %}}

```output
X InstanceHasNameTag [387ms]
  Error Message:
   Expected tags not to be <null> because Tags are not defined.

X InstanceMustNotUseInlineUserData [17ms]
  Error Message:
   Expected tags to be <null>, but found "#!/bin/bash echo "Hello, World!" > index.html nohup python3 -m http.server 80 &".

X SecurityGroupMustNotHaveSshPortsOpenToInternet [11ms]
  Error Message:
   Expected boolean to be false because Illegal SSH port 22 open to the internet (CIDR 0.0.0.0/0) on group urn:pulumi:stack::project::pulumi:pulumi:Stack$aws:ec2/securityGroup:SecurityGroup::web-secgrp, but found True.

Test Run Failed.
Total tests: 3
     Failed: 3
```

{{% /choosable %}}
{{% choosable language "java" %}}

```output
[ERROR] Tests run: 3, Failures: 3, Errors: 0, Skipped: 0
[ERROR] Ec2Tests.instanceMustHaveNameTag -- AssertionFailedError: Server ... must have a Name tag
[ERROR] Ec2Tests.instanceMustNotUseInlineUserData -- AssertionFailedError: Illegal use of userData on server ...
[ERROR] Ec2Tests.securityGroupMustNotHaveSshOpenToInternet -- AssertionFailedError: Illegal SSH port 22 open to the internet (CIDR 0.0.0.0/0) on group ...
[ERROR] BUILD FAILURE
```

{{% /choosable %}}

Now fix the program so that it complies:

{{% choosable language "typescript" %}}

{{< code-filename file="index.ts" />}}

```typescript
import * as aws from "@pulumi/aws";

export const group = new aws.ec2.SecurityGroup("web-secgrp", {
    ingress: [
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});

// Look up the latest Amazon Linux 2 AMI.
const ami = aws.ec2.getAmiOutput({
    owners: ["amazon"],
    mostRecent: true,
    filters: [{ name: "name", values: ["amzn2-ami-hvm-*-x86_64-gp2"] }],
});

export const server = new aws.ec2.Instance("web-server-www", {
    instanceType: "t2.micro",
    securityGroups: [ group.name ], // reference the group object above
    ami: ami.id,
    tags: { Name: "webserver" },    // name tag
});
```

{{% /choosable %}}
{{% choosable language "python" %}}

{{< code-filename file="__main__.py" />}}

```python
import pulumi
from pulumi_aws import ec2

group = ec2.SecurityGroup('web-secgrp', ingress=[
    { "protocol": "tcp", "from_port": 80, "to_port": 80, "cidr_blocks": ["0.0.0.0/0"] },
])

# Look up the latest Amazon Linux 2 AMI.
ami = ec2.get_ami_output(
    owners=["amazon"],
    most_recent=True,
    filters=[{"name": "name", "values": ["amzn2-ami-hvm-*-x86_64-gp2"]}])

server = ec2.Instance("web-server-www",
    instance_type="t2.micro",
    security_groups=[ group.name ], # reference the group object above
    tags={'Name': 'webserver'},     # name tag
    ami=ami.id)
```

{{% /choosable %}}
{{% choosable language "go" %}}

{{< code-filename file="main.go" />}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type infrastructure struct {
	group  *ec2.SecurityGroup
	server *ec2.Instance
}

func createInfrastructure(ctx *pulumi.Context) (*infrastructure, error) {
	group, err := ec2.NewSecurityGroup(ctx, "web-secgrp", &ec2.SecurityGroupArgs{
		Ingress: ec2.SecurityGroupIngressArray{
			ec2.SecurityGroupIngressArgs{
				Protocol:   pulumi.String("tcp"),
				FromPort:   pulumi.Int(80),
				ToPort:     pulumi.Int(80),
				CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
			},
		},
	})
	if err != nil {
		return nil, err
	}

	// Look up the latest Amazon Linux 2 AMI.
	ami, err := ec2.LookupAmi(ctx, &ec2.LookupAmiArgs{
		Owners:     []string{"amazon"},
		MostRecent: pulumi.BoolRef(true),
		Filters: []ec2.GetAmiFilter{
			{
				Name:   "name",
				Values: []string{"amzn2-ami-hvm-*-x86_64-gp2"},
			},
		},
	})
	if err != nil {
		return nil, err
	}

	server, err := ec2.NewInstance(ctx, "web-server-www", &ec2.InstanceArgs{
		InstanceType:   pulumi.String("t2.micro"),
		SecurityGroups: pulumi.StringArray{group.Name}, // reference the group object above
		Ami:            pulumi.String(ami.Id),
		Tags:           pulumi.StringMap{"Name": pulumi.String("webserver")},
	})
	if err != nil {
		return nil, err
	}

	return &infrastructure{
		group:  group,
		server: server,
	}, nil
}
```

{{% /choosable %}}
{{% choosable language "csharp" %}}

{{< code-filename file="WebserverStack.cs" />}}

```csharp
using Pulumi;
using Pulumi.Aws.Ec2;
using Pulumi.Aws.Ec2.Inputs;

public class WebserverStack : Stack
{
    public WebserverStack()
    {
        var group = new SecurityGroup("web-secgrp", new SecurityGroupArgs
        {
            Ingress =
            {
                new SecurityGroupIngressArgs { Protocol = "tcp", FromPort = 80, ToPort = 80, CidrBlocks = { "0.0.0.0/0" } }
            }
        });

        // Look up the latest Amazon Linux 2 AMI.
        var ami = GetAmi.Invoke(new GetAmiInvokeArgs
        {
            Owners = { "amazon" },
            MostRecent = true,
            Filters =
            {
                new GetAmiFilterInputArgs { Name = "name", Values = { "amzn2-ami-hvm-*-x86_64-gp2" } }
            }
        });

        var server = new Instance("web-server-www", new InstanceArgs
        {
            InstanceType = "t2.micro",
            SecurityGroups = { group.Name }, // reference the group object above
            Ami = ami.Apply(ami => ami.Id),
            Tags = { { "Name", "webserver" } }  // name tag
        });
    }
}
```

{{% /choosable %}}
{{% choosable language "java" %}}

{{< code-filename file="App.java" />}}

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.ec2.Ec2Functions;
import com.pulumi.aws.ec2.Instance;
import com.pulumi.aws.ec2.InstanceArgs;
import com.pulumi.aws.ec2.SecurityGroup;
import com.pulumi.aws.ec2.SecurityGroupArgs;
import com.pulumi.aws.ec2.inputs.GetAmiArgs;
import com.pulumi.aws.ec2.inputs.GetAmiFilterArgs;
import com.pulumi.aws.ec2.inputs.SecurityGroupIngressArgs;
import com.pulumi.aws.ec2.outputs.GetAmiResult;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var group = new SecurityGroup("web-secgrp", SecurityGroupArgs.builder()
            .ingress(
                SecurityGroupIngressArgs.builder()
                    .protocol("tcp").fromPort(80).toPort(80).cidrBlocks("0.0.0.0/0")
                    .build())
            .build());

        // Look up the latest Amazon Linux 2 AMI.
        var ami = Ec2Functions.getAmi(GetAmiArgs.builder()
            .owners("amazon")
            .mostRecent(true)
            .filters(GetAmiFilterArgs.builder()
                .name("name")
                .values("amzn2-ami-hvm-*-x86_64-gp2")
                .build())
            .build());

        var server = new Instance("web-server-www", InstanceArgs.builder()
            .instanceType("t2.micro")
            .securityGroups(group.name())  // reference the group object above
            .ami(ami.applyValue(GetAmiResult::id))
            .tags(Map.of("Name", "webserver")) // name tag
            .build());
    }
}
```

{{% /choosable %}}

Then rerun the tests:

{{% choosable language "typescript" %}}

```output
Infrastructure
    #server
      ✓ must have a name tag
      ✓ must not use userData (use an AMI instead)
    #group
      ✓ must not open port 22 (SSH) to the internet

  3 passing (454ms)
```

{{% /choosable %}}
{{% choosable language "python" %}}

```output
----------------------------------------------------------------------
Ran 3 tests in 0.022s

OK
```

{{% /choosable %}}
{{% choosable language "go" %}}

```output
PASS
ok  	testing-unit-go	0.704s
```

{{% /choosable %}}
{{% choosable language "csharp" %}}

```output
Test Run Successful.
Total tests: 3
     Passed: 3
```

{{% /choosable %}}
{{% choosable language "java" %}}

```output
[INFO] Tests run: 3, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

{{% /choosable %}}

All three tests pass.

## Limitations

When using mocks for unit testing, it's important to understand that the mock server does not implement the full Pulumi engine. This means certain features that rely on the engine's deployment orchestration will not execute during mock-based tests.

### Lifecycle hooks and transforms

Lifecycle hooks and resource transforms are not executed in mock tests. While your program can register hooks and transforms with the mock server, they will not actually run during test execution.

This limitation exists because implementing full hook and transform support would require reimplementing significant portions of the Pulumi engine in each language SDK. Since mocks are designed to run fast and deterministically without external dependencies, this trade-off is intentional.

If your program uses lifecycle hooks or transforms, structure your tests to work around this limitation:

1. **Test the logic separately**: Extract the logic from hooks and transforms into standalone functions that can be unit tested independently.
1. **Mock the expected outcomes**: Configure your mocks to return resource state that reflects what would happen after hooks or transforms execute.
1. **Use integration tests**: For end-to-end validation of hook and transform behavior, use integration tests that deploy actual resources to a testing environment.

For example, if you have a transform that adds default tags to all resources, your mock's `newResource` function can return resource state that already includes those tags, simulating the transform's effect without actually executing it.

## Full example

{{% choosable language "typescript" %}}

The full code for this guide is available in the examples repository: [Unit Tests in TypeScript](https://github.com/pulumi/examples/tree/master/testing-unit-ts).

&nbsp;
{{% /choosable %}}

{{% choosable language "python" %}}

The full code for this guide is available in the examples repository: [Unit Tests in Python](https://github.com/pulumi/examples/tree/master/testing-unit-py).

&nbsp;
{{% /choosable %}}

{{% choosable language "go" %}}

The full code for this guide is available in the examples repository: [Unit Tests in Go](https://github.com/pulumi/examples/tree/master/testing-unit-go).

&nbsp;
{{% /choosable %}}

{{% choosable language "csharp" %}}

The full code for this guide is available in the examples repository: [Unit Tests in C#](https://github.com/pulumi/examples/tree/master/testing-unit-cs).

&nbsp;

{{% /choosable %}}
{{% choosable language "java" %}}

A Java unit testing example is not yet available in the examples repository. Contributions are welcome at [pulumi/examples](https://github.com/pulumi/examples).

&nbsp;

{{% /choosable %}}

## Learn more

- [Integration testing](/docs/iac/guides/testing/integration/) deploys real resources and checks them end to end, which is where lifecycle hooks, transforms, and anything else the mock server doesn't implement belong.
- [Inputs and outputs](/docs/iac/concepts/inputs-outputs/) explains why resource properties resolve asynchronously, and how `apply` reaches their values.
- [Pulumi Policies](/docs/insights/policy/) enforces rules like the three in this guide across every stack in your organization, rather than one program at a time.
