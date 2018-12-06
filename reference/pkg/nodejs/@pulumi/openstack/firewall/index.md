---
title: Module firewall
---

<a href="../index.html">@pulumi/openstack</a> &gt; firewall

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Firewall">class Firewall</a>
* <a href="#Policy">class Policy</a>
* <a href="#Rule">class Rule</a>
* <a href="#getPolicy">function getPolicy</a>
* <a href="#FirewallArgs">interface FirewallArgs</a>
* <a href="#FirewallState">interface FirewallState</a>
* <a href="#GetPolicyArgs">interface GetPolicyArgs</a>
* <a href="#GetPolicyResult">interface GetPolicyResult</a>
* <a href="#PolicyArgs">interface PolicyArgs</a>
* <a href="#PolicyState">interface PolicyState</a>
* <a href="#RuleArgs">interface RuleArgs</a>
* <a href="#RuleState">interface RuleState</a>

<a href="/firewall/firewall.ts">firewall/firewall.ts</a> <a href="/firewall/getPolicy.ts">firewall/getPolicy.ts</a> <a href="/firewall/policy.ts">firewall/policy.ts</a> <a href="/firewall/rule.ts">firewall/rule.ts</a> 


<h2 class="pdoc-module-header" id="Firewall">
<a class="pdoc-member-name" href="/firewall/firewall.ts#L10">class Firewall</a>
</h2>

Manages a v1 firewall resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L72">constructor</a>
</h3>

```typescript
new Firewall(name: string, args: FirewallArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Firewall resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FirewallState, opts?: pulumi.CustomResourceOptions): Firewall
```


Get an existing Firewall resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/firewall/firewall.ts#L28">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean | undefined>;
```


Administrative up/down status for the firewall
(must be "true" or "false" if provided - defaults to "true").
Changing this updates the `admin_state_up` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L34">property associatedRouters</a>
</h3>

```typescript
public associatedRouters: pulumi.Output<string[]>;
```


Router(s) to associate this firewall instance
with. Must be a list of strings. Changing this updates the associated routers
of an existing firewall. Conflicts with `no_routers`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L39">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description for the firewall. Changing this
updates the `description` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A name for the firewall. Changing this
updates the `name` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L50">property noRouters</a>
</h3>

```typescript
public noRouters: pulumi.Output<boolean | undefined>;
```


Should this firewall not be associated with any routers
(must be "true" or "false" if provide - defaults to "false").
Conflicts with `associated_routers`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L55">property policyId</a>
</h3>

```typescript
public policyId: pulumi.Output<string>;
```


The policy resource id for the firewall. Changing
this updates the `policy_id` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L62">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L68">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The owner of the floating IP. Required if admin wants
to create a firewall for another tenant. Changing this creates a new
firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L72">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="Policy">
<a class="pdoc-member-name" href="/firewall/policy.ts#L10">class Policy</a>
</h2>

Manages a v1 firewall policy resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L66">constructor</a>
</h3>

```typescript
new Policy(name: string, args?: PolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Policy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyState, opts?: pulumi.CustomResourceOptions): Policy
```


Get an existing Policy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/firewall/policy.ts#L30">property audited</a>
</h3>

```typescript
public audited: pulumi.Output<boolean | undefined>;
```


Audit status of the firewall policy
(must be "true" or "false" if provided - defaults to "false").
This status is set to "false" whenever the firewall policy or any of its
rules are changed. Changing this updates the `audited` status of an existing
firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L35">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description for the firewall policy. Changing
this updates the `description` of an existing firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L40">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A name for the firewall policy. Changing this
updates the `name` of an existing firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L47">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall policy. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L53">property rules</a>
</h3>

```typescript
public rules: pulumi.Output<string[] | undefined>;
```


An array of one or more firewall rules that comprise
the policy. Changing this results in adding/removing rules from the
existing firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L61">property shared</a>
</h3>

```typescript
public shared: pulumi.Output<boolean | undefined>;
```


Sharing status of the firewall policy (must be "true"
or "false" if provided). If this is "true" the policy is visible to, and
can be used in, firewalls in other tenants. Changing this updates the
`shared` status of an existing firewall policy. Only administrative users
can specify if the policy should be shared.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L62">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L66">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="Rule">
<a class="pdoc-member-name" href="/firewall/rule.ts#L10">class Rule</a>
</h2>

Manages a v1 firewall rule resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L96">constructor</a>
</h3>

```typescript
new Rule(name: string, args: RuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Rule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RuleState, opts?: pulumi.CustomResourceOptions): Rule
```


Get an existing Rule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/firewall/rule.ts#L28">property action</a>
</h3>

```typescript
public action: pulumi.Output<string>;
```


Action to be taken ( must be "allow" or "deny") when the
firewall rule matches. Changing this updates the `action` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L33">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description for the firewall rule. Changing this
updates the `description` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L39">property destinationIpAddress</a>
</h3>

```typescript
public destinationIpAddress: pulumi.Output<string | undefined>;
```


The destination IP address on which the
firewall rule operates. Changing this updates the `destination_ip_address`
of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L45">property destinationPort</a>
</h3>

```typescript
public destinationPort: pulumi.Output<string | undefined>;
```


The destination port on which the firewall
rule operates. Changing this updates the `destination_port` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L51">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Enabled status for the firewall rule (must be "true"
or "false" if provided - defaults to "true"). Changing this updates the
`enabled` status of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L56">property ipVersion</a>
</h3>

```typescript
public ipVersion: pulumi.Output<number | undefined>;
```


IP version, either 4 (default) or 6. Changing this
updates the `ip_version` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L61">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the firewall rule. Changing this
updates the `name` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L67">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The protocol type on which the firewall rule operates.
Valid values are: `tcp`, `udp`, `icmp`, and `any`. Changing this updates the
`protocol` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L74">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the v1 Compute client.
A Compute client is needed to create a firewall rule. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L80">property sourceIpAddress</a>
</h3>

```typescript
public sourceIpAddress: pulumi.Output<string | undefined>;
```


The source IP address on which the firewall
rule operates. Changing this updates the `source_ip_address` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L86">property sourcePort</a>
</h3>

```typescript
public sourcePort: pulumi.Output<string | undefined>;
```


The source port on which the firewall
rule operates. Changing this updates the `source_port` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L92">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string | undefined>;
```


