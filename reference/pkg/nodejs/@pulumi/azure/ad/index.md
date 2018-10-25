---
title: Module ad
---

<a href="../index.html">@pulumi/azure</a> &gt; ad

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Application">class Application</a>
* <a href="#ServicePrincipal">class ServicePrincipal</a>
* <a href="#ServicePrincipalPassword">class ServicePrincipalPassword</a>
* <a href="#getApplication">function getApplication</a>
* <a href="#getServicePrincipal">function getServicePrincipal</a>
* <a href="#ApplicationArgs">interface ApplicationArgs</a>
* <a href="#ApplicationState">interface ApplicationState</a>
* <a href="#GetApplicationArgs">interface GetApplicationArgs</a>
* <a href="#GetApplicationResult">interface GetApplicationResult</a>
* <a href="#GetServicePrincipalArgs">interface GetServicePrincipalArgs</a>
* <a href="#GetServicePrincipalResult">interface GetServicePrincipalResult</a>
* <a href="#ServicePrincipalArgs">interface ServicePrincipalArgs</a>
* <a href="#ServicePrincipalPasswordArgs">interface ServicePrincipalPasswordArgs</a>
* <a href="#ServicePrincipalPasswordState">interface ServicePrincipalPasswordState</a>
* <a href="#ServicePrincipalState">interface ServicePrincipalState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts">ad/application.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts">ad/getApplication.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts">ad/getServicePrincipal.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts">ad/servicePrincipal.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts">ad/servicePrincipalPassword.ts</a> 


<h2 class="pdoc-module-header" id="Application">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L12">class Application</a>
</h2>

Manages an Application within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L52">constructor</a>
</h3>

```typescript
new Application(name: string, args?: ApplicationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Application resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApplicationState): Application
```


Get an existing Application resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L28">property applicationId</a>
</h3>

```typescript
public applicationId: pulumi.Output<string>;
```


The Application ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L32">property availableToOtherTenants</a>
</h3>

```typescript
public availableToOtherTenants: pulumi.Output<boolean | undefined>;
```


Is this Azure AD Application available to other tenants? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L36">property homepage</a>
</h3>

```typescript
public homepage: pulumi.Output<string>;
```


The URL to the application's home page. If no homepage is specified this defaults to `https://{name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L40">property identifierUris</a>
</h3>

```typescript
public identifierUris: pulumi.Output<string[]>;
```


A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The display name for the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L48">property oauth2AllowImplicitFlow</a>
</h3>

```typescript
public oauth2AllowImplicitFlow: pulumi.Output<boolean | undefined>;
```


Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L52">property replyUrls</a>
</h3>

```typescript
public replyUrls: pulumi.Output<string[]>;
```


A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ServicePrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L12">class ServicePrincipal</a>
</h2>

Manages a Service Principal associated with an Application within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L32">constructor</a>
</h3>

```typescript
new ServicePrincipal(name: string, args: ServicePrincipalArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ServicePrincipal resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServicePrincipalState): ServicePrincipal
```


Get an existing ServicePrincipal resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L28">property applicationId</a>
</h3>

```typescript
public applicationId: pulumi.Output<string>;
```


The ID of the Azure AD Application for which to create a Service Principal.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L32">property displayName</a>
</h3>

```typescript
public displayName: pulumi.Output<string>;
```


The Display Name of the Azure Active Directory Application associated with this Service Principal.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ServicePrincipalPassword">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L12">class ServicePrincipalPassword</a>
</h2>

Manages a Password associated with a Service Principal within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L44">constructor</a>
</h3>

```typescript
new ServicePrincipalPassword(name: string, args: ServicePrincipalPasswordArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ServicePrincipalPassword resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServicePrincipalPasswordState): ServicePrincipalPassword
```


Get an existing ServicePrincipalPassword resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L28">property endDate</a>
</h3>

```typescript
public endDate: pulumi.Output<string>;
```


The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L32">property keyId</a>
</h3>

```typescript
public keyId: pulumi.Output<string>;
```


A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L36">property servicePrincipalId</a>
</h3>

```typescript
public servicePrincipalId: pulumi.Output<string>;
```


The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L40">property startDate</a>
</h3>

```typescript
public startDate: pulumi.Output<string>;
```


The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L44">property value</a>
</h3>

```typescript
public value: pulumi.Output<string>;
```


The Password for this Service Principal.

<h2 class="pdoc-module-header" id="getApplication">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L12">function getApplication</a>
</h2>

```typescript
getApplication(args?: GetApplicationArgs, opts?: pulumi.InvokeOptions): Promise<GetApplicationResult>
```


Use this data source to access information about an existing Application within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

<h2 class="pdoc-module-header" id="getServicePrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L12">function getServicePrincipal</a>
</h2>

```typescript
getServicePrincipal(args?: GetServicePrincipalArgs, opts?: pulumi.InvokeOptions): Promise<GetServicePrincipalResult>
```


Gets information about an existing Service Principal associated with an Application within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

<h2 class="pdoc-module-header" id="ApplicationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L124">interface ApplicationArgs</a>
</h2>

The set of arguments for constructing a Application resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L128">property availableToOtherTenants</a>
</h3>

```typescript
availableToOtherTenants?: pulumi.Input<boolean>;
```


Is this Azure AD Application available to other tenants? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L132">property homepage</a>
</h3>

```typescript
homepage?: pulumi.Input<string>;
```


The URL to the application's home page. If no homepage is specified this defaults to `https://{name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L136">property identifierUris</a>
</h3>

```typescript
identifierUris?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L140">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The display name for the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L144">property oauth2AllowImplicitFlow</a>
</h3>

```typescript
oauth2AllowImplicitFlow?: pulumi.Input<boolean>;
```


Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L148">property replyUrls</a>
</h3>

```typescript
replyUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.

