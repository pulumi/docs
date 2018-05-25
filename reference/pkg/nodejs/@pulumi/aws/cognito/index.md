---
title: Module cognito
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#IdentityPool">class IdentityPool</a>
* <a href="#IdentityPoolRoleAttachment">class IdentityPoolRoleAttachment</a>
* <a href="#UserGroup">class UserGroup</a>
* <a href="#UserPool">class UserPool</a>
* <a href="#UserPoolClient">class UserPoolClient</a>
* <a href="#UserPoolDomain">class UserPoolDomain</a>
* <a href="#IdentityPoolArgs">interface IdentityPoolArgs</a>
* <a href="#IdentityPoolRoleAttachmentArgs">interface IdentityPoolRoleAttachmentArgs</a>
* <a href="#IdentityPoolRoleAttachmentState">interface IdentityPoolRoleAttachmentState</a>
* <a href="#IdentityPoolState">interface IdentityPoolState</a>
* <a href="#UserGroupArgs">interface UserGroupArgs</a>
* <a href="#UserGroupState">interface UserGroupState</a>
* <a href="#UserPoolArgs">interface UserPoolArgs</a>
* <a href="#UserPoolClientArgs">interface UserPoolClientArgs</a>
* <a href="#UserPoolClientState">interface UserPoolClientState</a>
* <a href="#UserPoolDomainArgs">interface UserPoolDomainArgs</a>
* <a href="#UserPoolDomainState">interface UserPoolDomainState</a>
* <a href="#UserPoolState">interface UserPoolState</a>

<a href="/cognito/identityPool.ts">cognito/identityPool.ts</a> <a href="/cognito/identityPoolRoleAttachment.ts">cognito/identityPoolRoleAttachment.ts</a> <a href="/cognito/userGroup.ts">cognito/userGroup.ts</a> <a href="/cognito/userPool.ts">cognito/userPool.ts</a> <a href="/cognito/userPoolClient.ts">cognito/userPoolClient.ts</a> <a href="/cognito/userPoolDomain.ts">cognito/userPoolDomain.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="IdentityPool">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L9">class IdentityPool</a>
</h2>

Provides an AWS Cognito Identity Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L50">constructor</a>
</h3>

```typescript
new IdentityPool(name: string, args: IdentityPoolArgs, opts?: pulumi.ResourceOptions)
```


Create a IdentityPool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new IdentityPool(name: string, state?: IdentityPoolState, opts?: pulumi.ResourceOptions)
```


Create a IdentityPool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IdentityPoolState): IdentityPool
```


Get an existing IdentityPool resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L25">property allowUnauthenticatedIdentities</a>
</h3>

```typescript
public allowUnauthenticatedIdentities: pulumi.Output<boolean | undefined>;
```


Whether the identity pool supports unauthenticated logins or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L29">property cognitoIdentityProviders</a>
</h3>

```typescript
public cognitoIdentityProviders: pulumi.Output<{ ... }[] | undefined>;
```


