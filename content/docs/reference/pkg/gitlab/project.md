
---
title: "Project"
block_external_search_index: true
---






## Create a Project Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gitlab/#Project">Project</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gitlab/#ProjectArgs">ProjectArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Project</span><span class="p">(resource_name, opts=None, </span>approvals_before_merge=None<span class="p">, </span>archived=None<span class="p">, </span>container_registry_enabled=None<span class="p">, </span>default_branch=None<span class="p">, </span>description=None<span class="p">, </span>initialize_with_readme=None<span class="p">, </span>issues_enabled=None<span class="p">, </span>lfs_enabled=None<span class="p">, </span>merge_method=None<span class="p">, </span>merge_requests_enabled=None<span class="p">, </span>name=None<span class="p">, </span>namespace_id=None<span class="p">, </span>only_allow_merge_if_all_discussions_are_resolved=None<span class="p">, </span>only_allow_merge_if_pipeline_succeeds=None<span class="p">, </span>path=None<span class="p">, </span>pipelines_enabled=None<span class="p">, </span>request_access_enabled=None<span class="p">, </span>shared_runners_enabled=None<span class="p">, </span>shared_with_groups=None<span class="p">, </span>snippets_enabled=None<span class="p">, </span>tags=None<span class="p">, </span>visibility_level=None<span class="p">, </span>wiki_enabled=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewProject<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gitlab/sdk/go/gitlab/?tab=doc#ProjectArgs">ProjectArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gitlab/sdk/go/gitlab/?tab=doc#Project">Project</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gitlab/Pulumi.Gitlab.Project.html">Project</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gitlab/Pulumi.GitLab.ProjectArgs.html">ProjectArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Approvals<wbr>Before<wbr>Merge</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Number of merge request approvals required for merging. Default is 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Archived</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Registry<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable container registry for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Branch</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The default branch for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A description of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initialize<wbr>With<wbr>Readme</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Create master branch with first commit containing a README.md file.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issues<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable issue tracking for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lfs<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable LFS for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Merge<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set to `ff` to create fast-forward merges
Valid values are `merge`, `rebase_merge`, `ff`
Repositories are created with `merge` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Merge<wbr>Requests<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable merge requests for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The namespace (group or user) of the project. Defaults to your user.
See `gitlab..Group` for an example.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Only<wbr>Allow<wbr>Merge<wbr>If<wbr>All<wbr>Discussions<wbr>Are<wbr>Resolved</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to true if you want allow merges only if all discussions are resolved.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Only<wbr>Allow<wbr>Merge<wbr>If<wbr>Pipeline<wbr>Succeeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to true if you want allow merges only if a pipeline succeeds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The path of the repository.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pipelines<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable pipelines for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Access<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allow users to request member access.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared<wbr>Runners<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable shared runners for this project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared<wbr>With<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#projectsharedwithgroup">List&lt;Pulumi.<wbr>Git<wbr>Lab.<wbr>Inputs.<wbr>Project<wbr>Shared<wbr>With<wbr>Group<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Enable sharing the project with a list of groups (maps).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snippets<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable snippets for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}Tags (topics) of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Visibility<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set to `public` to create a public project.
Valid values are `private`, `internal`, `public`.
Repositories are created as private by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wiki<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable wiki for the project.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Approvals<wbr>Before<wbr>Merge</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Number of merge request approvals required for merging. Default is 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Archived</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Registry<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable container registry for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Branch</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The default branch for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A description of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initialize<wbr>With<wbr>Readme</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Create master branch with first commit containing a README.md file.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issues<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable issue tracking for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lfs<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable LFS for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Merge<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set to `ff` to create fast-forward merges
Valid values are `merge`, `rebase_merge`, `ff`
Repositories are created with `merge` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Merge<wbr>Requests<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable merge requests for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The namespace (group or user) of the project. Defaults to your user.
See `gitlab..Group` for an example.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Only<wbr>Allow<wbr>Merge<wbr>If<wbr>All<wbr>Discussions<wbr>Are<wbr>Resolved</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to true if you want allow merges only if all discussions are resolved.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Only<wbr>Allow<wbr>Merge<wbr>If<wbr>Pipeline<wbr>Succeeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to true if you want allow merges only if a pipeline succeeds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The path of the repository.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pipelines<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable pipelines for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Access<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allow users to request member access.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared<wbr>Runners<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable shared runners for this project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared<wbr>With<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#projectsharedwithgroup">[]Project<wbr>Shared<wbr>With<wbr>Group</a></span>
    </dt>
    <dd>{{% md %}}Enable sharing the project with a list of groups (maps).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snippets<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable snippets for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Tags (topics) of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Visibility<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set to `public` to create a public project.