The owner of the firewall rule. Required if admin
wants to create a firewall rule for another tenant. Changing this creates a
new firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L96">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="getPolicy">
<a class="pdoc-member-name" href="/firewall/getPolicy.ts#L10">function getPolicy</a>
</h2>

```typescript
getPolicy(args?: GetPolicyArgs, opts?: pulumi.InvokeOptions): Promise<GetPolicyResult>
```


Use this data source to get firewall policy information of an available OpenStack firewall policy.

<h2 class="pdoc-module-header" id="FirewallArgs">
<a class="pdoc-member-name" href="/firewall/firewall.ts#L173">interface FirewallArgs</a>
</h2>

The set of arguments for constructing a Firewall resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L179">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


Administrative up/down status for the firewall
(must be "true" or "false" if provided - defaults to "true").
Changing this updates the `admin_state_up` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L185">property associatedRouters</a>
</h3>

```typescript
associatedRouters?: pulumi.Input<pulumi.Input<string>[]>;
```


Router(s) to associate this firewall instance
with. Must be a list of strings. Changing this updates the associated routers
of an existing firewall. Conflicts with `no_routers`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L190">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the firewall. Changing this
updates the `description` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L195">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the firewall. Changing this
updates the `name` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L201">property noRouters</a>
</h3>

```typescript
noRouters?: pulumi.Input<boolean>;
```


Should this firewall not be associated with any routers
(must be "true" or "false" if provide - defaults to "false").
Conflicts with `associated_routers`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L206">property policyId</a>
</h3>

```typescript
policyId: pulumi.Input<string>;
```


The policy resource id for the firewall. Changing
this updates the `policy_id` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L213">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L219">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the floating IP. Required if admin wants
to create a firewall for another tenant. Changing this creates a new
firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L223">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="FirewallState">
<a class="pdoc-member-name" href="/firewall/firewall.ts#L117">interface FirewallState</a>
</h2>

Input properties used for looking up and filtering Firewall resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L123">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


Administrative up/down status for the firewall
(must be "true" or "false" if provided - defaults to "true").
Changing this updates the `admin_state_up` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L129">property associatedRouters</a>
</h3>

```typescript
associatedRouters?: pulumi.Input<pulumi.Input<string>[]>;
```


