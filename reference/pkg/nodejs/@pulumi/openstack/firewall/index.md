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
<a class="pdoc-member-name" href="/firewall/firewall.ts#L9">class Firewall</a>
</h2>

Manages a v1 firewall resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L71">constructor</a>
</h3>

```typescript
new Firewall(name: string, args: FirewallArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Firewall resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FirewallState): Firewall
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
<a class="pdoc-child-name" href="/firewall/firewall.ts#L27">property adminStateUp</a>
</h3>

```typescript
public adminStateUp: pulumi.Output<boolean | undefined>;
```


Administrative up/down status for the firewall
(must be "true" or "false" if provided - defaults to "true").
Changing this updates the `admin_state_up` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L33">property associatedRouters</a>
</h3>

```typescript
public associatedRouters: pulumi.Output<string[]>;
```


Router(s) to associate this firewall instance
with. Must be a list of strings. Changing this updates the associated routers
of an existing firewall. Conflicts with `no_routers`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L38">property description</a>
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
<a class="pdoc-child-name" href="/firewall/firewall.ts#L43">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A name for the firewall. Changing this
updates the `name` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L49">property noRouters</a>
</h3>

```typescript
public noRouters: pulumi.Output<boolean | undefined>;
```


Should this firewall not be associated with any routers
(must be "true" or "false" if provide - defaults to "false").
Conflicts with `associated_routers`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L54">property policyId</a>
</h3>

```typescript
public policyId: pulumi.Output<string>;
```


The policy resource id for the firewall. Changing
this updates the `policy_id` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L61">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L67">property tenantId</a>
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
<a class="pdoc-child-name" href="/firewall/firewall.ts#L71">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="Policy">
<a class="pdoc-member-name" href="/firewall/policy.ts#L9">class Policy</a>
</h2>

Manages a v1 firewall policy resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L65">constructor</a>
</h3>

```typescript
new Policy(name: string, args?: PolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Policy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyState): Policy
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
<a class="pdoc-child-name" href="/firewall/policy.ts#L29">property audited</a>
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
<a class="pdoc-child-name" href="/firewall/policy.ts#L34">property description</a>
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
<a class="pdoc-child-name" href="/firewall/policy.ts#L39">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A name for the firewall policy. Changing this
updates the `name` of an existing firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L46">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall policy. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L52">property rules</a>
</h3>

```typescript
public rules: pulumi.Output<string[] | undefined>;
```


An array of one or more firewall rules that comprise
the policy. Changing this results in adding/removing rules from the
existing firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L60">property shared</a>
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
<a class="pdoc-child-name" href="/firewall/policy.ts#L61">property tenantId</a>
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
<a class="pdoc-child-name" href="/firewall/policy.ts#L65">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="Rule">
<a class="pdoc-member-name" href="/firewall/rule.ts#L9">class Rule</a>
</h2>

Manages a v1 firewall rule resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L95">constructor</a>
</h3>

