
---
title: "Record"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


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

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/route53/#Record">Record</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/route53/#RecordArgs">RecordArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Record</span><span class="p">(resource_name, id, opts=None, </span>aliases=None<span class="p">, </span>allow_overwrite=None<span class="p">, </span>failover_routing_policies=None<span class="p">, </span>geolocation_routing_policies=None<span class="p">, </span>health_check_id=None<span class="p">, </span>latency_routing_policies=None<span class="p">, </span>multivalue_answer_routing_policy=None<span class="p">, </span>name=None<span class="p">, </span>records=None<span class="p">, </span>set_identifier=None<span class="p">, </span>ttl=None<span class="p">, </span>type=None<span class="p">, </span>weighted_routing_policies=None<span class="p">, </span>zone_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewRecord<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordArgs">RecordArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#Record">Record</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.Record.html">Record</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.RecordArgs.html">RecordArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Record resource with the given unique name, arguments, and options.

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
            <td class="align-top">Aliases</td>
            <td class="align-top">
                
                <code><a href="#recordalias">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Record<wbr>Alias<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An alias block. Conflicts with `ttl` &amp; `records`.
Alias record documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Overwrite</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Failover<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordfailoverroutingpolicy">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Record<wbr>Failover<wbr>Routing<wbr>Policy<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Geolocation<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordgeolocationroutingpolicy">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Record<wbr>Geolocation<wbr>Routing<wbr>Policy<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The health check the record should be associated with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Latency<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordlatencyroutingpolicy">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Record<wbr>Latency<wbr>Routing<wbr>Policy<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Multivalue<wbr>Answer<wbr>Routing<wbr>Policy</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Records</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\&#34;\&#34;` inside the configuration string (e.g. `&#34;first255characters\&#34;\&#34;morecharacters&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Set<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ttl</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The TTL of the record.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Weighted<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordweightedroutingpolicy">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Record<wbr>Weighted<wbr>Routing<wbr>Policy<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
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
            <td class="align-top">Aliases</td>
            <td class="align-top">
                
                <code><a href="#recordalias">[]route53.<wbr>Record<wbr>Alias</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An alias block. Conflicts with `ttl` &amp; `records`.
