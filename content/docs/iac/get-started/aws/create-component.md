---
title_tag: Create a component | AWS
title: Create a component
h1: "Get started with Pulumi and AWS"
meta_desc: This page provides an overview on how to create infrastructure abstractions with Pulumi.
weight: 7
menu:
    iac:
        name: Create a component
        parent: aws-get-started
        weight: 7
---

## Create a component

[**Components**](/docs/iac/concepts/resources/components/) are infrastructure abstractions that encapsulate
complexity and enable sharing and reuse. Instead of copy-pasting common patterns, you can encode them as components.

You will now create your first component that packages up your S3 website so you can easily stamp out
entire websites in just a few lines of code:

{{% choosable language javascript %}}

```javascript
const website = new AwsS3Website("my-website", {
    files: [ "index.html" ],
});
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
const website = new AwsS3Website("my-website", {
    files: [ "index.html" ],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
website = AwsS3Website('my-website', files=['index.html'])
```

{{% /choosable %}}

{{% choosable language go %}}

```go
website, err := NewAwsS3Website(ctx, "my-website", AwsS3WebsiteArgs{
    Files: []string{"index.html"},
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var website = new AwsS3Website("my-website", new AwsS3WebsiteArgs()
{
    Files = new[] { "index.html" }
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
var website = new AwsS3Website("my-website",
    new AwsS3WebsiteArgs(new String[] { "index.html" }));
```

{{% /choosable %}}

{{% choosable language yaml %}}

{{% notes type="warning" %}}

Unfortunately, YAML lacks the language facilities to author components. Feel free to [skip ahead](/docs/iac/get-started/aws/destroy-stack/).

{{% /notes %}}

{{% /choosable %}}

Using components here also has the benefit that, as the requirements for S3 websites changes, you can
update the one component definition and have all uses of it benefit.

### Define a new component

To define a new component, create a class called `AwsS3Website` that derives from `ComponentResource`. It'll have a mostly-empty
constructor to start with but you will add the AWS S3 resources to it in the next step. You'll also define the inputs for the
component -- the `files` to add to the website -- and outputs -- a single property with the website `url`.

To get going, create a new file {{< compfile >}} alongside {{< langfile >}} and add the following:

{{% choosable language javascript %}}

