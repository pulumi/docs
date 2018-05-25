---
title: Module ses
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ActiveReceiptRuleSet">class ActiveReceiptRuleSet</a>
* <a href="#ConfgurationSet">class ConfgurationSet</a>
* <a href="#DomainDkim">class DomainDkim</a>
* <a href="#DomainIdentity">class DomainIdentity</a>
* <a href="#EventDestination">class EventDestination</a>
* <a href="#IdentityNotificationTopic">class IdentityNotificationTopic</a>
* <a href="#MailFrom">class MailFrom</a>
* <a href="#ReceiptFilter">class ReceiptFilter</a>
* <a href="#ReceiptRule">class ReceiptRule</a>
* <a href="#ReceiptRuleSet">class ReceiptRuleSet</a>
* <a href="#Template">class Template</a>
* <a href="#ActiveReceiptRuleSetArgs">interface ActiveReceiptRuleSetArgs</a>
* <a href="#ActiveReceiptRuleSetState">interface ActiveReceiptRuleSetState</a>
* <a href="#ConfgurationSetArgs">interface ConfgurationSetArgs</a>
* <a href="#ConfgurationSetState">interface ConfgurationSetState</a>
* <a href="#DomainDkimArgs">interface DomainDkimArgs</a>
* <a href="#DomainDkimState">interface DomainDkimState</a>
* <a href="#DomainIdentityArgs">interface DomainIdentityArgs</a>
* <a href="#DomainIdentityState">interface DomainIdentityState</a>
* <a href="#EventDestinationArgs">interface EventDestinationArgs</a>
* <a href="#EventDestinationState">interface EventDestinationState</a>
* <a href="#IdentityNotificationTopicArgs">interface IdentityNotificationTopicArgs</a>
* <a href="#IdentityNotificationTopicState">interface IdentityNotificationTopicState</a>
* <a href="#MailFromArgs">interface MailFromArgs</a>
* <a href="#MailFromState">interface MailFromState</a>
* <a href="#ReceiptFilterArgs">interface ReceiptFilterArgs</a>
* <a href="#ReceiptFilterState">interface ReceiptFilterState</a>
* <a href="#ReceiptRuleArgs">interface ReceiptRuleArgs</a>
* <a href="#ReceiptRuleSetArgs">interface ReceiptRuleSetArgs</a>
* <a href="#ReceiptRuleSetState">interface ReceiptRuleSetState</a>
* <a href="#ReceiptRuleState">interface ReceiptRuleState</a>
* <a href="#TemplateArgs">interface TemplateArgs</a>
* <a href="#TemplateState">interface TemplateState</a>

<a href="/ses/activeReceiptRuleSet.ts">ses/activeReceiptRuleSet.ts</a> <a href="/ses/confgurationSet.ts">ses/confgurationSet.ts</a> <a href="/ses/domainDkim.ts">ses/domainDkim.ts</a> <a href="/ses/domainIdentity.ts">ses/domainIdentity.ts</a> <a href="/ses/eventDestination.ts">ses/eventDestination.ts</a> <a href="/ses/identityNotificationTopic.ts">ses/identityNotificationTopic.ts</a> <a href="/ses/mailFrom.ts">ses/mailFrom.ts</a> <a href="/ses/receiptFilter.ts">ses/receiptFilter.ts</a> <a href="/ses/receiptRule.ts">ses/receiptRule.ts</a> <a href="/ses/receiptRuleSet.ts">ses/receiptRuleSet.ts</a> <a href="/ses/template.ts">ses/template.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="ActiveReceiptRuleSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/activeReceiptRuleSet.ts#L9">class ActiveReceiptRuleSet</a>
</h2>

Provides a resource to designate the active SES receipt rule set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/activeReceiptRuleSet.ts#L25">constructor</a>
</h3>

```typescript
new ActiveReceiptRuleSet(name: string, args: ActiveReceiptRuleSetArgs, opts?: pulumi.ResourceOptions)
```


Create a ActiveReceiptRuleSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new ActiveReceiptRuleSet(name: string, state?: ActiveReceiptRuleSetState, opts?: pulumi.ResourceOptions)
```


Create a ActiveReceiptRuleSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/activeReceiptRuleSet.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ActiveReceiptRuleSetState): ActiveReceiptRuleSet
```


