---
title: Unit Testing
meta_desc: "Guide to unit testing of Pulumi programs: mock-based tests across Node.js, Python, Go, and .NET."
weight: 1

menu:
  userguides:
    parent: testing
---

Pulumi programs are authored in a general-purpose language like TypeScript, Python, Go, or C#. The full power of each language is available, including access to tools and libraries for that runtime, including testing frameworks.

When running an update, your Pulumi program talks to the Pulumi CLI to orchestrate the deployment. The idea of **unit tests** is to cut this communication channel and replace the engine with mocks. The mocks respond to the commands from within the same OS process and return dummy data for each call that your Pulumi program makes.

Because mocks don't execute any real work, unit tests run very fast. Also, they can be made deterministic because tests don't depend on the behavior of any external system.

## Get Started

Unit tests are supported in all existing Pulumi runtimes: Node.js, Python, Go, and .NET.

Let's build a sample test suite. The example uses AWS resources, but the same capabilities and workflow apply to any Pulumi provider. To follow along, complete the [Get Started with AWS]({{< relref "/docs/get-started/aws" >}}) guide to set up a basic Pulumi program in your language of choice.

## Sample Program

Throughout this guide, we are testing a program that creates a simple AWS EC2-based webserver. We want to develop unit tests to ensure:

- Instances have a Name tag.
- Instances must not use an inline `userData` script&mdash;we must use a virtual machine image.
- Instances must not have SSH open to the Internet.