Alias record documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Overwrite</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Failover<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordfailoverroutingpolicy">[]route53.<wbr>Record<wbr>Failover<wbr>Routing<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Geolocation<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordgeolocationroutingpolicy">[]route53.<wbr>Record<wbr>Geolocation<wbr>Routing<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The health check the record should be associated with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Latency<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordlatencyroutingpolicy">[]route53.<wbr>Record<wbr>Latency<wbr>Routing<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Multivalue<wbr>Answer<wbr>Routing<wbr>Policy</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Records</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\&#34;\&#34;` inside the configuration string (e.g. `&#34;first255characters\&#34;\&#34;morecharacters&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Set<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ttl</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The TTL of the record.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Weighted<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordweightedroutingpolicy">[]route53.<wbr>Record<wbr>Weighted<wbr>Routing<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
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
            <td class="align-top">aliases</td>
            <td class="align-top">
                
                <code><a href="#recordalias">route53.<wbr>Record<wbr>Alias[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An alias block. Conflicts with `ttl` &amp; `records`.
Alias record documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow<wbr>Overwrite</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">failover<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordfailoverroutingpolicy">route53.<wbr>Record<wbr>Failover<wbr>Routing<wbr>Policy[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">geolocation<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordgeolocationroutingpolicy">route53.<wbr>Record<wbr>Geolocation<wbr>Routing<wbr>Policy[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The health check the record should be associated with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">latency<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordlatencyroutingpolicy">route53.<wbr>Record<wbr>Latency<wbr>Routing<wbr>Policy[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">multivalue<wbr>Answer<wbr>Routing<wbr>Policy</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">records</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\&#34;\&#34;` inside the configuration string (e.g. `&#34;first255characters\&#34;\&#34;morecharacters&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">set<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ttl</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The TTL of the record.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string | Record<wbr>Type</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">weighted<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordweightedroutingpolicy">route53.<wbr>Record<wbr>Weighted<wbr>Routing<wbr>Policy[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
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
            <td class="align-top">aliases</td>
            <td class="align-top">
                
                <code><a href="#recordalias">list[record_<wbr>alias]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An alias block. Conflicts with `ttl` &amp; `records`.
Alias record documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow_<wbr>overwrite</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">failover_<wbr>routing_<wbr>policies</td>
            <td class="align-top">
                
                <code><a href="#recordfailoverroutingpolicy">list[record_<wbr>failover_<wbr>routing_<wbr>policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">geolocation_<wbr>routing_<wbr>policies</td>
            <td class="align-top">
                
                <code><a href="#recordgeolocationroutingpolicy">list[record_<wbr>geolocation_<wbr>routing_<wbr>policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The health check the record should be associated with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">latency_<wbr>routing_<wbr>policies</td>
            <td class="align-top">
                
                <code><a href="#recordlatencyroutingpolicy">list[record_<wbr>latency_<wbr>routing_<wbr>policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">multivalue_<wbr>answer_<wbr>routing_<wbr>policy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">records</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\&#34;\&#34;` inside the configuration string (e.g. `&#34;first255characters\&#34;\&#34;morecharacters&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">set_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ttl</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The TTL of the record.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>dict</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">weighted_<wbr>routing_<wbr>policies</td>
            <td class="align-top">
                
                <code><a href="#recordweightedroutingpolicy">list[record_<wbr>weighted_<wbr>routing_<wbr>policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Record Output Properties

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
            <td class="align-top">Aliases</td>
            <td class="align-top">
                
                <code><a href="#recordalias">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Record<wbr>Alias&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} An alias block. Conflicts with `ttl` &amp; `records`.
Alias record documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Overwrite</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Failover<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordfailoverroutingpolicy">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Record<wbr>Failover<wbr>Routing<wbr>Policy&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Fqdn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} [FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Geolocation<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordgeolocationroutingpolicy">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Record<wbr>Geolocation<wbr>Routing<wbr>Policy&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The health check the record should be associated with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Latency<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordlatencyroutingpolicy">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Record<wbr>Latency<wbr>Routing<wbr>Policy&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Multivalue<wbr>Answer<wbr>Routing<wbr>Policy</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Records</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\&#34;\&#34;` inside the configuration string (e.g. `&#34;first255characters\&#34;\&#34;morecharacters&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Set<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ttl</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The TTL of the record.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Weighted<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordweightedroutingpolicy">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Record<wbr>Weighted<wbr>Routing<wbr>Policy&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
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
            <td class="align-top">Aliases</td>
            <td class="align-top">
                
                <code><a href="#recordalias">[]route53.<wbr>Record<wbr>Alias</a></code>
            </td>
            <td class="align-top">{{% md %}} An alias block. Conflicts with `ttl` &amp; `records`.
Alias record documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Overwrite</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Failover<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordfailoverroutingpolicy">[]route53.<wbr>Record<wbr>Failover<wbr>Routing<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Fqdn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} [FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Geolocation<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordgeolocationroutingpolicy">[]route53.<wbr>Record<wbr>Geolocation<wbr>Routing<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The health check the record should be associated with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Latency<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordlatencyroutingpolicy">[]route53.<wbr>Record<wbr>Latency<wbr>Routing<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Multivalue<wbr>Answer<wbr>Routing<wbr>Policy</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Records</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\&#34;\&#34;` inside the configuration string (e.g. `&#34;first255characters\&#34;\&#34;morecharacters&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Set<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ttl</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The TTL of the record.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Weighted<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordweightedroutingpolicy">[]route53.<wbr>Record<wbr>Weighted<wbr>Routing<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
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
            <td class="align-top">aliases</td>
            <td class="align-top">
                
                <code><a href="#recordalias">route53.<wbr>Record<wbr>Alias[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} An alias block. Conflicts with `ttl` &amp; `records`.
Alias record documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow<wbr>Overwrite</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">failover<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordfailoverroutingpolicy">route53.<wbr>Record<wbr>Failover<wbr>Routing<wbr>Policy[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">fqdn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} [FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">geolocation<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordgeolocationroutingpolicy">route53.<wbr>Record<wbr>Geolocation<wbr>Routing<wbr>Policy[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The health check the record should be associated with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">latency<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordlatencyroutingpolicy">route53.<wbr>Record<wbr>Latency<wbr>Routing<wbr>Policy[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">multivalue<wbr>Answer<wbr>Routing<wbr>Policy</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">records</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\&#34;\&#34;` inside the configuration string (e.g. `&#34;first255characters\&#34;\&#34;morecharacters&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">set<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ttl</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The TTL of the record.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">weighted<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordweightedroutingpolicy">route53.<wbr>Record<wbr>Weighted<wbr>Routing<wbr>Policy[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
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
            <td class="align-top">aliases</td>
            <td class="align-top">
                
                <code><a href="#recordalias">list[record_<wbr>alias]</a></code>
            </td>
            <td class="align-top">{{% md %}} An alias block. Conflicts with `ttl` &amp; `records`.
Alias record documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow_<wbr>overwrite</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">failover_<wbr>routing_<wbr>policies</td>
            <td class="align-top">
                
                <code><a href="#recordfailoverroutingpolicy">list[record_<wbr>failover_<wbr>routing_<wbr>policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">fqdn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} [FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">geolocation_<wbr>routing_<wbr>policies</td>
            <td class="align-top">
                
                <code><a href="#recordgeolocationroutingpolicy">list[record_<wbr>geolocation_<wbr>routing_<wbr>policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The health check the record should be associated with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">latency_<wbr>routing_<wbr>policies</td>
            <td class="align-top">
                
                <code><a href="#recordlatencyroutingpolicy">list[record_<wbr>latency_<wbr>routing_<wbr>policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">multivalue_<wbr>answer_<wbr>routing_<wbr>policy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">records</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\&#34;\&#34;` inside the configuration string (e.g. `&#34;first255characters\&#34;\&#34;morecharacters&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">set_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ttl</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The TTL of the record.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">weighted_<wbr>routing_<wbr>policies</td>
            <td class="align-top">
                
                <code><a href="#recordweightedroutingpolicy">list[record_<wbr>weighted_<wbr>routing_<wbr>policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Record Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RecordState, opts?: pulumi.CustomResourceOptions): Record;
```

```python
def get(resource_name, id, opts=None, aliases=None, allow_<wbr>overwrite=None, failover_<wbr>routing_<wbr>policies=None, fqdn=None, geolocation_<wbr>routing_<wbr>policies=None, health_<wbr>check_<wbr>id=None, latency_<wbr>routing_<wbr>policies=None, multivalue_<wbr>answer_<wbr>routing_<wbr>policy=None, name=None, records=None, set_<wbr>identifier=None, ttl=None, type=None, weighted_<wbr>routing_<wbr>policies=None, zone_<wbr>id=None)
```

```go
func GetRecord(ctx *pulumi.Context, name string, id pulumi.IDInput, state *RecordState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static Record Get(string name, Input<string> id, RecordState? state = null, CustomResourceOptions? options = null);
```

Get an existing Record resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Aliases</td>
            <td class="align-top">
                
                <code><a href="#recordalias">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Record<wbr>Alias<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An alias block. Conflicts with `ttl` &amp; `records`.
Alias record documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Overwrite</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Failover<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordfailoverroutingpolicy">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Record<wbr>Failover<wbr>Routing<wbr>Policy<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Fqdn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
[FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Geolocation<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordgeolocationroutingpolicy">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Record<wbr>Geolocation<wbr>Routing<wbr>Policy<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The health check the record should be associated with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Latency<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordlatencyroutingpolicy">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Record<wbr>Latency<wbr>Routing<wbr>Policy<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Multivalue<wbr>Answer<wbr>Routing<wbr>Policy</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
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
DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Records</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\&#34;\&#34;` inside the configuration string (e.g. `&#34;first255characters\&#34;\&#34;morecharacters&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Set<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ttl</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The TTL of the record.
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
`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Weighted<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordweightedroutingpolicy">List&lt;Pulumi.<wbr>Aws.<wbr>Route53.<wbr>Record<wbr>Weighted<wbr>Routing<wbr>Policy<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
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
            <td class="align-top">Aliases</td>
            <td class="align-top">
                
                <code><a href="#recordalias">[]route53.<wbr>Record<wbr>Alias</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An alias block. Conflicts with `ttl` &amp; `records`.
Alias record documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allow<wbr>Overwrite</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Failover<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordfailoverroutingpolicy">[]route53.<wbr>Record<wbr>Failover<wbr>Routing<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Fqdn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
[FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Geolocation<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordgeolocationroutingpolicy">[]route53.<wbr>Record<wbr>Geolocation<wbr>Routing<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The health check the record should be associated with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Latency<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordlatencyroutingpolicy">[]route53.<wbr>Record<wbr>Latency<wbr>Routing<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Multivalue<wbr>Answer<wbr>Routing<wbr>Policy</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
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
DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Records</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\&#34;\&#34;` inside the configuration string (e.g. `&#34;first255characters\&#34;\&#34;morecharacters&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Set<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ttl</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The TTL of the record.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Weighted<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordweightedroutingpolicy">[]route53.<wbr>Record<wbr>Weighted<wbr>Routing<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
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
            <td class="align-top">aliases</td>
            <td class="align-top">
                
                <code><a href="#recordalias">route53.<wbr>Record<wbr>Alias[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An alias block. Conflicts with `ttl` &amp; `records`.
Alias record documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow<wbr>Overwrite</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">failover<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordfailoverroutingpolicy">route53.<wbr>Record<wbr>Failover<wbr>Routing<wbr>Policy[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">fqdn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
[FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">geolocation<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordgeolocationroutingpolicy">route53.<wbr>Record<wbr>Geolocation<wbr>Routing<wbr>Policy[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The health check the record should be associated with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">latency<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordlatencyroutingpolicy">route53.<wbr>Record<wbr>Latency<wbr>Routing<wbr>Policy[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">multivalue<wbr>Answer<wbr>Routing<wbr>Policy</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
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
DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">records</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\&#34;\&#34;` inside the configuration string (e.g. `&#34;first255characters\&#34;\&#34;morecharacters&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">set<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ttl</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The TTL of the record.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string | Record<wbr>Type</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">weighted<wbr>Routing<wbr>Policies</td>
            <td class="align-top">
                
                <code><a href="#recordweightedroutingpolicy">route53.<wbr>Record<wbr>Weighted<wbr>Routing<wbr>Policy[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
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
            <td class="align-top">aliases</td>
            <td class="align-top">
                
                <code><a href="#recordalias">list[record_<wbr>alias]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An alias block. Conflicts with `ttl` &amp; `records`.
Alias record documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allow_<wbr>overwrite</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow creation of this record to overwrite an existing record, if any. This does not affect the ability to update the record using this provider and does not prevent other resources within this provider or manual Route 53 changes outside this provider from overwriting this record. `false` by default. This configuration is not recommended for most environments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">failover_<wbr>routing_<wbr>policies</td>
            <td class="align-top">
                
                <code><a href="#recordfailoverroutingpolicy">list[record_<wbr>failover_<wbr>routing_<wbr>policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">fqdn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
[FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">geolocation_<wbr>routing_<wbr>policies</td>
            <td class="align-top">
                
                <code><a href="#recordgeolocationroutingpolicy">list[record_<wbr>geolocation_<wbr>routing_<wbr>policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The health check the record should be associated with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">latency_<wbr>routing_<wbr>policies</td>
            <td class="align-top">
                
                <code><a href="#recordlatencyroutingpolicy">list[record_<wbr>latency_<wbr>routing_<wbr>policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">multivalue_<wbr>answer_<wbr>routing_<wbr>policy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
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
DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">records</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\&#34;\&#34;` inside the configuration string (e.g. `&#34;first255characters\&#34;\&#34;morecharacters&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">set_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ttl</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The TTL of the record.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>dict</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">weighted_<wbr>routing_<wbr>policies</td>
            <td class="align-top">
                
                <code><a href="#recordweightedroutingpolicy">list[record_<wbr>weighted_<wbr>routing_<wbr>policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### RecordAlias
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#RecordAlias">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#RecordAlias">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordAliasArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordAliasOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.RecordAliasArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.RecordAlias.html">output</a> API doc for this type.
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
            <td class="align-top">Evaluate<wbr>Target<wbr>Health</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Set to `true` if you want Route 53 to determine whether to respond to DNS queries using this resource record set by checking the health of the resource record set. Some resources have special requirements, see [related part of documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html#rrsets-values-alias-evaluate-target-health).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
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
            <td class="align-top">Evaluate<wbr>Target<wbr>Health</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Set to `true` if you want Route 53 to determine whether to respond to DNS queries using this resource record set by checking the health of the resource record set. Some resources have special requirements, see [related part of documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html#rrsets-values-alias-evaluate-target-health).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
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
            <td class="align-top">evaluate<wbr>Target<wbr>Health</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Set to `true` if you want Route 53 to determine whether to respond to DNS queries using this resource record set by checking the health of the resource record set. Some resources have special requirements, see [related part of documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html#rrsets-values-alias-evaluate-target-health).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
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
            <td class="align-top">evaluate_<wbr>target_<wbr>health</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Set to `true` if you want Route 53 to determine whether to respond to DNS queries using this resource record set by checking the health of the resource record set. Some resources have special requirements, see [related part of documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html#rrsets-values-alias-evaluate-target-health).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### RecordFailoverRoutingPolicy
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#RecordFailoverRoutingPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#RecordFailoverRoutingPolicy">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordFailoverRoutingPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordFailoverRoutingPolicyOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.RecordFailoverRoutingPolicyArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.RecordFailoverRoutingPolicy.html">output</a> API doc for this type.
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
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
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
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
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
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
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
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### RecordGeolocationRoutingPolicy
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#RecordGeolocationRoutingPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#RecordGeolocationRoutingPolicy">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordGeolocationRoutingPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordGeolocationRoutingPolicyOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.RecordGeolocationRoutingPolicyArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.RecordGeolocationRoutingPolicy.html">output</a> API doc for this type.
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
            <td class="align-top">Continent</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A two-letter continent code. See http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html for code details. Either `continent` or `country` must be specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Country</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A two-character country code or `*` to indicate a default resource record set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subdivision</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A subdivision code for a country.
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
            <td class="align-top">Continent</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A two-letter continent code. See http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html for code details. Either `continent` or `country` must be specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Country</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A two-character country code or `*` to indicate a default resource record set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subdivision</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A subdivision code for a country.
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
            <td class="align-top">continent</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A two-letter continent code. See http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html for code details. Either `continent` or `country` must be specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">country</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A two-character country code or `*` to indicate a default resource record set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subdivision</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A subdivision code for a country.
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
            <td class="align-top">continent</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A two-letter continent code. See http://docs.aws.amazon.com/Route53/latest/APIReference/API_GetGeoLocation.html for code details. Either `continent` or `country` must be specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">country</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A two-character country code or `*` to indicate a default resource record set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subdivision</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A subdivision code for a country.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### RecordLatencyRoutingPolicy
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#RecordLatencyRoutingPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#RecordLatencyRoutingPolicy">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordLatencyRoutingPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordLatencyRoutingPolicyOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.RecordLatencyRoutingPolicyArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.RecordLatencyRoutingPolicy.html">output</a> API doc for this type.
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
            <td class="align-top">Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An AWS region from which to measure latency. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency
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
            <td class="align-top">Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An AWS region from which to measure latency. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency
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
            <td class="align-top">region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An AWS region from which to measure latency. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency
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
            <td class="align-top">region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An AWS region from which to measure latency. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### RecordWeightedRoutingPolicy
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#RecordWeightedRoutingPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#RecordWeightedRoutingPolicy">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordWeightedRoutingPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/route53?tab=doc#RecordWeightedRoutingPolicyOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.RecordWeightedRoutingPolicyArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Route53.RecordWeightedRoutingPolicy.html">output</a> API doc for this type.
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
            <td class="align-top">Weight</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A numeric value indicating the relative weight of the record. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted.
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
            <td class="align-top">Weight</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A numeric value indicating the relative weight of the record. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted.
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
            <td class="align-top">weight</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A numeric value indicating the relative weight of the record. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted.
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
            <td class="align-top">weight</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A numeric value indicating the relative weight of the record. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







