---
title: Google-Native
meta_desc: 'This page provides an overview of the Google Cloud Native provider for Pulumi: Google-Native.'
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-google-native
    weight: 1

aliases: ["/docs/reference/clouds/google-native/"]
---

{{< notes >}}
The Google Cloud Native provider is currently in public preview.
{{< /notes >}}

<img src="/logos/tech/gcp.svg" align="right" class="h-16 px-8 pb-4">

The Google Cloud Native provider for Pulumi can be used to provision any of the cloud resources available in [Google Cloud](https://cloud.google.com/). The provider must be configured with credentials to deploy and update resources in Google Cloud.

See the [full API documentation]({{< relref "/docs/reference/pkg/google-native" >}}) for complete details of the available provider APIs.

## Setup

The Google Cloud Native provider supports several options for providing access to Google Cloud credentials.  See [setup page]({{< relref "setup" >}}) for details.

## Getting Started

The Google Cloud Native provider is currently in <strong> public preview</strong>. The quickest way to get started with Google Cloud is to follow the steps described in the [README](https://github.com/pulumi/pulumi-google-native#readme).

Some interesting examples are available complete with instructions:

* [Google Cloud Functions](https://github.com/pulumi/examples/tree/master/google-native-ts-functions): Create a serverless function
* [Ruby on Rails on GKE and Google Cloud SQL](https://github.com/pulumi/examples/tree/master/google-native-ts-k8s-ruby-on-rails-postgresql): Containerized Ruby on Rails app using Google Cloud SQL PostgresSQL, GKE and Google container registry.

## Example

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
import * as storage from "@pulumi/google-native/storage/v1";
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config("google-native");
const project = config.require("project");
const bucketName = "pulumi-goog-native-ts-01";

// Create a Google Cloud resource (Storage Bucket)
const bucket = new storage.Bucket("my-bucket", {
    name:bucketName,
    bucket:bucketName,
    project: project,
});

// Export the bucket self-link
export const bucketName = bucket.selfLink;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
from pulumi_google_native.storage import v1 as storage

config = pulumi.Config()
project = config.require('project')
# Create a Google Cloud resource (Storage Bucket)
bucket_name = "pulumi-goog-native-bucket-py-01"
bucket = storage.Bucket('my-bucket', name=bucket_name, bucket=bucket_name, project=project)

# Export the bucket self-link
pulumi.export('bucket', bucket.self_link)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	storage "github.com/pulumi/pulumi-google-native/sdk/go/google/storage/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	const bucketName = "pulumi-goog-native-bucket-go-01"
	pulumi.Run(func(ctx *pulumi.Context) error {
		conf := config.New(ctx, "google-native")
		project := conf.Require("project")
		// Create a Google Cloud resource (Storage Bucket)
		bucket, err := storage.NewBucket(ctx, "bucket", &storage.BucketArgs{
			Name:    pulumi.StringPtr(bucketName),
			Bucket:  pulumi.String(project),
			Project: project,
		})
		if err != nil {
			return err
		}
		// Export the bucket self-link
		ctx.Export("bucket", bucket.SelfLink)

		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Threading.Tasks;
using Pulumi;
using Pulumi.GoogleNative.Storage.V1;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var config = new Config("google-native");
            var project = config.Require("project");
            var bucketName = "pulumi-goog-native-bucket-cs-01";
            // Create a Google Cloud resource (Storage Bucket)
            var bucket = new Bucket("my-bucket", new BucketArgs{
                Name = bucketName,
                Bucket = bucketName,
                Project = project,
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

You can find additional examples of using the Google Cloud Native provider in
[the Pulumi examples repo](https://github.com/pulumi/examples).

## Libraries

The following packages are available in package managers:

* JavaScript/TypeScript: [`@pulumi/google-native`](https://www.npmjs.com/package/@pulumi/google-native)
* Python: [`pulumi-google-native`](https://pypi.org/project/pulumi-google-native/)
* Go: [`github.com/pulumi/pulumi-google-native/sdk/go/google`](https://github.com/pulumi/pulumi-google-native)
* .NET: [`Pulumi.GoogleNative`](https://www.nuget.org/packages/Pulumi.GoogleNative)

The Google Cloud Native provider is open source and available in the [pulumi/pulumi-google-native](https://github.com/pulumi/pulumi-google-native) repo.
