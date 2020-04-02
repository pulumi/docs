
---
title: "Record"
block_external_search_index: true
---

Provides a Route53 record resource.

## Example Usage

### Simple routing policy

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const www = new aws.route53.Record("www", {
    name: "www.example.com",
    records: [aws_eip_lb.publicIp],
    ttl: 300,
    type: "A",
    zoneId: aws_route53_zone_primary.zoneId,
});
```

### Weighted routing policy
Other routing policies are configured similarly. See [AWS Route53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html) for details.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const www_dev = new aws.route53.Record("www-dev", {
    name: "www",
    records: ["dev.example.com"],
    setIdentifier: "dev",
    ttl: 5,
    type: "CNAME",
    weightedRoutingPolicies: [{
        weight: 10,
    }],
    zoneId: aws_route53_zone_primary.zoneId,
});
const www_live = new aws.route53.Record("www-live", {
    name: "www",
    records: ["live.example.com"],
    setIdentifier: "live",
    ttl: 5,
    type: "CNAME",
    weightedRoutingPolicies: [{
        weight: 90,
    }],
    zoneId: aws_route53_zone_primary.zoneId,
});
```

### Alias record
See [related part of AWS Route53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html)
to understand differences between alias and non-alias records.

TTL for all alias records is [60 seconds](https://aws.amazon.com/route53/faqs/#dns_failover_do_i_need_to_adjust),
you cannot change this, therefore `ttl` has to be omitted in alias records.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const main = new aws.elb.LoadBalancer("main", {
    availabilityZones: ["us-east-1c"],
    listeners: [{
        instancePort: 80,
        instanceProtocol: "http",
        lbPort: 80,
        lbProtocol: "http",
    }],
});
const www = new aws.route53.Record("www", {
    aliases: [{
        evaluateTargetHealth: true,
        name: main.dnsName,
        zoneId: main.zoneId,
    }],
    name: "example.com",
    type: "A",
    zoneId: aws_route53_zone_primary.zoneId,
});
```

### NS and SOA Record Management

When creating Route 53 zones, the `NS` and `SOA` records for the zone are automatically created. Enabling the `allow_overwrite` argument will allow managing these records in a single deployment without the requirement for `import`.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleZone = new aws.route53.Zone("example", {});
const exampleRecord = new aws.route53.Record("example", {
    allowOverwrite: true,
    name: "test.example.com",
    records: [
        exampleZone.nameServers[0],
        exampleZone.nameServers[1],
        exampleZone.nameServers[2],
        exampleZone.nameServers[3],
    ],
    ttl: 30,
    type: "NS",
    zoneId: exampleZone.zoneId,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_record.html.markdown.



## Create a Record Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/route53/#Record">Record</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/route53/#RecordArgs">RecordArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Record</span><span class="p">(resource_name, opts=None, </span>aliases=None<span class="p">, </span>allow_overwrite=None<span class="p">, </span>failover_routing_policies=None<span class="p">, </span>geolocation_routing_policies=None<span class="p">, </span>health_check_id=None<span class="p">, </span>latency_routing_policies=None<span class="p">, </span>multivalue_answer_routing_policy=None<span class="p">, </span>name=None<span class="p">, </span>records=None<span class="p">, </span>set_identifier=None<span class="p">, </span>ttl=None<span class="p">, </span>type=None<span class="p">, </span>weighted_routing_policies=None<span class="p">, </span>zone_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewRecord<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordArgs">RecordArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#Record">Record</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.Record.html">Record</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.RecordArgs.html">RecordArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Aliases</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordalias">List&lt;Record<wbr>Alias<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}An alias block. Conflicts with `ttl` & `records`.
Alias record documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Overwrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failover<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordfailoverroutingpolicy">List&lt;Record<wbr>Failover<wbr>Routing<wbr>Policy<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Geolocation<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordgeolocationroutingpolicy">List&lt;Record<wbr>Geolocation<wbr>Routing<wbr>Policy<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Check<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The health check the record should be associated with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Latency<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordlatencyroutingpolicy">List&lt;Record<wbr>Latency<wbr>Routing<wbr>Policy<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Multivalue<wbr>Answer<wbr>Routing<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Records</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Set<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The TTL of the record.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weighted<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordweightedroutingpolicy">List&lt;Record<wbr>Weighted<wbr>Routing<wbr>Policy<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Aliases</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordalias">[]Record<wbr>Alias</a></span>
    </dt>
    <dd>{{% md %}}An alias block. Conflicts with `ttl` & `records`.
Alias record documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Overwrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failover<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordfailoverroutingpolicy">[]Record<wbr>Failover<wbr>Routing<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Geolocation<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordgeolocationroutingpolicy">[]Record<wbr>Geolocation<wbr>Routing<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Check<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The health check the record should be associated with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Latency<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordlatencyroutingpolicy">[]Record<wbr>Latency<wbr>Routing<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Multivalue<wbr>Answer<wbr>Routing<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Records</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Set<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The TTL of the record.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">interface{}</span>
    </dt>
    <dd>{{% md %}}`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weighted<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordweightedroutingpolicy">[]Record<wbr>Weighted<wbr>Routing<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>aliases</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordalias">Record<wbr>Alias[]?</a></span>
    </dt>
    <dd>{{% md %}}An alias block. Conflicts with `ttl` & `records`.
Alias record documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Overwrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failover<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordfailoverroutingpolicy">Record<wbr>Failover<wbr>Routing<wbr>Policy[]?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>geolocation<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordgeolocationroutingpolicy">Record<wbr>Geolocation<wbr>Routing<wbr>Policy[]?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health<wbr>Check<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The health check the record should be associated with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>latency<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordlatencyroutingpolicy">Record<wbr>Latency<wbr>Routing<wbr>Policy[]?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>multivalue<wbr>Answer<wbr>Routing<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>records</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>set<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The TTL of the record.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string | RecordType</span>
    </dt>
    <dd>{{% md %}}`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weighted<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordweightedroutingpolicy">Record<wbr>Weighted<wbr>Routing<wbr>Policy[]?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>aliases</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordalias">List[Record<wbr>Alias]</a></span>
    </dt>
    <dd>{{% md %}}An alias block. Conflicts with `ttl` & `records`.
Alias record documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>overwrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failover_<wbr>routing_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordfailoverroutingpolicy">List[Record<wbr>Failover<wbr>Routing<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>geolocation_<wbr>routing_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordgeolocationroutingpolicy">List[Record<wbr>Geolocation<wbr>Routing<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health_<wbr>check_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The health check the record should be associated with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>latency_<wbr>routing_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordlatencyroutingpolicy">List[Record<wbr>Latency<wbr>Routing<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>multivalue_<wbr>answer_<wbr>routing_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>records</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>set_<wbr>identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The TTL of the record.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weighted_<wbr>routing_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordweightedroutingpolicy">List[Record<wbr>Weighted<wbr>Routing<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zone_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Record Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Aliases</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordalias">List&lt;Record<wbr>Alias&gt;?</a></span>
    </dt>
    <dd>{{% md %}}An alias block. Conflicts with `ttl` & `records`.
Alias record documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Overwrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Failover<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordfailoverroutingpolicy">List&lt;Record<wbr>Failover<wbr>Routing<wbr>Policy&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}[FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Geolocation<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordgeolocationroutingpolicy">List&lt;Record<wbr>Geolocation<wbr>Routing<wbr>Policy&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Health<wbr>Check<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The health check the record should be associated with.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Latency<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordlatencyroutingpolicy">List&lt;Record<wbr>Latency<wbr>Routing<wbr>Policy&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Multivalue<wbr>Answer<wbr>Routing<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Records</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Set<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The TTL of the record.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Weighted<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordweightedroutingpolicy">List&lt;Record<wbr>Weighted<wbr>Routing<wbr>Policy&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Aliases</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordalias">[]Record<wbr>Alias</a></span>
    </dt>
    <dd>{{% md %}}An alias block. Conflicts with `ttl` & `records`.
Alias record documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Overwrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Failover<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordfailoverroutingpolicy">[]Record<wbr>Failover<wbr>Routing<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}[FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Geolocation<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordgeolocationroutingpolicy">[]Record<wbr>Geolocation<wbr>Routing<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Health<wbr>Check<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The health check the record should be associated with.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Latency<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordlatencyroutingpolicy">[]Record<wbr>Latency<wbr>Routing<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Multivalue<wbr>Answer<wbr>Routing<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Records</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Set<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The TTL of the record.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Weighted<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordweightedroutingpolicy">[]Record<wbr>Weighted<wbr>Routing<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>aliases</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordalias">Record<wbr>Alias[]?</a></span>
    </dt>
    <dd>{{% md %}}An alias block. Conflicts with `ttl` & `records`.
Alias record documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow<wbr>Overwrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>failover<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordfailoverroutingpolicy">Record<wbr>Failover<wbr>Routing<wbr>Policy[]?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}[FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>geolocation<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordgeolocationroutingpolicy">Record<wbr>Geolocation<wbr>Routing<wbr>Policy[]?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>health<wbr>Check<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The health check the record should be associated with.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>latency<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordlatencyroutingpolicy">Record<wbr>Latency<wbr>Routing<wbr>Policy[]?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>multivalue<wbr>Answer<wbr>Routing<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>records</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>set<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The TTL of the record.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>weighted<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordweightedroutingpolicy">Record<wbr>Weighted<wbr>Routing<wbr>Policy[]?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>aliases</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordalias">List[Record<wbr>Alias]</a></span>
    </dt>
    <dd>{{% md %}}An alias block. Conflicts with `ttl` & `records`.
Alias record documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow_<wbr>overwrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>failover_<wbr>routing_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordfailoverroutingpolicy">List[Record<wbr>Failover<wbr>Routing<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}[FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>geolocation_<wbr>routing_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordgeolocationroutingpolicy">List[Record<wbr>Geolocation<wbr>Routing<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>health_<wbr>check_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The health check the record should be associated with.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>latency_<wbr>routing_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordlatencyroutingpolicy">List[Record<wbr>Latency<wbr>Routing<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>multivalue_<wbr>answer_<wbr>routing_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>records</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>set_<wbr>identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The TTL of the record.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>weighted_<wbr>routing_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordweightedroutingpolicy">List[Record<wbr>Weighted<wbr>Routing<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Record Resource

Get an existing Record resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/route53/#RecordState">RecordState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/route53/#Record">Record</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>aliases=None<span class="p">, </span>allow_overwrite=None<span class="p">, </span>failover_routing_policies=None<span class="p">, </span>fqdn=None<span class="p">, </span>geolocation_routing_policies=None<span class="p">, </span>health_check_id=None<span class="p">, </span>latency_routing_policies=None<span class="p">, </span>multivalue_answer_routing_policy=None<span class="p">, </span>name=None<span class="p">, </span>records=None<span class="p">, </span>set_identifier=None<span class="p">, </span>ttl=None<span class="p">, </span>type=None<span class="p">, </span>weighted_routing_policies=None<span class="p">, </span>zone_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetRecord<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordState">RecordState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#Record">Record</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.Record.html">Record</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.RecordState.html">RecordState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Aliases</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordalias">List&lt;Record<wbr>Alias<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}An alias block. Conflicts with `ttl` & `records`.
Alias record documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Overwrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failover<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordfailoverroutingpolicy">List&lt;Record<wbr>Failover<wbr>Routing<wbr>Policy<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}[FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Geolocation<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordgeolocationroutingpolicy">List&lt;Record<wbr>Geolocation<wbr>Routing<wbr>Policy<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Check<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The health check the record should be associated with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Latency<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordlatencyroutingpolicy">List&lt;Record<wbr>Latency<wbr>Routing<wbr>Policy<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Multivalue<wbr>Answer<wbr>Routing<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Records</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Set<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The TTL of the record.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weighted<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordweightedroutingpolicy">List&lt;Record<wbr>Weighted<wbr>Routing<wbr>Policy<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Aliases</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordalias">[]Record<wbr>Alias</a></span>
    </dt>
    <dd>{{% md %}}An alias block. Conflicts with `ttl` & `records`.
Alias record documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Overwrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failover<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordfailoverroutingpolicy">[]Record<wbr>Failover<wbr>Routing<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}[FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Geolocation<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordgeolocationroutingpolicy">[]Record<wbr>Geolocation<wbr>Routing<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Check<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The health check the record should be associated with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Latency<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordlatencyroutingpolicy">[]Record<wbr>Latency<wbr>Routing<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Multivalue<wbr>Answer<wbr>Routing<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Records</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Set<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The TTL of the record.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">interface{}</span>
    </dt>
    <dd>{{% md %}}`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weighted<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordweightedroutingpolicy">[]Record<wbr>Weighted<wbr>Routing<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>aliases</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordalias">Record<wbr>Alias[]?</a></span>
    </dt>
    <dd>{{% md %}}An alias block. Conflicts with `ttl` & `records`.
Alias record documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Overwrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failover<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordfailoverroutingpolicy">Record<wbr>Failover<wbr>Routing<wbr>Policy[]?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}[FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>geolocation<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordgeolocationroutingpolicy">Record<wbr>Geolocation<wbr>Routing<wbr>Policy[]?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health<wbr>Check<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The health check the record should be associated with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>latency<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordlatencyroutingpolicy">Record<wbr>Latency<wbr>Routing<wbr>Policy[]?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>multivalue<wbr>Answer<wbr>Routing<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>records</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>set<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The TTL of the record.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string | RecordType</span>
    </dt>
    <dd>{{% md %}}`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weighted<wbr>Routing<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordweightedroutingpolicy">Record<wbr>Weighted<wbr>Routing<wbr>Policy[]?</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>aliases</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordalias">List[Record<wbr>Alias]</a></span>
    </dt>
    <dd>{{% md %}}An alias block. Conflicts with `ttl` & `records`.
Alias record documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>overwrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failover_<wbr>routing_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordfailoverroutingpolicy">List[Record<wbr>Failover<wbr>Routing<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}[FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>geolocation_<wbr>routing_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordgeolocationroutingpolicy">List[Record<wbr>Geolocation<wbr>Routing<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health_<wbr>check_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The health check the record should be associated with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>latency_<wbr>routing_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordlatencyroutingpolicy">List[Record<wbr>Latency<wbr>Routing<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>multivalue_<wbr>answer_<wbr>routing_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>records</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the configuration string (e.g. `"first255characters\"\"morecharacters"`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>set_<wbr>identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The TTL of the record.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weighted_<wbr>routing_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#recordweightedroutingpolicy">List[Record<wbr>Weighted<wbr>Routing<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Record<wbr>Alias</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#RecordAlias">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#RecordAlias">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordAliasArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordAliasOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Evaluate<wbr>Target<wbr>Health</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to `true` if you want Route 53 to determine whether to respond to DNS queries using this resource record set by checking the health of the resource record set. Some resources have special requirements, see [related part of documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html#rrsets-values-alias-evaluate-target-health).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Evaluate<wbr>Target<wbr>Health</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to `true` if you want Route 53 to determine whether to respond to DNS queries using this resource record set by checking the health of the resource record set. Some resources have special requirements, see [related part of documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html#rrsets-values-alias-evaluate-target-health).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>evaluate<wbr>Target<wbr>Health</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Set to `true` if you want Route 53 to determine whether to respond to DNS queries using this resource record set by checking the health of the resource record set. Some resources have special requirements, see [related part of documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html#rrsets-values-alias-evaluate-target-health).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>evaluate<wbr>Target<wbr>Health</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to `true` if you want Route 53 to determine whether to respond to DNS queries using this resource record set by checking the health of the resource record set. Some resources have special requirements, see [related part of documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html#rrsets-values-alias-evaluate-target-health).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zone_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Record<wbr>Failover<wbr>Routing<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#RecordFailoverRoutingPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#RecordFailoverRoutingPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordFailoverRoutingPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordFailoverRoutingPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Record<wbr>Geolocation<wbr>Routing<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#RecordGeolocationRoutingPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#RecordGeolocationRoutingPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordGeolocationRoutingPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordGeolocationRoutingPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Continent</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A two-letter continent code. See http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html for code details. Either `continent` or `country` must be specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Country</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A two-character country code or `*` to indicate a default resource record set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subdivision</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A subdivision code for a country.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Continent</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A two-letter continent code. See http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html for code details. Either `continent` or `country` must be specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Country</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A two-character country code or `*` to indicate a default resource record set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subdivision</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A subdivision code for a country.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>continent</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A two-letter continent code. See http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html for code details. Either `continent` or `country` must be specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>country</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A two-character country code or `*` to indicate a default resource record set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subdivision</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A subdivision code for a country.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>continent</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A two-letter continent code. See http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html for code details. Either `continent` or `country` must be specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>country</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A two-character country code or `*` to indicate a default resource record set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subdivision</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A subdivision code for a country.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Record<wbr>Latency<wbr>Routing<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#RecordLatencyRoutingPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#RecordLatencyRoutingPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordLatencyRoutingPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordLatencyRoutingPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An AWS region from which to measure latency. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An AWS region from which to measure latency. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An AWS region from which to measure latency. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An AWS region from which to measure latency. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Record<wbr>Weighted<wbr>Routing<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#RecordWeightedRoutingPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#RecordWeightedRoutingPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordWeightedRoutingPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordWeightedRoutingPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}A numeric value indicating the relative weight of the record. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}A numeric value indicating the relative weight of the record. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}A numeric value indicating the relative weight of the record. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}A numeric value indicating the relative weight of the record. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-aws">https://github.com/pulumi/pulumi-aws</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
