---
title: "Pulumi Command Provider 1.0 Release"

date: 2024-07-01T10:00:00-07:00

draft: false

meta_desc: >-
  The 1.0 release of the Pulumi Command provider marks its general availability (GA)
  and expands support for copying assets to remote hosts.

meta_image: meta.png

authors:
  - thomas-kappler

# None of the tags in BLOGGING.md seem to match, but `providers` exists already
tags:
  - providers

# The social copy used to promote this post on Twitter and Linkedin. These
# properties do not actually create the post and have no effect on the
# generated blog page. They are here strictly for reference.

# Here are some examples of posts we have made in the past for inspiration:
# https://www.linkedin.com/feed/update/urn:li:activity:7171191945841561601
# https://www.linkedin.com/feed/update/urn:li:activity:7169021002394296320
# https://www.linkedin.com/feed/update/urn:li:activity:7155606616455737345
# https://twitter.com/PulumiCorp/status/1763265391042654623
# https://twitter.com/PulumiCorp/status/1762900472489185492
# https://twitter.com/PulumiCorp/status/1755637618631405655

social:
  twitter:
  linkedin:
search:
  keywords:
    - Command
    - Provider
    - Command Provider
    - General Availability
---

Today, we’re happy to announce the 1.0 release of the [Pulumi Command](https://www.pulumi.com/registry/packages/command/) provider. This release marks the provider’s official transition from preview status to general availability (GA).
Since its first preview release in late 2021, thousands of Pulumi users incorporated the Command package into their cloud infrastructure projects to help manage local and remote command execution and filesystem operations. In fact, the Command provider is already our ninth-most popular provider, so it's time to make things official!

<!--more-->

The Pulumi Command Provider enables you to execute commands and scripts either locally or remotely as part of the Pulumi resource model, enabling stateful command execution. It also has convenient support for copying assets via SSH. Being able to run arbitrary commands opens up a wide variety of scenarios and integrations with other tools and systems.

Some of the provider's popular uses include:

- Running a command locally after creating a resource, to register it with an external service
- Running a command locally before deleting a resource, to deregister it with an external service
- Running a command on a remote host immediately after creating it
- Copying a file to a remote host after creating it (potentially as a script to be executed afterwards)
- As a simple alternative to some use cases for Dynamic Providers, by running appropriate commands in the different stages of the Pulumi life cycle.

Here’s a simple example of running an arbitrary command when another resource changes: once an AWS Lambda function is deployed, we call it and it responds with a message that is custom to the current Pulumi stack. In a real-world scenario, we could wait for a number of other resources to be deployed as well, and have the Lambda perform registration or initialization of services.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
import * as aws from "@pulumi/aws";
import { local } from "@pulumi/command";
import { getStack } from "@pulumi/pulumi";

const f = new aws.lambda.CallbackFunction("f", {
    publish: true,
    callback: async (ev: any) => {
        return `Stack ${ev.stackName} is deployed!`;
    }
});

const invoke = new local.Command("execf", {
    create: `aws lambda invoke --function-name "$FN" --payload '{"stackName": "${getStack()}"}' --cli-binary-format raw-in-base64-out out.txt >/dev/null && cat out.txt | tr -d '"'  && rm out.txt`,
    environment: {
        FN: f.qualifiedArn,
        AWS_REGION: aws.config.region!,
        AWS_PAGER: "",
    },
}, { dependsOn: f })

export const output = invoke.stdout;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import json
import pulumi_aws as aws
import pulumi_command as command

lambda_role = aws.iam.Role("lambdaRole", assume_role_policy=json.dumps({
    "Version": "2012-10-17",
    "Statement": [{
        "Action": "sts:AssumeRole",
        "Effect": "Allow",
        "Principal": {
            "Service": "lambda.amazonaws.com",
        },
    }],
}))

lambda_function = aws.lambda_.Function("lambdaFunction",
    name="f",
    publish=True,
    role=lambda_role.arn,
    handler="index.handler",
    runtime=aws.lambda_.Runtime.NODE_JS20D_X,
    code=pulumi.FileArchive("./handler"))

aws_config = pulumi.Config("aws")
aws_region = aws_config.require("region")

invoke_command = command.local.Command("invokeCommand",
    create=f"aws lambda invoke --function-name \"$FN\" --payload '{{\"stackName\": \"{pulumi.get_stack()}\"}}' --cli-binary-format raw-in-base64-out out.txt >/dev/null && cat out.txt | tr -d '\"'  && rm out.txt",
    environment={
        "FN": lambda_function.arn,
        "AWS_REGION": aws_region,
        "AWS_PAGER": "",
    },
    opts = pulumi.ResourceOptions(depends_on=[lambda_function]))

pulumi.export("output", invoke_command.stdout)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"encoding/json"
	"fmt"

	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/iam"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/lambda"
	"github.com/pulumi/pulumi-command/sdk/go/command/local"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		awsConfig := config.New(ctx, "aws")
		awsRegion := awsConfig.Require("region")

		tmpJSON0, err := json.Marshal(map[string]interface{}{
			"Version": "2012-10-17",
			"Statement": []map[string]interface{}{
				{
					"Action": "sts:AssumeRole",
					"Effect": "Allow",
					"Principal": map[string]interface{}{
						"Service": "lambda.amazonaws.com",
					},
				},
			},
		})
		if err != nil {
			return err
		}
		json0 := string(tmpJSON0)
		lambdaRole, err := iam.NewRole(ctx, "lambdaRole", &iam.RoleArgs{
			AssumeRolePolicy: pulumi.String(json0),
		})
		if err != nil {
			return err
		}
		lambdaFunction, err := lambda.NewFunction(ctx, "lambdaFunction", &lambda.FunctionArgs{
			Name:    pulumi.String("f"),
			Publish: pulumi.Bool(true),
			Role:    lambdaRole.Arn,
			Handler: pulumi.String("index.handler"),
			Runtime: pulumi.String(lambda.RuntimeNodeJS20dX),
			Code:    pulumi.NewFileArchive("./handler"),
		})
		if err != nil {
			return err
		}
		invokeCommand, err := local.NewCommand(ctx, "invokeCommand", &local.CommandArgs{
			Create: pulumi.String(fmt.Sprintf("aws lambda invoke --function-name \"$FN\" --payload '{\"stackName\": \"%v\"}' --cli-binary-format raw-in-base64-out out.txt >/dev/null && cat out.txt | tr -d '\"'  && rm out.txt", ctx.Stack())),
			Environment: pulumi.StringMap{
				"FN":         lambdaFunction.Arn,
				"AWS_REGION": pulumi.String(awsRegion),
				"AWS_PAGER":  pulumi.String(""),
			},
		}, pulumi.DependsOn([]pulumi.Resource{
			lambdaFunction,
		}))
		if err != nil {
			return err
		}
		ctx.Export("output", invokeCommand.Stdout)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Text.Json;
using Pulumi;
using Aws = Pulumi.Aws;
using Command = Pulumi.Command;

return await Deployment.RunAsync(() =>
{
    var awsConfig = new Config("aws");

    var lambdaRole = new Aws.Iam.Role("lambdaRole", new()
    {
        AssumeRolePolicy = JsonSerializer.Serialize(new Dictionary<string, object?>
        {
            ["Version"] = "2012-10-17",
            ["Statement"] = new[]
            {
                new Dictionary<string, object?>
                {
                    ["Action"] = "sts:AssumeRole",
                    ["Effect"] = "Allow",
                    ["Principal"] = new Dictionary<string, object?>
                    {
                        ["Service"] = "lambda.amazonaws.com",
                    },
                },
            },
        }),
    });

    var lambdaFunction = new Aws.Lambda.Function("lambdaFunction", new()
    {
        Name = "f",
        Publish = true,
        Role = lambdaRole.Arn,
        Handler = "index.handler",
        Runtime = Aws.Lambda.Runtime.NodeJS20dX,
        Code = new FileArchive("./handler"),
    });

    var invokeCommand = new Command.Local.Command("invokeCommand", new()
    {
        Create = $"aws lambda invoke --function-name \"$FN\" --payload '{{\"stackName\": \"{Deployment.Instance.StackName}\"}}' --cli-binary-format raw-in-base64-out out.txt >/dev/null && cat out.txt | tr -d '\"'  && rm out.txt",
        Environment =
        {
            { "FN", lambdaFunction.Arn },
            { "AWS_REGION", awsConfig.Require("region") },
            { "AWS_PAGER", "" },
        },
    }, new CustomResourceOptions
    {
        DependsOn =
        {
            lambdaFunction,
        },
    });

    return new Dictionary<string, object?>
    {
        ["output"] = invokeCommand.Stdout,
    };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.iam.Role;
import com.pulumi.aws.iam.RoleArgs;
import com.pulumi.aws.lambda.Function;
import com.pulumi.aws.lambda.FunctionArgs;
import com.pulumi.command.local.Command;
import com.pulumi.command.local.CommandArgs;
import static com.pulumi.codegen.internal.Serialization.*;
import com.pulumi.resources.CustomResourceOptions;
import com.pulumi.asset.FileArchive;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var awsConfig = ctx.config("aws");
        var awsRegion = awsConfig.require("region");

        var lambdaRole = new Role("lambdaRole", RoleArgs.builder()
                .assumeRolePolicy(serializeJson(
                        jsonObject(
                                jsonProperty("Version", "2012-10-17"),
                                jsonProperty("Statement", jsonArray(jsonObject(
                                        jsonProperty("Action", "sts:AssumeRole"),
                                        jsonProperty("Effect", "Allow"),
                                        jsonProperty("Principal", jsonObject(
                                                jsonProperty("Service", "lambda.amazonaws.com")))))))))
                .build());

        var lambdaFunction = new Function("lambdaFunction", FunctionArgs.builder()
                .name("f")
                .publish(true)
                .role(lambdaRole.arn())
                .handler("index.handler")
                .runtime("nodejs20.x")
                .code(new FileArchive("./handler"))
                .build());

        var lambdaInvokeOut = lambdaFunction.arn().applyValue(arn -> {
            var invokeCommand = new Command("invokeCommand", CommandArgs.builder()
                    .create(String.format(
                            "aws lambda invoke --function-name \"$FN\" --payload '{\"stackName\": \"%s\"}' --cli-binary-format raw-in-base64-out out.txt >/dev/null && cat out.txt | tr -d '\"'  && rm out.txt",
                            ctx.stackName()))
                    .environment(Map.ofEntries(
                            Map.entry("FN", arn),
                            Map.entry("AWS_REGION", awsRegion),
                            Map.entry("AWS_PAGER", "")))
                    .build(),
                    CustomResourceOptions.builder()
                            .dependsOn(lambdaFunction)
                            .build());

            return invokeCommand.stdout();
        });

        ctx.export("output", lambdaInvokeOut);
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml

resources:
  lambdaRole:
    type: aws:iam:Role
    properties:
      assumeRolePolicy:
        fn::toJSON:
          Version: "2012-10-17"
          Statement:
            - Action: sts:AssumeRole
              Effect: Allow
              Principal:
                Service: lambda.amazonaws.com

  lambdaFunction:
    type: aws:lambda:Function
    properties:
      name: f
      publish: true
      role: ${lambdaRole.arn}
      handler: index.handler
      runtime: "nodejs20.x"
      code:
        fn::fileArchive: ./handler

  invokeCommand:
    type: command:local:Command
    properties:
      create: 'aws lambda invoke --function-name "$FN" --payload ''{"stackName": "${pulumi.stack}"}'' --cli-binary-format raw-in-base64-out out.txt >/dev/null && cat out.txt | tr -d ''"''  && rm out.txt'
      environment:
        FN: ${lambdaFunction.arn}
        AWS_REGION: ${aws:region}
        AWS_PAGER: ""
    options:
      dependsOn:
        - ${lambdaFunction}

outputs:
  output: ${invokeCommand.stdout}
```

{{% /choosable %}}

## What's new

The 1.0 release of the Command provider marks a stable API for the 1.x series. Rather than simply putting a “v1” label on the existing provider, we also used this opportunity to enhance it with some previously requested capabilities to provide a more complete set of capabilities.

- The API documentation in the Pulumi registry has [examples in all Pulumi languages](https://github.com/pulumi/pulumi-command/issues/196) and is expanded.
- Capturing stdout and stderr of commands can now [be switched off](https://github.com/pulumi/pulumi-command/pull/451), which is useful when they might contain secrets or are very noisy.
- Environment handling for remote commands [has better error handling and is better documented](https://github.com/pulumi/pulumi-command/pull/395).
- The `CopyFile` resource is [superseded](https://github.com/pulumi/pulumi-command/pull/423) by the new `CopyToRemote` resource. It can copy whole directories in addition to individual files. The source of the copy is now a [Pulumi asset or archive](https://www.pulumi.com/docs/concepts/assets-archives/) which provides full interoperability with the Pulumi ecosystem. The use of assets and archives also makes Pulumi run copy operations only if the source has changed. For an easy transition, the previous `CopyFile` resource will remain available with a deprecation notice until the next major version.

Here’s an example of copying a directory to a remote host. For brevity, the remote server is assumed to exist, but it could also be provisioned in the same Pulumi program.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import { remote, types } from "@pulumi/command";
import * as fs from "fs";
import * as os from "os";
import * as path from "path";

export = async () => {
    const config = new pulumi.Config();

    // Get the private key to connect to the server. If a key is
    // provided, use it, otherwise default to the standard id_rsa SSH key.
    const privateKeyBase64 = config.get("privateKeyBase64");
    const privateKey = privateKeyBase64 ?
        Buffer.from(privateKeyBase64, 'base64').toString('ascii') :
        fs.readFileSync(path.join(os.homedir(), ".ssh", "id_rsa")).toString("utf8");

    const serverPublicIp = config.require("serverPublicIp");
    const userName = config.require("userName");

    // The configuration of our SSH connection to the instance.
    const connection: types.input.remote.ConnectionArgs = {
        host: serverPublicIp,
        user: userName,
        privateKey: privateKey,
    };

    // Set up source and target of the remote copy.
    const from = config.require("payload")!;
    const archive = new pulumi.asset.FileArchive(from);
    const to = config.require("destDir")!;

    // Copy the files to the remote.
    const copy = new remote.CopyToRemote("copy", {
        connection,
        source: archive,
        remotePath: to,
    });

    // Verify that the expected files were copied to the remote.
    // We want to run this after each copy, i.e., when something changed,
    // so we use the asset to be copied as a trigger.
    const find = new remote.Command("ls", {
        connection,
        create: `find ${to}/${from} | sort`,
        triggers: [archive],
    }, { dependsOn: copy });

    return {
        remoteContents: find.stdout
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_command as command

config = pulumi.Config()

server_public_ip = config.require("serverPublicIp")
user_name = config.require("userName")
private_key = config.require("privateKey")
payload = config.require("payload")
dest_dir = config.require("destDir")

archive = pulumi.FileArchive(payload)

# The configuration of our SSH connection to the instance.
conn = command.remote.ConnectionArgs(
    host = server_public_ip,
    user = user_name,
    privateKey = private_key,
)

# Copy the files to the remote.
copy = command.remote.CopyToRemote("copy",
    connection=conn,
    source=archive,
    destination=dest_dir)

# Verify that the expected files were copied to the remote.
# We want to run this after each copy, i.e., when something changed,
# so we use the asset to be copied as a trigger.
find = command.remote.Command("find",
    connection=conn,
    create=f"find {dest_dir}/{payload} | sort",
    triggers=[archive],
    opts = pulumi.ResourceOptions(depends_on=[copy]))

pulumi.export("remoteContents", find.stdout)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"fmt"

	"github.com/pulumi/pulumi-command/sdk/go/command/remote"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		cfg := config.New(ctx, "")
		serverPublicIp := cfg.Require("serverPublicIp")
		userName := cfg.Require("userName")
		privateKey := cfg.Require("privateKey")
		payload := cfg.Require("payload")
		destDir := cfg.Require("destDir")

		archive := pulumi.NewFileArchive(payload)

		conn := remote.ConnectionArgs{
			Host:       pulumi.String(serverPublicIp),
			User:       pulumi.String(userName),
			PrivateKey: pulumi.String(privateKey),
		}

		copy, err := remote.NewCopyToRemote(ctx, "copy", &remote.CopyToRemoteArgs{
			Connection: conn,
			Source:     archive,
		})
		if err != nil {
			return err
		}

		find, err := remote.NewCommand(ctx, "find", &remote.CommandArgs{
			Connection: conn,
			Create:     pulumi.String(fmt.Sprintf("find %v/%v | sort", destDir, payload)),
			Triggers: pulumi.Array{
				archive,
			},
		}, pulumi.DependsOn([]pulumi.Resource{
			copy,
		}))
		if err != nil {
			return err
		}

		ctx.Export("remoteContents", find.Stdout)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Command = Pulumi.Command;

return await Deployment.RunAsync(() =>
{
    var config = new Config();
    var serverPublicIp = config.Require("serverPublicIp");
    var userName = config.Require("userName");
    var privateKey = config.Require("privateKey");
    var payload = config.Require("payload");
    var destDir = config.Require("destDir");

    var archive = new FileArchive(payload);

    // The configuration of our SSH connection to the instance.
    var conn = new Command.Remote.Inputs.ConnectionArgs
    {
        Host = serverPublicIp,
        User = userName,
        PrivateKey = privateKey,
    };

    // Copy the files to the remote.
    var copy = new Command.Remote.CopyToRemote("copy", new()
    {
        Connection = conn,
        Source = archive,
    });

    // Verify that the expected files were copied to the remote.
    // We want to run this after each copy, i.e., when something changed,
    // so we use the asset to be copied as a trigger.
    var find = new Command.Remote.Command("find", new()
    {
        Connection = conn,
        Create = $"find {destDir}/{payload} | sort",
        Triggers = new[]
        {
            archive,
        },
    }, new CustomResourceOptions
    {
        DependsOn =
        {
            copy,
        },
    });

    return new Dictionary<string, object?>
    {
        ["remoteContents"] = find.Stdout,
    };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.command.remote.Command;
import com.pulumi.command.remote.CommandArgs;
import com.pulumi.command.remote.CopyToRemote;
import com.pulumi.command.remote.inputs.*;
import com.pulumi.resources.CustomResourceOptions;
import com.pulumi.asset.FileArchive;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        final var config = ctx.config();
        final var serverPublicIp = config.require("serverPublicIp");
        final var userName = config.require("userName");
        final var privateKey = config.require("privateKey");
        final var payload = config.require("payload");
        final var destDir = config.require("destDir");

        final var archive = new FileArchive(payload);

        // The configuration of our SSH connection to the instance.
        final var conn = ConnectionArgs.builder()
            .host(serverPublicIp)
            .user(userName)
            .privateKey(privateKey)
            .build();

        // Copy the files to the remote.
        var copy = new CopyToRemote("copy", CopyToRemoteArgs.builder()
            .connection(conn)
            .source(archive)
            .destination(destDir)
            .build());

        // Verify that the expected files were copied to the remote.
        // We want to run this after each copy, i.e., when something changed,
        // so we use the asset to be copied as a trigger.
        var find = new Command("find", CommandArgs.builder()
            .connection(conn)
            .create(String.format("find %s/%s | sort", destDir,payload))
            .triggers(archive)
            .build(), CustomResourceOptions.builder()
                .dependsOn(copy)
                .build());

        ctx.export("remoteContents", find.stdout());
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml

resources:
  # Copy the files to the remote.
  copy:
    type: command:remote:CopyToRemote
    properties:
      connection: ${conn}
      source: ${archive}
      remotePath: ${destDir}

  # Verify that the expected files were copied to the remote.
  # We want to run this after each copy, i.e., when something changed,
  # so we use the asset to be copied as a trigger.
  find:
    type: command:remote:Command
    properties:
      connection: ${conn}
      create: find ${destDir}/${payload} | sort
      triggers:
        - ${archive}
    options:
      dependsOn:
        - ${copy}

config:
  serverPublicIp:
    type: string
  userName:
    type: string
  privateKey:
    type: string
  payload:
    type: string
  destDir:
    type: string

variables:
  # The source directory or archive to copy.
  archive:
    fn::fileArchive: ${payload}
  # The configuration of our SSH connection to the instance.
  conn:
    host: ${serverPublicIp}
    user: ${userName}
    privateKey: ${privateKey}

outputs:
  remoteContents: ${find.stdout}
```

{{% /choosable %}}

### Getting started

If you're currently using one of the v0 pre-release versions of the Command provider, you don't need to make any changes to your existing code. However, the enhanced functionality of copying assets and archives is only available in the new `CopyToRemote` resource. If you're using `CopyFile`, you should consider migrating to the new resource after the upgrade to 1.0.

Enjoy the new features, and we’re looking forward to seeing what you build with the Command provider!
