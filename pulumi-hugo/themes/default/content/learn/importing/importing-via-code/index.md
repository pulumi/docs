---
title: "Importing via code"
layout: topic
date: 2022-06-03T11:33:05-05:00
draft: false
description: Try importing resources with code via Pulumi's ResourceOptions.
meta_desc: Try importing resources with code via Pulumi's ResourceOptions.
index: 3
estimated_time: 10
meta_image: meta.png
authors:
    - laura-santamaria
tags:
    - terraform
---

So, importing via the CLI is pretty nice. However, what if you want to import resource state in your code directly? Run the code once, then you're set to go? Well, we can do that with an import call in the code itself. This call is part of the `ResourceOptions` in every SDK that Pulumi provides.

## Finding identifiers

As before, we have to get `id`s from our providers to import resources. We've done this a couple times now, so you should have it handy!

## Coding up the import

We use the `ResourceOptions` `import` key to define a key:value pair that contains the ID. Let's try importing the frontend container. Make a new directory and initialize a new Pulumi program in the language of your choice. Then update the {{< langfile >}} to include the following code (with the ID pulled from Docker):

{{< chooser language "csharp,go,java,python,typescript,yaml" >}}

{{% choosable language csharp %}}

```csharp
var frontend_dev = new Docker.Container("frontend-dev", new Docker.ContainerArgs
    {
        Envs =
        {
            $"LISTEN_PORT={FrontendPort}",
            $"HTTP_PROXY=backend-dev:{BackendPort}",
            $"PROXY_PROTOCOL={Protocol}"
        }
        Image = frontendImage.Latest,
        Name = "frontend-dev",
        NetworksAdvanced =
        {
            new Docker.Inputs.ContainerNetworksAdvancedArgs
            {
                Name = networkName
            }
        }
        Ports =
        {
            new Docker.Inputs.ContainerPortArgs
            {
                External = FrontendPort,
                Internal = FrontendPort,
            },
        },
    },
    new CustomResourceOptions {
        ImportId = "08a181ba69e46b1eaa66f9806568f7158d1d9e7040770260535cbe139e6e5468"
    }
);
```

{{% /choosable %}}

{{% choosable language go %}}

```go
container, err := docker.NewContainer(ctx, "frontend-dev", &docker.ContainerArgs{
        Envs: [
            pulumi.String(fmt.Sprintf("LISTEN_PORT=%d",frontendPort)),
            pulumi.String(fmt.Sprintf("HTTP_PROXY=backend-%s:%d",stackName,backendPort)),
            pulumi.String(fmt.Sprintf("PROXY_PROTOCOL=%s",protocol))
        ]
        Image:       frontendImage.Latest,
        Name:        pulumi.String("frontend-dev"),
        NetworksAdvanced:  &ContainerNetworksAdvancedArgs{
            Name: Network.name
        },
        Ports: ContainerPortArray{
            &ContainerPortArgs{
                External: frontendPort,
                Internal: frontendPort,
            },
        },
    }, pulumi.Import(pulumi.ID("08a181ba69e46b1eaa66f9806568f7158d1d9e7040770260535cbe139e6e5468")),
)
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
/ ...

import java.util.*;
import java.io.*;
import java.nio.*;
// ...
import com.pulumi.resources.CustomResourceOptions;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var frontend_dev = new Container("frontend-dev",
        ContainerArgs.builder()
            .envs(List.of(
                    String.format("LISTEN_PORT=%d",frontendPort),
                    String.format("HTTP_PROXY=backend-%s:%d",stackName,backendPort),
                    String.format("PROXY_PROTOCOL=%s",protocol)
            ))
            .image(frontendImage.repoDigest())
            .name("frontend-dev")
            .networksAdvanced(ContainerNetworksAdvancedArgs.builder()
                    .name(network.name())
                    .build())
            .ports(ContainerPortArgs.builder()
                    .internal(frontendPort)
                    .external(frontendPort)
                    .build())
            .build(), CustomResourceOptions.builder()
                .importId("08a181ba69e46b1eaa66f9806568f7158d1d9e7040770260535cbe139e6e5468")
                .build());
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi_docker as docker
from pulumi import ResourceOptions

frontend_dev = docker.Container(
    "frontend-dev",
    envs=[
        f"LISTEN_PORT={frontend_port}",
        f"HTTP_PROXY=backend-dev:{backend_port}",
        f"PROXY_PROTOCOL={protocol}"
    ],
    image=frontend.repo_digest,
    name="frontend-dev",
    networks_advanced=[docker.ContainerNetworksAdvancedArgs(
        name=network.name
    )]
    ports=[docker.ContainerPortArgs(
        internal=frontend_port,
        external=frontend_port
    )],
    opts=ResourceOptions(import_='08a181ba69e46b1eaa66f9806568f7158d1d9e7040770260535cbe139e6e5468'))
```

