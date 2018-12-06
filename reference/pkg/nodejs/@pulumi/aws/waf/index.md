---
title: Module waf
---

<a href="../index.html">@pulumi/aws</a> &gt; waf

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ByteMatchSet">class ByteMatchSet</a>
* <a href="#GeoMatchSet">class GeoMatchSet</a>
* <a href="#IpSet">class IpSet</a>
* <a href="#RateBasedRule">class RateBasedRule</a>
* <a href="#RegexMatchSet">class RegexMatchSet</a>
* <a href="#RegexPatternSet">class RegexPatternSet</a>
* <a href="#Rule">class Rule</a>
* <a href="#RuleGroup">class RuleGroup</a>
* <a href="#SizeConstraintSet">class SizeConstraintSet</a>
* <a href="#SqlInjectionMatchSet">class SqlInjectionMatchSet</a>
* <a href="#WebAcl">class WebAcl</a>
* <a href="#XssMatchSet">class XssMatchSet</a>
* <a href="#ByteMatchSetArgs">interface ByteMatchSetArgs</a>
* <a href="#ByteMatchSetState">interface ByteMatchSetState</a>
* <a href="#GeoMatchSetArgs">interface GeoMatchSetArgs</a>
* <a href="#GeoMatchSetState">interface GeoMatchSetState</a>
* <a href="#IpSetArgs">interface IpSetArgs</a>
* <a href="#IpSetState">interface IpSetState</a>
* <a href="#RateBasedRuleArgs">interface RateBasedRuleArgs</a>
* <a href="#RateBasedRuleState">interface RateBasedRuleState</a>
* <a href="#RegexMatchSetArgs">interface RegexMatchSetArgs</a>
* <a href="#RegexMatchSetState">interface RegexMatchSetState</a>
* <a href="#RegexPatternSetArgs">interface RegexPatternSetArgs</a>
* <a href="#RegexPatternSetState">interface RegexPatternSetState</a>
* <a href="#RuleArgs">interface RuleArgs</a>
* <a href="#RuleGroupArgs">interface RuleGroupArgs</a>
* <a href="#RuleGroupState">interface RuleGroupState</a>
* <a href="#RuleState">interface RuleState</a>
* <a href="#SizeConstraintSetArgs">interface SizeConstraintSetArgs</a>
* <a href="#SizeConstraintSetState">interface SizeConstraintSetState</a>
* <a href="#SqlInjectionMatchSetArgs">interface SqlInjectionMatchSetArgs</a>
* <a href="#SqlInjectionMatchSetState">interface SqlInjectionMatchSetState</a>
* <a href="#WebAclArgs">interface WebAclArgs</a>
* <a href="#WebAclState">interface WebAclState</a>
* <a href="#XssMatchSetArgs">interface XssMatchSetArgs</a>
* <a href="#XssMatchSetState">interface XssMatchSetState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/byteMatchSet.ts">waf/byteMatchSet.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/geoMatchSet.ts">waf/geoMatchSet.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ipSet.ts">waf/ipSet.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts">waf/rateBasedRule.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexMatchSet.ts">waf/regexMatchSet.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexPatternSet.ts">waf/regexPatternSet.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rule.ts">waf/rule.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ruleGroup.ts">waf/ruleGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sizeConstraintSet.ts">waf/sizeConstraintSet.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sqlInjectionMatchSet.ts">waf/sqlInjectionMatchSet.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts">waf/webAcl.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/xssMatchSet.ts">waf/xssMatchSet.ts</a> 


<h2 class="pdoc-module-header" id="ByteMatchSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/byteMatchSet.ts#L10">class ByteMatchSet</a>
</h2>

Provides a WAF Byte Match Set Resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/byteMatchSet.ts#L32">constructor</a>
</h3>

```typescript
new ByteMatchSet(name: string, args?: ByteMatchSetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ByteMatchSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/byteMatchSet.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ByteMatchSetState): ByteMatchSet
```


Get an existing ByteMatchSet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/byteMatchSet.ts#L28">property byteMatchTuples</a>
</h3>

