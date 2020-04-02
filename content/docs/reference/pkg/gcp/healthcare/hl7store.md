
---
title: "Hl7Store"
block_external_search_index: true
---

A Hl7V2Store is a datastore inside a Healthcare dataset that conforms to the FHIR (https://www.hl7.org/hl7V2/STU3/)
standard for Healthcare information exchange

To get more information about Hl7V2Store, see:

* [API documentation](https://cloud.google.com/healthcare/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores)
* How-to Guides
    * [Creating a HL7v2 Store](https://cloud.google.com/healthcare/docs/how-tos/hl7v2)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/healthcare_hl7_v2_store.html.markdown.



## Create a Hl7Store Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/healthcare/#Hl7Store">Hl7Store</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/healthcare/#Hl7StoreArgs">Hl7StoreArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Hl7Store</span><span class="p">(resource_name, opts=None, </span>dataset=None<span class="p">, </span>labels=None<span class="p">, </span>name=None<span class="p">, </span>notification_config=None<span class="p">, </span>parser_config=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewHl7Store<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/healthcare?tab=doc#Hl7StoreArgs">Hl7StoreArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/healthcare?tab=doc#Hl7Store">Hl7Store</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Healthcare.Hl7Store.html">Hl7Store</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Healthcare.Hl7StoreArgs.html">Hl7StoreArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Dataset</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Identifies the dataset addressed by this request. Must be in the format
'projects/{project}/locations/{location}/datasets/{dataset}'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62} Label values are optional, must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. An object containing a list of
"key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The resource name for the Hl7V2Store. ** Changing this property may recreate the Hl7v2 store (removing all data) **
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storenotificationconfig">Hl7Store<wbr>Notification<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parser<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storeparserconfig">Hl7Store<wbr>Parser<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dataset</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Identifies the dataset addressed by this request. Must be in the format
'projects/{project}/locations/{location}/datasets/{dataset}'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62} Label values are optional, must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. An object containing a list of
"key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The resource name for the Hl7V2Store. ** Changing this property may recreate the Hl7v2 store (removing all data) **
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storenotificationconfig">*Hl7Store<wbr>Notification<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parser<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storeparserconfig">*Hl7Store<wbr>Parser<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dataset</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Identifies the dataset addressed by this request. Must be in the format
'projects/{project}/locations/{location}/datasets/{dataset}'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62} Label values are optional, must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. An object containing a list of
"key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The resource name for the Hl7V2Store. ** Changing this property may recreate the Hl7v2 store (removing all data) **
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storenotificationconfig">Hl7Store<wbr>Notification<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parser<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storeparserconfig">Hl7Store<wbr>Parser<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dataset</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Identifies the dataset addressed by this request. Must be in the format
'projects/{project}/locations/{location}/datasets/{dataset}'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62} Label values are optional, must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. An object containing a list of
"key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The resource name for the Hl7V2Store. ** Changing this property may recreate the Hl7v2 store (removing all data) **
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notification_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storenotificationconfig">Dict[Hl7Store<wbr>Notification<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parser_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storeparserconfig">Dict[Hl7Store<wbr>Parser<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Hl7Store Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Dataset</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Identifies the dataset addressed by this request. Must be in the format
'projects/{project}/locations/{location}/datasets/{dataset}'
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62} Label values are optional, must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. An object containing a list of
"key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The resource name for the Hl7V2Store. ** Changing this property may recreate the Hl7v2 store (removing all data) **
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storenotificationconfig">Hl7Store<wbr>Notification<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Parser<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storeparserconfig">Hl7Store<wbr>Parser<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The fully qualified name of this dataset
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Dataset</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Identifies the dataset addressed by this request. Must be in the format
'projects/{project}/locations/{location}/datasets/{dataset}'
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62} Label values are optional, must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. An object containing a list of
"key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The resource name for the Hl7V2Store. ** Changing this property may recreate the Hl7v2 store (removing all data) **
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storenotificationconfig">*Hl7Store<wbr>Notification<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Parser<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storeparserconfig">*Hl7Store<wbr>Parser<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The fully qualified name of this dataset
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>dataset</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Identifies the dataset addressed by this request. Must be in the format
'projects/{project}/locations/{location}/datasets/{dataset}'
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62} Label values are optional, must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. An object containing a list of
"key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The resource name for the Hl7V2Store. ** Changing this property may recreate the Hl7v2 store (removing all data) **
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storenotificationconfig">Hl7Store<wbr>Notification<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>parser<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storeparserconfig">Hl7Store<wbr>Parser<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The fully qualified name of this dataset
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>dataset</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Identifies the dataset addressed by this request. Must be in the format
'projects/{project}/locations/{location}/datasets/{dataset}'
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62} Label values are optional, must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. An object containing a list of
"key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The resource name for the Hl7V2Store. ** Changing this property may recreate the Hl7v2 store (removing all data) **
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>notification_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storenotificationconfig">Dict[Hl7Store<wbr>Notification<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>parser_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storeparserconfig">Dict[Hl7Store<wbr>Parser<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The fully qualified name of this dataset
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Hl7Store Resource

Get an existing Hl7Store resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/healthcare/#Hl7StoreState">Hl7StoreState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/healthcare/#Hl7Store">Hl7Store</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>dataset=None<span class="p">, </span>labels=None<span class="p">, </span>name=None<span class="p">, </span>notification_config=None<span class="p">, </span>parser_config=None<span class="p">, </span>self_link=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetHl7Store<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/healthcare?tab=doc#Hl7StoreState">Hl7StoreState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/healthcare?tab=doc#Hl7Store">Hl7Store</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Healthcare.Hl7Store.html">Hl7Store</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Healthcare.Hl7StoreState.html">Hl7StoreState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Dataset</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Identifies the dataset addressed by this request. Must be in the format
'projects/{project}/locations/{location}/datasets/{dataset}'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62} Label values are optional, must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. An object containing a list of
"key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The resource name for the Hl7V2Store. ** Changing this property may recreate the Hl7v2 store (removing all data) **
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storenotificationconfig">Hl7Store<wbr>Notification<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parser<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storeparserconfig">Hl7Store<wbr>Parser<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The fully qualified name of this dataset
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Dataset</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Identifies the dataset addressed by this request. Must be in the format
'projects/{project}/locations/{location}/datasets/{dataset}'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62} Label values are optional, must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. An object containing a list of
"key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The resource name for the Hl7V2Store. ** Changing this property may recreate the Hl7v2 store (removing all data) **
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storenotificationconfig">*Hl7Store<wbr>Notification<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parser<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storeparserconfig">*Hl7Store<wbr>Parser<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The fully qualified name of this dataset
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dataset</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Identifies the dataset addressed by this request. Must be in the format
'projects/{project}/locations/{location}/datasets/{dataset}'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62} Label values are optional, must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. An object containing a list of
"key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The resource name for the Hl7V2Store. ** Changing this property may recreate the Hl7v2 store (removing all data) **
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storenotificationconfig">Hl7Store<wbr>Notification<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parser<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storeparserconfig">Hl7Store<wbr>Parser<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The fully qualified name of this dataset
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dataset</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Identifies the dataset addressed by this request. Must be in the format
'projects/{project}/locations/{location}/datasets/{dataset}'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62} Label values are optional, must be between 1 and 63 characters long, have a
UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression:
[\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. An object containing a list of
"key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The resource name for the Hl7V2Store. ** Changing this property may recreate the Hl7v2 store (removing all data) **
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notification_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storenotificationconfig">Dict[Hl7Store<wbr>Notification<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parser_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#hl7storeparserconfig">Dict[Hl7Store<wbr>Parser<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A nested object resource
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The fully qualified name of this dataset
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Hl7Store<wbr>Notification<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#Hl7StoreNotificationConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#Hl7StoreNotificationConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/healthcare?tab=doc#Hl7StoreNotificationConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/healthcare?tab=doc#Hl7StoreNotificationConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Pubsub<wbr>Topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Pubsub<wbr>Topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>pubsub<wbr>Topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>pubsub<wbr>Topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Hl7Store<wbr>Parser<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#Hl7StoreParserConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#Hl7StoreParserConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/healthcare?tab=doc#Hl7StoreParserConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/healthcare?tab=doc#Hl7StoreParserConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Null<wbr>Header</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Segment<wbr>Terminator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Null<wbr>Header</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Segment<wbr>Terminator</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Null<wbr>Header</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>segment<wbr>Terminator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Null<wbr>Header</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>segment<wbr>Terminator</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
