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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L10">class IdentityPool</a>
</h2>

Provides an AWS Cognito Identity Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L55">constructor</a>
</h3>

```typescript
new IdentityPool(name: string, args: IdentityPoolArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IdentityPool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IdentityPoolState): IdentityPool
```


Get an existing IdentityPool resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L26">property allowUnauthenticatedIdentities</a>
</h3>

```typescript
public allowUnauthenticatedIdentities: pulumi.Output<boolean | undefined>;
```


Whether the identity pool supports unauthenticated logins or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L30">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the identity pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L34">property cognitoIdentityProviders</a>
</h3>

```typescript
public cognitoIdentityProviders: pulumi.Output<{ ... }[] | undefined>;
```


An array of Amazon Cognito Identity user pools and their client IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L39">property developerProviderName</a>
</h3>

```typescript
public developerProviderName: pulumi.Output<string | undefined>;
```


The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L43">property identityPoolName</a>
</h3>

```typescript
public identityPoolName: pulumi.Output<string>;
```


The Cognito Identity Pool name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L47">property openidConnectProviderArns</a>
</h3>

```typescript
public openidConnectProviderArns: pulumi.Output<string[] | undefined>;
```


A list of OpendID Connect provider ARNs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L51">property samlProviderArns</a>
</h3>

```typescript
public samlProviderArns: pulumi.Output<string[] | undefined>;
```


An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L55">property supportedLoginProviders</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L10">class IdentityPoolRoleAttachment</a>
</h2>

Provides an AWS Cognito Identity Pool Roles Attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L34">constructor</a>
</h3>

```typescript
new IdentityPoolRoleAttachment(name: string, args: IdentityPoolRoleAttachmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IdentityPoolRoleAttachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IdentityPoolRoleAttachmentState): IdentityPoolRoleAttachment
```


Get an existing IdentityPoolRoleAttachment resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L26">property identityPoolId</a>
</h3>

```typescript
public identityPoolId: pulumi.Output<string>;
```


An identity pool ID in the format REGION:GUID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L30">property roleMappings</a>
</h3>

```typescript
public roleMappings: pulumi.Output<{ ... }[] | undefined>;
```


A List of Role Mapping.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L34">property roles</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L10">class IdentityProvider</a>
</h2>

Provides a Cognito User Identity Provider resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L46">constructor</a>
</h3>

```typescript
new IdentityProvider(name: string, args: IdentityProviderArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IdentityProvider resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IdentityProviderState): IdentityProvider
```


Get an existing IdentityProvider resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L26">property attributeMapping</a>
</h3>

```typescript
public attributeMapping: pulumi.Output<{ ... } | undefined>;
```


