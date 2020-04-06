
---
title: "ApplicationCredential"
block_external_search_index: true
---



Manages a V3 Application Credential resource within OpenStack Keystone.

> **Note:** All arguments including the application credential name and secret
will be stored in the raw state as plain-text. [Read more about sensitive data
in state](https://www.terraform.io/docs/state/sensitive-data.html).

> **Note:** An Application Credential is created within the authenticated user
project scope and is not visible by an admin or other accounts.
The Application Credential visibility is similar to
`openstack.compute.Keypair`.

> This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_application_credential_v3.html.markdown.



## Create a ApplicationCredential Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/identity/#ApplicationCredential">ApplicationCredential</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/identity/#ApplicationCredentialArgs">ApplicationCredentialArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">ApplicationCredential</span><span class="p">(resource_name, opts=None, </span>access_rules=None<span class="p">, </span>description=None<span class="p">, </span>expires_at=None<span class="p">, </span>name=None<span class="p">, </span>region=None<span class="p">, </span>roles=None<span class="p">, </span>secret=None<span class="p">, </span>unrestricted=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewApplicationCredential<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/identity?tab=doc#ApplicationCredentialArgs">ApplicationCredentialArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/identity?tab=doc#ApplicationCredential">ApplicationCredential</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Identity.ApplicationCredential.html">ApplicationCredential</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Identity.ApplicationCredentialArgs.html">ApplicationCredentialArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Access<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationcredentialaccessrule">List&lt;Application<wbr>Credential<wbr>Access<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A collection of one or more access rules, which
this application credential allows to follow. The structure is described
below. Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A description of the application credential.
Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expires<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The expiration time of the application credential
in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
an application credential will never expire. Changing this creates a new
application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A name of the application credential. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A collection of one or more role names, which this
application credential has to be associated with its project. If omitted,
all the current user's roles within the scoped project will be inherited by
a new application credential. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The secret for the application credential. If omitted,
it will be generated by the server. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unrestricted</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}A flag indicating whether the application
credential may be used for creation or destruction of other application
credentials or trusts. Changing this creates a new application credential.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Access<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationcredentialaccessrule">[]Application<wbr>Credential<wbr>Access<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A collection of one or more access rules, which
this application credential allows to follow. The structure is described
below. Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A description of the application credential.
Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expires<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The expiration time of the application credential
in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
an application credential will never expire. Changing this creates a new
application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A name of the application credential. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A collection of one or more role names, which this
application credential has to be associated with its project. If omitted,
all the current user's roles within the scoped project will be inherited by
a new application credential. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The secret for the application credential. If omitted,
it will be generated by the server. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unrestricted</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}A flag indicating whether the application
credential may be used for creation or destruction of other application
credentials or trusts. Changing this creates a new application credential.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationcredentialaccessrule">Application<wbr>Credential<wbr>Access<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}A collection of one or more access rules, which
this application credential allows to follow. The structure is described
below. Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A description of the application credential.
Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expires<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The expiration time of the application credential
in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
an application credential will never expire. Changing this creates a new
application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A name of the application credential. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A collection of one or more role names, which this
application credential has to be associated with its project. If omitted,
all the current user's roles within the scoped project will be inherited by
a new application credential. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The secret for the application credential. If omitted,
it will be generated by the server. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unrestricted</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}A flag indicating whether the application
credential may be used for creation or destruction of other application
credentials or trusts. Changing this creates a new application credential.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationcredentialaccessrule">List[Application<wbr>Credential<wbr>Access<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A collection of one or more access rules, which
this application credential allows to follow. The structure is described
below. Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A description of the application credential.
Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expires_<wbr>at</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The expiration time of the application credential
in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
an application credential will never expire. Changing this creates a new
application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A name of the application credential. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A collection of one or more role names, which this
application credential has to be associated with its project. If omitted,
all the current user's roles within the scoped project will be inherited by
a new application credential. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The secret for the application credential. If omitted,
it will be generated by the server. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unrestricted</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}A flag indicating whether the application
credential may be used for creation or destruction of other application
credentials or trusts. Changing this creates a new application credential.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## ApplicationCredential Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Access<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationcredentialaccessrule">List&lt;Application<wbr>Credential<wbr>Access<wbr>Rule&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A collection of one or more access rules, which
this application credential allows to follow. The structure is described
below. Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A description of the application credential.
Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expires<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The expiration time of the application credential
in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
an application credential will never expire. Changing this creates a new
application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name of the application credential. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project the application credential was created
for and that authentication requests using this application credential will
be scoped to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A collection of one or more role names, which this
application credential has to be associated with its project. If omitted,
all the current user's roles within the scoped project will be inherited by
a new application credential. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secret for the application credential. If omitted,
it will be generated by the server. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Unrestricted</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}A flag indicating whether the application
credential may be used for creation or destruction of other application
credentials or trusts. Changing this creates a new application credential.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Access<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationcredentialaccessrule">[]Application<wbr>Credential<wbr>Access<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A collection of one or more access rules, which
this application credential allows to follow. The structure is described
below. Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A description of the application credential.
Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expires<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The expiration time of the application credential
in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
an application credential will never expire. Changing this creates a new
application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name of the application credential. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project the application credential was created
for and that authentication requests using this application credential will
be scoped to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A collection of one or more role names, which this
application credential has to be associated with its project. If omitted,
all the current user's roles within the scoped project will be inherited by
a new application credential. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secret for the application credential. If omitted,
it will be generated by the server. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Unrestricted</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}A flag indicating whether the application
credential may be used for creation or destruction of other application
credentials or trusts. Changing this creates a new application credential.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>access<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationcredentialaccessrule">Application<wbr>Credential<wbr>Access<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}A collection of one or more access rules, which
this application credential allows to follow. The structure is described
below. Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A description of the application credential.
Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expires<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The expiration time of the application credential
in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
an application credential will never expire. Changing this creates a new
application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name of the application credential. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project the application credential was created
for and that authentication requests using this application credential will
be scoped to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A collection of one or more role names, which this
application credential has to be associated with its project. If omitted,
all the current user's roles within the scoped project will be inherited by
a new application credential. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secret for the application credential. If omitted,
it will be generated by the server. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>unrestricted</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}A flag indicating whether the application
credential may be used for creation or destruction of other application
credentials or trusts. Changing this creates a new application credential.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>access_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationcredentialaccessrule">List[Application<wbr>Credential<wbr>Access<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A collection of one or more access rules, which
this application credential allows to follow. The structure is described
below. Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A description of the application credential.
Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expires_<wbr>at</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The expiration time of the application credential
in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
an application credential will never expire. Changing this creates a new
application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A name of the application credential. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project the application credential was created
for and that authentication requests using this application credential will
be scoped to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A collection of one or more role names, which this
application credential has to be associated with its project. If omitted,
all the current user's roles within the scoped project will be inherited by
a new application credential. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The secret for the application credential. If omitted,
it will be generated by the server. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>unrestricted</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}A flag indicating whether the application
credential may be used for creation or destruction of other application
credentials or trusts. Changing this creates a new application credential.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing ApplicationCredential Resource

