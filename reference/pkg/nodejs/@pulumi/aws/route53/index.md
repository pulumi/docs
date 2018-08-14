---
title: Module route53
---

<a href="../index.html">@pulumi/aws</a> &gt; route53

<h2 class="pdoc-module-header">Index</h2>

* <a href="#DelegationSet">class DelegationSet</a>
* <a href="#HealthCheck">class HealthCheck</a>
* <a href="#QueryLog">class QueryLog</a>
* <a href="#Record">class Record</a>
* <a href="#Zone">class Zone</a>
* <a href="#ZoneAssociation">class ZoneAssociation</a>
* <a href="#getZone">function getZone</a>
* <a href="#DelegationSetArgs">interface DelegationSetArgs</a>
* <a href="#DelegationSetState">interface DelegationSetState</a>
* <a href="#GetZoneArgs">interface GetZoneArgs</a>
* <a href="#GetZoneResult">interface GetZoneResult</a>
* <a href="#HealthCheckArgs">interface HealthCheckArgs</a>
* <a href="#HealthCheckState">interface HealthCheckState</a>
* <a href="#QueryLogArgs">interface QueryLogArgs</a>
* <a href="#QueryLogState">interface QueryLogState</a>
* <a href="#RecordArgs">interface RecordArgs</a>
* <a href="#RecordState">interface RecordState</a>
* <a href="#ZoneArgs">interface ZoneArgs</a>
* <a href="#ZoneAssociationArgs">interface ZoneAssociationArgs</a>
* <a href="#ZoneAssociationState">interface ZoneAssociationState</a>
* <a href="#ZoneState">interface ZoneState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/delegationSet.ts">route53/delegationSet.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts">route53/getZone.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts">route53/healthCheck.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/queryLog.ts">route53/queryLog.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts">route53/record.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts">route53/zone.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zoneAssociation.ts">route53/zoneAssociation.ts</a> 


<h2 class="pdoc-module-header" id="DelegationSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/delegationSet.ts#L9">class DelegationSet</a>
</h2>

Provides a [Route53 Delegation Set](https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html) resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/delegationSet.ts#L31">constructor</a>
</h3>

```typescript
new DelegationSet(name: string, args?: DelegationSetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DelegationSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/delegationSet.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DelegationSetState): DelegationSet
```


Get an existing DelegationSet resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/delegationSet.ts#L26">property nameServers</a>
</h3>

```typescript
public nameServers: pulumi.Output<string[]>;
```


A list of authoritative name servers for the hosted zone
(effectively a list of NS records).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/delegationSet.ts#L31">property referenceName</a>
</h3>

```typescript
public referenceName: pulumi.Output<string | undefined>;
```


This is a reference name used in Caller Reference
(helpful for identifying single delegation set amongst others)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="HealthCheck">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L11">class HealthCheck</a>
</h2>

Provides a Route53 health check.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L100">constructor</a>
</h3>

```typescript
new HealthCheck(name: string, args: HealthCheckArgs, opts?: pulumi.CustomResourceOptions)
```