Router(s) to associate this firewall instance
with. Must be a list of strings. Changing this updates the associated routers
of an existing firewall. Conflicts with `no_routers`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L134">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the firewall. Changing this
updates the `description` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L139">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the firewall. Changing this
updates the `name` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L145">property noRouters</a>
</h3>

```typescript
noRouters?: pulumi.Input<boolean>;
```


Should this firewall not be associated with any routers
(must be "true" or "false" if provide - defaults to "false").
Conflicts with `associated_routers`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L150">property policyId</a>
</h3>

```typescript
policyId?: pulumi.Input<string>;
```


The policy resource id for the firewall. Changing
this updates the `policy_id` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L157">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L163">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the floating IP. Required if admin wants
to create a firewall for another tenant. Changing this creates a new
firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L167">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="GetPolicyArgs">
<a class="pdoc-member-name" href="/firewall/getPolicy.ts#L23">interface GetPolicyArgs</a>
</h2>

A collection of arguments for invoking getPolicy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L27">property name</a>
</h3>

```typescript
name?: string;
```


The name of the firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L31">property policyId</a>
</h3>

```typescript
policyId?: string;
```


The ID of the firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L37">property region</a>
</h3>

```typescript
region?: string;
```


The region in which to obtain the V2 Neutron client.
A Neutron client is needed to retrieve firewall policy ids. If omitted, the
`region` argument of the provider is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L41">property tenantId</a>
</h3>

```typescript
tenantId?: string;
```


The owner of the firewall policy.

<h2 class="pdoc-module-header" id="GetPolicyResult">
<a class="pdoc-member-name" href="/firewall/getPolicy.ts#L47">interface GetPolicyResult</a>
</h2>

A collection of values returned by getPolicy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L51">property audited</a>
</h3>

```typescript
audited: boolean;
```


The audit status of the firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L55">property description</a>
</h3>

```typescript
description: string;
```


The description of the firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L75">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L59">property region</a>
</h3>

```typescript
region: string;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L63">property rules</a>
</h3>

```typescript
rules: string[];
```


The array of one or more firewall rules that comprise the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L67">property shared</a>
</h3>

```typescript
shared: boolean;
```


The sharing status of the firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L71">property tenantId</a>
</h3>

```typescript
tenantId: string;
```


See Argument Reference above.

<h2 class="pdoc-module-header" id="PolicyArgs">
<a class="pdoc-member-name" href="/firewall/policy.ts#L156">interface PolicyArgs</a>
</h2>

The set of arguments for constructing a Policy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L164">property audited</a>
</h3>

```typescript
audited?: pulumi.Input<boolean>;
```


Audit status of the firewall policy
(must be "true" or "false" if provided - defaults to "false").
This status is set to "false" whenever the firewall policy or any of its
rules are changed. Changing this updates the `audited` status of an existing
firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L169">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the firewall policy. Changing
this updates the `description` of an existing firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L174">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the firewall policy. Changing this
updates the `name` of an existing firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L181">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall policy. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L187">property rules</a>
</h3>

```typescript
rules?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of one or more firewall rules that comprise
the policy. Changing this results in adding/removing rules from the
existing firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L195">property shared</a>
</h3>

```typescript
shared?: pulumi.Input<boolean>;
```


Sharing status of the firewall policy (must be "true"
or "false" if provided). If this is "true" the policy is visible to, and
can be used in, firewalls in other tenants. Changing this updates the
`shared` status of an existing firewall policy. Only administrative users
can specify if the policy should be shared.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L196">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L200">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="PolicyState">
<a class="pdoc-member-name" href="/firewall/policy.ts#L106">interface PolicyState</a>
</h2>

Input properties used for looking up and filtering Policy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L114">property audited</a>
</h3>

```typescript
audited?: pulumi.Input<boolean>;
```


Audit status of the firewall policy
(must be "true" or "false" if provided - defaults to "false").
This status is set to "false" whenever the firewall policy or any of its
rules are changed. Changing this updates the `audited` status of an existing
firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L119">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the firewall policy. Changing
this updates the `description` of an existing firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L124">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the firewall policy. Changing this
updates the `name` of an existing firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L131">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall policy. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L137">property rules</a>
</h3>

