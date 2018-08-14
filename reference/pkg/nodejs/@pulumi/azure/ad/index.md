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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L11">class Application</a>
</h2>

Manages an Application within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L51">constructor</a>
</h3>

```typescript
new Application(name: string, args?: ApplicationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Application resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L27">property applicationId</a>
</h3>

```typescript
public applicationId: pulumi.Output<string>;
```


The Application ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L31">property availableToOtherTenants</a>
</h3>

```typescript
public availableToOtherTenants: pulumi.Output<boolean | undefined>;
```


Is this Azure AD Application available to other tenants? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L35">property homepage</a>
</h3>

```typescript
public homepage: pulumi.Output<string>;
```


The URL to the application's home page. If no homepage is specified this defaults to `http://{name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L39">property identifierUris</a>
</h3>

```typescript
public identifierUris: pulumi.Output<string[]>;
```


A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L43">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The display name for the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L47">property oauth2AllowImplicitFlow</a>
</h3>

```typescript
public oauth2AllowImplicitFlow: pulumi.Output<boolean | undefined>;
```


Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L51">property replyUrls</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L11">class ServicePrincipal</a>
</h2>

Manages a Service Principal associated with an Application within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L31">constructor</a>
</h3>

```typescript
new ServicePrincipal(name: string, args: ServicePrincipalArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ServicePrincipal resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L27">property applicationId</a>
</h3>

```typescript
public applicationId: pulumi.Output<string>;
```


The ID of the Azure AD Application for which to create a Service Principal.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L31">property displayName</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L11">class ServicePrincipalPassword</a>
</h2>

Manages a Password associated with a Service Principal within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L43">constructor</a>
</h3>

```typescript
new ServicePrincipalPassword(name: string, args: ServicePrincipalPasswordArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ServicePrincipalPassword resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L27">property endDate</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L31">property keyId</a>
</h3>

```typescript
public keyId: pulumi.Output<string>;
```


A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L35">property servicePrincipalId</a>
</h3>

```typescript
public servicePrincipalId: pulumi.Output<string>;
```


The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L39">property startDate</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L43">property value</a>
</h3>

```typescript
public value: pulumi.Output<string>;
```


The Password for this Service Principal.

<h2 class="pdoc-module-header" id="getApplication">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L11">function getApplication</a>
</h2>

```typescript
getApplication(args?: GetApplicationArgs, opts?: pulumi.InvokeOptions): Promise<GetApplicationResult>
```


Gets information about an Application within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

<h2 class="pdoc-module-header" id="getServicePrincipal">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L11">function getServicePrincipal</a>
</h2>

```typescript
getServicePrincipal(args?: GetServicePrincipalArgs, opts?: pulumi.InvokeOptions): Promise<GetServicePrincipalResult>
```


Gets information about a Service Principal associated with an Application within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

<h2 class="pdoc-module-header" id="ApplicationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L123">interface ApplicationArgs</a>
</h2>

The set of arguments for constructing a Application resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L127">property availableToOtherTenants</a>
</h3>

```typescript
availableToOtherTenants?: pulumi.Input<boolean>;
```


Is this Azure AD Application available to other tenants? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L131">property homepage</a>
</h3>

```typescript
homepage?: pulumi.Input<string>;
```


The URL to the application's home page. If no homepage is specified this defaults to `http://{name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L135">property identifierUris</a>
</h3>

```typescript
identifierUris?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L139">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The display name for the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L143">property oauth2AllowImplicitFlow</a>
</h3>

```typescript
oauth2AllowImplicitFlow?: pulumi.Input<boolean>;
```


Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L147">property replyUrls</a>
</h3>

```typescript
replyUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.

<h2 class="pdoc-module-header" id="ApplicationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L89">interface ApplicationState</a>
</h2>

Input properties used for looking up and filtering Application resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L93">property applicationId</a>
</h3>

```typescript
applicationId?: pulumi.Input<string>;
```


The Application ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L97">property availableToOtherTenants</a>
</h3>

```typescript
availableToOtherTenants?: pulumi.Input<boolean>;
```


Is this Azure AD Application available to other tenants? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L101">property homepage</a>
</h3>

```typescript
homepage?: pulumi.Input<string>;
```


The URL to the application's home page. If no homepage is specified this defaults to `http://{name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L105">property identifierUris</a>
</h3>

```typescript
identifierUris?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L109">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The display name for the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L113">property oauth2AllowImplicitFlow</a>
</h3>

```typescript
oauth2AllowImplicitFlow?: pulumi.Input<boolean>;
```


Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/application.ts#L117">property replyUrls</a>
</h3>

```typescript
replyUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.

<h2 class="pdoc-module-header" id="GetApplicationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L22">interface GetApplicationArgs</a>
</h2>

A collection of arguments for invoking getApplication.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L26">property name</a>
</h3>

```typescript
name?: string;
```


Specifies the name of the Application within Azure Active Directory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L30">property objectId</a>
</h3>

```typescript
objectId?: string;
```


Specifies the Object ID of the Application within Azure Active Directory.

<h2 class="pdoc-module-header" id="GetApplicationResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L36">interface GetApplicationResult</a>
</h2>

A collection of values returned by getApplication.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L40">property applicationId</a>
</h3>

```typescript
applicationId: string;
```


the Application ID of the Azure Active Directory Application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L44">property availableToOtherTenants</a>
</h3>

```typescript
availableToOtherTenants: boolean;
```


Is this Azure AD Application available to other tenants?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L45">property homepage</a>
</h3>

```typescript
homepage: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L66">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L49">property identifierUris</a>
</h3>

```typescript
identifierUris: string[];
```


A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L50">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L54">property oauth2AllowImplicitFlow</a>
</h3>

```typescript
oauth2AllowImplicitFlow: boolean;
```


Does this Azure AD Application allow OAuth2.0 implicit flow tokens?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L58">property objectId</a>
</h3>

```typescript
objectId: string;
```


the Object ID of the Azure Active Directory Application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getApplication.ts#L62">property replyUrls</a>
</h3>

```typescript
replyUrls: string[];
```


A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.

<h2 class="pdoc-module-header" id="GetServicePrincipalArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L23">interface GetServicePrincipalArgs</a>
</h2>

A collection of arguments for invoking getServicePrincipal.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L27">property applicationId</a>
</h3>

```typescript
applicationId?: string;
```


The ID of the Azure AD Application for which to create a Service Principal.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L31">property displayName</a>
</h3>

```typescript
displayName?: string;
```


The Display Name of the Azure AD Application associated with this Service Principal.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L35">property objectId</a>
</h3>

```typescript
objectId?: string;
```


The ID of the Azure AD Service Principal.

<h2 class="pdoc-module-header" id="GetServicePrincipalResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L41">interface GetServicePrincipalResult</a>
</h2>

A collection of values returned by getServicePrincipal.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L42">property applicationId</a>
</h3>

```typescript
applicationId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L43">property displayName</a>
</h3>

```typescript
displayName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L48">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/getServicePrincipal.ts#L44">property objectId</a>
</h3>

```typescript
objectId: string;
```

<h2 class="pdoc-module-header" id="ServicePrincipalArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L76">interface ServicePrincipalArgs</a>
</h2>

The set of arguments for constructing a ServicePrincipal resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L80">property applicationId</a>
</h3>

```typescript
applicationId: pulumi.Input<string>;
```


The ID of the Azure AD Application for which to create a Service Principal.

<h2 class="pdoc-module-header" id="ServicePrincipalPasswordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L112">interface ServicePrincipalPasswordArgs</a>
</h2>

The set of arguments for constructing a ServicePrincipalPassword resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L116">property endDate</a>
</h3>

```typescript
endDate: pulumi.Input<string>;
```


The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L120">property keyId</a>
</h3>

```typescript
keyId?: pulumi.Input<string>;
```


A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L124">property servicePrincipalId</a>
</h3>

```typescript
servicePrincipalId: pulumi.Input<string>;
```


The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L128">property startDate</a>
</h3>

```typescript
startDate?: pulumi.Input<string>;
```


The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L132">property value</a>
</h3>

```typescript
value: pulumi.Input<string>;
```


The Password for this Service Principal.

<h2 class="pdoc-module-header" id="ServicePrincipalPasswordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L86">interface ServicePrincipalPasswordState</a>
</h2>

Input properties used for looking up and filtering ServicePrincipalPassword resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L90">property endDate</a>
</h3>

```typescript
endDate?: pulumi.Input<string>;
```


The End Date which the Password is valid until, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L94">property keyId</a>
</h3>

```typescript
keyId?: pulumi.Input<string>;
```


A GUID used to uniquely identify this Key. If not specified a GUID will be created. Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L98">property servicePrincipalId</a>
</h3>

```typescript
servicePrincipalId?: pulumi.Input<string>;
```


The ID of the Service Principal for which this password should be created. Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L102">property startDate</a>
</h3>

```typescript
startDate?: pulumi.Input<string>;
```


The Start Date which the Password is valid from, formatted as a RFC3339 date string (e.g. `2018-01-01T01:02:03Z`). If this isn't specified, the current date is used.  Changing this field forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipalPassword.ts#L106">property value</a>
</h3>

```typescript
value?: pulumi.Input<string>;
```


The Password for this Service Principal.

<h2 class="pdoc-module-header" id="ServicePrincipalState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L62">interface ServicePrincipalState</a>
</h2>

Input properties used for looking up and filtering ServicePrincipal resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L66">property applicationId</a>
</h3>

```typescript
applicationId?: pulumi.Input<string>;
```


The ID of the Azure AD Application for which to create a Service Principal.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/ad/servicePrincipal.ts#L70">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


The Display Name of the Azure Active Directory Application associated with this Service Principal.

