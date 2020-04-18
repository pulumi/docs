
---
title: "GetRepos"
block_external_search_index: true
---



This data source provides a list Container Registry repositories on Alibaba Cloud.

> **NOTE:** Available in v1.35.0+

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as alicloud from "@pulumi/alicloud";

// Declare the data source
const myRepos = pulumi.output(alicloud.cr.getRepos({
    nameRegex: "my-repos",
    outputFile: "my-repo-json",
}, { async: true }));

export const output = myRepos.repos;
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/cr_repos.html.markdown.





## Using GetRepos

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getRepos<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/cr/#GetReposArgs">GetReposArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/cr/#GetReposResult">GetReposResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_repos(</span>enable_details=None<span class="p">, </span>name_regex=None<span class="p">, </span>namespace=None<span class="p">, </span>output_file=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupRepos<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cr?tab=doc#LookupReposArgs">LookupReposArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cr?tab=doc#LookupReposResult">LookupReposResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetRepos </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Cr.GetReposResult.html">GetReposResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.CR.GetReposArgs.html">GetReposArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Details</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean, false by default, only repository attributes are exported. Set to true if domain list and tags belong to this repository are needed. See `tags` in attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by repository name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of container registry namespace where the repositories are located in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
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
        <span>Enable<wbr>Details</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean, false by default, only repository attributes are exported. Set to true if domain list and tags belong to this repository are needed. See `tags` in attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by repository name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of container registry namespace where the repositories are located in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
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
        <span>enable<wbr>Details</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean, false by default, only repository attributes are exported. Set to true if domain list and tags belong to this repository are needed. See `tags` in attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by repository name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of container registry namespace where the repositories are located in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output<wbr>File</span>
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
        <span>enable_<wbr>details</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean, false by default, only repository attributes are exported. Set to true if domain list and tags belong to this repository are needed. See `tags` in attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by repository name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of container registry namespace where the repositories are located in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetRepos Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Enable<wbr>Details</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of matched Container Registry Repositories. Its element is set to `names`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of repository names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of container registry namespace where repo is located.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Repos</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getreposrepo">List&lt;Get<wbr>Repos<wbr>Repo&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of matched Container Registry Namespaces. Each element contains the following attributes:
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Enable<wbr>Details</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of matched Container Registry Repositories. Its element is set to `names`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of repository names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of container registry namespace where repo is located.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Repos</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getreposrepo">[]Get<wbr>Repos<wbr>Repo</a></span>
    </dt>
    <dd>{{% md %}}A list of matched Container Registry Namespaces. Each element contains the following attributes:
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>enable<wbr>Details</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of matched Container Registry Repositories. Its element is set to `names`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of repository names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of container registry namespace where repo is located.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>repos</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getreposrepo">Get<wbr>Repos<wbr>Repo[]</a></span>
    </dt>
    <dd>{{% md %}}A list of matched Container Registry Namespaces. Each element contains the following attributes:
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>enable_<wbr>details</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of matched Container Registry Repositories. Its element is set to `names`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of repository names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of container registry namespace where repo is located.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>repos</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getreposrepo">List[Get<wbr>Repos<wbr>Repo]</a></span>
    </dt>
    <dd>{{% md %}}A list of matched Container Registry Namespaces. Each element contains the following attributes:
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Repos<wbr>Repo</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetReposRepo">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cr?tab=doc#GetReposRepo">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>List</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getreposrepodomainlist">Get<wbr>Repos<wbr>Repo<wbr>Domain<wbr>List<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The repository domain list.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of container registry namespace.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of container registry namespace where the repositories are located in.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Repo<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}`PUBLIC` or `PRIVATE`, repository's visibility.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Summary</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The repository general information.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getreposrepotag">List&lt;Get<wbr>Repos<wbr>Repo<wbr>Tag<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of image tags belong to this repository. Each contains several attributes, see `Block Tag`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>List</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getreposrepodomainlist">Get<wbr>Repos<wbr>Repo<wbr>Domain<wbr>List</a></span>
    </dt>
    <dd>{{% md %}}The repository domain list.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of container registry namespace.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of container registry namespace where the repositories are located in.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Repo<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}`PUBLIC` or `PRIVATE`, repository's visibility.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Summary</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The repository general information.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getreposrepotag">[]Get<wbr>Repos<wbr>Repo<wbr>Tag</a></span>
    </dt>
    <dd>{{% md %}}A list of image tags belong to this repository. Each contains several attributes, see `Block Tag`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>domain<wbr>List</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getreposrepodomainlist">Get<wbr>Repos<wbr>Repo<wbr>Domain<wbr>List</a></span>
    </dt>
    <dd>{{% md %}}The repository domain list.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of container registry namespace.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of container registry namespace where the repositories are located in.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>repo<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}`PUBLIC` or `PRIVATE`, repository's visibility.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>summary</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The repository general information.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getreposrepotag">Get<wbr>Repos<wbr>Repo<wbr>Tag[]</a></span>
    </dt>
    <dd>{{% md %}}A list of image tags belong to this repository. Each contains several attributes, see `Block Tag`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>domain_<wbr>list</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getreposrepodomainlist">Dict[Get<wbr>Repos<wbr>Repo<wbr>Domain<wbr>List]</a></span>
    </dt>
    <dd>{{% md %}}The repository domain list.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of container registry namespace.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of container registry namespace where the repositories are located in.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>repo_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}`PUBLIC` or `PRIVATE`, repository's visibility.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>summary</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The repository general information.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getreposrepotag">List[Get<wbr>Repos<wbr>Repo<wbr>Tag]</a></span>
    </dt>
    <dd>{{% md %}}A list of image tags belong to this repository. Each contains several attributes, see `Block Tag`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Repos<wbr>Repo<wbr>Domain<wbr>List</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetReposRepoDomainList">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cr?tab=doc#GetReposRepoDomainList">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Internal</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Domain of internal endpoint, only in some regions.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Public</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Domain of public endpoint.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vpc</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Domain of vpc endpoint.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Internal</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Domain of internal endpoint, only in some regions.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Public</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Domain of public endpoint.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vpc</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Domain of vpc endpoint.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>internal</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Domain of internal endpoint, only in some regions.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>public</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Domain of public endpoint.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vpc</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Domain of vpc endpoint.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>internal</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Domain of internal endpoint, only in some regions.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>public</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Domain of public endpoint.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vpc</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Domain of vpc endpoint.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Repos<wbr>Repo<wbr>Tag</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetReposRepoTag">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cr?tab=doc#GetReposRepoTag">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Digest</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Digest of this image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Image<wbr>Create</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Create time of this image, unix time in nanoseconds.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Id of this image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Image<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Status of this image, in bytes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Image<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Last update time of this image, unix time in nanoseconds.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Status of this image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Tag of this image.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Digest</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Digest of this image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Image<wbr>Create</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Create time of this image, unix time in nanoseconds.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Id of this image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Image<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Status of this image, in bytes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Image<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Last update time of this image, unix time in nanoseconds.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Status of this image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Tag of this image.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>digest</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Digest of this image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>image<wbr>Create</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Create time of this image, unix time in nanoseconds.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Id of this image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>image<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Status of this image, in bytes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>image<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Last update time of this image, unix time in nanoseconds.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Status of this image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Tag of this image.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>digest</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Digest of this image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>image<wbr>Create</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Create time of this image, unix time in nanoseconds.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>image_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Id of this image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>image<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Status of this image, in bytes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>image<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Last update time of this image, unix time in nanoseconds.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Status of this image.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Tag of this image.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







