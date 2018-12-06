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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L17387">function isNetworkPolicy</a>
</h2>

```typescript
isNetworkPolicy(o: any): boolean
```

<h2 class="pdoc-module-header" id="isNetworkPolicyList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L17476">function isNetworkPolicyList</a>
</h2>

```typescript
isNetworkPolicyList(o: any): boolean
```

<h2 class="pdoc-module-header" id="IPBlock">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16462">interface IPBlock</a>
</h2>

IPBlock describes a particular CIDR (Ex. "192.168.1.1/24") that is allowed to the pods
matched by a NetworkPolicySpec's podSelector. The except entry describes CIDRs that should
not be included within this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16466">property cidr</a>
</h3>

```typescript
cidr: string;
```


CIDR is a string representing the IP Block Valid examples are "192.168.1.1/24"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16472">property except</a>
</h3>

```typescript
except: string[];
```


Except is a slice of CIDRs that should not be included within an IP Block Valid examples
are "192.168.1.1/24" Except values will be rejected if they are outside the CIDR range

<h2 class="pdoc-module-header" id="NetworkPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16479">interface NetworkPolicy</a>
</h2>

NetworkPolicy describes what network traffic is allowed for a set of Pods

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16486">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16494">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16500">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16505">property spec</a>
</h3>

```typescript
spec: NetworkPolicySpec;
```


Specification of the desired behavior for this NetworkPolicy.

<h2 class="pdoc-module-header" id="NetworkPolicyEgressRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16514">interface NetworkPolicyEgressRule</a>
</h2>

NetworkPolicyEgressRule describes a particular set of traffic that is allowed out of pods
matched by a NetworkPolicySpec's podSelector. The traffic must match both ports and to. This
type is beta-level in 1.8

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16521">property ports</a>
</h3>

```typescript
ports: NetworkPolicyPort[];
```


List of destination ports for outgoing traffic. Each item in this list is combined using a
logical OR. If this field is empty or missing, this rule matches all ports (traffic not
restricted by port). If this field is present and contains at least one item, then this
rule allows traffic only if the traffic matches at least one port in the list.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16530">property to</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16538">interface NetworkPolicyIngressRule</a>
</h2>

NetworkPolicyIngressRule describes a particular set of traffic that is allowed to the pods
matched by a NetworkPolicySpec's podSelector. The traffic must match both ports and from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16546">property from</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16555">property ports</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16562">interface NetworkPolicyList</a>
</h2>

NetworkPolicyList is a list of NetworkPolicy objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16569">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16574">property items</a>
</h3>

```typescript
items: NetworkPolicy[];
```


Items is a list of schema objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16582">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16588">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="NetworkPolicyPeer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16596">interface NetworkPolicyPeer</a>
</h2>

NetworkPolicyPeer describes a peer to allow traffic from. Only certain combinations of fields
are allowed

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16601">property ipBlock</a>
</h3>

```typescript
ipBlock: IPBlock;
```


IPBlock defines policy on a particular IPBlock. If this field is set then neither of the
other fields can be.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16611">property namespaceSelector</a>
</h3>

```typescript
namespaceSelector: LabelSelector;
```


Selects Namespaces using cluster-scoped labels. This field follows standard label selector
semantics; if present but empty, it selects all namespaces.

If PodSelector is also set, then the NetworkPolicyPeer as a whole selects the Pods matching
PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects all Pods
in the Namespaces selected by NamespaceSelector.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16621">property podSelector</a>
</h3>

```typescript
podSelector: LabelSelector;
```


This is a label selector which selects Pods. This field follows standard label selector
semantics; if present but empty, it selects all pods.

If NamespaceSelector is also set, then the NetworkPolicyPeer as a whole selects the Pods
matching PodSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects
the Pods matching PodSelector in the policy's own Namespace.

<h2 class="pdoc-module-header" id="NetworkPolicyPort">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16628">interface NetworkPolicyPort</a>
</h2>

NetworkPolicyPort describes a port to allow traffic on

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16633">property port</a>
</h3>

```typescript
port: number | string;
```


The port on the given protocol. This can either be a numerical or named port on a pod. If
this field is not provided, this matches all port names and numbers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16639">property protocol</a>
</h3>

```typescript
protocol: string;
```


The protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field
defaults to TCP.

<h2 class="pdoc-module-header" id="NetworkPolicySpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16646">interface NetworkPolicySpec</a>
</h2>

NetworkPolicySpec provides the specification of a NetworkPolicy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16655">property egress</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16665">property ingress</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16674">property podSelector</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L16687">property policyTypes</a>
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

