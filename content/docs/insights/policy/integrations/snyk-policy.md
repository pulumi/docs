---
title_tag: "Snyk Container Scanning | Pulumi Policy"
meta_desc: Snyk container scanning helps you ensure that your Docker images are secure.
title: Snyk Container Scanning
h1: Snyk Container Scanning
weight: 4
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    insights:
        name: Snyk Container Scanning
        parent: integrations
        weight: 1
aliases:
  - /docs/insights/policy/policy-as-code/snyk-policy/
  - /docs/iac/crossguard/snyk-policy/
  - /docs/guides/crossguard/snyk-container-scanning/
  - /docs/using-pulumi/crossguard/snyk-container-scanning/
  - /docs/using-pulumi/crossguard/snyk-policy/
  - /docs/iac/packages-and-automation/crossguard/snyk-policy/
  - /docs/iac/using-pulumi/crossguard/snyk-policy/
  - /docs/insights/policy/snyk-policy/
---
<!-- markdownlint-disable ul code -->

## Overview

{{% notes type="warning" %}}
**Experimental**: This integration is experimental. It shells out to the Snyk CLI tool and may not provide a seamless user experience.
{{% /notes %}}

[Snyk container scanning](https://github.com/pulumi/templates-policy/tree/master/snyk-typescript) is a Pulumi policy as code template that allows you to uses the [Snyk CLI](https://docs.snyk.io/cli-ide-and-ci-cd-integrations/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-snyk-container) to scan [`docker.Image`](/registry/packages/docker/api-docs/image/) resources for vulnerabilities.

For more information on Pulumi's Policy as Code solution, see [Get started with Pulumi policy as code](/docs/insights/policy/get-started/).

## Using Snyk container scanning

In this guide, we'll show you how to create a Policy Pack that enables Snyk container scanning.

### Prerequisites

- [Install Pulumi](/docs/install/)
- [Install Node.js](https://nodejs.org/en/download/)
- [Install the Snyk CLI](https://docs.snyk.io/snyk-cli)

### Running the policy pack

This guide assumes the following directory structure:

```text
.
├── infra # Your Pulumi IaC program lives here.
└── policy # Your policy pack will live here. Directory is assumed to be initially empty.
```

Your Pulumi IaC program should have at least one `docker.Image` resource, similar to the following:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as docker from "@pulumi/docker";

const exampleImage = new docker.Image("exampleImage", {
    imageName: "docker.io/your-user-name/your-image-name",
    buildOnPreview: true,
    build: {
        dockerfile: "./app/Dockerfile",
        context: "./app",
    },
    skipPush: true,
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_docker as docker

example_image = docker.Image("exampleImage",
    image_name="docker.io/your-user-name/your-image-name",
    build_on_preview=True,
    build=docker.DockerBuildArgs(
        dockerfile="./app/Dockerfile",
        context="./app",
    ),
    skip_push=True)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
 "github.com/pulumi/pulumi-docker/sdk/v4/go/docker"
 "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        _, err := docker.NewImage(ctx, "exampleImage", &docker.ImageArgs{
            ImageName:      pulumi.String("docker.io/your-user-name/your-image-name"),
            BuildOnPreview: pulumi.Bool(true),
            Build: &docker.DockerBuildArgs{
                Dockerfile: pulumi.String("./app/Dockerfile"),
                Context:    pulumi.String("./app"),
            },
            SkipPush:       pulumi.Bool(true),
        })

        if err != nil {
            return err
        }

        return nil
    })
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Linq;
using Pulumi;
using Docker = Pulumi.Docker;

return await Deployment.RunAsync(() =>
{
    var exampleImage = new Docker.Image("exampleImage", new()
    {
        ImageName = "docker.io/your-user-name/your-image-name",
        BuildOnPreview = true,
        Build = new Docker.Inputs.DockerBuildArgs
        {
            Dockerfile = "./app/Dockerfile",
            Context = "./app",
        },
        SkipPush = true,
    });

});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.docker.Image;
import com.pulumi.docker.ImageArgs;
import com.pulumi.docker.inputs.DockerBuildArgs;
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
        var exampleImage = new Image("exampleImage", ImageArgs.builder()
            .imageName("docker.io/your-user-name/your-image-name")
            .buildOnPreview(true)
            .build(DockerBuildArgs.builder()
                .dockerfile("./app/Dockerfile")
                .context("./app")
                .build())
            .skipPush(true)
            .build());

    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  exampleImage:
    type: docker:Image
    properties:
      imageName: "docker.io/your-user-name/your-image-name"
      buildOnPreview: true # This must be set for the policy to work on `pulumi preview`
      build:
        dockerfile: "./app/Dockerfile"
        context: "./app"
      skipPush: true
```

{{% /choosable %}}

Start by initializing a new policy in the `policy/` directory:

```bash
cd policy
pulumi policy new snyk-typescript
```

You can then run the policy against your Pulumi program:

```bash
cd ../infra
pulumi preview --policy-pack ../infra
```

{{< notes type="info" >}}
Note that the Snyk container policy is a stack policy (validates all resources in the stack after processing). This means that in order to have containers correctly scanned during a `pulumi preview`, your `docker.Image` resources must have the `buildOnPreview` set to `true`. If you run the policy pack during a `pulumi update`, the policy will execute _after_ your containers have been built, _and after they have been pushed_ if you have not explicitly specified the `skipPush` input to be `true`.
{{< /notes >}}

## Configuration options

### Configuration parameters

The Snyk policy template supports the following configurable options:

- `dockerfileScanning` (boolean): If set to `true`, Snyk will also scan your image's Dockerfile for additional remediation suggestions. If this value is set, `pulumiProgramAbsPath` must also be set. Default value is `false`.
- `excludeBaseImageVulns` (boolean): If set to `true`, Snyk will exclude vulnerabilities in the base image for your Dockerfile as defined in the `FROM` directive, and limit its results to layers added on top of the base image. Default value is `false`.
- `failOn` (enum): If set to `upgradable`, the image will be in violation only for vulnerabilities that have a known upgrade path. If set to `all`, the image will be in violation for all vulnerabilities. Default value is `all`.
- `pulumiProgramAbsPath` (string): The absolute path on disk to the Pulumi program to which this policy is being applied.Required (and only useful) if `dockerfileScanning` is set to `true`. Default value is an empty string.
- `severityThreshold` (enum): The minimum level of vulnerabilities to be reported, and if any are found, to find the image in violation of the policy. Valid values are `"low"`, `"medium"`, `"high"`, `"critical"`. Default value is `critical`.

### Setting configuration values

To set the configuration, you can do one of the following:

1. Hard-code the values in `index.ts` within the templated policy. (These values will serve as defaults and may still be overridden on a per-run basis by either of the methods that follow.)
1. Create a JSON file with the configuration values, e.g.:

    ```json
    {
        "snyk-container-scan": {
            "enforcementLevel": "disabled",
            "dockerfileScanning": true,
            "pulumiProgramAbsPath": "/path/to/pulumi/iac/program"
        }
    }
    ```

    And then pass that value to the Pulumi CLI when running the policy, e.g.:

    ```bash
    pulumi preview --policy-pack /path/to/policy --policy-pack-config /path/to/policy-config.json
    ```

    (Relative paths in the above command will also work.)
1. If using Pulumi Cloud's server-side enforcement, policy pack configuration can be centrally managed in the Pulumi Cloud UI. For details, see [Configuring policy packs](/docs/insights/policy/policy-packs/#pulumi-cloud-configuration).

## Next steps

Once you've tested the Policy Pack, an organization administrator can publish the Policy Pack to Pulumi Cloud to be enforced across your organization. To learn more,see [Enforcing a Policy Pack Across an Organization](/docs/insights/policy/get-started#enforcing-a-policy-pack).