```typescript
public byteMatchTuples: pulumi.Output<{ ... }[] | undefined>;
```


Specifies the bytes (typically a string that corresponds
with ASCII characters) that you want to search for in web requests,
the location in requests that you want to search, and other settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/byteMatchSet.ts#L32">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name or description of the Byte Match Set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="GeoMatchSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/geoMatchSet.ts#L10">class GeoMatchSet</a>
</h2>

Provides a WAF Geo Match Set Resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/geoMatchSet.ts#L30">constructor</a>
</h3>

```typescript
new GeoMatchSet(name: string, args?: GeoMatchSetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a GeoMatchSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/geoMatchSet.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GeoMatchSetState): GeoMatchSet
```


Get an existing GeoMatchSet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/geoMatchSet.ts#L26">property geoMatchConstraints</a>
</h3>

```typescript
public geoMatchConstraints: pulumi.Output<{ ... }[] | undefined>;
```


The GeoMatchConstraint objects which contain the country that you want AWS WAF to search for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/geoMatchSet.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name or description of the GeoMatchSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IpSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ipSet.ts#L10">class IpSet</a>
</h2>

Provides a WAF IPSet Resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ipSet.ts#L34">constructor</a>
</h3>

```typescript
new IpSet(name: string, args?: IpSetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IpSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ipSet.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IpSetState): IpSet
```


Get an existing IpSet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ipSet.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the WAF IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ipSet.ts#L30">property ipSetDescriptors</a>
</h3>

```typescript
public ipSetDescriptors: pulumi.Output<{ ... }[] | undefined>;
```


One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR format) from which web requests originate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ipSet.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name or description of the IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RateBasedRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L10">class RateBasedRule</a>
</h2>

Provides a WAF Rate Based Rule Resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L42">constructor</a>
</h3>

```typescript
new RateBasedRule(name: string, args: RateBasedRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RateBasedRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RateBasedRuleState): RateBasedRule
```


Get an existing RateBasedRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L26">property metricName</a>
</h3>

```typescript
public metricName: pulumi.Output<string>;
```


The name or description for the Amazon CloudWatch metric of this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name or description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L34">property predicates</a>
</h3>

```typescript
public predicates: pulumi.Output<{ ... }[] | undefined>;
```


One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L38">property rateKey</a>
</h3>

```typescript
public rateKey: pulumi.Output<string>;
```


Valid value is IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L42">property rateLimit</a>
</h3>

```typescript
public rateLimit: pulumi.Output<number>;
```


The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 2000.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RegexMatchSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexMatchSet.ts#L10">class RegexMatchSet</a>
</h2>

Provides a WAF Regex Match Set Resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexMatchSet.ts#L31">constructor</a>
</h3>

```typescript
new RegexMatchSet(name: string, args?: RegexMatchSetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RegexMatchSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexMatchSet.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RegexMatchSetState): RegexMatchSet
```


Get an existing RegexMatchSet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexMatchSet.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name or description of the Regex Match Set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexMatchSet.ts#L31">property regexMatchTuples</a>
</h3>

```typescript
public regexMatchTuples: pulumi.Output<{ ... }[] | undefined>;
```


The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RegexPatternSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexPatternSet.ts#L10">class RegexPatternSet</a>
</h2>

Provides a WAF Regex Pattern Set Resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexPatternSet.ts#L30">constructor</a>
</h3>

```typescript
new RegexPatternSet(name: string, args?: RegexPatternSetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RegexPatternSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexPatternSet.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RegexPatternSetState): RegexPatternSet
```


Get an existing RegexPatternSet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexPatternSet.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name or description of the Regex Pattern Set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexPatternSet.ts#L30">property regexPatternStrings</a>
</h3>

```typescript
public regexPatternStrings: pulumi.Output<string[] | undefined>;
```


A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Rule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rule.ts#L10">class Rule</a>
</h2>

Provides a WAF Rule Resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rule.ts#L34">constructor</a>
</h3>

```typescript
new Rule(name: string, args: RuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Rule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rule.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RuleState): Rule
```