The map of attribute mapping of user pool attributes. [AttributeMapping in AWS API documentation](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L30">property idpIdentifiers</a>
</h3>

```typescript
public idpIdentifiers: pulumi.Output<string[] | undefined>;
```


The list of identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L34">property providerDetails</a>
</h3>

```typescript
public providerDetails: pulumi.Output<{ ... }>;
```


The map of identity details, such as access token

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L38">property providerName</a>
</h3>

```typescript
public providerName: pulumi.Output<string>;
```


The provider name

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L42">property providerType</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L46">property userPoolId</a>
</h3>

```typescript
public userPoolId: pulumi.Output<string>;
```


The user pool id

<h2 class="pdoc-module-header" id="ResourceServer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L10">class ResourceServer</a>
</h2>

Provides a Cognito Resource Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L39">constructor</a>
</h3>

```typescript
new ResourceServer(name: string, args: ResourceServerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ResourceServer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ResourceServerState): ResourceServer
```


Get an existing ResourceServer resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L26">property identifier</a>
</h3>

```typescript
public identifier: pulumi.Output<string>;
```


An identifier for the resource server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A name for the resource server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L38">property scopeIdentifiers</a>
</h3>

```typescript
public scopeIdentifiers: pulumi.Output<string[]>;
```


A list of all scopes configured for this resource server in the format identifier/scope_name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L34">property scopes</a>
</h3>

```typescript
public scopes: pulumi.Output<{ ... }[] | undefined>;
```


A list of Authorization Scope.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L39">property userPoolId</a>
</h3>

```typescript
public userPoolId: pulumi.Output<string>;
```

<h2 class="pdoc-module-header" id="UserGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L10">class UserGroup</a>
</h2>

Provides a Cognito User Group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L42">constructor</a>
</h3>

```typescript
new UserGroup(name: string, args: UserGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a UserGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserGroupState): UserGroup
```


Get an existing UserGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L26">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L34">property precedence</a>
</h3>

```typescript
public precedence: pulumi.Output<number | undefined>;
```


The precedence of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L38">property roleArn</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L42">property userPoolId</a>
</h3>

```typescript
public userPoolId: pulumi.Output<string>;
```


The user pool ID.

<h2 class="pdoc-module-header" id="UserPool">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L12">class UserPool</a>
</h2>

Provides a Cognito User Pool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L112">constructor</a>
</h3>

```typescript
new UserPool(name: string, args?: UserPoolArgs, opts?: pulumi.CustomResourceOptions)
```


Create a UserPool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserPoolState): UserPool
```


Get an existing UserPool resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L28">property adminCreateUserConfig</a>
</h3>

```typescript
public adminCreateUserConfig: pulumi.Output<{ ... }>;
```


The configuration for AdminCreateUser requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L32">property aliasAttributes</a>
</h3>

```typescript
public aliasAttributes: pulumi.Output<string[] | undefined>;
```


Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L36">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the user pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L40">property autoVerifiedAttributes</a>
</h3>

```typescript
public autoVerifiedAttributes: pulumi.Output<string[] | undefined>;
```


The attributes to be auto-verified. Possible values: email, phone_number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L44">property creationDate</a>
</h3>

```typescript
public creationDate: pulumi.Output<string>;
```


The date the user pool was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L48">property deviceConfiguration</a>
</h3>

```typescript
public deviceConfiguration: pulumi.Output<{ ... } | undefined>;
```


The configuration for the user pool's device tracking.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L52">property emailConfiguration</a>
</h3>

```typescript
public emailConfiguration: pulumi.Output<{ ... } | undefined>;
```


The Email Configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L56">property emailVerificationMessage</a>
</h3>

```typescript
public emailVerificationMessage: pulumi.Output<string>;
```


A string representing the email verification message. Must contain the `{####}` placeholder. **NOTE:** - If `email_verification_message` and `verification_message_template.email_message` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L60">property emailVerificationSubject</a>
</h3>

```typescript
public emailVerificationSubject: pulumi.Output<string>;
```


A string representing the email verification subject. **NOTE:** - If `email_verification_subject` and `verification_message_template.email_subject` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L64">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L68">property lambdaConfig</a>
</h3>

```typescript
public lambdaConfig: pulumi.Output<{ ... }>;
```


A container for the AWS Lambda triggers associated with the user pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L72">property lastModifiedDate</a>
</h3>

```typescript
public lastModifiedDate: pulumi.Output<string>;
```


The date the user pool was last modified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L76">property mfaConfiguration</a>
</h3>

```typescript
public mfaConfiguration: pulumi.Output<string | undefined>;
```


Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L80">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the attribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L84">property passwordPolicy</a>
</h3>

```typescript
public passwordPolicy: pulumi.Output<{ ... }>;
```


A container for information about the user pool password policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L88">property schemas</a>
</h3>

```typescript
public schemas: pulumi.Output<{ ... }[] | undefined>;
```


A container with the schema attributes of a user pool. Maximum of 50 attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L92">property smsAuthenticationMessage</a>
</h3>

```typescript
public smsAuthenticationMessage: pulumi.Output<string | undefined>;
```


A string representing the SMS authentication message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L96">property smsConfiguration</a>
</h3>

```typescript
public smsConfiguration: pulumi.Output<{ ... } | undefined>;
```


The SMS Configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L100">property smsVerificationMessage</a>
</h3>

```typescript
public smsVerificationMessage: pulumi.Output<string | undefined>;
```


A string representing the SMS verification message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L104">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L108">property usernameAttributes</a>
</h3>

```typescript
public usernameAttributes: pulumi.Output<string[] | undefined>;
```


Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L112">property verificationMessageTemplate</a>
</h3>

```typescript
public verificationMessageTemplate: pulumi.Output<{ ... }>;
```


The verification message templates configuration.

<h2 class="pdoc-module-header" id="UserPoolClient">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L10">class UserPoolClient</a>
</h2>

Provides a Cognito User Pool Client resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L82">constructor</a>
</h3>

```typescript
new UserPoolClient(name: string, args: UserPoolClientArgs, opts?: pulumi.CustomResourceOptions)
```


Create a UserPoolClient resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserPoolClientState): UserPoolClient
```


Get an existing UserPoolClient resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L26">property allowedOauthFlows</a>
</h3>

```typescript
public allowedOauthFlows: pulumi.Output<string[] | undefined>;
```


List of allowed OAuth flows (code, implicit, client_credentials).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L30">property allowedOauthFlowsUserPoolClient</a>
</h3>

```typescript
public allowedOauthFlowsUserPoolClient: pulumi.Output<boolean | undefined>;
```


Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L34">property allowedOauthScopes</a>
</h3>

```typescript
public allowedOauthScopes: pulumi.Output<string[] | undefined>;
```


List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L38">property callbackUrls</a>
</h3>

```typescript
public callbackUrls: pulumi.Output<string[] | undefined>;
```


List of allowed callback URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L42">property clientSecret</a>
</h3>

```typescript
public clientSecret: pulumi.Output<string>;
```


The client secret of the user pool client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L46">property defaultRedirectUri</a>
</h3>

```typescript
public defaultRedirectUri: pulumi.Output<string | undefined>;
```


The default redirect URI. Must be in the list of callback URLs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L50">property explicitAuthFlows</a>
</h3>

```typescript
public explicitAuthFlows: pulumi.Output<string[] | undefined>;
```


List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY, USER_PASSWORD_AUTH).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L54">property generateSecret</a>
</h3>

```typescript
public generateSecret: pulumi.Output<boolean | undefined>;
```


Should an application secret be generated. AWS JavaScript SDK requires this to be false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L58">property logoutUrls</a>
</h3>

```typescript
public logoutUrls: pulumi.Output<string[] | undefined>;
```


List of allowed logout URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L62">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the application client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L66">property readAttributes</a>
</h3>

```typescript
public readAttributes: pulumi.Output<string[] | undefined>;
```


List of user pool attributes the application client can read from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L70">property refreshTokenValidity</a>
</h3>

```typescript
public refreshTokenValidity: pulumi.Output<number | undefined>;
```


The time limit in days refresh tokens are valid for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L74">property supportedIdentityProviders</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L78">property userPoolId</a>
</h3>

```typescript
public userPoolId: pulumi.Output<string>;
```


The user pool the client belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L82">property writeAttributes</a>
</h3>

```typescript
public writeAttributes: pulumi.Output<string[] | undefined>;
```


List of user pool attributes the application client can write to.

<h2 class="pdoc-module-header" id="UserPoolDomain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L10">class UserPoolDomain</a>
</h2>

Provides a Cognito User Pool Domain resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L46">constructor</a>
</h3>

```typescript
new UserPoolDomain(name: string, args: UserPoolDomainArgs, opts?: pulumi.CustomResourceOptions)
```


Create a UserPoolDomain resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserPoolDomainState): UserPoolDomain
```


