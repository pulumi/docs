---
title: "Hierarchical Config: The Interim Solution"
date: 2022-03-15T10:00:00Z
draft: false
meta_desc: In this aritcle, Rawkode takes a look at how he'd manage project and organizational configuration for Pulumi programs.
meta_image: meta.png
authors: ["david-flanagan"]
tags: ["config"]
---

A really common question that we receive on the Pulumi team is, "How can we set config at a project level, that can be used across all stacks?".

When I say "really common" ... I mean really, really common.

This [issue](https://github.com/pulumi/pulumi/issues/2307) was first open in 2018 and has received 52 votes from the community. Not only that, we've had plenty of similar issues created over the years too.

- [Feature-Request: project-wide secrets #2445](https://github.com/pulumi/pulumi/issues/2445)
- [Feature Request: Global Config Values](https://github.com/pulumi/pulumi-aws/issues/1052)
- [How to share a config between projects](https://github.com/pulumi/pulumi/issues/5473)
- [Project-wide variables (not stack specific) #6719](https://github.com/pulumi/pulumi/issues/6719)

This is clearly a feature that our community has asked for and we're currently working on delivering it as soon as we can. However, in the interim, I'm going to show you a few ways that you can get around this now.

## Project Level Config

Typically, when you need to access the stack configuration in a Pulumi program, you use the `config` package.

{{< chooser language "typescript,go,python,csharp" >}}

{{% choosable language typescript %}}

```typescript
import { Config } from "@pulumi/pulumi";

const config = new Config();
const region = config.require("region");
```

{{% /choosable %}}

{{% choosable language go %}}

```go
import (
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

conf := config.New(ctx, "")
region := conf.Require("region")
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi

config = pulumi.Config();
region = config.require('region');
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;

var config = new Config();
var region = config.Require("region");
```

{{% /choosable %}}

{{% /chooser %}}

This code will reach from the `Pulumi.<stack-name>.yaml` file and give you access to the configuration values for the prefix you want to load.

So if you want project level config that works across all stacks, you can "hard code" the configuration. It sounds too simple, right?

{{< chooser language "typescript,go,python,csharp" >}}

{{% choosable language typescript %}}

```typescript
export const projectLevelConfig = {
  region: "us-west-2",
  encryptionKmsKey: "arn:aws:kms:us-west-2:...",
  issueEmail: "bugs@ellingsonmineral.com"
};
```

{{% /choosable %}}

{{% choosable language go %}}

```go
type ProjectLevelConfig struct {
  Region string
  EncryptionKmsKey string
  IssueEmail string
}

const projectLevelConfig = ProjectLevelConfig{
  Region: "us-west-2",
  EncryptionKmsKey: "arn:aws:kms:us-west-2:...",
  IssueEmail: "bugs@ellingsonmineral.com"
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
projectLevelConfig = {
  "region": "us-west-2",
  "encryptionKmsKey": "arn:aws:kms:us-west-2:...",
  "issueEmail": "bugs@ellingsonmineral.com"
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var projectLevelConfig = new Dictionary<string, string>
{
  { "region", "us-west-2" },
  { "encryptionKmsKey", "arn:aws:kms:us-west-2:..." },
  { "issueEmail", "bugs@ellingsonmineral.com"
}
```

{{% /choosable %}}

{{% /chooser %}}

These objects/structs/dictionaries can all be consumed and imported across the various components and files within your Pulumi program, but they cannot be used at an organizational level across multiple Pulumi programs ... unless you've got a mono-repo. Do you? 😅

## Organization Level Config

So if you want to provide organizational level config, you need to fall deeper into the programming language ecosystem that you're using to build your infrastructure. Every programming language has a way to parse and consume JSON and YAML files. Better yet, every programming language has a way to fetch a remote JSON/YAML file and give you a object/struct/dictionary.

So really, there's no reason you can't use a remote JSON file to provide a common configuration object across all your Pulumi programs. That being said, there are definitely reasons you _shouldn't_ use a remote JSON file. Maintaining a remote JSON file is much more of a burden than it will initially seem. As you add more values to your JSON file and more teams/projects begin to rely on it, you'll start to feel the pain of schema management. How do I know that the JSON I'm pulling down has the values I need and that fields haven't been changed or replaced? 😬

So while I 💯 feel like you shouldn't do this, you _can_ if you really need to. Just make sure you understand the tradeoffs and enforce a schema.

A common way to manage schema is to use a [JSON Schema](https://json-schema.org/) or [CUE](https://cuelang.org) to define the structure of your JSON file.

By using one of these methods, you can publish a schema that is available within your organization and people can have confidence that the value they pull remotely can be deserialized to a strict type. Using CI/CD you can also ensure the value itself conforms to the schema before updating the public document.

With JSON Schema, you'd define something like:

```json
{
  "type": "object",
  "properties": {
    "region": {
      "type": "string",
      "default": "us-west-2"
    },
    "encryptionKmsKey": {
      "type": "string",
      "default": "arn:aws:kms:us-west-2:..."
    },
    "issueEmail": {
      "type": "string",
      "default": "bugs@ellingsonmineral.com"
    }
  }
}
```

With CUE, this is much more concise. [CUE is really awesome and I encourage you to check it out](https://cuelang.org).

```yaml
region: string | *"eu-west-2"
encryptionKmsKey: string | *"arn:aws:kms:eu-west-2:..."
issueEmail: string | *"bugs@ellingsonmineral.com"
```


## Pulumi Native Hierarchical Configuration

So we've worked out that project level configuration is a data structure within our Pulumi programs and it works pretty darn well.

However, the organization level config is prone and rife with pain, confusion, and delusion. It requires non-trivial tooling and process to ensure that a global document is valid and consistent with downstream consumers. What I've shown you is a "if you must" approach that I would use myself. We've also not even handled the "merge" of organization level with project level overrides, and then stack level overrides. Of course, with code it's all possible, but it's more and more code that you need to write that we don't want you to need to write, right? Right!

Pulumi wants to make this better for you. While this feature doesn't exist yet, we are actively working on it. If you want to follow along with the progress, I suggest you watch/subscribe to [this issue](https://github.com/pulumi/pulumi/issues/2307).

If you want to share your opinions on how **YOU** would like this feature to be implemented, jump into the comments. We'd love to hear from you!

Speak soon.