Get an existing Rule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rule.ts#L26">property metricName</a>
</h3>

```typescript
public metricName: pulumi.Output<string>;
```


The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rule.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name or description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rule.ts#L34">property predicates</a>
</h3>

```typescript
public predicates: pulumi.Output<{ ... }[] | undefined>;
```


One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RuleGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ruleGroup.ts#L10">class RuleGroup</a>
</h2>

Provides a WAF Rule Group Resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ruleGroup.ts#L34">constructor</a>
</h3>

```typescript
new RuleGroup(name: string, args: RuleGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RuleGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ruleGroup.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RuleGroupState): RuleGroup
```


Get an existing RuleGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ruleGroup.ts#L26">property activatedRules</a>
</h3>

```typescript
public activatedRules: pulumi.Output<{ ... }[] | undefined>;
```


A list of activated rules, see below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ruleGroup.ts#L30">property metricName</a>
</h3>

```typescript
public metricName: pulumi.Output<string>;
```


A friendly name for the metrics from the rule group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ruleGroup.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A friendly name of the rule group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SizeConstraintSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sizeConstraintSet.ts#L10">class SizeConstraintSet</a>
</h2>

Provides a WAF Size Constraint Set Resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sizeConstraintSet.ts#L30">constructor</a>
</h3>

```typescript
new SizeConstraintSet(name: string, args?: SizeConstraintSetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SizeConstraintSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sizeConstraintSet.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SizeConstraintSetState): SizeConstraintSet
```


Get an existing SizeConstraintSet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sizeConstraintSet.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name or description of the Size Constraint Set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sizeConstraintSet.ts#L30">property sizeConstraints</a>
</h3>

```typescript
public sizeConstraints: pulumi.Output<{ ... }[] | undefined>;
```


Specifies the parts of web requests that you want to inspect the size of.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SqlInjectionMatchSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sqlInjectionMatchSet.ts#L10">class SqlInjectionMatchSet</a>
</h2>

Provides a WAF SQL Injection Match Set Resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sqlInjectionMatchSet.ts#L30">constructor</a>
</h3>

```typescript
new SqlInjectionMatchSet(name: string, args?: SqlInjectionMatchSetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SqlInjectionMatchSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sqlInjectionMatchSet.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SqlInjectionMatchSetState): SqlInjectionMatchSet
```


Get an existing SqlInjectionMatchSet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sqlInjectionMatchSet.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name or description of the SizeConstraintSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sqlInjectionMatchSet.ts#L30">property sqlInjectionMatchTuples</a>
</h3>

```typescript
public sqlInjectionMatchTuples: pulumi.Output<{ ... }[] | undefined>;
```


The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="WebAcl">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts#L10">class WebAcl</a>
</h2>

Provides a WAF Web ACL Resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts#L38">constructor</a>
</h3>

```typescript
new WebAcl(name: string, args: WebAclArgs, opts?: pulumi.CustomResourceOptions)
```


Create a WebAcl resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WebAclState): WebAcl
```


Get an existing WebAcl resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts#L26">property defaultAction</a>
</h3>

```typescript
public defaultAction: pulumi.Output<{ ... }>;
```


The action that you want AWS WAF to take when a request doesn't match the criteria in any of the rules that are associated with the web ACL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts#L30">property metricName</a>
</h3>

```typescript
public metricName: pulumi.Output<string>;
```


The name or description for the Amazon CloudWatch metric of this web ACL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name or description of the web ACL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts#L38">property rules</a>
</h3>

```typescript
public rules: pulumi.Output<{ ... }[] | undefined>;
```


The rules to associate with the web ACL and the settings for each rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="XssMatchSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/xssMatchSet.ts#L10">class XssMatchSet</a>
</h2>

Provides a WAF XSS Match Set Resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/xssMatchSet.ts#L30">constructor</a>
</h3>

```typescript
new XssMatchSet(name: string, args?: XssMatchSetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a XssMatchSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/xssMatchSet.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: XssMatchSetState): XssMatchSet
```


Get an existing XssMatchSet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/xssMatchSet.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name or description of the SizeConstraintSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/xssMatchSet.ts#L30">property xssMatchTuples</a>
</h3>

```typescript
public xssMatchTuples: pulumi.Output<{ ... }[] | undefined>;
```


The parts of web requests that you want to inspect for cross-site scripting attacks.

<h2 class="pdoc-module-header" id="ByteMatchSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/byteMatchSet.ts#L76">interface ByteMatchSetArgs</a>
</h2>

The set of arguments for constructing a ByteMatchSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/byteMatchSet.ts#L82">property byteMatchTuples</a>
</h3>

```typescript
byteMatchTuples?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies the bytes (typically a string that corresponds
with ASCII characters) that you want to search for in web requests,
the location in requests that you want to search, and other settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/byteMatchSet.ts#L86">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the Byte Match Set.

