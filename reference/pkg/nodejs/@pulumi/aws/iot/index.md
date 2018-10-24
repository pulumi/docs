---
title: Module iot
---

<a href="../index.html">@pulumi/aws</a> &gt; iot

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Certificate">class Certificate</a>
* <a href="#Policy">class Policy</a>
* <a href="#Thing">class Thing</a>
* <a href="#ThingType">class ThingType</a>
* <a href="#TopicRule">class TopicRule</a>
* <a href="#getEndpoint">function getEndpoint</a>
* <a href="#CertificateArgs">interface CertificateArgs</a>
* <a href="#CertificateState">interface CertificateState</a>
* <a href="#GetEndpointResult">interface GetEndpointResult</a>
* <a href="#PolicyArgs">interface PolicyArgs</a>
* <a href="#PolicyState">interface PolicyState</a>
* <a href="#ThingArgs">interface ThingArgs</a>
* <a href="#ThingState">interface ThingState</a>
* <a href="#ThingTypeArgs">interface ThingTypeArgs</a>
* <a href="#ThingTypeState">interface ThingTypeState</a>
* <a href="#TopicRuleArgs">interface TopicRuleArgs</a>
* <a href="#TopicRuleState">interface TopicRuleState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/certificate.ts">iot/certificate.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/getEndpoint.ts">iot/getEndpoint.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/policy.ts">iot/policy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts">iot/thing.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thingType.ts">iot/thingType.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts">iot/topicRule.ts</a> 


<h2 class="pdoc-module-header" id="Certificate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/certificate.ts#L10">class Certificate</a>
</h2>

Creates and manages an AWS IoT certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/certificate.ts#L36">constructor</a>
</h3>

```typescript
new Certificate(name: string, args: CertificateArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Certificate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/certificate.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CertificateState): Certificate
```


Get an existing Certificate resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/certificate.ts#L26">property active</a>
</h3>

```typescript
public active: pulumi.Output<boolean>;
```


Boolean flag to indicate if the certificate should be active

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/certificate.ts#L30">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the created AWS IoT certificate

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/certificate.ts#L36">property csr</a>
</h3>

```typescript
public csr: pulumi.Output<string>;
```


