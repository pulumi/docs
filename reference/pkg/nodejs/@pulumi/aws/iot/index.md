---
title: Module iot
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Certificate">class Certificate</a>
* <a href="#Policy">class Policy</a>
* <a href="#Thing">class Thing</a>
* <a href="#ThingType">class ThingType</a>
* <a href="#TopicRule">class TopicRule</a>
* <a href="#CertificateArgs">interface CertificateArgs</a>
* <a href="#CertificateState">interface CertificateState</a>
* <a href="#PolicyArgs">interface PolicyArgs</a>
* <a href="#PolicyState">interface PolicyState</a>
* <a href="#ThingArgs">interface ThingArgs</a>
* <a href="#ThingState">interface ThingState</a>
* <a href="#ThingTypeArgs">interface ThingTypeArgs</a>
* <a href="#ThingTypeState">interface ThingTypeState</a>
* <a href="#TopicRuleArgs">interface TopicRuleArgs</a>
* <a href="#TopicRuleState">interface TopicRuleState</a>

<a href="/iot/certificate.ts">iot/certificate.ts</a> <a href="/iot/policy.ts">iot/policy.ts</a> <a href="/iot/thing.ts">iot/thing.ts</a> <a href="/iot/thingType.ts">iot/thingType.ts</a> <a href="/iot/topicRule.ts">iot/topicRule.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Certificate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/certificate.ts#L9">class Certificate</a>
</h2>

Creates and manages an AWS IoT certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/certificate.ts#L35">constructor</a>
</h3>

```typescript
new Certificate(name: string, args: CertificateArgs, opts?: pulumi.ResourceOptions)
```


Create a Certificate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Certificate(name: string, state?: CertificateState, opts?: pulumi.ResourceOptions)
```


Create a Certificate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/certificate.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CertificateState): Certificate
```


Get an existing Certificate resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/certificate.ts#L25">property active</a>
</h3>

```typescript
public active: pulumi.Output<boolean>;
```


Boolean flag to indicate if the certificate should be active

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/certificate.ts#L29">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the created AWS IoT certificate

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/certificate.ts#L35">property csr</a>
</h3>

```typescript
public csr: pulumi.Output<string>;
```


The certificate signing request. Review the
[IoT API Reference Guide] (http://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html)
for more information on creating a certificate from a certificate signing request (CSR).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Policy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/policy.ts#L29">class Policy</a>
</h2>

Provides an IoT policy.

```hcl
resource "aws_iot_policy" "pubsub" {
  name        = "PubSubToAnyTopic"
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "iot:*"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
EOF
}
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/policy.ts#L59">constructor</a>
</h3>

```typescript
new Policy(name: string, args: PolicyArgs, opts?: pulumi.ResourceOptions)
```


Create a Policy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Policy(name: string, state?: PolicyState, opts?: pulumi.ResourceOptions)
```


Create a Policy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/policy.ts#L38">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyState): Policy
```


Get an existing Policy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/policy.ts#L45">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN assigned by AWS to this policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/policy.ts#L49">property defaultVersionId</a>
</h3>

```typescript
public defaultVersionId: pulumi.Output<string>;
```


The default version of this policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/policy.ts#L53">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/policy.ts#L59">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The policy document. This is a JSON formatted string.
The heredoc syntax or `file` function is helpful here. Use the [IoT Developer Guide]
(http://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) for more information on IoT Policies

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Thing">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L9">class Thing</a>
</h2>

Creates and manages an AWS IoT Thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L45">constructor</a>
</h3>

```typescript
new Thing(name: string, args?: ThingArgs, opts?: pulumi.ResourceOptions)
```


Create a Thing resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Thing(name: string, state?: ThingState, opts?: pulumi.ResourceOptions)
```


Create a Thing resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ThingState): Thing
```


Get an existing Thing resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L29">property attributes</a>
</h3>

```typescript
public attributes: pulumi.Output<{ ... } | undefined>;
```


Map of attributes of the thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L33">property defaultClientId</a>
</h3>

```typescript
public defaultClientId: pulumi.Output<string>;
```


The default client ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L41">property thingTypeName</a>
</h3>

```typescript
public thingTypeName: pulumi.Output<string | undefined>;
```


The thing type name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L45">property version</a>
</h3>

```typescript
public version: pulumi.Output<number>;
```


The current version of the thing record in the registry.

<h2 class="pdoc-module-header" id="ThingType">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thingType.ts#L9">class ThingType</a>
</h2>

Creates and manages an AWS IoT Thing Type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thingType.ts#L34">constructor</a>
</h3>

```typescript
new ThingType(name: string, args?: ThingTypeArgs, opts?: pulumi.ResourceOptions)
```


Create a ThingType resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new ThingType(name: string, state?: ThingTypeState, opts?: pulumi.ResourceOptions)
```


