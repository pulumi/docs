---
title: Module guardduty
---

<a href="../index.html">@pulumi/aws</a> &gt; guardduty

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Detector">class Detector</a>
* <a href="#IPSet">class IPSet</a>
* <a href="#Member">class Member</a>
* <a href="#ThreatIntelSet">class ThreatIntelSet</a>
* <a href="#DetectorArgs">interface DetectorArgs</a>
* <a href="#DetectorState">interface DetectorState</a>
* <a href="#IPSetArgs">interface IPSetArgs</a>
* <a href="#IPSetState">interface IPSetState</a>
* <a href="#MemberArgs">interface MemberArgs</a>
* <a href="#MemberState">interface MemberState</a>
* <a href="#ThreatIntelSetArgs">interface ThreatIntelSetArgs</a>
* <a href="#ThreatIntelSetState">interface ThreatIntelSetState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/detector.ts">guardduty/detector.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts">guardduty/iPSet.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts">guardduty/member.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts">guardduty/threatIntelSet.ts</a> 


<h2 class="pdoc-module-header" id="Detector">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/detector.ts#L12">class Detector</a>
</h2>

Provides a resource to manage a GuardDuty detector.

~> **NOTE:** Deleting this resource is equivalent to "disabling" GuardDuty for an AWS region, which removes all existing findings. You can set the `enable` attribute to `false` to instead "suspend" monitoring and feedback reporting while keeping existing data. See the [Suspending or Disabling Amazon GuardDuty documentation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_suspend-disable.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/detector.ts#L32">constructor</a>
</h3>

```typescript
new Detector(name: string, args?: DetectorArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Detector resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/detector.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DetectorState): Detector
```


Get an existing Detector resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/detector.ts#L28">property accountId</a>
</h3>

```typescript
public accountId: pulumi.Output<string>;
```


The AWS account ID of the GuardDuty detector

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/detector.ts#L32">property enable</a>
</h3>

```typescript
public enable: pulumi.Output<boolean | undefined>;
```


Enable monitoring and feedback reporting. Setting to `false` is equivalent to "suspending" GuardDuty. Defaults to `true`.

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

<h2 class="pdoc-module-header" id="IPSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L12">class IPSet</a>
</h2>

Provides a resource to manage a GuardDuty IPSet.

~> **Note:** Currently in GuardDuty, users from member accounts cannot upload and further manage IPSets. IPSets that are uploaded by the master account are imposed on GuardDuty functionality in its member accounts. See the [GuardDuty API Documentation](https://docs.aws.amazon.com/guardduty/latest/ug/create-ip-set.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L44">constructor</a>
</h3>

```typescript
new IPSet(name: string, args: IPSetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IPSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IPSetState): IPSet
```


Get an existing IPSet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L28">property activate</a>
</h3>

```typescript
public activate: pulumi.Output<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L32">property detectorId</a>
</h3>

```typescript
public detectorId: pulumi.Output<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L36">property format</a>
</h3>

```typescript
public format: pulumi.Output<string>;
```


The format of the file that contains the IPSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L40">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The URI of the file that contains the IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The friendly name to identify the IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Member">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L12">class Member</a>
</h2>

Provides a resource to manage a GuardDuty member.

~> **NOTE:** Currently after using this resource, you must manually accept member account invitations before GuardDuty will begin sending cross-account events. More information for how to accomplish this via the AWS Console or API can be found in the [GuardDuty User Guide](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html). Terraform implementation of the member acceptance resource can be tracked in [Github](https://github.com/terraform-providers/terraform-provider-aws/issues/2489).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L52">constructor</a>
</h3>

```typescript
new Member(name: string, args: MemberArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Member resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MemberState): Member
```


Get an existing Member resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L28">property accountId</a>
</h3>

```typescript
public accountId: pulumi.Output<string>;
```


AWS account ID for member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L32">property detectorId</a>
</h3>

```typescript
public detectorId: pulumi.Output<string>;
```


The detector ID of the GuardDuty account where you want to create member accounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L36">property disableEmailNotification</a>
</h3>

```typescript
public disableEmailNotification: pulumi.Output<boolean | undefined>;
```


Boolean whether an email notification is sent to the accounts. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L40">property email</a>
</h3>

```typescript
public email: pulumi.Output<string>;
```


Email address for member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L44">property invitationMessage</a>
</h3>

```typescript
public invitationMessage: pulumi.Output<string | undefined>;
```


Message for invitation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L48">property invite</a>
</h3>

```typescript
public invite: pulumi.Output<boolean | undefined>;
```


Boolean whether to invite the account to GuardDuty as a member. Defaults to `false`. To detect if an invitation needs to be (re-)sent, the Terraform state value is `true` based on a `relationship_status` of `Disabled`, `Enabled`, `Invited`, or `EmailVerificationInProgress`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L52">property relationshipStatus</a>
</h3>

```typescript
public relationshipStatus: pulumi.Output<string>;
```


The status of the relationship between the member account and its master account. More information can be found in [Amazon GuardDuty API Reference](https://docs.aws.amazon.com/guardduty/latest/ug/get-members.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ThreatIntelSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L12">class ThreatIntelSet</a>
</h2>

Provides a resource to manage a GuardDuty ThreatIntelSet.

~> **Note:** Currently in GuardDuty, users from member accounts cannot upload and further manage ThreatIntelSets. ThreatIntelSets that are uploaded by the master account are imposed on GuardDuty functionality in its member accounts. See the [GuardDuty API Documentation](https://docs.aws.amazon.com/guardduty/latest/ug/create-threat-intel-set.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L44">constructor</a>
</h3>

```typescript
new ThreatIntelSet(name: string, args: ThreatIntelSetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ThreatIntelSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ThreatIntelSetState): ThreatIntelSet
```


Get an existing ThreatIntelSet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L28">property activate</a>
</h3>

```typescript
public activate: pulumi.Output<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L32">property detectorId</a>
</h3>

```typescript
public detectorId: pulumi.Output<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L36">property format</a>
</h3>

```typescript
public format: pulumi.Output<string>;
```


The format of the file that contains the ThreatIntelSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L40">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The URI of the file that contains the ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The friendly name to identify the ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DetectorArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/detector.ts#L74">interface DetectorArgs</a>
</h2>

The set of arguments for constructing a Detector resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/detector.ts#L78">property enable</a>
</h3>

```typescript
enable?: pulumi.Input<boolean>;
```


Enable monitoring and feedback reporting. Setting to `false` is equivalent to "suspending" GuardDuty. Defaults to `true`.

<h2 class="pdoc-module-header" id="DetectorState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/detector.ts#L60">interface DetectorState</a>
</h2>

Input properties used for looking up and filtering Detector resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/detector.ts#L64">property accountId</a>
</h3>

```typescript
accountId?: pulumi.Input<string>;
```


The AWS account ID of the GuardDuty detector

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/detector.ts#L68">property enable</a>
</h3>

```typescript
enable?: pulumi.Input<boolean>;
```


Enable monitoring and feedback reporting. Setting to `false` is equivalent to "suspending" GuardDuty. Defaults to `true`.

<h2 class="pdoc-module-header" id="IPSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L116">interface IPSetArgs</a>
</h2>

The set of arguments for constructing a IPSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L120">property activate</a>
</h3>

```typescript
activate: pulumi.Input<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L124">property detectorId</a>
</h3>

```typescript
detectorId: pulumi.Input<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L128">property format</a>
</h3>

```typescript
format: pulumi.Input<string>;
```


The format of the file that contains the IPSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L132">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The URI of the file that contains the IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L136">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name to identify the IPSet.

<h2 class="pdoc-module-header" id="IPSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L90">interface IPSetState</a>
</h2>

Input properties used for looking up and filtering IPSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L94">property activate</a>
</h3>

```typescript
activate?: pulumi.Input<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L98">property detectorId</a>
</h3>

```typescript
detectorId?: pulumi.Input<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L102">property format</a>
</h3>

```typescript
format?: pulumi.Input<string>;
```


The format of the file that contains the IPSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L106">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The URI of the file that contains the IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/iPSet.ts#L110">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name to identify the IPSet.

<h2 class="pdoc-module-header" id="MemberArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L133">interface MemberArgs</a>
</h2>

The set of arguments for constructing a Member resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L137">property accountId</a>
</h3>

```typescript
accountId: pulumi.Input<string>;
```


AWS account ID for member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L141">property detectorId</a>
</h3>

```typescript
detectorId: pulumi.Input<string>;
```


The detector ID of the GuardDuty account where you want to create member accounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L145">property disableEmailNotification</a>
</h3>

```typescript
disableEmailNotification?: pulumi.Input<boolean>;
```


Boolean whether an email notification is sent to the accounts. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L149">property email</a>
</h3>

```typescript
email: pulumi.Input<string>;
```


Email address for member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L153">property invitationMessage</a>
</h3>

```typescript
invitationMessage?: pulumi.Input<string>;
```


Message for invitation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L157">property invite</a>
</h3>

```typescript
invite?: pulumi.Input<boolean>;
```


Boolean whether to invite the account to GuardDuty as a member. Defaults to `false`. To detect if an invitation needs to be (re-)sent, the Terraform state value is `true` based on a `relationship_status` of `Disabled`, `Enabled`, `Invited`, or `EmailVerificationInProgress`.

<h2 class="pdoc-module-header" id="MemberState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L99">interface MemberState</a>
</h2>

Input properties used for looking up and filtering Member resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L103">property accountId</a>
</h3>

```typescript
accountId?: pulumi.Input<string>;
```


AWS account ID for member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L107">property detectorId</a>
</h3>

```typescript
detectorId?: pulumi.Input<string>;
```


The detector ID of the GuardDuty account where you want to create member accounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L111">property disableEmailNotification</a>
</h3>

```typescript
disableEmailNotification?: pulumi.Input<boolean>;
```


Boolean whether an email notification is sent to the accounts. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L115">property email</a>
</h3>

```typescript
email?: pulumi.Input<string>;
```


Email address for member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L119">property invitationMessage</a>
</h3>

```typescript
invitationMessage?: pulumi.Input<string>;
```


Message for invitation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L123">property invite</a>
</h3>

```typescript
invite?: pulumi.Input<boolean>;
```


Boolean whether to invite the account to GuardDuty as a member. Defaults to `false`. To detect if an invitation needs to be (re-)sent, the Terraform state value is `true` based on a `relationship_status` of `Disabled`, `Enabled`, `Invited`, or `EmailVerificationInProgress`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/member.ts#L127">property relationshipStatus</a>
</h3>

```typescript
relationshipStatus?: pulumi.Input<string>;
```


The status of the relationship between the member account and its master account. More information can be found in [Amazon GuardDuty API Reference](https://docs.aws.amazon.com/guardduty/latest/ug/get-members.html).

<h2 class="pdoc-module-header" id="ThreatIntelSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L116">interface ThreatIntelSetArgs</a>
</h2>

The set of arguments for constructing a ThreatIntelSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L120">property activate</a>
</h3>

```typescript
activate: pulumi.Input<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L124">property detectorId</a>
</h3>

```typescript
detectorId: pulumi.Input<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L128">property format</a>
</h3>

```typescript
format: pulumi.Input<string>;
```


The format of the file that contains the ThreatIntelSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L132">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The URI of the file that contains the ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L136">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name to identify the ThreatIntelSet.

<h2 class="pdoc-module-header" id="ThreatIntelSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L90">interface ThreatIntelSetState</a>
</h2>

Input properties used for looking up and filtering ThreatIntelSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L94">property activate</a>
</h3>

```typescript
activate?: pulumi.Input<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L98">property detectorId</a>
</h3>

```typescript
detectorId?: pulumi.Input<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L102">property format</a>
</h3>

```typescript
format?: pulumi.Input<string>;
```


The format of the file that contains the ThreatIntelSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L106">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The URI of the file that contains the ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/guardduty/threatIntelSet.ts#L110">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name to identify the ThreatIntelSet.