```typescript
new Rule(name: string, args: RuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Rule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RuleState): Rule
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
<a class="pdoc-child-name" href="/firewall/rule.ts#L27">property action</a>
</h3>

```typescript
public action: pulumi.Output<string>;
```


Action to be taken ( must be "allow" or "deny") when the
firewall rule matches. Changing this updates the `action` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L32">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description for the firewall rule. Changing this
updates the `description` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L38">property destinationIpAddress</a>
</h3>

```typescript
public destinationIpAddress: pulumi.Output<string | undefined>;
```


The destination IP address on which the
firewall rule operates. Changing this updates the `destination_ip_address`
of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L44">property destinationPort</a>
</h3>

```typescript
public destinationPort: pulumi.Output<string | undefined>;
```


The destination port on which the firewall
rule operates. Changing this updates the `destination_port` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L50">property enabled</a>
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
<a class="pdoc-child-name" href="/firewall/rule.ts#L55">property ipVersion</a>
</h3>

```typescript
public ipVersion: pulumi.Output<number | undefined>;
```


IP version, either 4 (default) or 6. Changing this
updates the `ip_version` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L60">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the firewall rule. Changing this
updates the `name` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L66">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The protocol type on which the firewall rule operates.
Valid values are: `tcp`, `udp`, `icmp`, and `any`. Changing this updates the
`protocol` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L73">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the v1 Compute client.
A Compute client is needed to create a firewall rule. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L79">property sourceIpAddress</a>
</h3>

```typescript
public sourceIpAddress: pulumi.Output<string | undefined>;
```


The source IP address on which the firewall
rule operates. Changing this updates the `source_ip_address` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L85">property sourcePort</a>
</h3>

```typescript
public sourcePort: pulumi.Output<string | undefined>;
```


The source port on which the firewall
rule operates. Changing this updates the `source_port` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L91">property tenantId</a>
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
<a class="pdoc-child-name" href="/firewall/rule.ts#L95">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="getPolicy">
<a class="pdoc-member-name" href="/firewall/getPolicy.ts#L9">function getPolicy</a>
</h2>

```typescript
getPolicy(args?: GetPolicyArgs, opts?: pulumi.InvokeOptions): Promise<GetPolicyResult>
```


Use this data source to get firewall policy information of an available OpenStack firewall policy.

<h2 class="pdoc-module-header" id="FirewallArgs">
<a class="pdoc-member-name" href="/firewall/firewall.ts#L172">interface FirewallArgs</a>
</h2>

The set of arguments for constructing a Firewall resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L178">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


Administrative up/down status for the firewall
(must be "true" or "false" if provided - defaults to "true").
Changing this updates the `admin_state_up` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L184">property associatedRouters</a>
</h3>

```typescript
associatedRouters?: pulumi.Input<pulumi.Input<string>[]>;
```


Router(s) to associate this firewall instance
with. Must be a list of strings. Changing this updates the associated routers
of an existing firewall. Conflicts with `no_routers`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L189">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the firewall. Changing this
updates the `description` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L194">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the firewall. Changing this
updates the `name` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L200">property noRouters</a>
</h3>

```typescript
noRouters?: pulumi.Input<boolean>;
```


Should this firewall not be associated with any routers
(must be "true" or "false" if provide - defaults to "false").
Conflicts with `associated_routers`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L205">property policyId</a>
</h3>

```typescript
policyId: pulumi.Input<string>;
```


The policy resource id for the firewall. Changing
this updates the `policy_id` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L212">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L218">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the floating IP. Required if admin wants
to create a firewall for another tenant. Changing this creates a new
firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L222">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="FirewallState">
<a class="pdoc-member-name" href="/firewall/firewall.ts#L116">interface FirewallState</a>
</h2>

Input properties used for looking up and filtering Firewall resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L122">property adminStateUp</a>
</h3>

```typescript
adminStateUp?: pulumi.Input<boolean>;
```


Administrative up/down status for the firewall
(must be "true" or "false" if provided - defaults to "true").
Changing this updates the `admin_state_up` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L128">property associatedRouters</a>
</h3>

```typescript
associatedRouters?: pulumi.Input<pulumi.Input<string>[]>;
```


Router(s) to associate this firewall instance
with. Must be a list of strings. Changing this updates the associated routers
of an existing firewall. Conflicts with `no_routers`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L133">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the firewall. Changing this
updates the `description` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L138">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the firewall. Changing this
updates the `name` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L144">property noRouters</a>
</h3>

```typescript
noRouters?: pulumi.Input<boolean>;
```


Should this firewall not be associated with any routers
(must be "true" or "false" if provide - defaults to "false").
Conflicts with `associated_routers`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L149">property policyId</a>
</h3>

```typescript
policyId?: pulumi.Input<string>;
```


The policy resource id for the firewall. Changing
this updates the `policy_id` of an existing firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L156">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L162">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the floating IP. Required if admin wants
to create a firewall for another tenant. Changing this creates a new
firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/firewall.ts#L166">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="GetPolicyArgs">
<a class="pdoc-member-name" href="/firewall/getPolicy.ts#L22">interface GetPolicyArgs</a>
</h2>

A collection of arguments for invoking getPolicy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L26">property name</a>
</h3>

```typescript
name?: string;
```


The name of the firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L30">property policyId</a>
</h3>

```typescript
policyId?: string;
```


The ID of the firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L36">property region</a>
</h3>

```typescript
region?: string;
```


The region in which to obtain the V2 Neutron client.
A Neutron client is needed to retrieve firewall policy ids. If omitted, the
`region` argument of the provider is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L40">property tenantId</a>
</h3>

```typescript
tenantId?: string;
```


The owner of the firewall policy.

<h2 class="pdoc-module-header" id="GetPolicyResult">
<a class="pdoc-member-name" href="/firewall/getPolicy.ts#L46">interface GetPolicyResult</a>
</h2>

A collection of values returned by getPolicy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L50">property audited</a>
</h3>

```typescript
audited: boolean;
```


The audit status of the firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L54">property description</a>
</h3>

```typescript
description: string;
```


The description of the firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L74">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L58">property region</a>
</h3>

```typescript
region: string;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L62">property rules</a>
</h3>

```typescript
rules: string[];
```


The array of one or more firewall rules that comprise the policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L66">property shared</a>
</h3>

```typescript
shared: boolean;
```


The sharing status of the firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/getPolicy.ts#L70">property tenantId</a>
</h3>

```typescript
tenantId: string;
```


See Argument Reference above.

<h2 class="pdoc-module-header" id="PolicyArgs">
<a class="pdoc-member-name" href="/firewall/policy.ts#L155">interface PolicyArgs</a>
</h2>

The set of arguments for constructing a Policy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L163">property audited</a>
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
<a class="pdoc-child-name" href="/firewall/policy.ts#L168">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the firewall policy. Changing
this updates the `description` of an existing firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L173">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the firewall policy. Changing this
updates the `name` of an existing firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L180">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall policy. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L186">property rules</a>
</h3>

