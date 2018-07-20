---
title: Module cognito
---

<a href="../index.html">@pulumi/aws</a> &gt; cognito

<h2 class="pdoc-module-header">Index</h2>

* <a href="#IdentityPool">class IdentityPool</a>
* <a href="#IdentityPoolRoleAttachment">class IdentityPoolRoleAttachment</a>
* <a href="#IdentityProvider">class IdentityProvider</a>
* <a href="#ResourceServer">class ResourceServer</a>
* <a href="#UserGroup">class UserGroup</a>
* <a href="#UserPool">class UserPool</a>
* <a href="#UserPoolClient">class UserPoolClient</a>
* <a href="#UserPoolDomain">class UserPoolDomain</a>
* <a href="#getUserPools">function getUserPools</a>
* <a href="#GetUserPoolsArgs">interface GetUserPoolsArgs</a>
* <a href="#GetUserPoolsResult">interface GetUserPoolsResult</a>
* <a href="#IdentityPoolArgs">interface IdentityPoolArgs</a>
* <a href="#IdentityPoolRoleAttachmentArgs">interface IdentityPoolRoleAttachmentArgs</a>
* <a href="#IdentityPoolRoleAttachmentState">interface IdentityPoolRoleAttachmentState</a>
* <a href="#IdentityPoolState">interface IdentityPoolState</a>
* <a href="#IdentityProviderArgs">interface IdentityProviderArgs</a>
* <a href="#IdentityProviderState">interface IdentityProviderState</a>
* <a href="#ResourceServerArgs">interface ResourceServerArgs</a>
* <a href="#ResourceServerState">interface ResourceServerState</a>
* <a href="#UserGroupArgs">interface UserGroupArgs</a>
* <a href="#UserGroupState">interface UserGroupState</a>
* <a href="#UserPoolArgs">interface UserPoolArgs</a>
* <a href="#UserPoolClientArgs">interface UserPoolClientArgs</a>
* <a href="#UserPoolClientState">interface UserPoolClientState</a>
* <a href="#UserPoolDomainArgs">interface UserPoolDomainArgs</a>
* <a href="#UserPoolDomainState">interface UserPoolDomainState</a>
* <a href="#UserPoolState">interface UserPoolState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/getUserPools.ts">cognito/getUserPools.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts">cognito/identityPool.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts">cognito/identityPoolRoleAttachment.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts">cognito/identityProvider.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts">cognito/resourceServer.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts">cognito/userGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts">cognito/userPool.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts">cognito/userPoolClient.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts">cognito/userPoolDomain.ts</a> 


<h2 class="pdoc-module-header" id="IdentityPool">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L9">class IdentityPool</a>
</h2>

Provides an AWS Cognito Identity Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L54">constructor</a>
</h3>

```typescript
new IdentityPool(name: string, args: IdentityPoolArgs, opts?: pulumi.ResourceOptions)
```


Create a IdentityPool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IdentityPoolState): IdentityPool
```


Get an existing IdentityPool resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L25">property allowUnauthenticatedIdentities</a>
</h3>

```typescript
public allowUnauthenticatedIdentities: pulumi.Output<boolean | undefined>;
```


Whether the identity pool supports unauthenticated logins or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L29">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the identity pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L33">property cognitoIdentityProviders</a>
</h3>

```typescript
public cognitoIdentityProviders: pulumi.Output<{ ... }[] | undefined>;
```


An array of [Amazon Cognito Identity user pools](#cognito-identity-providers) and their client IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L38">property developerProviderName</a>
</h3>

```typescript
public developerProviderName: pulumi.Output<string | undefined>;
```


The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L42">property identityPoolName</a>
</h3>

```typescript
public identityPoolName: pulumi.Output<string>;
```


The Cognito Identity Pool name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L46">property openidConnectProviderArns</a>
</h3>

```typescript
public openidConnectProviderArns: pulumi.Output<string[] | undefined>;
```


A list of OpendID Connect provider ARNs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L50">property samlProviderArns</a>
</h3>

```typescript
public samlProviderArns: pulumi.Output<string[] | undefined>;
```


An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L54">property supportedLoginProviders</a>
</h3>

```typescript
public supportedLoginProviders: pulumi.Output<{ ... } | undefined>;
```


Key-Value pairs mapping provider names to provider app IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IdentityPoolRoleAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L9">class IdentityPoolRoleAttachment</a>
</h2>

Provides an AWS Cognito Identity Pool Roles Attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L33">constructor</a>
</h3>

```typescript
new IdentityPoolRoleAttachment(name: string, args: IdentityPoolRoleAttachmentArgs, opts?: pulumi.ResourceOptions)
```


Create a IdentityPoolRoleAttachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IdentityPoolRoleAttachmentState): IdentityPoolRoleAttachment
```