An array of [Amazon Cognito Identity user pools](#cognito-identity-providers) and their client IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L34">property developerProviderName</a>
</h3>

```typescript
public developerProviderName: pulumi.Output<string | undefined>;
```


The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L38">property identityPoolName</a>
</h3>

```typescript
public identityPoolName: pulumi.Output<string>;
```


The Cognito Identity Pool name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L42">property openidConnectProviderArns</a>
</h3>

```typescript
public openidConnectProviderArns: pulumi.Output<string[] | undefined>;
```


A list of OpendID Connect provider ARNs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L46">property samlProviderArns</a>
</h3>

```typescript
public samlProviderArns: pulumi.Output<string[] | undefined>;
```


An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L50">property supportedLoginProviders</a>
</h3>

```typescript
public supportedLoginProviders: pulumi.Output<{ ... } | undefined>;
```


Key-Value pairs mapping provider names to provider app IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IdentityPoolRoleAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPoolRoleAttachment.ts#L9">class IdentityPoolRoleAttachment</a>
</h2>

Provides an AWS Cognito Identity Pool Roles Attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPoolRoleAttachment.ts#L33">constructor</a>
</h3>

```typescript
new IdentityPoolRoleAttachment(name: string, args: IdentityPoolRoleAttachmentArgs, opts?: pulumi.ResourceOptions)
```


Create a IdentityPoolRoleAttachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new IdentityPoolRoleAttachment(name: string, state?: IdentityPoolRoleAttachmentState, opts?: pulumi.ResourceOptions)
```


Create a IdentityPoolRoleAttachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPoolRoleAttachment.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IdentityPoolRoleAttachmentState): IdentityPoolRoleAttachment
```


Get an existing IdentityPoolRoleAttachment resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPoolRoleAttachment.ts#L25">property identityPoolId</a>
</h3>

```typescript
public identityPoolId: pulumi.Output<string>;
```


An identity pool ID in the format REGION:GUID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPoolRoleAttachment.ts#L29">property roleMappings</a>
</h3>

```typescript
public roleMappings: pulumi.Output<{ ... }[] | undefined>;
```


A List of [Role Mapping](#role-mappings).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPoolRoleAttachment.ts#L33">property roles</a>
</h3>

```typescript
public roles: pulumi.Output<{ ... }>;
```


The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="UserGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L9">class UserGroup</a>
</h2>

Provides a Cognito User Group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L41">constructor</a>
</h3>

```typescript
new UserGroup(name: string, args: UserGroupArgs, opts?: pulumi.ResourceOptions)
```


Create a UserGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new UserGroup(name: string, state?: UserGroupState, opts?: pulumi.ResourceOptions)
```


Create a UserGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserGroupState): UserGroup
```


Get an existing UserGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L25">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L33">property precedence</a>
</h3>

```typescript
public precedence: pulumi.Output<number | undefined>;
```


The precedence of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L37">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string | undefined>;
```


The ARN of the IAM role to be associated with the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L41">property userPoolId</a>
</h3>

```typescript
public userPoolId: pulumi.Output<string>;
```


The user pool ID.

<h2 class="pdoc-module-header" id="UserPool">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L9">class UserPool</a>
</h2>

Provides a Cognito User Pool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L105">constructor</a>
</h3>

```typescript
new UserPool(name: string, args?: UserPoolArgs, opts?: pulumi.ResourceOptions)
```


Create a UserPool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new UserPool(name: string, state?: UserPoolState, opts?: pulumi.ResourceOptions)
```


Create a UserPool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserPoolState): UserPool
```


Get an existing UserPool resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L25">property adminCreateUserConfig</a>
</h3>

```typescript
public adminCreateUserConfig: pulumi.Output<{ ... }>;
```


The configuration for [AdminCreateUser](#admin-create-user-config) requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L29">property aliasAttributes</a>
</h3>

```typescript
public aliasAttributes: pulumi.Output<string[] | undefined>;
```


Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L33">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the user pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L37">property autoVerifiedAttributes</a>
</h3>

```typescript
public autoVerifiedAttributes: pulumi.Output<string[] | undefined>;
```


The attributes to be auto-verified. Possible values: email, phone_number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L41">property creationDate</a>
</h3>

```typescript
public creationDate: pulumi.Output<string>;
```


The date the user pool was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L45">property deviceConfiguration</a>
</h3>

```typescript
public deviceConfiguration: pulumi.Output<{ ... } | undefined>;
```


The configuration for the [user pool's device tracking](#device-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L49">property emailConfiguration</a>
</h3>

```typescript
public emailConfiguration: pulumi.Output<{ ... } | undefined>;
```


The [Email Configuration](#email-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L53">property emailVerificationMessage</a>
</h3>

```typescript
public emailVerificationMessage: pulumi.Output<string>;
```


A string representing the email verification message. Must contain the `{####}` placeholder. **NOTE:** - If `email_verification_message` and `verification_message_template.email_message` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L57">property emailVerificationSubject</a>
</h3>

```typescript
public emailVerificationSubject: pulumi.Output<string>;
```


A string representing the email verification subject. **NOTE:** - If `email_verification_subject` and `verification_message_template.email_subject` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L61">property lambdaConfig</a>
</h3>

```typescript
public lambdaConfig: pulumi.Output<{ ... }>;
```


A container for the AWS [Lambda triggers](#lambda-configuration) associated with the user pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L65">property lastModifiedDate</a>
</h3>

```typescript
public lastModifiedDate: pulumi.Output<string>;
```


The date the user pool was last modified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L69">property mfaConfiguration</a>
</h3>

```typescript
public mfaConfiguration: pulumi.Output<string | undefined>;
```


Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L73">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the attribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L77">property passwordPolicy</a>
</h3>

```typescript
public passwordPolicy: pulumi.Output<{ ... }>;
```


A container for information about the [user pool password policy](#password-policy).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L81">property schemas</a>
</h3>

```typescript
public schemas: pulumi.Output<{ ... }[] | undefined>;
```


A container with the [schema attributes](#schema-attributes) of a user pool. Maximum of 50 attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L85">property smsAuthenticationMessage</a>
</h3>

```typescript
public smsAuthenticationMessage: pulumi.Output<string | undefined>;
```


A string representing the SMS authentication message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L89">property smsConfiguration</a>
</h3>

```typescript
public smsConfiguration: pulumi.Output<{ ... } | undefined>;
```


The [SMS Configuration](#sms-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L93">property smsVerificationMessage</a>
</h3>

```typescript
public smsVerificationMessage: pulumi.Output<string | undefined>;
```


A string representing the SMS verification message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L97">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


A mapping of tags to assign to the User Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L101">property usernameAttributes</a>
</h3>

```typescript
public usernameAttributes: pulumi.Output<string[] | undefined>;
```


Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L105">property verificationMessageTemplate</a>
</h3>

```typescript
public verificationMessageTemplate: pulumi.Output<{ ... }>;
```


The [verification message templates](#verification-message-template) configuration.

<h2 class="pdoc-module-header" id="UserPoolClient">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L9">class UserPoolClient</a>
</h2>

Provides a Cognito User Pool Client resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L81">constructor</a>
</h3>

```typescript
new UserPoolClient(name: string, args: UserPoolClientArgs, opts?: pulumi.ResourceOptions)
```


Create a UserPoolClient resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new UserPoolClient(name: string, state?: UserPoolClientState, opts?: pulumi.ResourceOptions)
```


Create a UserPoolClient resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserPoolClientState): UserPoolClient
```


Get an existing UserPoolClient resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L25">property allowedOauthFlows</a>
</h3>

```typescript
public allowedOauthFlows: pulumi.Output<string[] | undefined>;
```


List of allowed OAuth flows (code, implicit, client_credentials).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L29">property allowedOauthFlowsUserPoolClient</a>
</h3>

```typescript
public allowedOauthFlowsUserPoolClient: pulumi.Output<boolean | undefined>;
```


Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L33">property allowedOauthScopes</a>
</h3>

```typescript
public allowedOauthScopes: pulumi.Output<string[] | undefined>;
```


List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L37">property callbackUrls</a>
</h3>

```typescript
public callbackUrls: pulumi.Output<string[] | undefined>;
```


List of allowed callback URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L41">property clientSecret</a>
</h3>

```typescript
public clientSecret: pulumi.Output<string>;
```


The client secret of the user pool client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L45">property defaultRedirectUri</a>
</h3>

```typescript
public defaultRedirectUri: pulumi.Output<string | undefined>;
```


The default redirect URI. Must be in the list of callback URLs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L49">property explicitAuthFlows</a>
</h3>

```typescript
public explicitAuthFlows: pulumi.Output<string[] | undefined>;
```


List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY, USER_PASSWORD_AUTH).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L53">property generateSecret</a>
</h3>

```typescript
public generateSecret: pulumi.Output<boolean | undefined>;
```


Should an application secret be generated. AWS JavaScript SDK requires this to be false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L57">property logoutUrls</a>
</h3>

```typescript
public logoutUrls: pulumi.Output<string[] | undefined>;
```


List of allowed logout URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L61">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the application client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L65">property readAttributes</a>
</h3>

```typescript
public readAttributes: pulumi.Output<string[] | undefined>;
```


List of user pool attributes the application client can read from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L69">property refreshTokenValidity</a>
</h3>

```typescript
public refreshTokenValidity: pulumi.Output<number | undefined>;
```


The time limit in days refresh tokens are valid for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L73">property supportedIdentityProviders</a>
</h3>

```typescript
public supportedIdentityProviders: pulumi.Output<string[] | undefined>;
```


List of provider names for the identity providers that are supported on this client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L77">property userPoolId</a>
</h3>

```typescript
public userPoolId: pulumi.Output<string>;
```


The user pool the client belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L81">property writeAttributes</a>
</h3>

```typescript
public writeAttributes: pulumi.Output<string[] | undefined>;
```


List of user pool attributes the application client can write to.

<h2 class="pdoc-module-header" id="UserPoolDomain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L9">class UserPoolDomain</a>
</h2>

Provides a Cognito User Pool Domain resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L45">constructor</a>
</h3>

```typescript
new UserPoolDomain(name: string, args: UserPoolDomainArgs, opts?: pulumi.ResourceOptions)
```


Create a UserPoolDomain resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new UserPoolDomain(name: string, state?: UserPoolDomainState, opts?: pulumi.ResourceOptions)
```


Create a UserPoolDomain resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserPoolDomainState): UserPoolDomain
```


Get an existing UserPoolDomain resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L25">property awsAccountId</a>
</h3>

```typescript
public awsAccountId: pulumi.Output<string>;
```


The AWS account ID for the user pool owner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L29">property cloudfrontDistributionArn</a>
</h3>

```typescript
public cloudfrontDistributionArn: pulumi.Output<string>;
```


The ARN of the CloudFront distribution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L33">property domain</a>
</h3>

```typescript
public domain: pulumi.Output<string>;
```


The domain string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L37">property s3Bucket</a>
</h3>

```typescript
public s3Bucket: pulumi.Output<string>;
```


The S3 bucket where the static files for this domain are stored.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L41">property userPoolId</a>
</h3>

```typescript
public userPoolId: pulumi.Output<string>;
```


The user pool ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L45">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


The app version.

<h2 class="pdoc-module-header" id="IdentityPoolArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L128">interface IdentityPoolArgs</a>
</h2>

The set of arguments for constructing a IdentityPool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L132">property allowUnauthenticatedIdentities</a>
</h3>

```typescript
allowUnauthenticatedIdentities?: pulumi.Input<boolean>;
```


Whether the identity pool supports unauthenticated logins or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L136">property cognitoIdentityProviders</a>
</h3>

```typescript
cognitoIdentityProviders?: pulumi.Input<{ ... }[]>;
```


An array of [Amazon Cognito Identity user pools](#cognito-identity-providers) and their client IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L141">property developerProviderName</a>
</h3>

```typescript
developerProviderName?: pulumi.Input<string>;
```


The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L145">property identityPoolName</a>
</h3>

```typescript
identityPoolName: pulumi.Input<string>;
```


The Cognito Identity Pool name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L149">property openidConnectProviderArns</a>
</h3>

```typescript
openidConnectProviderArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of OpendID Connect provider ARNs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L153">property samlProviderArns</a>
</h3>

```typescript
samlProviderArns?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L157">property supportedLoginProviders</a>
</h3>

```typescript
supportedLoginProviders?: pulumi.Input<{ ... }>;
```


Key-Value pairs mapping provider names to provider app IDs.

<h2 class="pdoc-module-header" id="IdentityPoolRoleAttachmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPoolRoleAttachment.ts#L89">interface IdentityPoolRoleAttachmentArgs</a>
</h2>

The set of arguments for constructing a IdentityPoolRoleAttachment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPoolRoleAttachment.ts#L93">property identityPoolId</a>
</h3>

```typescript
identityPoolId: pulumi.Input<string>;
```


An identity pool ID in the format REGION:GUID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPoolRoleAttachment.ts#L97">property roleMappings</a>
</h3>

```typescript
roleMappings?: pulumi.Input<{ ... }[]>;
```


A List of [Role Mapping](#role-mappings).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPoolRoleAttachment.ts#L101">property roles</a>
</h3>

```typescript
roles: pulumi.Input<{ ... }>;
```


The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.

<h2 class="pdoc-module-header" id="IdentityPoolRoleAttachmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPoolRoleAttachment.ts#L71">interface IdentityPoolRoleAttachmentState</a>
</h2>

Input properties used for looking up and filtering IdentityPoolRoleAttachment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPoolRoleAttachment.ts#L75">property identityPoolId</a>
</h3>

```typescript
identityPoolId?: pulumi.Input<string>;
```


An identity pool ID in the format REGION:GUID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPoolRoleAttachment.ts#L79">property roleMappings</a>
</h3>

```typescript
roleMappings?: pulumi.Input<{ ... }[]>;
```


A List of [Role Mapping](#role-mappings).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPoolRoleAttachment.ts#L83">property roles</a>
</h3>

```typescript
roles?: pulumi.Input<{ ... }>;
```


The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.

<h2 class="pdoc-module-header" id="IdentityPoolState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L93">interface IdentityPoolState</a>
</h2>

Input properties used for looking up and filtering IdentityPool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L97">property allowUnauthenticatedIdentities</a>
</h3>

```typescript
allowUnauthenticatedIdentities?: pulumi.Input<boolean>;
```


Whether the identity pool supports unauthenticated logins or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L101">property cognitoIdentityProviders</a>
</h3>

```typescript
cognitoIdentityProviders?: pulumi.Input<{ ... }[]>;
```


An array of [Amazon Cognito Identity user pools](#cognito-identity-providers) and their client IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L106">property developerProviderName</a>
</h3>

```typescript
developerProviderName?: pulumi.Input<string>;
```


The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L110">property identityPoolName</a>
</h3>

```typescript
identityPoolName?: pulumi.Input<string>;
```


The Cognito Identity Pool name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L114">property openidConnectProviderArns</a>
</h3>

```typescript
openidConnectProviderArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of OpendID Connect provider ARNs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L118">property samlProviderArns</a>
</h3>

```typescript
samlProviderArns?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/identityPool.ts#L122">property supportedLoginProviders</a>
</h3>

```typescript
supportedLoginProviders?: pulumi.Input<{ ... }>;
```


Key-Value pairs mapping provider names to provider app IDs.

<h2 class="pdoc-module-header" id="UserGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L106">interface UserGroupArgs</a>
</h2>

The set of arguments for constructing a UserGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L110">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L114">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L118">property precedence</a>
</h3>

```typescript
precedence?: pulumi.Input<number>;
```


The precedence of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L122">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of the IAM role to be associated with the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L126">property userPoolId</a>
</h3>

```typescript
userPoolId: pulumi.Input<string>;
```


The user pool ID.

<h2 class="pdoc-module-header" id="UserGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L80">interface UserGroupState</a>
</h2>

Input properties used for looking up and filtering UserGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L84">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L88">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L92">property precedence</a>
</h3>

```typescript
precedence?: pulumi.Input<number>;
```


The precedence of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L96">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of the IAM role to be associated with the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userGroup.ts#L100">property userPoolId</a>
</h3>

```typescript
userPoolId?: pulumi.Input<string>;
```


The user pool ID.

<h2 class="pdoc-module-header" id="UserPoolArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L263">interface UserPoolArgs</a>
</h2>

The set of arguments for constructing a UserPool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L267">property adminCreateUserConfig</a>
</h3>

```typescript
adminCreateUserConfig?: pulumi.Input<{ ... }>;
```


The configuration for [AdminCreateUser](#admin-create-user-config) requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L271">property aliasAttributes</a>
</h3>

```typescript
aliasAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L275">property autoVerifiedAttributes</a>
</h3>

```typescript
autoVerifiedAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


The attributes to be auto-verified. Possible values: email, phone_number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L279">property deviceConfiguration</a>
</h3>

```typescript
deviceConfiguration?: pulumi.Input<{ ... }>;
```


The configuration for the [user pool's device tracking](#device-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L283">property emailConfiguration</a>
</h3>

```typescript
emailConfiguration?: pulumi.Input<{ ... }>;
```


The [Email Configuration](#email-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L287">property emailVerificationMessage</a>
</h3>

```typescript
emailVerificationMessage?: pulumi.Input<string>;
```


A string representing the email verification message. Must contain the `{####}` placeholder. **NOTE:** - If `email_verification_message` and `verification_message_template.email_message` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L291">property emailVerificationSubject</a>
</h3>

```typescript
emailVerificationSubject?: pulumi.Input<string>;
```


A string representing the email verification subject. **NOTE:** - If `email_verification_subject` and `verification_message_template.email_subject` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L295">property lambdaConfig</a>
</h3>

```typescript
lambdaConfig?: pulumi.Input<{ ... }>;
```


A container for the AWS [Lambda triggers](#lambda-configuration) associated with the user pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L299">property mfaConfiguration</a>
</h3>

```typescript
mfaConfiguration?: pulumi.Input<string>;
```


Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L303">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the attribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L307">property passwordPolicy</a>
</h3>

```typescript
passwordPolicy?: pulumi.Input<{ ... }>;
```


A container for information about the [user pool password policy](#password-policy).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L311">property schemas</a>
</h3>

```typescript
schemas?: pulumi.Input<{ ... }[]>;
```


A container with the [schema attributes](#schema-attributes) of a user pool. Maximum of 50 attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L315">property smsAuthenticationMessage</a>
</h3>

```typescript
smsAuthenticationMessage?: pulumi.Input<string>;
```


A string representing the SMS authentication message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L319">property smsConfiguration</a>
</h3>

```typescript
smsConfiguration?: pulumi.Input<{ ... }>;
```


The [SMS Configuration](#sms-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L323">property smsVerificationMessage</a>
</h3>

```typescript
smsVerificationMessage?: pulumi.Input<string>;
```


A string representing the SMS verification message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L327">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the User Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L331">property usernameAttributes</a>
</h3>

```typescript
usernameAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L335">property verificationMessageTemplate</a>
</h3>

```typescript
verificationMessageTemplate?: pulumi.Input<{ ... }>;
```


The [verification message templates](#verification-message-template) configuration.

<h2 class="pdoc-module-header" id="UserPoolClientArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L206">interface UserPoolClientArgs</a>
</h2>

The set of arguments for constructing a UserPoolClient resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L210">property allowedOauthFlows</a>
</h3>

```typescript
allowedOauthFlows?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed OAuth flows (code, implicit, client_credentials).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L214">property allowedOauthFlowsUserPoolClient</a>
</h3>

```typescript
allowedOauthFlowsUserPoolClient?: pulumi.Input<boolean>;
```


Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L218">property allowedOauthScopes</a>
</h3>

```typescript
allowedOauthScopes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L222">property callbackUrls</a>
</h3>

```typescript
callbackUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed callback URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L226">property defaultRedirectUri</a>
</h3>

```typescript
defaultRedirectUri?: pulumi.Input<string>;
```


The default redirect URI. Must be in the list of callback URLs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L230">property explicitAuthFlows</a>
</h3>

```typescript
explicitAuthFlows?: pulumi.Input<pulumi.Input<string>[]>;
```


List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY, USER_PASSWORD_AUTH).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L234">property generateSecret</a>
</h3>

```typescript
generateSecret?: pulumi.Input<boolean>;
```


Should an application secret be generated. AWS JavaScript SDK requires this to be false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L238">property logoutUrls</a>
</h3>

```typescript
logoutUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed logout URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L242">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the application client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L246">property readAttributes</a>
</h3>

```typescript
readAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of user pool attributes the application client can read from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L250">property refreshTokenValidity</a>
</h3>

```typescript
refreshTokenValidity?: pulumi.Input<number>;
```


The time limit in days refresh tokens are valid for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L254">property supportedIdentityProviders</a>
</h3>

```typescript
supportedIdentityProviders?: pulumi.Input<pulumi.Input<string>[]>;
```


List of provider names for the identity providers that are supported on this client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L258">property userPoolId</a>
</h3>

```typescript
userPoolId: pulumi.Input<string>;
```


The user pool the client belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L262">property writeAttributes</a>
</h3>

```typescript
writeAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of user pool attributes the application client can write to.

<h2 class="pdoc-module-header" id="UserPoolClientState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L140">interface UserPoolClientState</a>
</h2>

Input properties used for looking up and filtering UserPoolClient resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L144">property allowedOauthFlows</a>
</h3>

```typescript
allowedOauthFlows?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed OAuth flows (code, implicit, client_credentials).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L148">property allowedOauthFlowsUserPoolClient</a>
</h3>

```typescript
allowedOauthFlowsUserPoolClient?: pulumi.Input<boolean>;
```


Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L152">property allowedOauthScopes</a>
</h3>

```typescript
allowedOauthScopes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L156">property callbackUrls</a>
</h3>

```typescript
callbackUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed callback URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L160">property clientSecret</a>
</h3>

```typescript
clientSecret?: pulumi.Input<string>;
```


The client secret of the user pool client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L164">property defaultRedirectUri</a>
</h3>

```typescript
defaultRedirectUri?: pulumi.Input<string>;
```


The default redirect URI. Must be in the list of callback URLs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L168">property explicitAuthFlows</a>
</h3>

```typescript
explicitAuthFlows?: pulumi.Input<pulumi.Input<string>[]>;
```


List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY, USER_PASSWORD_AUTH).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L172">property generateSecret</a>
</h3>

```typescript
generateSecret?: pulumi.Input<boolean>;
```


Should an application secret be generated. AWS JavaScript SDK requires this to be false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L176">property logoutUrls</a>
</h3>

```typescript
logoutUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed logout URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L180">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the application client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L184">property readAttributes</a>
</h3>

```typescript
readAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of user pool attributes the application client can read from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L188">property refreshTokenValidity</a>
</h3>

```typescript
refreshTokenValidity?: pulumi.Input<number>;
```


The time limit in days refresh tokens are valid for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L192">property supportedIdentityProviders</a>
</h3>

```typescript
supportedIdentityProviders?: pulumi.Input<pulumi.Input<string>[]>;
```


List of provider names for the identity providers that are supported on this client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L196">property userPoolId</a>
</h3>

```typescript
userPoolId?: pulumi.Input<string>;
```


The user pool the client belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolClient.ts#L200">property writeAttributes</a>
</h3>

```typescript
writeAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of user pool attributes the application client can write to.

<h2 class="pdoc-module-header" id="UserPoolDomainArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L119">interface UserPoolDomainArgs</a>
</h2>

The set of arguments for constructing a UserPoolDomain resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L123">property domain</a>
</h3>

```typescript
domain: pulumi.Input<string>;
```


The domain string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L127">property userPoolId</a>
</h3>

```typescript
userPoolId: pulumi.Input<string>;
```


The user pool ID.

<h2 class="pdoc-module-header" id="UserPoolDomainState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L89">interface UserPoolDomainState</a>
</h2>

Input properties used for looking up and filtering UserPoolDomain resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L93">property awsAccountId</a>
</h3>

```typescript
awsAccountId?: pulumi.Input<string>;
```


The AWS account ID for the user pool owner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L97">property cloudfrontDistributionArn</a>
</h3>

```typescript
cloudfrontDistributionArn?: pulumi.Input<string>;
```


The ARN of the CloudFront distribution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L101">property domain</a>
</h3>

```typescript
domain?: pulumi.Input<string>;
```


The domain string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L105">property s3Bucket</a>
</h3>

```typescript
s3Bucket?: pulumi.Input<string>;
```


The S3 bucket where the static files for this domain are stored.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L109">property userPoolId</a>
</h3>

```typescript
userPoolId?: pulumi.Input<string>;
```


The user pool ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPoolDomain.ts#L113">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The app version.

<h2 class="pdoc-module-header" id="UserPoolState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L173">interface UserPoolState</a>
</h2>

Input properties used for looking up and filtering UserPool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L177">property adminCreateUserConfig</a>
</h3>

```typescript
adminCreateUserConfig?: pulumi.Input<{ ... }>;
```


The configuration for [AdminCreateUser](#admin-create-user-config) requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L181">property aliasAttributes</a>
</h3>

```typescript
aliasAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L185">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the user pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L189">property autoVerifiedAttributes</a>
</h3>

```typescript
autoVerifiedAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


The attributes to be auto-verified. Possible values: email, phone_number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L193">property creationDate</a>
</h3>

```typescript
creationDate?: pulumi.Input<string>;
```


The date the user pool was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L197">property deviceConfiguration</a>
</h3>

```typescript
deviceConfiguration?: pulumi.Input<{ ... }>;
```


The configuration for the [user pool's device tracking](#device-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L201">property emailConfiguration</a>
</h3>

```typescript
emailConfiguration?: pulumi.Input<{ ... }>;
```


The [Email Configuration](#email-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L205">property emailVerificationMessage</a>
</h3>

```typescript
emailVerificationMessage?: pulumi.Input<string>;
```


A string representing the email verification message. Must contain the `{####}` placeholder. **NOTE:** - If `email_verification_message` and `verification_message_template.email_message` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L209">property emailVerificationSubject</a>
</h3>

```typescript
emailVerificationSubject?: pulumi.Input<string>;
```


A string representing the email verification subject. **NOTE:** - If `email_verification_subject` and `verification_message_template.email_subject` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L213">property lambdaConfig</a>
</h3>

```typescript
lambdaConfig?: pulumi.Input<{ ... }>;
```


A container for the AWS [Lambda triggers](#lambda-configuration) associated with the user pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L217">property lastModifiedDate</a>
</h3>

```typescript
lastModifiedDate?: pulumi.Input<string>;
```


The date the user pool was last modified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L221">property mfaConfiguration</a>
</h3>

```typescript
mfaConfiguration?: pulumi.Input<string>;
```


Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L225">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the attribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L229">property passwordPolicy</a>
</h3>

```typescript
passwordPolicy?: pulumi.Input<{ ... }>;
```


A container for information about the [user pool password policy](#password-policy).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L233">property schemas</a>
</h3>

```typescript
schemas?: pulumi.Input<{ ... }[]>;
```


A container with the [schema attributes](#schema-attributes) of a user pool. Maximum of 50 attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L237">property smsAuthenticationMessage</a>
</h3>

```typescript
smsAuthenticationMessage?: pulumi.Input<string>;
```


A string representing the SMS authentication message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L241">property smsConfiguration</a>
</h3>

```typescript
smsConfiguration?: pulumi.Input<{ ... }>;
```


The [SMS Configuration](#sms-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L245">property smsVerificationMessage</a>
</h3>

```typescript
smsVerificationMessage?: pulumi.Input<string>;
```


A string representing the SMS verification message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L249">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the User Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L253">property usernameAttributes</a>
</h3>

```typescript
usernameAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/cognito/userPool.ts#L257">property verificationMessageTemplate</a>
</h3>

```typescript
verificationMessageTemplate?: pulumi.Input<{ ... }>;
```


The [verification message templates](#verification-message-template) configuration.

