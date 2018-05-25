---
title: Module organizations
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Account">class Account</a>
* <a href="#Organization">class Organization</a>
* <a href="#AccountArgs">interface AccountArgs</a>
* <a href="#AccountState">interface AccountState</a>
* <a href="#OrganizationArgs">interface OrganizationArgs</a>
* <a href="#OrganizationState">interface OrganizationState</a>

<a href="/organizations/account.ts">organizations/account.ts</a> <a href="/organizations/organization.ts">organizations/organization.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Account">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L13">class Account</a>
</h2>

Provides a resource to create a member account in the current organization.

~> **Note:** Account management must be done from the organization's master account.

!> **WARNING:** Deleting this Terraform resource will only remove an AWS account from an organization. Terraform will not close the account. The member account must be prepared to be a standalone account beforehand. See the [AWS Organizations documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L45">constructor</a>
</h3>

```typescript
new Account(name: string, args: AccountArgs, opts?: pulumi.ResourceOptions)
```


Create a Account resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Account(name: string, state?: AccountState, opts?: pulumi.ResourceOptions)
```


Create a Account resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccountState): Account
```


Get an existing Account resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L30">property email</a>
</h3>

```typescript
public email: pulumi.Output<string>;
```


The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L34">property iamUserAccessToBilling</a>
</h3>

```typescript
public iamUserAccessToBilling: pulumi.Output<string | undefined>;
```


If set to `ALLOW`, the new account enables IAM users to access account billing information if they have the required permissions. If set to `DENY`, then only the root user of the new account can access account billing information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L35">property joinedMethod</a>
</h3>

```typescript
public joinedMethod: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L36">property joinedTimestamp</a>
</h3>

```typescript
public joinedTimestamp: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L40">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A friendly name for the member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L44">property roleName</a>
</h3>

```typescript
public roleName: pulumi.Output<string | undefined>;
```


The name of an IAM role that Organizations automatically preconfigures in the new member account. This role trusts the master account, allowing users in the master account to assume the role, as permitted by the master account administrator. The role has administrator permissions in the new member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L45">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Organization">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/organization.ts#L9">class Organization</a>
</h2>

Provides a resource to create an organization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/organization.ts#L41">constructor</a>
</h3>

```typescript
new Organization(name: string, args?: OrganizationArgs, opts?: pulumi.ResourceOptions)
```


Create a Organization resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Organization(name: string, state?: OrganizationState, opts?: pulumi.ResourceOptions)
```


Create a Organization resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/organization.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OrganizationState): Organization
```


Get an existing Organization resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/organization.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


ARN of the organization

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/organization.ts#L29">property featureSet</a>
</h3>

```typescript
public featureSet: pulumi.Output<string | undefined>;
```


Specify "ALL" (default) or "CONSOLIDATED_BILLING".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/organization.ts#L33">property masterAccountArn</a>
</h3>

```typescript
public masterAccountArn: pulumi.Output<string>;
```


ARN of the master account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/organization.ts#L37">property masterAccountEmail</a>
</h3>

```typescript
public masterAccountEmail: pulumi.Output<string>;
```


Email address of the master account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/organization.ts#L41">property masterAccountId</a>
</h3>

```typescript
public masterAccountId: pulumi.Output<string>;
```


Identifier of the master account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L116">interface AccountArgs</a>
</h2>

The set of arguments for constructing a Account resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L120">property email</a>
</h3>

```typescript
email: pulumi.Input<string>;
```


The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L124">property iamUserAccessToBilling</a>
</h3>

```typescript
iamUserAccessToBilling?: pulumi.Input<string>;
```


If set to `ALLOW`, the new account enables IAM users to access account billing information if they have the required permissions. If set to `DENY`, then only the root user of the new account can access account billing information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L128">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A friendly name for the member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L132">property roleName</a>
</h3>

```typescript
roleName?: pulumi.Input<string>;
```


The name of an IAM role that Organizations automatically preconfigures in the new member account. This role trusts the master account, allowing users in the master account to assume the role, as permitted by the master account administrator. The role has administrator permissions in the new member account.

<h2 class="pdoc-module-header" id="AccountState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L90">interface AccountState</a>
</h2>

Input properties used for looking up and filtering Account resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L91">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L95">property email</a>
</h3>

```typescript
email?: pulumi.Input<string>;
```


The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L99">property iamUserAccessToBilling</a>
</h3>

```typescript
iamUserAccessToBilling?: pulumi.Input<string>;
```


If set to `ALLOW`, the new account enables IAM users to access account billing information if they have the required permissions. If set to `DENY`, then only the root user of the new account can access account billing information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L100">property joinedMethod</a>
</h3>

```typescript
joinedMethod?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L101">property joinedTimestamp</a>
</h3>

```typescript
joinedTimestamp?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L105">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A friendly name for the member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L109">property roleName</a>
</h3>

```typescript
roleName?: pulumi.Input<string>;
```


The name of an IAM role that Organizations automatically preconfigures in the new member account. This role trusts the master account, allowing users in the master account to assume the role, as permitted by the master account administrator. The role has administrator permissions in the new member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/account.ts#L110">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="OrganizationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/organization.ts#L103">interface OrganizationArgs</a>
</h2>

The set of arguments for constructing a Organization resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/organization.ts#L107">property featureSet</a>
</h3>

```typescript
featureSet?: pulumi.Input<string>;
```


Specify "ALL" (default) or "CONSOLIDATED_BILLING".

<h2 class="pdoc-module-header" id="OrganizationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/organization.ts#L77">interface OrganizationState</a>
</h2>

Input properties used for looking up and filtering Organization resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/organization.ts#L81">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


ARN of the organization

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/organization.ts#L85">property featureSet</a>
</h3>

```typescript
featureSet?: pulumi.Input<string>;
```


Specify "ALL" (default) or "CONSOLIDATED_BILLING".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/organization.ts#L89">property masterAccountArn</a>
</h3>

```typescript
masterAccountArn?: pulumi.Input<string>;
```


ARN of the master account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/organization.ts#L93">property masterAccountEmail</a>
</h3>

```typescript
masterAccountEmail?: pulumi.Input<string>;
```


Email address of the master account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/organizations/organization.ts#L97">property masterAccountId</a>
</h3>

```typescript
masterAccountId?: pulumi.Input<string>;
```


Identifier of the master account