Valid values are `private`, `internal`, `public`.
Repositories are created as private by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wiki<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable wiki for the project.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>approvals<wbr>Before<wbr>Merge</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Number of merge request approvals required for merging. Default is 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>archived</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>container<wbr>Registry<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable container registry for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Branch</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The default branch for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A description of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initialize<wbr>With<wbr>Readme</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Create master branch with first commit containing a README.md file.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issues<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable issue tracking for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lfs<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable LFS for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>merge<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set to `ff` to create fast-forward merges
Valid values are `merge`, `rebase_merge`, `ff`
Repositories are created with `merge` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>merge<wbr>Requests<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable merge requests for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The namespace (group or user) of the project. Defaults to your user.
See `gitlab..Group` for an example.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>only<wbr>Allow<wbr>Merge<wbr>If<wbr>All<wbr>Discussions<wbr>Are<wbr>Resolved</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Set to true if you want allow merges only if all discussions are resolved.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>only<wbr>Allow<wbr>Merge<wbr>If<wbr>Pipeline<wbr>Succeeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Set to true if you want allow merges only if a pipeline succeeds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The path of the repository.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pipelines<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable pipelines for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Access<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Allow users to request member access.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared<wbr>Runners<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable shared runners for this project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared<wbr>With<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#projectsharedwithgroup">Project<wbr>Shared<wbr>With<wbr>Group[]</a></span>
    </dt>
    <dd>{{% md %}}Enable sharing the project with a list of groups (maps).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snippets<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable snippets for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Tags (topics) of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>visibility<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set to `public` to create a public project.
Valid values are `private`, `internal`, `public`.
Repositories are created as private by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wiki<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable wiki for the project.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>approvals_<wbr>before_<wbr>merge</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of merge request approvals required for merging. Default is 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>archived</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>container_<wbr>registry_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable container registry for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>branch</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The default branch for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A description of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initialize_<wbr>with_<wbr>readme</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Create master branch with first commit containing a README.md file.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issues_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable issue tracking for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lfs_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable LFS for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>merge_<wbr>method</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Set to `ff` to create fast-forward merges
Valid values are `merge`, `rebase_merge`, `ff`
Repositories are created with `merge` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>merge_<wbr>requests_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable merge requests for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The namespace (group or user) of the project. Defaults to your user.
See `gitlab..Group` for an example.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>only_<wbr>allow_<wbr>merge_<wbr>if_<wbr>all_<wbr>discussions_<wbr>are_<wbr>resolved</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to true if you want allow merges only if all discussions are resolved.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>only_<wbr>allow_<wbr>merge_<wbr>if_<wbr>pipeline_<wbr>succeeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to true if you want allow merges only if a pipeline succeeds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The path of the repository.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pipelines_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable pipelines for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request_<wbr>access_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allow users to request member access.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared_<wbr>runners_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable shared runners for this project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared_<wbr>with_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#projectsharedwithgroup">List[Project<wbr>Shared<wbr>With<wbr>Group]</a></span>
    </dt>
    <dd>{{% md %}}Enable sharing the project with a list of groups (maps).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snippets_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable snippets for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Tags (topics) of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>visibility_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Set to `public` to create a public project.
