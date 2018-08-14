---
title: Module identity
---

<a href="../index.html">@pulumi/openstack</a> &gt; identity

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Project">class Project</a>
* <a href="#Role">class Role</a>
* <a href="#RoleAssignment">class RoleAssignment</a>
* <a href="#User">class User</a>
* <a href="#getAuthScope">function getAuthScope</a>
* <a href="#getEndpoint">function getEndpoint</a>
* <a href="#getGroup">function getGroup</a>
* <a href="#getProject">function getProject</a>
* <a href="#getRole">function getRole</a>
* <a href="#getUser">function getUser</a>
* <a href="#GetAuthScopeArgs">interface GetAuthScopeArgs</a>
* <a href="#GetAuthScopeResult">interface GetAuthScopeResult</a>
* <a href="#GetEndpointArgs">interface GetEndpointArgs</a>
* <a href="#GetEndpointResult">interface GetEndpointResult</a>
* <a href="#GetGroupArgs">interface GetGroupArgs</a>
* <a href="#GetGroupResult">interface GetGroupResult</a>
* <a href="#GetProjectArgs">interface GetProjectArgs</a>
* <a href="#GetProjectResult">interface GetProjectResult</a>
* <a href="#GetRoleArgs">interface GetRoleArgs</a>
* <a href="#GetRoleResult">interface GetRoleResult</a>
* <a href="#GetUserArgs">interface GetUserArgs</a>
* <a href="#GetUserResult">interface GetUserResult</a>
* <a href="#ProjectArgs">interface ProjectArgs</a>
* <a href="#ProjectState">interface ProjectState</a>
* <a href="#RoleArgs">interface RoleArgs</a>
* <a href="#RoleAssignmentArgs">interface RoleAssignmentArgs</a>
* <a href="#RoleAssignmentState">interface RoleAssignmentState</a>
* <a href="#RoleState">interface RoleState</a>
* <a href="#UserArgs">interface UserArgs</a>
* <a href="#UserState">interface UserState</a>

<a href="/identity/getAuthScope.ts">identity/getAuthScope.ts</a> <a href="/identity/getEndpoint.ts">identity/getEndpoint.ts</a> <a href="/identity/getGroup.ts">identity/getGroup.ts</a> <a href="/identity/getProject.ts">identity/getProject.ts</a> <a href="/identity/getRole.ts">identity/getRole.ts</a> <a href="/identity/getUser.ts">identity/getUser.ts</a> <a href="/identity/project.ts">identity/project.ts</a> <a href="/identity/role.ts">identity/role.ts</a> <a href="/identity/roleAssignment.ts">identity/roleAssignment.ts</a> <a href="/identity/user.ts">identity/user.ts</a> 


<h2 class="pdoc-module-header" id="Project">
<a class="pdoc-member-name" href="/identity/project.ts#L12">class Project</a>
</h2>

Manages a V3 Project resource within OpenStack Keystone.

Note: You _must_ have admin privileges in your OpenStack cloud to use
this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L56">constructor</a>
</h3>

```typescript
new Project(name: string, args?: ProjectArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Project resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProjectState): Project
```


Get an existing Project resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L28">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L32">property domainId</a>
</h3>

```typescript
public domainId: pulumi.Output<string>;
```


The domain this project belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L37">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Whether the project is enabled or disabled. Valid
values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L42">property isDomain</a>
</h3>

```typescript
public isDomain: pulumi.Output<boolean | undefined>;
```


Whether this project is a domain. Valid values
are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L46">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L50">property parentId</a>
</h3>

```typescript
public parentId: pulumi.Output<string>;
```


The parent of this project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L56">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new User.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Role">
<a class="pdoc-member-name" href="/identity/role.ts#L12">class Role</a>
</h2>

Manages a V3 Role resource within OpenStack Keystone.

Note: You _must_ have admin privileges in your OpenStack cloud to use
this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/role.ts#L38">constructor</a>
</h3>

```typescript
new Role(name: string, args?: RoleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Role resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/role.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RoleState): Role
```


Get an existing Role resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/role.ts#L28">property domainId</a>
</h3>

```typescript
public domainId: pulumi.Output<string>;
```


The domain the role belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/role.ts#L32">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/role.ts#L38">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new Role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RoleAssignment">
<a class="pdoc-member-name" href="/identity/roleAssignment.ts#L12">class RoleAssignment</a>
</h2>

Manages a V3 Role assignment within OpenStack Keystone.

