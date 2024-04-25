---
title_tag: "Assets & Archives"
meta_desc: "The Pulumi SDK provides two classes for working with files: Asset and Archive. Learn about the different object types for each class and how to use them."
title: Assets & archives
h1: Assets & archives
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    weight: 13
aliases:
- /docs/intro/concepts/assets-archives/
- /docs/concepts/inputs-outputs/assets-archives/
---

The Pulumi SDK provides two classes for working with files: `Asset` and `Archive`. Some Pulumi resource inputs accept either an `Asset` or an `Archive` as input, and Pulumi understands how to take the files referenced by the `Asset` or `Archive` and package them up for use by the resource. There are several different concrete implementations of these two concepts, based on the three ways the files might be provided, whether in memory, on disk, or in an archive. Similarly, files can be consumed by resources that expect a variety of packaging formats.

## Assets

There are three types of `Asset` objects:

- `FileAsset`:  The contents of the asset are read from a file on disk.
- `StringAsset`: The contents of the asset are read from a string in memory.
- `RemoteAsset`: The contents of the asset are read from an `http`, `https` or `file` URI.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let fileAsset = new pulumi.asset.FileAsset("./file.txt");
let stringAsset = new pulumi.asset.StringAsset("Hello, world!");
let remoteAsset = new pulumi.asset.RemoteAsset("http://worldclockapi.com/api/json/est/now");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let fileAsset = new pulumi.asset.FileAsset("./file.txt");
let stringAsset = new pulumi.asset.StringAsset("Hello, world!");
let remoteAsset = new pulumi.asset.RemoteAsset("http://worldclockapi.com/api/json/est/now");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
file_asset = pulumi.FileAsset("./file.txt")
string_asset = pulumi.StringAsset("Hello, world!")
remote_asset = pulumi.RemoteAsset("http://worldclockapi.com/api/json/est/now")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
fileAsset := pulumi.NewFileAsset("./file.txt")
stringAsset := pulumi.NewStringAsset("Hello, world!")
remoteAsset := pulumi.NewRemoteAsset("http://worldclockapi.com/api/json/est/now")
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;

var fileAsset = new FileAsset("./file.txt");
var stringAsset = new StringAsset("Hello, world!");
var remoteAsset = new RemoteAsset("http://worldclockapi.com/api/json/est/now");
```

{{% /choosable %}}
{{% choosable language java %}}

```java
final var fileAsset = new com.pulumi.asset.FileAsset("./file.txt");
final var stringAsset = new com.pulumi.asset.StringAsset("Hello, world!");
final var remoteAsset = new com.pulumi.asset.RemoteAsset("http://worldclockapi.com/api/json/est/now");
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
variables:
  fileAsset:
    Fn::FileAsset: ./file.txt
  stringAsset:
    Fn::StringAsset: Hello, world!
  remoteAsset:
    Fn::RemoteAsset: http://worldclockapi.com/api/json/est/now
```

{{% /choosable %}}

{{< /chooser >}}

Any of these assets can be passed to a resource accepting an `Asset` as input.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let object = new aws.s3.BucketObject(`obj`, {
    bucket: bucket.id,
    key: key,
    source: fileAsset,
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let object = new aws.s3.BucketObject("obj", {
    bucket: bucket.id,
    key: key,
    source: fileAsset,
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
obj = aws.s3.BucketObject("obj",
    bucket=bucket.id,
    key=key,
    source=file_asset)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
obj, err := s3.NewBucketObject(ctx, "obj", &s3.BucketObjectArgs{
    Bucket: bucket.ID(),
    Key:    key,
    Source: fileAsset,
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var obj = new Aws.S3.BucketObject("obj", new Aws.S3.BucketObjectArgs
{
    Bucket = bucket.Id,
    Key = key,
    Source = fileAsset,
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var obj = new com.pulumi.aws.s3.BucketObject("obj",
    com.pulumi.aws.s3.BucketObjectArgs.builder()
        .bucket(bucket.getId())
        .key(key)
        .source(fileAsset)
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  obj:
    type: aws:s3:BucketObject
    properties:
      bucket: ${bucket}
      key: ${key}
      source: ${fileAsset}
```

{{% /choosable %}}

{{< /chooser >}}

## Archives

There are three types of `Archive` objects:

