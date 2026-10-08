---
title_tag: "Assets & archives | Pulumi Concepts"
meta_desc: Assets and archives are built-in Pulumi types for passing files and folders to resources. Learn the six kinds and how Pulumi detects content changes.
title: Assets & archives
h1: Assets & archives
menu:
    iac:
        name: Assets & archives
        parent: iac-concepts
        weight: 110
search:
   keywords:
      - FileAsset
      - StringAsset
      - RemoteAsset
      - FileArchive
      - RemoteArchive
      - AssetArchive
      - fileasset
      - filearchive
      - assetarchive
      - fn::fileAsset
      - fn::fileArchive
      - asset hash
      - archive formats
aliases:
- /docs/intro/concepts/assets-archives/
- /docs/concepts/inputs-outputs/assets-archives/
- /docs/concepts/assets-archives/
---

Some resource inputs take a file or a folder instead of a string or a number. Pulumi has two built-in types for those inputs: an *asset*, which is a single file, and an *archive*, which is a collection of files. When you pass one to a resource, Pulumi reads the contents, packages them in the format the resource expects, and tracks them as part of your stack.

Each type comes in three kinds that differ in where the contents come from. An asset's contents come from an in-memory string, a path on disk, or a remote URI. An archive's contents come from a path on disk, a remote URI, or a map of other assets and archives. Most languages expose them as constructors. YAML and Pulumi HCL expose them as built-in functions instead, so the names look a little different there: `fn::fileAsset` in YAML, and all-lowercase `fileasset` in Pulumi HCL.

## Assets {#assets}

An asset is a single file. Pass one to any resource input that expects a file, such as the body of an object in a storage bucket.

### `FileAsset`

Takes the contents from a file on disk. This is the most common kind: point it at a path in your project, and Pulumi uses whatever is in that file at deployment time.

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const indexHtml = new pulumi.asset.FileAsset("./index.html");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
index_html = pulumi.FileAsset("./index.html")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
indexHTML := pulumi.NewFileAsset("./index.html")
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var indexHtml = new FileAsset("./index.html");
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var indexHtml = new FileAsset("./index.html");
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
variables:
  indexHtml:
    fn::fileAsset: ./index.html
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
locals {
  index_html = fileasset("./index.html")
}
```

{{% /choosable %}}

{{< /chooser >}}

### `StringAsset`

Takes the contents from a string in memory. Reach for this when your program computes the file contents rather than reading them from disk, such as rendering a configuration file from stack outputs.

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const greeting = new pulumi.asset.StringAsset("Hello, world!");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
greeting = pulumi.StringAsset("Hello, world!")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
greeting := pulumi.NewStringAsset("Hello, world!")
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var greeting = new StringAsset("Hello, world!");
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var greeting = new StringAsset("Hello, world!");
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
variables:
  greeting:
    fn::stringAsset: Hello, world!
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
locals {
  greeting = stringasset("Hello, world!")
}
```

{{% /choosable %}}

{{< /chooser >}}

### `RemoteAsset`

Takes the contents from a URI. Pulumi supports the `http`, `https`, and `file` schemes. A `file://` URI must have an empty host or `localhost`; it cannot point at another machine.

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const license = new pulumi.asset.RemoteAsset("https://example.com/LICENSE.txt");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
license = pulumi.RemoteAsset("https://example.com/LICENSE.txt")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
license := pulumi.NewRemoteAsset("https://example.com/LICENSE.txt")
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var license = new RemoteAsset("https://example.com/LICENSE.txt");
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var license = new RemoteAsset("https://example.com/LICENSE.txt");
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
variables:
  license:
    fn::remoteAsset: https://example.com/LICENSE.txt
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
locals {
  license = remoteasset("https://example.com/LICENSE.txt")
}
```

{{% /choosable %}}

{{< /chooser >}}

## Archives {#archives}

An archive is a collection of files. A resource that takes an archive, such as a serverless function's code bundle, receives them all at once.

Pulumi recognizes archive files by extension: `.tar`, `.tgz`, `.tar.gz`, `.zip`, and `.jar`. Detection is based on the extension alone, so a `.zip` file renamed to something else is not recognized as an archive.

### `FileArchive`

Takes the contents from a path on disk, which can be either a folder or an existing archive file in one of the supported formats. Pointing it at a folder is the usual choice for a serverless function's source, as in the [AWS Lambda guide](/docs/iac/guides/clouds/aws/lambda/).

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const app = new pulumi.asset.FileArchive("./app");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
app = pulumi.FileArchive("./app")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
app := pulumi.NewFileArchive("./app")
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var app = new FileArchive("./app");
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var app = new FileArchive("./app");
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
variables:
  app:
    fn::fileArchive: ./app
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
locals {
  app = filearchive("./app")
}
```

