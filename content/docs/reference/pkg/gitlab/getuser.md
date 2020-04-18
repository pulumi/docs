
---
title: "GetUser"
block_external_search_index: true
---



Provides details about a specific user in the gitlab provider. Especially the ability to lookup the id for linking to other resources.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gitlab from "@pulumi/gitlab";

const example = pulumi.output(gitlab.getUser({
    username: "myuser",
}, { async: true }));
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/d/user.html.markdown.





## Using GetUser

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getUser<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gitlab/#GetUserArgs">GetUserArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gitlab/#GetUserResult">GetUserResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_user(</span>email=None<span class="p">, </span>user_id=None<span class="p">, </span>username=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupUser<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gitlab/sdk/go/gitlab/?tab=doc#GetUserArgs">GetUserArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gitlab/sdk/go/gitlab/?tab=doc#LookupUserResult">LookupUserResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetUser </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gitlab/Pulumi.Gitlab.GetUserResult.html">GetUserResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gitlab/Pulumi.Gitlab.GetUserArgs.html">GetUserArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The e-mail address of the user. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The ID of the user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The username of the user.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The e-mail address of the user. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The ID of the user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The username of the user.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The e-mail address of the user. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The ID of the user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The username of the user.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The e-mail address of the user. (Requires administrator privileges)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The ID of the user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The username of the user.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetUser Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Avatar<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The avatar URL of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bio</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The bio of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Can<wbr>Create<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user can create groups.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Can<wbr>Create<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user can create projects.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Color<wbr>Scheme<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}User's color scheme ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Date the user was created at.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Current<wbr>Sign<wbr>In<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Current user's sign-in date.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The e-mail address of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Extern<wbr>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The external UID of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>External</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user is external.
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
        <span>Is<wbr>Admin</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user is an admin.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Last<wbr>Sign<wbr>In<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Last user's sign-in date.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Linkedin</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Linkedin profile of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The organization of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Projects<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Number of projects the user can create.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Skype</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Skype username of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Whether the user is active or blocked.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Theme<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}User's theme ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Twitter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Twitter username of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Two<wbr>Factor<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether user's two factor auth is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UID provider of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
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

    <dt class="property-"
            title="">
        <span>Avatar<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The avatar URL of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bio</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The bio of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Can<wbr>Create<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user can create groups.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Can<wbr>Create<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user can create projects.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Color<wbr>Scheme<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}User's color scheme ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Date the user was created at.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Current<wbr>Sign<wbr>In<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Current user's sign-in date.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The e-mail address of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Extern<wbr>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The external UID of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>External</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user is external.
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
        <span>Is<wbr>Admin</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user is an admin.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Last<wbr>Sign<wbr>In<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Last user's sign-in date.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Linkedin</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Linkedin profile of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The organization of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Projects<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Number of projects the user can create.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Skype</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Skype username of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Whether the user is active or blocked.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Theme<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}User's theme ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Twitter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Twitter username of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Two<wbr>Factor<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether user's two factor auth is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UID provider of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
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

    <dt class="property-"
            title="">
        <span>avatar<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The avatar URL of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bio</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The bio of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>can<wbr>Create<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the user can create groups.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>can<wbr>Create<wbr>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the user can create projects.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>color<wbr>Scheme<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}User's color scheme ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Date the user was created at.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>current<wbr>Sign<wbr>In<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Current user's sign-in date.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The e-mail address of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>extern<wbr>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The external UID of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>external</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the user is external.
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
        <span>is<wbr>Admin</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the user is an admin.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>last<wbr>Sign<wbr>In<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Last user's sign-in date.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>linkedin</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Linkedin profile of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The organization of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>projects<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Number of projects the user can create.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>skype</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Skype username of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Whether the user is active or blocked.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>theme<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}User's theme ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>twitter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Twitter username of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>two<wbr>Factor<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether user's two factor auth is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user<wbr>Provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UID provider of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
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

    <dt class="property-"
            title="">
        <span>avatar_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The avatar URL of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bio</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The bio of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>can_<wbr>create_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user can create groups.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>can_<wbr>create_<wbr>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user can create projects.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>color_<wbr>scheme_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}User's color scheme ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created_<wbr>at</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Date the user was created at.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>current_<wbr>sign_<wbr>in_<wbr>at</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Current user's sign-in date.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The e-mail address of the user.
{{% /md %}}</dd>

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
        <span>external</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user is external.
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
        <span>is_<wbr>admin</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the user is an admin.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>last_<wbr>sign_<wbr>in_<wbr>at</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Last user's sign-in date.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>linkedin</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Linkedin profile of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>organization</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The organization of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>projects_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of projects the user can create.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>skype</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Skype username of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Whether the user is active or blocked.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>theme_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}User's theme ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>twitter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Twitter username of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>two_<wbr>factor_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether user's two factor auth is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user_<wbr>provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The UID provider of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The username of the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>website_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User's website URL.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