```typescript
rules?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of one or more firewall rules that comprise
the policy. Changing this results in adding/removing rules from the
existing firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L145">property shared</a>
</h3>

```typescript
shared?: pulumi.Input<boolean>;
```


Sharing status of the firewall policy (must be "true"
or "false" if provided). If this is "true" the policy is visible to, and
can be used in, firewalls in other tenants. Changing this updates the
`shared` status of an existing firewall policy. Only administrative users
can specify if the policy should be shared.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L146">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L150">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="RuleArgs">
<a class="pdoc-member-name" href="/firewall/rule.ts#L232">interface RuleArgs</a>
</h2>

The set of arguments for constructing a Rule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L238">property action</a>
</h3>

```typescript
action: pulumi.Input<string>;
```


Action to be taken ( must be "allow" or "deny") when the
firewall rule matches. Changing this updates the `action` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L243">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the firewall rule. Changing this
updates the `description` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L249">property destinationIpAddress</a>
</h3>

```typescript
destinationIpAddress?: pulumi.Input<string>;
```


The destination IP address on which the
firewall rule operates. Changing this updates the `destination_ip_address`
of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L255">property destinationPort</a>
</h3>

```typescript
destinationPort?: pulumi.Input<string>;
```


The destination port on which the firewall
rule operates. Changing this updates the `destination_port` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L261">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Enabled status for the firewall rule (must be "true"
or "false" if provided - defaults to "true"). Changing this updates the
`enabled` status of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L266">property ipVersion</a>
</h3>

```typescript
ipVersion?: pulumi.Input<number>;
```


IP version, either 4 (default) or 6. Changing this
updates the `ip_version` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L271">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the firewall rule. Changing this
updates the `name` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L277">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The protocol type on which the firewall rule operates.
Valid values are: `tcp`, `udp`, `icmp`, and `any`. Changing this updates the
`protocol` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L284">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the v1 Compute client.
A Compute client is needed to create a firewall rule. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L290">property sourceIpAddress</a>
</h3>

```typescript
sourceIpAddress?: pulumi.Input<string>;
```


The source IP address on which the firewall
rule operates. Changing this updates the `source_ip_address` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L296">property sourcePort</a>
</h3>

```typescript
sourcePort?: pulumi.Input<string>;
```


The source port on which the firewall
rule operates. Changing this updates the `source_port` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L302">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the firewall rule. Required if admin
wants to create a firewall rule for another tenant. Changing this creates a
new firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L306">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="RuleState">
<a class="pdoc-member-name" href="/firewall/rule.ts#L152">interface RuleState</a>
</h2>

Input properties used for looking up and filtering Rule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L158">property action</a>
</h3>

```typescript
action?: pulumi.Input<string>;
```


Action to be taken ( must be "allow" or "deny") when the
firewall rule matches. Changing this updates the `action` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L163">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the firewall rule. Changing this
updates the `description` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L169">property destinationIpAddress</a>
</h3>

```typescript
destinationIpAddress?: pulumi.Input<string>;
```


The destination IP address on which the
firewall rule operates. Changing this updates the `destination_ip_address`
of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L175">property destinationPort</a>
</h3>

```typescript
destinationPort?: pulumi.Input<string>;
```


The destination port on which the firewall
rule operates. Changing this updates the `destination_port` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L181">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Enabled status for the firewall rule (must be "true"
or "false" if provided - defaults to "true"). Changing this updates the
`enabled` status of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L186">property ipVersion</a>
</h3>

```typescript
ipVersion?: pulumi.Input<number>;
```


IP version, either 4 (default) or 6. Changing this
updates the `ip_version` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L191">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the firewall rule. Changing this
updates the `name` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L197">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The protocol type on which the firewall rule operates.
Valid values are: `tcp`, `udp`, `icmp`, and `any`. Changing this updates the
`protocol` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L204">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the v1 Compute client.
A Compute client is needed to create a firewall rule. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L210">property sourceIpAddress</a>
</h3>

```typescript
sourceIpAddress?: pulumi.Input<string>;
```


The source IP address on which the firewall
rule operates. Changing this updates the `source_ip_address` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L216">property sourcePort</a>
</h3>

```typescript
sourcePort?: pulumi.Input<string>;
```


The source port on which the firewall
rule operates. Changing this updates the `source_port` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L222">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the firewall rule. Required if admin
wants to create a firewall rule for another tenant. Changing this creates a
new firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L226">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

