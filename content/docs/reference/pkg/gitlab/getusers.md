
---
title: "GetUsers"
block_external_search_index: true
---



Provides details about a list of users in the gitlab provider. The results include id, username, email, name and more about the requested users. Users can also be sorted and filtered using several options.

**NOTE**: Some of the available options require administrator privileges. Please visit [Gitlab API documentation][users_for_admins] for more information.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gitlab from "@pulumi/gitlab";

const example = pulumi.output(gitlab.getUsers({
    createdBefore: "2019-01-01",
    orderBy: "name",
    sort: "desc",
}, { async: true }));
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/d/users.html.markdown.





## Using GetUsers

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getUsers<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gitlab/#GetUsersArgs">GetUsersArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gitlab/#GetUsersResult">GetUsersResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_users(</span>active=None<span class="p">, </span>blocked=None<span class="p">, </span>created_after=None<span class="p">, </span>created_before=None<span class="p">, </span>extern_provider=None<span class="p">, </span>extern_uid=None<span class="p">, </span>order_by=None<span class="p">, </span>search=None<span class="p">, </span>sort=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupUsers<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gitlab/sdk/go/gitlab/?tab=doc#GetUsersArgs">GetUsersArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gitlab/sdk/go/gitlab/?tab=doc#LookupUsersResult">LookupUsersResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetUsers </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gitlab/Pulumi.Gitlab.GetUsersResult.html">GetUsersResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gitlab/Pulumi.Gitlab.GetUsersArgs.html">GetUsersArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Filter users that are active.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Blocked</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Filter users that are blocked.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Created<wbr>After</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Search for users created after a specific date. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Created<wbr>Before</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Search for users created before a specific date. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Extern<wbr>Provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Lookup users by external provider. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Extern<wbr>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Lookup users by external UID. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Order<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Order the users' list by `id`, `name`, `username`, `created_at` or `updated_at`. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Search</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Search users by username, name or email.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sort</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Sort users' list in asc or desc order. (Requires administrator privileges)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Filter users that are active.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Blocked</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Filter users that are blocked.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Created<wbr>After</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Search for users created after a specific date. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Created<wbr>Before</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Search for users created before a specific date. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Extern<wbr>Provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Lookup users by external provider. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Extern<wbr>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Lookup users by external UID. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Order<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Order the users' list by `id`, `name`, `username`, `created_at` or `updated_at`. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Search</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Search users by username, name or email.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sort</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Sort users' list in asc or desc order. (Requires administrator privileges)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>active</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Filter users that are active.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>blocked</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Filter users that are blocked.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>created<wbr>After</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Search for users created after a specific date. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>created<wbr>Before</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Search for users created before a specific date. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>extern<wbr>Provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Lookup users by external provider. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>extern<wbr>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Lookup users by external UID. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>order<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Order the users' list by `id`, `name`, `username`, `created_at` or `updated_at`. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>search</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Search users by username, name or email.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sort</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Sort users' list in asc or desc order. (Requires administrator privileges)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>active</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Filter users that are active.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>blocked</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Filter users that are blocked.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>created_<wbr>after</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Search for users created after a specific date. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>created_<wbr>before</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Search for users created before a specific date. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>extern_<wbr>provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Lookup users by external provider. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>extern_<wbr>uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Lookup users by external UID. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>order_<wbr>by</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Order the users' list by `id`, `name`, `username`, `created_at` or `updated_at`. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>search</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Search users by username, name or email.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sort</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Sort users' list in asc or desc order. (Requires administrator privileges)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetUsers Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Blocked</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created<wbr>After</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created<wbr>Before</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Extern<wbr>Provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Extern<wbr>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The external UID of the user.
{{% /md %}}</dd>

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
        <span>Order<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Search</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sort</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getusersuser">List&lt;Get<wbr>Users<wbr>User&gt;</a></span>
    </dt>
    <dd>{{% md %}}The list of users.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Blocked</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created<wbr>After</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created<wbr>Before</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Extern<wbr>Provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Extern<wbr>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The external UID of the user.
{{% /md %}}</dd>

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
        <span>Order<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Search</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sort</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getusersuser">[]Get<wbr>Users<wbr>User</a></span>
    </dt>
    <dd>{{% md %}}The list of users.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>active</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>blocked</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created<wbr>After</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created<wbr>Before</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>extern<wbr>Provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>extern<wbr>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The external UID of the user.
{{% /md %}}</dd>

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
        <span>order<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>search</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sort</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>users</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getusersuser">Get<wbr>Users<wbr>User[]</a></span>
    </dt>
    <dd>{{% md %}}The list of users.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>active</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>blocked</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created_<wbr>after</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created_<wbr>before</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>extern_<wbr>provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>extern_<wbr>uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The external UID of the user.
{{% /md %}}</dd>

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
        <span>order_<wbr>by</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>search</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sort</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>users</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getusersuser">List[Get<wbr>Users<wbr>User]</a></span>
    </dt>
    <dd>{{% md %}}The list of users.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Users<wbr>User</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gitlab/types/output/#GetUsersUser">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gitlab/sdk/go/gitlab/?tab=doc#GetUsersUser">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Avatar<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The avatar URL of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Bio</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The bio of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Can<wbr>Create<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user can create groups.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Can<wbr>Create<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user can create projects.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Color<wbr>Scheme<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}User's color scheme ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Created<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Date the user was created at.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Current<wbr>Sign<wbr>In<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Current user's sign-in date.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The e-mail address of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Extern<wbr>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Lookup users by external UID. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>External</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user is external.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The unique id assigned to the user by the gitlab server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Admin</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user is an admin.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Last<wbr>Sign<wbr>In<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Last user's sign-in date.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Linkedin</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Linkedin profile of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The organization of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Projects<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Number of projects the user can create.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UID provider of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Skype</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Skype username of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Whether the user is active or blocked.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Theme<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}User's theme ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Twitter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Twitter username of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Two<wbr>Factor<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether user's two factor auth is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Website<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}User's website URL.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Avatar<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The avatar URL of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Bio</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The bio of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Can<wbr>Create<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user can create groups.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Can<wbr>Create<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user can create projects.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Color<wbr>Scheme<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}User's color scheme ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Created<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Date the user was created at.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Current<wbr>Sign<wbr>In<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Current user's sign-in date.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The e-mail address of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Extern<wbr>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Lookup users by external UID. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>External</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user is external.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The unique id assigned to the user by the gitlab server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Admin</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user is an admin.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Last<wbr>Sign<wbr>In<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Last user's sign-in date.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Linkedin</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Linkedin profile of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The organization of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Projects<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Number of projects the user can create.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UID provider of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Skype</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Skype username of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Whether the user is active or blocked.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Theme<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}User's theme ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Twitter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Twitter username of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Two<wbr>Factor<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether user's two factor auth is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Website<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}User's website URL.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>avatar<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The avatar URL of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>bio</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The bio of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>can<wbr>Create<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the user can create groups.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>can<wbr>Create<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the user can create projects.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>color<wbr>Scheme<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}User's color scheme ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>created<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Date the user was created at.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>current<wbr>Sign<wbr>In<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Current user's sign-in date.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The e-mail address of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>extern<wbr>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Lookup users by external UID. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>external</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the user is external.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The unique id assigned to the user by the gitlab server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>is<wbr>Admin</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the user is an admin.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>last<wbr>Sign<wbr>In<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Last user's sign-in date.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>linkedin</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Linkedin profile of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The organization of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>projects<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Number of projects the user can create.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UID provider of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>skype</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Skype username of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Whether the user is active or blocked.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>theme<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}User's theme ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>twitter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Twitter username of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>two<wbr>Factor<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether user's two factor auth is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>website<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}User's website URL.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>avatar<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The avatar URL of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>bio</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The bio of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>can_<wbr>create_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user can create groups.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>can<wbr>Create<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user can create projects.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>color<wbr>Scheme<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}User's color scheme ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>created_<wbr>at</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Date the user was created at.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>current<wbr>Sign<wbr>In<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Current user's sign-in date.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The e-mail address of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>extern<wbr>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Lookup users by external UID. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>external</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user is external.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The unique id assigned to the user by the gitlab server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>is_<wbr>admin</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user is an admin.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>last<wbr>Sign<wbr>In<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Last user's sign-in date.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>linkedin</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Linkedin profile of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The organization of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>projects_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of projects the user can create.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The UID provider of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>skype</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Skype username of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Whether the user is active or blocked.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>theme<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}User's theme ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>twitter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Twitter username of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>two<wbr>Factor<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether user's two factor auth is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The username of the user.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>website<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User's website URL.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







