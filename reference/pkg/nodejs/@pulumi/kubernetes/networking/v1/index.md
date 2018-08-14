---
title: Module networking/v1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">networking</a> &gt; v1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isNetworkPolicy">function isNetworkPolicy</a>
* <a href="#isNetworkPolicyList">function isNetworkPolicyList</a>
* <a href="#IPBlock">interface IPBlock</a>
* <a href="#NetworkPolicy">interface NetworkPolicy</a>
* <a href="#NetworkPolicyEgressRule">interface NetworkPolicyEgressRule</a>
* <a href="#NetworkPolicyIngressRule">interface NetworkPolicyIngressRule</a>
* <a href="#NetworkPolicyList">interface NetworkPolicyList</a>
* <a href="#NetworkPolicyPeer">interface NetworkPolicyPeer</a>
* <a href="#NetworkPolicyPort">interface NetworkPolicyPort</a>
* <a href="#NetworkPolicySpec">interface NetworkPolicySpec</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isNetworkPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L15273">function isNetworkPolicy</a>
</h2>

```typescript
isNetworkPolicy(o: any): boolean
```

<h2 class="pdoc-module-header" id="isNetworkPolicyList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L15362">function isNetworkPolicyList</a>
</h2>

```typescript
isNetworkPolicyList(o: any): boolean
```

<h2 class="pdoc-module-header" id="IPBlock">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14428">interface IPBlock</a>
</h2>

IPBlock describes a particular CIDR (Ex. "192.168.1.1/24") that is allowed to the pods
matched by a NetworkPolicySpec's podSelector. The except entry describes CIDRs that should
not be included within this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14432">property cidr</a>
</h3>

```typescript
cidr: string;
```


CIDR is a string representing the IP Block Valid examples are "192.168.1.1/24"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14438">property except</a>
</h3>

```typescript
except: string[];
```


Except is a slice of CIDRs that should not be included within an IP Block Valid examples
are "192.168.1.1/24" Except values will be rejected if they are outside the CIDR range

<h2 class="pdoc-module-header" id="NetworkPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14445">interface NetworkPolicy</a>
</h2>

NetworkPolicy describes what network traffic is allowed for a set of Pods

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14452">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14460">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14466">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14471">property spec</a>
</h3>

```typescript
spec: NetworkPolicySpec;
```


Specification of the desired behavior for this NetworkPolicy.

<h2 class="pdoc-module-header" id="NetworkPolicyEgressRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14480">interface NetworkPolicyEgressRule</a>
</h2>

NetworkPolicyEgressRule describes a particular set of traffic that is allowed out of pods
matched by a NetworkPolicySpec's podSelector. The traffic must match both ports and to. This
type is beta-level in 1.8

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14487">property ports</a>
</h3>

```typescript
ports: NetworkPolicyPort[];
```


List of destination ports for outgoing traffic. Each item in this list is combined using a
logical OR. If this field is empty or missing, this rule matches all ports (traffic not
restricted by port). If this field is present and contains at least one item, then this
rule allows traffic only if the traffic matches at least one port in the list.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14496">property to</a>
</h3>

```typescript
to: NetworkPolicyPeer[];
```


List of destinations for outgoing traffic of pods selected for this rule. Items in this
list are combined using a logical OR operation. If this field is empty or missing, this
rule matches all destinations (traffic not restricted by destination). If this field is
present and contains at least one item, this rule allows traffic only if the traffic
matches at least one item in the to list.

<h2 class="pdoc-module-header" id="NetworkPolicyIngressRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14504">interface NetworkPolicyIngressRule</a>
</h2>

NetworkPolicyIngressRule describes a particular set of traffic that is allowed to the pods
matched by a NetworkPolicySpec's podSelector. The traffic must match both ports and from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14512">property from</a>
</h3>

```typescript
from: NetworkPolicyPeer[];
```


List of sources which should be able to access the pods selected for this rule. Items in
this list are combined using a logical OR operation. If this field is empty or missing,
this rule matches all sources (traffic not restricted by source). If this field is present
and contains at least on item, this rule allows traffic only if the traffic matches at
least one item in the from list.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14521">property ports</a>
</h3>

```typescript
ports: NetworkPolicyPort[];
```