```javascript
"use strict";
const aws = require("@pulumi/aws");
const pulumi = require("@pulumi/pulumi");

// A component that encapsulates creating an AWS S3 hosted static website.
export class AwsS3Website extends pulumi.ComponentResource {
    constructor(name, args, opts) {
        super("quickstart:index:AwsS3Website", name, args, opts);

        // Component initialization will go here next...

        this.registerOutputs({}); // Signal component completion.
    }
}

module.exports = {
    AWSS3Website,
    AWSS3WebsiteArgs,
};
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

// Arguments for the AWS S3 hosted static website component.
export interface AwsS3WebsiteArgs {
    files: string[]; // a list of files to serve.
}

// A component that encapsulates creating an AWS S3 hosted static website.
export class AwsS3Website extends pulumi.ComponentResource {
    public readonly url: pulumi.Output<string>; // the S3 website url.

    constructor(name: string, args: AwsS3WebsiteArgs, opts: pulumi.ComponentResourceOptions) {
        super("quickstart:index:AwsS3Website", name, args, opts);

        // Component initialization will go here next...

        this.registerOutputs({}); // Signal component completion.
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_aws import s3
from typing import List

# A component that encapsulates creating an AWS S3 hosted static website.
class AwsS3Website(pulumi.ComponentResource):
    def __init__(self, name: str, files: List[str] = None, opts = None):
        super().__init__('quickstart:index:AwsS3Website', name, { 'files': files }, opts)

        # Component initialization will go here next...

        self.register_outputs({}) # Signal component completion.
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type AwsS3Website struct {
    pulumi.ResourceState
    Url pulumi.StringOutput // the S3 website url.
}

type AwsS3WebsiteArgs struct {
    Files []string // a list of files to serve.
}

func NewAwsS3Website(ctx *pulumi.Context, name string, args AwsS3WebsiteArgs, opts ...pulumi.ResourceOption) (*AwsS3Website, error) {
    self := &AwsS3Website{}
    err := ctx.RegisterComponentResource("quickstart:index:AwsS3Website", name, self, opts...)
    if err != nil {
        return nil, err
    }

    // Component initialization will go here next...

    ctx.RegisterResourceOutputs(self, pulumi.Map{}) // Signal component completion.
    return self, nil
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Aws.S3;
using Pulumi.Aws.S3.Inputs;
using System.Collections.Generic;

public class AwsS3WebsiteArgs
{
    public string[]? Files { get; set; }
}

public class AwsS3Website : Pulumi.ComponentResource
{
    public Output<string> Url { get; private set; }

    public AwsS3Website(string name, AwsS3WebsiteArgs args, ComponentResourceOptions? opts = null)
        : base("quickstart:index:AwsS3Website", name, opts)
    {
        // Component initialization will go here next...

        this.RegisterOutputs(new Dictionary<string, object>{}); // Signal component completion.
    }
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.aws.s3.BucketV2;
import com.pulumi.resources.ComponentResource;
import com.pulumi.resources.ComponentResourceOptions;

public class AwsS3WebsiteArgs {
    public String[] files;
    public AwsS3WebsiteArgs(String[] files) {
        this.files = files;
    }
}

public class AwsS3Website extends ComponentResource {
    public Output<String> url;

    public AwsS3Website(String name, AwsS3WebsiteArgs args, ComponentResourceOptions opts) {
        super("quickstart:index:AwsS3Website", name, args, opts);

        // Component initialization will go here next...

        this.registerOutputs(Map.of());
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

{{% notes type="warning" %}}

Unfortunately, YAML lacks the language facilities to author components. Feel free to [skip ahead](/docs/iac/get-started/aws/destroy-stack/).

{{% /notes %}}

{{% /choosable %}}

This defines a component but it doesn't do much yet.

### Refactor your code into the component

Next, make four changes:

1. Move all resources from {{< langfile >}} ino the component's constructor
2. Change each resource to use the component [as the `parent`](/docs/iac/concepts/options/parent/)
3. Generalize the creation of bucket objects by looping over the list of `files`
4. Assign the resulting website URL to the `url` property of the component

The resulting {{< compfile >}} file will look like this; feel free to make each edit one at a time if you'd like
to get a feel for things, or simply paste the contents of this into {{< compfile >}}:

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");

// A component that encapsulates creating an AWS S3 hosted static website.
class AwsS3Website extends pulumi.ComponentResource {
    constructor(name, args, opts) {
        super("quickstart:index:AwsS3Website", name, args, opts);

        // Create an AWS resource (S3 Bucket)
        const bucket = new aws.s3.BucketV2("my-bucket", {}, {
            // Set the parent to the component (step #2) above.
            // Also, do the same for all other resources below.
            parent: this,
        });

        // Turn the bucket into a website:
        const website = new aws.s3.BucketWebsiteConfigurationV2("website", {
            bucket: bucket.id,
            indexDocument: {
                suffix: "index.html",
            },
        }, { parent: this });

        // Permit access control configuration:
        const ownershipControls = new aws.s3.BucketOwnershipControls("ownership-controls", {
            bucket: bucket.id,
            rule: {
                objectOwnership: "ObjectWriter"
            }
        }, { parent: this });

        // Enable public access to the website:
        const publicAccessBlock = new aws.s3.BucketPublicAccessBlock("public-access-block", {
            bucket: bucket.id,
            blockPublicAcls: false,
        }, { parent: this });

        // Create an S3 Bucket object for each file; note the changes to name/source:
        for (const file of args.files) {
            new aws.s3.BucketObject(file, {
                bucket: bucket.id,
                source: new pulumi.asset.FileAsset(file),
                contentType: "text/html",
                acl: "public-read",
            }, {
                dependsOn: [ownershipControls, publicAccessBlock],
                parent: this,
            });
        }

        // Capture the URL and make it available as a component property and output:
        this.url = pulumi.interpolate`http://${website.websiteEndpoint}`;
        this.registerOutputs({ url: this.url }) // Signal component completion.
    }
}

module.exports = {
    AWSS3Website,
};
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

// Arguments for the AWS S3 hosted static website component.
export interface AwsS3WebsiteArgs {
    files: string[]; // a list of files to serve.
}

// A component that encapsulates creating an AWS S3 hosted static website.
export class AwsS3Website extends pulumi.ComponentResource {
    public readonly url: pulumi.Output<string>; // the S3 website url.

