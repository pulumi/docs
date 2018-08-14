---
title: Module asset
---

<a href="../index.html">@pulumi/pulumi</a> &gt; asset

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Archive">class Archive</a>
* <a href="#Asset">class Asset</a>
* <a href="#AssetArchive">class AssetArchive</a>
* <a href="#FileArchive">class FileArchive</a>
* <a href="#FileAsset">class FileAsset</a>
* <a href="#RemoteArchive">class RemoteArchive</a>
* <a href="#RemoteAsset">class RemoteAsset</a>
* <a href="#StringAsset">class StringAsset</a>
* <a href="#AssetMap">type AssetMap</a>

<a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/archive.ts">asset/archive.ts</a> <a href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/asset.ts">asset/asset.ts</a> 


<h2 class="pdoc-module-header" id="Archive">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/archive.ts#L21">class Archive</a>
</h2>

An Archive represents a collection of named assets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/archive.ts#L32">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of an Archive.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h2 class="pdoc-module-header" id="Asset">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/asset.ts#L20">class Asset</a>
</h2>

Asset represents a single blob of text or data that is managed as a first class entity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/asset.ts#L31">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of an Asset.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h2 class="pdoc-module-header" id="AssetArchive">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/archive.ts#L45">class AssetArchive</a>
</h2>

An AssetArchive is an archive created from an in-memory collection of named assets or other archives.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/archive.ts#L49">constructor</a>
</h3>

```typescript
new AssetArchive(assets: AssetMap | Promise<AssetMap>)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/archive.ts#L32">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of an Archive.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/archive.ts#L49">property assets</a>
</h3>

```typescript
public assets: Promise<AssetMap>;
```


A map of names to assets.

<h2 class="pdoc-module-header" id="FileArchive">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/archive.ts#L61">class FileArchive</a>
</h2>

A FileArchive is a file-based archive, or a collection of file-based assets.  This can be a raw directory or a
single archive file in one of the supported formats (.tar, .tar.gz, or .zip).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/archive.ts#L65">constructor</a>
</h3>

```typescript
new FileArchive(path: string | Promise<string>)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/archive.ts#L32">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of an Archive.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/archive.ts#L65">property path</a>
</h3>

```typescript
public path: Promise<string>;
```


The path to the asset file.

<h2 class="pdoc-module-header" id="FileAsset">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/asset.ts#L50">class FileAsset</a>
</h2>

FileAsset is a kind of asset produced from a given path to a file on the local filesystem.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/asset.ts#L54">constructor</a>
</h3>

```typescript
new FileAsset(path: string | Promise<string>)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/asset.ts#L31">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of an Asset.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/asset.ts#L54">property path</a>
</h3>

```typescript
public path: Promise<string>;
```


The path to the asset file.

<h2 class="pdoc-module-header" id="RemoteArchive">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/archive.ts#L78">class RemoteArchive</a>
</h2>

A RemoteArchive is a file-based archive fetched from a remote location.  The URI's scheme dictates the
protocol for fetching the archive's contents: `file://` is a local file (just like a FileArchive), `http://` and
`https://` specify HTTP and HTTPS, respectively, and specific providers may recognize custom schemes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/archive.ts#L82">constructor</a>
</h3>

```typescript
new RemoteArchive(uri: string | Promise<string>)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/archive.ts#L32">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of an Archive.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/archive.ts#L82">property uri</a>
</h3>

```typescript
public uri: Promise<string>;
```


The URI where the archive lives.

<h2 class="pdoc-module-header" id="RemoteAsset">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/asset.ts#L82">class RemoteAsset</a>
</h2>

RemoteAsset is a kind of asset produced from a given URI string.  The URI's scheme dictates the protocol for fetching
contents: `file://` specifies a local file, `http://` and `https://` specify HTTP and HTTPS, respectively.  Note that
specific providers may recognize alternative schemes; this is merely the base-most set that all providers support.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/asset.ts#L86">constructor</a>
</h3>

```typescript
new RemoteAsset(uri: string | Promise<string>)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/asset.ts#L31">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of an Asset.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/asset.ts#L86">property uri</a>
</h3>

```typescript
public uri: Promise<string>;
```


The URI where the asset lives.

<h2 class="pdoc-module-header" id="StringAsset">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/asset.ts#L65">class StringAsset</a>
</h2>

StringAsset is a kind of asset produced from an in-memory UTF8-encoded string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/asset.ts#L69">constructor</a>
</h3>

```typescript
new StringAsset(text: string | Promise<string>)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/asset.ts#L31">method isInstance</a>
</h3>

```typescript
public static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of an Asset.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/asset.ts#L69">property text</a>
</h3>

```typescript
public text: Promise<string>;
```


The string contents.

<h2 class="pdoc-module-header" id="AssetMap">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi/blob/master/sdk/nodejs/asset/archive.ts#L40">type AssetMap</a>
</h2>

```typescript
type AssetMap = { ... };
```


AssetMap is a map of assets.