<h2 class="pdoc-module-header" id="ByteMatchSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/byteMatchSet.ts#L60">interface ByteMatchSetState</a>
</h2>

Input properties used for looking up and filtering ByteMatchSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/byteMatchSet.ts#L66">property byteMatchTuples</a>
</h3>

```typescript
byteMatchTuples?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies the bytes (typically a string that corresponds
with ASCII characters) that you want to search for in web requests,
the location in requests that you want to search, and other settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/byteMatchSet.ts#L70">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the Byte Match Set.

<h2 class="pdoc-module-header" id="GeoMatchSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/geoMatchSet.ts#L72">interface GeoMatchSetArgs</a>
</h2>

The set of arguments for constructing a GeoMatchSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/geoMatchSet.ts#L76">property geoMatchConstraints</a>
</h3>

```typescript
geoMatchConstraints?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The GeoMatchConstraint objects which contain the country that you want AWS WAF to search for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/geoMatchSet.ts#L80">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the GeoMatchSet.

<h2 class="pdoc-module-header" id="GeoMatchSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/geoMatchSet.ts#L58">interface GeoMatchSetState</a>
</h2>

Input properties used for looking up and filtering GeoMatchSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/geoMatchSet.ts#L62">property geoMatchConstraints</a>
</h3>

```typescript
geoMatchConstraints?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The GeoMatchConstraint objects which contain the country that you want AWS WAF to search for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/geoMatchSet.ts#L66">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the GeoMatchSet.

<h2 class="pdoc-module-header" id="IpSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ipSet.ts#L82">interface IpSetArgs</a>
</h2>

The set of arguments for constructing a IpSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ipSet.ts#L86">property ipSetDescriptors</a>
</h3>

```typescript
ipSetDescriptors?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR format) from which web requests originate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ipSet.ts#L90">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the IPSet.

<h2 class="pdoc-module-header" id="IpSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ipSet.ts#L64">interface IpSetState</a>
</h2>

Input properties used for looking up and filtering IpSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ipSet.ts#L68">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the WAF IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ipSet.ts#L72">property ipSetDescriptors</a>
</h3>

```typescript
ipSetDescriptors?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more pairs specifying the IP address type (IPV4 or IPV6) and the IP address range (in CIDR format) from which web requests originate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ipSet.ts#L76">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the IPSet.

<h2 class="pdoc-module-header" id="RateBasedRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L111">interface RateBasedRuleArgs</a>
</h2>

The set of arguments for constructing a RateBasedRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L115">property metricName</a>
</h3>

```typescript
metricName: pulumi.Input<string>;
```


The name or description for the Amazon CloudWatch metric of this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L119">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L123">property predicates</a>
</h3>

```typescript
predicates?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L127">property rateKey</a>
</h3>

```typescript
rateKey: pulumi.Input<string>;
```


Valid value is IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L131">property rateLimit</a>
</h3>

```typescript
rateLimit: pulumi.Input<number>;
```


The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 2000.

<h2 class="pdoc-module-header" id="RateBasedRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L85">interface RateBasedRuleState</a>
</h2>

Input properties used for looking up and filtering RateBasedRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L89">property metricName</a>
</h3>

```typescript
metricName?: pulumi.Input<string>;
```


The name or description for the Amazon CloudWatch metric of this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L93">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L97">property predicates</a>
</h3>

