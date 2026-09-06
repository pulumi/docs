---
title_tag: "Classes & Components | Language Essentials"
meta_desc: Learn the minimal class syntax you need and how ComponentResource turns a class into a reusable Pulumi module.
title: Classes and Components
h1: Classes and Components
menu:
    iac:
        name: Classes & Components
        parent: iac-guides-language-essentials
        weight: 50
aliases:
    - /docs/iac/guides/language-essentials/classes/
---

A class groups related data and behavior under one name. Where a function
groups a piece of logic, a class groups a piece of state, plus the operations
that act on it, so the group can be passed around, referenced, and reused as
a single thing. You don't need inheritance, interfaces, or generics to use a
class productively in a Pulumi program; the minimal version, a constructor
plus a few fields, covers what you'll actually reach for.

## Where you have seen this before

You've already grouped resources under a shared identity: a Terraform module
with its own inputs and outputs, or, in Pulumi YAML, a set of resources that
share a naming prefix and configuration. A class that extends
`ComponentResource`, covered later on this page, is Pulumi's version of that
same grouping, expressed as a reusable unit in your language rather than a
separate module directory.

## The syntax

A class has fields to hold state and a constructor to set them.

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
class Endpoint {
  readonly host: string;
  readonly port: number;

  constructor(host: string, port: number) {
    this.host = host;
    this.port = port;
  }

  url(): string {
    return `https://${this.host}:${this.port}`;
  }
}

const endpoint = new Endpoint("api.example.com", 443);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
class Endpoint:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def url(self) -> str:
        return f"https://{self.host}:{self.port}"

endpoint = Endpoint("api.example.com", 443)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
type Endpoint struct {
	Host string
	Port int
}

func (e Endpoint) URL() string {
	return fmt.Sprintf("https://%s:%d", e.Host, e.Port)
}

endpoint := Endpoint{Host: "api.example.com", Port: 443}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
class Endpoint
{
    public string Host { get; }
    public int Port { get; }

    public Endpoint(string host, int port)
    {
        Host = host;
        Port = port;
    }

    public string Url() => $"https://{Host}:{Port}";
}

var endpoint = new Endpoint("api.example.com", 443);
```

{{% /choosable %}}
{{% choosable language java %}}

```java
class Endpoint {
    final String host;
    final int port;

    Endpoint(String host, int port) {
        this.host = host;
        this.port = port;
    }

    String url() {
        return "https://" + host + ":" + port;
    }
}