Create a HealthCheck resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HealthCheckState): HealthCheck
```


Get an existing HealthCheck resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L27">property childHealthThreshold</a>
</h3>

```typescript
public childHealthThreshold: pulumi.Output<number | undefined>;
```


The minimum number of child health checks that must be healthy for Route 53 to consider the parent health check to be healthy. Valid values are integers between 0 and 256, inclusive

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L31">property childHealthchecks</a>
</h3>

```typescript
public childHealthchecks: pulumi.Output<string[] | undefined>;
```


For a specified parent health check, a list of HealthCheckId values for the associated child health checks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L35">property cloudwatchAlarmName</a>
</h3>

```typescript
public cloudwatchAlarmName: pulumi.Output<string | undefined>;
```


The name of the CloudWatch alarm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L39">property cloudwatchAlarmRegion</a>
</h3>

```typescript
public cloudwatchAlarmRegion: pulumi.Output<string | undefined>;
```


The CloudWatchRegion that the CloudWatch alarm was created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L43">property enableSni</a>
</h3>

```typescript
public enableSni: pulumi.Output<boolean>;
```


A boolean value that indicates whether Route53 should send the `fqdn` to the endpoint when performing the health check. This defaults to AWS' defaults: when the `type` is "HTTPS" `enable_sni` defaults to `true`, when `type` is anything else `enable_sni` defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L47">property failureThreshold</a>
</h3>

```typescript
public failureThreshold: pulumi.Output<number | undefined>;
```


The number of consecutive health checks that an endpoint must pass or fail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L51">property fqdn</a>
</h3>

```typescript
public fqdn: pulumi.Output<string | undefined>;
```


The fully qualified domain name of the endpoint to be checked.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L55">property insufficientDataHealthStatus</a>
</h3>

```typescript
public insufficientDataHealthStatus: pulumi.Output<string | undefined>;
```


The status of the health check when CloudWatch has insufficient data about the state of associated alarm. Valid values are `Healthy` , `Unhealthy` and `LastKnownStatus`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L59">property invertHealthcheck</a>
</h3>

```typescript
public invertHealthcheck: pulumi.Output<boolean | undefined>;
```


A boolean value that indicates whether the status of health check should be inverted. For example, if a health check is healthy but Inverted is True , then Route 53 considers the health check to be unhealthy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L63">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string | undefined>;
```


The IP address of the endpoint to be checked.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L67">property measureLatency</a>
</h3>

```typescript
public measureLatency: pulumi.Output<boolean | undefined>;
```


A Boolean value that indicates whether you want Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint and to display CloudWatch latency graphs in the Route 53 console.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L71">property port</a>
</h3>

```typescript
public port: pulumi.Output<number | undefined>;
```


The port of the endpoint to be checked.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L76">property referenceName</a>
</h3>

```typescript
public referenceName: pulumi.Output<string | undefined>;
```


This is a reference name used in Caller Reference
(helpful for identifying single health_check set amongst others)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L80">property regions</a>
</h3>

```typescript
public regions: pulumi.Output<string[] | undefined>;
```


A list of AWS regions that you want Amazon Route 53 health checkers to check the specified endpoint from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L84">property requestInterval</a>
</h3>

```typescript
public requestInterval: pulumi.Output<number | undefined>;
```


The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L88">property resourcePath</a>
</h3>

```typescript
public resourcePath: pulumi.Output<string | undefined>;
```


The path that you want Amazon Route 53 to request when performing health checks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L92">property searchString</a>
</h3>

```typescript
public searchString: pulumi.Output<string | undefined>;
```


String searched in the first 5120 bytes of the response body for check to be considered healthy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L96">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the health check.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L100">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The protocol to use when performing health checks. Valid values are `HTTP`, `HTTPS`, `HTTP_STR_MATCH`, `HTTPS_STR_MATCH`, `TCP`, `CALCULATED` and `CLOUDWATCH_METRIC`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="QueryLog">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/queryLog.ts#L15">class QueryLog</a>
</h2>

Provides a Route53 query logging configuration resource.