Get an existing ActiveReceiptRuleSet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/activeReceiptRuleSet.ts#L25">property ruleSetName</a>
</h3>

```typescript
public ruleSetName: pulumi.Output<string>;
```


The name of the rule set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ConfgurationSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/confgurationSet.ts#L9">class ConfgurationSet</a>
</h2>

Provides an SES configuration set resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/confgurationSet.ts#L25">constructor</a>
</h3>

```typescript
new ConfgurationSet(name: string, args?: ConfgurationSetArgs, opts?: pulumi.ResourceOptions)
```


Create a ConfgurationSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new ConfgurationSet(name: string, state?: ConfgurationSetState, opts?: pulumi.ResourceOptions)
```


Create a ConfgurationSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/confgurationSet.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConfgurationSetState): ConfgurationSet
```


Get an existing ConfgurationSet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/confgurationSet.ts#L25">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the configuration set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DomainDkim">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainDkim.ts#L11">class DomainDkim</a>
</h2>

Provides an SES domain DKIM generation resource.

Domain ownership needs to be confirmed first using [ses_domain_identity Resource](/docs/providers/aws/r/ses_domain_identity.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainDkim.ts#L36">constructor</a>
</h3>

```typescript
new DomainDkim(name: string, args: DomainDkimArgs, opts?: pulumi.ResourceOptions)
```


Create a DomainDkim resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new DomainDkim(name: string, state?: DomainDkimState, opts?: pulumi.ResourceOptions)
```


Create a DomainDkim resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainDkim.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DomainDkimState): DomainDkim
```


Get an existing DomainDkim resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainDkim.ts#L32">property dkimTokens</a>
</h3>

```typescript
public dkimTokens: pulumi.Output<string[]>;
```


DKIM tokens generated by SES.
These tokens should be used to create CNAME records used to verify SES Easy DKIM.
See below for an example of how this might be achieved
when the domain is hosted in Route 53 and managed by Terraform.
Find out more about verifying domains in Amazon SES
in the [AWS SES docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-records.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainDkim.ts#L36">property domain</a>
</h3>

```typescript
public domain: pulumi.Output<string>;
```


Verified domain name to generate DKIM tokens for.

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

<h2 class="pdoc-module-header" id="DomainIdentity">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainIdentity.ts#L9">class DomainIdentity</a>
</h2>

Provides an SES domain identity resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainIdentity.ts#L39">constructor</a>
</h3>

```typescript
new DomainIdentity(name: string, args: DomainIdentityArgs, opts?: pulumi.ResourceOptions)
```


Create a DomainIdentity resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new DomainIdentity(name: string, state?: DomainIdentityState, opts?: pulumi.ResourceOptions)
```


Create a DomainIdentity resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainIdentity.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DomainIdentityState): DomainIdentity
```


Get an existing DomainIdentity resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainIdentity.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the domain identity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainIdentity.ts#L29">property domain</a>
</h3>

```typescript
public domain: pulumi.Output<string>;
```


The domain name to assign to SES

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

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainIdentity.ts#L39">property verificationToken</a>
</h3>

```typescript
public verificationToken: pulumi.Output<string>;
```


A code which when added to the domain as a TXT record
will signal to SES that the owner of the domain has authorised SES to act on
their behalf. The domain identity will be in state "verification pending"
until this is done. See below for an example of how this might be achieved
when the domain is hosted in Route 53 and managed by Terraform.  Find out
more about verifying domains in Amazon SES in the [AWS SES
docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html).

<h2 class="pdoc-module-header" id="EventDestination">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L9">class EventDestination</a>
</h2>

Provides an SES event destination

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L49">constructor</a>
</h3>

```typescript
new EventDestination(name: string, args: EventDestinationArgs, opts?: pulumi.ResourceOptions)
```


Create a EventDestination resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new EventDestination(name: string, state?: EventDestinationState, opts?: pulumi.ResourceOptions)
```


Create a EventDestination resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventDestinationState): EventDestination
```


Get an existing EventDestination resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L25">property cloudwatchDestination</a>
</h3>

```typescript
public cloudwatchDestination: pulumi.Output<{ ... } | undefined>;
```


CloudWatch destination for the events

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L29">property configurationSetName</a>
</h3>

```typescript
public configurationSetName: pulumi.Output<string>;
```


The name of the configuration set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L33">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


If true, the event destination will be enabled

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L37">property kinesisDestination</a>
</h3>

```typescript
public kinesisDestination: pulumi.Output<{ ... } | undefined>;
```


Send the events to a kinesis firehose destination

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L41">property matchingTypes</a>
</h3>

```typescript
public matchingTypes: pulumi.Output<string[]>;
```


A list of matching types. May be any of `"send"`, `"reject"`, `"bounce"`, `"complaint"`, `"delivery"`, `"open"`, or `"click"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the event destination

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L49">property snsDestination</a>
</h3>

```typescript
public snsDestination: pulumi.Output<{ ... } | undefined>;
```


Send the events to an SNS Topic destination

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IdentityNotificationTopic">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/identityNotificationTopic.ts#L9">class IdentityNotificationTopic</a>
</h2>

Resource for managing SES Identity Notification Topics

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/identityNotificationTopic.ts#L33">constructor</a>
</h3>

```typescript
new IdentityNotificationTopic(name: string, args: IdentityNotificationTopicArgs, opts?: pulumi.ResourceOptions)
```


Create a IdentityNotificationTopic resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new IdentityNotificationTopic(name: string, state?: IdentityNotificationTopicState, opts?: pulumi.ResourceOptions)
```


Create a IdentityNotificationTopic resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/identityNotificationTopic.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IdentityNotificationTopicState): IdentityNotificationTopic
```


Get an existing IdentityNotificationTopic resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/identityNotificationTopic.ts#L25">property identity</a>
</h3>

```typescript
public identity: pulumi.Output<string>;
```


The identity for which the Amazon SNS topic will be set. You can specify an identity by using its name or by using its Amazon Resource Name (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/identityNotificationTopic.ts#L29">property notificationType</a>
</h3>

```typescript
public notificationType: pulumi.Output<string>;
```


The type of notifications that will be published to the specified Amazon SNS topic. Valid Values: *Bounce*, *Complaint* or *Delivery*.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/identityNotificationTopic.ts#L33">property topicArn</a>
</h3>

```typescript
public topicArn: pulumi.Output<string | undefined>;
```


The Amazon Resource Name (ARN) of the Amazon SNS topic. Can be set to "" (an empty string) to disable publishing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="MailFrom">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/mailFrom.ts#L11">class MailFrom</a>
</h2>

Provides an SES domain MAIL FROM resource.

~> **NOTE:** For the MAIL FROM domain to be fully usable, this resource should be paired with the [aws_ses_domain_identity resource](/docs/providers/aws/r/ses_domain_identity.html). To validate the MAIL FROM domain, a DNS MX record is required. To pass SPF checks, a DNS TXT record may also be required. See the [Amazon SES MAIL FROM documentation](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from-set.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/mailFrom.ts#L35">constructor</a>
</h3>

```typescript
new MailFrom(name: string, args: MailFromArgs, opts?: pulumi.ResourceOptions)
```


Create a MailFrom resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new MailFrom(name: string, state?: MailFromState, opts?: pulumi.ResourceOptions)
```


Create a MailFrom resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/mailFrom.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MailFromState): MailFrom
```


Get an existing MailFrom resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/mailFrom.ts#L27">property behaviorOnMxFailure</a>
</h3>

```typescript
public behaviorOnMxFailure: pulumi.Output<string | undefined>;
```


The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. Defaults to `UseDefaultValue`. See the [SES API documentation](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/mailFrom.ts#L31">property domain</a>
</h3>

```typescript
public domain: pulumi.Output<string>;
```


Verified domain name to generate DKIM tokens for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/mailFrom.ts#L35">property mailFromDomain</a>
</h3>

```typescript
public mailFromDomain: pulumi.Output<string>;
```


Subdomain (of above domain) which is to be used as MAIL FROM address (Required for DMARC validation)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ReceiptFilter">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptFilter.ts#L9">class ReceiptFilter</a>
</h2>

Provides an SES receipt filter resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptFilter.ts#L33">constructor</a>
</h3>

```typescript
new ReceiptFilter(name: string, args: ReceiptFilterArgs, opts?: pulumi.ResourceOptions)
```


Create a ReceiptFilter resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new ReceiptFilter(name: string, state?: ReceiptFilterState, opts?: pulumi.ResourceOptions)
```