Our starting code is loosely based on the [aws-js-webserver example](https://github.com/pulumi/examples/tree/master/aws-js-webserver):

<div class="note note-info" role="alert">
    <p>
        Choose the language below to adjust the contents of this guide. Your choice is applied throughout the guide.
    </p>
</div>

{{< chooser language "typescript,python,go,csharp" / >}}

<div></div>

{{% choosable language "typescript" %}}

**index.ts**:

```typescript
import * as aws from "@pulumi/aws";

export const group = new aws.ec2.SecurityGroup("web-secgrp", {
    ingress: [
        { protocol: "tcp", fromPort: 22, toPort: 22, cidrBlocks: ["0.0.0.0/0"] },
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});

const userData = `#!/bin/bash echo "Hello, World!" > index.html nohup python -m SimpleHTTPServer 80 &`;

export const server = new aws.ec2.Instance("web-server-www", {
    instanceType: "t2.micro",
    securityGroups: [ group.name ], // reference the group object above
    ami: "ami-c55673a0",            // AMI for us-east-2 (Ohio)
    userData: userData,             // start a simple webserver
});
```

{{% /choosable %}}
{{% choosable language "python" %}}

**infra.py**:

```python
import pulumi
from pulumi_aws import ec2

group = ec2.SecurityGroup('web-secgrp', ingress=[
    { "protocol": "tcp", "from_port": 22, "to_port": 22, "cidr_blocks": ["0.0.0.0/0"] },
    { "protocol": "tcp", "from_port": 80, "to_port": 80, "cidr_blocks": ["0.0.0.0/0"] },
])

user_data = '#!/bin/bash echo "Hello, World!" > index.html nohup python -m SimpleHTTPServer 80 &'

server = ec2.Instance('web-server-www;',
    instance_type="t2.micro",
    security_groups=[ group.name ], # reference the group object above
    ami="ami-c55673a0",             # AMI for us-east-2 (Ohio)
    user_data=user_data)            # start a simple web server
```

{{% /choosable %}}
{{% choosable language "go" %}}

**main.go**:

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/go/aws/ec2"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
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
                FromPort:   pulumi.Int(22),
                ToPort:     pulumi.Int(22),
                CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
            },
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

    const userData = `#!/bin/bash echo "Hello, World!" > index.html nohup python -m SimpleHTTPServer 80 &`

    server, err := ec2.NewInstance(ctx, "web-server-www", &ec2.InstanceArgs{
        InstanceType:   pulumi.String("t2-micro"),
        SecurityGroups: pulumi.StringArray{group.ID()}, // reference the group object above
        Ami:            pulumi.String("ami-c55673a0"),  // AMI for us-east-2 (Ohio)
        UserData:       pulumi.String(userData),        // start a simple web server
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

**WebserverStack.cs**:

``` csharp
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
                new SecurityGroupIngressArgs { Protocol = "tcp", FromPort = 22, ToPort = 22, CidrBlocks = { "0.0.0.0/0" } },
                new SecurityGroupIngressArgs { Protocol = "tcp", FromPort = 80, ToPort = 80, CidrBlocks = { "0.0.0.0/0" } }
            }
        });

        var userData = "#!/bin/bash echo \"Hello, World!\" > index.html nohup python -m SimpleHTTPServer 80 &";

        var server = new Instance("web-server-www", new InstanceArgs
        {
            InstanceType = "t2.micro",
            SecurityGroups = { group.Name }, // reference the group object above
            Ami = "ami-c55673a0",            // AMI for us-east-2 (Ohio)
            UserData = userData              // start a simple webserver
        });
    }
}
```

{{% /choosable %}}

This basic Pulumi program allocates a security group and an instance. Notice, however, that we are violating all three of the rules stated above&mdash;let's write some tests!

## Install the unit testing framework

You are free to use your favorite frameworks and libraries for writing unit tests and assertions.

{{% choosable language "typescript" %}}

This guide uses Mocha as the testing framework. [Install Mocha](https://mochajs.org/#installation) to your development environment.

Then, install additional NPM modules to your program:

```bash
npm install mocha @types/mocha ts-node
```

{{% /choosable %}}

{{% choosable language python %}}

We use the built-in [`unittest`](https://docs.python.org/3/library/unittest.html) framework, so no need to install anything.

{{% /choosable %}}

{{% choosable language go %}}

We use the built-in `go test` command, so no need to install anything.

{{% /choosable %}}

{{% choosable language "csharp" %}}

We use [NUnit](https://nunit.org/) test framework to define and run the tests, [Moq](https://github.com/moq/moq4) for mocks, and [FluentAssertions](https://github.com/fluentassertions/fluentassertions) for assertions.

Install the corresponding NuGet packages to your program:

```bash
dotnet add package NUnit
dotnet add package NUnit3TestAdapter
dotnet add package Moq
dotnet add package FluentAssertions
```

{{% /choosable %}}

## Add Mocks

Let's add the following code to mock the external calls to the Pulumi CLI.

{{% choosable language "typescript" %}}
**ec2tests.ts**

```ts
import * as pulumi from "@pulumi/pulumi";

pulumi.runtime.setMocks({
    newResource: function(type: string, name: string, inputs: any): {id: string, state: any} {
        return {
            id: inputs.name + "_id",
            state: inputs,
        };
    },
    call: function(token: string, args: any, provider?: string) {
        return args;
    },
});
```

{{% /choosable %}}

{{% choosable language python %}}

**test_ec2.py**:

```python
import pulumi

class MyMocks(pulumi.runtime.Mocks):
    def new_resource(self, type_, name, inputs, provider, id_):
        return [name + '_id', inputs]
    def call(self, token, args, provider):
        return {}

pulumi.runtime.set_mocks(MyMocks())
```

{{% /choosable %}}

{{% choosable language go %}}
**main_test.go**

```go
import (
    "github.com/pulumi/pulumi/pkg/resource"
)

type mocks int

func (mocks) NewResource(typeToken, name string, inputs resource.PropertyMap, provider, id string) (string, resource.PropertyMap, error) {
    return name + "_id", inputs, nil
}

func (mocks) Call(token string, args resource.PropertyMap, provider string) (resource.PropertyMap, error) {
    return args, nil
}
```

{{% /choosable %}}

{{% choosable language "csharp" %}}
**Testing.cs**

```csharp
public static class Testing
{
    public static Task<ImmutableArray<Resource>> RunAsync<T>() where T : Stack, new()
    {
        var mocks = new Mock<IMocks>();
        mocks.Setup(m => m.NewResourceAsync(It.IsAny<string>(), It.IsAny<string>(),
                It.IsAny<ImmutableDictionary<string, object>>(), It.IsAny<string>(), It.IsAny<string>()))
            .ReturnsAsync((string type, string name, ImmutableDictionary<string, object> inputs, string? provider, string? id) => (id ?? "", inputs));
        mocks.Setup(m => m.CallAsync(It.IsAny<string>(), It.IsAny<ImmutableDictionary<string, object>>(), It.IsAny<string>()))
            .ReturnsAsync((string token, ImmutableDictionary<string, object> args, string? provider) => args);
        return Deployment.TestAsync<T>(mocks.Object, new TestOptions { IsPreview = false });
    }
}
```

{{% /choosable %}}

## Write the Tests

{{% choosable language "typescript" %}}
The overall structure and scaffolding of our tests will look like any ordinary Mocha testing:

**ec2tests.ts**:

```typescript
import * as pulumi from "@pulumi/pulumi";
import "mocha";

pulumi.runtime.setMocks({
    // ... mocks as shown above
});

// It's important to import the program _after_ the mocks are defined.
import * as infra from "./index";

describe("Infrastructure", function() {
    const server = infra.server;
    describe("#server", function() {
        // TODO(check 1): Instances have a Name tag.
        // TODO(check 2): Instances must not use an inline userData script.
    });

    const group = infra.group;
    describe("#group", function() {
        // TODO(check 3): Instances must not have SSH open to the Internet.
    });
});
```

{{% /choosable %}}
{{% choosable language "python" %}}
The overall structure and scaffolding of our tests will look like any ordinary Python's unittest testing:

**test_ec2.py**:

```python
import unittest
import pulumi

# ... MyMocks as shown above
pulumi.runtime.set_mocks(MyMocks())

# It's important to import `infra` _after_ the mocks are defined.
import infra

class TestingWithMocks(unittest.TestCase):
    # TODO(check 1): Instances have a Name tag.
    # TODO(check 2): Instances must not use an inline userData script.
    # TODO(check 3): Instances must not have SSH open to the Internet.
```

{{% /choosable %}}
{{% choosable language "go" %}}

The overall structure and scaffolding of our tests will look like any ordinary Go test:

**main_test.go**:

```go
package main

import (
    "sync"
    "testing"

    "github.com/pulumi/pulumi-aws/sdk/go/aws/ec2"
    "github.com/pulumi/pulumi/pkg/resource"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
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
        // TODO(check 3): Instances must not have SSH open to the Internet.

        wg.Wait()
        return nil
    }, pulumi.WithMocks("project", "stack", mocks(0)))
    assert.NoError(t, err)
}
```

{{% /choosable %}}
{{% choosable language "csharp" %}}
The overall structure and scaffolding of our tests will look like any ordinary NUnit testing:

**WebserverStackTests.cs**:

```csharp
using NUnit.Framework;

namespace UnitTesting
{
	  [TestFixture]
	  public class WebserverStackTests
	  {
        // TODO(check 1): Instances have a Name tag.
        // TODO(check 2): Instances must not use an inline userData script.
        // TODO(check 3): Instances must not have SSH open to the Internet.
	  }
}
```

{{% /choosable %}}

Now let's implement our first test: ensuring that instances have a `Name` tag. To verify this we need to grab hold of the EC2 instance object, and check the relevant property:

{{% choosable language "typescript" %}}

```typescript
// check 1: Instances have a Name tag.
it("must have a name tag", function(done) {
    pulumi.all([server.urn, server.tags]).apply(([urn, tags]) => {
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
# check 1: Instances have a Name tag.
@pulumi.runtime.test
def test_server_tags(self):
    def check_tags(args):
        urn, tags = args
        self.assertIsNotNone(tags, f'server {urn} must have tags')
        self.assertIn('Name', tags, 'server {urn} must have a name tag')

    return pulumi.Output.all(infra.server.urn, infra.server.tags).apply(check_tags)
```

{{% /choosable %}}
{{% choosable language "go" %}}

```go
// check 1: Instances have a Name tag.
pulumi.All(infra.server.URN(), infra.server.Tags).ApplyT(func(all []interface{}) error {
    urn := all[0].(pulumi.URN)
    tags := all[1].(map[string]interface{})

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

This looks like a normal test, with a few noteworthy pieces:

- Since we're querying resource state without doing a deployment, there are many properties whose values will be undefined. This includes any output properties computed by your cloud provider that you did not explicitly return from the mocks. That's fine for these tests&mdash;we're checking for valid inputs anyway.
- Because all Pulumi resource properties are [outputs](https://www.pulumi.com/docs/intro/concepts/programming-model/#outputs)&mdash;since many of them are computed asynchronously&mdash;we need to use the `apply` method to get access to the values.
- Finally, since these outputs are resolved asynchronously, we need to use the framework's built-in asynchronous test capability.

After we've gotten through that setup, we get access to the raw inputs as plain values. The tags property is a map, so we make sure it is (1) defined, and (2) not missing an entry for the `Name` key. This is very basic, but we can check anything!

Now let's write our second check to assert that `userdata` property is empty:

{{% choosable language "typescript" %}}

```typescript
// check 2: Instances must not use an inline userData script.
it("must not use userData (use an AMI instead)", function(done) {
    pulumi.all([server.urn, server.userData]).apply(([urn, userData]) => {
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
# check 2: Instances must not use an inline userData script.
@pulumi.runtime.test
def test_server_userdata(self):
    def check_user_data(args):
        urn, user_data = args
        self.assertFalse(user_data, f'illegal use of user_data on server {urn}')

    return pulumi.Output.all(infra.server.urn, infra.server.user_data).apply(check_user_data)
```

{{% /choosable %}}
{{% choosable language "go" %}}

```go
// check 2: Instances must not use an inline userData script.
pulumi.All(infra.server.URN(), infra.server.UserData).ApplyT(func(all []interface{}) error {
    urn := all[0].(pulumi.URN)
    userData := all[1].(*string)

    assert.Nilf(t, userData, "illegal use of userData on server %v", urn)
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

And finally, let's write our third check. It’s a bit more complex because we're searching for ingress rules associated with a security group&mdash;of which there may be many&mdash;and CIDR blocks within those ingress rules&mdash;of which there may also be many. But it's still several lines of code:

{{% choosable language "typescript" %}}

```typescript
// check 3: Instances must not have SSH open to the Internet.
it("must not open port 22 (SSH) to the Internet", function(done) {
    pulumi.all([ group.urn, group.ingress ]).apply(([ urn, ingress ]) => {
        if (ingress.find(rule =>
            rule.fromPort === 22 && (rule.cidrBlocks || []).find(block => block === "0.0.0.0/0"))) {
                done(new Error(`Illegal SSH port 22 open to the Internet (CIDR 0.0.0.0/0) on group ${urn}`));
        } else {
            done();
        }
    });
});
```

{{% /choosable %}}
{{% choosable language "python" %}}

```python
# check 3: Test if port 22 for ssh is exposed.
@pulumi.runtime.test
def test_security_group_rules(self):
    def check_security_group_rules(args):
        urn, ingress = args
        ssh_open = any([rule['from_port'] == 22 and any([block == "0.0.0.0/0" for block in rule['cidr_blocks']]) for rule in ingress])
        self.assertFalse(ssh_open, f'security group {urn} exposes port 22 to the Internet (CIDR 0.0.0.0/0)')

    return pulumi.Output.all(infra.group.urn, infra.group.ingress).apply(check_security_group_rules)
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

        assert.Falsef(t, i.FromPort == 22 && openToInternet, "illegal SSH port 22 open to the Internet (CIDR 0.0.0.0/0) on group %v", urn)
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
                .Should().BeFalse($"Illegal SSH port 22 open to the Internet (CIDR 0.0.0.0/0) on group {urn}");
        }
    }
}
```

{{% /choosable %}}

That's it&mdash;now let's run the tests.

## Run the Tests

{{% choosable language "typescript" %}}

When running Mocha tests, we have to pass three additional pieces of information:

- Your project name, which can be supplied with the `PULUMI_NODEJS_PROJECT` environment variable.
- Your stack name, which can be supplied with the `PULUMI_NODEJS_STACK` environment variable.
- Switch the engine to the test mode by setting `PULUMI_TEST_MODE` to `true`.

The command line to run your Mocha tests would therefore be:

```bash
$ PULUMI_TEST_MODE=true  \
  PULUMI_NODEJS_STACK="my-ws" \
  PULUMI_NODEJS_PROJECT="dev" \
  mocha -r ts-node/register ec2tests.ts
```

{{% /choosable %}}
{{% choosable language "python" %}}
Run the following command to execute your Python tests:

```bash
$ python -m unittest
```

{{% /choosable %}}
{{% choosable language "go" %}}
Run the following command to execute your Go tests:

```bash
$ go test
```

{{% /choosable %}}
{{% choosable language "csharp" %}}
Run the following command to execute your Python tests:

```bash
$ dotnet test
```

{{% /choosable %}}

Running this will tell us that we have three failing tests, as we had planned.

{{% choosable language "typescript" %}}

```bash
  Infrastructure
    #server
      1) must have a name tag
      2) must not use userData (use an AMI instead)
    #group
      3) must not open port 22 (SSH) to the Internet


  0 passing (454ms)
  3 failing
```

{{% /choosable %}}
{{% choosable language "python" %}}

```bash
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

```bash
--- FAIL: TestInfrastructure (0.00s)
...
        	Error:      	Should be false
        	Test:       	TestInfrastructure
        	Messages:   	illegal SSH port 22 open to the Internet (CIDR 0.0.0.0/0) on group urn:pulumi:stack::project::aws:ec2/securityGroup:SecurityGroup::web-secgrp
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

```bash
X InstanceHasNameTag [387ms]
  Error Message:
   Expected tags not to be <null> because Tags are not defined.

X InstanceMustNotUseInlineUserData [17ms]
  Error Message:
   Expected tags to be <null>, but found "#!/bin/bash echo "Hello, World!" > index.html nohup python -m SimpleHTTPServer 80 &".

X SecurityGroupMustNotHaveSshPortsOpenToInternet [11ms]
  Error Message:
   Expected boolean to be false because Illegal SSH port 22 open to the Internet (CIDR 0.0.0.0/0) on group urn:pulumi:stack::project::pulumi:pulumi:Stack$aws:ec2/securityGroup:SecurityGroup::web-secgrp, but found True.

Test Run Failed.
Total tests: 3
     Failed: 3
```

{{% /choosable %}}

Let's fix our program to comply:

{{% choosable language "typescript" %}}
**index.ts**

```typescript
import * as aws from "@pulumi/aws";

export const group = new aws.ec2.SecurityGroup("web-secgrp", {
    ingress: [
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});

export const server = new aws.ec2.Instance("web-server-www", {
    instanceType: "t2.micro",
    securityGroups: [ group.name ], // reference the group object above
    ami: "ami-c55673a0",            // AMI for us-east-2 (Ohio)
    tags: { Name: "www-server" },   // name tag
});
```

{{% /choosable %}}
{{% choosable language "python" %}}
**infra.py**

```python
import pulumi
from pulumi_aws import ec2

group = ec2.SecurityGroup('web-secgrp', ingress=[
    { "protocol": "tcp", "from_port": 80, "to_port": 80, "cidr_blocks": ["0.0.0.0/0"] },
])

server = ec2.Instance('web-server-www;',
    instance_type="t2.micro",
    security_groups=[ group.name ], # reference the group object above
    tags={'Name': 'webserver'},     # name tag
    ami="ami-c55673a0")             # AMI for us-east-2 (Ohio)
```

{{% /choosable %}}
{{% choosable language "go" %}}
**main.go**

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/go/aws/ec2"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
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

    server, err := ec2.NewInstance(ctx, "web-server-www", &ec2.InstanceArgs{
        InstanceType:   pulumi.String("t2-micro"),
        SecurityGroups: pulumi.StringArray{group.ID()}, // reference the group object above
        Ami:            pulumi.String("ami-c55673a0"),  // AMI for us-east-2 (Ohio)
        Tags:           pulumi.Map{ "Name": pulumi.String("webserver") },
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
**WebserverStack.cs**

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

        var server = new Instance("web-server-www", new InstanceArgs
        {
            InstanceType = "t2.micro",
            SecurityGroups = { group.Name }, // reference the group object above
            Ami = "ami-c55673a0",            // AMI for us-east-2 (Ohio)
            Tags = { { "Name", "webserver" }}// name tag
        });
    }
}
```

{{% /choosable %}}

And then rerun our tests:

{{% choosable language "typescript" %}}

```
Infrastructure
    #server
      ✓ must have a name tag
      ✓ must not use userData (use an AMI instead)
    #group
      ✓ must not open port 22 (SSH) to the Internet


  3 passing (454ms)
```

{{% /choosable %}}
{{% choosable language "python" %}}

```
----------------------------------------------------------------------
Ran 3 tests in 0.022s

OK
```

{{% /choosable %}}
{{% choosable language "go" %}}

```
PASS
ok  	testing-unit-go	0.704s
```

{{% /choosable %}}
{{% choosable language "csharp" %}}

```
Test Run Successful.
Total tests: 3
     Passed: 3
```

{{% /choosable %}}

All the tests passed!

## Full Example

{{% choosable language "typescript" %}}
The full code for this guide is available in the examples repository: [Unit Tests in TypeScript](https://github.com/pulumi/examples/tree/master/testing-unit-ts).
{{% /choosable %}}
{{% choosable language "python" %}}
The full code for this guide is available in the examples repository: [Unit Tests in Python](https://github.com/pulumi/examples/tree/master/testing-unit-py).
{{% /choosable %}}
{{% choosable language "go" %}}
The full code for this guide is available in the examples repository: [Unit Tests in Go](https://github.com/pulumi/examples/tree/master/testing-unit-go).
{{% /choosable %}}
{{% choosable language "csharp" %}}
The full code for this guide is available in the examples repository: [Unit Tests in C#](https://github.com/pulumi/examples/tree/master/testing-unit-cs).
{{% /choosable %}}