Note: You _must_ have admin privileges in your OpenStack cloud to use
this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/roleAssignment.ts#L44">constructor</a>
</h3>

```typescript
new RoleAssignment(name: string, args: RoleAssignmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RoleAssignment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/roleAssignment.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RoleAssignmentState): RoleAssignment
```


Get an existing RoleAssignment resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/roleAssignment.ts#L28">property domainId</a>
</h3>

```typescript
public domainId: pulumi.Output<string | undefined>;
```


The domain to assign the role in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/roleAssignment.ts#L32">property groupId</a>
</h3>

```typescript
public groupId: pulumi.Output<string | undefined>;
```


The group to assign the role to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/roleAssignment.ts#L36">property projectId</a>
</h3>

```typescript
public projectId: pulumi.Output<string | undefined>;
```


The project to assign the role in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/roleAssignment.ts#L40">property roleId</a>
</h3>

```typescript
public roleId: pulumi.Output<string>;
```


The role to assign.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/roleAssignment.ts#L44">property userId</a>
</h3>

```typescript
public userId: pulumi.Output<string | undefined>;
```


The user to assign the role to.

<h2 class="pdoc-module-header" id="User">
<a class="pdoc-member-name" href="/identity/user.ts#L12">class User</a>
</h2>

Manages a V3 User resource within OpenStack Keystone.

Note: You _must_ have admin privileges in your OpenStack cloud to use
this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L86">constructor</a>
</h3>

```typescript
new User(name: string, args?: UserArgs, opts?: pulumi.CustomResourceOptions)
```