{{% /choosable %}}

{{< /chooser >}}

{{% notes type="info" %}}
When `FileArchive` points at a folder, Pulumi packs everything under it, minus the `.pulumi` bookkeeping directory. Symbolic links to files are followed and stored as copies, and symbolic links to directories are skipped. Ignore files are not supported, so anything you leave in the folder, such as a `node_modules` or `.venv` directory, ships with the archive.
{{% /notes %}}

### `RemoteArchive`

Takes an archive from an `http`, `https`, or `file` URI. The file it fetches must be in one of the supported archive formats.

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const app = new pulumi.asset.RemoteArchive("https://example.com/app.zip");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
app = pulumi.RemoteArchive("https://example.com/app.zip")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
app := pulumi.NewRemoteArchive("https://example.com/app.zip")
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var app = new RemoteArchive("https://example.com/app.zip");
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var app = new RemoteArchive("https://example.com/app.zip");
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
variables:
  app:
    fn::remoteArchive: https://example.com/app.zip
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
locals {
  app = remotearchive("https://example.com/app.zip")
}
```

{{% /choosable %}}

{{< /chooser >}}

### `AssetArchive`

Builds an archive from a map of other assets and archives, which lets you assemble a bundle in your program instead of staging a directory on disk. Each entry is either one file, from an asset, or one folder, from an archive, and archives can nest.

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const bundle = new pulumi.asset.AssetArchive({
    "config.json": new pulumi.asset.StringAsset(JSON.stringify({ debug: false })),
    "src": new pulumi.asset.FileArchive("./src"),
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
bundle = pulumi.AssetArchive({
    "config.json": pulumi.StringAsset('{"debug": false}'),
    "src": pulumi.FileArchive("./src"),
})
```

{{% /choosable %}}
{{% choosable language go %}}

```go
bundle := pulumi.NewAssetArchive(map[string]any{
    "config.json": pulumi.NewStringAsset(`{"debug": false}`),
    "src":         pulumi.NewFileArchive("./src"),
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var bundle = new AssetArchive(new Dictionary<string, AssetOrArchive>
{
    { "config.json", new StringAsset("{\"debug\": false}") },
    { "src", new FileArchive("./src") },
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var bundle = new AssetArchive(Map.of(
    "config.json", new StringAsset("{\"debug\": false}"),
    "src", new FileArchive("./src")));
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
variables:
  bundle:
    fn::assetArchive:
      config.json:
        fn::stringAsset: '{"debug": false}'
      src:
        fn::fileArchive: ./src
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
locals {
  bundle = assetarchive({
    "config.json" = stringasset("{\"debug\": false}")
    "src"         = filearchive("./src")
  })
}
```

{{% /choosable %}}

{{< /chooser >}}

## Passing assets and archives to resources

