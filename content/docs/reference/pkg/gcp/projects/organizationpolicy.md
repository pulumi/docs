
---
title: "OrganizationPolicy"
block_external_search_index: true
---

Allows management of Organization policies for a Google Project. For more information see
[the official
documentation](https://cloud.google.com/resource-manager/docs/organization-policy/overview) and
[API](https://cloud.google.com/resource-manager/reference/rest/v1/projects/setOrgPolicy).

## Example Usage

To set policy with a [boolean constraint](https://cloud.google.com/resource-manager/docs/organization-policy/quickstart-boolean-constraints):

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

const serialPortPolicy = new gcp.projects.OrganizationPolicy("serial_port_policy", {
    booleanPolicy: {
        enforced: true,
    },
    constraint: "compute.disableSerialPortAccess",
    project: "your-project-id",
});
```


To set a policy with a [list constraint](https://cloud.google.com/resource-manager/docs/organization-policy/quickstart-list-constraints):

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

const servicesPolicy = new gcp.projects.OrganizationPolicy("services_policy", {
    constraint: "serviceuser.services",
    listPolicy: {
        allow: {
            all: true,
        },
    },
    project: "your-project-id",
});
```


Or to deny some services, use the following instead:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

const servicesPolicy = new gcp.projects.OrganizationPolicy("services_policy", {
    constraint: "serviceuser.services",
    listPolicy: {
        deny: {
            values: ["cloudresourcemanager.googleapis.com"],
        },
        suggestedValue: "compute.googleapis.com",
    },
    project: "your-project-id",
});
```

To restore the default project organization policy, use the following instead:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

const servicesPolicy = new gcp.projects.OrganizationPolicy("services_policy", {
    constraint: "serviceuser.services",
    project: "your-project-id",
    restorePolicy: {
        default: true,
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/google_project_organization_policy.html.markdown.



## Create a OrganizationPolicy Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/projects/#OrganizationPolicy">OrganizationPolicy</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/projects/#OrganizationPolicyArgs">OrganizationPolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">OrganizationPolicy</span><span class="p">(resource_name, opts=None, </span>boolean_policy=None<span class="p">, </span>constraint=None<span class="p">, </span>list_policy=None<span class="p">, </span>project=None<span class="p">, </span>restore_policy=None<span class="p">, </span>version=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewOrganizationPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/projects?tab=doc#OrganizationPolicyArgs">OrganizationPolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/projects?tab=doc#OrganizationPolicy">OrganizationPolicy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Projects.OrganizationPolicy.html">OrganizationPolicy</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Projects.Inputs.OrganizationPolicyArgs.html">OrganizationPolicyArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Boolean<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicybooleanpolicy">Organization<wbr>Policy<wbr>Boolean<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A boolean policy is a constraint that is either enforced or not. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Constraint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>List<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicy">Organization<wbr>Policy<wbr>List<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The project id of the project to set the policy for.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Restore<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicyrestorepolicy">Organization<wbr>Policy<wbr>Restore<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A restore policy is a constraint to restore the default policy. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Version of the Policy. Default version is 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Boolean<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicybooleanpolicy">*Organization<wbr>Policy<wbr>Boolean<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A boolean policy is a constraint that is either enforced or not. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Constraint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>List<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicy">*Organization<wbr>Policy<wbr>List<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The project id of the project to set the policy for.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Restore<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicyrestorepolicy">*Organization<wbr>Policy<wbr>Restore<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A restore policy is a constraint to restore the default policy. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Version of the Policy. Default version is 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>boolean<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicybooleanpolicy">Organization<wbr>Policy<wbr>Boolean<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A boolean policy is a constraint that is either enforced or not. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>constraint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>list<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicy">Organization<wbr>Policy<wbr>List<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The project id of the project to set the policy for.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>restore<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicyrestorepolicy">Organization<wbr>Policy<wbr>Restore<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A restore policy is a constraint to restore the default policy. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Version of the Policy. Default version is 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>boolean_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicybooleanpolicy">Dict[Organization<wbr>Policy<wbr>Boolean<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A boolean policy is a constraint that is either enforced or not. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>constraint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>list_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicy">Dict[Organization<wbr>Policy<wbr>List<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The project id of the project to set the policy for.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>restore_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicyrestorepolicy">Dict[Organization<wbr>Policy<wbr>Restore<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A restore policy is a constraint to restore the default policy. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Version of the Policy. Default version is 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## OrganizationPolicy Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Boolean<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicybooleanpolicy">Organization<wbr>Policy<wbr>Boolean<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A boolean policy is a constraint that is either enforced or not. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Constraint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>List<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicy">Organization<wbr>Policy<wbr>List<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The project id of the project to set the policy for.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Restore<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicyrestorepolicy">Organization<wbr>Policy<wbr>Restore<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A restore policy is a constraint to restore the default policy. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Update<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Version of the Policy. Default version is 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Boolean<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicybooleanpolicy">*Organization<wbr>Policy<wbr>Boolean<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A boolean policy is a constraint that is either enforced or not. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Constraint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>List<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicy">*Organization<wbr>Policy<wbr>List<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The project id of the project to set the policy for.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Restore<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicyrestorepolicy">*Organization<wbr>Policy<wbr>Restore<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A restore policy is a constraint to restore the default policy. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Update<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Version of the Policy. Default version is 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>boolean<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicybooleanpolicy">Organization<wbr>Policy<wbr>Boolean<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A boolean policy is a constraint that is either enforced or not. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>constraint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>list<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicy">Organization<wbr>Policy<wbr>List<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The project id of the project to set the policy for.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>restore<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicyrestorepolicy">Organization<wbr>Policy<wbr>Restore<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A restore policy is a constraint to restore the default policy. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>update<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Version of the Policy. Default version is 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>boolean_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicybooleanpolicy">Dict[Organization<wbr>Policy<wbr>Boolean<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A boolean policy is a constraint that is either enforced or not. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>constraint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>list_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicy">Dict[Organization<wbr>Policy<wbr>List<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The project id of the project to set the policy for.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>restore_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicyrestorepolicy">Dict[Organization<wbr>Policy<wbr>Restore<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A restore policy is a constraint to restore the default policy. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>update_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Version of the Policy. Default version is 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing OrganizationPolicy Resource

Get an existing OrganizationPolicy resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/projects/#OrganizationPolicyState">OrganizationPolicyState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/projects/#OrganizationPolicy">OrganizationPolicy</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>boolean_policy=None<span class="p">, </span>constraint=None<span class="p">, </span>etag=None<span class="p">, </span>list_policy=None<span class="p">, </span>project=None<span class="p">, </span>restore_policy=None<span class="p">, </span>update_time=None<span class="p">, </span>version=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetOrganizationPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/projects?tab=doc#OrganizationPolicyState">OrganizationPolicyState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/projects?tab=doc#OrganizationPolicy">OrganizationPolicy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Projects.OrganizationPolicy.html">OrganizationPolicy</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Projects.OrganizationPolicyState.html">OrganizationPolicyState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Boolean<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicybooleanpolicy">Organization<wbr>Policy<wbr>Boolean<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A boolean policy is a constraint that is either enforced or not. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Constraint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>List<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicy">Organization<wbr>Policy<wbr>List<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The project id of the project to set the policy for.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Restore<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicyrestorepolicy">Organization<wbr>Policy<wbr>Restore<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A restore policy is a constraint to restore the default policy. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Update<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Version of the Policy. Default version is 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Boolean<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicybooleanpolicy">*Organization<wbr>Policy<wbr>Boolean<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A boolean policy is a constraint that is either enforced or not. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Constraint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}(Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>List<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicy">*Organization<wbr>Policy<wbr>List<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The project id of the project to set the policy for.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Restore<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicyrestorepolicy">*Organization<wbr>Policy<wbr>Restore<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A restore policy is a constraint to restore the default policy. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Update<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}(Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Version of the Policy. Default version is 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>boolean<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicybooleanpolicy">Organization<wbr>Policy<wbr>Boolean<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A boolean policy is a constraint that is either enforced or not. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>constraint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>list<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicy">Organization<wbr>Policy<wbr>List<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The project id of the project to set the policy for.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>restore<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicyrestorepolicy">Organization<wbr>Policy<wbr>Restore<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A restore policy is a constraint to restore the default policy. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>update<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Version of the Policy. Default version is 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>boolean_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicybooleanpolicy">Dict[Organization<wbr>Policy<wbr>Boolean<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A boolean policy is a constraint that is either enforced or not. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>constraint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Constraint the Policy is configuring, for example, `serviceuser.services`. Check out the [complete list of available constraints](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(Computed) The etag of the organization policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>list_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicy">Dict[Organization<wbr>Policy<wbr>List<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The project id of the project to set the policy for.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>restore_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicyrestorepolicy">Dict[Organization<wbr>Policy<wbr>Restore<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A restore policy is a constraint to restore the default policy. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>update_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(Computed) The timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds, representing when the variable was last updated. Example: "2016-10-09T12:33:37.578138407Z".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Version of the Policy. Default version is 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Organization<wbr>Policy<wbr>Boolean<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#OrganizationPolicyBooleanPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#OrganizationPolicyBooleanPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/projects?tab=doc#OrganizationPolicyBooleanPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/projects?tab=doc#OrganizationPolicyBooleanPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enforced</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, then the Policy is enforced. If false, then any configuration is acceptable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enforced</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, then the Policy is enforced. If false, then any configuration is acceptable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enforced</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If true, then the Policy is enforced. If false, then any configuration is acceptable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enforced</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, then the Policy is enforced. If false, then any configuration is acceptable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Organization<wbr>Policy<wbr>List<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#OrganizationPolicyListPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#OrganizationPolicyListPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/projects?tab=doc#OrganizationPolicyListPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/projects?tab=doc#OrganizationPolicyListPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicyallow">Organization<wbr>Policy<wbr>List<wbr>Policy<wbr>Allow<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deny</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicydeny">Organization<wbr>Policy<wbr>List<wbr>Policy<wbr>Deny<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inherit<wbr>From<wbr>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If set to true, the values from the effective Policy of the parent resource
are inherited, meaning the values set in this Policy are added to the values inherited up the hierarchy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Suggested<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Google Cloud Console will try to default to a configuration that matches the value specified in this field.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicyallow">*Organization<wbr>Policy<wbr>List<wbr>Policy<wbr>Allow</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deny</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicydeny">*Organization<wbr>Policy<wbr>List<wbr>Policy<wbr>Deny</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inherit<wbr>From<wbr>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If set to true, the values from the effective Policy of the parent resource
are inherited, meaning the values set in this Policy are added to the values inherited up the hierarchy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Suggested<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Google Cloud Console will try to default to a configuration that matches the value specified in this field.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicyallow">Organization<wbr>Policy<wbr>List<wbr>Policy<wbr>Allow?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deny</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicydeny">Organization<wbr>Policy<wbr>List<wbr>Policy<wbr>Deny?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inherit<wbr>From<wbr>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If set to true, the values from the effective Policy of the parent resource
are inherited, meaning the values set in this Policy are added to the values inherited up the hierarchy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>suggested<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Google Cloud Console will try to default to a configuration that matches the value specified in this field.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicyallow">Dict[Organization<wbr>Policy<wbr>List<wbr>Policy<wbr>Allow]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deny</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#organizationpolicylistpolicydeny">Dict[Organization<wbr>Policy<wbr>List<wbr>Policy<wbr>Deny]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inherit<wbr>From<wbr>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If set to true, the values from the effective Policy of the parent resource
are inherited, meaning the values set in this Policy are added to the values inherited up the hierarchy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>suggested<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Google Cloud Console will try to default to a configuration that matches the value specified in this field.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Organization<wbr>Policy<wbr>List<wbr>Policy<wbr>Allow</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#OrganizationPolicyListPolicyAllow">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#OrganizationPolicyListPolicyAllow">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/projects?tab=doc#OrganizationPolicyListPolicyAllowArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/projects?tab=doc#OrganizationPolicyListPolicyAllowOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>All</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}The policy allows or denies all values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The policy can define specific values that are allowed or denied.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>All</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}The policy allows or denies all values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The policy can define specific values that are allowed or denied.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>all</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}The policy allows or denies all values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The policy can define specific values that are allowed or denied.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>all</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The policy allows or denies all values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The policy can define specific values that are allowed or denied.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Organization<wbr>Policy<wbr>List<wbr>Policy<wbr>Deny</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#OrganizationPolicyListPolicyDeny">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#OrganizationPolicyListPolicyDeny">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/projects?tab=doc#OrganizationPolicyListPolicyDenyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/projects?tab=doc#OrganizationPolicyListPolicyDenyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>All</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}The policy allows or denies all values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The policy can define specific values that are allowed or denied.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>All</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}The policy allows or denies all values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The policy can define specific values that are allowed or denied.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>all</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}The policy allows or denies all values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The policy can define specific values that are allowed or denied.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>all</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The policy allows or denies all values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The policy can define specific values that are allowed or denied.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Organization<wbr>Policy<wbr>Restore<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#OrganizationPolicyRestorePolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#OrganizationPolicyRestorePolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/projects?tab=doc#OrganizationPolicyRestorePolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/projects?tab=doc#OrganizationPolicyRestorePolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}May only be set to true. If set, then the default Policy is restored.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}May only be set to true. If set, then the default Policy is restored.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>default</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}May only be set to true. If set, then the default Policy is restored.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}May only be set to true. If set, then the default Policy is restored.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