Get an existing UserPoolDomain resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L26">property awsAccountId</a>
</h3>

```typescript
public awsAccountId: pulumi.Output<string>;
```


The AWS account ID for the user pool owner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L30">property cloudfrontDistributionArn</a>
</h3>

```typescript
public cloudfrontDistributionArn: pulumi.Output<string>;
```


The ARN of the CloudFront distribution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L34">property domain</a>
</h3>

```typescript
public domain: pulumi.Output<string>;
```


The domain string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L38">property s3Bucket</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L42">property userPoolId</a>
</h3>

```typescript
public userPoolId: pulumi.Output<string>;
```


The user pool ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L46">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


The app version.

<h2 class="pdoc-module-header" id="getUserPools">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/getUserPools.ts#L10">function getUserPools</a>
</h2>

```typescript
getUserPools(args: GetUserPoolsArgs, opts?: pulumi.InvokeOptions): Promise<GetUserPoolsResult>
```


Use this data source to get a list of cognito user pools.

<h2 class="pdoc-module-header" id="GetUserPoolsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/getUserPools.ts#L19">interface GetUserPoolsArgs</a>
</h2>

A collection of arguments for invoking getUserPools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/getUserPools.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


Name of the cognito user pools. Name is not a unique attribute for cognito user pool, so multiple pools might be returned with given name.