    constructor(name: string, args: AwsS3WebsiteArgs, opts?: pulumi.ComponentResourceOptions) {
        super("quickstart:index:AwsS3Website", name, args, opts);

        // Create an AWS resource (S3 Bucket)
        const bucket = new aws.s3.BucketV2("my-bucket", {}, {
            // Set the parent to the component (step #2) above.
            // Also, do the same for all other resources below.
            parent: this,
        });

        // Turn the bucket into a website:
        const website = new aws.s3.BucketWebsiteConfigurationV2("website", {
            bucket: bucket.id,
            indexDocument: {
                suffix: "index.html",
            },
        }, { parent: this });

        // Permit access control configuration:
        const ownershipControls = new aws.s3.BucketOwnershipControls("ownership-controls", {
            bucket: bucket.id,
            rule: {
                objectOwnership: "ObjectWriter"
            }
        }, { parent: this });

        // Enable public access to the website:
        const publicAccessBlock = new aws.s3.BucketPublicAccessBlock("public-access-block", {
            bucket: bucket.id,
            blockPublicAcls: false,
        }, { parent: this });

        // Create an S3 Bucket object for each file; note the changes to name/source:
        for (const file of args.files) {
            new aws.s3.BucketObject(file, {
                bucket: bucket.id,
                source: new pulumi.asset.FileAsset(file),
                contentType: "text/html",
                acl: "public-read",
            }, {
                dependsOn: [ownershipControls, publicAccessBlock],
                parent: this,
            });
        }

        // Capture the URL and make it available as a component property and output:
        this.url = pulumi.interpolate`http://${website.websiteEndpoint}`;
        this.registerOutputs({ url: this.url }) // Signal component completion.
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_aws import s3
from typing import List

# A component that encapsulates creating an AWS S3 hosted static website.
class AwsS3Website(pulumi.ComponentResource):
    def __init__(self, name: str, files: List[str] = None, opts = None):
        super().__init__('quickstart:index:AwsS3Website', name, { 'files': files }, opts)

        # Create an AWS resource (S3 Bucket)
        bucket = s3.BucketV2('my-bucket',
            # Set the parent to the component (step #2) above.
            # Also, do the same for all other resources below.
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Turn the bucket into a website:
        website = s3.BucketWebsiteConfigurationV2("website",
            bucket=bucket.id,
            index_document={
                "suffix": "index.html",
            },
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Permit access control configuration:
        ownership_controls = s3.BucketOwnershipControls(
            'ownership-controls',
            bucket=bucket.id,
            rule={
                "object_ownership": 'ObjectWriter',
            },
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Enable public access to the website:
        public_access_block = s3.BucketPublicAccessBlock(
            'public-access-block', bucket=bucket.id, block_public_acls=False,
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Create an S3 Bucket object for each file; note the changes to name/source:
        for file in files:
            s3.BucketObject(
                file,
                bucket=bucket.id,
                source=pulumi.FileAsset(file),
                content_type='text/html',
                acl='public-read',
                opts=pulumi.ResourceOptions(
                    depends_on=[ownership_controls, public_access_block],
                    parent=self,
                ),
            )

        # Capture the URL and make it available as a component property and output:
        self.url = pulumi.Output.concat('http://', website.website_endpoint)
        self.register_outputs({ 'url': self.url }) # Signal component completion.
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"fmt"

	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type AwsS3Website struct {
	pulumi.ResourceState
	Url pulumi.StringOutput // the S3 website url.
}

type AwsS3WebsiteArgs struct {
	Files []string // a list of files to serve.
}

func NewAwsS3Website(ctx *pulumi.Context, name string, args AwsS3WebsiteArgs, opts ...pulumi.ResourceOption) (*AwsS3Website, error) {
	self := &AwsS3Website{}
	err := ctx.RegisterComponentResource("quickstart:index:AwsS3Website", name, self, opts...)
	if err != nil {
		return nil, err
	}

	// Create an AWS resource (S3 Bucket)
	bucket, err := s3.NewBucketV2(ctx, "my-bucket", nil,
		// Set the parent to the component (step #2) above.
		// Also, do the same for all other resources below.
		pulumi.Parent(self))
	if err != nil {
		return nil, err
	}

	// Turn the bucket into a website:
	website, err := s3.NewBucketWebsiteConfigurationV2(ctx, "website", &s3.BucketWebsiteConfigurationV2Args{
		Bucket: bucket.ID(),
		IndexDocument: &s3.BucketWebsiteConfigurationV2IndexDocumentArgs{
			Suffix: pulumi.String("index.html"),
		},
	}, pulumi.Parent(self))
	if err != nil {
		return nil, err
	}

	// Permit access control configuration:
	ownershipControls, err := s3.NewBucketOwnershipControls(ctx, "ownership-controls", &s3.BucketOwnershipControlsArgs{
		Bucket: bucket.ID(),
		Rule: &s3.BucketOwnershipControlsRuleArgs{
			ObjectOwnership: pulumi.String("ObjectWriter"),
		},
	}, pulumi.Parent(self))
	if err != nil {
		return nil, err
	}

	// Enable public access to the website:
	publicAccessBlock, err := s3.NewBucketPublicAccessBlock(ctx, "public-access-block", &s3.BucketPublicAccessBlockArgs{
		Bucket:          bucket.ID(),
		BlockPublicAcls: pulumi.Bool(false),
	}, pulumi.Parent(self))
	if err != nil {
		return nil, err
	}

	// Create an S3 Bucket object for each file; note the changes to name/source:
	for _, file := range args.Files {
		_, err = s3.NewBucketObject(ctx, file, &s3.BucketObjectArgs{
			Bucket:      bucket.ID(),
			Source:      pulumi.NewFileAsset(file),
			ContentType: pulumi.String("text/html"),
			Acl:         pulumi.String("public-read"),
		}, pulumi.DependsOn([]pulumi.Resource{ownershipControls, publicAccessBlock}), pulumi.Parent(self))
		if err != nil {
			return nil, err
		}
	}

	// Export the bucket's autoassigned URL:
	self.Url = website.WebsiteEndpoint.ApplyT(func(websiteEndpoint string) (string, error) {
		return fmt.Sprintf("http://%v", websiteEndpoint), nil
	}).(pulumi.StringOutput)

	ctx.RegisterResourceOutputs(website, pulumi.Map{"url": self.Url}) // Signal component completion.
	return self, nil
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Aws.S3;
using Pulumi.Aws.S3.Inputs;
using System.Collections.Generic;

public class AwsS3WebsiteArgs
{
    public string[]? Files { get; set; }
}

public class AwsS3Website : Pulumi.ComponentResource
{
    public Output<string> Url { get; private set; }

    public AwsS3Website(string name, AwsS3WebsiteArgs args, ComponentResourceOptions? opts = null)
        : base("quickstart:index:AwsS3Website", name, opts)
    {
        // Create an AWS resource (S3 Bucket)
        var bucket = new BucketV2("my-bucket", new(), new CustomResourceOptions
        {
            // Set the parent to the component (step #2) above.
            // Also, do the same for all other resources below.
            Parent = this,
        });

        // Turn the bucket into a website:
        var website = new BucketWebsiteConfigurationV2("website", new()
        {
            Bucket = bucket.Id,
            IndexDocument = new BucketWebsiteConfigurationV2IndexDocumentArgs
            {
                Suffix = "index.html",
            },
        }, new CustomResourceOptions
        {
            Parent = this,
        });

        // Permit access control configuration:
        var ownershipControls = new BucketOwnershipControls("ownership-controls", new()
        {
            Bucket = bucket.Id,
            Rule = new BucketOwnershipControlsRuleArgs
            {
                ObjectOwnership = "ObjectWriter",
            },
        }, new CustomResourceOptions
        {
            Parent = this,
        });

        // Enable public access to the website:
        var publicAccessBlock = new BucketPublicAccessBlock("public-access-block", new()
        {
            Bucket = bucket.Id,
            BlockPublicAcls = false,
        }, new CustomResourceOptions
        {
            Parent = this,
        });

        // Create an S3 Bucket object for each file; note the changes to name/source:
        foreach (var file in args.Files) {
            new BucketObject(file, new()
            {
                Bucket = bucket.Id,
                Source = new FileAsset(file),
                ContentType = "text/html",
                Acl = "public-read",
            }, new CustomResourceOptions
            {
                DependsOn = new Resource[]
                {
                    ownershipControls,
                    publicAccessBlock,
                },
                Parent = this,
            });
        }

        // Export the bucket's autoassigned URL:
        this.Url = website.WebsiteEndpoint.Apply(websiteEndpoint => $"http://{websiteEndpoint}");
        this.RegisterOutputs(new Dictionary<string, object?>{
            ["url"] = this.Url
        });
    }
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.*;
import com.pulumi.core.*;
import com.pulumi.asset.FileAsset;
import com.pulumi.resources.*;

import com.pulumi.aws.s3.*;
import com.pulumi.aws.s3.inputs.*;

import java.util.Map;

class AwsS3WebsiteArgs extends ResourceArgs {
    public String[] files;
    public AwsS3WebsiteArgs(String[] files) {
        this.files = files;
    }
}

class AwsS3Website extends ComponentResource {
    public Output<String> url;

    public AwsS3Website(String name, AwsS3WebsiteArgs args) {
        this(name, args, null);
    }

    public AwsS3Website(String name, AwsS3WebsiteArgs args, ComponentResourceOptions opts) {
        super("quickstart:index:AwsS3Website", name, args, opts);

        // Create an AWS resource (S3 Bucket)
        var bucket = new BucketV2("my-bucket", null,
            // Set the parent to the component (step #2) above.
            // Also, do the same for all other resources below.
            CustomResourceOptions.builder().parent(this).build());

        // Turn the bucket into a website:
        var website = new BucketWebsiteConfigurationV2("website", BucketWebsiteConfigurationV2Args.builder()
            .bucket(bucket.id())
            .indexDocument(BucketWebsiteConfigurationV2IndexDocumentArgs.builder()
                .suffix("index.html")
                .build())
            .build(), CustomResourceOptions.builder().parent(this).build());

        // Permit access control configuration:
        var ownershipControls = new BucketOwnershipControls("ownershipControls", BucketOwnershipControlsArgs.builder()
            .bucket(bucket.id())
            .rule(BucketOwnershipControlsRuleArgs.builder()
                .objectOwnership("ObjectWriter")
                .build())
            .build(), CustomResourceOptions.builder().parent(this).build());

        // Enable public access to the website:
        var publicAccessBlock = new BucketPublicAccessBlock("publicAccessBlock", BucketPublicAccessBlockArgs.builder()
            .bucket(bucket.id())
            .blockPublicAcls(false)
            .build(), CustomResourceOptions.builder().parent(this).build());

        // Create an S3 Bucket object for each file; note the changes to name/source:
        for (var file : args.files) {
            new BucketObject("index.html", BucketObjectArgs.builder()
                .bucket(bucket.id())
                .source(new FileAsset("index.html"))
                .contentType("text/html")
                .acl("public-read")
                .build(), CustomResourceOptions.builder()
                    .dependsOn(
                        ownershipControls,
                        publicAccessBlock)
                    .parent(this)
                    .build());
        }

        // Export the bucket's autoassigned URL:
        this.url = website.websiteEndpoint().applyValue(
            websiteEndpoint -> String.format("http://%s", websiteEndpoint));
        this.registerOutputs(Map.of("url", this.url));
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

{{% notes type="warning" %}}

Unfortunately, YAML lacks the language facilities to author components. Feel free to [skip ahead](/docs/iac/get-started/aws/destroy-stack/).

{{% /notes %}}

{{% /choosable %}}

### Instantiate the component

Now go back to your original file {{< langfile >}}. Now that you have moved all of the resources, you can start over with a clean slate.
Ensure the file is empty and we will build it back up by simply importing and instantiating our new component.

Add this to your now-empty {{< langfile >}}:

{{% choosable language javascript %}}

```javascript
"use strict";
// Import from our new component module:
const web = require("./website");

// Create an instance of our component with the same files as before:
const website = new web.AwsS3Website("my-website", {
    files: [ "index.html" ],
});

exports.url = website.url;
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
// Import from our new component module:
import { AwsS3Website } from "./website";

// Create an instance of our component with the same files as before:
const website = new AwsS3Website("my-website", {
    files: [ "index.html" ],
});

// And export its autoassigned URL:
export const url = website.url;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi

# Import from our new component module:
from website import AwsS3Website

# Create an instance of our component with the same files as before:
website = AwsS3Website('my-website', files=['index.html'])

# And export its autoassigned URL:
pulumi.export("url", website.url)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create an instance of our component with the same files as before:
        website, err := NewAwsS3Website(ctx, "my-website", AwsS3WebsiteArgs{
            Files: []string{"index.html"},
        })
        if err != nil {
            return err
        }

        // And export its autoassigned URL:
        ctx.Export("url", website.Url)
        return nil
	  })
}

```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Aws.S3;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
    // Create an instance of our component with the same files as before:
    var website = new AwsS3Website("my-website", new AwsS3WebsiteArgs()
    {
        Files = new[] { "index.html" }
    });

   // And export its autoassigned URL:
   return new Dictionary<string, object?>
   {
      ["url"] = website.Url
   };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create an instance of our component with the same files as before:
            var website = new AwsS3Website("my-website",
                new AwsS3WebsiteArgs(new String[] { "index.html" }));

            // And export its autoassigned URL:
            ctx.export("url", website.url);
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

{{% notes type="warning" %}}

Unfortunately, YAML lacks the language facilities to author components. Feel free to [skip ahead](/docs/iac/get-started/aws/destroy-stack/).

{{% /notes %}}

{{% /choosable %}}

### Deploy the component

Now deploy the resulting component instantiation. To do so, run `pulumi up` as usual:

```
$ pulumi up
Previewing update (dev)

     Type                                       Name                 Plan
     pulumi:pulumi:Stack                        quickstart-dev
 +   ├─ quickstart:index:AwsS3Website           my-site              create
 +   │  ├─ aws:s3:BucketV2                      my-bucket            create
 +   │  ├─ aws:s3:BucketWebsiteConfigurationV2  website              create
 +   │  ├─ aws:s3:BucketOwnershipControls       ownership-controls   create
 +   │  ├─ aws:s3:BucketPublicAccessBlock       public-access-block  create
 +   │  └─ aws:s3:BucketObject                  index.html           create
 -   ├─ aws:s3:BucketObject                     index.html           delete
 -   ├─ aws:s3:BucketPublicAccessBlock          public-access-block  delete
 -   ├─ aws:s3:BucketOwnershipControls          ownership-controls   delete
 -   ├─ aws:s3:BucketWebsiteConfigurationV2     website              delete
 -   └─ aws:s3:BucketV2                         my-bucket            delete

Resources:
    + 6 to create
    - 5 to delete
    11 changes. 1 unchanged

Do you want to perform this update?  [Use arrows to move, type to filter]
  yes
> no
  details
```

This preview shows you a few things. First, you'll see our `AwsS3Website` component with all of its children
resources neatly parented underneath it. This helps to see what resources relate to which components. Next,
you'll see that your old resources are being destroyed.

{{% notes type="info" %}}

If you're wondering why Pulumi didn't simply update the resources in place, it's because certain changes -- like
refactoring resources into a component -- fundamentally change a resource's identity. Many changes like updating
properties or moving resources between files are not disruptive like this. It such cases, you can assign
[aliases](/docs/iac/concepts/options/aliases/) to prevent deletions from happening.

{{% /notes %}}

Accept the changes by selecting `yes` and the deployment will occur:

```
Updating (dev)

     Type                                       Name                 Status
     pulumi:pulumi:Stack                        pu-quickstart-dev
 +   ├─ quickstart:index:AwsS3Website           my-site              created (0.16s)
 +   │  ├─ aws:s3:BucketV2                      my-bucket            created (1s)
 +   │  ├─ aws:s3:BucketWebsiteConfigurationV2  website              created (0.24s)
 +   │  ├─ aws:s3:BucketPublicAccessBlock       public-access-block  created (0.49s)
 +   │  ├─ aws:s3:BucketOwnershipControls       ownership-controls   created (0.63s)
 +   │  └─ aws:s3:BucketObject                  index.html           created (0.19s)
 -   ├─ aws:s3:BucketObject                     index.html           deleted (0.18s)
 -   ├─ aws:s3:BucketOwnershipControls          ownership-controls   deleted (0.58s)
 -   ├─ aws:s3:BucketPublicAccessBlock          public-access-block  deleted (0.18s)
 -   ├─ aws:s3:BucketWebsiteConfigurationV2     website              deleted (0.27s)
 -   └─ aws:s3:BucketV2                         my-bucket            deleted (0.51s)

Outputs:
  ~ url: "http://my-bucket-b531107.s3-website-us-west-2.amazonaws.com" => "http://my-bucket-d05c30a.s3-website-us-west-2.amazonaws.com"

Resources:
    + 6 created
    - 5 deleted
    11 changes. 1 unchanged

Duration: 10s
```

Now test out your new website -- it works like before, just with a tidier codebase now!

{{% choosable os "linux,macos" %}}

```bash
$ curl $(pulumi stack output url)
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
```

{{% /choosable %}}

{{% choosable os "windows" %}}

```powershell
> curl (pulumi stack output url)
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
```

{{% /choosable %}}

Once you are ready to move on, let's destroy everything we've spun up in this tutorial.

{{< get-started-stepper >}}