Valid values are `private`, `internal`, `public`.
Repositories are created as private by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wiki_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable wiki for the project.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Project Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Http<wbr>Url<wbr>To<wbr>Repo</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be provided to `git clone` to clone the
repository via HTTP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Runners<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Registration token to use during runner setup.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ssh<wbr>Url<wbr>To<wbr>Repo</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be provided to `git clone` to clone the
repository via SSH.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Web<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be used to find the project in a browser.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Http<wbr>Url<wbr>To<wbr>Repo</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be provided to `git clone` to clone the
repository via HTTP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Runners<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Registration token to use during runner setup.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ssh<wbr>Url<wbr>To<wbr>Repo</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be provided to `git clone` to clone the
repository via SSH.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Web<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be used to find the project in a browser.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>http<wbr>Url<wbr>To<wbr>Repo</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be provided to `git clone` to clone the
repository via HTTP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>runners<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Registration token to use during runner setup.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ssh<wbr>Url<wbr>To<wbr>Repo</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be provided to `git clone` to clone the
repository via SSH.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>web<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be used to find the project in a browser.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>http_<wbr>url_<wbr>to_<wbr>repo</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}URL that can be provided to `git clone` to clone the
repository via HTTP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>runners_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Registration token to use during runner setup.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ssh_<wbr>url_<wbr>to_<wbr>repo</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}URL that can be provided to `git clone` to clone the
repository via SSH.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>web_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}URL that can be used to find the project in a browser.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Project Resource

Get an existing Project resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gitlab/#ProjectState">ProjectState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gitlab/#Project">Project</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>approvals_before_merge=None<span class="p">, </span>archived=None<span class="p">, </span>container_registry_enabled=None<span class="p">, </span>default_branch=None<span class="p">, </span>description=None<span class="p">, </span>http_url_to_repo=None<span class="p">, </span>initialize_with_readme=None<span class="p">, </span>issues_enabled=None<span class="p">, </span>lfs_enabled=None<span class="p">, </span>merge_method=None<span class="p">, </span>merge_requests_enabled=None<span class="p">, </span>name=None<span class="p">, </span>namespace_id=None<span class="p">, </span>only_allow_merge_if_all_discussions_are_resolved=None<span class="p">, </span>only_allow_merge_if_pipeline_succeeds=None<span class="p">, </span>path=None<span class="p">, </span>pipelines_enabled=None<span class="p">, </span>request_access_enabled=None<span class="p">, </span>runners_token=None<span class="p">, </span>shared_runners_enabled=None<span class="p">, </span>shared_with_groups=None<span class="p">, </span>snippets_enabled=None<span class="p">, </span>ssh_url_to_repo=None<span class="p">, </span>tags=None<span class="p">, </span>visibility_level=None<span class="p">, </span>web_url=None<span class="p">, </span>wiki_enabled=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetProject<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gitlab/sdk/go/gitlab/?tab=doc#ProjectState">ProjectState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gitlab/sdk/go/gitlab/?tab=doc#Project">Project</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gitlab/Pulumi.Gitlab.Project.html">Project</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gitlab/Pulumi.Gitlab..ProjectState.html">ProjectState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Approvals<wbr>Before<wbr>Merge</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Number of merge request approvals required for merging. Default is 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Archived</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Registry<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable container registry for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Branch</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The default branch for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A description of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Url<wbr>To<wbr>Repo</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be provided to `git clone` to clone the
repository via HTTP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initialize<wbr>With<wbr>Readme</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Create master branch with first commit containing a README.md file.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issues<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable issue tracking for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lfs<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable LFS for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Merge<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set to `ff` to create fast-forward merges
Valid values are `merge`, `rebase_merge`, `ff`
Repositories are created with `merge` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Merge<wbr>Requests<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable merge requests for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The namespace (group or user) of the project. Defaults to your user.
See `gitlab..Group` for an example.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Only<wbr>Allow<wbr>Merge<wbr>If<wbr>All<wbr>Discussions<wbr>Are<wbr>Resolved</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to true if you want allow merges only if all discussions are resolved.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Only<wbr>Allow<wbr>Merge<wbr>If<wbr>Pipeline<wbr>Succeeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to true if you want allow merges only if a pipeline succeeds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The path of the repository.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pipelines<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable pipelines for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Access<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allow users to request member access.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runners<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Registration token to use during runner setup.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared<wbr>Runners<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable shared runners for this project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared<wbr>With<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#projectsharedwithgroup">List&lt;Pulumi.<wbr>Git<wbr>Lab.<wbr>Inputs.<wbr>Project<wbr>Shared<wbr>With<wbr>Group<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Enable sharing the project with a list of groups (maps).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snippets<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable snippets for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssh<wbr>Url<wbr>To<wbr>Repo</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be provided to `git clone` to clone the
repository via SSH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}Tags (topics) of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Visibility<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set to `public` to create a public project.
Valid values are `private`, `internal`, `public`.
Repositories are created as private by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Web<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be used to find the project in a browser.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wiki<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable wiki for the project.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Approvals<wbr>Before<wbr>Merge</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Number of merge request approvals required for merging. Default is 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Archived</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Registry<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable container registry for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Branch</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The default branch for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A description of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Url<wbr>To<wbr>Repo</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be provided to `git clone` to clone the
repository via HTTP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initialize<wbr>With<wbr>Readme</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Create master branch with first commit containing a README.md file.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issues<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable issue tracking for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lfs<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable LFS for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Merge<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set to `ff` to create fast-forward merges
Valid values are `merge`, `rebase_merge`, `ff`
Repositories are created with `merge` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Merge<wbr>Requests<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable merge requests for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The namespace (group or user) of the project. Defaults to your user.
See `gitlab..Group` for an example.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Only<wbr>Allow<wbr>Merge<wbr>If<wbr>All<wbr>Discussions<wbr>Are<wbr>Resolved</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to true if you want allow merges only if all discussions are resolved.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Only<wbr>Allow<wbr>Merge<wbr>If<wbr>Pipeline<wbr>Succeeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to true if you want allow merges only if a pipeline succeeds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The path of the repository.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pipelines<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable pipelines for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Access<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allow users to request member access.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runners<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Registration token to use during runner setup.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared<wbr>Runners<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable shared runners for this project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared<wbr>With<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#projectsharedwithgroup">[]Project<wbr>Shared<wbr>With<wbr>Group</a></span>
    </dt>
    <dd>{{% md %}}Enable sharing the project with a list of groups (maps).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snippets<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable snippets for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssh<wbr>Url<wbr>To<wbr>Repo</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be provided to `git clone` to clone the
