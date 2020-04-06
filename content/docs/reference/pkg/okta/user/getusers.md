
---
title: "GetUsers"
block_external_search_index: true
---



Use this data source to retrieve a list of users from Okta.

> This content is derived from https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/d/users.html.markdown.





## Using GetUsers

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getUsers<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/user/#GetUsersArgs">GetUsersArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/user/#GetUsersResult">GetUsersResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_users(</span>searches=None<span class="p">, </span>users=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupUsers<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/user?tab=doc#LookupUsersArgs">LookupUsersArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/user?tab=doc#LookupUsersResult">LookupUsersResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetUsers </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.User.GetUsersResult.html">GetUsersResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.User.GetUsersArgs.html">GetUsersArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Searches</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getuserssearch">List&lt;Get<wbr>Users<wbr>Search<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Map of search criteria to use to find users. It supports the following properties.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getusersuser">List&lt;Get<wbr>Users<wbr>User<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}collection of users retrieved from Okta with the following properties.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Searches</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getuserssearch">[]Get<wbr>Users<wbr>Search</a></span>
    </dt>
    <dd>{{% md %}}Map of search criteria to use to find users. It supports the following properties.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getusersuser">[]Get<wbr>Users<wbr>User</a></span>
    </dt>
    <dd>{{% md %}}collection of users retrieved from Okta with the following properties.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>searches</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getuserssearch">Get<wbr>Users<wbr>Search[]</a></span>
    </dt>
    <dd>{{% md %}}Map of search criteria to use to find users. It supports the following properties.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>users</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getusersuser">Get<wbr>Users<wbr>User[]?</a></span>
    </dt>
    <dd>{{% md %}}collection of users retrieved from Okta with the following properties.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>searches</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getuserssearch">List[Get<wbr>Users<wbr>Search]</a></span>
    </dt>
    <dd>{{% md %}}Map of search criteria to use to find users. It supports the following properties.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>users</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getusersuser">List[Get<wbr>Users<wbr>User]</a></span>
    </dt>
    <dd>{{% md %}}collection of users retrieved from Okta with the following properties.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetUsers Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Searches</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getuserssearch">List&lt;Get<wbr>Users<wbr>Search&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getusersuser">List&lt;Get<wbr>Users<wbr>User&gt;?</a></span>
    </dt>
    <dd>{{% md %}}collection of users retrieved from Okta with the following properties.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Searches</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getuserssearch">[]Get<wbr>Users<wbr>Search</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getusersuser">[]Get<wbr>Users<wbr>User</a></span>
    </dt>
    <dd>{{% md %}}collection of users retrieved from Okta with the following properties.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>searches</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getuserssearch">Get<wbr>Users<wbr>Search[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>users</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getusersuser">Get<wbr>Users<wbr>User[]?</a></span>
    </dt>
    <dd>{{% md %}}collection of users retrieved from Okta with the following properties.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>searches</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getuserssearch">List[Get<wbr>Users<wbr>Search]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>users</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getusersuser">List[Get<wbr>Users<wbr>User]</a></span>
    </dt>
    <dd>{{% md %}}collection of users retrieved from Okta with the following properties.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Users<wbr>Search</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/input/#GetUsersSearch">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/output/#GetUsersSearch">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/user?tab=doc#GetUsersSearchArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/user?tab=doc#GetUsersSearch">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Comparison</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Comparison to use.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of property to search against.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Value to compare with.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Comparison</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Comparison to use.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of property to search against.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Value to compare with.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>comparison</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Comparison to use.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of property to search against.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Value to compare with.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>comparison</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Comparison to use.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of property to search against.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Value to compare with.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Users<wbr>User</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/input/#GetUsersUser">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/output/#GetUsersUser">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/user?tab=doc#GetUsersUserArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/user?tab=doc#GetUsersUser">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Admin<wbr>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}Administrator roles assigned to user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>City</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cost<wbr>Center</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Country<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Custom<wbr>Profile<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}raw JSON containing all custom profile attributes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Department</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Division</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Employee<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>First<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Group<wbr>Memberships</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Honorific<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Honorific<wbr>Suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Last<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Locale</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Login</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Manager</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Manager<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Middle<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Mobile<wbr>Phone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Nick<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Postal<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Preferred<wbr>Language</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Primary<wbr>Phone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Profile<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Second<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Street<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Title</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>User<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zip<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Admin<wbr>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Administrator roles assigned to user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>City</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cost<wbr>Center</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Country<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Custom<wbr>Profile<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}raw JSON containing all custom profile attributes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Department</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Division</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Employee<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>First<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Group<wbr>Memberships</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Honorific<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Honorific<wbr>Suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Last<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Locale</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Login</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Manager</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Manager<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Middle<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Mobile<wbr>Phone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Nick<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Postal<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Preferred<wbr>Language</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Primary<wbr>Phone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Profile<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Second<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Street<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Title</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>User<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zip<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>admin<wbr>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Administrator roles assigned to user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>city</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cost<wbr>Center</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>country<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>custom<wbr>Profile<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}raw JSON containing all custom profile attributes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>department</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>division</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>employee<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>first<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>group<wbr>Memberships</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>honorific<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>honorific<wbr>Suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>last<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>locale</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>login</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>manager</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>manager<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>middle<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>mobile<wbr>Phone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>nick<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>postal<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>preferred<wbr>Language</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>primary<wbr>Phone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>profile<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>second<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>street<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>title</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>user<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zip<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>admin_<wbr>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Administrator roles assigned to user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>city</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cost_<wbr>center</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>country_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>custom_<wbr>profile_<wbr>attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}raw JSON containing all custom profile attributes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>department</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>division</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>employee_<wbr>number</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>first_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>group_<wbr>memberships</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>honorific_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>honorific_<wbr>suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>last_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>locale</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>login</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>manager</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>manager_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>middle_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>mobile_<wbr>phone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>nick_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>postal_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>preferred_<wbr>language</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>primary_<wbr>phone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>profile_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>second_<wbr>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>street_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>title</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>user_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zip_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}user profile property.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