The certificate signing request. Review the
[IoT API Reference Guide] (http://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html)
for more information on creating a certificate from a certificate signing request (CSR).

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

<h2 class="pdoc-module-header" id="Policy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/policy.ts#L10">class Policy</a>
</h2>

Provides an IoT policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/policy.ts#L38">constructor</a>
</h3>

```typescript
new Policy(name: string, args: PolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Policy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/policy.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyState): Policy
```


Get an existing Policy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/policy.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN assigned by AWS to this policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/policy.ts#L30">property defaultVersionId</a>
</h3>

```typescript
public defaultVersionId: pulumi.Output<string>;
```


The default version of this policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/policy.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/policy.ts#L38">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The policy document. This is a JSON formatted string. Use the [IoT Developer Guide](http://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) for more information on IoT Policies. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Thing">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L10">class Thing</a>
</h2>

Creates and manages an AWS IoT Thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L46">constructor</a>
</h3>

```typescript
new Thing(name: string, args?: ThingArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Thing resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ThingState): Thing
```


Get an existing Thing resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L30">property attributes</a>
</h3>

```typescript
public attributes: pulumi.Output<{ ... } | undefined>;
```


Map of attributes of the thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L34">property defaultClientId</a>
</h3>

```typescript
public defaultClientId: pulumi.Output<string>;
```


The default client ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L42">property thingTypeName</a>
</h3>

```typescript
public thingTypeName: pulumi.Output<string | undefined>;
```


The thing type name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L46">property version</a>
</h3>

```typescript
public version: pulumi.Output<number>;
```


The current version of the thing record in the registry.

<h2 class="pdoc-module-header" id="ThingType">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thingType.ts#L10">class ThingType</a>
</h2>

Creates and manages an AWS IoT Thing Type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thingType.ts#L35">constructor</a>
</h3>

```typescript
new ThingType(name: string, args?: ThingTypeArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ThingType resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thingType.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ThingTypeState): ThingType
```


Get an existing ThingType resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thingType.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the created AWS IoT Thing Type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thingType.ts#L30">property deprecated</a>
</h3>

```typescript
public deprecated: pulumi.Output<boolean | undefined>;
```


Whether the thing type is deprecated. If true, no new things could be associated with this type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thingType.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the thing type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thingType.ts#L35">property properties</a>
</h3>

```typescript
public properties: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TopicRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L7">class TopicRule</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L54">constructor</a>
</h3>

```typescript
new TopicRule(name: string, args: TopicRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TopicRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L16">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicRuleState): TopicRule
```


Get an existing TopicRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L23">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the topic rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L24">property cloudwatchAlarm</a>
</h3>

```typescript
public cloudwatchAlarm: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L25">property cloudwatchMetric</a>
</h3>

```typescript
public cloudwatchMetric: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L30">property dynamodb</a>
</h3>

```typescript
public dynamodb: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L31">property elasticsearch</a>
</h3>

```typescript
public elasticsearch: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L35">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean>;
```


Specifies whether the rule is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L36">property firehose</a>
</h3>

```typescript
public firehose: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L37">property kinesis</a>
</h3>

```typescript
public kinesis: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L38">property lambda</a>
</h3>

```typescript
public lambda: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L43">property republish</a>
</h3>

```typescript
public republish: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L44">property s3</a>
</h3>

```typescript
public s3: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L45">property sns</a>
</h3>

```typescript
public sns: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L49">property sql</a>
</h3>

```typescript
public sql: pulumi.Output<string>;
```


The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L53">property sqlVersion</a>
</h3>

```typescript
public sqlVersion: pulumi.Output<string>;
```


The version of the SQL rules engine to use when evaluating the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L54">property sqs</a>
</h3>

```typescript
public sqs: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getEndpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/getEndpoint.ts#L10">function getEndpoint</a>
</h2>

```typescript
getEndpoint(opts?: pulumi.InvokeOptions): Promise<GetEndpointResult>
```


Returns a unique endpoint specific to the AWS account making the call.

<h2 class="pdoc-module-header" id="CertificateArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/certificate.ts#L92">interface CertificateArgs</a>
</h2>

The set of arguments for constructing a Certificate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/certificate.ts#L96">property active</a>
</h3>

```typescript
active: pulumi.Input<boolean>;
```


Boolean flag to indicate if the certificate should be active

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/certificate.ts#L102">property csr</a>
</h3>

```typescript
csr: pulumi.Input<string>;
```


The certificate signing request. Review the
[IoT API Reference Guide] (http://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html)
for more information on creating a certificate from a certificate signing request (CSR).

<h2 class="pdoc-module-header" id="CertificateState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/certificate.ts#L72">interface CertificateState</a>
</h2>

Input properties used for looking up and filtering Certificate resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/certificate.ts#L76">property active</a>
</h3>

```typescript
active?: pulumi.Input<boolean>;
```


Boolean flag to indicate if the certificate should be active

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/certificate.ts#L80">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the created AWS IoT certificate

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/certificate.ts#L86">property csr</a>
</h3>

```typescript
csr?: pulumi.Input<string>;
```


The certificate signing request. Review the
[IoT API Reference Guide] (http://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html)
for more information on creating a certificate from a certificate signing request (CSR).

<h2 class="pdoc-module-header" id="GetEndpointResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/getEndpoint.ts#L18">interface GetEndpointResult</a>
</h2>

A collection of values returned by getEndpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/getEndpoint.ts#L22">property endpointAddress</a>
</h3>

```typescript
endpointAddress: string;
```


The endpoint. The format of the endpoint is as follows: `IDENTIFIER.iot.REGION.amazonaws.com`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/getEndpoint.ts#L26">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="PolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/policy.ts#L95">interface PolicyArgs</a>
</h2>

The set of arguments for constructing a Policy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/policy.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/policy.ts#L103">property policy</a>
</h3>

```typescript
policy: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string. Use the [IoT Developer Guide](http://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) for more information on IoT Policies. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).

<h2 class="pdoc-module-header" id="PolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/policy.ts#L73">interface PolicyState</a>
</h2>

Input properties used for looking up and filtering Policy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/policy.ts#L77">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN assigned by AWS to this policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/policy.ts#L81">property defaultVersionId</a>
</h3>

```typescript
defaultVersionId?: pulumi.Input<string>;
```


The default version of this policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/policy.ts#L85">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/policy.ts#L89">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string. Use the [IoT Developer Guide](http://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) for more information on IoT Policies. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).

<h2 class="pdoc-module-header" id="ThingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L112">interface ThingArgs</a>
</h2>

The set of arguments for constructing a Thing resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L116">property attributes</a>
</h3>

```typescript
attributes?: pulumi.Input<{ ... }>;
```


Map of attributes of the thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L120">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L124">property thingTypeName</a>
</h3>

```typescript
thingTypeName?: pulumi.Input<string>;
```


The thing type name.

<h2 class="pdoc-module-header" id="ThingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L82">interface ThingState</a>
</h2>

Input properties used for looking up and filtering Thing resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L86">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L90">property attributes</a>
</h3>

```typescript
attributes?: pulumi.Input<{ ... }>;
```


Map of attributes of the thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L94">property defaultClientId</a>
</h3>

```typescript
defaultClientId?: pulumi.Input<string>;
```


The default client ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L98">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L102">property thingTypeName</a>
</h3>

```typescript
thingTypeName?: pulumi.Input<string>;
```


The thing type name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thing.ts#L106">property version</a>
</h3>

```typescript
version?: pulumi.Input<number>;
```


The current version of the thing record in the registry.

<h2 class="pdoc-module-header" id="ThingTypeArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thingType.ts#L86">interface ThingTypeArgs</a>
</h2>

The set of arguments for constructing a ThingType resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thingType.ts#L90">property deprecated</a>
</h3>

```typescript
deprecated?: pulumi.Input<boolean>;
```


Whether the thing type is deprecated. If true, no new things could be associated with this type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thingType.ts#L94">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the thing type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thingType.ts#L95">property properties</a>
</h3>

```typescript
properties?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="ThingTypeState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thingType.ts#L67">interface ThingTypeState</a>
</h2>

Input properties used for looking up and filtering ThingType resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thingType.ts#L71">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the created AWS IoT Thing Type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thingType.ts#L75">property deprecated</a>
</h3>

```typescript
deprecated?: pulumi.Input<boolean>;
```


Whether the thing type is deprecated. If true, no new things could be associated with this type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thingType.ts#L79">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the thing type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/thingType.ts#L80">property properties</a>
</h3>

```typescript
properties?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="TopicRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L162">interface TopicRuleArgs</a>
</h2>

The set of arguments for constructing a TopicRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L163">property cloudwatchAlarm</a>
</h3>

```typescript
cloudwatchAlarm?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L164">property cloudwatchMetric</a>
</h3>

```typescript
cloudwatchMetric?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L168">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L169">property dynamodb</a>
</h3>

```typescript
dynamodb?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L170">property elasticsearch</a>
</h3>

```typescript
elasticsearch?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L174">property enabled</a>
</h3>

```typescript
enabled: pulumi.Input<boolean>;
```


Specifies whether the rule is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L175">property firehose</a>
</h3>

```typescript
firehose?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L176">property kinesis</a>
</h3>

```typescript
kinesis?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L177">property lambda</a>
</h3>

```typescript
lambda?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L181">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L182">property republish</a>
</h3>

```typescript
republish?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L183">property s3</a>
</h3>

```typescript
s3?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L184">property sns</a>
</h3>

```typescript
sns?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L188">property sql</a>
</h3>

```typescript
sql: pulumi.Input<string>;
```


The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L192">property sqlVersion</a>
</h3>

```typescript
sqlVersion: pulumi.Input<string>;
```


The version of the SQL rules engine to use when evaluating the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L193">property sqs</a>
</h3>

```typescript
sqs?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="TopicRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L121">interface TopicRuleState</a>
</h2>

Input properties used for looking up and filtering TopicRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L125">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the topic rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L126">property cloudwatchAlarm</a>
</h3>

```typescript
cloudwatchAlarm?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L127">property cloudwatchMetric</a>
</h3>

```typescript
cloudwatchMetric?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L131">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L132">property dynamodb</a>
</h3>

```typescript
dynamodb?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L133">property elasticsearch</a>
</h3>

```typescript
elasticsearch?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L137">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Specifies whether the rule is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L138">property firehose</a>
</h3>

```typescript
firehose?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L139">property kinesis</a>
</h3>

```typescript
kinesis?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L140">property lambda</a>
</h3>

```typescript
lambda?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L144">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L145">property republish</a>
</h3>

```typescript
republish?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L146">property s3</a>
</h3>

```typescript
s3?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L147">property sns</a>
</h3>

```typescript
sns?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L151">property sql</a>
</h3>

```typescript
sql?: pulumi.Input<string>;
```


The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L155">property sqlVersion</a>
</h3>

```typescript
sqlVersion?: pulumi.Input<string>;
```


The version of the SQL rules engine to use when evaluating the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/iot/topicRule.ts#L156">property sqs</a>
</h3>

```typescript
sqs?: pulumi.Input<{ ... }>;
```