repository via SSH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Tags (topics) of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Visibility<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set to `public` to create a public project.
Valid values are `private`, `internal`, `public`.
Repositories are created as private by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Web<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be used to find the project in a browser.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wiki<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable wiki for the project.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>approvals<wbr>Before<wbr>Merge</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Number of merge request approvals required for merging. Default is 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>archived</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>container<wbr>Registry<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable container registry for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Branch</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The default branch for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A description of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Url<wbr>To<wbr>Repo</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be provided to `git clone` to clone the
repository via HTTP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initialize<wbr>With<wbr>Readme</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Create master branch with first commit containing a README.md file.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issues<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable issue tracking for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lfs<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable LFS for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>merge<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set to `ff` to create fast-forward merges
Valid values are `merge`, `rebase_merge`, `ff`
Repositories are created with `merge` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>merge<wbr>Requests<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable merge requests for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The namespace (group or user) of the project. Defaults to your user.
See `gitlab..Group` for an example.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>only<wbr>Allow<wbr>Merge<wbr>If<wbr>All<wbr>Discussions<wbr>Are<wbr>Resolved</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Set to true if you want allow merges only if all discussions are resolved.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>only<wbr>Allow<wbr>Merge<wbr>If<wbr>Pipeline<wbr>Succeeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Set to true if you want allow merges only if a pipeline succeeds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The path of the repository.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pipelines<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable pipelines for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Access<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Allow users to request member access.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runners<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Registration token to use during runner setup.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared<wbr>Runners<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable shared runners for this project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared<wbr>With<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#projectsharedwithgroup">Project<wbr>Shared<wbr>With<wbr>Group[]</a></span>
    </dt>
    <dd>{{% md %}}Enable sharing the project with a list of groups (maps).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snippets<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable snippets for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssh<wbr>Url<wbr>To<wbr>Repo</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be provided to `git clone` to clone the