```typescript
rules?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of one or more firewall rules that comprise
the policy. Changing this results in adding/removing rules from the
existing firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L194">property shared</a>
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
<a class="pdoc-child-name" href="/firewall/policy.ts#L195">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L199">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="PolicyState">
<a class="pdoc-member-name" href="/firewall/policy.ts#L105">interface PolicyState</a>
</h2>

Input properties used for looking up and filtering Policy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L113">property audited</a>
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
<a class="pdoc-child-name" href="/firewall/policy.ts#L118">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the firewall policy. Changing
this updates the `description` of an existing firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L123">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for the firewall policy. Changing this
updates the `name` of an existing firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L130">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall policy. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L136">property rules</a>
</h3>

```typescript
rules?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of one or more firewall rules that comprise
the policy. Changing this results in adding/removing rules from the
existing firewall policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L144">property shared</a>
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
<a class="pdoc-child-name" href="/firewall/policy.ts#L145">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/policy.ts#L149">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="RuleArgs">
<a class="pdoc-member-name" href="/firewall/rule.ts#L231">interface RuleArgs</a>
</h2>

The set of arguments for constructing a Rule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L237">property action</a>
</h3>

```typescript
action: pulumi.Input<string>;
```


Action to be taken ( must be "allow" or "deny") when the
firewall rule matches. Changing this updates the `action` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L242">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the firewall rule. Changing this
updates the `description` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L248">property destinationIpAddress</a>
</h3>

```typescript
destinationIpAddress?: pulumi.Input<string>;
```


The destination IP address on which the
firewall rule operates. Changing this updates the `destination_ip_address`
of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L254">property destinationPort</a>
</h3>

```typescript
destinationPort?: pulumi.Input<string>;
```


The destination port on which the firewall
rule operates. Changing this updates the `destination_port` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L260">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Enabled status for the firewall rule (must be "true"
or "false" if provided - defaults to "true"). Changing this updates the
`enabled` status of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L265">property ipVersion</a>
</h3>

```typescript
ipVersion?: pulumi.Input<number>;
```


IP version, either 4 (default) or 6. Changing this
updates the `ip_version` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L270">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the firewall rule. Changing this
updates the `name` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L276">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The protocol type on which the firewall rule operates.
Valid values are: `tcp`, `udp`, `icmp`, and `any`. Changing this updates the
`protocol` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L283">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the v1 Compute client.
A Compute client is needed to create a firewall rule. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L289">property sourceIpAddress</a>
</h3>

```typescript
sourceIpAddress?: pulumi.Input<string>;
```


The source IP address on which the firewall
rule operates. Changing this updates the `source_ip_address` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L295">property sourcePort</a>
</h3>

```typescript
sourcePort?: pulumi.Input<string>;
```


The source port on which the firewall
rule operates. Changing this updates the `source_port` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L301">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the firewall rule. Required if admin
wants to create a firewall rule for another tenant. Changing this creates a
new firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L305">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="RuleState">
<a class="pdoc-member-name" href="/firewall/rule.ts#L151">interface RuleState</a>
</h2>

Input properties used for looking up and filtering Rule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L157">property action</a>
</h3>

```typescript
action?: pulumi.Input<string>;
```


Action to be taken ( must be "allow" or "deny") when the
firewall rule matches. Changing this updates the `action` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L162">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the firewall rule. Changing this
updates the `description` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L168">property destinationIpAddress</a>
</h3>

```typescript
destinationIpAddress?: pulumi.Input<string>;
```


The destination IP address on which the
firewall rule operates. Changing this updates the `destination_ip_address`
of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L174">property destinationPort</a>
</h3>

```typescript
destinationPort?: pulumi.Input<string>;
```


The destination port on which the firewall
rule operates. Changing this updates the `destination_port` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L180">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Enabled status for the firewall rule (must be "true"
or "false" if provided - defaults to "true"). Changing this updates the
`enabled` status of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L185">property ipVersion</a>
</h3>

```typescript
ipVersion?: pulumi.Input<number>;
```


IP version, either 4 (default) or 6. Changing this
updates the `ip_version` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L190">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the firewall rule. Changing this
updates the `name` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L196">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The protocol type on which the firewall rule operates.
Valid values are: `tcp`, `udp`, `icmp`, and `any`. Changing this updates the
`protocol` of an existing firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L203">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the v1 Compute client.
A Compute client is needed to create a firewall rule. If omitted, the
`region` argument of the provider is used. Changing this creates a new
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L209">property sourceIpAddress</a>
</h3>

```typescript
sourceIpAddress?: pulumi.Input<string>;
```


The source IP address on which the firewall
rule operates. Changing this updates the `source_ip_address` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L215">property sourcePort</a>
</h3>

```typescript
sourcePort?: pulumi.Input<string>;
```


The source port on which the firewall
rule operates. Changing this updates the `source_port` of an existing
firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L221">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The owner of the firewall rule. Required if admin
wants to create a firewall rule for another tenant. Changing this creates a
new firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/firewall/rule.ts#L225">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

