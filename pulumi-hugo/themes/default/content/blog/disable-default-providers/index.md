---
title: "Unlock Programmatic Control by Disabling Default Providers"
date: 2022-04-01
meta_desc: Introducing the new config parameter disable-default-providers.
authors: [ ian-wahbe ]
meta_image: disable-default-providers.png
tags: [ features ]
---

As of 3.23.0, users can disable the default provider with Pulumi. So what does this mean for you? If you’ve been using
Pulumi for a bit, you’ll have encountered [provider resources][prov-res], which are how we abstract the global state of
a cloud provider. All resources have an associated provider. If no provider is supplied in the user’s code, a [default
provider][def-prov] is created to serve the resource. Explicit providers, which are  defined by the user in code, allow
programmatic and dynamic control of how a resource deploys into a cloud. A Pulumi [resource][res] can be instructed to
use an explicit provider by setting the [provider resource option][prov-res-opts] or by inheriting the provider from the
resource's [parent resource][par-res].

[prov-res]:{{< relref "/docs/intro/concepts/resources/providers" >}}
[def-prov]:{{< relref "/docs/intro/concepts/resources/providers#default-provider-configuration" >}}
[res]:{{< relref "/docs/intro/concepts/resources" >}}
[prov-res-opts]:{{< relref "/docs/intro/concepts/resources/options/provider" >}}
[par-res]:{{< relref "/docs/intro/concepts/resources/options/parent" >}}

<!-- more -->

As an example, consider this basic S3 bucket and object for AWS, with an explicit provider that defines an AWS region:

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
const west = new aws.Provider("provider", {
  region: aws.Region.USWest2,
});

// Create `bucket` with explicitly set provider `west`
const bucket = new aws.s3.Bucket("my-bucket", {
  website: {
    indexDocument: "index.html",
  },
}, { provider: west });

// Inherit provider `west` from parent `bucket`
const bucketObject = new aws.s3.BucketObject("index.html", {
  acl: "public-read",
  contentType: "text/html",
  bucket: bucket,
  source: new pulumi.asset.FileAsset("index.html"),
}, { parent: bucket });
```

{{% /choosable %}}

{{% choosable language python %}}

```python
west = aws.Provider("provider", region="us-east-1")

bucket = aws.s3.Bucket(
    "my-bucket",
    website=aws.s3.BucketWebsiteArgs(index_document="index.html"),
    opts=ResourceOptions(provider=west),
)