```typescript
predicates?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L101">property rateKey</a>
</h3>

```typescript
rateKey?: pulumi.Input<string>;
```


Valid value is IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rateBasedRule.ts#L105">property rateLimit</a>
</h3>

```typescript
rateLimit?: pulumi.Input<number>;
```


The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 2000.

<h2 class="pdoc-module-header" id="RegexMatchSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexMatchSet.ts#L74">interface RegexMatchSetArgs</a>
</h2>

The set of arguments for constructing a RegexMatchSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexMatchSet.ts#L78">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the Regex Match Set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexMatchSet.ts#L83">property regexMatchTuples</a>
</h3>

```typescript
regexMatchTuples?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.

<h2 class="pdoc-module-header" id="RegexMatchSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexMatchSet.ts#L59">interface RegexMatchSetState</a>
</h2>

Input properties used for looking up and filtering RegexMatchSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexMatchSet.ts#L63">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the Regex Match Set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexMatchSet.ts#L68">property regexMatchTuples</a>
</h3>

```typescript
regexMatchTuples?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The regular expression pattern that you want AWS WAF to search for in web requests,
the location in requests that you want AWS WAF to search, and other settings. See below.

<h2 class="pdoc-module-header" id="RegexPatternSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexPatternSet.ts#L72">interface RegexPatternSetArgs</a>
</h2>

The set of arguments for constructing a RegexPatternSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexPatternSet.ts#L76">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the Regex Pattern Set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexPatternSet.ts#L80">property regexPatternStrings</a>
</h3>

```typescript
regexPatternStrings?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.

<h2 class="pdoc-module-header" id="RegexPatternSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexPatternSet.ts#L58">interface RegexPatternSetState</a>
</h2>

Input properties used for looking up and filtering RegexPatternSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexPatternSet.ts#L62">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the Regex Pattern Set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/regexPatternSet.ts#L66">property regexPatternStrings</a>
</h3>

```typescript
regexPatternStrings?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.

<h2 class="pdoc-module-header" id="RuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rule.ts#L85">interface RuleArgs</a>
</h2>

The set of arguments for constructing a Rule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rule.ts#L89">property metricName</a>
</h3>

```typescript
metricName: pulumi.Input<string>;
```


The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rule.ts#L93">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rule.ts#L97">property predicates</a>
</h3>

```typescript
predicates?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.

<h2 class="pdoc-module-header" id="RuleGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ruleGroup.ts#L85">interface RuleGroupArgs</a>
</h2>

The set of arguments for constructing a RuleGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ruleGroup.ts#L89">property activatedRules</a>
</h3>

```typescript
activatedRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of activated rules, see below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ruleGroup.ts#L93">property metricName</a>
</h3>

```typescript
metricName: pulumi.Input<string>;
```


A friendly name for the metrics from the rule group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ruleGroup.ts#L97">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A friendly name of the rule group

<h2 class="pdoc-module-header" id="RuleGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ruleGroup.ts#L67">interface RuleGroupState</a>
</h2>

Input properties used for looking up and filtering RuleGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ruleGroup.ts#L71">property activatedRules</a>
</h3>

```typescript
activatedRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of activated rules, see below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ruleGroup.ts#L75">property metricName</a>
</h3>

```typescript
metricName?: pulumi.Input<string>;
```


A friendly name for the metrics from the rule group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/ruleGroup.ts#L79">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A friendly name of the rule group

<h2 class="pdoc-module-header" id="RuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rule.ts#L67">interface RuleState</a>
</h2>

Input properties used for looking up and filtering Rule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rule.ts#L71">property metricName</a>
</h3>

```typescript
metricName?: pulumi.Input<string>;
```


The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rule.ts#L75">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/rule.ts#L79">property predicates</a>
</h3>

```typescript
predicates?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.

<h2 class="pdoc-module-header" id="SizeConstraintSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sizeConstraintSet.ts#L72">interface SizeConstraintSetArgs</a>
</h2>

The set of arguments for constructing a SizeConstraintSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sizeConstraintSet.ts#L76">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the Size Constraint Set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sizeConstraintSet.ts#L80">property sizeConstraints</a>
</h3>

```typescript
sizeConstraints?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies the parts of web requests that you want to inspect the size of.