Create a ThingType resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thingType.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ThingTypeState): ThingType
```


Get an existing ThingType resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thingType.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the created AWS IoT Thing Type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thingType.ts#L29">property deprecated</a>
</h3>

```typescript
public deprecated: pulumi.Output<boolean | undefined>;
```


Whether the thing type is deprecated. If true, no new things could be associated with this type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thingType.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the thing type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thingType.ts#L34">property properties</a>
</h3>

```typescript
public properties: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TopicRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L6">class TopicRule</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L53">constructor</a>
</h3>

```typescript
new TopicRule(name: string, args: TopicRuleArgs, opts?: pulumi.ResourceOptions)
```


Create a TopicRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new TopicRule(name: string, state?: TopicRuleState, opts?: pulumi.ResourceOptions)
```


Create a TopicRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L15">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicRuleState): TopicRule
```


Get an existing TopicRule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L22">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the topic rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L23">property cloudwatchAlarm</a>
</h3>

```typescript
public cloudwatchAlarm: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L24">property cloudwatchMetric</a>
</h3>

```typescript
public cloudwatchMetric: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L28">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L29">property dynamodb</a>
</h3>

```typescript
public dynamodb: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L30">property elasticsearch</a>
</h3>

```typescript
public elasticsearch: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L34">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean>;
```


Specifies whether the rule is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L35">property firehose</a>
</h3>

```typescript
public firehose: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L36">property kinesis</a>
</h3>

```typescript
public kinesis: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L37">property lambda</a>
</h3>

```typescript
public lambda: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L41">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L42">property republish</a>
</h3>

```typescript
public republish: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L43">property s3</a>
</h3>

```typescript
public s3: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L44">property sns</a>
</h3>

```typescript
public sns: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L48">property sql</a>
</h3>

```typescript
public sql: pulumi.Output<string>;
```


The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L52">property sqlVersion</a>
</h3>

```typescript
public sqlVersion: pulumi.Output<string>;
```


The version of the SQL rules engine to use when evaluating the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L53">property sqs</a>
</h3>

```typescript
public sqs: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="CertificateArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/certificate.ts#L93">interface CertificateArgs</a>
</h2>

The set of arguments for constructing a Certificate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/certificate.ts#L97">property active</a>
</h3>

```typescript
active: pulumi.Input<boolean>;
```


Boolean flag to indicate if the certificate should be active

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/certificate.ts#L103">property csr</a>
</h3>

```typescript
csr: pulumi.Input<string>;
```


