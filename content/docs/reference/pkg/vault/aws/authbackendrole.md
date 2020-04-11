
---
title: "AuthBackendRole"
block_external_search_index: true
---






## Create a AuthBackendRole Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/aws/#AuthBackendRole">AuthBackendRole</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/aws/#AuthBackendRoleArgs">AuthBackendRoleArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">AuthBackendRole</span><span class="p">(resource_name, opts=None, </span>allow_instance_migration=None<span class="p">, </span>auth_type=None<span class="p">, </span>backend=None<span class="p">, </span>bound_account_ids=None<span class="p">, </span>bound_ami_ids=None<span class="p">, </span>bound_ec2_instance_ids=None<span class="p">, </span>bound_iam_instance_profile_arns=None<span class="p">, </span>bound_iam_principal_arns=None<span class="p">, </span>bound_iam_role_arns=None<span class="p">, </span>bound_regions=None<span class="p">, </span>bound_subnet_ids=None<span class="p">, </span>bound_vpc_ids=None<span class="p">, </span>disallow_reauthentication=None<span class="p">, </span>inferred_aws_region=None<span class="p">, </span>inferred_entity_type=None<span class="p">, </span>max_ttl=None<span class="p">, </span>period=None<span class="p">, </span>policies=None<span class="p">, </span>resolve_aws_unique_ids=None<span class="p">, </span>role=None<span class="p">, </span>role_tag=None<span class="p">, </span>token_bound_cidrs=None<span class="p">, </span>token_explicit_max_ttl=None<span class="p">, </span>token_max_ttl=None<span class="p">, </span>token_no_default_policy=None<span class="p">, </span>token_num_uses=None<span class="p">, </span>token_period=None<span class="p">, </span>token_policies=None<span class="p">, </span>token_ttl=None<span class="p">, </span>token_type=None<span class="p">, </span>ttl=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewAuthBackendRole<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/aws?tab=doc#AuthBackendRoleArgs">AuthBackendRoleArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/aws?tab=doc#AuthBackendRole">AuthBackendRole</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.Aws.AuthBackendRole.html">AuthBackendRole</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.Aws.AuthBackendRoleArgs.html">AuthBackendRoleArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Allow<wbr>Instance<wbr>Migration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When true, allows migration of the underlying instance where the client resides. Use with caution.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The auth type permitted for this role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Account<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances with this account ID in their identity document will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Ami<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances using this AMI ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Ec2Instance<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this instance ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Iam<wbr>Instance<wbr>Profile<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with an IAM instance profile ARN that matches this value will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Iam<wbr>Principal<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The IAM principal that must be authenticated using the iam auth method.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Iam<wbr>Role<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this IAM role ARN will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances in this region will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this subnet ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Vpc<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this VPC ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disallow<wbr>Reauthentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When true, only allows a single token to be granted per instance ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inferred<wbr>Aws<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region to search for the inferred entities in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inferred<wbr>Entity<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of inferencing Vault should do.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed lifetime of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}If set, indicates that the token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token's TTL will be set to the value of this field. The maximum
allowed lifetime of token issued using this role. Specified as a number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resolve<wbr>Aws<wbr>Unique<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether or not Vault should resolve the bound_iam_principal_arn to an AWS Unique ID. When true, deleting a principal and
recreating it with the same name won't automatically grant the new principal the same roles in Vault that the old
principal had.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key of the tag on EC2 instance to use for role tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The TTL period of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Instance<wbr>Migration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When true, allows migration of the underlying instance where the client resides. Use with caution.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The auth type permitted for this role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Account<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances with this account ID in their identity document will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Ami<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances using this AMI ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Ec2Instance<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this instance ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Iam<wbr>Instance<wbr>Profile<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with an IAM instance profile ARN that matches this value will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Iam<wbr>Principal<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The IAM principal that must be authenticated using the iam auth method.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Iam<wbr>Role<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this IAM role ARN will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances in this region will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this subnet ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Vpc<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this VPC ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disallow<wbr>Reauthentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When true, only allows a single token to be granted per instance ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inferred<wbr>Aws<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region to search for the inferred entities in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inferred<wbr>Entity<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of inferencing Vault should do.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed lifetime of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}If set, indicates that the token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token's TTL will be set to the value of this field. The maximum
allowed lifetime of token issued using this role. Specified as a number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resolve<wbr>Aws<wbr>Unique<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether or not Vault should resolve the bound_iam_principal_arn to an AWS Unique ID. When true, deleting a principal and
recreating it with the same name won't automatically grant the new principal the same roles in Vault that the old
principal had.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The key of the tag on EC2 instance to use for role tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The TTL period of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Instance<wbr>Migration</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When true, allows migration of the underlying instance where the client resides. Use with caution.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auth<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The auth type permitted for this role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Account<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances with this account ID in their identity document will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Ami<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances using this AMI ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Ec2Instance<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this instance ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Iam<wbr>Instance<wbr>Profile<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with an IAM instance profile ARN that matches this value will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Iam<wbr>Principal<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The IAM principal that must be authenticated using the iam auth method.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Iam<wbr>Role<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this IAM role ARN will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances in this region will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this subnet ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Vpc<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this VPC ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disallow<wbr>Reauthentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When true, only allows a single token to be granted per instance ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inferred<wbr>Aws<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region to search for the inferred entities in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inferred<wbr>Entity<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of inferencing Vault should do.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed lifetime of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}If set, indicates that the token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token's TTL will be set to the value of this field. The maximum
allowed lifetime of token issued using this role. Specified as a number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>resolve<wbr>Aws<wbr>Unique<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether or not Vault should resolve the bound_iam_principal_arn to an AWS Unique ID. When true, deleting a principal and
recreating it with the same name won't automatically grant the new principal the same roles in Vault that the old
principal had.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key of the tag on EC2 instance to use for role tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The TTL period of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>instance_<wbr>migration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, allows migration of the underlying instance where the client resides. Use with caution.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auth_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The auth type permitted for this role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>account_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances with this account ID in their identity document will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>ami_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances using this AMI ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>ec2_<wbr>instance_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this instance ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>iam_<wbr>instance_<wbr>profile_<wbr>arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with an IAM instance profile ARN that matches this value will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>iam_<wbr>principal_<wbr>arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The IAM principal that must be authenticated using the iam auth method.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>iam_<wbr>role_<wbr>arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this IAM role ARN will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances in this region will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>subnet_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this subnet ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>vpc_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this VPC ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disallow_<wbr>reauthentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, only allows a single token to be granted per instance ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inferred_<wbr>aws_<wbr>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region to search for the inferred entities in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inferred_<wbr>entity_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of inferencing Vault should do.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed lifetime of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}If set, indicates that the token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token's TTL will be set to the value of this field. The maximum
allowed lifetime of token issued using this role. Specified as a number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>resolve_<wbr>aws_<wbr>unique_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether or not Vault should resolve the bound_iam_principal_arn to an AWS Unique ID. When true, deleting a principal and
recreating it with the same name won't automatically grant the new principal the same roles in Vault that the old
principal had.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role_<wbr>tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The key of the tag on EC2 instance to use for role tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>bound_<wbr>cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>explicit_<wbr>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>no_<wbr>default_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>num_<wbr>uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The TTL period of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}