<h2 class="pdoc-module-header" id="ApplicationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L90">interface ApplicationState</a>
</h2>

Input properties used for looking up and filtering Application resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L94">property applicationId</a>
</h3>

```typescript
applicationId?: pulumi.Input<string>;
```


The Application ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L98">property availableToOtherTenants</a>
</h3>

```typescript
availableToOtherTenants?: pulumi.Input<boolean>;
```


Is this Azure AD Application available to other tenants? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L102">property homepage</a>
</h3>

```typescript
homepage?: pulumi.Input<string>;
```


The URL to the application's home page. If no homepage is specified this defaults to `https://{name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L106">property identifierUris</a>
</h3>

```typescript
identifierUris?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L110">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The display name for the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L114">property oauth2AllowImplicitFlow</a>
</h3>

```typescript
oauth2AllowImplicitFlow?: pulumi.Input<boolean>;
```


Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L118">property replyUrls</a>
</h3>

```typescript
replyUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.

<h2 class="pdoc-module-header" id="GetApplicationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L23">interface GetApplicationArgs</a>
</h2>

A collection of arguments for invoking getApplication.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L27">property name</a>
</h3>

```typescript
name?: string;
```


Specifies the name of the Application within Azure Active Directory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L31">property objectId</a>
</h3>

```typescript
objectId?: string;
```


Specifies the Object ID of the Application within Azure Active Directory.

<h2 class="pdoc-module-header" id="GetApplicationResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L37">interface GetApplicationResult</a>
</h2>

A collection of values returned by getApplication.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L41">property applicationId</a>
</h3>

```typescript
applicationId: string;
```


the Application ID of the Azure Active Directory Application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L45">property availableToOtherTenants</a>
</h3>

```typescript
availableToOtherTenants: boolean;
```


Is this Azure AD Application available to other tenants?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L46">property homepage</a>
</h3>

```typescript
homepage: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L67">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L50">property identifierUris</a>
</h3>

```typescript
identifierUris: string[];
```


A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L51">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L55">property oauth2AllowImplicitFlow</a>
</h3>

```typescript
oauth2AllowImplicitFlow: boolean;
```


Does this Azure AD Application allow OAuth2.0 implicit flow tokens?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L59">property objectId</a>
</h3>

```typescript
objectId: string;
```


the Object ID of the Azure Active Directory Application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L63">property replyUrls</a>
</h3>

```typescript
replyUrls: string[];
```


A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.

<h2 class="pdoc-module-header" id="GetServicePrincipalArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L24">interface GetServicePrincipalArgs</a>
</h2>

A collection of arguments for invoking getServicePrincipal.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L28">property applicationId</a>
</h3>

```typescript
applicationId?: string;
```


The ID of the Azure AD Application for which to create a Service Principal.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L32">property displayName</a>
</h3>

```typescript
displayName?: string;
```


The Display Name of the Azure AD Application associated with this Service Principal.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L36">property objectId</a>
</h3>

```typescript
objectId?: string;
```


The ID of the Azure AD Service Principal.

<h2 class="pdoc-module-header" id="GetServicePrincipalResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L42">interface GetServicePrincipalResult</a>
</h2>

A collection of values returned by getServicePrincipal.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L43">property applicationId</a>
</h3>

```typescript
applicationId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L44">property displayName</a>
</h3>

```typescript
displayName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L49">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L45">property objectId</a>
</h3>

```typescript
objectId: string;
```

<h2 class="pdoc-module-header" id="ServicePrincipalArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L77">interface ServicePrincipalArgs</a>
</h2>

The set of arguments for constructing a ServicePrincipal resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L81">property applicationId</a>
</h3>

```typescript
applicationId: pulumi.Input<string>;
```


The ID of the Azure AD Application for which to create a Service Principal.

<h2 class="pdoc-module-header" id="ServicePrincipalPasswordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L113">interface ServicePrincipalPasswordArgs</a>
</h2>

The set of arguments for constructing a ServicePrincipalPassword resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L117">property endDate</a>
</h3>

```typescript
endDate: pulumi.Input<string>;
```


The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L121">property keyId</a>
</h3>

```typescript
keyId?: pulumi.Input<string>;
```


A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L125">property servicePrincipalId</a>
</h3>

```typescript
servicePrincipalId: pulumi.Input<string>;
```


The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L129">property startDate</a>
</h3>

```typescript
startDate?: pulumi.Input<string>;
```


The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L133">property value</a>
</h3>

```typescript
value: pulumi.Input<string>;
```


The Password for this Service Principal.

<h2 class="pdoc-module-header" id="ServicePrincipalPasswordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L87">interface ServicePrincipalPasswordState</a>
</h2>

Input properties used for looking up and filtering ServicePrincipalPassword resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L91">property endDate</a>
</h3>

```typescript
endDate?: pulumi.Input<string>;
```


The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L95">property keyId</a>
</h3>

```typescript
keyId?: pulumi.Input<string>;
```


A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L99">property servicePrincipalId</a>
</h3>

```typescript
servicePrincipalId?: pulumi.Input<string>;
```


The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L103">property startDate</a>
</h3>

```typescript
startDate?: pulumi.Input<string>;
```


The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L107">property value</a>
</h3>

```typescript
value?: pulumi.Input<string>;
```


The Password for this Service Principal.

<h2 class="pdoc-module-header" id="ServicePrincipalState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L63">interface ServicePrincipalState</a>
</h2>

Input properties used for looking up and filtering ServicePrincipal resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L67">property applicationId</a>
</h3>

```typescript
applicationId?: pulumi.Input<string>;
```


The ID of the Azure AD Application for which to create a Service Principal.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L71">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


The Display Name of the Azure Active Directory Application associated with this Service Principal.