var endpoint = new Endpoint("api.example.com", 443);
```

{{% /choosable %}}
{{% choosable language yaml %}}

Pulumi YAML has no classes and no way to define a reusable type. It works
directly with the resource types and object shapes that a provider or
component already defines.

{{% /choosable %}}
{{% choosable language hcl %}}

Terraform HCL has no classes either. A module, shown below, is the closest
equivalent, and it's a directory-level construct rather than a language-level
one.

{{% /choosable %}}

{{< /chooser >}}

Go doesn't have classes; a `struct` plus functions that take it as a receiver
serves the same purpose, as shown above.

## In a Pulumi program

Pulumi's equivalent of a Terraform module is a class that extends
`ComponentResource`. It groups a set of resources under one logical name in
the resource graph, exposes the outputs that matter, and can be instantiated
as many times as you need, each with its own name:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

export class StaticWebsite extends pulumi.ComponentResource {
  public readonly bucket: aws.s3.Bucket;
  public readonly url: pulumi.Output<string>;

  constructor(
    name: string,
    args: { indexDocument: string },
    opts?: pulumi.ComponentResourceOptions,
  ) {
    super("example:index:StaticWebsite", name, {}, opts);

    this.bucket = new aws.s3.Bucket(
      `${name}-bucket`,
      { website: { indexDocument: args.indexDocument } },
      { parent: this },
    );

    this.url = this.bucket.websiteEndpoint;

    this.registerOutputs({ url: this.url });
  }
}

const site = new StaticWebsite("docs", { indexDocument: "index.html" });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws

class StaticWebsite(pulumi.ComponentResource):
    def __init__(self, name: str, index_document: str, opts: pulumi.ResourceOptions = None):
        super().__init__("example:index:StaticWebsite", name, {}, opts)

        self.bucket = aws.s3.Bucket(
            f"{name}-bucket",
            website=aws.s3.BucketWebsiteArgs(index_document=index_document),
            opts=pulumi.ResourceOptions(parent=self),
        )

        self.url = self.bucket.website_endpoint

        self.register_outputs({"url": self.url})

site = StaticWebsite("docs", "index.html")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
type StaticWebsiteArgs struct {
	IndexDocument string
}

type StaticWebsite struct {
	pulumi.ResourceState

	URL pulumi.StringOutput `pulumi:"url"`
}

func NewStaticWebsite(ctx *pulumi.Context, name string, args StaticWebsiteArgs, opts ...pulumi.ResourceOption) (*StaticWebsite, error) {
	component := &StaticWebsite{}
	if err := ctx.RegisterComponentResource("example:index:StaticWebsite", name, component, opts...); err != nil {
		return nil, err
	}

	bucket, err := s3.NewBucket(ctx, name+"-bucket", &s3.BucketArgs{
		Website: &s3.BucketWebsiteArgs{
			IndexDocument: pulumi.String(args.IndexDocument),
		},
	}, pulumi.Parent(component))
	if err != nil {
		return nil, err
	}

	component.URL = bucket.WebsiteEndpoint
	if err := ctx.RegisterResourceOutputs(component, pulumi.Map{"url": component.URL}); err != nil {
		return nil, err
	}
	return component, nil
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
public class StaticWebsiteArgs
{
    public string IndexDocument { get; set; } = "index.html";
}

public class StaticWebsite : ComponentResource
{
    public Output<string> Url { get; private set; }

    public StaticWebsite(string name, StaticWebsiteArgs args, ComponentResourceOptions? opts = null)
        : base("example:index:StaticWebsite", name, opts)
    {
        var bucket = new Bucket($"{name}-bucket", new BucketArgs
        {
            Website = new BucketWebsiteArgs { IndexDocument = args.IndexDocument },
        }, new CustomResourceOptions { Parent = this });

        Url = bucket.WebsiteEndpoint;

        RegisterOutputs(new Dictionary<string, object?> { { "url", Url } });
    }
}

var site = new StaticWebsite("docs", new StaticWebsiteArgs { IndexDocument = "index.html" });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
public class StaticWebsite extends ComponentResource {
    private final Output<String> url;

    public StaticWebsite(String name, String indexDocument, ComponentResourceOptions options) {
        super("example:index:StaticWebsite", name, options);

        var bucket = new Bucket(name + "-bucket", BucketArgs.builder()
            .website(BucketWebsiteArgs.builder().indexDocument(indexDocument).build())
            .build(), CustomResourceOptions.builder().parent(this).build());

        this.url = bucket.websiteEndpoint();

        this.registerOutputs(Map.of("url", Output.of(this.url)));
    }
}

var site = new StaticWebsite("docs", "index.html", CustomResourceOptions.Empty);
```

{{% /choosable %}}

{{< /chooser >}}

The call to the base constructor, `super(...)` in TypeScript, C#, and Java,
`super().__init__(...)` in Python, or `RegisterComponentResource` in Go,
registers the component with Pulumi under a type token. Setting each child
resource's parent to the component attaches it in the resource graph, and
`registerOutputs` (or `RegisterResourceOutputs` in Go) declares which of the
component's own properties are worth exposing.

## Reusing a component across languages

A component authored once, packaged, and published can be consumed from any
Pulumi language, including Pulumi YAML. That means a team that prefers to
keep writing YAML for most of its stacks can still consume a component
someone on the team wrote in Python or Go, without anyone switching
languages for day-to-day work. See
[when to build a component](/docs/iac/guides/building-extending/components/when-to-build-a-component/)
for the decision itself, and
[building a component](/docs/iac/guides/building-extending/components/build-a-component/)
for the full walkthrough, including packaging it for other languages to
consume.

## Frequently asked questions

### Do I need to know object-oriented programming to use Pulumi?

No. Classes are entirely optional in Pulumi, and most day-to-day infrastructure code is plain functions and resource declarations. You only reach for a class when you want to package resources into a reusable, named component that other code can create and reference as a unit.

### What is a ComponentResource?

A `ComponentResource` is a resource that groups a set of child resources under one logical parent and exposes their combined outputs through a single interface, using `registerOutputs` (`RegisterOutputs` in C#). Consumers of the [component](/docs/iac/concepts/components/) interact with that simple interface instead of wiring up each child resource themselves.

### Can I use a component written in another language?

Yes, if it's packaged as a source-based package. Consumers run `pulumi package add` against its Git URL, and Pulumi generates an SDK in whichever language they're using, YAML included. A plain npm- or PyPI-style native language package, by contrast, only works in the language it was published for.

## Next steps

Continue to
[packages and dependencies](/docs/iac/guides/basics/language-essentials/packages-and-dependencies/)
to see how a component gets published and installed like any other package.