Create a ReceiptFilter resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptFilter.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ReceiptFilterState): ReceiptFilter
```


Get an existing ReceiptFilter resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptFilter.ts#L25">property cidr</a>
</h3>

```typescript
public cidr: pulumi.Output<string>;
```


The IP address or address range to filter, in CIDR notation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptFilter.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the filter

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptFilter.ts#L33">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


Block or Allow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ReceiptRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L9">class ReceiptRule</a>
</h2>

Provides an SES receipt rule resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L77">constructor</a>
</h3>

```typescript
new ReceiptRule(name: string, args: ReceiptRuleArgs, opts?: pulumi.ResourceOptions)
```


Create a ReceiptRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new ReceiptRule(name: string, state?: ReceiptRuleState, opts?: pulumi.ResourceOptions)
```


Create a ReceiptRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ReceiptRuleState): ReceiptRule
```


Get an existing ReceiptRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L25">property addHeaderActions</a>
</h3>

```typescript
public addHeaderActions: pulumi.Output<{ ... }[] | undefined>;
```


A list of Add Header Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L29">property after</a>
</h3>

```typescript
public after: pulumi.Output<string | undefined>;
```


The name of the rule to place this rule after

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L33">property bounceActions</a>
</h3>

```typescript
public bounceActions: pulumi.Output<{ ... }[] | undefined>;
```


A list of Bounce Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L37">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean>;
```


