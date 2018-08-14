---
title: Module organizations
---

<a href="../index.html">@pulumi/aws</a> &gt; organizations

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Account">class Account</a>
* <a href="#Organization">class Organization</a>
* <a href="#Policy">class Policy</a>
* <a href="#PolicyAttachment">class PolicyAttachment</a>
* <a href="#AccountArgs">interface AccountArgs</a>
* <a href="#AccountState">interface AccountState</a>
* <a href="#OrganizationArgs">interface OrganizationArgs</a>
* <a href="#OrganizationState">interface OrganizationState</a>
* <a href="#PolicyArgs">interface PolicyArgs</a>
* <a href="#PolicyAttachmentArgs">interface PolicyAttachmentArgs</a>
* <a href="#PolicyAttachmentState">interface PolicyAttachmentState</a>
* <a href="#PolicyState">interface PolicyState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts">organizations/account.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/organization.ts">organizations/organization.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts">organizations/policy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policyAttachment.ts">organizations/policyAttachment.ts</a> 


<h2 class="pdoc-module-header" id="Account">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L13">class Account</a>
</h2>

Provides a resource to create a member account in the current organization.

~> **Note:** Account management must be done from the organization's master account.

!> **WARNING:** Deleting this Terraform resource will only remove an AWS account from an organization. Terraform will not close the account. The member account must be prepared to be a standalone account beforehand. See the [AWS Organizations documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L48">constructor</a>
</h3>

```typescript
new Account(name: string, args: AccountArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Account resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccountState): Account
```


Get an existing Account resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L29">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN for this account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L33">property email</a>
</h3>

```typescript
public email: pulumi.Output<string>;
```


The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L37">property iamUserAccessToBilling</a>
</h3>

```typescript
public iamUserAccessToBilling: pulumi.Output<string | undefined>;
```


If set to `ALLOW`, the new account enables IAM users to access account billing information if they have the required permissions. If set to `DENY`, then only the root user of the new account can access account billing information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L38">property joinedMethod</a>
</h3>

```typescript
public joinedMethod: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L39">property joinedTimestamp</a>
</h3>

```typescript
public joinedTimestamp: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L43">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A friendly name for the member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L47">property roleName</a>
</h3>

```typescript
public roleName: pulumi.Output<string | undefined>;
```


The name of an IAM role that Organizations automatically preconfigures in the new member account. This role trusts the master account, allowing users in the master account to assume the role, as permitted by the master account administrator. The role has administrator permissions in the new member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L48">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Organization">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/organization.ts#L9">class Organization</a>
</h2>

Provides a resource to create an organization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/organization.ts#L41">constructor</a>
</h3>

```typescript
new Organization(name: string, args?: OrganizationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Organization resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/organization.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OrganizationState): Organization
```


Get an existing Organization resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/organization.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


ARN of the organization

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/organization.ts#L29">property featureSet</a>
</h3>

```typescript
public featureSet: pulumi.Output<string | undefined>;
```


Specify "ALL" (default) or "CONSOLIDATED_BILLING".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/organization.ts#L33">property masterAccountArn</a>
</h3>

```typescript
public masterAccountArn: pulumi.Output<string>;
```


ARN of the master account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/organization.ts#L37">property masterAccountEmail</a>
</h3>

```typescript
public masterAccountEmail: pulumi.Output<string>;
```


Email address of the master account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/organization.ts#L41">property masterAccountId</a>
</h3>

```typescript
public masterAccountId: pulumi.Output<string>;
```


Identifier of the master account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Policy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L9">class Policy</a>
</h2>

Provides a resource to manage an [AWS Organizations policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L41">constructor</a>
</h3>

```typescript
new Policy(name: string, args: PolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Policy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L29">property content</a>
</h3>

```typescript
public content: pulumi.Output<string>;
```


The policy content to add to the new policy. For example, if you create a [service control policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html), this string must be JSON text that specifies the permissions that admins in attached accounts can delegate to their users, groups, and roles. For more information about the SCP syntax, see the [Service Control Policy Syntax documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L33">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description to assign to the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The friendly name to assign to the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L41">property type</a>
</h3>

```typescript
public type: pulumi.Output<string | undefined>;
```


The type of policy to create. Currently, the only valid value is `SERVICE_CONTROL_POLICY` (SCP).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="PolicyAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policyAttachment.ts#L9">class PolicyAttachment</a>
</h2>

Provides a resource to attach an AWS Organizations policy to an organization account, root, or unit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policyAttachment.ts#L29">constructor</a>
</h3>

```typescript
new PolicyAttachment(name: string, args: PolicyAttachmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a PolicyAttachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policyAttachment.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyAttachmentState): PolicyAttachment
```


Get an existing PolicyAttachment resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policyAttachment.ts#L25">property policyId</a>
</h3>

```typescript
public policyId: pulumi.Output<string>;
```


The unique identifier (ID) of the policy that you want to attach to the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policyAttachment.ts#L29">property targetId</a>
</h3>

```typescript
public targetId: pulumi.Output<string>;
```


The unique identifier (ID) of the root, organizational unit, or account number that you want to attach the policy to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L120">interface AccountArgs</a>
</h2>

The set of arguments for constructing a Account resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L124">property email</a>
</h3>

```typescript
email: pulumi.Input<string>;
```


The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L128">property iamUserAccessToBilling</a>
</h3>

```typescript
iamUserAccessToBilling?: pulumi.Input<string>;
```


If set to `ALLOW`, the new account enables IAM users to access account billing information if they have the required permissions. If set to `DENY`, then only the root user of the new account can access account billing information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L132">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A friendly name for the member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L136">property roleName</a>
</h3>

```typescript
roleName?: pulumi.Input<string>;
```


The name of an IAM role that Organizations automatically preconfigures in the new member account. This role trusts the master account, allowing users in the master account to assume the role, as permitted by the master account administrator. The role has administrator permissions in the new member account.

<h2 class="pdoc-module-header" id="AccountState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L91">interface AccountState</a>
</h2>

Input properties used for looking up and filtering Account resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L95">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN for this account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L99">property email</a>
</h3>

```typescript
email?: pulumi.Input<string>;
```


The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L103">property iamUserAccessToBilling</a>
</h3>

```typescript
iamUserAccessToBilling?: pulumi.Input<string>;
```


If set to `ALLOW`, the new account enables IAM users to access account billing information if they have the required permissions. If set to `DENY`, then only the root user of the new account can access account billing information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L104">property joinedMethod</a>
</h3>

```typescript
joinedMethod?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L105">property joinedTimestamp</a>
</h3>

```typescript
joinedTimestamp?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L109">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A friendly name for the member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L113">property roleName</a>
</h3>

```typescript
roleName?: pulumi.Input<string>;
```


The name of an IAM role that Organizations automatically preconfigures in the new member account. This role trusts the master account, allowing users in the master account to assume the role, as permitted by the master account administrator. The role has administrator permissions in the new member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/account.ts#L114">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="OrganizationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/organization.ts#L101">interface OrganizationArgs</a>
</h2>

The set of arguments for constructing a Organization resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/organization.ts#L105">property featureSet</a>
</h3>

```typescript
featureSet?: pulumi.Input<string>;
```


Specify "ALL" (default) or "CONSOLIDATED_BILLING".

<h2 class="pdoc-module-header" id="OrganizationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/organization.ts#L75">interface OrganizationState</a>
</h2>

Input properties used for looking up and filtering Organization resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/organization.ts#L79">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


ARN of the organization

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/organization.ts#L83">property featureSet</a>
</h3>

```typescript
featureSet?: pulumi.Input<string>;
```


Specify "ALL" (default) or "CONSOLIDATED_BILLING".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/organization.ts#L87">property masterAccountArn</a>
</h3>

```typescript
masterAccountArn?: pulumi.Input<string>;
```


ARN of the master account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/organization.ts#L91">property masterAccountEmail</a>
</h3>

```typescript
masterAccountEmail?: pulumi.Input<string>;
```


Email address of the master account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/organization.ts#L95">property masterAccountId</a>
</h3>

```typescript
masterAccountId?: pulumi.Input<string>;
```


Identifier of the master account

<h2 class="pdoc-module-header" id="PolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L104">interface PolicyArgs</a>
</h2>

The set of arguments for constructing a Policy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L108">property content</a>
</h3>

```typescript
content: pulumi.Input<string>;
```


The policy content to add to the new policy. For example, if you create a [service control policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html), this string must be JSON text that specifies the permissions that admins in attached accounts can delegate to their users, groups, and roles. For more information about the SCP syntax, see the [Service Control Policy Syntax documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L112">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description to assign to the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L116">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name to assign to the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L120">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of policy to create. Currently, the only valid value is `SERVICE_CONTROL_POLICY` (SCP).

<h2 class="pdoc-module-header" id="PolicyAttachmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policyAttachment.ts#L77">interface PolicyAttachmentArgs</a>
</h2>

The set of arguments for constructing a PolicyAttachment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policyAttachment.ts#L81">property policyId</a>
</h3>

```typescript
policyId: pulumi.Input<string>;
```


The unique identifier (ID) of the policy that you want to attach to the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policyAttachment.ts#L85">property targetId</a>
</h3>

```typescript
targetId: pulumi.Input<string>;
```


The unique identifier (ID) of the root, organizational unit, or account number that you want to attach the policy to.

<h2 class="pdoc-module-header" id="PolicyAttachmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policyAttachment.ts#L63">interface PolicyAttachmentState</a>
</h2>

Input properties used for looking up and filtering PolicyAttachment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policyAttachment.ts#L67">property policyId</a>
</h3>

```typescript
policyId?: pulumi.Input<string>;
```


The unique identifier (ID) of the policy that you want to attach to the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policyAttachment.ts#L71">property targetId</a>
</h3>

```typescript
targetId?: pulumi.Input<string>;
```


The unique identifier (ID) of the root, organizational unit, or account number that you want to attach the policy to.

<h2 class="pdoc-module-header" id="PolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L78">interface PolicyState</a>
</h2>

Input properties used for looking up and filtering Policy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L82">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L86">property content</a>
</h3>

```typescript
content?: pulumi.Input<string>;
```


The policy content to add to the new policy. For example, if you create a [service control policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html), this string must be JSON text that specifies the permissions that admins in attached accounts can delegate to their users, groups, and roles. For more information about the SCP syntax, see the [Service Control Policy Syntax documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L90">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description to assign to the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L94">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name to assign to the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/organizations/policy.ts#L98">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of policy to create. Currently, the only valid value is `SERVICE_CONTROL_POLICY` (SCP).