<h2 class="pdoc-module-header" id="GetUserPoolsResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/getUserPools.ts#L29">interface GetUserPoolsResult</a>
</h2>

A collection of values returned by getUserPools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/getUserPools.ts#L30">property arns</a>
</h3>

```typescript
arns: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/getUserPools.ts#L38">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/getUserPools.ts#L34">property ids</a>
</h3>

```typescript
ids: string[];
```


The list of cognito user pool ids.

<h2 class="pdoc-module-header" id="IdentityPoolArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L137">interface IdentityPoolArgs</a>
</h2>

The set of arguments for constructing a IdentityPool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L141">property allowUnauthenticatedIdentities</a>
</h3>

```typescript
allowUnauthenticatedIdentities?: pulumi.Input<boolean>;
```


Whether the identity pool supports unauthenticated logins or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L145">property cognitoIdentityProviders</a>
</h3>

```typescript
cognitoIdentityProviders?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of Amazon Cognito Identity user pools and their client IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L150">property developerProviderName</a>
</h3>

```typescript
developerProviderName?: pulumi.Input<string>;
```


The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L154">property identityPoolName</a>
</h3>

```typescript
identityPoolName: pulumi.Input<string>;
```


The Cognito Identity Pool name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L158">property openidConnectProviderArns</a>
</h3>

```typescript
openidConnectProviderArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of OpendID Connect provider ARNs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L162">property samlProviderArns</a>
</h3>

```typescript
samlProviderArns?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L166">property supportedLoginProviders</a>
</h3>

```typescript
supportedLoginProviders?: pulumi.Input<{ ... }>;
```


Key-Value pairs mapping provider names to provider app IDs.

<h2 class="pdoc-module-header" id="IdentityPoolRoleAttachmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L88">interface IdentityPoolRoleAttachmentArgs</a>
</h2>

The set of arguments for constructing a IdentityPoolRoleAttachment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L92">property identityPoolId</a>
</h3>

```typescript
identityPoolId: pulumi.Input<string>;
```


An identity pool ID in the format REGION:GUID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L96">property roleMappings</a>
</h3>

```typescript
roleMappings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A List of Role Mapping.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L100">property roles</a>
</h3>

```typescript
roles: pulumi.Input<{ ... }>;
```


The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.

<h2 class="pdoc-module-header" id="IdentityPoolRoleAttachmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L70">interface IdentityPoolRoleAttachmentState</a>
</h2>

Input properties used for looking up and filtering IdentityPoolRoleAttachment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L74">property identityPoolId</a>
</h3>

```typescript
identityPoolId?: pulumi.Input<string>;
```


An identity pool ID in the format REGION:GUID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L78">property roleMappings</a>
</h3>

```typescript
roleMappings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A List of Role Mapping.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPoolRoleAttachment.ts#L82">property roles</a>
</h3>

```typescript
roles?: pulumi.Input<{ ... }>;
```


The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.

<h2 class="pdoc-module-header" id="IdentityPoolState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L98">interface IdentityPoolState</a>
</h2>

Input properties used for looking up and filtering IdentityPool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L102">property allowUnauthenticatedIdentities</a>
</h3>

```typescript
allowUnauthenticatedIdentities?: pulumi.Input<boolean>;
```


Whether the identity pool supports unauthenticated logins or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L106">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the identity pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L110">property cognitoIdentityProviders</a>
</h3>