If true, the rule will be enabled

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L41">property lambdaActions</a>
</h3>

```typescript
public lambdaActions: pulumi.Output<{ ... }[] | undefined>;
```


A list of Lambda Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L49">property recipients</a>
</h3>

```typescript
public recipients: pulumi.Output<string[] | undefined>;
```


A list of email addresses

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L53">property ruleSetName</a>
</h3>

```typescript
public ruleSetName: pulumi.Output<string>;
```


The name of the rule set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L57">property s3Actions</a>
</h3>

```typescript
public s3Actions: pulumi.Output<{ ... }[] | undefined>;
```


A list of S3 Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L61">property scanEnabled</a>
</h3>

```typescript
public scanEnabled: pulumi.Output<boolean>;
```


If true, incoming emails will be scanned for spam and viruses

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L65">property snsActions</a>
</h3>

```typescript
public snsActions: pulumi.Output<{ ... }[] | undefined>;
```


A list of SNS Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L69">property stopActions</a>
</h3>

```typescript
public stopActions: pulumi.Output<{ ... }[] | undefined>;
```


A list of Stop Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L73">property tlsPolicy</a>
</h3>

```typescript
public tlsPolicy: pulumi.Output<string>;
```


Require or Optional

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L77">property workmailActions</a>
</h3>

```typescript
public workmailActions: pulumi.Output<{ ... }[] | undefined>;
```


A list of WorkMail Action blocks. Documented below.

<h2 class="pdoc-module-header" id="ReceiptRuleSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRuleSet.ts#L9">class ReceiptRuleSet</a>
</h2>

Provides an SES receipt rule set resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRuleSet.ts#L25">constructor</a>
</h3>

```typescript
new ReceiptRuleSet(name: string, args: ReceiptRuleSetArgs, opts?: pulumi.ResourceOptions)
```


Create a ReceiptRuleSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new ReceiptRuleSet(name: string, state?: ReceiptRuleSetState, opts?: pulumi.ResourceOptions)
```


Create a ReceiptRuleSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRuleSet.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ReceiptRuleSetState): ReceiptRuleSet
```


Get an existing ReceiptRuleSet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRuleSet.ts#L25">property ruleSetName</a>
</h3>

```typescript
public ruleSetName: pulumi.Output<string>;
```


The name of the rule set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Template">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/template.ts#L9">class Template</a>
</h2>

Provides a resource to create a SES template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/template.ts#L37">constructor</a>
</h3>

```typescript
new Template(name: string, args?: TemplateArgs, opts?: pulumi.ResourceOptions)
```


