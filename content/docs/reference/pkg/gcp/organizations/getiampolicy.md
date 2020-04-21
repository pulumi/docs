
---
title: "GetIAMPolicy"
block_external_search_index: true
---



Generates an IAM policy document that may be referenced by and applied to
other Google Cloud Platform resources, such as the `gcp.organizations.Project` resource.

**Note:** Several restrictions apply when setting IAM policies through this API.
See the [setIamPolicy docs](https://cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy)
for a list of these restrictions.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

const admin = gcp.organizations.getIAMPolicy({
    auditConfigs: [{
        auditLogConfigs: [
            {
                exemptedMembers: ["user:you@domain.com"],
                logType: "DATA_READ",
            },
            {
                logType: "DATA_WRITE",
            },
            {
                logType: "ADMIN_READ",
            },
        ],
        service: "cloudkms.googleapis.com",
    }],
    bindings: [
        {
            members: ["serviceAccount:your-custom-sa@your-project.iam.gserviceaccount.com"],
            role: "roles/compute.instanceAdmin",
        },
        {
            members: ["user:alice@gmail.com"],
            role: "roles/storage.objectViewer",
        },
    ],
});
```

This data source is used to define IAM policies to apply to other resources.
Currently, defining a policy through a datasource and referencing that policy
from another resource is the only way to apply an IAM policy to a resource.





## Using GetIAMPolicy {#using}

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getIAMPolicy<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/organizations/#GetIAMPolicyArgs">GetIAMPolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/organizations/#GetIAMPolicyResult">GetIAMPolicyResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_iam_policy(</span>audit_configs=None<span class="p">, </span>bindings=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupIAMPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/organizations?tab=doc#LookupIAMPolicyArgs">LookupIAMPolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/organizations?tab=doc#LookupIAMPolicyResult">LookupIAMPolicyResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetIAMPolicy </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Organizations.GetIAMPolicyResult.html">GetIAMPolicyResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Organizations.GetIAMPolicyArgs.html">GetIAMPolicyArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Audit<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicyauditconfig">List&lt;Get<wbr>IAMPolicy<wbr>Audit<wbr>Config<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block that defines logging additional configuration for your project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bindings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicybinding">List&lt;Get<wbr>IAMPolicy<wbr>Binding<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block (described below)
defining a binding to be included in the policy document. Multiple
`binding` arguments are supported.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Audit<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicyauditconfig">[]Get<wbr>IAMPolicy<wbr>Audit<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block that defines logging additional configuration for your project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bindings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicybinding">[]Get<wbr>IAMPolicy<wbr>Binding</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block (described below)
defining a binding to be included in the policy document. Multiple
`binding` arguments are supported.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>audit<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicyauditconfig">Get<wbr>IAMPolicy<wbr>Audit<wbr>Config[]</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block that defines logging additional configuration for your project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bindings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicybinding">Get<wbr>IAMPolicy<wbr>Binding[]</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block (described below)
defining a binding to be included in the policy document. Multiple
`binding` arguments are supported.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>audit_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicyauditconfig">List[Get<wbr>IAMPolicy<wbr>Audit<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block that defines logging additional configuration for your project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bindings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicybinding">List[Get<wbr>IAMPolicy<wbr>Binding]</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block (described below)
defining a binding to be included in the policy document. Multiple
`binding` arguments are supported.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetIAMPolicy Result {#result}

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Policy<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The above bindings serialized in a format suitable for
referencing from a resource that supports IAM.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Audit<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicyauditconfig">List&lt;Get<wbr>IAMPolicy<wbr>Audit<wbr>Config&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bindings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicybinding">List&lt;Get<wbr>IAMPolicy<wbr>Binding&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Policy<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The above bindings serialized in a format suitable for
referencing from a resource that supports IAM.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Audit<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicyauditconfig">[]Get<wbr>IAMPolicy<wbr>Audit<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bindings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicybinding">[]Get<wbr>IAMPolicy<wbr>Binding</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>policy<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The above bindings serialized in a format suitable for
referencing from a resource that supports IAM.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>audit<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicyauditconfig">Get<wbr>IAMPolicy<wbr>Audit<wbr>Config[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bindings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicybinding">Get<wbr>IAMPolicy<wbr>Binding[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>policy_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The above bindings serialized in a format suitable for
referencing from a resource that supports IAM.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>audit_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicyauditconfig">List[Get<wbr>IAMPolicy<wbr>Audit<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bindings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicybinding">List[Get<wbr>IAMPolicy<wbr>Binding]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types


<h4 id="getiampolicyauditconfig">Get<wbr>IAMPolicy<wbr>Audit<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#GetIAMPolicyAuditConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetIAMPolicyAuditConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/organizations?tab=doc#GetIAMPolicyAuditConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/organizations?tab=doc#GetIAMPolicyAuditConfig">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Audit<wbr>Log<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicyauditconfigauditlogconfig">List&lt;Get<wbr>IAMPolicy<wbr>Audit<wbr>Config<wbr>Audit<wbr>Log<wbr>Config<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A nested block that defines the operations you'd like to log.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Defines a service that will be enabled for audit logging. For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Audit<wbr>Log<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicyauditconfigauditlogconfig">[]Get<wbr>IAMPolicy<wbr>Audit<wbr>Config<wbr>Audit<wbr>Log<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A nested block that defines the operations you'd like to log.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Defines a service that will be enabled for audit logging. For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>audit<wbr>Log<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicyauditconfigauditlogconfig">Get<wbr>IAMPolicy<wbr>Audit<wbr>Config<wbr>Audit<wbr>Log<wbr>Config[]</a></span>
    </dt>
    <dd>{{% md %}}A nested block that defines the operations you'd like to log.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Defines a service that will be enabled for audit logging. For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>audit_<wbr>log_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicyauditconfigauditlogconfig">List[Get<wbr>IAMPolicy<wbr>Audit<wbr>Config<wbr>Audit<wbr>Log<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A nested block that defines the operations you'd like to log.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Defines a service that will be enabled for audit logging. For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getiampolicyauditconfigauditlogconfig">Get<wbr>IAMPolicy<wbr>Audit<wbr>Config<wbr>Audit<wbr>Log<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#GetIAMPolicyAuditConfigAuditLogConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetIAMPolicyAuditConfigAuditLogConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/organizations?tab=doc#GetIAMPolicyAuditConfigAuditLogConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/organizations?tab=doc#GetIAMPolicyAuditConfigAuditLogConfig">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Log<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Defines the logging level. `DATA_READ`, `DATA_WRITE` and `ADMIN_READ` capture different types of events. See [the audit configuration documentation](https://cloud.google.com/resource-manager/reference/rest/Shared.Types/AuditConfig) for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Exempted<wbr>Members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}Specifies the identities that are exempt from these types of logging operations. Follows the same format of the `members` array for `binding`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Log<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Defines the logging level. `DATA_READ`, `DATA_WRITE` and `ADMIN_READ` capture different types of events. See [the audit configuration documentation](https://cloud.google.com/resource-manager/reference/rest/Shared.Types/AuditConfig) for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Exempted<wbr>Members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the identities that are exempt from these types of logging operations. Follows the same format of the `members` array for `binding`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>log<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Defines the logging level. `DATA_READ`, `DATA_WRITE` and `ADMIN_READ` capture different types of events. See [the audit configuration documentation](https://cloud.google.com/resource-manager/reference/rest/Shared.Types/AuditConfig) for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>exempted<wbr>Members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}Specifies the identities that are exempt from these types of logging operations. Follows the same format of the `members` array for `binding`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>log<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Defines the logging level. `DATA_READ`, `DATA_WRITE` and `ADMIN_READ` capture different types of events. See [the audit configuration documentation](https://cloud.google.com/resource-manager/reference/rest/Shared.Types/AuditConfig) for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>exempted<wbr>Members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}Specifies the identities that are exempt from these types of logging operations. Follows the same format of the `members` array for `binding`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getiampolicybinding">Get<wbr>IAMPolicy<wbr>Binding</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#GetIAMPolicyBinding">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetIAMPolicyBinding">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/organizations?tab=doc#GetIAMPolicyBindingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/organizations?tab=doc#GetIAMPolicyBinding">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}An array of identities that will be granted the privilege in the `role`. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding
Each entry can have one of the following values:
* **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account. It **can't** be used with the `gcp.organizations.Project` resource.
* **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account. It **can't** be used with the `gcp.organizations.Project` resource.
* **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com.
* **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
* **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
* **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The role/permission that will be granted to the members.
See the [IAM Roles](https://cloud.google.com/compute/docs/access/iam) documentation for a complete list of roles.
Note that custom roles must be of the format `[projects|organizations]/{parent-name}/roles/{role-name}`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Condition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicybindingcondition">Get<wbr>IAMPolicy<wbr>Binding<wbr>Condition<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}An array of identities that will be granted the privilege in the `role`. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding
Each entry can have one of the following values:
* **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account. It **can't** be used with the `gcp.organizations.Project` resource.
* **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account. It **can't** be used with the `gcp.organizations.Project` resource.
* **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com.
* **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
* **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
* **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The role/permission that will be granted to the members.
See the [IAM Roles](https://cloud.google.com/compute/docs/access/iam) documentation for a complete list of roles.
Note that custom roles must be of the format `[projects|organizations]/{parent-name}/roles/{role-name}`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Condition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicybindingcondition">Get<wbr>IAMPolicy<wbr>Binding<wbr>Condition</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}An array of identities that will be granted the privilege in the `role`. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding
Each entry can have one of the following values:
* **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account. It **can't** be used with the `gcp.organizations.Project` resource.
* **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account. It **can't** be used with the `gcp.organizations.Project` resource.
* **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com.
* **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
* **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
* **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The role/permission that will be granted to the members.
See the [IAM Roles](https://cloud.google.com/compute/docs/access/iam) documentation for a complete list of roles.
Note that custom roles must be of the format `[projects|organizations]/{parent-name}/roles/{role-name}`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>condition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicybindingcondition">Get<wbr>IAMPolicy<wbr>Binding<wbr>Condition</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}An array of identities that will be granted the privilege in the `role`. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding
Each entry can have one of the following values:
* **allUsers**: A special identifier that represents anyone who is on the internet; with or without a Google account. It **can't** be used with the `gcp.organizations.Project` resource.
* **allAuthenticatedUsers**: A special identifier that represents anyone who is authenticated with a Google account or a service account. It **can't** be used with the `gcp.organizations.Project` resource.
* **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com.
* **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
* **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
* **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The role/permission that will be granted to the members.
See the [IAM Roles](https://cloud.google.com/compute/docs/access/iam) documentation for a complete list of roles.
Note that custom roles must be of the format `[projects|organizations]/{parent-name}/roles/{role-name}`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>condition</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getiampolicybindingcondition">Dict[Get<wbr>IAMPolicy<wbr>Binding<wbr>Condition]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getiampolicybindingcondition">Get<wbr>IAMPolicy<wbr>Binding<wbr>Condition</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#GetIAMPolicyBindingCondition">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GetIAMPolicyBindingCondition">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/organizations?tab=doc#GetIAMPolicyBindingConditionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/organizations?tab=doc#GetIAMPolicyBindingCondition">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Expression</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Title</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Expression</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Title</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>expression</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>title</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>expression</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>title</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}