The certificate signing request. Review the
[IoT API Reference Guide] (http://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html)
for more information on creating a certificate from a certificate signing request (CSR).

<h2 class="pdoc-module-header" id="CertificateState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/certificate.ts#L73">interface CertificateState</a>
</h2>

Input properties used for looking up and filtering Certificate resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/certificate.ts#L77">property active</a>
</h3>

```typescript
active?: pulumi.Input<boolean>;
```


Boolean flag to indicate if the certificate should be active

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/certificate.ts#L81">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the created AWS IoT certificate

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/certificate.ts#L87">property csr</a>
</h3>

```typescript
csr?: pulumi.Input<string>;
```


The certificate signing request. Review the
[IoT API Reference Guide] (http://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html)
for more information on creating a certificate from a certificate signing request (CSR).

<h2 class="pdoc-module-header" id="PolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/policy.ts#L120">interface PolicyArgs</a>
</h2>

The set of arguments for constructing a Policy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/policy.ts#L124">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/policy.ts#L130">property policy</a>
</h3>

```typescript
policy: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string.
The heredoc syntax or `file` function is helpful here. Use the [IoT Developer Guide]
(http://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) for more information on IoT Policies

<h2 class="pdoc-module-header" id="PolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/policy.ts#L96">interface PolicyState</a>
</h2>

Input properties used for looking up and filtering Policy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/policy.ts#L100">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN assigned by AWS to this policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/policy.ts#L104">property defaultVersionId</a>
</h3>

```typescript
defaultVersionId?: pulumi.Input<string>;
```


The default version of this policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/policy.ts#L108">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/policy.ts#L114">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string.
The heredoc syntax or `file` function is helpful here. Use the [IoT Developer Guide]
(http://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) for more information on IoT Policies

<h2 class="pdoc-module-header" id="ThingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L113">interface ThingArgs</a>
</h2>

The set of arguments for constructing a Thing resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L117">property attributes</a>
</h3>

```typescript
attributes?: pulumi.Input<{ ... }>;
```


Map of attributes of the thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L121">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L125">property thingTypeName</a>
</h3>

```typescript
thingTypeName?: pulumi.Input<string>;
```


The thing type name.

<h2 class="pdoc-module-header" id="ThingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L83">interface ThingState</a>
</h2>

Input properties used for looking up and filtering Thing resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L87">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L91">property attributes</a>
</h3>

```typescript
attributes?: pulumi.Input<{ ... }>;
```


Map of attributes of the thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L95">property defaultClientId</a>
</h3>

```typescript
defaultClientId?: pulumi.Input<string>;
```


The default client ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the thing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L103">property thingTypeName</a>
</h3>

```typescript
thingTypeName?: pulumi.Input<string>;
```


The thing type name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thing.ts#L107">property version</a>
</h3>

```typescript
version?: pulumi.Input<number>;
```


The current version of the thing record in the registry.

<h2 class="pdoc-module-header" id="ThingTypeArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thingType.ts#L87">interface ThingTypeArgs</a>
</h2>

The set of arguments for constructing a ThingType resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thingType.ts#L91">property deprecated</a>
</h3>

```typescript
deprecated?: pulumi.Input<boolean>;
```


Whether the thing type is deprecated. If true, no new things could be associated with this type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thingType.ts#L95">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the thing type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thingType.ts#L96">property properties</a>
</h3>

```typescript
properties?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="ThingTypeState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thingType.ts#L68">interface ThingTypeState</a>
</h2>

Input properties used for looking up and filtering ThingType resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thingType.ts#L72">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the created AWS IoT Thing Type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thingType.ts#L76">property deprecated</a>
</h3>

```typescript
deprecated?: pulumi.Input<boolean>;
```


Whether the thing type is deprecated. If true, no new things could be associated with this type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thingType.ts#L80">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the thing type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/thingType.ts#L81">property properties</a>
</h3>

```typescript
properties?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="TopicRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L163">interface TopicRuleArgs</a>
</h2>

The set of arguments for constructing a TopicRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L164">property cloudwatchAlarm</a>
</h3>

```typescript
cloudwatchAlarm?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L165">property cloudwatchMetric</a>
</h3>

```typescript
cloudwatchMetric?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L169">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L170">property dynamodb</a>
</h3>

```typescript
dynamodb?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L171">property elasticsearch</a>
</h3>

```typescript
elasticsearch?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L175">property enabled</a>
</h3>

```typescript
enabled: pulumi.Input<boolean>;
```


Specifies whether the rule is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L176">property firehose</a>
</h3>

```typescript
firehose?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L177">property kinesis</a>
</h3>

```typescript
kinesis?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L178">property lambda</a>
</h3>

```typescript
lambda?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L182">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L183">property republish</a>
</h3>

```typescript
republish?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L184">property s3</a>
</h3>

```typescript
s3?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L185">property sns</a>
</h3>

```typescript
sns?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L189">property sql</a>
</h3>

```typescript
sql: pulumi.Input<string>;
```


The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L193">property sqlVersion</a>
</h3>

```typescript
sqlVersion: pulumi.Input<string>;
```


The version of the SQL rules engine to use when evaluating the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L194">property sqs</a>
</h3>

```typescript
sqs?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="TopicRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L122">interface TopicRuleState</a>
</h2>

Input properties used for looking up and filtering TopicRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L126">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the topic rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L127">property cloudwatchAlarm</a>
</h3>

```typescript
cloudwatchAlarm?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L128">property cloudwatchMetric</a>
</h3>

```typescript
cloudwatchMetric?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L132">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L133">property dynamodb</a>
</h3>

```typescript
dynamodb?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L134">property elasticsearch</a>
</h3>

```typescript
elasticsearch?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L138">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Specifies whether the rule is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L139">property firehose</a>
</h3>

```typescript
firehose?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L140">property kinesis</a>
</h3>

```typescript
kinesis?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L141">property lambda</a>
</h3>

```typescript
lambda?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L145">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L146">property republish</a>
</h3>

```typescript
republish?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L147">property s3</a>
</h3>

```typescript
s3?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L148">property sns</a>
</h3>

```typescript
sns?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L152">property sql</a>
</h3>

```typescript
sql?: pulumi.Input<string>;
```


The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L156">property sqlVersion</a>
</h3>

```typescript
sqlVersion?: pulumi.Input<string>;
```


The version of the SQL rules engine to use when evaluating the rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/iot/topicRule.ts#L157">property sqs</a>
</h3>

```typescript
sqs?: pulumi.Input<{ ... }>;
```