Create a Template resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Template(name: string, state?: TemplateState, opts?: pulumi.ResourceOptions)
```


Create a Template resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/template.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TemplateState): Template
```


Get an existing Template resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/template.ts#L25">property html</a>
</h3>

```typescript
public html: pulumi.Output<string | undefined>;
```


The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/template.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/template.ts#L33">property subject</a>
</h3>

```typescript
public subject: pulumi.Output<string | undefined>;
```


The subject line of the email.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/template.ts#L37">property text</a>
</h3>

```typescript
public text: pulumi.Output<string | undefined>;
```


The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ActiveReceiptRuleSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/activeReceiptRuleSet.ts#L66">interface ActiveReceiptRuleSetArgs</a>
</h2>

The set of arguments for constructing a ActiveReceiptRuleSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/activeReceiptRuleSet.ts#L70">property ruleSetName</a>
</h3>

```typescript
ruleSetName: pulumi.Input<string>;
```


The name of the rule set

<h2 class="pdoc-module-header" id="ActiveReceiptRuleSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/activeReceiptRuleSet.ts#L56">interface ActiveReceiptRuleSetState</a>
</h2>

Input properties used for looking up and filtering ActiveReceiptRuleSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/activeReceiptRuleSet.ts#L60">property ruleSetName</a>
</h3>

```typescript
ruleSetName?: pulumi.Input<string>;
```


The name of the rule set

<h2 class="pdoc-module-header" id="ConfgurationSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/confgurationSet.ts#L63">interface ConfgurationSetArgs</a>
</h2>

The set of arguments for constructing a ConfgurationSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/confgurationSet.ts#L67">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the configuration set

<h2 class="pdoc-module-header" id="ConfgurationSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/confgurationSet.ts#L53">interface ConfgurationSetState</a>
</h2>

Input properties used for looking up and filtering ConfgurationSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/confgurationSet.ts#L57">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the configuration set

<h2 class="pdoc-module-header" id="DomainDkimArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainDkim.ts#L88">interface DomainDkimArgs</a>
</h2>

The set of arguments for constructing a DomainDkim resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainDkim.ts#L92">property domain</a>
</h3>

```typescript
domain: pulumi.Input<string>;
```


Verified domain name to generate DKIM tokens for.

<h2 class="pdoc-module-header" id="DomainDkimState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainDkim.ts#L69">interface DomainDkimState</a>
</h2>

Input properties used for looking up and filtering DomainDkim resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainDkim.ts#L78">property dkimTokens</a>
</h3>

```typescript
dkimTokens?: pulumi.Input<pulumi.Input<string>[]>;
```