Get an existing IdentityPoolRoleAttachment resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L25">property identityPoolId</a>
</h3>

```typescript
public identityPoolId: pulumi.Output<string>;
```


An identity pool ID in the format REGION:GUID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L29">property roleMappings</a>
</h3>

```typescript
public roleMappings: pulumi.Output<{ ... }[] | undefined>;
```


A List of [Role Mapping](#role-mappings).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L33">property roles</a>
</h3>

```typescript
public roles: pulumi.Output<{ ... }>;
```


The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IdentityProvider">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L9">class IdentityProvider</a>
</h2>

Provides a Cognito User Identity Provider resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L45">constructor</a>
</h3>

```typescript
new IdentityProvider(name: string, args: IdentityProviderArgs, opts?: pulumi.ResourceOptions)
```


Create a IdentityProvider resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IdentityProviderState): IdentityProvider
```


Get an existing IdentityProvider resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L25">property attributeMapping</a>
</h3>

```typescript
public attributeMapping: pulumi.Output<{ ... } | undefined>;
```


The map of attribute mapping of user pool attributes. [AttributeMapping in AWS API documentation](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L29">property idpIdentifiers</a>
</h3>

```typescript
public idpIdentifiers: pulumi.Output<string[] | undefined>;
```


The list of identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L33">property providerDetails</a>
</h3>

```typescript
public providerDetails: pulumi.Output<{ ... }>;
```


The map of identity details, such as access token

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L37">property providerName</a>
</h3>

```typescript
public providerName: pulumi.Output<string>;
```


The provider name

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L41">property providerType</a>
</h3>

```typescript
public providerType: pulumi.Output<string>;
```


The provider type.  [See AWS API for valid values](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L45">property userPoolId</a>
</h3>

```typescript
public userPoolId: pulumi.Output<string>;
```


The user pool id

<h2 class="pdoc-module-header" id="ResourceServer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L9">class ResourceServer</a>
</h2>

Provides a Cognito Resource Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L38">constructor</a>
</h3>

```typescript
new ResourceServer(name: string, args: ResourceServerArgs, opts?: pulumi.ResourceOptions)
```


Create a ResourceServer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ResourceServerState): ResourceServer
```


Get an existing ResourceServer resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L25">property identifier</a>
</h3>

```typescript
public identifier: pulumi.Output<string>;
```


An identifier for the resource server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A name for the resource server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L37">property scopeIdentifiers</a>
</h3>

```typescript
public scopeIdentifiers: pulumi.Output<string[]>;
```


A list of all scopes configured for this resource server in the format identifier/scope_name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L33">property scopes</a>
</h3>

```typescript
public scopes: pulumi.Output<{ ... }[] | undefined>;
```


A list of [Authorization Scope](#authorization_scope).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L38">property userPoolId</a>
</h3>

```typescript
public userPoolId: pulumi.Output<string>;
```

<h2 class="pdoc-module-header" id="UserGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L9">class UserGroup</a>
</h2>

Provides a Cognito User Group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L41">constructor</a>
</h3>

```typescript
new UserGroup(name: string, args: UserGroupArgs, opts?: pulumi.ResourceOptions)
```


Create a UserGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserGroupState): UserGroup
```


Get an existing UserGroup resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L25">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L33">property precedence</a>
</h3>

```typescript
public precedence: pulumi.Output<number | undefined>;
```


The precedence of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L37">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string | undefined>;
```


The ARN of the IAM role to be associated with the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L41">property userPoolId</a>
</h3>

```typescript
public userPoolId: pulumi.Output<string>;
```


The user pool ID.

<h2 class="pdoc-module-header" id="UserPool">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L9">class UserPool</a>
</h2>

Provides a Cognito User Pool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L109">constructor</a>
</h3>

```typescript
new UserPool(name: string, args?: UserPoolArgs, opts?: pulumi.ResourceOptions)
```