~> **NOTE:** There are restrictions on the configuration of query logging. Notably,
the CloudWatch log group must be in the `us-east-1` region,
a permissive CloudWatch log resource policy must be in place, and
the Route53 hosted zone must be public.
See [Configuring Logging for DNS Queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html?console_help=true#query-logs-configuring) for additional details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/queryLog.ts#L35">constructor</a>
</h3>

```typescript
new QueryLog(name: string, args: QueryLogArgs, opts?: pulumi.CustomResourceOptions)
```


Create a QueryLog resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/queryLog.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: QueryLogState): QueryLog
```


Get an existing QueryLog resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/queryLog.ts#L31">property cloudwatchLogGroupArn</a>
</h3>

```typescript
public cloudwatchLogGroupArn: pulumi.Output<string>;
```


CloudWatch log group ARN to send query logs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/queryLog.ts#L35">property zoneId</a>
</h3>

```typescript
public zoneId: pulumi.Output<string>;
```


Route53 hosted zone ID to enable query logs.

<h2 class="pdoc-module-header" id="Record">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L9">class Record</a>
</h2>

Provides a Route53 record resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L82">constructor</a>
</h3>

```typescript
new Record(name: string, args: RecordArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Record resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RecordState): Record
```


Get an existing Record resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L26">property aliases</a>
</h3>

```typescript
public aliases: pulumi.Output<{ ... }[] | undefined>;
```


An alias block. Conflicts with `ttl` & `records`.
Alias record documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L30">property allowOverwrite</a>
</h3>

```typescript
public allowOverwrite: pulumi.Output<boolean | undefined>;
```


Allow creation of this record in Terraform to overwrite an existing record, if any. This does not prevent other resources within Terraform or manual Route53 changes from overwriting this record. `true` by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L34">property failoverRoutingPolicies</a>
</h3>

```typescript
public failoverRoutingPolicies: pulumi.Output<{ ... }[] | undefined>;
```


A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L38">property fqdn</a>
</h3>

```typescript
public fqdn: pulumi.Output<string>;
```


[FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L42">property geolocationRoutingPolicies</a>
</h3>

```typescript
public geolocationRoutingPolicies: pulumi.Output<{ ... }[] | undefined>;
```


A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L46">property healthCheckId</a>
</h3>

```typescript
public healthCheckId: pulumi.Output<string | undefined>;
```


The health check the record should be associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L50">property latencyRoutingPolicies</a>
</h3>

```typescript
public latencyRoutingPolicies: pulumi.Output<{ ... }[] | undefined>;
```


A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L54">property multivalueAnswerRoutingPolicy</a>
</h3>

```typescript
public multivalueAnswerRoutingPolicy: pulumi.Output<boolean | undefined>;
```


Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L58">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L62">property records</a>
</h3>

```typescript
public records: pulumi.Output<string[] | undefined>;
```


A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the Terraform configuration string (e.g. `"first255characters\"\"morecharacters"`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L66">property setIdentifier</a>
</h3>

```typescript
public setIdentifier: pulumi.Output<string | undefined>;
```


Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L70">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number | undefined>;
```


The TTL of the record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L74">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L78">property weightedRoutingPolicies</a>
</h3>

```typescript
public weightedRoutingPolicies: pulumi.Output<{ ... }[] | undefined>;
```


A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L82">property zoneId</a>
</h3>