## AuthBackendRole Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Allow<wbr>Instance<wbr>Migration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When true, allows migration of the underlying instance where the client resides. Use with caution.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Auth<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The auth type permitted for this role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Account<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances with this account ID in their identity document will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Ami<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances using this AMI ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Ec2Instance<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this instance ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Iam<wbr>Instance<wbr>Profile<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with an IAM instance profile ARN that matches this value will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Iam<wbr>Principal<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The IAM principal that must be authenticated using the iam auth method.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Iam<wbr>Role<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this IAM role ARN will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances in this region will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this subnet ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Vpc<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this VPC ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disallow<wbr>Reauthentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When true, only allows a single token to be granted per instance ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Inferred<wbr>Aws<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region to search for the inferred entities in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Inferred<wbr>Entity<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of inferencing Vault should do.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed lifetime of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}If set, indicates that the token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token's TTL will be set to the value of this field. The maximum
allowed lifetime of token issued using this role. Specified as a number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Resolve<wbr>Aws<wbr>Unique<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether or not Vault should resolve the bound_iam_principal_arn to an AWS Unique ID. When true, deleting a principal and
recreating it with the same name won't automatically grant the new principal the same roles in Vault that the old
principal had.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key of the tag on EC2 instance to use for role tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The TTL period of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Allow<wbr>Instance<wbr>Migration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When true, allows migration of the underlying instance where the client resides. Use with caution.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Auth<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The auth type permitted for this role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Account<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances with this account ID in their identity document will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Ami<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances using this AMI ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Ec2Instance<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this instance ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Iam<wbr>Instance<wbr>Profile<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with an IAM instance profile ARN that matches this value will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Iam<wbr>Principal<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The IAM principal that must be authenticated using the iam auth method.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Iam<wbr>Role<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this IAM role ARN will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances in this region will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this subnet ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bound<wbr>Vpc<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this VPC ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disallow<wbr>Reauthentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When true, only allows a single token to be granted per instance ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Inferred<wbr>Aws<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region to search for the inferred entities in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Inferred<wbr>Entity<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of inferencing Vault should do.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed lifetime of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}If set, indicates that the token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token's TTL will be set to the value of this field. The maximum
allowed lifetime of token issued using this role. Specified as a number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Resolve<wbr>Aws<wbr>Unique<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether or not Vault should resolve the bound_iam_principal_arn to an AWS Unique ID. When true, deleting a principal and
recreating it with the same name won't automatically grant the new principal the same roles in Vault that the old
principal had.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The key of the tag on EC2 instance to use for role tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The TTL period of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>allow<wbr>Instance<wbr>Migration</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When true, allows migration of the underlying instance where the client resides. Use with caution.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>auth<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The auth type permitted for this role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound<wbr>Account<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances with this account ID in their identity document will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound<wbr>Ami<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances using this AMI ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound<wbr>Ec2Instance<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this instance ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound<wbr>Iam<wbr>Instance<wbr>Profile<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with an IAM instance profile ARN that matches this value will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound<wbr>Iam<wbr>Principal<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The IAM principal that must be authenticated using the iam auth method.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound<wbr>Iam<wbr>Role<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this IAM role ARN will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances in this region will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound<wbr>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this subnet ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound<wbr>Vpc<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this VPC ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disallow<wbr>Reauthentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When true, only allows a single token to be granted per instance ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>inferred<wbr>Aws<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region to search for the inferred entities in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>inferred<wbr>Entity<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of inferencing Vault should do.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed lifetime of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}If set, indicates that the token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token's TTL will be set to the value of this field. The maximum
allowed lifetime of token issued using this role. Specified as a number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>resolve<wbr>Aws<wbr>Unique<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether or not Vault should resolve the bound_iam_principal_arn to an AWS Unique ID. When true, deleting a principal and
recreating it with the same name won't automatically grant the new principal the same roles in Vault that the old
principal had.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key of the tag on EC2 instance to use for role tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The TTL period of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>allow_<wbr>instance_<wbr>migration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, allows migration of the underlying instance where the client resides. Use with caution.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>auth_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The auth type permitted for this role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound_<wbr>account_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances with this account ID in their identity document will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound_<wbr>ami_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances using this AMI ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound_<wbr>ec2_<wbr>instance_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this instance ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound_<wbr>iam_<wbr>instance_<wbr>profile_<wbr>arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with an IAM instance profile ARN that matches this value will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound_<wbr>iam_<wbr>principal_<wbr>arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The IAM principal that must be authenticated using the iam auth method.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound_<wbr>iam_<wbr>role_<wbr>arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this IAM role ARN will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound_<wbr>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances in this region will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound_<wbr>subnet_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this subnet ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bound_<wbr>vpc_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this VPC ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disallow_<wbr>reauthentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, only allows a single token to be granted per instance ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>inferred_<wbr>aws_<wbr>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region to search for the inferred entities in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>inferred_<wbr>entity_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of inferencing Vault should do.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed lifetime of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}If set, indicates that the token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token's TTL will be set to the value of this field. The maximum
allowed lifetime of token issued using this role. Specified as a number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>resolve_<wbr>aws_<wbr>unique_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether or not Vault should resolve the bound_iam_principal_arn to an AWS Unique ID. When true, deleting a principal and
recreating it with the same name won't automatically grant the new principal the same roles in Vault that the old
principal had.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role_<wbr>tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The key of the tag on EC2 instance to use for role tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>bound_<wbr>cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>explicit_<wbr>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>no_<wbr>default_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>num_<wbr>uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The TTL period of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}