Note that the resource option has an underscore at the end due to the `import` keyword.

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as docker from "@pulumi/docker";

const frontend_dev = new docker.Container("frontend-dev", {
    image: frontend.repoDigest,
    name: `frontend-dev`,
    ports: [
        {
            internal: frontendPort,
            external: frontendPort,
        },
    ],
    envs: [
        `LISTEN_PORT=${frontendPort}`,
        `HTTP_PROXY=backend-dev:${backendPort}`,
        `PROXY_PROTOCOL=${protocol}`
    ],
    networksAdvanced: [
        {
            name: network.name,
        },
    ],
}, {
    import: "08a181ba69e46b1eaa66f9806568f7158d1d9e7040770260535cbe139e6e5468"
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
# ...
  frontend-dev:
    type: docker:index:Container
    properties:
      envs:
        [
          "LISTEN_PORT=${frontendPort}",
          "HTTP_PROXY=backend-${pulumi.stack}:${backendPort}",
          "PROXY_PROTOCOL=http://"
        ]
      image: ${frontend-image.repoDigest}
      name: frontend-dev
      networksAdvanced:
        - name: ${network.name}
          aliases: ["frontend-dev"]
      ports:
        - external: ${frontendPort}
          internal: ${frontendPort}
    options:
      import: "08a181ba69e46b1eaa66f9806568f7158d1d9e7040770260535cbe139e6e5468"
```

{{% /choosable %}}

{{< /chooser >}}

## Running the import

Now that you have the code, actually importing the resource is one command away: `pulumi up`. As before, you'll get an equal sign instead of a plus sign in the preview of the actions taken by Pulumi. This means nothing specifically changed with the resource; the service just set it in the stack based on the results coming from the provider.

If you run `pulumi up` (or `pulumi preview`) and get an error like this, you need to check your `id` value:

```bash
error: Preview failed: importing <id> <type> not found
```

If you had any issues with the CLI command, you'll notice the slight difference in the error message. Here's the error you'd get from the CLI:

```bash
error: Preview failed: resource <id> does not exist
```

One big difference to note for this method compared to the others is that this method **does not** protect the resource automatically. From here, any subsequent action by Pulumi as a result of modification of your code will apply to the resource, including destruction if you were to remove the resource from your code.

## Moving forward

From here, you need to remove the `import` option to continue to update the resource. We only run that option once. And you can modify the resources as you see fit in the code with every `pulumi up` or `pulumi destroy` applying to the resource as with every other one you have in your code.

{{% notes type=warning %}}

If you were following along, don't forget to tear down your stack and tear down the Terraform resources you stood up! `pulumi destroy` and `terraform destroy`

{{% /notes %}}

<br/>
<hr/>
Congratulations! You've now finished this pathway on importing resources and migrating to Pulumi! In this pathway, you've learned about importing resources via a CLI command, importing resources in bulk, and importing resources in code.

Go build new things, and watch this space for more learning experiences with Pulumi!