Create a UserPool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserPoolState): UserPool
```


Get an existing UserPool resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L25">property adminCreateUserConfig</a>
</h3>

```typescript
public adminCreateUserConfig: pulumi.Output<{ ... }>;
```


The configuration for [AdminCreateUser](#admin-create-user-config) requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L29">property aliasAttributes</a>
</h3>

```typescript
public aliasAttributes: pulumi.Output<string[] | undefined>;
```


Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L33">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the user pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L37">property autoVerifiedAttributes</a>
</h3>

```typescript
public autoVerifiedAttributes: pulumi.Output<string[] | undefined>;
```


The attributes to be auto-verified. Possible values: email, phone_number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L41">property creationDate</a>
</h3>

```typescript
public creationDate: pulumi.Output<string>;
```


The date the user pool was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L45">property deviceConfiguration</a>
</h3>

```typescript
public deviceConfiguration: pulumi.Output<{ ... } | undefined>;
```


The configuration for the [user pool's device tracking](#device-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L49">property emailConfiguration</a>
</h3>

```typescript
public emailConfiguration: pulumi.Output<{ ... } | undefined>;
```


The [Email Configuration](#email-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L53">property emailVerificationMessage</a>
</h3>

```typescript
public emailVerificationMessage: pulumi.Output<string>;
```


A string representing the email verification message. Must contain the `{####}` placeholder. **NOTE:** - If `email_verification_message` and `verification_message_template.email_message` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L57">property emailVerificationSubject</a>
</h3>

```typescript
public emailVerificationSubject: pulumi.Output<string>;
```


A string representing the email verification subject. **NOTE:** - If `email_verification_subject` and `verification_message_template.email_subject` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L61">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L65">property lambdaConfig</a>
</h3>

```typescript
public lambdaConfig: pulumi.Output<{ ... }>;
```


A container for the AWS [Lambda triggers](#lambda-configuration) associated with the user pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L69">property lastModifiedDate</a>
</h3>

```typescript
public lastModifiedDate: pulumi.Output<string>;
```


The date the user pool was last modified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L73">property mfaConfiguration</a>
</h3>

```typescript
public mfaConfiguration: pulumi.Output<string | undefined>;
```


Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L77">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the attribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L81">property passwordPolicy</a>
</h3>

```typescript
public passwordPolicy: pulumi.Output<{ ... }>;
```


A container for information about the [user pool password policy](#password-policy).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L85">property schemas</a>
</h3>

```typescript
public schemas: pulumi.Output<{ ... }[] | undefined>;
```


A container with the [schema attributes](#schema-attributes) of a user pool. Maximum of 50 attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L89">property smsAuthenticationMessage</a>
</h3>

```typescript
public smsAuthenticationMessage: pulumi.Output<string | undefined>;
```


A string representing the SMS authentication message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L93">property smsConfiguration</a>
</h3>

```typescript
public smsConfiguration: pulumi.Output<{ ... } | undefined>;
```


The [SMS Configuration](#sms-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L97">property smsVerificationMessage</a>
</h3>

```typescript
public smsVerificationMessage: pulumi.Output<string | undefined>;
```


A string representing the SMS verification message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L101">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


A mapping of tags to assign to the User Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L105">property usernameAttributes</a>
</h3>

```typescript
public usernameAttributes: pulumi.Output<string[] | undefined>;
```


Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L109">property verificationMessageTemplate</a>
</h3>

```typescript
public verificationMessageTemplate: pulumi.Output<{ ... }>;
```


The [verification message templates](#verification-message-template) configuration.

<h2 class="pdoc-module-header" id="UserPoolClient">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L9">class UserPoolClient</a>
</h2>

Provides a Cognito User Pool Client resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L81">constructor</a>
</h3>

```typescript
new UserPoolClient(name: string, args: UserPoolClientArgs, opts?: pulumi.ResourceOptions)
```


Create a UserPoolClient resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserPoolClientState): UserPoolClient
```


Get an existing UserPoolClient resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L25">property allowedOauthFlows</a>
</h3>

```typescript
public allowedOauthFlows: pulumi.Output<string[] | undefined>;
```


List of allowed OAuth flows (code, implicit, client_credentials).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L29">property allowedOauthFlowsUserPoolClient</a>
</h3>

```typescript
public allowedOauthFlowsUserPoolClient: pulumi.Output<boolean | undefined>;
```


Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L33">property allowedOauthScopes</a>
</h3>

```typescript
public allowedOauthScopes: pulumi.Output<string[] | undefined>;
```


List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L37">property callbackUrls</a>
</h3>

```typescript
public callbackUrls: pulumi.Output<string[] | undefined>;
```


List of allowed callback URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L41">property clientSecret</a>
</h3>

```typescript
public clientSecret: pulumi.Output<string>;
```


The client secret of the user pool client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L45">property defaultRedirectUri</a>
</h3>

```typescript
public defaultRedirectUri: pulumi.Output<string | undefined>;
```


The default redirect URI. Must be in the list of callback URLs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L49">property explicitAuthFlows</a>
</h3>

```typescript
public explicitAuthFlows: pulumi.Output<string[] | undefined>;
```


List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY, USER_PASSWORD_AUTH).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L53">property generateSecret</a>
</h3>

```typescript
public generateSecret: pulumi.Output<boolean | undefined>;
```


Should an application secret be generated. AWS JavaScript SDK requires this to be false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L57">property logoutUrls</a>
</h3>

```typescript
public logoutUrls: pulumi.Output<string[] | undefined>;
```


List of allowed logout URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L61">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the application client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L65">property readAttributes</a>
</h3>

```typescript
public readAttributes: pulumi.Output<string[] | undefined>;
```


List of user pool attributes the application client can read from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L69">property refreshTokenValidity</a>
</h3>

```typescript
public refreshTokenValidity: pulumi.Output<number | undefined>;
```


The time limit in days refresh tokens are valid for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L73">property supportedIdentityProviders</a>
</h3>

```typescript
public supportedIdentityProviders: pulumi.Output<string[] | undefined>;
```


List of provider names for the identity providers that are supported on this client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L77">property userPoolId</a>
</h3>

```typescript
public userPoolId: pulumi.Output<string>;
```


The user pool the client belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L81">property writeAttributes</a>
</h3>

```typescript
public writeAttributes: pulumi.Output<string[] | undefined>;
```


List of user pool attributes the application client can write to.

<h2 class="pdoc-module-header" id="UserPoolDomain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L9">class UserPoolDomain</a>
</h2>

Provides a Cognito User Pool Domain resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L45">constructor</a>
</h3>

```typescript
new UserPoolDomain(name: string, args: UserPoolDomainArgs, opts?: pulumi.ResourceOptions)
```


Create a UserPoolDomain resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserPoolDomainState): UserPoolDomain
```


Get an existing UserPoolDomain resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L25">property awsAccountId</a>
</h3>

```typescript
public awsAccountId: pulumi.Output<string>;
```


The AWS account ID for the user pool owner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L29">property cloudfrontDistributionArn</a>
</h3>

```typescript
public cloudfrontDistributionArn: pulumi.Output<string>;
```


The ARN of the CloudFront distribution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L33">property domain</a>
</h3>

```typescript
public domain: pulumi.Output<string>;
```


The domain string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L37">property s3Bucket</a>
</h3>

```typescript
public s3Bucket: pulumi.Output<string>;
```


The S3 bucket where the static files for this domain are stored.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L41">property userPoolId</a>
</h3>

```typescript
public userPoolId: pulumi.Output<string>;
```


The user pool ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L45">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


The app version.

<h2 class="pdoc-module-header" id="getUserPools">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/getUserPools.ts#L9">function getUserPools</a>
</h2>

```typescript
getUserPools(args: GetUserPoolsArgs): Promise<GetUserPoolsResult>
```


Use this data source to get a list of cognito user pools.

<h2 class="pdoc-module-header" id="GetUserPoolsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/getUserPools.ts#L18">interface GetUserPoolsArgs</a>
</h2>

A collection of arguments for invoking getUserPools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/getUserPools.ts#L22">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


Name of the cognito user pools. Name is not a unique attribute for cognito user pool, so multiple pools might be returned with given name.

<h2 class="pdoc-module-header" id="GetUserPoolsResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/getUserPools.ts#L28">interface GetUserPoolsResult</a>
</h2>

A collection of values returned by getUserPools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/getUserPools.ts#L29">property arns</a>
</h3>

```typescript
arns: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/getUserPools.ts#L37">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/getUserPools.ts#L33">property ids</a>
</h3>

```typescript
ids: string[];
```


The list of cognito user pool ids.

<h2 class="pdoc-module-header" id="IdentityPoolArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L136">interface IdentityPoolArgs</a>
</h2>

The set of arguments for constructing a IdentityPool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L140">property allowUnauthenticatedIdentities</a>
</h3>

```typescript
allowUnauthenticatedIdentities?: pulumi.Input<boolean>;
```


Whether the identity pool supports unauthenticated logins or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L144">property cognitoIdentityProviders</a>
</h3>

```typescript
cognitoIdentityProviders?: pulumi.Input<{ ... }[]>;
```


An array of [Amazon Cognito Identity user pools](#cognito-identity-providers) and their client IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L149">property developerProviderName</a>
</h3>

```typescript
developerProviderName?: pulumi.Input<string>;
```


The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L153">property identityPoolName</a>
</h3>

```typescript
identityPoolName: pulumi.Input<string>;
```


The Cognito Identity Pool name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L157">property openidConnectProviderArns</a>
</h3>

```typescript
openidConnectProviderArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of OpendID Connect provider ARNs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L161">property samlProviderArns</a>
</h3>

```typescript
samlProviderArns?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L165">property supportedLoginProviders</a>
</h3>

```typescript
supportedLoginProviders?: pulumi.Input<{ ... }>;
```


Key-Value pairs mapping provider names to provider app IDs.

<h2 class="pdoc-module-header" id="IdentityPoolRoleAttachmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L87">interface IdentityPoolRoleAttachmentArgs</a>
</h2>

The set of arguments for constructing a IdentityPoolRoleAttachment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L91">property identityPoolId</a>
</h3>

```typescript
identityPoolId: pulumi.Input<string>;
```


An identity pool ID in the format REGION:GUID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L95">property roleMappings</a>
</h3>

```typescript
roleMappings?: pulumi.Input<{ ... }[]>;
```


A List of [Role Mapping](#role-mappings).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L99">property roles</a>
</h3>

```typescript
roles: pulumi.Input<{ ... }>;
```


The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.

<h2 class="pdoc-module-header" id="IdentityPoolRoleAttachmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L69">interface IdentityPoolRoleAttachmentState</a>
</h2>

Input properties used for looking up and filtering IdentityPoolRoleAttachment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L73">property identityPoolId</a>
</h3>

```typescript
identityPoolId?: pulumi.Input<string>;
```


An identity pool ID in the format REGION:GUID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L77">property roleMappings</a>
</h3>

```typescript
roleMappings?: pulumi.Input<{ ... }[]>;
```


A List of [Role Mapping](#role-mappings).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L81">property roles</a>
</h3>

```typescript
roles?: pulumi.Input<{ ... }>;
```


The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.

<h2 class="pdoc-module-header" id="IdentityPoolState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L97">interface IdentityPoolState</a>
</h2>

Input properties used for looking up and filtering IdentityPool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L101">property allowUnauthenticatedIdentities</a>
</h3>

```typescript
allowUnauthenticatedIdentities?: pulumi.Input<boolean>;
```


Whether the identity pool supports unauthenticated logins or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L105">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the identity pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L109">property cognitoIdentityProviders</a>
</h3>

```typescript
cognitoIdentityProviders?: pulumi.Input<{ ... }[]>;
```


An array of [Amazon Cognito Identity user pools](#cognito-identity-providers) and their client IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L114">property developerProviderName</a>
</h3>

```typescript
developerProviderName?: pulumi.Input<string>;
```


The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L118">property identityPoolName</a>
</h3>

```typescript
identityPoolName?: pulumi.Input<string>;
```


The Cognito Identity Pool name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L122">property openidConnectProviderArns</a>
</h3>

```typescript
openidConnectProviderArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of OpendID Connect provider ARNs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L126">property samlProviderArns</a>
</h3>

```typescript
samlProviderArns?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L130">property supportedLoginProviders</a>
</h3>

```typescript
supportedLoginProviders?: pulumi.Input<{ ... }>;
```


Key-Value pairs mapping provider names to provider app IDs.

<h2 class="pdoc-module-header" id="IdentityProviderArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L123">interface IdentityProviderArgs</a>
</h2>

The set of arguments for constructing a IdentityProvider resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L127">property attributeMapping</a>
</h3>

```typescript
attributeMapping?: pulumi.Input<{ ... }>;
```


The map of attribute mapping of user pool attributes. [AttributeMapping in AWS API documentation](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L131">property idpIdentifiers</a>
</h3>

```typescript
idpIdentifiers?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L135">property providerDetails</a>
</h3>

```typescript
providerDetails: pulumi.Input<{ ... }>;
```


The map of identity details, such as access token

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L139">property providerName</a>
</h3>

```typescript
providerName: pulumi.Input<string>;
```


The provider name

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L143">property providerType</a>
</h3>

```typescript
providerType: pulumi.Input<string>;
```


The provider type.  [See AWS API for valid values](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L147">property userPoolId</a>
</h3>

```typescript
userPoolId: pulumi.Input<string>;
```


The user pool id

<h2 class="pdoc-module-header" id="IdentityProviderState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L93">interface IdentityProviderState</a>
</h2>

Input properties used for looking up and filtering IdentityProvider resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L97">property attributeMapping</a>
</h3>

```typescript
attributeMapping?: pulumi.Input<{ ... }>;
```


The map of attribute mapping of user pool attributes. [AttributeMapping in AWS API documentation](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L101">property idpIdentifiers</a>
</h3>

```typescript
idpIdentifiers?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L105">property providerDetails</a>
</h3>

```typescript
providerDetails?: pulumi.Input<{ ... }>;
```


The map of identity details, such as access token

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L109">property providerName</a>
</h3>

```typescript
providerName?: pulumi.Input<string>;
```


The provider name

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L113">property providerType</a>
</h3>

```typescript
providerType?: pulumi.Input<string>;
```


The provider type.  [See AWS API for valid values](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L117">property userPoolId</a>
</h3>

```typescript
userPoolId?: pulumi.Input<string>;
```


The user pool id

<h2 class="pdoc-module-header" id="ResourceServerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L101">interface ResourceServerArgs</a>
</h2>

The set of arguments for constructing a ResourceServer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L105">property identifier</a>
</h3>

```typescript
identifier: pulumi.Input<string>;
```


An identifier for the resource server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L109">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the resource server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L113">property scopes</a>
</h3>

```typescript
scopes?: pulumi.Input<{ ... }[]>;
```


A list of [Authorization Scope](#authorization_scope).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L114">property userPoolId</a>
</h3>

```typescript
userPoolId: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="ResourceServerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L78">interface ResourceServerState</a>
</h2>

Input properties used for looking up and filtering ResourceServer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L82">property identifier</a>
</h3>

```typescript
identifier?: pulumi.Input<string>;
```


An identifier for the resource server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L86">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the resource server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L94">property scopeIdentifiers</a>
</h3>

```typescript
scopeIdentifiers?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of all scopes configured for this resource server in the format identifier/scope_name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L90">property scopes</a>
</h3>

```typescript
scopes?: pulumi.Input<{ ... }[]>;
```


A list of [Authorization Scope](#authorization_scope).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L95">property userPoolId</a>
</h3>

```typescript
userPoolId?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="UserGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L104">interface UserGroupArgs</a>
</h2>

The set of arguments for constructing a UserGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L108">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L112">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L116">property precedence</a>
</h3>

```typescript
precedence?: pulumi.Input<number>;
```


The precedence of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L120">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of the IAM role to be associated with the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L124">property userPoolId</a>
</h3>

```typescript
userPoolId: pulumi.Input<string>;
```


The user pool ID.

<h2 class="pdoc-module-header" id="UserGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L78">interface UserGroupState</a>
</h2>

Input properties used for looking up and filtering UserGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L82">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L86">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L90">property precedence</a>
</h3>

```typescript
precedence?: pulumi.Input<number>;
```


The precedence of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L94">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of the IAM role to be associated with the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L98">property userPoolId</a>
</h3>

```typescript
userPoolId?: pulumi.Input<string>;
```


The user pool ID.

<h2 class="pdoc-module-header" id="UserPoolArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L271">interface UserPoolArgs</a>
</h2>

The set of arguments for constructing a UserPool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L275">property adminCreateUserConfig</a>
</h3>

```typescript
adminCreateUserConfig?: pulumi.Input<{ ... }>;
```


The configuration for [AdminCreateUser](#admin-create-user-config) requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L279">property aliasAttributes</a>
</h3>

```typescript
aliasAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L283">property autoVerifiedAttributes</a>
</h3>

```typescript
autoVerifiedAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


The attributes to be auto-verified. Possible values: email, phone_number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L287">property deviceConfiguration</a>
</h3>

```typescript
deviceConfiguration?: pulumi.Input<{ ... }>;
```


The configuration for the [user pool's device tracking](#device-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L291">property emailConfiguration</a>
</h3>

```typescript
emailConfiguration?: pulumi.Input<{ ... }>;
```


The [Email Configuration](#email-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L295">property emailVerificationMessage</a>
</h3>

```typescript
emailVerificationMessage?: pulumi.Input<string>;
```


A string representing the email verification message. Must contain the `{####}` placeholder. **NOTE:** - If `email_verification_message` and `verification_message_template.email_message` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L299">property emailVerificationSubject</a>
</h3>

```typescript
emailVerificationSubject?: pulumi.Input<string>;
```


A string representing the email verification subject. **NOTE:** - If `email_verification_subject` and `verification_message_template.email_subject` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L303">property lambdaConfig</a>
</h3>

```typescript
lambdaConfig?: pulumi.Input<{ ... }>;
```


A container for the AWS [Lambda triggers](#lambda-configuration) associated with the user pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L307">property mfaConfiguration</a>
</h3>

```typescript
mfaConfiguration?: pulumi.Input<string>;
```


Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L311">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the attribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L315">property passwordPolicy</a>
</h3>

```typescript
passwordPolicy?: pulumi.Input<{ ... }>;
```


A container for information about the [user pool password policy](#password-policy).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L319">property schemas</a>
</h3>

```typescript
schemas?: pulumi.Input<{ ... }[]>;
```


A container with the [schema attributes](#schema-attributes) of a user pool. Maximum of 50 attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L323">property smsAuthenticationMessage</a>
</h3>

```typescript
smsAuthenticationMessage?: pulumi.Input<string>;
```


A string representing the SMS authentication message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L327">property smsConfiguration</a>
</h3>

```typescript
smsConfiguration?: pulumi.Input<{ ... }>;
```


The [SMS Configuration](#sms-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L331">property smsVerificationMessage</a>
</h3>

```typescript
smsVerificationMessage?: pulumi.Input<string>;
```


A string representing the SMS verification message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L335">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the User Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L339">property usernameAttributes</a>
</h3>

```typescript
usernameAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L343">property verificationMessageTemplate</a>
</h3>

```typescript
verificationMessageTemplate?: pulumi.Input<{ ... }>;
```


The [verification message templates](#verification-message-template) configuration.

<h2 class="pdoc-module-header" id="UserPoolClientArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L204">interface UserPoolClientArgs</a>
</h2>

The set of arguments for constructing a UserPoolClient resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L208">property allowedOauthFlows</a>
</h3>

```typescript
allowedOauthFlows?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed OAuth flows (code, implicit, client_credentials).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L212">property allowedOauthFlowsUserPoolClient</a>
</h3>

```typescript
allowedOauthFlowsUserPoolClient?: pulumi.Input<boolean>;
```


Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L216">property allowedOauthScopes</a>
</h3>

```typescript
allowedOauthScopes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L220">property callbackUrls</a>
</h3>

```typescript
callbackUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed callback URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L224">property defaultRedirectUri</a>
</h3>

```typescript
defaultRedirectUri?: pulumi.Input<string>;
```


The default redirect URI. Must be in the list of callback URLs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L228">property explicitAuthFlows</a>
</h3>

```typescript
explicitAuthFlows?: pulumi.Input<pulumi.Input<string>[]>;
```


List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY, USER_PASSWORD_AUTH).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L232">property generateSecret</a>
</h3>

```typescript
generateSecret?: pulumi.Input<boolean>;
```


Should an application secret be generated. AWS JavaScript SDK requires this to be false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L236">property logoutUrls</a>
</h3>

```typescript
logoutUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed logout URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L240">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the application client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L244">property readAttributes</a>
</h3>

```typescript
readAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of user pool attributes the application client can read from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L248">property refreshTokenValidity</a>
</h3>

```typescript
refreshTokenValidity?: pulumi.Input<number>;
```


The time limit in days refresh tokens are valid for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L252">property supportedIdentityProviders</a>
</h3>

```typescript
supportedIdentityProviders?: pulumi.Input<pulumi.Input<string>[]>;
```


List of provider names for the identity providers that are supported on this client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L256">property userPoolId</a>
</h3>

```typescript
userPoolId: pulumi.Input<string>;
```


The user pool the client belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L260">property writeAttributes</a>
</h3>

```typescript
writeAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of user pool attributes the application client can write to.

<h2 class="pdoc-module-header" id="UserPoolClientState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L138">interface UserPoolClientState</a>
</h2>

Input properties used for looking up and filtering UserPoolClient resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L142">property allowedOauthFlows</a>
</h3>

```typescript
allowedOauthFlows?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed OAuth flows (code, implicit, client_credentials).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L146">property allowedOauthFlowsUserPoolClient</a>
</h3>

```typescript
allowedOauthFlowsUserPoolClient?: pulumi.Input<boolean>;
```


Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L150">property allowedOauthScopes</a>
</h3>

```typescript
allowedOauthScopes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L154">property callbackUrls</a>
</h3>

```typescript
callbackUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed callback URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L158">property clientSecret</a>
</h3>

```typescript
clientSecret?: pulumi.Input<string>;
```


The client secret of the user pool client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L162">property defaultRedirectUri</a>
</h3>

```typescript
defaultRedirectUri?: pulumi.Input<string>;
```


The default redirect URI. Must be in the list of callback URLs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L166">property explicitAuthFlows</a>
</h3>

```typescript
explicitAuthFlows?: pulumi.Input<pulumi.Input<string>[]>;
```


List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY, USER_PASSWORD_AUTH).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L170">property generateSecret</a>
</h3>

```typescript
generateSecret?: pulumi.Input<boolean>;
```


Should an application secret be generated. AWS JavaScript SDK requires this to be false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L174">property logoutUrls</a>
</h3>

```typescript
logoutUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed logout URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L178">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the application client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L182">property readAttributes</a>
</h3>

```typescript
readAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of user pool attributes the application client can read from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L186">property refreshTokenValidity</a>
</h3>

```typescript
refreshTokenValidity?: pulumi.Input<number>;
```


The time limit in days refresh tokens are valid for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L190">property supportedIdentityProviders</a>
</h3>

```typescript
supportedIdentityProviders?: pulumi.Input<pulumi.Input<string>[]>;
```


List of provider names for the identity providers that are supported on this client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L194">property userPoolId</a>
</h3>

```typescript
userPoolId?: pulumi.Input<string>;
```


The user pool the client belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L198">property writeAttributes</a>
</h3>

```typescript
writeAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of user pool attributes the application client can write to.

<h2 class="pdoc-module-header" id="UserPoolDomainArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L117">interface UserPoolDomainArgs</a>
</h2>

The set of arguments for constructing a UserPoolDomain resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L121">property domain</a>
</h3>

```typescript
domain: pulumi.Input<string>;
```


The domain string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L125">property userPoolId</a>
</h3>

```typescript
userPoolId: pulumi.Input<string>;
```


The user pool ID.

<h2 class="pdoc-module-header" id="UserPoolDomainState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L87">interface UserPoolDomainState</a>
</h2>

Input properties used for looking up and filtering UserPoolDomain resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L91">property awsAccountId</a>
</h3>

```typescript
awsAccountId?: pulumi.Input<string>;
```


The AWS account ID for the user pool owner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L95">property cloudfrontDistributionArn</a>
</h3>

```typescript
cloudfrontDistributionArn?: pulumi.Input<string>;
```


The ARN of the CloudFront distribution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L99">property domain</a>
</h3>

```typescript
domain?: pulumi.Input<string>;
```


The domain string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L103">property s3Bucket</a>
</h3>

```typescript
s3Bucket?: pulumi.Input<string>;
```


The S3 bucket where the static files for this domain are stored.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L107">property userPoolId</a>
</h3>

```typescript
userPoolId?: pulumi.Input<string>;
```


The user pool ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L111">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The app version.

<h2 class="pdoc-module-header" id="UserPoolState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L177">interface UserPoolState</a>
</h2>

Input properties used for looking up and filtering UserPool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L181">property adminCreateUserConfig</a>
</h3>

```typescript
adminCreateUserConfig?: pulumi.Input<{ ... }>;
```


The configuration for [AdminCreateUser](#admin-create-user-config) requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L185">property aliasAttributes</a>
</h3>

```typescript
aliasAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L189">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the user pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L193">property autoVerifiedAttributes</a>
</h3>

```typescript
autoVerifiedAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


The attributes to be auto-verified. Possible values: email, phone_number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L197">property creationDate</a>
</h3>

```typescript
creationDate?: pulumi.Input<string>;
```


The date the user pool was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L201">property deviceConfiguration</a>
</h3>

```typescript
deviceConfiguration?: pulumi.Input<{ ... }>;
```


The configuration for the [user pool's device tracking](#device-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L205">property emailConfiguration</a>
</h3>

```typescript
emailConfiguration?: pulumi.Input<{ ... }>;
```


The [Email Configuration](#email-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L209">property emailVerificationMessage</a>
</h3>

```typescript
emailVerificationMessage?: pulumi.Input<string>;
```


A string representing the email verification message. Must contain the `{####}` placeholder. **NOTE:** - If `email_verification_message` and `verification_message_template.email_message` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L213">property emailVerificationSubject</a>
</h3>

```typescript
emailVerificationSubject?: pulumi.Input<string>;
```


A string representing the email verification subject. **NOTE:** - If `email_verification_subject` and `verification_message_template.email_subject` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L217">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L221">property lambdaConfig</a>
</h3>

```typescript
lambdaConfig?: pulumi.Input<{ ... }>;
```


A container for the AWS [Lambda triggers](#lambda-configuration) associated with the user pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L225">property lastModifiedDate</a>
</h3>

```typescript
lastModifiedDate?: pulumi.Input<string>;
```


The date the user pool was last modified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L229">property mfaConfiguration</a>
</h3>

```typescript
mfaConfiguration?: pulumi.Input<string>;
```


Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L233">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the attribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L237">property passwordPolicy</a>
</h3>

```typescript
passwordPolicy?: pulumi.Input<{ ... }>;
```


A container for information about the [user pool password policy](#password-policy).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L241">property schemas</a>
</h3>

```typescript
schemas?: pulumi.Input<{ ... }[]>;
```


A container with the [schema attributes](#schema-attributes) of a user pool. Maximum of 50 attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L245">property smsAuthenticationMessage</a>
</h3>

```typescript
smsAuthenticationMessage?: pulumi.Input<string>;
```


A string representing the SMS authentication message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L249">property smsConfiguration</a>
</h3>

```typescript
smsConfiguration?: pulumi.Input<{ ... }>;
```


The [SMS Configuration](#sms-configuration).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L253">property smsVerificationMessage</a>
</h3>

```typescript
smsVerificationMessage?: pulumi.Input<string>;
```


A string representing the SMS verification message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L257">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the User Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L261">property usernameAttributes</a>
</h3>

```typescript
usernameAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L265">property verificationMessageTemplate</a>
</h3>

```typescript
verificationMessageTemplate?: pulumi.Input<{ ... }>;
```


The [verification message templates](#verification-message-template) configuration.