bucketObject = aws.s3.BucketObject(
    "index.html",
    acl="public-read",
    content_type="text/html",
    bucket=bucket,
    source=asset.FileAsset("index.html"),
    opts=ResourceOptions(parent=bucket),
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
west, err := aws.NewProvider(ctx, "provider", &aws.ProviderArgs{
	Region: aws.RegionUSEast1,
})
if err != nil {
	return err
}

bucket, err := s3.NewBucket(ctx, "my-bucket", &s3.BucketArgs{
	Website: s3.BucketWebsiteArgs{
	IndexDocument: pulumi.StringPtr("index.html"),
	},
}, pulumi.Provider(west))
if err != nil {
	return err
}

_, err = s3.NewBucketObject(ctx, "index.html", &s3.BucketObjectArgs{
	Acl:         s3.CannedAclPublicRead,
	ContentType: pulumi.StringPtr("text/html"),
	Bucket:      bucket,
	Source:      pulumi.NewFileAsset("index.html"),
}, pulumi.Parent(bucket))
if err != nil {
	return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var west = new Aws.Provider("provider", new Aws.ProviderArgs {
        Region = "us-east-1",
});

var bucket = new S3.Bucket("my-bucket", new S3.BucketArgs {
        Website = new Aws.S3.Inputs.BucketWebsiteArgs {
            IndexDocument = "index.html"
        },
    },
    new CustomResourceOptions { Provider = west },
);

new S3.BucketObject("index.html", new S3.BucketObjectArgs {
        Acl = "public-read",
        ContentType = "text/html",
        Bucket = bucket,
        Source = FileAsset("index.html"),
     },
    new CustomResourceOptions { Parent = bucket },
);
```

{{% /choosable %}}

{{< /chooser >}}

Default providers help keep simple things simple but make other actions impossible. As demonstrated in the above
example, [AWS providers][aws-prov], whether they are explicit or default, control the deployment region. That means
multi-region deployments necessitate explicit providers. Likewise, deploying to a newly created Kubernetes cluster
requires explicit providers since [Kubernetes providers][k8s-prov] describe their cluster. There are many scenarios when
explicit providers are mandatory for a correct deployment. When it is important that only explicitly configured
providers are used, default providers can lead to unpredictable deployments.

[aws-prov]:{{< relref "/registry/packages/aws/api-docs/provider/" >}}
[k8s-prov]:{{< relref "/registry/packages/kubernetes/api-docs/provider/" >}}

Imagine you are trying to create a bucket in each AWS region you have access to. I might write the following code:

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
const filter = {
  allRegions: false,
  filters: [{
    name: "opt-in-status",
    values: ["opted-in", "opt-in-not-required"],
  }],
};

async function regionalBuckets(
  config: pulumi.Config,
): Promise<Array<aws.s3.Bucket>> {
  const bucketList = new Array<aws.s3.Bucket>();
  for (
    const region in (await aws.getRegions(filter)).names
  ) {
    const provider = new aws.Provider(`${region}-provider`, {
      region: region as aws.Region,
      accessKey: config.requireSecret("key"),
      secretKey: config.requireSecret("secret"),
    });
    const bucket = new aws.s3.Bucket(`${region}-bucket`, {}, { provider });
    bucketList.push(bucket);
  }
  return bucketList;
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
filters = [
    aws.GetRegionsFilterArgs(
        name="opt-in-status", values=["opted-in", "opt-in-not-required"]
    )
]


async def regional_buckets(config: pulumi.Config) -> Output[List[s3.Bucket]]:
    bucket_list = []
    for region in (await aws.get_regions(filters=filters)).names:
        provider = aws.Provider(
            f"{region}-provider",
            region=region,
            access_key=config.require_secret("key"),
            secret_key=config.require_secret("secret"),
        )
        bucket = s3.Bucket(f"{region}-bucket", opts=ResourceOptions(provider=provider))
        bucket_list.append(bucket)
    return bucket_list
```

{{% /choosable %}}

{{% choosable language go %}}

```go
var filters = []aws.GetRegionsFilter{{
	Name:   "opt-in-status",
	Values: []string{"opted-in", "opt-in-not-required"},
}}

func regionalBuckets(ctx *pulumi.Context, config config.Config) (s3.BucketArray, error) {
	var bucketList s3.BucketArray
	regions, err := aws.GetRegions(ctx, &aws.GetRegionsArgs{Filters: filters})
	if err != nil {
		return nil, err
	}
	for _, region := range regions.Names {
		provider, err := aws.NewProvider(ctx, region+"-provider", &aws.ProviderArgs{
			Region: pulumi.String(region),
			AccessKey: config.RequireSecret("key"),
			SecretKey: config.RequireSecret("secret"),
		})
		if err != nil {
			return nil, err
		}
		bucket, err := s3.NewBucket(ctx, region+"-bucket", nil, pulumi.Provider(provider))
		if err != nil {
			return nil, err
		}
		bucketList = append(bucketList, bucket)
	}
	return bucketList, nil
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
async Task<S3.Bucket[]> regionalBuckets(Pulumi.Config config) {
    var filter = new Aws.Inputs.GetRegionsFilterArgs{
             Name = "opt-in-status",
            Values = {"opted-in", "opt-in-not-required"},
    };
    var regions = await Aws.GetRegions.InvokeAsync(new Aws.GetRegionsArgs{Filters = {filter}});
    var bucketList = new List<S3.Bucket>();
    foreach (var region  in regions.Names) {
        var provider = new Aws.Provider(region+"-provider", new Aws.ProviderArgs {
                Region = region,
                AccessKey = config.GetSecret("key")!,
                SecretKey = config.GetSecret("secret")!,
        });
        var bucket = new S3.Bucket(region+"-bucket", null, new CustomResourceOptions {
                Provider = provider
            });
        bucketList.Add(bucket);
    }
    return bucketList.ToArray();
}
```

{{% /choosable %}}

{{< /chooser >}}

This code will create a bucket in each region that the currently logged-in AWS account has access to. If someone else
ran the same code on a computer logged in to another account, Pulumi could create different buckets, even though all
buckets were provisioned by an explicit provider. This behavior is because we forgot to specify the provider for the
call to `aws.getRegions`. You might not notice that something unexpected happened because there would be no error
message, just inconsistent deployments. To prevent this category of problem, Pulumi now offers the ability to
disable default providers on a per-stack basis.  

By disabling the default `aws` provider, we would get the following error:

```
Error: Invoke: Default provider for 'aws' disabled. 'aws:index/getRegions:getRegions' must use an explicit provider.
```

Disabling default providers has been a popular [community request][req]. To meet that request, we’ve added the ability
to disable default providers in the [3.23.0 release][release]. The Pulumi config variable
`pulumi:disable-default-providers` represents the list of packages whose default providers are disabled. Attempting to
invoke a disabled default provider will fail, raising an error as in the previous example.

[req]:<https://github.com/pulumi/pulumi/issues/3383>
[release]:<https://github.com/pulumi/pulumi/releases/tag/v3.23.0>

## How to disable default providers

Disabling a default provider involves adding the relevant package name to the config list
`pulumi:disable-default-providers`. For example, disabling the default provider for Kubernetes and AWS would look like
this snippet in the [configuration file][config]:

[config]:{{< relref "/docs/intro/concepts/project#stack-settings-file" >}}

```yaml
pulumi:disable-default-providers:
- aws
- kubernetes
```

If you want to enforce that no resource should use a default provider, you would add the following snippet to the
configuration file:

```yaml
pulumi:disable-default-providers: [“*”]
```

Now that you can [disable the default provider][dis-def-prov], you don’t have to worry about all of the possible unexpected consequences
accidentally relying on your system configuration. We can’t wait to find out what you’ll build next! If you want to have
an impact on our roadmap, you can go to our [public roadmap][roadmap] and vote on issues with the rest of the community.
Let us know what you think!

[dis-def-prov]:{{< relref "/docs/intro/concepts/resources/providers#disabling-default-providers" >}}
[roadmap]:<https://github.com/orgs/pulumi/projects/44>