List of ports which should be made accessible on the pods selected for this rule. Each item
in this list is combined using a logical OR. If this field is empty or missing, this rule
matches all ports (traffic not restricted by port). If this field is present and contains
at least one item, then this rule allows traffic only if the traffic matches at least one
port in the list.

<h2 class="pdoc-module-header" id="NetworkPolicyList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14528">interface NetworkPolicyList</a>
</h2>

NetworkPolicyList is a list of NetworkPolicy objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14535">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14540">property items</a>
</h3>

```typescript
items: NetworkPolicy[];
```


Items is a list of schema objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14548">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14554">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="NetworkPolicyPeer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14562">interface NetworkPolicyPeer</a>
</h2>

NetworkPolicyPeer describes a peer to allow traffic from. Exactly one of its fields must be
specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14566">property ipBlock</a>
</h3>

```typescript
ipBlock: IPBlock;
```


IPBlock defines policy on a particular IPBlock

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14573">property namespaceSelector</a>
</h3>

```typescript
namespaceSelector: LabelSelector;
```


Selects Namespaces using cluster scoped-labels. This matches all pods in all namespaces
selected by this label selector. This field follows standard label selector semantics. If
present but empty, this selector selects all namespaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14580">property podSelector</a>
</h3>

```typescript
podSelector: LabelSelector;
```


This is a label selector which selects Pods in this namespace. This field follows standard
label selector semantics. If present but empty, this selector selects all pods in this
namespace.

<h2 class="pdoc-module-header" id="NetworkPolicyPort">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14587">interface NetworkPolicyPort</a>
</h2>

NetworkPolicyPort describes a port to allow traffic on

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14592">property port</a>
</h3>

```typescript
port: number | string;
```


The port on the given protocol. This can either be a numerical or named port on a pod. If
this field is not provided, this matches all port names and numbers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14598">property protocol</a>
</h3>

```typescript
protocol: string;
```


The protocol (TCP or UDP) which traffic must match. If not specified, this field defaults
to TCP.

<h2 class="pdoc-module-header" id="NetworkPolicySpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14605">interface NetworkPolicySpec</a>
</h2>

NetworkPolicySpec provides the specification of a NetworkPolicy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14614">property egress</a>
</h3>

```typescript
egress: NetworkPolicyEgressRule[];
```


List of egress rules to be applied to the selected pods. Outgoing traffic is allowed if
there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the
traffic), OR if the traffic matches at least one egress rule across all of the
NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this
NetworkPolicy limits all outgoing traffic (and serves solely to ensure that the pods it
selects are isolated by default). This field is beta-level in 1.8

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14624">property ingress</a>
</h3>

```typescript
ingress: NetworkPolicyIngressRule[];
```


List of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if
there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the
traffic), OR if the traffic source is the pod's local node, OR if the traffic matches at
least one ingress rule across all of the NetworkPolicy objects whose podSelector matches
the pod. If this field is empty then this NetworkPolicy does not allow any traffic (and
serves solely to ensure that the pods it selects are isolated by default)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14633">property podSelector</a>
</h3>

```typescript
podSelector: LabelSelector;
```


Selects the pods to which this NetworkPolicy object applies. The array of ingress rules is
applied to any pods selected by this field. Multiple network policies can select the same
set of pods. In this case, the ingress rules for each are combined additively. This field
is NOT optional and follows standard label selector semantics. An empty podSelector matches
all pods in this namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L14646">property policyTypes</a>
</h3>

```typescript
policyTypes: string[];
```


List of rule types that the NetworkPolicy relates to. Valid options are Ingress, Egress, or
Ingress,Egress. If this field is not specified, it will default based on the existence of
Ingress or Egress rules; policies that contain an Egress section are assumed to affect
Egress, and all policies (whether or not they contain an Ingress section) are assumed to
affect Ingress. If you want to write an egress-only policy, you must explicitly specify
policyTypes [ "Egress" ]. Likewise, if you want to write a policy that specifies that no
egress is allowed, you must specify a policyTypes value that include "Egress" (since such a
policy would not include an Egress section and would otherwise default to just [ "Ingress"
]). This field is beta-level in 1.8

