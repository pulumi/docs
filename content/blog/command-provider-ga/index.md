---
title: "Pulumi Command Provider 1.0"

date: 2024-06-20T11:02:20+02:00

draft: false

meta_desc: >-
    The 1.0 release of the Pulumi Command provider marks the provider’s general availability (GA).
    The release expands support for copying assets between local and remote hosts.

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

Here’s a simple example of running commands when another resource changes. In this case, a file is created when a pet name is created or changed, and the file is deleted when the pet name is removed. In a real-world scenario, the command could register/deregister the resource with an external API.

{{< chooser language "typescript,go,python,csharp,yaml" >}}

{{% choosable language yaml %}}

```yaml
resources:
  pet:
    type: random:RandomPet

  petFileCommand:
    type: command:local:Command
    properties:
      create: 'touch "${pet.id}.txt"'
      delete: 'rm "${pet.id}.txt"'
      triggers:
        # Replace this resource, i.e., re-run the 'create'
        # command, when the pet resource changes.
        - ${pet.id}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        final var config = ctx.config();
        final var pulumiTags = config.get("pulumiTags");
        var pet = new RandomPet("pet");

        var petFileCommand = new Command("petFileCommand", CommandArgs.builder()
            .create(pet.id().applyValue(id -> String.format("touch \"%s.txt\"", id)))
            .delete(pet.id().applyValue(id -> String.format("rm \"%s.txt\"", id)))
            .triggers(pet.id())
            .build());
    }
}
```

{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as command from "@pulumi/command";
import * as random from "@pulumi/random";

const pet = new random.RandomPet("pet", {});

const petFileCommand = new command.local.Command("petFileCommand", {
    create: pulumi.interpolate`touch "${pet.id}.txt"`,
    delete: pulumi.interpolate`rm "${pet.id}.txt"`,
    // Replace the resource, i.e., re-run the 'create' command,
    // when the pet resource changes.
    triggers: [pet.id],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_command as command
import pulumi_random as random

pet = random.RandomPet("pet")

pet_file_command = command.local.Command("petFileCommand",
    create=pet.id.apply(lambda id: f"touch \"{id}.txt\""),
    delete=pet.id.apply(lambda id: f"rm \"{id}.txt\""),
    # Replace the resource, i.e., re-run the 'create' command,
    # when the pet resource changes.
    triggers=[pet.id])
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"fmt"

	"github.com/pulumi/pulumi-command/sdk/go/command/local"
	"github.com/pulumi/pulumi-random/sdk/v4/go/random"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		pet, err := random.NewRandomPet(ctx, "pet", nil)
		if err != nil {
			return err
		}
		_, err = local.NewCommand(ctx, "petFileCommand", &local.CommandArgs{
			Create: pulumi.String(fmt.Sprintf("touch \"%v.txt\"", pet.ID())),
			Delete: pulumi.String(fmt.Sprintf("rm \"%v.txt\"", pet.ID())),
			// Replace the resource, i.e., re-run the 'create' command,
			// when the pet resource changes.
			Triggers: pulumi.Array{ pet.ID() },
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
using Pulumi;
using Command = Pulumi.Command;
using Random = Pulumi.Random;

return await Deployment.RunAsync(() =>
{
    var pet = new Random.RandomPet("pet");

    var petFileCommand = new Command.Local.Command("petFileCommand", new()
    {
        Create = pet.Id.Apply(id => $"touch \"{id}.txt\""),
        Delete = pet.Id.Apply(id => $"rm \"{id}.txt\""),
        Triggers = new[]
        {
            pet.Id,
        },
    });
});
```

{{% /choosable %}}

{{< /chooser >}}

Rather than simply putting a “v1” label on the existing provider, we used this opportunity to enhance it with some previously requested capabilities.

- The API documentation in the Pulumi registry has [examples in all Pulumi languages](https://github.com/pulumi/pulumi-command/issues/196) and is expanded.
- Capturing stdout and stderr of commands can now [be switched off](https://github.com/pulumi/pulumi-command/pull/451), which is useful when they might contain secrets or are very noisy.
- Environment handling for remote commands was [fixed and is better documented](https://github.com/pulumi/pulumi-command/pull/395).
- The `CopyFile` resource is [superseded](https://github.com/pulumi/pulumi-command/pull/423) by the new `CopyToRemote` resource. It can copy whole directories in addition to individual files. The source of the copy is now a [Pulumi asset or archive](https://www.pulumi.com/docs/concepts/assets-archives/) which provides full interoperability with the Pulumi ecosystem. The use of assets and archives also makes Pulumi run copy operations only if the source has changed. For an easy transition, the previous `CopyFile` resource will remain available for a while with a deprecation notice.

Here’s an example of copying a directory to a remote host.
**TODO: Insert remote copy directory example here**

{{< chooser language "typescript,go,python,csharp,yaml" >}}

{{< /chooser >}}

**TODO**: Insert section on breaking changes and migrating here. Depends on whether we decide to keep the existing `CopyFile` resource with a deprecation notice.

Enjoy the new features, and we’re looking forward to seeing what you build with the Command provider!