Create a User resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserState): User
```


Get an existing User resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L28">property defaultProjectId</a>
</h3>

```typescript
public defaultProjectId: pulumi.Output<string>;
```


The default project this user belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L32">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L36">property domainId</a>
</h3>

```typescript
public domainId: pulumi.Output<string>;
```


The domain this user belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L41">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Whether the user is enabled or disabled. Valid
values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L45">property extra</a>
</h3>

```typescript
public extra: pulumi.Output<{ ... } | undefined>;
```


Free-form key/value pairs of extra information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L50">property ignoreChangePasswordUponFirstUse</a>
</h3>

```typescript
public ignoreChangePasswordUponFirstUse: pulumi.Output<boolean | undefined>;
```


User will not have to
change their password upon first use. Valid values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L55">property ignoreLockoutFailureAttempts</a>
</h3>

```typescript
public ignoreLockoutFailureAttempts: pulumi.Output<boolean | undefined>;
```


User will not have a failure
lockout placed on their account. Valid values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L60">property ignorePasswordExpiry</a>
</h3>

```typescript
public ignorePasswordExpiry: pulumi.Output<boolean | undefined>;
```


User's password will not expire.
Valid values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L65">property multiFactorAuthEnabled</a>
</h3>

```typescript
public multiFactorAuthEnabled: pulumi.Output<boolean | undefined>;
```


Whether to enable multi-factor
authentication. Valid values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L72">property multiFactorAuthRules</a>
</h3>

```typescript
public multiFactorAuthRules: pulumi.Output<{ ... }[] | undefined>;
```


A multi-factor authentication rule.
The structure is documented below. Please see the
[Ocata release notes](https://docs.openstack.org/releasenotes/keystone/ocata.html)
for more information on how to use mulit-factor rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L76">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L80">property password</a>
</h3>

```typescript
public password: pulumi.Output<string | undefined>;
```


The password for the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L86">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new User.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getAuthScope">
<a class="pdoc-member-name" href="/identity/getAuthScope.ts#L11">function getAuthScope</a>
</h2>

```typescript
getAuthScope(args: GetAuthScopeArgs, opts?: pulumi.InvokeOptions): Promise<GetAuthScopeResult>
```


Use this data source to get authentication information about the current
auth scope in use. This can be used as self-discovery or introspection of
the username or project name currently in use.

<h2 class="pdoc-module-header" id="getEndpoint">
<a class="pdoc-member-name" href="/identity/getEndpoint.ts#L11">function getEndpoint</a>
</h2>

```typescript
getEndpoint(args?: GetEndpointArgs, opts?: pulumi.InvokeOptions): Promise<GetEndpointResult>
```


Use this data source to get the ID of an OpenStack endpoint.

Note: This usually requires admin privileges.

<h2 class="pdoc-module-header" id="getGroup">
<a class="pdoc-member-name" href="/identity/getGroup.ts#L11">function getGroup</a>
</h2>

```typescript
getGroup(args: GetGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetGroupResult>
```


Use this data source to get the ID of an OpenStack group.

Note: This usually requires admin privileges.

<h2 class="pdoc-module-header" id="getProject">
<a class="pdoc-member-name" href="/identity/getProject.ts#L9">function getProject</a>
</h2>

```typescript
getProject(args?: GetProjectArgs, opts?: pulumi.InvokeOptions): Promise<GetProjectResult>
```


Use this data source to get the ID of an OpenStack project.

<h2 class="pdoc-module-header" id="getRole">
<a class="pdoc-member-name" href="/identity/getRole.ts#L9">function getRole</a>
</h2>

```typescript
getRole(args: GetRoleArgs, opts?: pulumi.InvokeOptions): Promise<GetRoleResult>
```


Use this data source to get the ID of an OpenStack role.

<h2 class="pdoc-module-header" id="getUser">
<a class="pdoc-member-name" href="/identity/getUser.ts#L9">function getUser</a>
</h2>

```typescript
getUser(args?: GetUserArgs, opts?: pulumi.InvokeOptions): Promise<GetUserResult>
```


Use this data source to get the ID of an OpenStack user.

<h2 class="pdoc-module-header" id="GetAuthScopeArgs">
<a class="pdoc-member-name" href="/identity/getAuthScope.ts#L21">interface GetAuthScopeArgs</a>
</h2>

A collection of arguments for invoking getAuthScope.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getAuthScope.ts#L26">property name</a>
</h3>

```typescript
name: string;
```


The name of the scope. This is an arbitrary name which is
only used as a unique identifier so an actual token isn't used as the ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getAuthScope.ts#L32">property region</a>
</h3>

```typescript
region?: string;
```


The region in which to obtain the V3 Identity client.
A Identity client is needed to retrieve tokens IDs. If omitted, the
`region` argument of the provider is used.

<h2 class="pdoc-module-header" id="GetAuthScopeResult">
<a class="pdoc-member-name" href="/identity/getAuthScope.ts#L38">interface GetAuthScopeResult</a>
</h2>

A collection of values returned by getAuthScope.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getAuthScope.ts#L79">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getAuthScope.ts#L42">property projectDomainId</a>
</h3>

```typescript
projectDomainId: string;
```


The domain ID of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getAuthScope.ts#L46">property projectDomainName</a>
</h3>

```typescript
projectDomainName: string;
```


The domain name of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getAuthScope.ts#L50">property projectId</a>
</h3>

```typescript
projectId: string;
```


The project ID of the scope.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getAuthScope.ts#L54">property projectName</a>
</h3>

```typescript
projectName: string;
```


The project name of the scope.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getAuthScope.ts#L55">property region</a>
</h3>

```typescript
region: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getAuthScope.ts#L59">property roles</a>
</h3>

```typescript
roles: { ... }[];
```


A list of roles in the current scope. See reference below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getAuthScope.ts#L63">property userDomainId</a>
</h3>

```typescript
userDomainId: string;
```


The domain ID of the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getAuthScope.ts#L67">property userDomainName</a>
</h3>

```typescript
userDomainName: string;
```


The domain name of the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getAuthScope.ts#L71">property userId</a>
</h3>

```typescript
userId: string;
```


The user ID the of the scope.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getAuthScope.ts#L75">property userName</a>
</h3>

```typescript
userName: string;
```


The username of the scope.

<h2 class="pdoc-module-header" id="GetEndpointArgs">
<a class="pdoc-member-name" href="/identity/getEndpoint.ts#L24">interface GetEndpointArgs</a>
</h2>

A collection of arguments for invoking getEndpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getEndpoint.ts#L29">property interface</a>
</h3>

```typescript
interface?: string;
```


The endpoint interface. Valid values are `public`,
`internal`, and `admin`. Default value is `public`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getEndpoint.ts#L33">property region</a>
</h3>

```typescript
region?: string;
```


The region the endpoint is located in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getEndpoint.ts#L37">property serviceId</a>
</h3>

```typescript
serviceId?: string;
```


The service id this endpoint belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getEndpoint.ts#L41">property serviceName</a>
</h3>

```typescript
serviceName?: string;
```


The service name of the endpoint.

<h2 class="pdoc-module-header" id="GetEndpointResult">
<a class="pdoc-member-name" href="/identity/getEndpoint.ts#L47">interface GetEndpointResult</a>
</h2>

A collection of values returned by getEndpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getEndpoint.ts#L59">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getEndpoint.ts#L51">property region</a>
</h3>

```typescript
region: string;
```


The region the endpoint is located in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getEndpoint.ts#L55">property url</a>
</h3>

```typescript
url: string;
```


The endpoint URL

<h2 class="pdoc-module-header" id="GetGroupArgs">
<a class="pdoc-member-name" href="/identity/getGroup.ts#L22">interface GetGroupArgs</a>
</h2>

A collection of arguments for invoking getGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getGroup.ts#L26">property domainId</a>
</h3>

```typescript
domainId?: string;
```


The domain the group belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getGroup.ts#L30">property name</a>
</h3>

```typescript
name: string;
```


The name of the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getGroup.ts#L35">property region</a>
</h3>

```typescript
region?: string;
```


The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used.

<h2 class="pdoc-module-header" id="GetGroupResult">
<a class="pdoc-member-name" href="/identity/getGroup.ts#L41">interface GetGroupResult</a>
</h2>

A collection of values returned by getGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getGroup.ts#L45">property domainId</a>
</h3>

```typescript
domainId: string;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getGroup.ts#L53">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getGroup.ts#L49">property region</a>
</h3>

```typescript
region: string;
```


See Argument Reference above.

<h2 class="pdoc-module-header" id="GetProjectArgs">
<a class="pdoc-member-name" href="/identity/getProject.ts#L24">interface GetProjectArgs</a>
</h2>

A collection of arguments for invoking getProject.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getProject.ts#L28">property domainId</a>
</h3>

```typescript
domainId?: string;
```


The domain this project belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getProject.ts#L33">property enabled</a>
</h3>

```typescript
enabled?: boolean;
```


Whether the project is enabled or disabled. Valid
values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getProject.ts#L38">property isDomain</a>
</h3>

```typescript
isDomain?: boolean;
```


Whether this project is a domain. Valid values
are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getProject.ts#L42">property name</a>
</h3>

```typescript
name?: string;
```


The name of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getProject.ts#L46">property parentId</a>
</h3>

```typescript
parentId?: string;
```


The parent of this project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getProject.ts#L47">property region</a>
</h3>

```typescript
region?: string;
```

<h2 class="pdoc-module-header" id="GetProjectResult">
<a class="pdoc-member-name" href="/identity/getProject.ts#L53">interface GetProjectResult</a>
</h2>

A collection of values returned by getProject.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getProject.ts#L57">property description</a>
</h3>

```typescript
description: string;
```


The description of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getProject.ts#L61">property domainId</a>
</h3>

```typescript
domainId: string;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getProject.ts#L69">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getProject.ts#L65">property region</a>
</h3>

```typescript
region: string;
```


The region the project is located in.

<h2 class="pdoc-module-header" id="GetRoleArgs">
<a class="pdoc-member-name" href="/identity/getRole.ts#L20">interface GetRoleArgs</a>
</h2>

A collection of arguments for invoking getRole.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getRole.ts#L24">property domainId</a>
</h3>

```typescript
domainId?: string;
```


The domain the role belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getRole.ts#L28">property name</a>
</h3>

```typescript
name: string;
```


The name of the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getRole.ts#L33">property region</a>
</h3>

```typescript
region?: string;
```


The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used.

<h2 class="pdoc-module-header" id="GetRoleResult">
<a class="pdoc-member-name" href="/identity/getRole.ts#L39">interface GetRoleResult</a>
</h2>

A collection of values returned by getRole.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getRole.ts#L43">property domainId</a>
</h3>

```typescript
domainId: string;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getRole.ts#L51">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getRole.ts#L47">property region</a>
</h3>

```typescript
region: string;
```


See Argument Reference above.

<h2 class="pdoc-module-header" id="GetUserArgs">
<a class="pdoc-member-name" href="/identity/getUser.ts#L26">interface GetUserArgs</a>
</h2>

A collection of arguments for invoking getUser.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getUser.ts#L30">property domainId</a>
</h3>

```typescript
domainId?: string;
```


The domain this user belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getUser.ts#L35">property enabled</a>
</h3>

```typescript
enabled?: boolean;
```


Whether the user is enabled or disabled. Valid
values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getUser.ts#L39">property idpId</a>
</h3>

```typescript
idpId?: string;
```


The identity provider ID of the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getUser.ts#L43">property name</a>
</h3>

```typescript
name?: string;
```


The name of the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getUser.ts#L47">property passwordExpiresAt</a>
</h3>

```typescript
passwordExpiresAt?: string;
```


Query for expired passwords. See the [OpenStack API docs](https://developer.openstack.org/api-ref/identity/v3/#list-users) for more information on the query format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getUser.ts#L51">property protocolId</a>
</h3>

```typescript
protocolId?: string;
```


The protocol ID of the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getUser.ts#L52">property region</a>
</h3>

```typescript
region?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getUser.ts#L56">property uniqueId</a>
</h3>

```typescript
uniqueId?: string;
```


The unique ID of the user.

<h2 class="pdoc-module-header" id="GetUserResult">
<a class="pdoc-member-name" href="/identity/getUser.ts#L62">interface GetUserResult</a>
</h2>

A collection of values returned by getUser.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getUser.ts#L66">property defaultProjectId</a>
</h3>

```typescript
defaultProjectId: string;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getUser.ts#L70">property domainId</a>
</h3>

```typescript
domainId: string;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getUser.ts#L78">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/getUser.ts#L74">property region</a>
</h3>

```typescript
region: string;
```


The region the user is located in.

<h2 class="pdoc-module-header" id="ProjectArgs">
<a class="pdoc-member-name" href="/identity/project.ts#L132">interface ProjectArgs</a>
</h2>

The set of arguments for constructing a Project resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L136">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L140">property domainId</a>
</h3>

```typescript
domainId?: pulumi.Input<string>;
```


The domain this project belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L145">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Whether the project is enabled or disabled. Valid
values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L150">property isDomain</a>
</h3>

```typescript
isDomain?: pulumi.Input<boolean>;
```


Whether this project is a domain. Valid values
are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L154">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L158">property parentId</a>
</h3>

```typescript
parentId?: pulumi.Input<string>;
```


The parent of this project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L164">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new User.

<h2 class="pdoc-module-header" id="ProjectState">
<a class="pdoc-member-name" href="/identity/project.ts#L94">interface ProjectState</a>
</h2>

Input properties used for looking up and filtering Project resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L98">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L102">property domainId</a>
</h3>

```typescript
domainId?: pulumi.Input<string>;
```


The domain this project belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L107">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Whether the project is enabled or disabled. Valid
values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L112">property isDomain</a>
</h3>

```typescript
isDomain?: pulumi.Input<boolean>;
```


Whether this project is a domain. Valid values
are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L116">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L120">property parentId</a>
</h3>

```typescript
parentId?: pulumi.Input<string>;
```


The parent of this project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/project.ts#L126">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new User.

<h2 class="pdoc-module-header" id="RoleArgs">
<a class="pdoc-member-name" href="/identity/role.ts#L88">interface RoleArgs</a>
</h2>

The set of arguments for constructing a Role resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/role.ts#L92">property domainId</a>
</h3>

```typescript
domainId?: pulumi.Input<string>;
```


The domain the role belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/role.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/role.ts#L102">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new Role.

<h2 class="pdoc-module-header" id="RoleAssignmentArgs">
<a class="pdoc-member-name" href="/identity/roleAssignment.ts#L107">interface RoleAssignmentArgs</a>
</h2>

The set of arguments for constructing a RoleAssignment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/roleAssignment.ts#L111">property domainId</a>
</h3>

```typescript
domainId?: pulumi.Input<string>;
```


The domain to assign the role in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/roleAssignment.ts#L115">property groupId</a>
</h3>

```typescript
groupId?: pulumi.Input<string>;
```


The group to assign the role to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/roleAssignment.ts#L119">property projectId</a>
</h3>

```typescript
projectId?: pulumi.Input<string>;
```


The project to assign the role in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/roleAssignment.ts#L123">property roleId</a>
</h3>

```typescript
roleId: pulumi.Input<string>;
```


The role to assign.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/roleAssignment.ts#L127">property userId</a>
</h3>

```typescript
userId?: pulumi.Input<string>;
```


The user to assign the role to.

<h2 class="pdoc-module-header" id="RoleAssignmentState">
<a class="pdoc-member-name" href="/identity/roleAssignment.ts#L81">interface RoleAssignmentState</a>
</h2>

Input properties used for looking up and filtering RoleAssignment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/roleAssignment.ts#L85">property domainId</a>
</h3>

```typescript
domainId?: pulumi.Input<string>;
```


The domain to assign the role in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/roleAssignment.ts#L89">property groupId</a>
</h3>

```typescript
groupId?: pulumi.Input<string>;
```


The group to assign the role to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/roleAssignment.ts#L93">property projectId</a>
</h3>

```typescript
projectId?: pulumi.Input<string>;
```


The project to assign the role in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/roleAssignment.ts#L97">property roleId</a>
</h3>

```typescript
roleId?: pulumi.Input<string>;
```


The role to assign.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/roleAssignment.ts#L101">property userId</a>
</h3>

```typescript
userId?: pulumi.Input<string>;
```


The user to assign the role to.

<h2 class="pdoc-module-header" id="RoleState">
<a class="pdoc-member-name" href="/identity/role.ts#L68">interface RoleState</a>
</h2>

Input properties used for looking up and filtering Role resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/role.ts#L72">property domainId</a>
</h3>

```typescript
domainId?: pulumi.Input<string>;
```


The domain the role belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/role.ts#L76">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/role.ts#L82">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new Role.

<h2 class="pdoc-module-header" id="UserArgs">
<a class="pdoc-member-name" href="/identity/user.ts#L204">interface UserArgs</a>
</h2>

The set of arguments for constructing a User resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L208">property defaultProjectId</a>
</h3>

```typescript
defaultProjectId?: pulumi.Input<string>;
```


The default project this user belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L212">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L216">property domainId</a>
</h3>

```typescript
domainId?: pulumi.Input<string>;
```


The domain this user belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L221">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Whether the user is enabled or disabled. Valid
values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L225">property extra</a>
</h3>

```typescript
extra?: pulumi.Input<{ ... }>;
```


Free-form key/value pairs of extra information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L230">property ignoreChangePasswordUponFirstUse</a>
</h3>

```typescript
ignoreChangePasswordUponFirstUse?: pulumi.Input<boolean>;
```


User will not have to
change their password upon first use. Valid values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L235">property ignoreLockoutFailureAttempts</a>
</h3>

```typescript
ignoreLockoutFailureAttempts?: pulumi.Input<boolean>;
```


User will not have a failure
lockout placed on their account. Valid values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L240">property ignorePasswordExpiry</a>
</h3>

```typescript
ignorePasswordExpiry?: pulumi.Input<boolean>;
```


User's password will not expire.
Valid values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L245">property multiFactorAuthEnabled</a>
</h3>

```typescript
multiFactorAuthEnabled?: pulumi.Input<boolean>;
```


Whether to enable multi-factor
authentication. Valid values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L252">property multiFactorAuthRules</a>
</h3>

```typescript
multiFactorAuthRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A multi-factor authentication rule.
The structure is documented below. Please see the
[Ocata release notes](https://docs.openstack.org/releasenotes/keystone/ocata.html)
for more information on how to use mulit-factor rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L256">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L260">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


The password for the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L266">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new User.

<h2 class="pdoc-module-header" id="UserState">
<a class="pdoc-member-name" href="/identity/user.ts#L136">interface UserState</a>
</h2>

Input properties used for looking up and filtering User resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L140">property defaultProjectId</a>
</h3>

```typescript
defaultProjectId?: pulumi.Input<string>;
```


The default project this user belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L144">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L148">property domainId</a>
</h3>

```typescript
domainId?: pulumi.Input<string>;
```


The domain this user belongs to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L153">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Whether the user is enabled or disabled. Valid
values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L157">property extra</a>
</h3>

```typescript
extra?: pulumi.Input<{ ... }>;
```


Free-form key/value pairs of extra information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L162">property ignoreChangePasswordUponFirstUse</a>
</h3>

```typescript
ignoreChangePasswordUponFirstUse?: pulumi.Input<boolean>;
```


User will not have to
change their password upon first use. Valid values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L167">property ignoreLockoutFailureAttempts</a>
</h3>

```typescript
ignoreLockoutFailureAttempts?: pulumi.Input<boolean>;
```


User will not have a failure
lockout placed on their account. Valid values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L172">property ignorePasswordExpiry</a>
</h3>

```typescript
ignorePasswordExpiry?: pulumi.Input<boolean>;
```


User's password will not expire.
Valid values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L177">property multiFactorAuthEnabled</a>
</h3>

```typescript
multiFactorAuthEnabled?: pulumi.Input<boolean>;
```


Whether to enable multi-factor
authentication. Valid values are `true` and `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L184">property multiFactorAuthRules</a>
</h3>

```typescript
multiFactorAuthRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A multi-factor authentication rule.
The structure is documented below. Please see the
[Ocata release notes](https://docs.openstack.org/releasenotes/keystone/ocata.html)
for more information on how to use mulit-factor rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L188">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L192">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


The password for the user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/identity/user.ts#L198">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new User.