```typescript
public zoneId: pulumi.Output<string>;
```


Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](/docs/providers/aws/r/elb.html#zone_id) for example.

<h2 class="pdoc-module-header" id="Zone">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L11">class Zone</a>
</h2>

Provides a Route53 Hosted Zone resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L63">constructor</a>
</h3>

```typescript
new Zone(name: string, args?: ZoneArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Zone resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ZoneState): Zone
```


Get an existing Zone resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L27">property comment</a>
</h3>

```typescript
public comment: pulumi.Output<string>;
```


A comment for the hosted zone. Defaults to 'Managed by Terraform'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L32">property delegationSetId</a>
</h3>

```typescript
public delegationSetId: pulumi.Output<string | undefined>;
```


The ID of the reusable delegation set whose NS records you want to assign to the hosted zone.
Conflicts w/ `vpc_id` as delegation sets can only be used for public zones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L37">property forceDestroy</a>
</h3>

```typescript
public forceDestroy: pulumi.Output<boolean | undefined>;
```


Whether to destroy all records (possibly managed outside of Terraform)
in the zone when destroying the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L41">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


This is the name of the hosted zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L46">property nameServers</a>
</h3>

```typescript
public nameServers: pulumi.Output<string[]>;
```


A list of name servers in associated (or default) delegation set.
Find more about delegation sets in [AWS docs](https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L50">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L55">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string | undefined>;
```


The VPC to associate with a private hosted zone. Specifying `vpc_id` will create a private hosted zone.
Conflicts w/ `delegation_set_id` as delegation sets can only be used for public zones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L59">property vpcRegion</a>
</h3>

```typescript
public vpcRegion: pulumi.Output<string>;
```


The VPC's region. Defaults to the region of the AWS provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L63">property zoneId</a>
</h3>

```typescript
public zoneId: pulumi.Output<string>;
```


The Hosted Zone ID. This can be referenced by zone records.

<h2 class="pdoc-module-header" id="ZoneAssociation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zoneAssociation.ts#L9">class ZoneAssociation</a>
</h2>

Provides a Route53 private Hosted Zone to VPC association resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zoneAssociation.ts#L33">constructor</a>
</h3>

```typescript
new ZoneAssociation(name: string, args: ZoneAssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ZoneAssociation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zoneAssociation.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ZoneAssociationState): ZoneAssociation
```


Get an existing ZoneAssociation resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zoneAssociation.ts#L25">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The VPC to associate with the private hosted zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zoneAssociation.ts#L29">property vpcRegion</a>
</h3>

```typescript
public vpcRegion: pulumi.Output<string>;
```


The VPC's region. Defaults to the region of the AWS provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zoneAssociation.ts#L33">property zoneId</a>
</h3>

```typescript
public zoneId: pulumi.Output<string>;
```


The private hosted zone to associate.

<h2 class="pdoc-module-header" id="getZone">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L11">function getZone</a>
</h2>

```typescript
getZone(args?: GetZoneArgs, opts?: pulumi.InvokeOptions): Promise<GetZoneResult>
```


`aws_route53_zone` provides details about a specific Route 53 Hosted Zone.

This data source allows to find a Hosted Zone ID given Hosted Zone name and certain search criteria.

<h2 class="pdoc-module-header" id="DelegationSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/delegationSet.ts#L75">interface DelegationSetArgs</a>
</h2>

The set of arguments for constructing a DelegationSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/delegationSet.ts#L80">property referenceName</a>
</h3>

```typescript
referenceName?: pulumi.Input<string>;
```


This is a reference name used in Caller Reference
(helpful for identifying single delegation set amongst others)

<h2 class="pdoc-module-header" id="DelegationSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/delegationSet.ts#L59">interface DelegationSetState</a>
</h2>

Input properties used for looking up and filtering DelegationSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/delegationSet.ts#L64">property nameServers</a>
</h3>

```typescript
nameServers?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of authoritative name servers for the hosted zone
(effectively a list of NS records).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/delegationSet.ts#L69">property referenceName</a>
</h3>

```typescript
referenceName?: pulumi.Input<string>;
```


This is a reference name used in Caller Reference
(helpful for identifying single delegation set amongst others)

<h2 class="pdoc-module-header" id="GetZoneArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L28">interface GetZoneArgs</a>
</h2>

A collection of arguments for invoking getZone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L29">property callerReference</a>
</h3>

```typescript
callerReference?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L30">property comment</a>
</h3>

```typescript
comment?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L34">property name</a>
</h3>

```typescript
name?: string;
```


The Hosted Zone name of the desired Hosted Zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L38">property privateZone</a>
</h3>

```typescript
privateZone?: boolean;
```


Used with `name` field to get a private Hosted Zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L39">property resourceRecordSetCount</a>
</h3>

```typescript
resourceRecordSetCount?: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L44">property tags</a>
</h3>

```typescript
tags?: { ... };
```


Used with `name` field. A mapping of tags, each pair of which must exactly match
a pair on the desired Hosted Zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L48">property vpcId</a>
</h3>

```typescript
vpcId?: string;
```


Used with `name` field to get a private Hosted Zone associated with the vpc_id (in this case, private_zone is not mandatory).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L52">property zoneId</a>
</h3>

```typescript
zoneId?: string;
```


The Hosted Zone id of the desired Hosted Zone.

<h2 class="pdoc-module-header" id="GetZoneResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L58">interface GetZoneResult</a>
</h2>

A collection of values returned by getZone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L62">property callerReference</a>
</h3>

```typescript
callerReference: string;
```


Caller Reference of the Hosted Zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L66">property comment</a>
</h3>

```typescript
comment: string;
```


The comment field of the Hosted Zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L82">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L67">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L71">property nameServers</a>
</h3>

```typescript
nameServers: string[];
```


The list of DNS name servers for the Hosted Zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L75">property resourceRecordSetCount</a>
</h3>

```typescript
resourceRecordSetCount: number;
```


the number of Record Set in the Hosted Zone

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L76">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L77">property vpcId</a>
</h3>

```typescript
vpcId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/getZone.ts#L78">property zoneId</a>
</h3>

```typescript
zoneId: string;
```

<h2 class="pdoc-module-header" id="HealthCheckArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L248">interface HealthCheckArgs</a>
</h2>

The set of arguments for constructing a HealthCheck resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L252">property childHealthThreshold</a>
</h3>

```typescript
childHealthThreshold?: pulumi.Input<number>;
```


The minimum number of child health checks that must be healthy for Route 53 to consider the parent health check to be healthy. Valid values are integers between 0 and 256, inclusive

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L256">property childHealthchecks</a>
</h3>

```typescript
childHealthchecks?: pulumi.Input<pulumi.Input<string>[]>;
```


For a specified parent health check, a list of HealthCheckId values for the associated child health checks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L260">property cloudwatchAlarmName</a>
</h3>

```typescript
cloudwatchAlarmName?: pulumi.Input<string>;
```


The name of the CloudWatch alarm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L264">property cloudwatchAlarmRegion</a>
</h3>

```typescript
cloudwatchAlarmRegion?: pulumi.Input<string>;
```


The CloudWatchRegion that the CloudWatch alarm was created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L268">property enableSni</a>
</h3>

```typescript
enableSni?: pulumi.Input<boolean>;
```


A boolean value that indicates whether Route53 should send the `fqdn` to the endpoint when performing the health check. This defaults to AWS' defaults: when the `type` is "HTTPS" `enable_sni` defaults to `true`, when `type` is anything else `enable_sni` defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L272">property failureThreshold</a>
</h3>

```typescript
failureThreshold?: pulumi.Input<number>;
```


The number of consecutive health checks that an endpoint must pass or fail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L276">property fqdn</a>
</h3>

```typescript
fqdn?: pulumi.Input<string>;
```


The fully qualified domain name of the endpoint to be checked.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L280">property insufficientDataHealthStatus</a>
</h3>

```typescript
insufficientDataHealthStatus?: pulumi.Input<string>;
```


The status of the health check when CloudWatch has insufficient data about the state of associated alarm. Valid values are `Healthy` , `Unhealthy` and `LastKnownStatus`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L284">property invertHealthcheck</a>
</h3>

```typescript
invertHealthcheck?: pulumi.Input<boolean>;
```


A boolean value that indicates whether the status of health check should be inverted. For example, if a health check is healthy but Inverted is True , then Route 53 considers the health check to be unhealthy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L288">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The IP address of the endpoint to be checked.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L292">property measureLatency</a>
</h3>

```typescript
measureLatency?: pulumi.Input<boolean>;
```


A Boolean value that indicates whether you want Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint and to display CloudWatch latency graphs in the Route 53 console.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L296">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port of the endpoint to be checked.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L301">property referenceName</a>
</h3>

```typescript
referenceName?: pulumi.Input<string>;
```


This is a reference name used in Caller Reference
(helpful for identifying single health_check set amongst others)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L305">property regions</a>
</h3>

```typescript
regions?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of AWS regions that you want Amazon Route 53 health checkers to check the specified endpoint from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L309">property requestInterval</a>
</h3>

```typescript
requestInterval?: pulumi.Input<number>;
```


The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L313">property resourcePath</a>
</h3>

```typescript
resourcePath?: pulumi.Input<string>;
```


The path that you want Amazon Route 53 to request when performing health checks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L317">property searchString</a>
</h3>

```typescript
searchString?: pulumi.Input<string>;
```


String searched in the first 5120 bytes of the response body for check to be considered healthy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L321">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the health check.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L325">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The protocol to use when performing health checks. Valid values are `HTTP`, `HTTPS`, `HTTP_STR_MATCH`, `HTTPS_STR_MATCH`, `TCP`, `CALCULATED` and `CLOUDWATCH_METRIC`.

<h2 class="pdoc-module-header" id="HealthCheckState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L165">interface HealthCheckState</a>
</h2>

Input properties used for looking up and filtering HealthCheck resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L169">property childHealthThreshold</a>
</h3>

```typescript
childHealthThreshold?: pulumi.Input<number>;
```


The minimum number of child health checks that must be healthy for Route 53 to consider the parent health check to be healthy. Valid values are integers between 0 and 256, inclusive

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L173">property childHealthchecks</a>
</h3>

```typescript
childHealthchecks?: pulumi.Input<pulumi.Input<string>[]>;
```


For a specified parent health check, a list of HealthCheckId values for the associated child health checks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L177">property cloudwatchAlarmName</a>
</h3>

```typescript
cloudwatchAlarmName?: pulumi.Input<string>;
```


The name of the CloudWatch alarm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L181">property cloudwatchAlarmRegion</a>
</h3>

```typescript
cloudwatchAlarmRegion?: pulumi.Input<string>;
```


The CloudWatchRegion that the CloudWatch alarm was created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L185">property enableSni</a>
</h3>

```typescript
enableSni?: pulumi.Input<boolean>;
```


A boolean value that indicates whether Route53 should send the `fqdn` to the endpoint when performing the health check. This defaults to AWS' defaults: when the `type` is "HTTPS" `enable_sni` defaults to `true`, when `type` is anything else `enable_sni` defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L189">property failureThreshold</a>
</h3>

```typescript
failureThreshold?: pulumi.Input<number>;
```


The number of consecutive health checks that an endpoint must pass or fail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L193">property fqdn</a>
</h3>

```typescript
fqdn?: pulumi.Input<string>;
```


The fully qualified domain name of the endpoint to be checked.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L197">property insufficientDataHealthStatus</a>
</h3>

```typescript
insufficientDataHealthStatus?: pulumi.Input<string>;
```


The status of the health check when CloudWatch has insufficient data about the state of associated alarm. Valid values are `Healthy` , `Unhealthy` and `LastKnownStatus`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L201">property invertHealthcheck</a>
</h3>

```typescript
invertHealthcheck?: pulumi.Input<boolean>;
```


A boolean value that indicates whether the status of health check should be inverted. For example, if a health check is healthy but Inverted is True , then Route 53 considers the health check to be unhealthy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L205">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The IP address of the endpoint to be checked.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L209">property measureLatency</a>
</h3>

```typescript
measureLatency?: pulumi.Input<boolean>;
```


A Boolean value that indicates whether you want Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint and to display CloudWatch latency graphs in the Route 53 console.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L213">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```


The port of the endpoint to be checked.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L218">property referenceName</a>
</h3>

```typescript
referenceName?: pulumi.Input<string>;
```


This is a reference name used in Caller Reference
(helpful for identifying single health_check set amongst others)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L222">property regions</a>
</h3>

```typescript
regions?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of AWS regions that you want Amazon Route 53 health checkers to check the specified endpoint from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L226">property requestInterval</a>
</h3>

```typescript
requestInterval?: pulumi.Input<number>;
```


The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L230">property resourcePath</a>
</h3>

```typescript
resourcePath?: pulumi.Input<string>;
```


The path that you want Amazon Route 53 to request when performing health checks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L234">property searchString</a>
</h3>

```typescript
searchString?: pulumi.Input<string>;
```


String searched in the first 5120 bytes of the response body for check to be considered healthy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L238">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the health check.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/healthCheck.ts#L242">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The protocol to use when performing health checks. Valid values are `HTTP`, `HTTPS`, `HTTP_STR_MATCH`, `HTTPS_STR_MATCH`, `TCP`, `CALCULATED` and `CLOUDWATCH_METRIC`.

<h2 class="pdoc-module-header" id="QueryLogArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/queryLog.ts#L83">interface QueryLogArgs</a>
</h2>

The set of arguments for constructing a QueryLog resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/queryLog.ts#L87">property cloudwatchLogGroupArn</a>
</h3>

```typescript
cloudwatchLogGroupArn: pulumi.Input<string>;
```


CloudWatch log group ARN to send query logs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/queryLog.ts#L91">property zoneId</a>
</h3>

```typescript
zoneId: pulumi.Input<string>;
```


Route53 hosted zone ID to enable query logs.

<h2 class="pdoc-module-header" id="QueryLogState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/queryLog.ts#L69">interface QueryLogState</a>
</h2>

Input properties used for looking up and filtering QueryLog resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/queryLog.ts#L73">property cloudwatchLogGroupArn</a>
</h3>

```typescript
cloudwatchLogGroupArn?: pulumi.Input<string>;
```


CloudWatch log group ARN to send query logs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/queryLog.ts#L77">property zoneId</a>
</h3>

```typescript
zoneId?: pulumi.Input<string>;
```


Route53 hosted zone ID to enable query logs.

<h2 class="pdoc-module-header" id="RecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L209">interface RecordArgs</a>
</h2>

The set of arguments for constructing a Record resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L214">property aliases</a>
</h3>

```typescript
aliases?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An alias block. Conflicts with `ttl` & `records`.
Alias record documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L218">property allowOverwrite</a>
</h3>

```typescript
allowOverwrite?: pulumi.Input<boolean>;
```


Allow creation of this record in Terraform to overwrite an existing record, if any. This does not prevent other resources within Terraform or manual Route53 changes from overwriting this record. `true` by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L222">property failoverRoutingPolicies</a>
</h3>

```typescript
failoverRoutingPolicies?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L226">property geolocationRoutingPolicies</a>
</h3>

```typescript
geolocationRoutingPolicies?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L230">property healthCheckId</a>
</h3>

```typescript
healthCheckId?: pulumi.Input<string>;
```


The health check the record should be associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L234">property latencyRoutingPolicies</a>
</h3>

```typescript
latencyRoutingPolicies?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L238">property multivalueAnswerRoutingPolicy</a>
</h3>

```typescript
multivalueAnswerRoutingPolicy?: pulumi.Input<boolean>;
```


Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L242">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L246">property records</a>
</h3>

```typescript
records?: pulumi.Input<pulumi.Input<string>[]>;
```


A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the Terraform configuration string (e.g. `"first255characters\"\"morecharacters"`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L250">property setIdentifier</a>
</h3>

```typescript
setIdentifier?: pulumi.Input<string>;
```


Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L254">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The TTL of the record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L258">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L262">property weightedRoutingPolicies</a>
</h3>

```typescript
weightedRoutingPolicies?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L266">property zoneId</a>
</h3>

```typescript
zoneId: pulumi.Input<string>;
```


Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](/docs/providers/aws/r/elb.html#zone_id) for example.

<h2 class="pdoc-module-header" id="RecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L142">interface RecordState</a>
</h2>

Input properties used for looking up and filtering Record resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L147">property aliases</a>
</h3>

```typescript
aliases?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An alias block. Conflicts with `ttl` & `records`.
Alias record documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L151">property allowOverwrite</a>
</h3>

```typescript
allowOverwrite?: pulumi.Input<boolean>;
```


Allow creation of this record in Terraform to overwrite an existing record, if any. This does not prevent other resources within Terraform or manual Route53 changes from overwriting this record. `true` by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L155">property failoverRoutingPolicies</a>
</h3>

```typescript
failoverRoutingPolicies?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L159">property fqdn</a>
</h3>

```typescript
fqdn?: pulumi.Input<string>;
```


[FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L163">property geolocationRoutingPolicies</a>
</h3>

```typescript
geolocationRoutingPolicies?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L167">property healthCheckId</a>
</h3>

```typescript
healthCheckId?: pulumi.Input<string>;
```


The health check the record should be associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L171">property latencyRoutingPolicies</a>
</h3>

```typescript
latencyRoutingPolicies?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L175">property multivalueAnswerRoutingPolicy</a>
</h3>

```typescript
multivalueAnswerRoutingPolicy?: pulumi.Input<boolean>;
```


Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L179">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L183">property records</a>
</h3>

```typescript
records?: pulumi.Input<pulumi.Input<string>[]>;
```


A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the Terraform configuration string (e.g. `"first255characters\"\"morecharacters"`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L187">property setIdentifier</a>
</h3>

```typescript
setIdentifier?: pulumi.Input<string>;
```


Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L191">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The TTL of the record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L195">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


`PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L199">property weightedRoutingPolicies</a>
</h3>

```typescript
weightedRoutingPolicies?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/record.ts#L203">property zoneId</a>
</h3>

```typescript
zoneId?: pulumi.Input<string>;
```


Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](/docs/providers/aws/r/elb.html#zone_id) for example.

<h2 class="pdoc-module-header" id="ZoneArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L151">interface ZoneArgs</a>
</h2>

The set of arguments for constructing a Zone resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L155">property comment</a>
</h3>

```typescript
comment?: pulumi.Input<string>;
```


A comment for the hosted zone. Defaults to 'Managed by Terraform'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L160">property delegationSetId</a>
</h3>

```typescript
delegationSetId?: pulumi.Input<string>;
```


The ID of the reusable delegation set whose NS records you want to assign to the hosted zone.
Conflicts w/ `vpc_id` as delegation sets can only be used for public zones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L165">property forceDestroy</a>
</h3>

```typescript
forceDestroy?: pulumi.Input<boolean>;
```


Whether to destroy all records (possibly managed outside of Terraform)
in the zone when destroying the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L169">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


This is the name of the hosted zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L173">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L178">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC to associate with a private hosted zone. Specifying `vpc_id` will create a private hosted zone.
Conflicts w/ `delegation_set_id` as delegation sets can only be used for public zones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L182">property vpcRegion</a>
</h3>

```typescript
vpcRegion?: pulumi.Input<string>;
```


The VPC's region. Defaults to the region of the AWS provider.

<h2 class="pdoc-module-header" id="ZoneAssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zoneAssociation.ts#L87">interface ZoneAssociationArgs</a>
</h2>

The set of arguments for constructing a ZoneAssociation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zoneAssociation.ts#L91">property vpcId</a>
</h3>

```typescript
vpcId: pulumi.Input<string>;
```


The VPC to associate with the private hosted zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zoneAssociation.ts#L95">property vpcRegion</a>
</h3>

```typescript
vpcRegion?: pulumi.Input<string>;
```


The VPC's region. Defaults to the region of the AWS provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zoneAssociation.ts#L99">property zoneId</a>
</h3>

```typescript
zoneId: pulumi.Input<string>;
```


The private hosted zone to associate.

<h2 class="pdoc-module-header" id="ZoneAssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zoneAssociation.ts#L69">interface ZoneAssociationState</a>
</h2>

Input properties used for looking up and filtering ZoneAssociation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zoneAssociation.ts#L73">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC to associate with the private hosted zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zoneAssociation.ts#L77">property vpcRegion</a>
</h3>

```typescript
vpcRegion?: pulumi.Input<string>;
```


The VPC's region. Defaults to the region of the AWS provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zoneAssociation.ts#L81">property zoneId</a>
</h3>

```typescript
zoneId?: pulumi.Input<string>;
```


The private hosted zone to associate.

<h2 class="pdoc-module-header" id="ZoneState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L105">interface ZoneState</a>
</h2>

Input properties used for looking up and filtering Zone resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L109">property comment</a>
</h3>

```typescript
comment?: pulumi.Input<string>;
```


A comment for the hosted zone. Defaults to 'Managed by Terraform'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L114">property delegationSetId</a>
</h3>

```typescript
delegationSetId?: pulumi.Input<string>;
```


The ID of the reusable delegation set whose NS records you want to assign to the hosted zone.
Conflicts w/ `vpc_id` as delegation sets can only be used for public zones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L119">property forceDestroy</a>
</h3>

```typescript
forceDestroy?: pulumi.Input<boolean>;
```


Whether to destroy all records (possibly managed outside of Terraform)
in the zone when destroying the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L123">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


This is the name of the hosted zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L128">property nameServers</a>
</h3>

```typescript
nameServers?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of name servers in associated (or default) delegation set.
Find more about delegation sets in [AWS docs](https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L132">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L137">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC to associate with a private hosted zone. Specifying `vpc_id` will create a private hosted zone.
Conflicts w/ `delegation_set_id` as delegation sets can only be used for public zones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L141">property vpcRegion</a>
</h3>

```typescript
vpcRegion?: pulumi.Input<string>;
```


The VPC's region. Defaults to the region of the AWS provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/route53/zone.ts#L145">property zoneId</a>
</h3>

```typescript
zoneId?: pulumi.Input<string>;
```


The Hosted Zone ID. This can be referenced by zone records.

