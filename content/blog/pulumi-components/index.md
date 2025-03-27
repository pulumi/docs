---
title: "Announcing the Next-Generation of Pulumi Components: Enabling Infrastructure Abstractions"
date: 2025-03-27
draft: false
meta_desc: Pulumi Components enable you to create, share, and consume reusable infrastructure building blocks across your organization and the broader community.
meta_image: meta.png
authors:
    - mikhail-shilkov
    - meagan-cojocar
tags:
    - releases 
    - platform-teams
    - features
    - iac
    - components
social:
    twitter: "Introducing enhanced Pulumi Components: Create in one language, consume in any other—even YAML! Perfect for platform teams building reusable infrastructure that developers can easily adopt."
    linkedin: "We're excited to announce significant enhancements to Pulumi Components! Now platform teams can build sophisticated infrastructure abstractions in their preferred language, while developers can easily consume these components using simpler interfaces or YAML. It's a more intuitive, more secure way to codify organizational standards while giving developers straightforward access to rock-solid abstractions—without worrying about the underlying details. A true win-win that accelerates innovation and drives productivity across your organization."
---

Pulumi Components enable you to create, share, and consume reusable infrastructure building blocks across your organization and the broader community. Today, we're excited to announce significant enhancements to Pulumi Components that make them more powerful, accessible, and easier to use than ever before.

<!--more-->

With this release, we've made it possible to author components in one language and consume them in any other Pulumi language—including Pulumi YAML. This breakthrough enables platform teams to build sophisticated infrastructure abstractions in their preferred programming language while application developers can easily consume these components using simpler interfaces or even YAML, all without sacrificing type safety or functionality.

For platform teams, the new Pulumi Components offer a more intuitive, more secure way to codify organizational standards. For developers, it's a straightforward way to pull in platform-approved abstractions without having to worry about all the underlying details. It's a win-win that drastically accelerates innovation and drives productivity across your teams.

"Pulumi's reusable components have transformed our infrastructure collaboration," said Kevin Keeler, Vice President - DevOps, QA, and Architecture at A+E Networks. "Our developers interact with Pulumi YAML to provision infrastructure quickly and easily, while our platform team leverages Pulumi's programming capabilities to build robust, reusable components. This ensures compliance with organizational standards and best practices without burdening developers with complexity. By streamlining this workflow, we've enhanced productivity and focused more on delivering customer value."

## Understanding Component Resources

At their core, Pulumi Component Resources are logical groupings of resources that encapsulate infrastructure patterns and best practices. Unlike standard resources that map directly to cloud provider resources, component resources are higher-level abstractions that can contain multiple child resources working together to implement a specific capability. While similar in concept to Terraform modules, Pulumi Components offer more power through full programming language capabilities, stronger typing, and now, cross-language support.

For example, a `SecureBucket` might include a bucket, versioning configuration, encryption settings, and tagging policies—all bundled together as a single, reusable unit that enforces your organization's security and compliance standards.

## What's New with Pulumi Components

Our latest enhancements focus on making components more accessible and easier to share:

1. **Cross-language consumption**: Components authored in one language can now be consumed in any Pulumi language, including Pulumi YAML.

2. **Simplified sharing**: Share components by simply pushing code to a git repository - no need to manually publish SDKs.

3. **Streamlined consumption**: Use the `pulumi package add` command with any git URL (like `github.com/org/repo`) to easily incorporate any components into your projects.

## How It Works

### Creating Components

Creating a component remains the same as before—define a class that extends `ComponentResource`:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

export interface SecureBucketArgs {
    bucketName?: pulumi.Input<string>;
    versioning?: boolean;
    encryption?: boolean;
    tags?: { [key: string]: pulumi.Input<string> };
}

export class SecureBucket extends pulumi.ComponentResource {
    public readonly bucket: aws.s3.Bucket;
    public readonly bucketName: pulumi.Output<string>;