DKIM tokens generated by SES.
These tokens should be used to create CNAME records used to verify SES Easy DKIM.
See below for an example of how this might be achieved
when the domain is hosted in Route 53 and managed by Terraform.
Find out more about verifying domains in Amazon SES
in the [AWS SES docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-records.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainDkim.ts#L82">property domain</a>
</h3>

```typescript
domain?: pulumi.Input<string>;
```


Verified domain name to generate DKIM tokens for.

<h2 class="pdoc-module-header" id="DomainIdentityArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainIdentity.ts#L98">interface DomainIdentityArgs</a>
</h2>

The set of arguments for constructing a DomainIdentity resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainIdentity.ts#L102">property domain</a>
</h3>

```typescript
domain: pulumi.Input<string>;
```


The domain name to assign to SES

<h2 class="pdoc-module-header" id="DomainIdentityState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainIdentity.ts#L74">interface DomainIdentityState</a>
</h2>

Input properties used for looking up and filtering DomainIdentity resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainIdentity.ts#L78">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the domain identity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainIdentity.ts#L82">property domain</a>
</h3>

```typescript
domain?: pulumi.Input<string>;
```


The domain name to assign to SES

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/domainIdentity.ts#L92">property verificationToken</a>
</h3>

```typescript
verificationToken?: pulumi.Input<string>;
```


A code which when added to the domain as a TXT record
will signal to SES that the owner of the domain has authorised SES to act on
their behalf. The domain identity will be in state "verification pending"
until this is done. See below for an example of how this might be achieved
when the domain is hosted in Route 53 and managed by Terraform.  Find out
more about verifying domains in Amazon SES in the [AWS SES
docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html).

<h2 class="pdoc-module-header" id="EventDestinationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L129">interface EventDestinationArgs</a>
</h2>

The set of arguments for constructing a EventDestination resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L133">property cloudwatchDestination</a>
</h3>

```typescript
cloudwatchDestination?: pulumi.Input<{ ... }>;
```


CloudWatch destination for the events

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L137">property configurationSetName</a>
</h3>

```typescript
configurationSetName: pulumi.Input<string>;
```


The name of the configuration set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L141">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


If true, the event destination will be enabled

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L145">property kinesisDestination</a>
</h3>

```typescript
kinesisDestination?: pulumi.Input<{ ... }>;
```


Send the events to a kinesis firehose destination

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L149">property matchingTypes</a>
</h3>

```typescript
matchingTypes: pulumi.Input<pulumi.Input<string>[]>;
```


A list of matching types. May be any of `"send"`, `"reject"`, `"bounce"`, `"complaint"`, `"delivery"`, `"open"`, or `"click"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L153">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the event destination

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L157">property snsDestination</a>
</h3>

```typescript
snsDestination?: pulumi.Input<{ ... }>;
```


Send the events to an SNS Topic destination

<h2 class="pdoc-module-header" id="EventDestinationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L95">interface EventDestinationState</a>
</h2>

Input properties used for looking up and filtering EventDestination resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L99">property cloudwatchDestination</a>
</h3>

```typescript
cloudwatchDestination?: pulumi.Input<{ ... }>;
```


CloudWatch destination for the events

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L103">property configurationSetName</a>
</h3>

```typescript
configurationSetName?: pulumi.Input<string>;
```


The name of the configuration set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L107">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


If true, the event destination will be enabled

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L111">property kinesisDestination</a>
</h3>

```typescript
kinesisDestination?: pulumi.Input<{ ... }>;
```


Send the events to a kinesis firehose destination

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L115">property matchingTypes</a>
</h3>

```typescript
matchingTypes?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of matching types. May be any of `"send"`, `"reject"`, `"bounce"`, `"complaint"`, `"delivery"`, `"open"`, or `"click"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L119">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the event destination

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/eventDestination.ts#L123">property snsDestination</a>
</h3>

```typescript
snsDestination?: pulumi.Input<{ ... }>;
```


Send the events to an SNS Topic destination

<h2 class="pdoc-module-header" id="IdentityNotificationTopicArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/identityNotificationTopic.ts#L89">interface IdentityNotificationTopicArgs</a>
</h2>

The set of arguments for constructing a IdentityNotificationTopic resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/identityNotificationTopic.ts#L93">property identity</a>
</h3>

```typescript
identity: pulumi.Input<string>;
```


The identity for which the Amazon SNS topic will be set. You can specify an identity by using its name or by using its Amazon Resource Name (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/identityNotificationTopic.ts#L97">property notificationType</a>
</h3>

```typescript
notificationType: pulumi.Input<string>;
```


The type of notifications that will be published to the specified Amazon SNS topic. Valid Values: *Bounce*, *Complaint* or *Delivery*.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/identityNotificationTopic.ts#L101">property topicArn</a>
</h3>

```typescript
topicArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the Amazon SNS topic. Can be set to "" (an empty string) to disable publishing.

<h2 class="pdoc-module-header" id="IdentityNotificationTopicState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/identityNotificationTopic.ts#L71">interface IdentityNotificationTopicState</a>
</h2>

Input properties used for looking up and filtering IdentityNotificationTopic resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/identityNotificationTopic.ts#L75">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<string>;
```


The identity for which the Amazon SNS topic will be set. You can specify an identity by using its name or by using its Amazon Resource Name (ARN).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/identityNotificationTopic.ts#L79">property notificationType</a>
</h3>

```typescript
notificationType?: pulumi.Input<string>;
```


The type of notifications that will be published to the specified Amazon SNS topic. Valid Values: *Bounce*, *Complaint* or *Delivery*.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/identityNotificationTopic.ts#L83">property topicArn</a>
</h3>

```typescript
topicArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the Amazon SNS topic. Can be set to "" (an empty string) to disable publishing.

<h2 class="pdoc-module-header" id="MailFromArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/mailFrom.ts#L91">interface MailFromArgs</a>
</h2>

The set of arguments for constructing a MailFrom resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/mailFrom.ts#L95">property behaviorOnMxFailure</a>
</h3>

```typescript
behaviorOnMxFailure?: pulumi.Input<string>;
```


The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. Defaults to `UseDefaultValue`. See the [SES API documentation](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/mailFrom.ts#L99">property domain</a>
</h3>

```typescript
domain: pulumi.Input<string>;
```


Verified domain name to generate DKIM tokens for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/mailFrom.ts#L103">property mailFromDomain</a>
</h3>

```typescript
mailFromDomain: pulumi.Input<string>;
```


Subdomain (of above domain) which is to be used as MAIL FROM address (Required for DMARC validation)

<h2 class="pdoc-module-header" id="MailFromState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/mailFrom.ts#L73">interface MailFromState</a>
</h2>

Input properties used for looking up and filtering MailFrom resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/mailFrom.ts#L77">property behaviorOnMxFailure</a>
</h3>

```typescript
behaviorOnMxFailure?: pulumi.Input<string>;
```


The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. Defaults to `UseDefaultValue`. See the [SES API documentation](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/mailFrom.ts#L81">property domain</a>
</h3>

```typescript
domain?: pulumi.Input<string>;
```


Verified domain name to generate DKIM tokens for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/mailFrom.ts#L85">property mailFromDomain</a>
</h3>

```typescript
mailFromDomain?: pulumi.Input<string>;
```


Subdomain (of above domain) which is to be used as MAIL FROM address (Required for DMARC validation)

<h2 class="pdoc-module-header" id="ReceiptFilterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptFilter.ts#L89">interface ReceiptFilterArgs</a>
</h2>

The set of arguments for constructing a ReceiptFilter resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptFilter.ts#L93">property cidr</a>
</h3>

```typescript
cidr: pulumi.Input<string>;
```


The IP address or address range to filter, in CIDR notation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptFilter.ts#L97">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the filter

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptFilter.ts#L101">property policy</a>
</h3>

```typescript
policy: pulumi.Input<string>;
```


Block or Allow

<h2 class="pdoc-module-header" id="ReceiptFilterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptFilter.ts#L71">interface ReceiptFilterState</a>
</h2>

Input properties used for looking up and filtering ReceiptFilter resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptFilter.ts#L75">property cidr</a>
</h3>

```typescript
cidr?: pulumi.Input<string>;
```


The IP address or address range to filter, in CIDR notation

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptFilter.ts#L79">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the filter

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptFilter.ts#L83">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


Block or Allow

<h2 class="pdoc-module-header" id="ReceiptRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L196">interface ReceiptRuleArgs</a>
</h2>

The set of arguments for constructing a ReceiptRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L200">property addHeaderActions</a>
</h3>

```typescript
addHeaderActions?: pulumi.Input<{ ... }[]>;
```


A list of Add Header Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L204">property after</a>
</h3>

```typescript
after?: pulumi.Input<string>;
```


The name of the rule to place this rule after

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L208">property bounceActions</a>
</h3>

```typescript
bounceActions?: pulumi.Input<{ ... }[]>;
```


A list of Bounce Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L212">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


If true, the rule will be enabled

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L216">property lambdaActions</a>
</h3>

```typescript
lambdaActions?: pulumi.Input<{ ... }[]>;
```


A list of Lambda Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L220">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L224">property recipients</a>
</h3>

```typescript
recipients?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of email addresses

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L228">property ruleSetName</a>
</h3>

```typescript
ruleSetName: pulumi.Input<string>;
```


The name of the rule set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L232">property s3Actions</a>
</h3>

```typescript
s3Actions?: pulumi.Input<{ ... }[]>;
```


A list of S3 Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L236">property scanEnabled</a>
</h3>

```typescript
scanEnabled?: pulumi.Input<boolean>;
```


If true, incoming emails will be scanned for spam and viruses

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L240">property snsActions</a>
</h3>

```typescript
snsActions?: pulumi.Input<{ ... }[]>;
```


A list of SNS Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L244">property stopActions</a>
</h3>

```typescript
stopActions?: pulumi.Input<{ ... }[]>;
```


A list of Stop Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L248">property tlsPolicy</a>
</h3>

```typescript
tlsPolicy?: pulumi.Input<string>;
```


Require or Optional

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L252">property workmailActions</a>
</h3>

```typescript
workmailActions?: pulumi.Input<{ ... }[]>;
```


A list of WorkMail Action blocks. Documented below.

<h2 class="pdoc-module-header" id="ReceiptRuleSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRuleSet.ts#L66">interface ReceiptRuleSetArgs</a>
</h2>

The set of arguments for constructing a ReceiptRuleSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRuleSet.ts#L70">property ruleSetName</a>
</h3>

```typescript
ruleSetName: pulumi.Input<string>;
```


The name of the rule set

<h2 class="pdoc-module-header" id="ReceiptRuleSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRuleSet.ts#L56">interface ReceiptRuleSetState</a>
</h2>

Input properties used for looking up and filtering ReceiptRuleSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRuleSet.ts#L60">property ruleSetName</a>
</h3>

```typescript
ruleSetName?: pulumi.Input<string>;
```


The name of the rule set

<h2 class="pdoc-module-header" id="ReceiptRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L134">interface ReceiptRuleState</a>
</h2>

Input properties used for looking up and filtering ReceiptRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L138">property addHeaderActions</a>
</h3>

```typescript
addHeaderActions?: pulumi.Input<{ ... }[]>;
```


A list of Add Header Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L142">property after</a>
</h3>

```typescript
after?: pulumi.Input<string>;
```


The name of the rule to place this rule after

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L146">property bounceActions</a>
</h3>

```typescript
bounceActions?: pulumi.Input<{ ... }[]>;
```


A list of Bounce Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L150">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


If true, the rule will be enabled

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L154">property lambdaActions</a>
</h3>

```typescript
lambdaActions?: pulumi.Input<{ ... }[]>;
```


A list of Lambda Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L158">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L162">property recipients</a>
</h3>

```typescript
recipients?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of email addresses

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L166">property ruleSetName</a>
</h3>

```typescript
ruleSetName?: pulumi.Input<string>;
```


The name of the rule set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L170">property s3Actions</a>
</h3>

```typescript
s3Actions?: pulumi.Input<{ ... }[]>;
```


A list of S3 Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L174">property scanEnabled</a>
</h3>

```typescript
scanEnabled?: pulumi.Input<boolean>;
```


If true, incoming emails will be scanned for spam and viruses

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L178">property snsActions</a>
</h3>

```typescript
snsActions?: pulumi.Input<{ ... }[]>;
```


A list of SNS Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L182">property stopActions</a>
</h3>

```typescript
stopActions?: pulumi.Input<{ ... }[]>;
```


A list of Stop Action blocks. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L186">property tlsPolicy</a>
</h3>

```typescript
tlsPolicy?: pulumi.Input<string>;
```


Require or Optional

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/receiptRule.ts#L190">property workmailActions</a>
</h3>

```typescript
workmailActions?: pulumi.Input<{ ... }[]>;
```


A list of WorkMail Action blocks. Documented below.

<h2 class="pdoc-module-header" id="TemplateArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/template.ts#L93">interface TemplateArgs</a>
</h2>

The set of arguments for constructing a Template resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/template.ts#L97">property html</a>
</h3>

```typescript
html?: pulumi.Input<string>;
```


The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/template.ts#L101">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/template.ts#L105">property subject</a>
</h3>

```typescript
subject?: pulumi.Input<string>;
```


The subject line of the email.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/template.ts#L109">property text</a>
</h3>

```typescript
text?: pulumi.Input<string>;
```


The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.

<h2 class="pdoc-module-header" id="TemplateState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/template.ts#L71">interface TemplateState</a>
</h2>

Input properties used for looking up and filtering Template resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/template.ts#L75">property html</a>
</h3>

```typescript
html?: pulumi.Input<string>;
```


The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/template.ts#L79">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/template.ts#L83">property subject</a>
</h3>

```typescript
subject?: pulumi.Input<string>;
```


The subject line of the email.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/ses/template.ts#L87">property text</a>
</h3>

```typescript
text?: pulumi.Input<string>;
```


The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.