```typescript
cognitoIdentityProviders?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of Amazon Cognito Identity user pools and their client IDs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L115">property developerProviderName</a>
</h3>

```typescript
developerProviderName?: pulumi.Input<string>;
```


The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L119">property identityPoolName</a>
</h3>

```typescript
identityPoolName?: pulumi.Input<string>;
```


The Cognito Identity Pool name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L123">property openidConnectProviderArns</a>
</h3>

```typescript
openidConnectProviderArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of OpendID Connect provider ARNs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L127">property samlProviderArns</a>
</h3>

```typescript
samlProviderArns?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityPool.ts#L131">property supportedLoginProviders</a>
</h3>

```typescript
supportedLoginProviders?: pulumi.Input<{ ... }>;
```


Key-Value pairs mapping provider names to provider app IDs.

<h2 class="pdoc-module-header" id="IdentityProviderArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L124">interface IdentityProviderArgs</a>
</h2>

The set of arguments for constructing a IdentityProvider resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L128">property attributeMapping</a>
</h3>

```typescript
attributeMapping?: pulumi.Input<{ ... }>;
```


The map of attribute mapping of user pool attributes. [AttributeMapping in AWS API documentation](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L132">property idpIdentifiers</a>
</h3>

```typescript
idpIdentifiers?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L136">property providerDetails</a>
</h3>

```typescript
providerDetails: pulumi.Input<{ ... }>;
```


The map of identity details, such as access token

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L140">property providerName</a>
</h3>

```typescript
providerName: pulumi.Input<string>;
```


The provider name

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L144">property providerType</a>
</h3>

```typescript
providerType: pulumi.Input<string>;
```


