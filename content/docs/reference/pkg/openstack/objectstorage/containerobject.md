
---
title: "ContainerObject"
block_external_search_index: true
---



Manages a V1 container object resource within OpenStack.

## Example Usage

### Example with simple content

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as openstack from "@pulumi/openstack";

const container1 = new openstack.objectstorage.Container("container_1", {
    contentType: "application/json",
    metadata: {
        test: "true",
    },
    region: "RegionOne",
});
const doc1 = new openstack.objectstorage.ContainerObject("doc_1", {
    containerName: container1.name,
    content: `               {
                 "foo" : "bar"
               }
`,
    contentType: "application/json",
    metadata: {
        test: "true",
    },
    region: "RegionOne",
});
```

### Example with content from file

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as openstack from "@pulumi/openstack";

const container1 = new openstack.objectstorage.Container("container_1", {
    contentType: "application/json",
    metadata: {
        test: "true",
    },
    region: "RegionOne",
});
const doc1 = new openstack.objectstorage.ContainerObject("doc_1", {
    containerName: container1.name,
    contentType: "application/json",
    metadata: {
        test: "true",
    },
    region: "RegionOne",
    source: "./default.json",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/objectstorage_object_v1.html.markdown.



## Create a ContainerObject Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/objectstorage/#ContainerObject">ContainerObject</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/objectstorage/#ContainerObjectArgs">ContainerObjectArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">ContainerObject</span><span class="p">(resource_name, opts=None, </span>container_name=None<span class="p">, </span>content=None<span class="p">, </span>content_disposition=None<span class="p">, </span>content_encoding=None<span class="p">, </span>content_type=None<span class="p">, </span>copy_from=None<span class="p">, </span>delete_after=None<span class="p">, </span>delete_at=None<span class="p">, </span>detect_content_type=None<span class="p">, </span>etag=None<span class="p">, </span>metadata=None<span class="p">, </span>name=None<span class="p">, </span>object_manifest=None<span class="p">, </span>region=None<span class="p">, </span>source=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewContainerObject<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/objectstorage?tab=doc#ContainerObjectArgs">ContainerObjectArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/objectstorage?tab=doc#ContainerObject">ContainerObject</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.ObjectStorage.ContainerObject.html">ContainerObject</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.OpenStack.ObjectStorage.ContainerObjectArgs.html">ContainerObjectArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

#### Resource Arguments




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique (within an account) name for the container. 
The container name must be from 1 to 256 characters long and can start
with any character and contain any pattern. Character set must be UTF-8.
The container name cannot contain a slash (/) character because this
character delimits the container and object name. For example, the path
/v1/account/www/pages specifies the www container, not the www/pages container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the content of the object. Conflicts with
`source` and `copy_from`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string which specifies the override behavior for 
the browser. For example, this header might specify that the browser use a download
program to save this file rather than show the file, which is the default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the value of the Content-Encoding
metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string which sets the MIME type for the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Copy<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the name of an object 
used to create the new object by copying the `copy_from` object. The value is in form
{container}/{object}. You must UTF-8-encode and then URL-encode the names of the
container and object before you include them in the header. Conflicts with `source` and
`content`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>After</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}An integer representing the number of seconds after which the
system removes the object. Internally, the Object Storage system stores this value in
the X-Delete-At metadata item.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An string representing the date when the system removes the object. 
For example, "2015-08-26" is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Detect<wbr>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If set to true, Object Storage guesses the content 
type based on the file extension and ignores the value sent in the Content-Type
header, if present.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. The only meaningful value is ${md5(file("path/to/file"))}.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Object<wbr>Manifest</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string set to specify that this is a dynamic large 
object manifest object. The value is the container and object name prefix of the
segment objects in the form container/prefix. You must UTF-8-encode and then
URL-encode the names of the container and prefix before you include them in this
header.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to create the container. If
omitted, the `region` argument of the provider is used. Changing this
creates a new container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the local path of a file which will be used
as the object's content. Conflicts with `source` and `copy_from`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique (within an account) name for the container. 
The container name must be from 1 to 256 characters long and can start
with any character and contain any pattern. Character set must be UTF-8.
The container name cannot contain a slash (/) character because this
character delimits the container and object name. For example, the path
/v1/account/www/pages specifies the www container, not the www/pages container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the content of the object. Conflicts with
`source` and `copy_from`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string which specifies the override behavior for 
the browser. For example, this header might specify that the browser use a download
program to save this file rather than show the file, which is the default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the value of the Content-Encoding
metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string which sets the MIME type for the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Copy<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the name of an object 
used to create the new object by copying the `copy_from` object. The value is in form
{container}/{object}. You must UTF-8-encode and then URL-encode the names of the
container and object before you include them in the header. Conflicts with `source` and
`content`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>After</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}An integer representing the number of seconds after which the
system removes the object. Internally, the Object Storage system stores this value in
the X-Delete-At metadata item.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An string representing the date when the system removes the object. 
For example, "2015-08-26" is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Detect<wbr>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If set to true, Object Storage guesses the content 
type based on the file extension and ignores the value sent in the Content-Type
header, if present.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. The only meaningful value is ${md5(file("path/to/file"))}.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Object<wbr>Manifest</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string set to specify that this is a dynamic large 
object manifest object. The value is the container and object name prefix of the
segment objects in the form container/prefix. You must UTF-8-encode and then
URL-encode the names of the container and prefix before you include them in this
header.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to create the container. If
omitted, the `region` argument of the provider is used. Changing this
creates a new container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the local path of a file which will be used
as the object's content. Conflicts with `source` and `copy_from`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique (within an account) name for the container. 
The container name must be from 1 to 256 characters long and can start
with any character and contain any pattern. Character set must be UTF-8.
The container name cannot contain a slash (/) character because this
character delimits the container and object name. For example, the path
/v1/account/www/pages specifies the www container, not the www/pages container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the content of the object. Conflicts with
`source` and `copy_from`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string which specifies the override behavior for 
the browser. For example, this header might specify that the browser use a download
program to save this file rather than show the file, which is the default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the value of the Content-Encoding
metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string which sets the MIME type for the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>copy<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the name of an object 
used to create the new object by copying the `copy_from` object. The value is in form
{container}/{object}. You must UTF-8-encode and then URL-encode the names of the
container and object before you include them in the header. Conflicts with `source` and
`content`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete<wbr>After</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}An integer representing the number of seconds after which the
system removes the object. Internally, the Object Storage system stores this value in
the X-Delete-At metadata item.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An string representing the date when the system removes the object. 
For example, "2015-08-26" is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>detect<wbr>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If set to true, Object Storage guesses the content 
type based on the file extension and ignores the value sent in the Content-Type
header, if present.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. The only meaningful value is ${md5(file("path/to/file"))}.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>object<wbr>Manifest</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string set to specify that this is a dynamic large 
object manifest object. The value is the container and object name prefix of the
segment objects in the form container/prefix. You must UTF-8-encode and then
URL-encode the names of the container and prefix before you include them in this
header.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to create the container. If
omitted, the `region` argument of the provider is used. Changing this
creates a new container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the local path of a file which will be used
as the object's content. Conflicts with `source` and `copy_from`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>container_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique (within an account) name for the container. 
The container name must be from 1 to 256 characters long and can start
with any character and contain any pattern. Character set must be UTF-8.
The container name cannot contain a slash (/) character because this
character delimits the container and object name. For example, the path
/v1/account/www/pages specifies the www container, not the www/pages container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A string representing the content of the object. Conflicts with
`source` and `copy_from`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A string which specifies the override behavior for 
the browser. For example, this header might specify that the browser use a download
program to save this file rather than show the file, which is the default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A string representing the value of the Content-Encoding
metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A string which sets the MIME type for the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>copy_<wbr>from</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A string representing the name of an object 
used to create the new object by copying the `copy_from` object. The value is in form
{container}/{object}. You must UTF-8-encode and then URL-encode the names of the
container and object before you include them in the header. Conflicts with `source` and
`content`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete_<wbr>after</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}An integer representing the number of seconds after which the
system removes the object. Internally, the Object Storage system stores this value in
the X-Delete-At metadata item.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete_<wbr>at</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An string representing the date when the system removes the object. 
For example, "2015-08-26" is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>detect_<wbr>content_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If set to true, Object Storage guesses the content 
type based on the file extension and ignores the value sent in the Content-Type
header, if present.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. The only meaningful value is ${md5(file("path/to/file"))}.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>object_<wbr>manifest</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A string set to specify that this is a dynamic large 
object manifest object. The value is the container and object name prefix of the
segment objects in the form container/prefix. You must UTF-8-encode and then
URL-encode the names of the container and prefix before you include them in this
header.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to create the container. If
omitted, the `region` argument of the provider is used. Changing this
creates a new container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A string representing the local path of a file which will be used
as the object's content. Conflicts with `source` and `copy_from`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## ContainerObject Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Content<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}If the operation succeeds, this value is zero (0) or the 
length of informational or error text in the response body.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date and time the system responded to the request, using the preferred 
format of RFC 7231 as shown in this example Thu, 16 Jun 2016 15:10:38 GMT. The
time is always in UTC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Last<wbr>Modified</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date and time when the object was last modified. The date and time 
stamp format is ISO 8601:
CCYY-MM-DDThh:mm:ss±hh:mm
For example, 2015-08-27T09:49:58-05:00.
The ±hh:mm value, if included, is the time zone as an offset from UTC. In the previous
example, the offset value is -05:00.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Trans<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique transaction ID for this request. Your service provider might 
need this value if you report a problem.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Content<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}If the operation succeeds, this value is zero (0) or the 
length of informational or error text in the response body.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date and time the system responded to the request, using the preferred 
format of RFC 7231 as shown in this example Thu, 16 Jun 2016 15:10:38 GMT. The
time is always in UTC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Last<wbr>Modified</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date and time when the object was last modified. The date and time 
stamp format is ISO 8601:
CCYY-MM-DDThh:mm:ss±hh:mm
For example, 2015-08-27T09:49:58-05:00.
The ±hh:mm value, if included, is the time zone as an offset from UTC. In the previous
example, the offset value is -05:00.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Trans<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique transaction ID for this request. Your service provider might 
need this value if you report a problem.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>content<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}If the operation succeeds, this value is zero (0) or the 
length of informational or error text in the response body.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date and time the system responded to the request, using the preferred 
format of RFC 7231 as shown in this example Thu, 16 Jun 2016 15:10:38 GMT. The
time is always in UTC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>last<wbr>Modified</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date and time when the object was last modified. The date and time 
stamp format is ISO 8601:
CCYY-MM-DDThh:mm:ss±hh:mm
For example, 2015-08-27T09:49:58-05:00.
The ±hh:mm value, if included, is the time zone as an offset from UTC. In the previous
example, the offset value is -05:00.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>trans<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique transaction ID for this request. Your service provider might 
need this value if you report a problem.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>content_<wbr>length</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}If the operation succeeds, this value is zero (0) or the 
length of informational or error text in the response body.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>date</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The date and time the system responded to the request, using the preferred 
format of RFC 7231 as shown in this example Thu, 16 Jun 2016 15:10:38 GMT. The
time is always in UTC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>last_<wbr>modified</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The date and time when the object was last modified. The date and time 
stamp format is ISO 8601:
CCYY-MM-DDThh:mm:ss±hh:mm
For example, 2015-08-27T09:49:58-05:00.
The ±hh:mm value, if included, is the time zone as an offset from UTC. In the previous
example, the offset value is -05:00.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>trans_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique transaction ID for this request. Your service provider might 
need this value if you report a problem.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing ContainerObject Resource

Get an existing ContainerObject resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/objectstorage/#ContainerObjectState">ContainerObjectState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/objectstorage/#ContainerObject">ContainerObject</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>container_name=None<span class="p">, </span>content=None<span class="p">, </span>content_disposition=None<span class="p">, </span>content_encoding=None<span class="p">, </span>content_length=None<span class="p">, </span>content_type=None<span class="p">, </span>copy_from=None<span class="p">, </span>date=None<span class="p">, </span>delete_after=None<span class="p">, </span>delete_at=None<span class="p">, </span>detect_content_type=None<span class="p">, </span>etag=None<span class="p">, </span>last_modified=None<span class="p">, </span>metadata=None<span class="p">, </span>name=None<span class="p">, </span>object_manifest=None<span class="p">, </span>region=None<span class="p">, </span>source=None<span class="p">, </span>trans_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetContainerObject<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/objectstorage?tab=doc#ContainerObjectState">ContainerObjectState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/objectstorage?tab=doc#ContainerObject">ContainerObject</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.ObjectStorage.ContainerObject.html">ContainerObject</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.ObjectStorage.ContainerObjectState.html">ContainerObjectState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>resource_name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

The following state arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique (within an account) name for the container. 
The container name must be from 1 to 256 characters long and can start
with any character and contain any pattern. Character set must be UTF-8.
The container name cannot contain a slash (/) character because this
character delimits the container and object name. For example, the path
/v1/account/www/pages specifies the www container, not the www/pages container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the content of the object. Conflicts with
`source` and `copy_from`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string which specifies the override behavior for 
the browser. For example, this header might specify that the browser use a download
program to save this file rather than show the file, which is the default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the value of the Content-Encoding
metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}If the operation succeeds, this value is zero (0) or the 
length of informational or error text in the response body.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string which sets the MIME type for the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Copy<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the name of an object 
used to create the new object by copying the `copy_from` object. The value is in form
{container}/{object}. You must UTF-8-encode and then URL-encode the names of the
container and object before you include them in the header. Conflicts with `source` and
`content`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date and time the system responded to the request, using the preferred 
format of RFC 7231 as shown in this example Thu, 16 Jun 2016 15:10:38 GMT. The
time is always in UTC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>After</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}An integer representing the number of seconds after which the
system removes the object. Internally, the Object Storage system stores this value in
the X-Delete-At metadata item.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An string representing the date when the system removes the object. 
For example, "2015-08-26" is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Detect<wbr>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If set to true, Object Storage guesses the content 
type based on the file extension and ignores the value sent in the Content-Type
header, if present.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. The only meaningful value is ${md5(file("path/to/file"))}.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Modified</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date and time when the object was last modified. The date and time 
stamp format is ISO 8601:
CCYY-MM-DDThh:mm:ss±hh:mm
For example, 2015-08-27T09:49:58-05:00.
The ±hh:mm value, if included, is the time zone as an offset from UTC. In the previous
example, the offset value is -05:00.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Object<wbr>Manifest</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string set to specify that this is a dynamic large 
object manifest object. The value is the container and object name prefix of the
segment objects in the form container/prefix. You must UTF-8-encode and then
URL-encode the names of the container and prefix before you include them in this
header.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to create the container. If
omitted, the `region` argument of the provider is used. Changing this
creates a new container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the local path of a file which will be used
as the object's content. Conflicts with `source` and `copy_from`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Trans<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique transaction ID for this request. Your service provider might 
need this value if you report a problem.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique (within an account) name for the container. 
The container name must be from 1 to 256 characters long and can start
with any character and contain any pattern. Character set must be UTF-8.
The container name cannot contain a slash (/) character because this
character delimits the container and object name. For example, the path
/v1/account/www/pages specifies the www container, not the www/pages container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the content of the object. Conflicts with
`source` and `copy_from`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string which specifies the override behavior for 
the browser. For example, this header might specify that the browser use a download
program to save this file rather than show the file, which is the default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the value of the Content-Encoding
metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}If the operation succeeds, this value is zero (0) or the 
length of informational or error text in the response body.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string which sets the MIME type for the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Copy<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the name of an object 
used to create the new object by copying the `copy_from` object. The value is in form
{container}/{object}. You must UTF-8-encode and then URL-encode the names of the
container and object before you include them in the header. Conflicts with `source` and
`content`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date and time the system responded to the request, using the preferred 
format of RFC 7231 as shown in this example Thu, 16 Jun 2016 15:10:38 GMT. The
time is always in UTC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>After</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}An integer representing the number of seconds after which the
system removes the object. Internally, the Object Storage system stores this value in
the X-Delete-At metadata item.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An string representing the date when the system removes the object. 
For example, "2015-08-26" is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Detect<wbr>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If set to true, Object Storage guesses the content 
type based on the file extension and ignores the value sent in the Content-Type
header, if present.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. The only meaningful value is ${md5(file("path/to/file"))}.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Modified</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date and time when the object was last modified. The date and time 
stamp format is ISO 8601:
CCYY-MM-DDThh:mm:ss±hh:mm
For example, 2015-08-27T09:49:58-05:00.
The ±hh:mm value, if included, is the time zone as an offset from UTC. In the previous
example, the offset value is -05:00.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Object<wbr>Manifest</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string set to specify that this is a dynamic large 
object manifest object. The value is the container and object name prefix of the
segment objects in the form container/prefix. You must UTF-8-encode and then
URL-encode the names of the container and prefix before you include them in this
header.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to create the container. If
omitted, the `region` argument of the provider is used. Changing this
creates a new container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the local path of a file which will be used
as the object's content. Conflicts with `source` and `copy_from`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Trans<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique transaction ID for this request. Your service provider might 
need this value if you report a problem.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique (within an account) name for the container. 
The container name must be from 1 to 256 characters long and can start
with any character and contain any pattern. Character set must be UTF-8.
The container name cannot contain a slash (/) character because this
character delimits the container and object name. For example, the path
/v1/account/www/pages specifies the www container, not the www/pages container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the content of the object. Conflicts with
`source` and `copy_from`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string which specifies the override behavior for 
the browser. For example, this header might specify that the browser use a download
program to save this file rather than show the file, which is the default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the value of the Content-Encoding
metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}If the operation succeeds, this value is zero (0) or the 
length of informational or error text in the response body.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string which sets the MIME type for the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>copy<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the name of an object 
used to create the new object by copying the `copy_from` object. The value is in form
{container}/{object}. You must UTF-8-encode and then URL-encode the names of the
container and object before you include them in the header. Conflicts with `source` and
`content`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date and time the system responded to the request, using the preferred 
format of RFC 7231 as shown in this example Thu, 16 Jun 2016 15:10:38 GMT. The
time is always in UTC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete<wbr>After</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}An integer representing the number of seconds after which the
system removes the object. Internally, the Object Storage system stores this value in
the X-Delete-At metadata item.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An string representing the date when the system removes the object. 
For example, "2015-08-26" is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>detect<wbr>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If set to true, Object Storage guesses the content 
type based on the file extension and ignores the value sent in the Content-Type
header, if present.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. The only meaningful value is ${md5(file("path/to/file"))}.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>last<wbr>Modified</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date and time when the object was last modified. The date and time 
stamp format is ISO 8601:
CCYY-MM-DDThh:mm:ss±hh:mm
For example, 2015-08-27T09:49:58-05:00.
The ±hh:mm value, if included, is the time zone as an offset from UTC. In the previous
example, the offset value is -05:00.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>object<wbr>Manifest</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string set to specify that this is a dynamic large 
object manifest object. The value is the container and object name prefix of the
segment objects in the form container/prefix. You must UTF-8-encode and then
URL-encode the names of the container and prefix before you include them in this
header.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to create the container. If
omitted, the `region` argument of the provider is used. Changing this
creates a new container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A string representing the local path of a file which will be used
as the object's content. Conflicts with `source` and `copy_from`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>trans<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique transaction ID for this request. Your service provider might 
need this value if you report a problem.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>container_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique (within an account) name for the container. 
The container name must be from 1 to 256 characters long and can start
with any character and contain any pattern. Character set must be UTF-8.
The container name cannot contain a slash (/) character because this
character delimits the container and object name. For example, the path
/v1/account/www/pages specifies the www container, not the www/pages container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A string representing the content of the object. Conflicts with
`source` and `copy_from`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A string which specifies the override behavior for 
the browser. For example, this header might specify that the browser use a download
program to save this file rather than show the file, which is the default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A string representing the value of the Content-Encoding
metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>length</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}If the operation succeeds, this value is zero (0) or the 
length of informational or error text in the response body.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A string which sets the MIME type for the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>copy_<wbr>from</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A string representing the name of an object 
used to create the new object by copying the `copy_from` object. The value is in form
{container}/{object}. You must UTF-8-encode and then URL-encode the names of the
container and object before you include them in the header. Conflicts with `source` and
`content`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>date</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The date and time the system responded to the request, using the preferred 
format of RFC 7231 as shown in this example Thu, 16 Jun 2016 15:10:38 GMT. The
time is always in UTC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete_<wbr>after</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}An integer representing the number of seconds after which the
system removes the object. Internally, the Object Storage system stores this value in
the X-Delete-At metadata item.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete_<wbr>at</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An string representing the date when the system removes the object. 
For example, "2015-08-26" is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>detect_<wbr>content_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If set to true, Object Storage guesses the content 
type based on the file extension and ignores the value sent in the Content-Type
header, if present.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. The only meaningful value is ${md5(file("path/to/file"))}.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>last_<wbr>modified</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The date and time when the object was last modified. The date and time 
stamp format is ISO 8601:
CCYY-MM-DDThh:mm:ss±hh:mm
For example, 2015-08-27T09:49:58-05:00.
The ±hh:mm value, if included, is the time zone as an offset from UTC. In the previous
example, the offset value is -05:00.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>object_<wbr>manifest</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A string set to specify that this is a dynamic large 
object manifest object. The value is the container and object name prefix of the
segment objects in the form container/prefix. You must UTF-8-encode and then
URL-encode the names of the container and prefix before you include them in this
header.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to create the container. If
omitted, the `region` argument of the provider is used. Changing this
creates a new container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A string representing the local path of a file which will be used
as the object's content. Conflicts with `source` and `copy_from`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>trans_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique transaction ID for this request. Your service provider might 
need this value if you report a problem.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-openstack">https://github.com/pulumi/pulumi-openstack</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

