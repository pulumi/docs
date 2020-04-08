
---
title: "AuthConfigOkta"
block_external_search_index: true
---



Provides a Rancher v2 Auth Config OKTA resource. This can be used to configure and enable Auth Config OKTA for Rancher v2 RKE clusters and retrieve their information.

In addition to the built-in local auth, only one external auth config provider can be enabled at a time.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as rancher2 from "@pulumi/rancher2";

// Create a new rancher2 Auth Config OKTA
const okta = new rancher2.AuthConfigOkta("okta", {
    displayNameField: "<DISPLAY_NAME_FIELD>",
    groupsField: "<GROUPS_FIELD>",
    idpMetadataContent: "<IDP_METADATA_CONTENT>",
    rancherApiHost: "https://<RANCHER_API_HOST>",
    spCert: "<SP_CERT>",
    spKey: "<SP_KEY>",
    uidField: "<UID_FIELD>",
    userNameField: "<USER_NAME_FIELD>",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-rancher2/blob/master/website/docs/r/authConfigOKTA.html.markdown.



## Create a AuthConfigOkta Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/rancher2/#AuthConfigOkta">AuthConfigOkta</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/rancher2/#AuthConfigOktaArgs">AuthConfigOktaArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">AuthConfigOkta</span><span class="p">(resource_name, opts=None, </span>access_mode=None<span class="p">, </span>allowed_principal_ids=None<span class="p">, </span>annotations=None<span class="p">, </span>display_name_field=None<span class="p">, </span>enabled=None<span class="p">, </span>groups_field=None<span class="p">, </span>idp_metadata_content=None<span class="p">, </span>labels=None<span class="p">, </span>rancher_api_host=None<span class="p">, </span>sp_cert=None<span class="p">, </span>sp_key=None<span class="p">, </span>uid_field=None<span class="p">, </span>user_name_field=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewAuthConfigOkta<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#AuthConfigOktaArgs">AuthConfigOktaArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#AuthConfigOkta">AuthConfigOkta</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Rancher2/Pulumi.Rancher2..AuthConfigOkta.html">AuthConfigOkta</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Rancher2/Pulumi.Rancher2.AuthConfigOktaArgs.html">AuthConfigOktaArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-optional"
            title="Optional">
        <span>Access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Access mode for auth. `required`, `restricted`, `unrestricted` are supported. Default `unrestricted` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Principal<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Allowed principal ids for auth. Required if `access_mode` is `required` or `restricted`. Ex: `okta_user://<USER_ID>`  `okta_group://<GROUP_ID>` (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Annotations of the resource (map)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Display<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA display name field (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable auth config provider. Default `true` (bool)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Groups<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA group field (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Idp<wbr>Metadata<wbr>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA IDP metadata content (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Labels of the resource (map)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rancher<wbr>Api<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Rancher url. Schema needs to be specified, `https://<RANCHER_API_HOST>` (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sp<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA SP cert (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sp<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA SP key (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Uid<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA UID field (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>User<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA user name field (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Access mode for auth. `required`, `restricted`, `unrestricted` are supported. Default `unrestricted` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Principal<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Allowed principal ids for auth. Required if `access_mode` is `required` or `restricted`. Ex: `okta_user://<USER_ID>`  `okta_group://<GROUP_ID>` (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Annotations of the resource (map)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Display<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA display name field (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable auth config provider. Default `true` (bool)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Groups<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA group field (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Idp<wbr>Metadata<wbr>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA IDP metadata content (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Labels of the resource (map)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rancher<wbr>Api<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Rancher url. Schema needs to be specified, `https://<RANCHER_API_HOST>` (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sp<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA SP cert (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sp<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA SP key (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Uid<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA UID field (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>User<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA user name field (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Access mode for auth. `required`, `restricted`, `unrestricted` are supported. Default `unrestricted` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed<wbr>Principal<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Allowed principal ids for auth. Required if `access_mode` is `required` or `restricted`. Ex: `okta_user://<USER_ID>`  `okta_group://<GROUP_ID>` (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Annotations of the resource (map)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>display<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA display name field (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable auth config provider. Default `true` (bool)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>groups<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA group field (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>idp<wbr>Metadata<wbr>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA IDP metadata content (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Labels of the resource (map)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rancher<wbr>Api<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Rancher url. Schema needs to be specified, `https://<RANCHER_API_HOST>` (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sp<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA SP cert (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sp<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA SP key (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>uid<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA UID field (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>user<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA user name field (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Access mode for auth. `required`, `restricted`, `unrestricted` are supported. Default `unrestricted` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed_<wbr>principal_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Allowed principal ids for auth. Required if `access_mode` is `required` or `restricted`. Ex: `okta_user://<USER_ID>`  `okta_group://<GROUP_ID>` (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Annotations of the resource (map)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>display_<wbr>name_<wbr>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA display name field (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable auth config provider. Default `true` (bool)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>groups_<wbr>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA group field (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>idp_<wbr>metadata_<wbr>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA IDP metadata content (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Labels of the resource (map)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rancher_<wbr>api_<wbr>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Rancher url. Schema needs to be specified, `https://<RANCHER_API_HOST>` (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sp_<wbr>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA SP cert (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sp_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA SP key (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>uid_<wbr>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA UID field (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>user_<wbr>name_<wbr>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA user name field (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## AuthConfigOkta Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Access mode for auth. `required`, `restricted`, `unrestricted` are supported. Default `unrestricted` (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allowed<wbr>Principal<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Allowed principal ids for auth. Required if `access_mode` is `required` or `restricted`. Ex: `okta_user://<USER_ID>`  `okta_group://<GROUP_ID>` (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object></span>
    </dt>
    <dd>{{% md %}}Annotations of the resource (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Display<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA display name field (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable auth config provider. Default `true` (bool)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Groups<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA group field (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Idp<wbr>Metadata<wbr>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA IDP metadata content (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object></span>
    </dt>
    <dd>{{% md %}}Labels of the resource (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The name of the resource (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Rancher<wbr>Api<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Rancher url. Schema needs to be specified, `https://<RANCHER_API_HOST>` (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sp<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA SP cert (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sp<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA SP key (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The type of the resource (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Uid<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA UID field (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA user name field (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Access mode for auth. `required`, `restricted`, `unrestricted` are supported. Default `unrestricted` (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allowed<wbr>Principal<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Allowed principal ids for auth. Required if `access_mode` is `required` or `restricted`. Ex: `okta_user://<USER_ID>`  `okta_group://<GROUP_ID>` (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Annotations of the resource (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Display<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA display name field (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable auth config provider. Default `true` (bool)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Groups<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA group field (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Idp<wbr>Metadata<wbr>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA IDP metadata content (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Labels of the resource (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The name of the resource (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Rancher<wbr>Api<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Rancher url. Schema needs to be specified, `https://<RANCHER_API_HOST>` (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sp<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA SP cert (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sp<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA SP key (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The type of the resource (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Uid<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA UID field (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA user name field (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Access mode for auth. `required`, `restricted`, `unrestricted` are supported. Default `unrestricted` (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allowed<wbr>Principal<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Allowed principal ids for auth. Required if `access_mode` is `required` or `restricted`. Ex: `okta_user://<USER_ID>`  `okta_group://<GROUP_ID>` (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}Annotations of the resource (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>display<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA display name field (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable auth config provider. Default `true` (bool)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>groups<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA group field (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>idp<wbr>Metadata<wbr>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA IDP metadata content (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}Labels of the resource (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The name of the resource (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>rancher<wbr>Api<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Rancher url. Schema needs to be specified, `https://<RANCHER_API_HOST>` (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sp<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA SP cert (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sp<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA SP key (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The type of the resource (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>uid<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA UID field (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}OKTA user name field (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>access_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Access mode for auth. `required`, `restricted`, `unrestricted` are supported. Default `unrestricted` (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allowed_<wbr>principal_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Allowed principal ids for auth. Required if `access_mode` is `required` or `restricted`. Ex: `okta_user://<USER_ID>`  `okta_group://<GROUP_ID>` (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Annotations of the resource (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>display_<wbr>name_<wbr>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA display name field (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable auth config provider. Default `true` (bool)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>groups_<wbr>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA group field (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>idp_<wbr>metadata_<wbr>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA IDP metadata content (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Labels of the resource (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(Computed) The name of the resource (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>rancher_<wbr>api_<wbr>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Rancher url. Schema needs to be specified, `https://<RANCHER_API_HOST>` (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sp_<wbr>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA SP cert (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sp_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA SP key (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(Computed) The type of the resource (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>uid_<wbr>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA UID field (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user_<wbr>name_<wbr>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA user name field (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing AuthConfigOkta Resource

Get an existing AuthConfigOkta resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/rancher2/#AuthConfigOktaState">AuthConfigOktaState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/rancher2/#AuthConfigOkta">AuthConfigOkta</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>access_mode=None<span class="p">, </span>allowed_principal_ids=None<span class="p">, </span>annotations=None<span class="p">, </span>display_name_field=None<span class="p">, </span>enabled=None<span class="p">, </span>groups_field=None<span class="p">, </span>idp_metadata_content=None<span class="p">, </span>labels=None<span class="p">, </span>name=None<span class="p">, </span>rancher_api_host=None<span class="p">, </span>sp_cert=None<span class="p">, </span>sp_key=None<span class="p">, </span>type=None<span class="p">, </span>uid_field=None<span class="p">, </span>user_name_field=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetAuthConfigOkta<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#AuthConfigOktaState">AuthConfigOktaState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#AuthConfigOkta">AuthConfigOkta</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Rancher2/Pulumi.Rancher2..AuthConfigOkta.html">AuthConfigOkta</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Rancher2/Pulumi.Rancher2..AuthConfigOktaState.html">AuthConfigOktaState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Access mode for auth. `required`, `restricted`, `unrestricted` are supported. Default `unrestricted` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Principal<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Allowed principal ids for auth. Required if `access_mode` is `required` or `restricted`. Ex: `okta_user://<USER_ID>`  `okta_group://<GROUP_ID>` (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Annotations of the resource (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}OKTA display name field (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable auth config provider. Default `true` (bool)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Groups<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}OKTA group field (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Idp<wbr>Metadata<wbr>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}OKTA IDP metadata content (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Labels of the resource (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(Computed) The name of the resource (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rancher<wbr>Api<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Rancher url. Schema needs to be specified, `https://<RANCHER_API_HOST>` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sp<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}OKTA SP cert (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sp<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}OKTA SP key (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(Computed) The type of the resource (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uid<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}OKTA UID field (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}OKTA user name field (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Access mode for auth. `required`, `restricted`, `unrestricted` are supported. Default `unrestricted` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Principal<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Allowed principal ids for auth. Required if `access_mode` is `required` or `restricted`. Ex: `okta_user://<USER_ID>`  `okta_group://<GROUP_ID>` (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Annotations of the resource (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}OKTA display name field (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable auth config provider. Default `true` (bool)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Groups<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}OKTA group field (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Idp<wbr>Metadata<wbr>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}OKTA IDP metadata content (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Labels of the resource (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}(Computed) The name of the resource (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rancher<wbr>Api<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Rancher url. Schema needs to be specified, `https://<RANCHER_API_HOST>` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sp<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}OKTA SP cert (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sp<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}OKTA SP key (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}(Computed) The type of the resource (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uid<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}OKTA UID field (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}OKTA user name field (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Access mode for auth. `required`, `restricted`, `unrestricted` are supported. Default `unrestricted` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed<wbr>Principal<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Allowed principal ids for auth. Required if `access_mode` is `required` or `restricted`. Ex: `okta_user://<USER_ID>`  `okta_group://<GROUP_ID>` (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Annotations of the resource (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}OKTA display name field (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable auth config provider. Default `true` (bool)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>groups<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}OKTA group field (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>idp<wbr>Metadata<wbr>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}OKTA IDP metadata content (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Labels of the resource (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(Computed) The name of the resource (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rancher<wbr>Api<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Rancher url. Schema needs to be specified, `https://<RANCHER_API_HOST>` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sp<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}OKTA SP cert (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sp<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}OKTA SP key (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(Computed) The type of the resource (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uid<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}OKTA UID field (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user<wbr>Name<wbr>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}OKTA user name field (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Access mode for auth. `required`, `restricted`, `unrestricted` are supported. Default `unrestricted` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed_<wbr>principal_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Allowed principal ids for auth. Required if `access_mode` is `required` or `restricted`. Ex: `okta_user://<USER_ID>`  `okta_group://<GROUP_ID>` (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Annotations of the resource (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display_<wbr>name_<wbr>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA display name field (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable auth config provider. Default `true` (bool)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>groups_<wbr>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA group field (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>idp_<wbr>metadata_<wbr>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA IDP metadata content (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Labels of the resource (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(Computed) The name of the resource (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rancher_<wbr>api_<wbr>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Rancher url. Schema needs to be specified, `https://<RANCHER_API_HOST>` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sp_<wbr>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA SP cert (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sp_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA SP key (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(Computed) The type of the resource (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uid_<wbr>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA UID field (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user_<wbr>name_<wbr>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}OKTA user name field (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-rancher2">https://github.com/pulumi/pulumi-rancher2</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