- `FileArchive`: The contents of the archive are read from either a folder on disk or a file on disk in one of the supported formats: `.tar`, `.tgz`, `.tar.gz`, `.zip` or `.jar`.
- `RemoteArchive`: The contents of the asset are read from an `http`, `https` or `file` URI, which must produce an archive of one of the same supported types as `FileArchive`.
- `AssetArchive`:  The contents of the archive are read from a map of either [`Asset`](#asset) or [`Archive`](#archive) objects, one file or folder respectively per entry in the map.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let fileArchive = new pulumi.asset.FileArchive("./file.zip");
let remoteArchive = new pulumi.asset.RemoteArchive("http://contoso.com/file.zip");
let assetArchive = new pulumi.asset.AssetArchive({
    "file": new pulumi.asset.StringAsset("Hello, world!"),
    "folder": new pulumi.asset.FileArchive("./folder"),
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let fileArchive = new pulumi.asset.FileArchive("./file.zip");
let remoteArchive = new pulumi.asset.RemoteArchive("http://contoso.com/file.zip");
let assetArchive = new pulumi.asset.AssetArchive({
    "file": new pulumi.asset.StringAsset("Hello, world!"),
    "folder": new pulumi.asset.FileArchive("./folder"),
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
file_archive = pulumi.FileArchive("./file.zip")
remote_archive = pulumi.RemoteArchive("http://contoso.com/file.zip")
asset_archive = pulumi.AssetArchive({
    "file": pulumi.StringAsset("Hello, world!"),
    "folder": pulumi.FileArchive("./folder")
})
```

{{% /choosable %}}
{{% choosable language go %}}

```go
fileArchive := pulumi.NewFileArchive("./file.zip")
remoteArchive := pulumi.NewRemoteArchive("http://contoso.com/file.zip")
assetArchive := pulumi.NewAssetArchive(map[string]interface{}{
    "file": pulumi.NewStringAsset("Hello, world!"),
    "folder": pulumi.NewFileArchive("./folder"),
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;

var fileArchive = new FileArchive("./file.zip");
var remoteArchive = new RemoteArchive("http://contoso.com/file.zip");
var assetArchive = new AssetArchive(new Dictionary<string, string>
{
    { "file", new StringAsset("Hello, world!") },
    { "folder", new FileArchive("./folder") }
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var fileArchive = new com.pulumi.asset.FileArchive("./file.zip");
var remoteArchive = new com.pulumi.asset.RemoteArchive("http://contoso.com/file.zip");
var assetArchive = new com.pulumi.asset.AssetArchive(
    Map.of(
        "file", new com.pulumi.asset.StringAsset("Hello, world!"),
        "folder", new com.pulumi.asset.FileArchive("./folder")));
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
variables:
  fileArchive:
    Fn::FileArchive: ./file.zip
  remoteArchive:
    Fn::RemoteArchive: http://contoso.com/file.zip
  assetArchive:
    Fn::AssetArchive:
      file:
        Fn::StringAsset: Hello, World!
      folder:
        Fn::FileArchive: ./folder
```

{{% /choosable %}}

{{< /chooser >}}

Note that a folder may be passed to `FileArchive` to construct an archive from the contents of that folder. Also, both assets (single files) and archives (folders containing files) can be combined as part of building up an `AssetArchive`.

Any of these archives can be passed to a resource accepting an `Archive` as input.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let fn = new aws.lambda.Function(`fn`, {
    role: role.arn,
    runtime: "python3.7",
    handler: "hello.handler",
    code: fileArchive,
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let fn = new aws.lambda.Function(`fn`, {
    role: role.arn,
    runtime: "python3.7",
    handler: "hello.handler",
    code: fileArchive,
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
fn = lambda_.Function("fn",
    role=role.arn,
    runtime="python3.7",
    handler="hello.handler",
    code=file_archive)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
fn, err := lambda.NewFunction(ctx, "fn", &lambda.FunctionArgs{
    Bucket:  role.ARN(),
    Runtime: "python3.7",
    Handler: "hello.handler",
    Code:    fileArchive,
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var fn = new Aws.Lambda.Function("fn", new Aws.Lambda.FunctionArgs
{
    Role = role.arn,
    Runtime = "python3.7",
    Handler = "hello.handler",
    Code = fileArchive,
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var fn = new com.pulumi.aws.lambda.Function("fn",
    com.pulumi.aws.lambda.FunctionArgs.builder()
        .role(role.arn())
        .runtime("python3.7")
        .handler("hello.handler")
        .code(fileArchive)
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  fn:
    type: aws:lambda:Function
    properties:
      role: ${role.arn}
      runtime: python3.7
      handler: hello.handler
      code: ${fileArchive}
```

{{% /choosable %}}

{{< /chooser >}}