<h2 class="pdoc-module-header" id="SizeConstraintSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sizeConstraintSet.ts#L58">interface SizeConstraintSetState</a>
</h2>

Input properties used for looking up and filtering SizeConstraintSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sizeConstraintSet.ts#L62">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the Size Constraint Set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sizeConstraintSet.ts#L66">property sizeConstraints</a>
</h3>

```typescript
sizeConstraints?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies the parts of web requests that you want to inspect the size of.

<h2 class="pdoc-module-header" id="SqlInjectionMatchSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sqlInjectionMatchSet.ts#L72">interface SqlInjectionMatchSetArgs</a>
</h2>

The set of arguments for constructing a SqlInjectionMatchSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sqlInjectionMatchSet.ts#L76">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the SizeConstraintSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sqlInjectionMatchSet.ts#L80">property sqlInjectionMatchTuples</a>
</h3>

```typescript
sqlInjectionMatchTuples?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.

<h2 class="pdoc-module-header" id="SqlInjectionMatchSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sqlInjectionMatchSet.ts#L58">interface SqlInjectionMatchSetState</a>
</h2>

Input properties used for looking up and filtering SqlInjectionMatchSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sqlInjectionMatchSet.ts#L62">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the SizeConstraintSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/sqlInjectionMatchSet.ts#L66">property sqlInjectionMatchTuples</a>
</h3>

```typescript
sqlInjectionMatchTuples?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The parts of web requests that you want AWS WAF to inspect for malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.

<h2 class="pdoc-module-header" id="WebAclArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts#L98">interface WebAclArgs</a>
</h2>

The set of arguments for constructing a WebAcl resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts#L102">property defaultAction</a>
</h3>

```typescript
defaultAction: pulumi.Input<{ ... }>;
```


The action that you want AWS WAF to take when a request doesn't match the criteria in any of the rules that are associated with the web ACL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts#L106">property metricName</a>
</h3>

```typescript
metricName: pulumi.Input<string>;
```


The name or description for the Amazon CloudWatch metric of this web ACL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts#L110">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the web ACL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts#L114">property rules</a>
</h3>

```typescript
rules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The rules to associate with the web ACL and the settings for each rule.

<h2 class="pdoc-module-header" id="WebAclState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts#L76">interface WebAclState</a>
</h2>

Input properties used for looking up and filtering WebAcl resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts#L80">property defaultAction</a>
</h3>

```typescript
defaultAction?: pulumi.Input<{ ... }>;
```


The action that you want AWS WAF to take when a request doesn't match the criteria in any of the rules that are associated with the web ACL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts#L84">property metricName</a>
</h3>

```typescript
metricName?: pulumi.Input<string>;
```


The name or description for the Amazon CloudWatch metric of this web ACL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts#L88">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the web ACL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/webAcl.ts#L92">property rules</a>
</h3>

```typescript
rules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The rules to associate with the web ACL and the settings for each rule.

<h2 class="pdoc-module-header" id="XssMatchSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/xssMatchSet.ts#L72">interface XssMatchSetArgs</a>
</h2>

The set of arguments for constructing a XssMatchSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/xssMatchSet.ts#L76">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the SizeConstraintSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/xssMatchSet.ts#L80">property xssMatchTuples</a>
</h3>

```typescript
xssMatchTuples?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The parts of web requests that you want to inspect for cross-site scripting attacks.

<h2 class="pdoc-module-header" id="XssMatchSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/xssMatchSet.ts#L58">interface XssMatchSetState</a>
</h2>

Input properties used for looking up and filtering XssMatchSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/xssMatchSet.ts#L62">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name or description of the SizeConstraintSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/waf/xssMatchSet.ts#L66">property xssMatchTuples</a>
</h3>

```typescript
xssMatchTuples?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The parts of web requests that you want to inspect for cross-site scripting attacks.