Any of these values can be passed to a resource input that accepts one. This example uploads a local file as the body of an object in an S3 bucket.

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const indexHtml = new aws.s3.BucketObject("index.html", {
    bucket: bucket.id,
    key: "index.html",
    source: new pulumi.asset.FileAsset("./index.html"),
    contentType: "text/html",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
index_html = aws.s3.BucketObject("index.html",
    bucket=bucket.id,
    key="index.html",
    source=pulumi.FileAsset("./index.html"),
    content_type="text/html")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
indexHTML, err := s3.NewBucketObject(ctx, "index.html", &s3.BucketObjectArgs{
    Bucket:      bucket.ID(),
    Key:         pulumi.String("index.html"),
    Source:      pulumi.NewFileAsset("./index.html"),
    ContentType: pulumi.String("text/html"),
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var indexHtml = new BucketObject("index.html", new()
{
    Bucket = bucket.Id,
    Key = "index.html",
    Source = new FileAsset("./index.html"),
    ContentType = "text/html",
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var indexHtml = new BucketObject("index.html", BucketObjectArgs.builder()
    .bucket(bucket.id())
    .key("index.html")
    .source(new FileAsset("./index.html"))
    .contentType("text/html")
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  index.html:
    type: aws:s3:BucketObject
    properties:
      bucket: ${bucket.id}
      key: index.html
      source:
        fn::fileAsset: ./index.html
      contentType: text/html
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
resource "aws_s3_bucket_object" "index-html" {
  bucket       = aws_s3_bucket.bucket.id
  key          = "index.html"
  source       = fileasset("./index.html")
  content_type = "text/html"
}
```

{{% /choosable %}}

{{< /chooser >}}

An archive is passed the same way, to an input that expects a collection of files. The most common example is a serverless function's code, such as the `code` property of an [AWS Lambda function](/docs/iac/guides/clouds/aws/lambda/).

## How Pulumi detects changes {#change-detection}

Pulumi identifies an asset or an archive by a SHA256 hash of its contents, not by the path or URI it came from. Two assets are the same when their hashes match, even if one was read from disk and the other from a URL, and they are different when their hashes differ, even if both point at the same path.

That hash is computed from the live contents on every deployment. Edit a file that a `FileAsset` points at, run `pulumi up`, and the property shows a diff. Leave it alone and it does not. The same applies to a `RemoteAsset` or `RemoteArchive`, which Pulumi fetches over the network each deployment to compute the hash, so a change at the other end of the URL shows up as a change in your stack.

When a `FileArchive` points at a *folder*, Pulumi packs it deterministically: files are walked in a fixed order and stored with fixed metadata. The hash depends only on file names and contents, not on timestamps or permissions, so touching a file without editing it produces no diff.

{{% notes type="warning" %}}
When a `FileArchive` points at an existing archive *file*, Pulumi hashes that file's bytes as they are. Most archiving tools record a timestamp for every entry, so re-creating the archive from unchanged sources produces different bytes, a different hash, and a redeployment. If a resource keeps updating when nothing has changed, point `FileArchive` at the source folder and let Pulumi do the packing, or make your packaging step reproducible.
{{% /notes %}}

## Working with file paths

Relative paths are resolved against the directory Pulumi runs your program in, which is your project directory, not the directory you happened to run the CLI from. Running `pulumi up -C my-project` resolves `./index.html` inside `my-project`, regardless of your shell's location. Paths are also relative to the program as a whole, not to the individual source file that constructs the asset, which matters once you split a program across several files or directories.

In Pulumi HCL, the asset and archive functions resolve relative paths against the program's base directory in the same way.

## Learn more

- [Inputs and outputs](/docs/iac/concepts/inputs-outputs/) explains how resource properties flow through a Pulumi program.
- [AWS Lambda](/docs/iac/guides/clouds/aws/lambda/) shows archives packaging serverless function code end to end.
- The full API surface for each language: [TypeScript and JavaScript](/docs/reference/pkg/nodejs/pulumi/pulumi/modules/asset.html), [Python](/docs/reference/pkg/python/pulumi/#pulumi.Asset), [Go](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi#Asset), [.NET](/docs/reference/pkg/dotnet/pulumi/pulumi.asset.html), and [Java](/docs/reference/pkg/java/com/pulumi/asset/package-summary.html).
- The built-in functions for [YAML](/docs/iac/languages-sdks/yaml/yaml-language-reference/) and [Pulumi HCL](/docs/iac/languages-sdks/hcl/hcl-language-reference/).