The provider type.  [See AWS API for valid values](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L148">property userPoolId</a>
</h3>

```typescript
userPoolId: pulumi.Input<string>;
```


The user pool id

<h2 class="pdoc-module-header" id="IdentityProviderState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L94">interface IdentityProviderState</a>
</h2>

Input properties used for looking up and filtering IdentityProvider resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L98">property attributeMapping</a>
</h3>

```typescript
attributeMapping?: pulumi.Input<{ ... }>;
```


The map of attribute mapping of user pool attributes. [AttributeMapping in AWS API documentation](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-AttributeMapping)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L102">property idpIdentifiers</a>
</h3>

```typescript
idpIdentifiers?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L106">property providerDetails</a>
</h3>

```typescript
providerDetails?: pulumi.Input<{ ... }>;
```


The map of identity details, such as access token

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L110">property providerName</a>
</h3>

```typescript
providerName?: pulumi.Input<string>;
```


The provider name

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L114">property providerType</a>
</h3>

```typescript
providerType?: pulumi.Input<string>;
```


The provider type.  [See AWS API for valid values](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.html#CognitoUserPools-CreateIdentityProvider-request-ProviderType)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/identityProvider.ts#L118">property userPoolId</a>
</h3>

```typescript
userPoolId?: pulumi.Input<string>;
```


The user pool id

<h2 class="pdoc-module-header" id="ResourceServerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L102">interface ResourceServerArgs</a>
</h2>

The set of arguments for constructing a ResourceServer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L106">property identifier</a>
</h3>

```typescript
identifier: pulumi.Input<string>;
```


An identifier for the resource server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L110">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the resource server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L114">property scopes</a>
</h3>

```typescript
scopes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of Authorization Scope.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L115">property userPoolId</a>
</h3>

```typescript
userPoolId: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="ResourceServerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L79">interface ResourceServerState</a>
</h2>

Input properties used for looking up and filtering ResourceServer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L83">property identifier</a>
</h3>

```typescript
identifier?: pulumi.Input<string>;
```


An identifier for the resource server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L87">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the resource server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L95">property scopeIdentifiers</a>
</h3>

```typescript
scopeIdentifiers?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of all scopes configured for this resource server in the format identifier/scope_name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L91">property scopes</a>
</h3>

```typescript
scopes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of Authorization Scope.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/resourceServer.ts#L96">property userPoolId</a>
</h3>

```typescript
userPoolId?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="UserGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L105">interface UserGroupArgs</a>
</h2>

The set of arguments for constructing a UserGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L109">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L113">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L117">property precedence</a>
</h3>

```typescript
precedence?: pulumi.Input<number>;
```


The precedence of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L121">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of the IAM role to be associated with the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L125">property userPoolId</a>
</h3>

```typescript
userPoolId: pulumi.Input<string>;
```


The user pool ID.

<h2 class="pdoc-module-header" id="UserGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L79">interface UserGroupState</a>
</h2>

Input properties used for looking up and filtering UserGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L83">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L87">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L91">property precedence</a>
</h3>

```typescript
precedence?: pulumi.Input<number>;
```


The precedence of the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L95">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of the IAM role to be associated with the user group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userGroup.ts#L99">property userPoolId</a>
</h3>

```typescript
userPoolId?: pulumi.Input<string>;
```


The user pool ID.

<h2 class="pdoc-module-header" id="UserPoolArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L274">interface UserPoolArgs</a>
</h2>

The set of arguments for constructing a UserPool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L278">property adminCreateUserConfig</a>
</h3>

```typescript
adminCreateUserConfig?: pulumi.Input<{ ... }>;
```


The configuration for AdminCreateUser requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L282">property aliasAttributes</a>
</h3>

```typescript
aliasAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L286">property autoVerifiedAttributes</a>
</h3>

```typescript
autoVerifiedAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


The attributes to be auto-verified. Possible values: email, phone_number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L290">property deviceConfiguration</a>
</h3>

```typescript
deviceConfiguration?: pulumi.Input<{ ... }>;
```


The configuration for the user pool's device tracking.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L294">property emailConfiguration</a>
</h3>

```typescript
emailConfiguration?: pulumi.Input<{ ... }>;
```


The Email Configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L298">property emailVerificationMessage</a>
</h3>

```typescript
emailVerificationMessage?: pulumi.Input<string>;
```


A string representing the email verification message. Must contain the `{####}` placeholder. **NOTE:** - If `email_verification_message` and `verification_message_template.email_message` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L302">property emailVerificationSubject</a>
</h3>

```typescript
emailVerificationSubject?: pulumi.Input<string>;
```


A string representing the email verification subject. **NOTE:** - If `email_verification_subject` and `verification_message_template.email_subject` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L306">property lambdaConfig</a>
</h3>

```typescript
lambdaConfig?: pulumi.Input<{ ... }>;
```


A container for the AWS Lambda triggers associated with the user pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L310">property mfaConfiguration</a>
</h3>

```typescript
mfaConfiguration?: pulumi.Input<string>;
```


Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L314">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the attribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L318">property passwordPolicy</a>
</h3>

```typescript
passwordPolicy?: pulumi.Input<{ ... }>;
```


A container for information about the user pool password policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L322">property schemas</a>
</h3>

```typescript
schemas?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A container with the schema attributes of a user pool. Maximum of 50 attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L326">property smsAuthenticationMessage</a>
</h3>

```typescript
smsAuthenticationMessage?: pulumi.Input<string>;
```


A string representing the SMS authentication message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L330">property smsConfiguration</a>
</h3>

```typescript
smsConfiguration?: pulumi.Input<{ ... }>;
```


The SMS Configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L334">property smsVerificationMessage</a>
</h3>

```typescript
smsVerificationMessage?: pulumi.Input<string>;
```


A string representing the SMS verification message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L338">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the User Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L342">property usernameAttributes</a>
</h3>

```typescript
usernameAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L346">property verificationMessageTemplate</a>
</h3>

```typescript
verificationMessageTemplate?: pulumi.Input<{ ... }>;
```


The verification message templates configuration.

<h2 class="pdoc-module-header" id="UserPoolClientArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L205">interface UserPoolClientArgs</a>
</h2>

The set of arguments for constructing a UserPoolClient resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L209">property allowedOauthFlows</a>
</h3>

```typescript
allowedOauthFlows?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed OAuth flows (code, implicit, client_credentials).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L213">property allowedOauthFlowsUserPoolClient</a>
</h3>

```typescript
allowedOauthFlowsUserPoolClient?: pulumi.Input<boolean>;
```


Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L217">property allowedOauthScopes</a>
</h3>

```typescript
allowedOauthScopes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L221">property callbackUrls</a>
</h3>

```typescript
callbackUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed callback URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L225">property defaultRedirectUri</a>
</h3>

```typescript
defaultRedirectUri?: pulumi.Input<string>;
```


The default redirect URI. Must be in the list of callback URLs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L229">property explicitAuthFlows</a>
</h3>

```typescript
explicitAuthFlows?: pulumi.Input<pulumi.Input<string>[]>;
```


List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY, USER_PASSWORD_AUTH).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L233">property generateSecret</a>
</h3>

```typescript
generateSecret?: pulumi.Input<boolean>;
```


Should an application secret be generated. AWS JavaScript SDK requires this to be false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L237">property logoutUrls</a>
</h3>

```typescript
logoutUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed logout URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L241">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the application client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L245">property readAttributes</a>
</h3>

```typescript
readAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of user pool attributes the application client can read from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L249">property refreshTokenValidity</a>
</h3>

```typescript
refreshTokenValidity?: pulumi.Input<number>;
```


The time limit in days refresh tokens are valid for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L253">property supportedIdentityProviders</a>
</h3>

```typescript
supportedIdentityProviders?: pulumi.Input<pulumi.Input<string>[]>;
```


List of provider names for the identity providers that are supported on this client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L257">property userPoolId</a>
</h3>

```typescript
userPoolId: pulumi.Input<string>;
```


The user pool the client belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L261">property writeAttributes</a>
</h3>

```typescript
writeAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of user pool attributes the application client can write to.

<h2 class="pdoc-module-header" id="UserPoolClientState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L139">interface UserPoolClientState</a>
</h2>

Input properties used for looking up and filtering UserPoolClient resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L143">property allowedOauthFlows</a>
</h3>

```typescript
allowedOauthFlows?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed OAuth flows (code, implicit, client_credentials).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L147">property allowedOauthFlowsUserPoolClient</a>
</h3>

```typescript
allowedOauthFlowsUserPoolClient?: pulumi.Input<boolean>;
```


Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L151">property allowedOauthScopes</a>
</h3>

```typescript
allowedOauthScopes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L155">property callbackUrls</a>
</h3>

```typescript
callbackUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed callback URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L159">property clientSecret</a>
</h3>

```typescript
clientSecret?: pulumi.Input<string>;
```


The client secret of the user pool client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L163">property defaultRedirectUri</a>
</h3>

```typescript
defaultRedirectUri?: pulumi.Input<string>;
```


The default redirect URI. Must be in the list of callback URLs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L167">property explicitAuthFlows</a>
</h3>

```typescript
explicitAuthFlows?: pulumi.Input<pulumi.Input<string>[]>;
```


List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY, USER_PASSWORD_AUTH).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L171">property generateSecret</a>
</h3>

```typescript
generateSecret?: pulumi.Input<boolean>;
```


Should an application secret be generated. AWS JavaScript SDK requires this to be false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L175">property logoutUrls</a>
</h3>

```typescript
logoutUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


List of allowed logout URLs for the identity providers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L179">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the application client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L183">property readAttributes</a>
</h3>

```typescript
readAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of user pool attributes the application client can read from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L187">property refreshTokenValidity</a>
</h3>

```typescript
refreshTokenValidity?: pulumi.Input<number>;
```


The time limit in days refresh tokens are valid for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L191">property supportedIdentityProviders</a>
</h3>

```typescript
supportedIdentityProviders?: pulumi.Input<pulumi.Input<string>[]>;
```


List of provider names for the identity providers that are supported on this client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L195">property userPoolId</a>
</h3>

```typescript
userPoolId?: pulumi.Input<string>;
```


The user pool the client belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolClient.ts#L199">property writeAttributes</a>
</h3>

```typescript
writeAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


List of user pool attributes the application client can write to.

<h2 class="pdoc-module-header" id="UserPoolDomainArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L118">interface UserPoolDomainArgs</a>
</h2>

The set of arguments for constructing a UserPoolDomain resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L122">property domain</a>
</h3>

```typescript
domain: pulumi.Input<string>;
```


The domain string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L126">property userPoolId</a>
</h3>

```typescript
userPoolId: pulumi.Input<string>;
```


The user pool ID.

<h2 class="pdoc-module-header" id="UserPoolDomainState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L88">interface UserPoolDomainState</a>
</h2>

Input properties used for looking up and filtering UserPoolDomain resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L92">property awsAccountId</a>
</h3>

```typescript
awsAccountId?: pulumi.Input<string>;
```


The AWS account ID for the user pool owner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L96">property cloudfrontDistributionArn</a>
</h3>

```typescript
cloudfrontDistributionArn?: pulumi.Input<string>;
```


The ARN of the CloudFront distribution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L100">property domain</a>
</h3>

```typescript
domain?: pulumi.Input<string>;
```


The domain string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L104">property s3Bucket</a>
</h3>

```typescript
s3Bucket?: pulumi.Input<string>;
```


The S3 bucket where the static files for this domain are stored.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L108">property userPoolId</a>
</h3>

```typescript
userPoolId?: pulumi.Input<string>;
```


The user pool ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPoolDomain.ts#L112">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The app version.

<h2 class="pdoc-module-header" id="UserPoolState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L180">interface UserPoolState</a>
</h2>

Input properties used for looking up and filtering UserPool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L184">property adminCreateUserConfig</a>
</h3>

```typescript
adminCreateUserConfig?: pulumi.Input<{ ... }>;
```


The configuration for AdminCreateUser requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L188">property aliasAttributes</a>
</h3>

```typescript
aliasAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L192">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the user pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L196">property autoVerifiedAttributes</a>
</h3>

```typescript
autoVerifiedAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


The attributes to be auto-verified. Possible values: email, phone_number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L200">property creationDate</a>
</h3>

```typescript
creationDate?: pulumi.Input<string>;
```


The date the user pool was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L204">property deviceConfiguration</a>
</h3>

```typescript
deviceConfiguration?: pulumi.Input<{ ... }>;
```


The configuration for the user pool's device tracking.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L208">property emailConfiguration</a>
</h3>

```typescript
emailConfiguration?: pulumi.Input<{ ... }>;
```


The Email Configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L212">property emailVerificationMessage</a>
</h3>

```typescript
emailVerificationMessage?: pulumi.Input<string>;
```


A string representing the email verification message. Must contain the `{####}` placeholder. **NOTE:** - If `email_verification_message` and `verification_message_template.email_message` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L216">property emailVerificationSubject</a>
</h3>

```typescript
emailVerificationSubject?: pulumi.Input<string>;
```


A string representing the email verification subject. **NOTE:** - If `email_verification_subject` and `verification_message_template.email_subject` are specified and the values are different, either one is prioritized and updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L220">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L224">property lambdaConfig</a>
</h3>

```typescript
lambdaConfig?: pulumi.Input<{ ... }>;
```


A container for the AWS Lambda triggers associated with the user pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L228">property lastModifiedDate</a>
</h3>

```typescript
lastModifiedDate?: pulumi.Input<string>;
```


The date the user pool was last modified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L232">property mfaConfiguration</a>
</h3>

```typescript
mfaConfiguration?: pulumi.Input<string>;
```


Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L236">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the attribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L240">property passwordPolicy</a>
</h3>

```typescript
passwordPolicy?: pulumi.Input<{ ... }>;
```


A container for information about the user pool password policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L244">property schemas</a>
</h3>

```typescript
schemas?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A container with the schema attributes of a user pool. Maximum of 50 attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L248">property smsAuthenticationMessage</a>
</h3>

```typescript
smsAuthenticationMessage?: pulumi.Input<string>;
```


A string representing the SMS authentication message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L252">property smsConfiguration</a>
</h3>

```typescript
smsConfiguration?: pulumi.Input<{ ... }>;
```


The SMS Configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L256">property smsVerificationMessage</a>
</h3>

```typescript
smsVerificationMessage?: pulumi.Input<string>;
```


A string representing the SMS verification message.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L260">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the User Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L264">property usernameAttributes</a>
</h3>

```typescript
usernameAttributes?: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cognito/userPool.ts#L268">property verificationMessageTemplate</a>
</h3>

```typescript
verificationMessageTemplate?: pulumi.Input<{ ... }>;
```


The verification message templates configuration.