    constructor(name: string, args: SecureBucketArgs = {}, opts?: pulumi.ComponentResourceOptions) {
        super("my:components:SecureBucket", name, {}, opts);

        // Create an S3 bucket with best practices by default
        this.bucket = new aws.s3.Bucket(`${name}`, {
            bucket: args.bucketName,
            tags: {
                ManagedBy: "Pulumi",
                ...args.tags,
            },
        }, { parent: this });

        // Conditionally enable versioning
        if (args.versioning !== false) {
            new aws.s3.BucketVersioningV2(`${name}-versioning`, {
                bucket: this.bucket.id,
                versioningConfiguration: {
                    status: "Enabled",
                },
            }, { parent: this });
        }

        // Conditionally enable encryption
        if (args.encryption !== false) {
            new aws.s3.BucketServerSideEncryptionConfigurationV2(`${name}-encryption`, {
                bucket: this.bucket.id,
                rules: [{
                    applyServerSideEncryptionByDefault: {
                        sseAlgorithm: "AES256",
                    },
                }],
            }, { parent: this });
        }

        this.bucketName = this.bucket.id;

        this.registerOutputs({
            bucket: this.bucket,
            bucketName: this.bucketName,
        });
    }
}
```

### Sharing Components

Pulumi's new Components capability is designed to make sharing infrastructure building blocks as easy as possible, whether you're publishing them to a Git repository or referencing them from a local folder in a monorepo.

#### Publishing to Git

Once you've authored your component, sharing it is as simple as pushing your code to a Git repository and optionally tagging a release. From there, anyone (including you) can pull it down and use it in their own Pulumi projects.

For example, after pushing your SecureBucket to GitHub and tagging it as v1.0.0, others can consume it by running:

```bash
pulumi package add github.com/myorg/secure-s3-component@v1.0.0
```

Under the hood, Pulumi:

1. Fetches your code from GitHub
2. Auto-generates a local SDK from the component's schema
3. Makes it available to your Pulumi program in your chosen language

#### Referencing Components Locally

For scenarios like monorepos, rapid development iterations, or when you're working with components that don't need to be published to a repository, you can reference local source code directly:

```bash
pulumi package add /path/to/local/secure-s3-component
```

Pulumi will identify the folder as a Pulumi component project, generate a local SDK, and make it available for import in your program—even if your consumer program is in a different language.

### Consuming Components Across Languages

The real power comes in how these components can now be consumed in any Pulumi language:

{{< chooser language "typescript,python,csharp,go,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import { SecureBucket } from "@myorg/secure-s3-component";

const secureBucket = new SecureBucket("my-secure-bucket", {
    bucketName: "my-company-secure-assets",
    tags: {
        Environment: "production",
        Department: "engineering",
    },
});

export const bucketName = secureBucket.bucketName;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from myorg_secure_s3_component import SecureBucket

secure_bucket = SecureBucket("my-secure-bucket", 
    bucket_name="my-company-secure-assets",
    tags={
        "Environment": "production",
        "Department": "engineering",
    })

pulumi.export("bucket_name", secure_bucket.bucket_name)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using MyOrg.SecureS3Component;

return await Deployment.RunAsync(() =>
{
    var tags = new Dictionary<string, string>
    {
        { "Environment", "production" },
        { "Department", "engineering" }
    };
    
    var secureBucket = new SecureBucket("my-secure-bucket", new SecureBucketArgs
    {
        BucketName = "my-company-secure-assets",
        Tags = tags
    });

    // Export the bucket name
    return new Dictionary<string, object?>
    {
        ["BucketName"] = secureBucket.BucketName
    };
});
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	secure "github.com/myorg/secure-s3-component/sdk/go/secure-s3-component"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		tags := make(map[string]string)
		tags["Environment"] = "production"
		tags["Department"] = "engineering"
		
		secureBucket, err := secure.NewSecureBucket(ctx, "my-secure-bucket", &secure.SecureBucketArgs{
			BucketName: pulumi.String("my-company-secure-assets"),
			Tags:       pulumi.ToStringMap(tags),
		})
		if err != nil {
			return err
		}
		
		ctx.Export("bucketName", secureBucket.BucketName)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package mypackage;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.myorg.secures3component.SecureBucket;
import com.myorg.secures3component.SecureBucketArgs;

import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var tags = Map.of(
                "Environment", "production",
                "Department", "engineering"
            );
            
            var bucketArgs = SecureBucketArgs.builder()
                .bucketName("my-company-secure-assets")
                .tags(tags)
                .build();
                
            var secureBucket = new SecureBucket("my-secure-bucket", bucketArgs);
            
            ctx.export("bucketName", secureBucket.bucketName());
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: my-infrastructure
runtime: yaml
description: A stack that uses SecureBucket component

packages:
  secure-s3-component: github.com/myorg/secure-s3-component@v1.0.0
  
resources:
  secureBucket:
    type: secure-s3-component:SecureBucket
    properties:
      bucketName: my-company-secure-assets
      tags:
        Environment: production
        Department: engineering

outputs:
  bucketName: ${secureBucket.bucketName}
```

