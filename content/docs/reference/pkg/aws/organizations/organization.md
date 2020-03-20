
---
title: "Organization"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides a resource to create an organization.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const org = new aws.organizations.Organization("org", {
    awsServiceAccessPrincipals: [
        "cloudtrail.amazonaws.com",
        "config.amazonaws.com",
    ],
    featureSet: "ALL",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/organizations_organization.html.markdown.



## Create a Organization Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/organizations/#Organization">Organization</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/organizations/#OrganizationArgs">OrganizationArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Organization</span><span class="p">(resource_name, opts=None, </span>aws_service_access_principals=None<span class="p">, </span>enabled_policy_types=None<span class="p">, </span>feature_set=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewOrganization<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/organizations?tab=doc#OrganizationArgs">OrganizationArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/organizations?tab=doc#Organization">Organization</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Organizations.Organization.html">Organization</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Organizations.OrganizationArgs.html">OrganizationArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Organization resource with the given unique name, arguments, and options.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Aws<wbr>Service<wbr>Access<wbr>Principals</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Policy<wbr>Types</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY` and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Feature<wbr>Set</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify &#34;ALL&#34; (default) or &#34;CONSOLIDATED_BILLING&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Aws<wbr>Service<wbr>Access<wbr>Principals</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Policy<wbr>Types</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY` and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Feature<wbr>Set</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify &#34;ALL&#34; (default) or &#34;CONSOLIDATED_BILLING&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">aws<wbr>Service<wbr>Access<wbr>Principals</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled<wbr>Policy<wbr>Types</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY` and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">feature<wbr>Set</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify &#34;ALL&#34; (default) or &#34;CONSOLIDATED_BILLING&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">aws_<wbr>service_<wbr>access_<wbr>principals</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled_<wbr>policy_<wbr>types</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY` and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">feature_<wbr>set</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify &#34;ALL&#34; (default) or &#34;CONSOLIDATED_BILLING&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Organization Output Properties

The following output properties are available:



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Accounts</td>
            <td class="align-top">
                
                <code><a href="#organizationaccount">List&lt;Pulumi.<wbr>Aws.<wbr>Organizations.<wbr>Organization<wbr>Account&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} List of organization accounts including the master account. For a list excluding the master account, see the `non_master_accounts` attribute. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Aws<wbr>Service<wbr>Access<wbr>Principals</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Policy<wbr>Types</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY` and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Feature<wbr>Set</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Specify &#34;ALL&#34; (default) or &#34;CONSOLIDATED_BILLING&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Account<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} ARN of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Account<wbr>Email</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Email address of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Identifier of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Non<wbr>Master<wbr>Accounts</td>
            <td class="align-top">
                
                <code><a href="#organizationnonmasteraccount">List&lt;Pulumi.<wbr>Aws.<wbr>Organizations.<wbr>Organization<wbr>Non<wbr>Master<wbr>Account&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} List of organization accounts excluding the master account. For a list including the master account, see the `accounts` attribute. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Roots</td>
            <td class="align-top">
                
                <code><a href="#organizationroot">List&lt;Pulumi.<wbr>Aws.<wbr>Organizations.<wbr>Organization<wbr>Root&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} List of organization roots. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Accounts</td>
            <td class="align-top">
                
                <code><a href="#organizationaccount">[]Organization<wbr>Account</a></code>
            </td>
            <td class="align-top">{{% md %}} List of organization accounts including the master account. For a list excluding the master account, see the `non_master_accounts` attribute. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Aws<wbr>Service<wbr>Access<wbr>Principals</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Policy<wbr>Types</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY` and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Feature<wbr>Set</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Specify &#34;ALL&#34; (default) or &#34;CONSOLIDATED_BILLING&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Account<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} ARN of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Account<wbr>Email</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Email address of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Identifier of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Non<wbr>Master<wbr>Accounts</td>
            <td class="align-top">
                
                <code><a href="#organizationnonmasteraccount">[]Organization<wbr>Non<wbr>Master<wbr>Account</a></code>
            </td>
            <td class="align-top">{{% md %}} List of organization accounts excluding the master account. For a list including the master account, see the `accounts` attribute. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Roots</td>
            <td class="align-top">
                
                <code><a href="#organizationroot">[]Organization<wbr>Root</a></code>
            </td>
            <td class="align-top">{{% md %}} List of organization roots. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">accounts</td>
            <td class="align-top">
                
                <code><a href="#organizationaccount">organizations.<wbr>Organization<wbr>Account[]</a></code>
            </td>
            <td class="align-top">{{% md %}} List of organization accounts including the master account. For a list excluding the master account, see the `non_master_accounts` attribute. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">aws<wbr>Service<wbr>Access<wbr>Principals</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled<wbr>Policy<wbr>Types</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY` and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">feature<wbr>Set</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Specify &#34;ALL&#34; (default) or &#34;CONSOLIDATED_BILLING&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master<wbr>Account<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} ARN of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master<wbr>Account<wbr>Email</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Email address of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Identifier of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">non<wbr>Master<wbr>Accounts</td>
            <td class="align-top">
                
                <code><a href="#organizationnonmasteraccount">organizations.<wbr>Organization<wbr>Non<wbr>Master<wbr>Account[]</a></code>
            </td>
            <td class="align-top">{{% md %}} List of organization accounts excluding the master account. For a list including the master account, see the `accounts` attribute. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">roots</td>
            <td class="align-top">
                
                <code><a href="#organizationroot">organizations.<wbr>Organization<wbr>Root[]</a></code>
            </td>
            <td class="align-top">{{% md %}} List of organization roots. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">accounts</td>
            <td class="align-top">
                
                <code><a href="#organizationaccount">List[Organization<wbr>Account]</a></code>
            </td>
            <td class="align-top">{{% md %}} List of organization accounts including the master account. For a list excluding the master account, see the `non_master_accounts` attribute. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">aws_<wbr>service_<wbr>access_<wbr>principals</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled_<wbr>policy_<wbr>types</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY` and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">feature_<wbr>set</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Specify &#34;ALL&#34; (default) or &#34;CONSOLIDATED_BILLING&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master_<wbr>account_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} ARN of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master_<wbr>account_<wbr>email</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Email address of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master_<wbr>account_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Identifier of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">non_<wbr>master_<wbr>accounts</td>
            <td class="align-top">
                
                <code><a href="#organizationnonmasteraccount">List[Organization<wbr>Non<wbr>Master<wbr>Account]</a></code>
            </td>
            <td class="align-top">{{% md %}} List of organization accounts excluding the master account. For a list including the master account, see the `accounts` attribute. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">roots</td>
            <td class="align-top">
                
                <code><a href="#organizationroot">List[Organization<wbr>Root]</a></code>
            </td>
            <td class="align-top">{{% md %}} List of organization roots. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Organization Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/organizations/#OrganizationState">OrganizationState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/organizations/#Organization">Organization</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>accounts=None<span class="p">, </span>arn=None<span class="p">, </span>aws_service_access_principals=None<span class="p">, </span>enabled_policy_types=None<span class="p">, </span>feature_set=None<span class="p">, </span>master_account_arn=None<span class="p">, </span>master_account_email=None<span class="p">, </span>master_account_id=None<span class="p">, </span>non_master_accounts=None<span class="p">, </span>roots=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetOrganization<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/organizations?tab=doc#OrganizationState">OrganizationState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/organizations?tab=doc#Organization">Organization</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Organizations.Organization.html">Organization</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Organizations.OrganizationState.html">OrganizationState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Organization resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following state arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Accounts</td>
            <td class="align-top">
                
                <code><a href="#organizationaccount">List&lt;Pulumi.<wbr>Aws.<wbr>Organizations.<wbr>Organization<wbr>Account<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of organization accounts including the master account. For a list excluding the master account, see the `non_master_accounts` attribute. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Aws<wbr>Service<wbr>Access<wbr>Principals</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Policy<wbr>Types</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY` and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Feature<wbr>Set</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify &#34;ALL&#34; (default) or &#34;CONSOLIDATED_BILLING&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Account<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Account<wbr>Email</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Email address of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Non<wbr>Master<wbr>Accounts</td>
            <td class="align-top">
                
                <code><a href="#organizationnonmasteraccount">List&lt;Pulumi.<wbr>Aws.<wbr>Organizations.<wbr>Organization<wbr>Non<wbr>Master<wbr>Account<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of organization accounts excluding the master account. For a list including the master account, see the `accounts` attribute. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Roots</td>
            <td class="align-top">
                
                <code><a href="#organizationroot">List&lt;Pulumi.<wbr>Aws.<wbr>Organizations.<wbr>Organization<wbr>Root<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of organization roots. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Accounts</td>
            <td class="align-top">
                
                <code><a href="#organizationaccount">[]Organization<wbr>Account</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of organization accounts including the master account. For a list excluding the master account, see the `non_master_accounts` attribute. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Aws<wbr>Service<wbr>Access<wbr>Principals</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Policy<wbr>Types</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY` and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Feature<wbr>Set</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify &#34;ALL&#34; (default) or &#34;CONSOLIDATED_BILLING&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Account<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Account<wbr>Email</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Email address of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Master<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Non<wbr>Master<wbr>Accounts</td>
            <td class="align-top">
                
                <code><a href="#organizationnonmasteraccount">[]Organization<wbr>Non<wbr>Master<wbr>Account</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of organization accounts excluding the master account. For a list including the master account, see the `accounts` attribute. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Roots</td>
            <td class="align-top">
                
                <code><a href="#organizationroot">[]Organization<wbr>Root</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of organization roots. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">accounts</td>
            <td class="align-top">
                
                <code><a href="#organizationaccount">organizations.<wbr>Organization<wbr>Account[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of organization accounts including the master account. For a list excluding the master account, see the `non_master_accounts` attribute. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">aws<wbr>Service<wbr>Access<wbr>Principals</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled<wbr>Policy<wbr>Types</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY` and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">feature<wbr>Set</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify &#34;ALL&#34; (default) or &#34;CONSOLIDATED_BILLING&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master<wbr>Account<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master<wbr>Account<wbr>Email</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Email address of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master<wbr>Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">non<wbr>Master<wbr>Accounts</td>
            <td class="align-top">
                
                <code><a href="#organizationnonmasteraccount">organizations.<wbr>Organization<wbr>Non<wbr>Master<wbr>Account[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of organization accounts excluding the master account. For a list including the master account, see the `accounts` attribute. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">roots</td>
            <td class="align-top">
                
                <code><a href="#organizationroot">organizations.<wbr>Organization<wbr>Root[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of organization roots. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">accounts</td>
            <td class="align-top">
                
                <code><a href="#organizationaccount">List[Organization<wbr>Account]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of organization accounts including the master account. For a list excluding the master account, see the `non_master_accounts` attribute. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">aws_<wbr>service_<wbr>access_<wbr>principals</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled_<wbr>policy_<wbr>types</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Organizations policy types to enable in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY` and `TAG_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">feature_<wbr>set</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify &#34;ALL&#34; (default) or &#34;CONSOLIDATED_BILLING&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master_<wbr>account_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master_<wbr>account_<wbr>email</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Email address of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">master_<wbr>account_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the master account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">non_<wbr>master_<wbr>accounts</td>
            <td class="align-top">
                
                <code><a href="#organizationnonmasteraccount">List[Organization<wbr>Non<wbr>Master<wbr>Account]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of organization accounts excluding the master account. For a list including the master account, see the `accounts` attribute. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">roots</td>
            <td class="align-top">
                
                <code><a href="#organizationroot">List[Organization<wbr>Root]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of organization roots. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### OrganizationAccount
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#OrganizationAccount">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/organizations?tab=doc#OrganizationAccountOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Organizations.OrganizationAccount.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Email of the account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the policy type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The status of the policy type as it relates to the associated root
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Email of the account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the policy type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The status of the policy type as it relates to the associated root
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Email of the account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the policy type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The status of the policy type as it relates to the associated root
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Email of the account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the policy type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The status of the policy type as it relates to the associated root
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### OrganizationNonMasterAccount
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#OrganizationNonMasterAccount">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/organizations?tab=doc#OrganizationNonMasterAccountOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Organizations.OrganizationNonMasterAccount.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Email of the account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the policy type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The status of the policy type as it relates to the associated root
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Email of the account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the policy type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The status of the policy type as it relates to the associated root
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Email of the account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the policy type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The status of the policy type as it relates to the associated root
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Email of the account
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the policy type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The status of the policy type as it relates to the associated root
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### OrganizationRoot
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#OrganizationRoot">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/organizations?tab=doc#OrganizationRootOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Organizations.OrganizationRoot.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the policy type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy<wbr>Types</td>
            <td class="align-top">
                
                <code><a href="#organizationrootpolicytype">List&lt;Pulumi.<wbr>Aws.<wbr>Organizations.<wbr>Organization<wbr>Root<wbr>Policy<wbr>Type<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of policy types enabled for this root. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the policy type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy<wbr>Types</td>
            <td class="align-top">
                
                <code><a href="#organizationrootpolicytype">[]Organization<wbr>Root<wbr>Policy<wbr>Type</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of policy types enabled for this root. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the policy type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy<wbr>Types</td>
            <td class="align-top">
                
                <code><a href="#organizationrootpolicytype">organizations.<wbr>Organization<wbr>Root<wbr>Policy<wbr>Type[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of policy types enabled for this root. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the policy type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy<wbr>Types</td>
            <td class="align-top">
                
                <code><a href="#organizationrootpolicytype">List[Organization<wbr>Root<wbr>Policy<wbr>Type]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of policy types enabled for this root. All elements have these attributes:
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### OrganizationRootPolicyType
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#OrganizationRootPolicyType">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/organizations?tab=doc#OrganizationRootPolicyTypeOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Organizations.OrganizationRootPolicyType.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The status of the policy type as it relates to the associated root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The status of the policy type as it relates to the associated root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The status of the policy type as it relates to the associated root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The status of the policy type as it relates to the associated root
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