## Look up an Existing AuthBackendRole Resource

Get an existing AuthBackendRole resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/aws/#AuthBackendRoleState">AuthBackendRoleState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vault/aws/#AuthBackendRole">AuthBackendRole</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>allow_instance_migration=None<span class="p">, </span>auth_type=None<span class="p">, </span>backend=None<span class="p">, </span>bound_account_ids=None<span class="p">, </span>bound_ami_ids=None<span class="p">, </span>bound_ec2_instance_ids=None<span class="p">, </span>bound_iam_instance_profile_arns=None<span class="p">, </span>bound_iam_principal_arns=None<span class="p">, </span>bound_iam_role_arns=None<span class="p">, </span>bound_regions=None<span class="p">, </span>bound_subnet_ids=None<span class="p">, </span>bound_vpc_ids=None<span class="p">, </span>disallow_reauthentication=None<span class="p">, </span>inferred_aws_region=None<span class="p">, </span>inferred_entity_type=None<span class="p">, </span>max_ttl=None<span class="p">, </span>period=None<span class="p">, </span>policies=None<span class="p">, </span>resolve_aws_unique_ids=None<span class="p">, </span>role=None<span class="p">, </span>role_tag=None<span class="p">, </span>token_bound_cidrs=None<span class="p">, </span>token_explicit_max_ttl=None<span class="p">, </span>token_max_ttl=None<span class="p">, </span>token_no_default_policy=None<span class="p">, </span>token_num_uses=None<span class="p">, </span>token_period=None<span class="p">, </span>token_policies=None<span class="p">, </span>token_ttl=None<span class="p">, </span>token_type=None<span class="p">, </span>ttl=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetAuthBackendRole<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/aws?tab=doc#AuthBackendRoleState">AuthBackendRoleState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vault/sdk/go/vault/aws?tab=doc#AuthBackendRole">AuthBackendRole</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.Aws.AuthBackendRole.html">AuthBackendRole</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vault/Pulumi.Vault.Aws.AuthBackendRoleState.html">AuthBackendRoleState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Allow<wbr>Instance<wbr>Migration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When true, allows migration of the underlying instance where the client resides. Use with caution.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The auth type permitted for this role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Account<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances with this account ID in their identity document will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Ami<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances using this AMI ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Ec2Instance<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this instance ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Iam<wbr>Instance<wbr>Profile<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with an IAM instance profile ARN that matches this value will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Iam<wbr>Principal<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The IAM principal that must be authenticated using the iam auth method.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Iam<wbr>Role<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this IAM role ARN will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances in this region will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this subnet ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Vpc<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this VPC ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disallow<wbr>Reauthentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When true, only allows a single token to be granted per instance ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inferred<wbr>Aws<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region to search for the inferred entities in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inferred<wbr>Entity<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of inferencing Vault should do.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed lifetime of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}If set, indicates that the token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token's TTL will be set to the value of this field. The maximum
allowed lifetime of token issued using this role. Specified as a number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resolve<wbr>Aws<wbr>Unique<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether or not Vault should resolve the bound_iam_principal_arn to an AWS Unique ID. When true, deleting a principal and
recreating it with the same name won't automatically grant the new principal the same roles in Vault that the old
principal had.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key of the tag on EC2 instance to use for role tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The TTL period of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Instance<wbr>Migration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When true, allows migration of the underlying instance where the client resides. Use with caution.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The auth type permitted for this role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Account<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances with this account ID in their identity document will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Ami<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances using this AMI ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Ec2Instance<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this instance ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Iam<wbr>Instance<wbr>Profile<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with an IAM instance profile ARN that matches this value will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Iam<wbr>Principal<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The IAM principal that must be authenticated using the iam auth method.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Iam<wbr>Role<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this IAM role ARN will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances in this region will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this subnet ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bound<wbr>Vpc<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this VPC ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disallow<wbr>Reauthentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When true, only allows a single token to be granted per instance ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inferred<wbr>Aws<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region to search for the inferred entities in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inferred<wbr>Entity<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of inferencing Vault should do.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed lifetime of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}If set, indicates that the token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token's TTL will be set to the value of this field. The maximum
allowed lifetime of token issued using this role. Specified as a number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resolve<wbr>Aws<wbr>Unique<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether or not Vault should resolve the bound_iam_principal_arn to an AWS Unique ID. When true, deleting a principal and
recreating it with the same name won't automatically grant the new principal the same roles in Vault that the old
principal had.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The key of the tag on EC2 instance to use for role tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The TTL period of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Instance<wbr>Migration</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When true, allows migration of the underlying instance where the client resides. Use with caution.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auth<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The auth type permitted for this role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Account<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances with this account ID in their identity document will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Ami<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances using this AMI ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Ec2Instance<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this instance ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Iam<wbr>Instance<wbr>Profile<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with an IAM instance profile ARN that matches this value will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Iam<wbr>Principal<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The IAM principal that must be authenticated using the iam auth method.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Iam<wbr>Role<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this IAM role ARN will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances in this region will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this subnet ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound<wbr>Vpc<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this VPC ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disallow<wbr>Reauthentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When true, only allows a single token to be granted per instance ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inferred<wbr>Aws<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region to search for the inferred entities in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inferred<wbr>Entity<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of inferencing Vault should do.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed lifetime of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}If set, indicates that the token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token's TTL will be set to the value of this field. The maximum
allowed lifetime of token issued using this role. Specified as a number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>resolve<wbr>Aws<wbr>Unique<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether or not Vault should resolve the bound_iam_principal_arn to an AWS Unique ID. When true, deleting a principal and
recreating it with the same name won't automatically grant the new principal the same roles in Vault that the old
principal had.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role<wbr>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key of the tag on EC2 instance to use for role tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Bound<wbr>Cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Explicit<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Max<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>No<wbr>Default<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Num<wbr>Uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The TTL period of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>instance_<wbr>migration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, allows migration of the underlying instance where the client resides. Use with caution.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auth_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The auth type permitted for this role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backend</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name of the auth backend to configure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>account_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances with this account ID in their identity document will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>ami_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances using this AMI ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>ec2_<wbr>instance_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this instance ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>iam_<wbr>instance_<wbr>profile_<wbr>arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with an IAM instance profile ARN that matches this value will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>iam_<wbr>principal_<wbr>arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The IAM principal that must be authenticated using the iam auth method.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>iam_<wbr>role_<wbr>arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances that match this IAM role ARN will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances in this region will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>subnet_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this subnet ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bound_<wbr>vpc_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Only EC2 instances associated with this VPC ID will be permitted to log in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disallow_<wbr>reauthentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, only allows a single token to be granted per instance ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inferred_<wbr>aws_<wbr>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region to search for the inferred entities in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inferred_<wbr>entity_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of inferencing Vault should do.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed lifetime of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_max_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}If set, indicates that the token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token's TTL will be set to the value of this field. The maximum
allowed lifetime of token issued using this role. Specified as a number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_period` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Policies to be set on tokens issued using this role.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_policies` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>resolve_<wbr>aws_<wbr>unique_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether or not Vault should resolve the bound_iam_principal_arn to an AWS Unique ID. When true, deleting a principal and
recreating it with the same name won't automatically grant the new principal the same roles in Vault that the old
principal had.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role_<wbr>tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The key of the tag on EC2 instance to use for role tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>bound_<wbr>cidrs</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies the blocks of IP addresses which are allowed to use the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>explicit_<wbr>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Generated Token's Explicit Maximum TTL in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>max_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum lifetime of the generated token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>no_<wbr>default_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, the 'default' policy will not automatically be added to generated tokens
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>num_<wbr>uses</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of times a token may be used, a value of zero means unlimited
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Generated Token's Period
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Generated Token's Policies
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The initial ttl of the token to generate in seconds
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of token to generate, service or batch
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The TTL period of tokens issued using this role, provided as the number of seconds.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use `token_ttl` instead if you are running Vault &gt;= 1.2{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-vault">https://github.com/pulumi/pulumi-vault</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