{{% /choosable %}}

{{< /chooser >}}

## Pro Tips

- **Tagging Releases**: If you're working with Git-based components, you can tag version releases (both stable and preview versions). This ensures downstream users can easily choose specific versions without chasing a moving target.

- **Managing Dependencies**: Once you've run `pulumi package add <repo-url>`, Pulumi will generate a local SDK in your project and add an entry to the `packages` section of your Pulumi.yaml file. Check in these files if you want fully reproducible builds; or add them to `.gitignore` if you prefer to regenerate them on each checkout. When using `.gitignore`, team members can simply run `pulumi install` to restore all packages listed in Pulumi.yaml and regenerate the SDK.

- **Leveraging Private Repos**: If you need to keep your components private, you can still point to a Git source in a private repository. Just make sure the correct access tokens are set in the environment [as described in our package management documentation](https://www.pulumi.com/docs/using-pulumi/pulumi-packages/package-management/).

## The Spectrum of Pulumi Components You Can Build

You can use Pulumi Components with more flexibility and control depending on your use case. This table shows the variety of use cases:

| Feature | Single language | Multi-language with Auto-Generated SDKs | Manual Schema and SDKs |
|---------|--------------------------|-------------------------------------------|--------------------------|
| **Best for** | Quick development within a single language ecosystem | Cross-language teams needing to share components | More flexibility and control needed or strict API requirements |
| **Cross-language consumption** | No - limited to original language | Yes - consume in any Pulumi language | Yes - consume in any Pulumi language but YAML|
| **Setup complexity** | Minimal - standard programming patterns | Minimal - just requires package management | High - requires schema authoring and validation |
| **Development workflow** | Fast iteration with direct code changes | Requires SDK regeneration when component changes | Complex with schema updates and SDK publishing |
| **API control** | N/A | Moderate - auto-generated from source | Full - ship the same interface to all consumers |
| **Version management** | Simple - standard code versioning | Moderate - requires careful API changes | Complex - strict semantic versioning needed |
| **Typical user** | Individual developers or same-language teams | Platform teams sharing with developers | Enterprise teams with strict requirements or package publishers |
| **Ideal use cases** | • Rapid prototyping<br>• Single team projects<br>• Simple components | • Organization-wide libraries<br>• Platform engineering<br>• Multi-language environments | • Published packages<br>• Complex validation needs |
| **Limitations** | • Single language only<br>• | • SDK regeneration overhead<br>• Runtime dependencies<br>• Some translation limitations | • Complex setup<br>• Steep learning curve<br>• Slower iteration |

## Conclusion

The ability to author components in one language and consume them in any other Pulumi language—including YAML—provides unprecedented flexibility and collaboration opportunities between platform teams and application developers.

We're excited to see what you build with Pulumi Components! Share your feedback with us on the [Pulumi Community Slack](https://slack.pulumi.com/) or open an issue in the [pulumi/pulumi GitHub repository](https://github.com/pulumi/pulumi).