Get an existing ApplicationCredential resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/identity/#ApplicationCredentialState">ApplicationCredentialState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/identity/#ApplicationCredential">ApplicationCredential</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>access_rules=None<span class="p">, </span>description=None<span class="p">, </span>expires_at=None<span class="p">, </span>name=None<span class="p">, </span>project_id=None<span class="p">, </span>region=None<span class="p">, </span>roles=None<span class="p">, </span>secret=None<span class="p">, </span>unrestricted=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetApplicationCredential<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/identity?tab=doc#ApplicationCredentialState">ApplicationCredentialState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/identity?tab=doc#ApplicationCredential">ApplicationCredential</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Identity.ApplicationCredential.html">ApplicationCredential</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Identity.ApplicationCredentialState.html">ApplicationCredentialState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Access<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationcredentialaccessrule">List&lt;Application<wbr>Credential<wbr>Access<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A collection of one or more access rules, which
this application credential allows to follow. The structure is described
below. Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A description of the application credential.
Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expires<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The expiration time of the application credential
in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
an application credential will never expire. Changing this creates a new
application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A name of the application credential. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project the application credential was created
for and that authentication requests using this application credential will
be scoped to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A collection of one or more role names, which this
application credential has to be associated with its project. If omitted,
all the current user's roles within the scoped project will be inherited by
a new application credential. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The secret for the application credential. If omitted,
it will be generated by the server. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unrestricted</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}A flag indicating whether the application
credential may be used for creation or destruction of other application
credentials or trusts. Changing this creates a new application credential.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Access<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationcredentialaccessrule">[]Application<wbr>Credential<wbr>Access<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A collection of one or more access rules, which
this application credential allows to follow. The structure is described
below. Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A description of the application credential.
Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expires<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The expiration time of the application credential
in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
an application credential will never expire. Changing this creates a new
application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A name of the application credential. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project the application credential was created
for and that authentication requests using this application credential will
be scoped to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A collection of one or more role names, which this
application credential has to be associated with its project. If omitted,
all the current user's roles within the scoped project will be inherited by
a new application credential. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The secret for the application credential. If omitted,
it will be generated by the server. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unrestricted</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}A flag indicating whether the application
credential may be used for creation or destruction of other application
credentials or trusts. Changing this creates a new application credential.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationcredentialaccessrule">Application<wbr>Credential<wbr>Access<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}A collection of one or more access rules, which
this application credential allows to follow. The structure is described
below. Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A description of the application credential.
Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expires<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The expiration time of the application credential
in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
an application credential will never expire. Changing this creates a new
application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A name of the application credential. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project the application credential was created
for and that authentication requests using this application credential will
be scoped to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A collection of one or more role names, which this
application credential has to be associated with its project. If omitted,
all the current user's roles within the scoped project will be inherited by
a new application credential. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The secret for the application credential. If omitted,
it will be generated by the server. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unrestricted</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}A flag indicating whether the application
credential may be used for creation or destruction of other application
credentials or trusts. Changing this creates a new application credential.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationcredentialaccessrule">List[Application<wbr>Credential<wbr>Access<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A collection of one or more access rules, which
this application credential allows to follow. The structure is described
below. Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A description of the application credential.
Changing this creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expires_<wbr>at</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The expiration time of the application credential
in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
an application credential will never expire. Changing this creates a new
application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A name of the application credential. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project the application credential was created
for and that authentication requests using this application credential will
be scoped to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new application credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A collection of one or more role names, which this
application credential has to be associated with its project. If omitted,
all the current user's roles within the scoped project will be inherited by
a new application credential. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The secret for the application credential. If omitted,
it will be generated by the server. Changing this creates a new application
credential.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unrestricted</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}A flag indicating whether the application
credential may be used for creation or destruction of other application
credentials or trusts. Changing this creates a new application credential.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Application<wbr>Credential<wbr>Access<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/input/#ApplicationCredentialAccessRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/output/#ApplicationCredentialAccessRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/identity?tab=doc#ApplicationCredentialAccessRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/identity?tab=doc#ApplicationCredentialAccessRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the existing access rule. The access rule ID of
another application credential can be provided.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The request method that the application credential is
permitted to use for a given API endpoint. Allowed values: `POST`, `GET`,
`HEAD`, `PATCH`, `PUT` and `DELETE`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The API path that the application credential is permitted
to access. May use named wildcards such as **{tag}** or the unnamed wildcard
**\*** to match against any string in the path up to a **/**, or the recursive
wildcard **\*\*** to include **/** in the matched path.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The service type identifier for the service that the
application credential is granted to access. Must be a service type that is
listed in the service catalog and not a code name for a service. E.g.
**identity**, **compute**, **volumev3**, **image**, **network**,
**object-store**, **sharev2**, **dns**, **key-manager**, **monitoring**, etc.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the existing access rule. The access rule ID of
another application credential can be provided.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The request method that the application credential is
permitted to use for a given API endpoint. Allowed values: `POST`, `GET`,
`HEAD`, `PATCH`, `PUT` and `DELETE`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The API path that the application credential is permitted
to access. May use named wildcards such as **{tag}** or the unnamed wildcard
**\*** to match against any string in the path up to a **/**, or the recursive
wildcard **\*\*** to include **/** in the matched path.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The service type identifier for the service that the
application credential is granted to access. Must be a service type that is
listed in the service catalog and not a code name for a service. E.g.
**identity**, **compute**, **volumev3**, **image**, **network**,
**object-store**, **sharev2**, **dns**, **key-manager**, **monitoring**, etc.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the existing access rule. The access rule ID of
another application credential can be provided.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The request method that the application credential is
permitted to use for a given API endpoint. Allowed values: `POST`, `GET`,
`HEAD`, `PATCH`, `PUT` and `DELETE`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The API path that the application credential is permitted
to access. May use named wildcards such as **{tag}** or the unnamed wildcard
**\*** to match against any string in the path up to a **/**, or the recursive
wildcard **\*\*** to include **/** in the matched path.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The service type identifier for the service that the
application credential is granted to access. Must be a service type that is
listed in the service catalog and not a code name for a service. E.g.
**identity**, **compute**, **volumev3**, **image**, **network**,
**object-store**, **sharev2**, **dns**, **key-manager**, **monitoring**, etc.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the existing access rule. The access rule ID of
another application credential can be provided.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>method</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The request method that the application credential is
permitted to use for a given API endpoint. Allowed values: `POST`, `GET`,
`HEAD`, `PATCH`, `PUT` and `DELETE`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The API path that the application credential is permitted
to access. May use named wildcards such as **{tag}** or the unnamed wildcard
**\*** to match against any string in the path up to a **/**, or the recursive
wildcard **\*\*** to include **/** in the matched path.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The service type identifier for the service that the
application credential is granted to access. Must be a service type that is
listed in the service catalog and not a code name for a service. E.g.
**identity**, **compute**, **volumev3**, **image**, **network**,
**object-store**, **sharev2**, **dns**, **key-manager**, **monitoring**, etc.
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