repository via SSH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Tags (topics) of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>visibility<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set to `public` to create a public project.
Valid values are `private`, `internal`, `public`.
Repositories are created as private by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>web<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL that can be used to find the project in a browser.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wiki<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable wiki for the project.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>approvals_<wbr>before_<wbr>merge</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of merge request approvals required for merging. Default is 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>archived</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>container_<wbr>registry_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable container registry for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>branch</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The default branch for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A description of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http_<wbr>url_<wbr>to_<wbr>repo</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}URL that can be provided to `git clone` to clone the
repository via HTTP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initialize_<wbr>with_<wbr>readme</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Create master branch with first commit containing a README.md file.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issues_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable issue tracking for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lfs_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable LFS for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>merge_<wbr>method</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Set to `ff` to create fast-forward merges
Valid values are `merge`, `rebase_merge`, `ff`
Repositories are created with `merge` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>merge_<wbr>requests_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable merge requests for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The namespace (group or user) of the project. Defaults to your user.
See `gitlab..Group` for an example.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>only_<wbr>allow_<wbr>merge_<wbr>if_<wbr>all_<wbr>discussions_<wbr>are_<wbr>resolved</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to true if you want allow merges only if all discussions are resolved.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>only_<wbr>allow_<wbr>merge_<wbr>if_<wbr>pipeline_<wbr>succeeds</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to true if you want allow merges only if a pipeline succeeds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The path of the repository.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pipelines_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable pipelines for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request_<wbr>access_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allow users to request member access.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runners_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Registration token to use during runner setup.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared_<wbr>runners_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable shared runners for this project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared_<wbr>with_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#projectsharedwithgroup">List[Project<wbr>Shared<wbr>With<wbr>Group]</a></span>
    </dt>
    <dd>{{% md %}}Enable sharing the project with a list of groups (maps).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snippets_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable snippets for the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssh_<wbr>url_<wbr>to_<wbr>repo</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}URL that can be provided to `git clone` to clone the
repository via SSH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Tags (topics) of the project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>visibility_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Set to `public` to create a public project.
Valid values are `private`, `internal`, `public`.
Repositories are created as private by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>web_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}URL that can be used to find the project in a browser.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wiki_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable wiki for the project.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Project<wbr>Shared<wbr>With<wbr>Group</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gitlab/types/input/#ProjectSharedWithGroup">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gitlab/types/output/#ProjectSharedWithGroup">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gitlab/sdk/go/gitlab/?tab=doc#ProjectSharedWithGroupArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gitlab/sdk/go/gitlab/?tab=doc#ProjectSharedWithGroupOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Group<wbr>Access<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Group's sharing permissions. See [group members permission][group_members_permissions] for more info.
Valid values are `guest`, `reporter`, `developer`, `master`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Group id of the group you want to share the project with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Group's name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Group<wbr>Access<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Group's sharing permissions. See [group members permission][group_members_permissions] for more info.
Valid values are `guest`, `reporter`, `developer`, `master`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Group id of the group you want to share the project with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Group's name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>group<wbr>Access<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Group's sharing permissions. See [group members permission][group_members_permissions] for more info.
Valid values are `guest`, `reporter`, `developer`, `master`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Group id of the group you want to share the project with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Group's name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>group<wbr>Access<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Group's sharing permissions. See [group members permission][group_members_permissions] for more info.
Valid values are `guest`, `reporter`, `developer`, `master`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Group id of the group you want to share the project with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Group's name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gitlab">https://github.com/pulumi/pulumi-gitlab</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

