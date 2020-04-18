
---
title: "GetDomain"
block_external_search_index: true
---



Use this data source to get information about an Elasticsearch Domain

{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const myDomain = pulumi.output(aws.elasticsearch.getDomain({
    domainName: "my-domain-name",
}, { async: true }));
```

{{% /example %}}
{{% /examples %}}





## Using GetDomain

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getDomain<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elasticsearch/#GetDomainArgs">GetDomainArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elasticsearch/#GetDomainResult">GetDomainResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_domain(</span>domain_name=None<span class="p">, </span>tags=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupDomain<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/v2/go/aws/elasticsearch?tab=doc#LookupDomainArgs">LookupDomainArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/v2/go/aws/elasticsearch?tab=doc#LookupDomainResult">LookupDomainResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetDomain </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.GetDomainResult.html">GetDomainResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.ElasticSearch.GetDomainArgs.html">GetDomainArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the domain.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;</span>
    </dt>
    <dd>{{% md %}}The tags assigned to the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the domain.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}The tags assigned to the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the domain.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}The tags assigned to the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>domain_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Name of the domain.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}The tags assigned to the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetDomain Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Access<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The policy document attached to the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Advanced<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;</span>
    </dt>
    <dd>{{% md %}}Key-value string pairs to specify advanced configuration options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainclusterconfig">List&lt;Get<wbr>Domain<wbr>Cluster<wbr>Config&gt;</a></span>
    </dt>
    <dd>{{% md %}}Cluster configuration of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cognito<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomaincognitooption">List&lt;Get<wbr>Domain<wbr>Cognito<wbr>Option&gt;</a></span>
    </dt>
    <dd>{{% md %}}Domain Amazon Cognito Authentication options for Kibana.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Status of the creation of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Deleted</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Status of the deletion of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Domain<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Unique identifier for the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ebs<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainebsoption">List&lt;Get<wbr>Domain<wbr>Ebs<wbr>Option&gt;</a></span>
    </dt>
    <dd>{{% md %}}EBS Options for the instances in the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Elasticsearch<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}ElasticSearch version for the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Encryption<wbr>At<wbr>Rests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainencryptionatrest">List&lt;Get<wbr>Domain<wbr>Encryption<wbr>At<wbr>Rest&gt;</a></span>
    </dt>
    <dd>{{% md %}}Domain encryption at rest related options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Domain-specific endpoint used to submit index, search, and data upload requests.
{{% /md %}}</dd>

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
        <span>Kibana<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Domain-specific endpoint used to access the Kibana application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Log<wbr>Publishing<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainlogpublishingoption">List&lt;Get<wbr>Domain<wbr>Log<wbr>Publishing<wbr>Option&gt;</a></span>
    </dt>
    <dd>{{% md %}}Domain log publishing related options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>To<wbr>Node<wbr>Encryptions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainnodetonodeencryption">List&lt;Get<wbr>Domain<wbr>Node<wbr>To<wbr>Node<wbr>Encryption&gt;</a></span>
    </dt>
    <dd>{{% md %}}Domain in transit encryption related options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Processing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Status of a configuration change in the domain.
* `snapshot_options` – Domain snapshot related options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Snapshot<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainsnapshotoption">List&lt;Get<wbr>Domain<wbr>Snapshot<wbr>Option&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;</span>
    </dt>
    <dd>{{% md %}}The tags assigned to the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainvpcoption">List&lt;Get<wbr>Domain<wbr>Vpc<wbr>Option&gt;</a></span>
    </dt>
    <dd>{{% md %}}VPC Options for private Elasticsearch domains.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Access<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The policy document attached to the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Advanced<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Key-value string pairs to specify advanced configuration options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainclusterconfig">[]Get<wbr>Domain<wbr>Cluster<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Cluster configuration of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cognito<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomaincognitooption">[]Get<wbr>Domain<wbr>Cognito<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}Domain Amazon Cognito Authentication options for Kibana.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Status of the creation of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Deleted</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Status of the deletion of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Domain<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Unique identifier for the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ebs<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainebsoption">[]Get<wbr>Domain<wbr>Ebs<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}EBS Options for the instances in the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Elasticsearch<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}ElasticSearch version for the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Encryption<wbr>At<wbr>Rests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainencryptionatrest">[]Get<wbr>Domain<wbr>Encryption<wbr>At<wbr>Rest</a></span>
    </dt>
    <dd>{{% md %}}Domain encryption at rest related options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Domain-specific endpoint used to submit index, search, and data upload requests.
{{% /md %}}</dd>

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
        <span>Kibana<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Domain-specific endpoint used to access the Kibana application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Log<wbr>Publishing<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainlogpublishingoption">[]Get<wbr>Domain<wbr>Log<wbr>Publishing<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}Domain log publishing related options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>To<wbr>Node<wbr>Encryptions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainnodetonodeencryption">[]Get<wbr>Domain<wbr>Node<wbr>To<wbr>Node<wbr>Encryption</a></span>
    </dt>
    <dd>{{% md %}}Domain in transit encryption related options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Processing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Status of a configuration change in the domain.
* `snapshot_options` – Domain snapshot related options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Snapshot<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainsnapshotoption">[]Get<wbr>Domain<wbr>Snapshot<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}The tags assigned to the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainvpcoption">[]Get<wbr>Domain<wbr>Vpc<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}VPC Options for private Elasticsearch domains.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>access<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The policy document attached to the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>advanced<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}Key-value string pairs to specify advanced configuration options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cluster<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainclusterconfig">Get<wbr>Domain<wbr>Cluster<wbr>Config[]</a></span>
    </dt>
    <dd>{{% md %}}Cluster configuration of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cognito<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomaincognitooption">Get<wbr>Domain<wbr>Cognito<wbr>Option[]</a></span>
    </dt>
    <dd>{{% md %}}Domain Amazon Cognito Authentication options for Kibana.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Status of the creation of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>deleted</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Status of the deletion of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>domain<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Unique identifier for the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ebs<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainebsoption">Get<wbr>Domain<wbr>Ebs<wbr>Option[]</a></span>
    </dt>
    <dd>{{% md %}}EBS Options for the instances in the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>elasticsearch<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}ElasticSearch version for the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>encryption<wbr>At<wbr>Rests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainencryptionatrest">Get<wbr>Domain<wbr>Encryption<wbr>At<wbr>Rest[]</a></span>
    </dt>
    <dd>{{% md %}}Domain encryption at rest related options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Domain-specific endpoint used to submit index, search, and data upload requests.
{{% /md %}}</dd>

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
        <span>kibana<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Domain-specific endpoint used to access the Kibana application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>log<wbr>Publishing<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainlogpublishingoption">Get<wbr>Domain<wbr>Log<wbr>Publishing<wbr>Option[]</a></span>
    </dt>
    <dd>{{% md %}}Domain log publishing related options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node<wbr>To<wbr>Node<wbr>Encryptions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainnodetonodeencryption">Get<wbr>Domain<wbr>Node<wbr>To<wbr>Node<wbr>Encryption[]</a></span>
    </dt>
    <dd>{{% md %}}Domain in transit encryption related options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>processing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Status of a configuration change in the domain.
* `snapshot_options` – Domain snapshot related options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>snapshot<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainsnapshotoption">Get<wbr>Domain<wbr>Snapshot<wbr>Option[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}The tags assigned to the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainvpcoption">Get<wbr>Domain<wbr>Vpc<wbr>Option[]</a></span>
    </dt>
    <dd>{{% md %}}VPC Options for private Elasticsearch domains.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>access_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The policy document attached to the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>advanced_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Key-value string pairs to specify advanced configuration options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cluster_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainclusterconfig">List[Get<wbr>Domain<wbr>Cluster<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Cluster configuration of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cognito_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomaincognitooption">List[Get<wbr>Domain<wbr>Cognito<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}Domain Amazon Cognito Authentication options for Kibana.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Status of the creation of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>deleted</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Status of the deletion of the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>domain_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Unique identifier for the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>domain_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ebs_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainebsoption">List[Get<wbr>Domain<wbr>Ebs<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}EBS Options for the instances in the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>elasticsearch_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}ElasticSearch version for the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>encryption_<wbr>at_<wbr>rests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainencryptionatrest">List[Get<wbr>Domain<wbr>Encryption<wbr>At<wbr>Rest]</a></span>
    </dt>
    <dd>{{% md %}}Domain encryption at rest related options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Domain-specific endpoint used to submit index, search, and data upload requests.
{{% /md %}}</dd>

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
        <span>kibana_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Domain-specific endpoint used to access the Kibana application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>log_<wbr>publishing_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainlogpublishingoption">List[Get<wbr>Domain<wbr>Log<wbr>Publishing<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}Domain log publishing related options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node_<wbr>to_<wbr>node_<wbr>encryptions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainnodetonodeencryption">List[Get<wbr>Domain<wbr>Node<wbr>To<wbr>Node<wbr>Encryption]</a></span>
    </dt>
    <dd>{{% md %}}Domain in transit encryption related options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>processing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Status of a configuration change in the domain.
* `snapshot_options` – Domain snapshot related options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>snapshot_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainsnapshotoption">List[Get<wbr>Domain<wbr>Snapshot<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}The tags assigned to the domain.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainvpcoption">List[Get<wbr>Domain<wbr>Vpc<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}VPC Options for private Elasticsearch domains.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Domain<wbr>Cluster<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetDomainClusterConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/v2/go/aws/elasticsearch?tab=doc#GetDomainClusterConfig">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dedicated<wbr>Master<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Number of dedicated master nodes in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Dedicated<wbr>Master<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether dedicated master nodes are enabled for the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Dedicated<wbr>Master<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Instance type of the dedicated master nodes in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Number of instances in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Instance type of data nodes in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zone<wbr>Awareness<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainclusterconfigzoneawarenessconfig">List&lt;Get<wbr>Domain<wbr>Cluster<wbr>Config<wbr>Zone<wbr>Awareness<wbr>Config<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Configuration block containing zone awareness settings.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zone<wbr>Awareness<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether zone awareness is enabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dedicated<wbr>Master<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Number of dedicated master nodes in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Dedicated<wbr>Master<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether dedicated master nodes are enabled for the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Dedicated<wbr>Master<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Instance type of the dedicated master nodes in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Number of instances in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Instance type of data nodes in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zone<wbr>Awareness<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainclusterconfigzoneawarenessconfig">[]Get<wbr>Domain<wbr>Cluster<wbr>Config<wbr>Zone<wbr>Awareness<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration block containing zone awareness settings.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zone<wbr>Awareness<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether zone awareness is enabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dedicated<wbr>Master<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Number of dedicated master nodes in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>dedicated<wbr>Master<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether dedicated master nodes are enabled for the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>dedicated<wbr>Master<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Instance type of the dedicated master nodes in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Number of instances in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Instance type of data nodes in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zone<wbr>Awareness<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainclusterconfigzoneawarenessconfig">Get<wbr>Domain<wbr>Cluster<wbr>Config<wbr>Zone<wbr>Awareness<wbr>Config[]</a></span>
    </dt>
    <dd>{{% md %}}Configuration block containing zone awareness settings.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zone<wbr>Awareness<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether zone awareness is enabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dedicated<wbr>Master<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Number of dedicated master nodes in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>dedicated<wbr>Master<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether dedicated master nodes are enabled for the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>dedicated<wbr>Master<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Instance type of the dedicated master nodes in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Number of instances in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Instance type of data nodes in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zone<wbr>Awareness<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getdomainclusterconfigzoneawarenessconfig">List[Get<wbr>Domain<wbr>Cluster<wbr>Config<wbr>Zone<wbr>Awareness<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Configuration block containing zone awareness settings.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zone<wbr>Awareness<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether zone awareness is enabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Domain<wbr>Cluster<wbr>Config<wbr>Zone<wbr>Awareness<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetDomainClusterConfigZoneAwarenessConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/v2/go/aws/elasticsearch?tab=doc#GetDomainClusterConfigZoneAwarenessConfig">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Availability<wbr>Zone<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Number of availability zones used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Availability<wbr>Zone<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Number of availability zones used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>availability<wbr>Zone<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Number of availability zones used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>availability<wbr>Zone<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Number of availability zones used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Domain<wbr>Cognito<wbr>Option</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetDomainCognitoOption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/v2/go/aws/elasticsearch?tab=doc#GetDomainCognitoOption">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether node to node encryption is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Identity<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Cognito Identity pool used by the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The IAM Role with the AmazonESCognitoAccess policy attached.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>User<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Cognito User pool used by the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether node to node encryption is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Identity<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Cognito Identity pool used by the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The IAM Role with the AmazonESCognitoAccess policy attached.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>User<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Cognito User pool used by the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether node to node encryption is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>identity<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Cognito Identity pool used by the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The IAM Role with the AmazonESCognitoAccess policy attached.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>user<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Cognito User pool used by the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether node to node encryption is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>identity_<wbr>pool_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Cognito Identity pool used by the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The IAM Role with the AmazonESCognitoAccess policy attached.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>user_<wbr>pool_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Cognito User pool used by the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Domain<wbr>Ebs<wbr>Option</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetDomainEbsOption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/v2/go/aws/elasticsearch?tab=doc#GetDomainEbsOption">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Ebs<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether EBS volumes are attached to data nodes in the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Iops</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The baseline input/output (I/O) performance of EBS volumes
attached to data nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The size of EBS volumes attached to data nodes (in GB).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of EBS volumes attached to data nodes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Ebs<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether EBS volumes are attached to data nodes in the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Iops</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The baseline input/output (I/O) performance of EBS volumes
attached to data nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The size of EBS volumes attached to data nodes (in GB).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of EBS volumes attached to data nodes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>ebs<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether EBS volumes are attached to data nodes in the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>iops</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The baseline input/output (I/O) performance of EBS volumes
attached to data nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The size of EBS volumes attached to data nodes (in GB).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of EBS volumes attached to data nodes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>ebs<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether EBS volumes are attached to data nodes in the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>iops</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The baseline input/output (I/O) performance of EBS volumes
attached to data nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The size of EBS volumes attached to data nodes (in GB).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of EBS volumes attached to data nodes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Domain<wbr>Encryption<wbr>At<wbr>Rest</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetDomainEncryptionAtRest">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/v2/go/aws/elasticsearch?tab=doc#GetDomainEncryptionAtRest">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether node to node encryption is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The KMS key id used to encrypt data at rest.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether node to node encryption is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The KMS key id used to encrypt data at rest.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether node to node encryption is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The KMS key id used to encrypt data at rest.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether node to node encryption is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>kms_<wbr>key_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The KMS key id used to encrypt data at rest.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Domain<wbr>Log<wbr>Publishing<wbr>Option</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetDomainLogPublishingOption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/v2/go/aws/elasticsearch?tab=doc#GetDomainLogPublishingOption">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cloudwatch<wbr>Log<wbr>Group<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The CloudWatch Log Group where the logs are published.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether node to node encryption is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Log<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of Elasticsearch log being published.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cloudwatch<wbr>Log<wbr>Group<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The CloudWatch Log Group where the logs are published.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether node to node encryption is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Log<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of Elasticsearch log being published.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cloudwatch<wbr>Log<wbr>Group<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The CloudWatch Log Group where the logs are published.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether node to node encryption is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>log<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of Elasticsearch log being published.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cloudwatch_<wbr>log_<wbr>group_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The CloudWatch Log Group where the logs are published.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether node to node encryption is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>log<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of Elasticsearch log being published.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Domain<wbr>Node<wbr>To<wbr>Node<wbr>Encryption</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetDomainNodeToNodeEncryption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/v2/go/aws/elasticsearch?tab=doc#GetDomainNodeToNodeEncryption">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether node to node encryption is enabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether node to node encryption is enabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether node to node encryption is enabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether node to node encryption is enabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Domain<wbr>Snapshot<wbr>Option</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetDomainSnapshotOption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/v2/go/aws/elasticsearch?tab=doc#GetDomainSnapshotOption">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Automated<wbr>Snapshot<wbr>Start<wbr>Hour</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Hour during which the service takes an automated daily
snapshot of the indices in the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Automated<wbr>Snapshot<wbr>Start<wbr>Hour</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Hour during which the service takes an automated daily
snapshot of the indices in the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>automated<wbr>Snapshot<wbr>Start<wbr>Hour</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Hour during which the service takes an automated daily
snapshot of the indices in the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>automated<wbr>Snapshot<wbr>Start<wbr>Hour</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Hour during which the service takes an automated daily
snapshot of the indices in the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Domain<wbr>Vpc<wbr>Option</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetDomainVpcOption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/v2/go/aws/elasticsearch?tab=doc#GetDomainVpcOption">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Availability<wbr>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The availability zones used by the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The security groups used by the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The subnets used by the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The VPC used by the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Availability<wbr>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The availability zones used by the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The security groups used by the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The subnets used by the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The VPC used by the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>availability<wbr>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The availability zones used by the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The security groups used by the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The subnets used by the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The VPC used by the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>availability_<wbr>zones</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The availability zones used by the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>security_<wbr>group_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The security groups used by the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnet_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The subnets used by the domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vpc_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The VPC used by the domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







