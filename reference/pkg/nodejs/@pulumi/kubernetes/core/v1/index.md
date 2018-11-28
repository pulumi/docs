---
title: Module core/v1
---

<a href="../../index.html">@pulumi/kubernetes</a> &gt; <a href="../index.html">core</a> &gt; v1

<h2 class="pdoc-module-header">Index</h2>

* <a href="#isBinding">function isBinding</a>
* <a href="#isComponentStatus">function isComponentStatus</a>
* <a href="#isComponentStatusList">function isComponentStatusList</a>
* <a href="#isConfigMap">function isConfigMap</a>
* <a href="#isConfigMapList">function isConfigMapList</a>
* <a href="#isEndpoints">function isEndpoints</a>
* <a href="#isEndpointsList">function isEndpointsList</a>
* <a href="#isEvent">function isEvent</a>
* <a href="#isEventList">function isEventList</a>
* <a href="#isLimitRange">function isLimitRange</a>
* <a href="#isLimitRangeList">function isLimitRangeList</a>
* <a href="#isNamespace">function isNamespace</a>
* <a href="#isNamespaceList">function isNamespaceList</a>
* <a href="#isNode">function isNode</a>
* <a href="#isNodeList">function isNodeList</a>
* <a href="#isObjectFieldSelector">function isObjectFieldSelector</a>
* <a href="#isObjectReference">function isObjectReference</a>
* <a href="#isPersistentVolume">function isPersistentVolume</a>
* <a href="#isPersistentVolumeClaim">function isPersistentVolumeClaim</a>
* <a href="#isPersistentVolumeClaimList">function isPersistentVolumeClaimList</a>
* <a href="#isPersistentVolumeList">function isPersistentVolumeList</a>
* <a href="#isPod">function isPod</a>
* <a href="#isPodList">function isPodList</a>
* <a href="#isPodTemplate">function isPodTemplate</a>
* <a href="#isPodTemplateList">function isPodTemplateList</a>
* <a href="#isReplicationController">function isReplicationController</a>
* <a href="#isReplicationControllerList">function isReplicationControllerList</a>
* <a href="#isResourceQuota">function isResourceQuota</a>
* <a href="#isResourceQuotaList">function isResourceQuotaList</a>
* <a href="#isSecret">function isSecret</a>
* <a href="#isSecretList">function isSecretList</a>
* <a href="#isService">function isService</a>
* <a href="#isServiceAccount">function isServiceAccount</a>
* <a href="#isServiceAccountList">function isServiceAccountList</a>
* <a href="#isServiceList">function isServiceList</a>
* <a href="#AWSElasticBlockStoreVolumeSource">interface AWSElasticBlockStoreVolumeSource</a>
* <a href="#Affinity">interface Affinity</a>
* <a href="#AttachedVolume">interface AttachedVolume</a>
* <a href="#AzureDiskVolumeSource">interface AzureDiskVolumeSource</a>
* <a href="#AzureFilePersistentVolumeSource">interface AzureFilePersistentVolumeSource</a>
* <a href="#AzureFileVolumeSource">interface AzureFileVolumeSource</a>
* <a href="#Binding">interface Binding</a>
* <a href="#CSIPersistentVolumeSource">interface CSIPersistentVolumeSource</a>
* <a href="#Capabilities">interface Capabilities</a>
* <a href="#CephFSPersistentVolumeSource">interface CephFSPersistentVolumeSource</a>
* <a href="#CephFSVolumeSource">interface CephFSVolumeSource</a>
* <a href="#CinderPersistentVolumeSource">interface CinderPersistentVolumeSource</a>
* <a href="#CinderVolumeSource">interface CinderVolumeSource</a>
* <a href="#ClientIPConfig">interface ClientIPConfig</a>
* <a href="#ComponentCondition">interface ComponentCondition</a>
* <a href="#ComponentStatus">interface ComponentStatus</a>
* <a href="#ComponentStatusList">interface ComponentStatusList</a>
* <a href="#ConfigMap">interface ConfigMap</a>
* <a href="#ConfigMapEnvSource">interface ConfigMapEnvSource</a>
* <a href="#ConfigMapKeySelector">interface ConfigMapKeySelector</a>
* <a href="#ConfigMapList">interface ConfigMapList</a>
* <a href="#ConfigMapNodeConfigSource">interface ConfigMapNodeConfigSource</a>
* <a href="#ConfigMapProjection">interface ConfigMapProjection</a>
* <a href="#ConfigMapVolumeSource">interface ConfigMapVolumeSource</a>
* <a href="#Container">interface Container</a>
* <a href="#ContainerImage">interface ContainerImage</a>
* <a href="#ContainerPort">interface ContainerPort</a>
* <a href="#ContainerState">interface ContainerState</a>
* <a href="#ContainerStateRunning">interface ContainerStateRunning</a>
* <a href="#ContainerStateTerminated">interface ContainerStateTerminated</a>
* <a href="#ContainerStateWaiting">interface ContainerStateWaiting</a>
* <a href="#ContainerStatus">interface ContainerStatus</a>
* <a href="#DaemonEndpoint">interface DaemonEndpoint</a>
* <a href="#DownwardAPIProjection">interface DownwardAPIProjection</a>
* <a href="#DownwardAPIVolumeFile">interface DownwardAPIVolumeFile</a>
* <a href="#DownwardAPIVolumeSource">interface DownwardAPIVolumeSource</a>
* <a href="#EmptyDirVolumeSource">interface EmptyDirVolumeSource</a>
* <a href="#EndpointAddress">interface EndpointAddress</a>
* <a href="#EndpointPort">interface EndpointPort</a>
* <a href="#EndpointSubset">interface EndpointSubset</a>
* <a href="#Endpoints">interface Endpoints</a>
* <a href="#EndpointsList">interface EndpointsList</a>
* <a href="#EnvFromSource">interface EnvFromSource</a>
* <a href="#EnvVar">interface EnvVar</a>
* <a href="#EnvVarSource">interface EnvVarSource</a>
* <a href="#Event">interface Event</a>
* <a href="#EventList">interface EventList</a>
* <a href="#EventSeries">interface EventSeries</a>
* <a href="#EventSource">interface EventSource</a>
* <a href="#ExecAction">interface ExecAction</a>
* <a href="#FCVolumeSource">interface FCVolumeSource</a>
* <a href="#FlexPersistentVolumeSource">interface FlexPersistentVolumeSource</a>
* <a href="#FlexVolumeSource">interface FlexVolumeSource</a>
* <a href="#FlockerVolumeSource">interface FlockerVolumeSource</a>
* <a href="#GCEPersistentDiskVolumeSource">interface GCEPersistentDiskVolumeSource</a>
* <a href="#GitRepoVolumeSource">interface GitRepoVolumeSource</a>
* <a href="#GlusterfsVolumeSource">interface GlusterfsVolumeSource</a>
* <a href="#HTTPGetAction">interface HTTPGetAction</a>
* <a href="#HTTPHeader">interface HTTPHeader</a>
* <a href="#Handler">interface Handler</a>
* <a href="#HostAlias">interface HostAlias</a>
* <a href="#HostPathVolumeSource">interface HostPathVolumeSource</a>
* <a href="#ISCSIPersistentVolumeSource">interface ISCSIPersistentVolumeSource</a>
* <a href="#ISCSIVolumeSource">interface ISCSIVolumeSource</a>
* <a href="#KeyToPath">interface KeyToPath</a>
* <a href="#Lifecycle">interface Lifecycle</a>
* <a href="#LimitRange">interface LimitRange</a>
* <a href="#LimitRangeItem">interface LimitRangeItem</a>
* <a href="#LimitRangeList">interface LimitRangeList</a>
* <a href="#LimitRangeSpec">interface LimitRangeSpec</a>
* <a href="#LoadBalancerIngress">interface LoadBalancerIngress</a>
* <a href="#LoadBalancerStatus">interface LoadBalancerStatus</a>
* <a href="#LocalObjectReference">interface LocalObjectReference</a>
* <a href="#LocalVolumeSource">interface LocalVolumeSource</a>
* <a href="#NFSVolumeSource">interface NFSVolumeSource</a>
* <a href="#Namespace">interface Namespace</a>
* <a href="#NamespaceList">interface NamespaceList</a>
* <a href="#NamespaceSpec">interface NamespaceSpec</a>
* <a href="#NamespaceStatus">interface NamespaceStatus</a>
* <a href="#Node">interface Node</a>
* <a href="#NodeAddress">interface NodeAddress</a>
* <a href="#NodeAffinity">interface NodeAffinity</a>
* <a href="#NodeCondition">interface NodeCondition</a>
* <a href="#NodeConfigSource">interface NodeConfigSource</a>
* <a href="#NodeConfigStatus">interface NodeConfigStatus</a>
* <a href="#NodeDaemonEndpoints">interface NodeDaemonEndpoints</a>
* <a href="#NodeList">interface NodeList</a>
* <a href="#NodeSelector">interface NodeSelector</a>
* <a href="#NodeSelectorRequirement">interface NodeSelectorRequirement</a>
* <a href="#NodeSelectorTerm">interface NodeSelectorTerm</a>
* <a href="#NodeSpec">interface NodeSpec</a>
* <a href="#NodeStatus">interface NodeStatus</a>
* <a href="#NodeSystemInfo">interface NodeSystemInfo</a>
* <a href="#ObjectFieldSelector">interface ObjectFieldSelector</a>
* <a href="#ObjectReference">interface ObjectReference</a>
* <a href="#PersistentVolume">interface PersistentVolume</a>
* <a href="#PersistentVolumeClaim">interface PersistentVolumeClaim</a>
* <a href="#PersistentVolumeClaimCondition">interface PersistentVolumeClaimCondition</a>
* <a href="#PersistentVolumeClaimList">interface PersistentVolumeClaimList</a>
* <a href="#PersistentVolumeClaimSpec">interface PersistentVolumeClaimSpec</a>
* <a href="#PersistentVolumeClaimStatus">interface PersistentVolumeClaimStatus</a>
* <a href="#PersistentVolumeClaimVolumeSource">interface PersistentVolumeClaimVolumeSource</a>
* <a href="#PersistentVolumeList">interface PersistentVolumeList</a>
* <a href="#PersistentVolumeSpec">interface PersistentVolumeSpec</a>
* <a href="#PersistentVolumeStatus">interface PersistentVolumeStatus</a>
* <a href="#PhotonPersistentDiskVolumeSource">interface PhotonPersistentDiskVolumeSource</a>
* <a href="#Pod">interface Pod</a>
* <a href="#PodAffinity">interface PodAffinity</a>
* <a href="#PodAffinityTerm">interface PodAffinityTerm</a>
* <a href="#PodAntiAffinity">interface PodAntiAffinity</a>
* <a href="#PodCondition">interface PodCondition</a>
* <a href="#PodDNSConfig">interface PodDNSConfig</a>
* <a href="#PodDNSConfigOption">interface PodDNSConfigOption</a>
* <a href="#PodList">interface PodList</a>
* <a href="#PodReadinessGate">interface PodReadinessGate</a>
* <a href="#PodSecurityContext">interface PodSecurityContext</a>
* <a href="#PodSpec">interface PodSpec</a>
* <a href="#PodStatus">interface PodStatus</a>
* <a href="#PodTemplate">interface PodTemplate</a>
* <a href="#PodTemplateList">interface PodTemplateList</a>
* <a href="#PodTemplateSpec">interface PodTemplateSpec</a>
* <a href="#PortworxVolumeSource">interface PortworxVolumeSource</a>
* <a href="#PreferredSchedulingTerm">interface PreferredSchedulingTerm</a>
* <a href="#Probe">interface Probe</a>
* <a href="#ProjectedVolumeSource">interface ProjectedVolumeSource</a>
* <a href="#QuobyteVolumeSource">interface QuobyteVolumeSource</a>
* <a href="#RBDPersistentVolumeSource">interface RBDPersistentVolumeSource</a>
* <a href="#RBDVolumeSource">interface RBDVolumeSource</a>
* <a href="#ReplicationController">interface ReplicationController</a>
* <a href="#ReplicationControllerCondition">interface ReplicationControllerCondition</a>
* <a href="#ReplicationControllerList">interface ReplicationControllerList</a>
* <a href="#ReplicationControllerSpec">interface ReplicationControllerSpec</a>
* <a href="#ReplicationControllerStatus">interface ReplicationControllerStatus</a>
* <a href="#ResourceFieldSelector">interface ResourceFieldSelector</a>
* <a href="#ResourceQuota">interface ResourceQuota</a>
* <a href="#ResourceQuotaList">interface ResourceQuotaList</a>
* <a href="#ResourceQuotaSpec">interface ResourceQuotaSpec</a>
* <a href="#ResourceQuotaStatus">interface ResourceQuotaStatus</a>
* <a href="#ResourceRequirements">interface ResourceRequirements</a>
* <a href="#SELinuxOptions">interface SELinuxOptions</a>
* <a href="#ScaleIOPersistentVolumeSource">interface ScaleIOPersistentVolumeSource</a>
* <a href="#ScaleIOVolumeSource">interface ScaleIOVolumeSource</a>
* <a href="#ScopeSelector">interface ScopeSelector</a>
* <a href="#ScopedResourceSelectorRequirement">interface ScopedResourceSelectorRequirement</a>
* <a href="#Secret">interface Secret</a>
* <a href="#SecretEnvSource">interface SecretEnvSource</a>
* <a href="#SecretKeySelector">interface SecretKeySelector</a>
* <a href="#SecretList">interface SecretList</a>
* <a href="#SecretProjection">interface SecretProjection</a>
* <a href="#SecretReference">interface SecretReference</a>
* <a href="#SecretVolumeSource">interface SecretVolumeSource</a>
* <a href="#SecurityContext">interface SecurityContext</a>
* <a href="#Service">interface Service</a>
* <a href="#ServiceAccount">interface ServiceAccount</a>
* <a href="#ServiceAccountList">interface ServiceAccountList</a>
* <a href="#ServiceAccountTokenProjection">interface ServiceAccountTokenProjection</a>
* <a href="#ServiceList">interface ServiceList</a>
* <a href="#ServicePort">interface ServicePort</a>
* <a href="#ServiceSpec">interface ServiceSpec</a>
* <a href="#ServiceStatus">interface ServiceStatus</a>
* <a href="#SessionAffinityConfig">interface SessionAffinityConfig</a>
* <a href="#StorageOSPersistentVolumeSource">interface StorageOSPersistentVolumeSource</a>
* <a href="#StorageOSVolumeSource">interface StorageOSVolumeSource</a>
* <a href="#Sysctl">interface Sysctl</a>
* <a href="#TCPSocketAction">interface TCPSocketAction</a>
* <a href="#Taint">interface Taint</a>
* <a href="#Toleration">interface Toleration</a>
* <a href="#TopologySelectorLabelRequirement">interface TopologySelectorLabelRequirement</a>
* <a href="#TopologySelectorTerm">interface TopologySelectorTerm</a>
* <a href="#TypedLocalObjectReference">interface TypedLocalObjectReference</a>
* <a href="#Volume">interface Volume</a>
* <a href="#VolumeDevice">interface VolumeDevice</a>
* <a href="#VolumeMount">interface VolumeMount</a>
* <a href="#VolumeNodeAffinity">interface VolumeNodeAffinity</a>
* <a href="#VolumeProjection">interface VolumeProjection</a>
* <a href="#VsphereVirtualDiskVolumeSource">interface VsphereVirtualDiskVolumeSource</a>
* <a href="#WeightedPodAffinityTerm">interface WeightedPodAffinityTerm</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts">types/input.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts">types/output.ts</a> 


<h2 class="pdoc-module-header" id="isBinding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L7898">function isBinding</a>
</h2>

```typescript
isBinding(o: any): boolean
```

<h2 class="pdoc-module-header" id="isComponentStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L8207">function isComponentStatus</a>
</h2>

```typescript
isComponentStatus(o: any): boolean
```

<h2 class="pdoc-module-header" id="isComponentStatusList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L8244">function isComponentStatusList</a>
</h2>

```typescript
isComponentStatusList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isConfigMap">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L8292">function isConfigMap</a>
</h2>

```typescript
isConfigMap(o: any): boolean
```

<h2 class="pdoc-module-header" id="isConfigMapList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L8372">function isConfigMapList</a>
</h2>

```typescript
isConfigMapList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isEndpoints">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L9089">function isEndpoints</a>
</h2>

```typescript
isEndpoints(o: any): boolean
```

<h2 class="pdoc-module-header" id="isEndpointsList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L9126">function isEndpointsList</a>
</h2>

```typescript
isEndpointsList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isEvent">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L9307">function isEvent</a>
</h2>

```typescript
isEvent(o: any): boolean
```

<h2 class="pdoc-module-header" id="isEventList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L9344">function isEventList</a>
</h2>

```typescript
isEventList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isLimitRange">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L9966">function isLimitRange</a>
</h2>

```typescript
isLimitRange(o: any): boolean
```

<h2 class="pdoc-module-header" id="isLimitRangeList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L10044">function isLimitRangeList</a>
</h2>

```typescript
isLimitRangeList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isNamespace">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L10193">function isNamespace</a>
</h2>

```typescript
isNamespace(o: any): boolean
```

<h2 class="pdoc-module-header" id="isNamespaceList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L10231">function isNamespaceList</a>
</h2>

```typescript
isNamespaceList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isNode">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L10302">function isNode</a>
</h2>

```typescript
isNode(o: any): boolean
```

<h2 class="pdoc-module-header" id="isNodeList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L10499">function isNodeList</a>
</h2>

```typescript
isNodeList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isObjectFieldSelector">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L10750">function isObjectFieldSelector</a>
</h2>

```typescript
isObjectFieldSelector(o: any): boolean
```

<h2 class="pdoc-module-header" id="isObjectReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L10806">function isObjectReference</a>
</h2>

```typescript
isObjectReference(o: any): boolean
```

<h2 class="pdoc-module-header" id="isPersistentVolume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L10853">function isPersistentVolume</a>
</h2>

```typescript
isPersistentVolume(o: any): boolean
```

<h2 class="pdoc-module-header" id="isPersistentVolumeClaim">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L10898">function isPersistentVolumeClaim</a>
</h2>

```typescript
isPersistentVolumeClaim(o: any): boolean
```

<h2 class="pdoc-module-header" id="isPersistentVolumeClaimList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L10971">function isPersistentVolumeClaimList</a>
</h2>

```typescript
isPersistentVolumeClaimList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isPersistentVolumeList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L11113">function isPersistentVolumeList</a>
</h2>

```typescript
isPersistentVolumeList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isPod">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L11392">function isPod</a>
</h2>

```typescript
isPod(o: any): boolean
```

<h2 class="pdoc-module-header" id="isPodList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L11597">function isPodList</a>
</h2>

```typescript
isPodList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isPodTemplate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L12021">function isPodTemplate</a>
</h2>

```typescript
isPodTemplate(o: any): boolean
```

<h2 class="pdoc-module-header" id="isPodTemplateList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L12058">function isPodTemplateList</a>
</h2>

```typescript
isPodTemplateList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isReplicationController">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L12393">function isReplicationController</a>
</h2>

```typescript
isReplicationController(o: any): boolean
```

<h2 class="pdoc-module-header" id="isReplicationControllerList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L12464">function isReplicationControllerList</a>
</h2>

```typescript
isReplicationControllerList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isResourceQuota">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L12608">function isResourceQuota</a>
</h2>

```typescript
isResourceQuota(o: any): boolean
```

<h2 class="pdoc-module-header" id="isResourceQuotaList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L12646">function isResourceQuotaList</a>
</h2>

```typescript
isResourceQuotaList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isSecret">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L12955">function isSecret</a>
</h2>

```typescript
isSecret(o: any): boolean
```

<h2 class="pdoc-module-header" id="isSecretList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L13037">function isSecretList</a>
</h2>

```typescript
isSecretList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isService">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L13246">function isService</a>
</h2>

```typescript
isService(o: any): boolean
```

<h2 class="pdoc-module-header" id="isServiceAccount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L13301">function isServiceAccount</a>
</h2>

```typescript
isServiceAccount(o: any): boolean
```

<h2 class="pdoc-module-header" id="isServiceAccountList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L13339">function isServiceAccountList</a>
</h2>

```typescript
isServiceAccountList(o: any): boolean
```

<h2 class="pdoc-module-header" id="isServiceList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/input.ts#L13406">function isServiceList</a>
</h2>

```typescript
isServiceList(o: any): boolean
```

<h2 class="pdoc-module-header" id="AWSElasticBlockStoreVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7266">interface AWSElasticBlockStoreVolumeSource</a>
</h2>

Represents a Persistent Disk resource in AWS.

An AWS EBS disk must exist before mounting to a container. The disk must also be in the same
AWS zone as the kubelet. An AWS EBS disk can only be mounted as read/write once. AWS EBS
volumes support ownership management and SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7273">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type
is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly
inferred to be "ext4" if unspecified. More info:
https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7280">property partition</a>
</h3>

```typescript
partition: number;
```


The partition in the volume that you want to mount. If omitted, the default is to mount by
volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly,
the volume partition for /dev/sda is "0" (or you can leave the property empty).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7287">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". If
omitted, the default is "false". More info:
https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7293">property volumeID</a>
</h3>

```typescript
volumeID: string;
```


Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info:
https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore

<h2 class="pdoc-module-header" id="Affinity">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7300">interface Affinity</a>
</h2>

Affinity is a group of affinity scheduling rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7304">property nodeAffinity</a>
</h3>

```typescript
nodeAffinity: NodeAffinity;
```


Describes node affinity scheduling rules for the pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7310">property podAffinity</a>
</h3>

```typescript
podAffinity: PodAffinity;
```


Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone,
etc. as some other pod(s)).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7316">property podAntiAffinity</a>
</h3>

```typescript
podAntiAffinity: PodAntiAffinity;
```


Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node,
zone, etc. as some other pod(s)).

<h2 class="pdoc-module-header" id="AttachedVolume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7323">interface AttachedVolume</a>
</h2>

AttachedVolume describes a volume attached to a node

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7327">property devicePath</a>
</h3>

```typescript
devicePath: string;
```


DevicePath represents the device path where the volume should be available

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7332">property name</a>
</h3>

```typescript
name: string;
```


Name of the attached volume

<h2 class="pdoc-module-header" id="AzureDiskVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7339">interface AzureDiskVolumeSource</a>
</h2>

AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7343">property cachingMode</a>
</h3>

```typescript
cachingMode: string;
```


Host Caching mode: None, Read Only, Read Write.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7348">property diskName</a>
</h3>

```typescript
diskName: string;
```


The Name of the data disk in the blob storage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7353">property diskURI</a>
</h3>

```typescript
diskURI: string;
```


The URI the data disk in the blob storage

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7359">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type to mount. Must be a filesystem type supported by the host operating system.
Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7366">property kind</a>
</h3>

```typescript
kind: string;
```


Expected values Shared: multiple blob disks per storage account  Dedicated: single blob
disk per storage account  Managed: azure managed data disk (only in managed availability
set). defaults to shared

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7372">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
VolumeMounts.

<h2 class="pdoc-module-header" id="AzureFilePersistentVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7379">interface AzureFilePersistentVolumeSource</a>
</h2>

AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7384">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
VolumeMounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7389">property secretName</a>
</h3>

```typescript
secretName: string;
```


the name of secret that contains Azure Storage Account Name and Key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7395">property secretNamespace</a>
</h3>

```typescript
secretNamespace: string;
```


the namespace of the secret that contains Azure Storage Account Name and Key default is the
same as the Pod

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7400">property shareName</a>
</h3>

```typescript
shareName: string;
```


Share Name

<h2 class="pdoc-module-header" id="AzureFileVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7407">interface AzureFileVolumeSource</a>
</h2>

AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7412">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
VolumeMounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7417">property secretName</a>
</h3>

```typescript
secretName: string;
```


the name of secret that contains Azure Storage Account Name and Key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7422">property shareName</a>
</h3>

```typescript
shareName: string;
```


Share Name

<h2 class="pdoc-module-header" id="Binding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7430">interface Binding</a>
</h2>

Binding ties one object to another; for example, a pod is bound to a node by a scheduler.
Deprecated in 1.7, please use the bindings subresource of pods instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7437">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7445">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7451">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7456">property target</a>
</h3>

```typescript
target: ObjectReference;
```


The target object that you want to bind to the standard object.

<h2 class="pdoc-module-header" id="CSIPersistentVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7463">interface CSIPersistentVolumeSource</a>
</h2>

Represents storage that is managed by an external CSI volume driver (Beta feature)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7470">property controllerPublishSecretRef</a>
</h3>

```typescript
controllerPublishSecretRef: SecretReference;
```


ControllerPublishSecretRef is a reference to the secret object containing sensitive
information to pass to the CSI driver to complete the CSI ControllerPublishVolume and
ControllerUnpublishVolume calls. This field is optional, and  may be empty if no secret is
required. If the secret object contains more than one secret, all secrets are passed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7475">property driver</a>
</h3>

```typescript
driver: string;
```


Driver is the name of the driver to use for this volume. Required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7481">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type to mount. Must be a filesystem type supported by the host operating system.
Ex. "ext4", "xfs", "ntfs".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7489">property nodePublishSecretRef</a>
</h3>

```typescript
nodePublishSecretRef: SecretReference;
```


NodePublishSecretRef is a reference to the secret object containing sensitive information
to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume
calls. This field is optional, and  may be empty if no secret is required. If the secret
object contains more than one secret, all secrets are passed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7497">property nodeStageSecretRef</a>
</h3>

```typescript
nodeStageSecretRef: SecretReference;
```


NodeStageSecretRef is a reference to the secret object containing sensitive information to
pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and
NodeUnstageVolume calls. This field is optional, and  may be empty if no secret is
required. If the secret object contains more than one secret, all secrets are passed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7503">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Optional: The value to pass to ControllerPublishVolumeRequest. Defaults to false
(read/write).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7508">property volumeAttributes</a>
</h3>

```typescript
volumeAttributes: { ... };
```


Attributes of the volume to publish.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7514">property volumeHandle</a>
</h3>

```typescript
volumeHandle: string;
```


VolumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume
to refer to the volume on all subsequent calls. Required.

<h2 class="pdoc-module-header" id="Capabilities">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7521">interface Capabilities</a>
</h2>

Adds and removes POSIX capabilities from running containers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7525">property add</a>
</h3>

```typescript
add: string[];
```


Added capabilities

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7530">property drop</a>
</h3>

```typescript
drop: string[];
```


Removed capabilities

<h2 class="pdoc-module-header" id="CephFSPersistentVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7538">interface CephFSPersistentVolumeSource</a>
</h2>

Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not
support ownership management or SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7543">property monitors</a>
</h3>

```typescript
monitors: string[];
```


Required: Monitors is a collection of Ceph monitors More info:
https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7548">property path</a>
</h3>

```typescript
path: string;
```


Optional: Used as the mounted root, rather than the full Ceph tree, default is /

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7555">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
VolumeMounts. More info:
https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7561">property secretFile</a>
</h3>

```typescript
secretFile: string;
```


Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret
More info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7567">property secretRef</a>
</h3>

```typescript
secretRef: SecretReference;
```


Optional: SecretRef is reference to the authentication secret for User, default is empty.
More info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7573">property user</a>
</h3>

```typescript
user: string;
```


Optional: User is the rados user name, default is admin More info:
https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

<h2 class="pdoc-module-header" id="CephFSVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7581">interface CephFSVolumeSource</a>
</h2>

Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not
support ownership management or SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7586">property monitors</a>
</h3>

```typescript
monitors: string[];
```


Required: Monitors is a collection of Ceph monitors More info:
https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7591">property path</a>
</h3>

```typescript
path: string;
```


Optional: Used as the mounted root, rather than the full Ceph tree, default is /

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7598">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
VolumeMounts. More info:
https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7604">property secretFile</a>
</h3>

```typescript
secretFile: string;
```


Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret
More info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7610">property secretRef</a>
</h3>

```typescript
secretRef: LocalObjectReference;
```


Optional: SecretRef is reference to the authentication secret for User, default is empty.
More info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7616">property user</a>
</h3>

```typescript
user: string;
```


Optional: User is the rados user name, default is admin More info:
https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

<h2 class="pdoc-module-header" id="CinderPersistentVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7625">interface CinderPersistentVolumeSource</a>
</h2>

Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting
to a container. The volume must also be in the same region as the kubelet. Cinder volumes
support ownership management and SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7631">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type to mount. Must be a filesystem type supported by the host operating system.
Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More
info: https://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7637">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
VolumeMounts. More info: https://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7642">property secretRef</a>
</h3>

```typescript
secretRef: SecretReference;
```


Optional: points to a secret object containing parameters used to connect to OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7648">property volumeID</a>
</h3>

```typescript
volumeID: string;
```


volume id used to identify the volume in cinder More info:
https://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

<h2 class="pdoc-module-header" id="CinderVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7657">interface CinderVolumeSource</a>
</h2>

Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting
to a container. The volume must also be in the same region as the kubelet. Cinder volumes
support ownership management and SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7663">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type to mount. Must be a filesystem type supported by the host operating system.
Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More
info: https://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7669">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
VolumeMounts. More info: https://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7674">property secretRef</a>
</h3>

```typescript
secretRef: LocalObjectReference;
```


Optional: points to a secret object containing parameters used to connect to OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7680">property volumeID</a>
</h3>

```typescript
volumeID: string;
```


volume id used to identify the volume in cinder More info:
https://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

<h2 class="pdoc-module-header" id="ClientIPConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7687">interface ClientIPConfig</a>
</h2>

ClientIPConfig represents the configurations of Client IP based session affinity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7693">property timeoutSeconds</a>
</h3>

```typescript
timeoutSeconds: number;
```


timeoutSeconds specifies the seconds of ClientIP type session sticky time. The value must
be >0 && <=86400(for 1 day) if ServiceAffinity == "ClientIP". Default value is 10800(for 3
hours).

<h2 class="pdoc-module-header" id="ComponentCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7700">interface ComponentCondition</a>
</h2>

Information about the condition of a component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7704">property error</a>
</h3>

```typescript
error: string;
```


Condition error code for a component. For example, a health check error code.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7709">property message</a>
</h3>

```typescript
message: string;
```


Message about the condition for a component. For example, information about a health check.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7715">property status</a>
</h3>

```typescript
status: string;
```


Status of the condition for a component. Valid values for "Healthy": "True", "False", or
"Unknown".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7720">property type</a>
</h3>

```typescript
type: string;
```


Type of condition for a component. Valid value: "Healthy"

<h2 class="pdoc-module-header" id="ComponentStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7727">interface ComponentStatus</a>
</h2>

ComponentStatus (and ComponentStatusList) holds the cluster validation info.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7734">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7739">property conditions</a>
</h3>

```typescript
conditions: ComponentCondition[];
```


List of component conditions observed

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7747">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7753">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="ComponentStatusList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7760">interface ComponentStatusList</a>
</h2>

Status of all the conditions for the component as a list of ComponentStatus objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7767">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7772">property items</a>
</h3>

```typescript
items: ComponentStatus[];
```


List of ComponentStatus objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7780">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7786">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="ConfigMap">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7793">interface ConfigMap</a>
</h2>

ConfigMap holds configuration data for pods to consume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7800">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7808">property binaryData</a>
</h3>

```typescript
binaryData: object;
```


BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-',
'_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys
stored in BinaryData must not overlap with the ones in the Data field, this is enforced
during validation process. Using this field will require 1.10+ apiserver and kubelet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7816">property data</a>
</h3>

```typescript
data: { ... };
```


Data contains the configuration data. Each key must consist of alphanumeric characters,
'-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The
keys stored in Data must not overlap with the keys in the BinaryData field, this is
enforced during validation process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7824">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7830">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="ConfigMapEnvSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7840">interface ConfigMapEnvSource</a>
</h2>

ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.

The contents of the target ConfigMap's Data field will represent the key-value pairs as
environment variables.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7845">property name</a>
</h3>

```typescript
name: string;
```


Name of the referent. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7850">property optional</a>
</h3>

```typescript
optional: boolean;
```


Specify whether the ConfigMap must be defined

<h2 class="pdoc-module-header" id="ConfigMapKeySelector">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7857">interface ConfigMapKeySelector</a>
</h2>

Selects a key from a ConfigMap.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7861">property key</a>
</h3>

```typescript
key: string;
```


The key to select.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7867">property name</a>
</h3>

```typescript
name: string;
```


Name of the referent. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7872">property optional</a>
</h3>

```typescript
optional: boolean;
```


Specify whether the ConfigMap or it's key must be defined

<h2 class="pdoc-module-header" id="ConfigMapList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7879">interface ConfigMapList</a>
</h2>

ConfigMapList is a resource containing a list of ConfigMap objects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7886">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7891">property items</a>
</h3>

```typescript
items: ConfigMap[];
```


Items is the list of ConfigMaps.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7899">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7904">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h2 class="pdoc-module-header" id="ConfigMapNodeConfigSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7912">interface ConfigMapNodeConfigSource</a>
</h2>

ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config
source for the Node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7917">property kubeletConfigKey</a>
</h3>

```typescript
kubeletConfigKey: string;
```


KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the
KubeletConfiguration structure This field is required in all cases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7922">property name</a>
</h3>

```typescript
name: string;
```


Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7928">property namespace</a>
</h3>

```typescript
namespace: string;
```


Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in
all cases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7934">property resourceVersion</a>
</h3>

```typescript
resourceVersion: string;
```


ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is
forbidden in Node.Spec, and required in Node.Status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7940">property uid</a>
</h3>

```typescript
uid: string;
```


UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec,
and required in Node.Status.

<h2 class="pdoc-module-header" id="ConfigMapProjection">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7952">interface ConfigMapProjection</a>
</h2>

Adapts a ConfigMap into a projected volume.

The contents of the target ConfigMap's Data field will be presented in a projected volume as
files using the keys in the Data field as the file names, unless the items element is
populated with specific mappings of keys to paths. Note that this is identical to a configmap
volume source without the default mode.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7961">property items</a>
</h3>

```typescript
items: KeyToPath[];
```


If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be
projected into the volume as a file whose name is the key and content is the value. If
specified, the listed keys will be projected into the specified paths, and unlisted keys
will not be present. If a key is specified which is not present in the ConfigMap, the
volume setup will error unless it is marked optional. Paths must be relative and may not
contain the '..' path or start with '..'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7967">property name</a>
</h3>

```typescript
name: string;
```


Name of the referent. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7972">property optional</a>
</h3>

```typescript
optional: boolean;
```


Specify whether the ConfigMap or it's keys must be defined

<h2 class="pdoc-module-header" id="ConfigMapVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7984">interface ConfigMapVolumeSource</a>
</h2>

Adapts a ConfigMap into a volume.

The contents of the target ConfigMap's Data field will be presented in a volume as files
using the keys in the Data field as the file names, unless the items element is populated
with specific mappings of keys to paths. ConfigMap volumes support ownership management and
SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L7991">property defaultMode</a>
</h3>

```typescript
defaultMode: number;
```


Optional: mode bits to use on created files by default. Must be a value between 0 and 0777.
Defaults to 0644. Directories within the path are not affected by this setting. This might
be in conflict with other options that affect the file mode, like fsGroup, and the result
can be other mode bits set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8001">property items</a>
</h3>

```typescript
items: KeyToPath[];
```


If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be
projected into the volume as a file whose name is the key and content is the value. If
specified, the listed keys will be projected into the specified paths, and unlisted keys
will not be present. If a key is specified which is not present in the ConfigMap, the
volume setup will error unless it is marked optional. Paths must be relative and may not
contain the '..' path or start with '..'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8007">property name</a>
</h3>

```typescript
name: string;
```


Name of the referent. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8012">property optional</a>
</h3>

```typescript
optional: boolean;
```


Specify whether the ConfigMap or it's keys must be defined

<h2 class="pdoc-module-header" id="Container">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8019">interface Container</a>
</h2>

A single application container that you want to run within a pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8029">property args</a>
</h3>

```typescript
args: string[];
```


Arguments to the entrypoint. The docker image's CMD is used if this is not provided.
Variable references $(VAR_NAME) are expanded using the container's environment. If a
variable cannot be resolved, the reference in the input string will be unchanged. The
$(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references
will never be expanded, regardless of whether the variable exists or not. Cannot be
updated. More info:
https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8040">property command</a>
</h3>

```typescript
command: string[];
```


Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if
this is not provided. Variable references $(VAR_NAME) are expanded using the container's
environment. If a variable cannot be resolved, the reference in the input string will be
unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME).
Escaped references will never be expanded, regardless of whether the variable exists or
not. Cannot be updated. More info:
https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8045">property env</a>
</h3>

```typescript
env: EnvVar[];
```


List of environment variables to set in the container. Cannot be updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8054">property envFrom</a>
</h3>

```typescript
envFrom: EnvFromSource[];
```


List of sources to populate environment variables in the container. The keys defined within
a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the
container is starting. When a key exists in multiple sources, the value associated with the
last source will take precedence. Values defined by an Env with a duplicate key will take
precedence. Cannot be updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8061">property image</a>
</h3>

```typescript
image: string;
```


Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images This
field is optional to allow higher level config management to default or override container
images in workload controllers like Deployments and StatefulSets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8068">property imagePullPolicy</a>
</h3>

```typescript
imagePullPolicy: string;
```


Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is
specified, or IfNotPresent otherwise. Cannot be updated. More info:
https://kubernetes.io/docs/concepts/containers/images#updating-images

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8074">property lifecycle</a>
</h3>

```typescript
lifecycle: Lifecycle;
```


Actions that the management system should take in response to container lifecycle events.
Cannot be updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8081">property livenessProbe</a>
</h3>

```typescript
livenessProbe: Probe;
```


Periodic probe of container liveness. Container will be restarted if the probe fails.
Cannot be updated. More info:
https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8087">property name</a>
</h3>

```typescript
name: string;
```


Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique
name (DNS_LABEL). Cannot be updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8096">property ports</a>
</h3>

```typescript
ports: ContainerPort[];
```


List of ports to expose from the container. Exposing a port here gives the system
additional information about the network connections a container uses, but is primarily
informational. Not specifying a port here DOES NOT prevent that port from being exposed.
Any port which is listening on the default "0.0.0.0" address inside a container will be
accessible from the network. Cannot be updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8103">property readinessProbe</a>
</h3>

```typescript
readinessProbe: Probe;
```


Periodic probe of container service readiness. Container will be removed from service
endpoints if the probe fails. Cannot be updated. More info:
https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8109">property resources</a>
</h3>

```typescript
resources: ResourceRequirements;
```


Compute Resources required by this container. Cannot be updated. More info:
https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8116">property securityContext</a>
</h3>

```typescript
securityContext: SecurityContext;
```


Security options the pod should run with. More info:
https://kubernetes.io/docs/concepts/policy/security-context/ More info:
https://kubernetes.io/docs/tasks/configure-pod-container/security-context/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8122">property stdin</a>
</h3>

```typescript
stdin: boolean;
```


Whether this container should allocate a buffer for stdin in the container runtime. If this
is not set, reads from stdin in the container will always result in EOF. Default is false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8133">property stdinOnce</a>
</h3>

```typescript
stdinOnce: boolean;
```


Whether the container runtime should close the stdin channel after it has been opened by a
single attach. When stdin is true the stdin stream will remain open across multiple attach
sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until
the first client attaches to stdin, and then remains open and accepts data until the client
disconnects, at which time stdin is closed and remains closed until the container is
restarted. If this flag is false, a container processes that reads from stdin will never
receive an EOF. Default is false

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8142">property terminationMessagePath</a>
</h3>

```typescript
terminationMessagePath: string;
```


Optional: Path at which the file to which the container's termination message will be
written is mounted into the container's filesystem. Message written is intended to be brief
final status, such as an assertion failure message. Will be truncated by the node if
greater than 4096 bytes. The total message length across all containers will be limited to
12kb. Defaults to /dev/termination-log. Cannot be updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8152">property terminationMessagePolicy</a>
</h3>

```typescript
terminationMessagePolicy: string;
```


Indicate how the termination message should be populated. File will use the contents of
terminationMessagePath to populate the container status message on both success and
failure. FallbackToLogsOnError will use the last chunk of container log output if the
termination message file is empty and the container exited with an error. The log output is
limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be
updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8158">property tty</a>
</h3>

```typescript
tty: boolean;
```


Whether this container should allocate a TTY for itself, also requires 'stdin' to be true.
Default is false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8164">property volumeDevices</a>
</h3>

```typescript
volumeDevices: VolumeDevice[];
```


volumeDevices is the list of block devices to be used by the container. This is an alpha
feature and may change in the future.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8169">property volumeMounts</a>
</h3>

```typescript
volumeMounts: VolumeMount[];
```


Pod volumes to mount into the container's filesystem. Cannot be updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8175">property workingDir</a>
</h3>

```typescript
workingDir: string;
```


Container's working directory. If not specified, the container runtime's default will be
used, which might be configured in the container image. Cannot be updated.

<h2 class="pdoc-module-header" id="ContainerImage">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8182">interface ContainerImage</a>
</h2>

Describe a container image

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8187">property names</a>
</h3>

```typescript
names: string[];
```


Names by which this image is known. e.g. ["k8s.gcr.io/hyperkube:v1.0.7",
"dockerhub.io/google_containers/hyperkube:v1.0.7"]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8192">property sizeBytes</a>
</h3>

```typescript
sizeBytes: number;
```


The size of the image in bytes.

<h2 class="pdoc-module-header" id="ContainerPort">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8199">interface ContainerPort</a>
</h2>

ContainerPort represents a network port in a single container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8204">property containerPort</a>
</h3>

```typescript
containerPort: number;
```


Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x <
65536.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8209">property hostIP</a>
</h3>

```typescript
hostIP: string;
```


What host IP to bind the external port to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8216">property hostPort</a>
</h3>

```typescript
hostPort: number;
```


Number of port to expose on the host. If specified, this must be a valid port number, 0 < x
< 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not
need this.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8222">property name</a>
</h3>

```typescript
name: string;
```


If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a
pod must have a unique name. Name for the port that can be referred to by services.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8227">property protocol</a>
</h3>

```typescript
protocol: string;
```


Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".

<h2 class="pdoc-module-header" id="ContainerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8235">interface ContainerState</a>
</h2>

ContainerState holds a possible state of container. Only one of its members may be specified.
If none of them is specified, the default one is ContainerStateWaiting.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8239">property running</a>
</h3>

```typescript
running: ContainerStateRunning;
```


Details about a running container

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8244">property terminated</a>
</h3>

```typescript
terminated: ContainerStateTerminated;
```


Details about a terminated container

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8249">property waiting</a>
</h3>

```typescript
waiting: ContainerStateWaiting;
```


Details about a waiting container

<h2 class="pdoc-module-header" id="ContainerStateRunning">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8256">interface ContainerStateRunning</a>
</h2>

ContainerStateRunning is a running state of a container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8260">property startedAt</a>
</h3>

```typescript
startedAt: string;
```


Time at which the container was last (re-)started

<h2 class="pdoc-module-header" id="ContainerStateTerminated">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8267">interface ContainerStateTerminated</a>
</h2>

ContainerStateTerminated is a terminated state of a container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8271">property containerID</a>
</h3>

```typescript
containerID: string;
```


Container's ID in the format 'docker://<container_id>'

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8276">property exitCode</a>
</h3>

```typescript
exitCode: number;
```


Exit status from the last termination of the container

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8281">property finishedAt</a>
</h3>

```typescript
finishedAt: string;
```


Time at which the container last terminated

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8286">property message</a>
</h3>

```typescript
message: string;
```


Message regarding the last termination of the container

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8291">property reason</a>
</h3>

```typescript
reason: string;
```


(brief) reason from the last termination of the container

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8296">property signal</a>
</h3>

```typescript
signal: number;
```


Signal from the last termination of the container

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8301">property startedAt</a>
</h3>

```typescript
startedAt: string;
```


Time at which previous execution of the container started

<h2 class="pdoc-module-header" id="ContainerStateWaiting">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8308">interface ContainerStateWaiting</a>
</h2>

ContainerStateWaiting is a waiting state of a container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8312">property message</a>
</h3>

```typescript
message: string;
```


Message regarding why the container is not yet running.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8317">property reason</a>
</h3>

```typescript
reason: string;
```


(brief) reason the container is not yet running.

<h2 class="pdoc-module-header" id="ContainerStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8324">interface ContainerStatus</a>
</h2>

ContainerStatus contains details for the current status of this container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8328">property containerID</a>
</h3>

```typescript
containerID: string;
```


Container's ID in the format 'docker://<container_id>'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8334">property image</a>
</h3>

```typescript
image: string;
```


The image the container is running. More info:
https://kubernetes.io/docs/concepts/containers/images

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8339">property imageID</a>
</h3>

```typescript
imageID: string;
```


ImageID of the container's image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8344">property lastState</a>
</h3>

```typescript
lastState: ContainerState;
```


Details about the container's last termination condition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8350">property name</a>
</h3>

```typescript
name: string;
```


This must be a DNS_LABEL. Each container in a pod must have a unique name. Cannot be
updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8355">property ready</a>
</h3>

```typescript
ready: boolean;
```


Specifies whether the container has passed its readiness probe.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8363">property restartCount</a>
</h3>

```typescript
restartCount: number;
```


The number of times the container has been restarted, currently based on the number of dead
containers that have not yet been removed. Note that this is calculated from dead
containers. But those containers are subject to garbage collection. This value will get
capped at 5 by GC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8368">property state</a>
</h3>

```typescript
state: ContainerState;
```


Details about the container's current condition.

<h2 class="pdoc-module-header" id="DaemonEndpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8375">interface DaemonEndpoint</a>
</h2>

DaemonEndpoint contains information about a single Daemon endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8379">property Port</a>
</h3>

```typescript
Port: number;
```


Port number of the given endpoint.

<h2 class="pdoc-module-header" id="DownwardAPIProjection">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8387">interface DownwardAPIProjection</a>
</h2>

Represents downward API info for projecting into a projected volume. Note that this is
identical to a downwardAPI volume source without the default mode.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8391">property items</a>
</h3>

```typescript
items: DownwardAPIVolumeFile[];
```


Items is a list of DownwardAPIVolume file

<h2 class="pdoc-module-header" id="DownwardAPIVolumeFile">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8398">interface DownwardAPIVolumeFile</a>
</h2>

DownwardAPIVolumeFile represents information to create the file containing the pod field

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8403">property fieldRef</a>
</h3>

```typescript
fieldRef: ObjectFieldSelector;
```


Required: Selects a field of the pod: only annotations, labels, name and namespace are
supported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8410">property mode</a>
</h3>

```typescript
mode: number;
```


Optional: mode bits to use on this file, must be a value between 0 and 0777. If not
specified, the volume defaultMode will be used. This might be in conflict with other
options that affect the file mode, like fsGroup, and the result can be other mode bits set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8417">property path</a>
</h3>

```typescript
path: string;
```


Required: Path is  the relative path name of the file to be created. Must not be absolute
or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must
not start with '..'

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8423">property resourceFieldRef</a>
</h3>

```typescript
resourceFieldRef: ResourceFieldSelector;
```


Selects a resource of the container: only resources limits and requests (limits.cpu,
limits.memory, requests.cpu and requests.memory) are currently supported.

<h2 class="pdoc-module-header" id="DownwardAPIVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8431">interface DownwardAPIVolumeSource</a>
</h2>

DownwardAPIVolumeSource represents a volume containing downward API info. Downward API
volumes support ownership management and SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8438">property defaultMode</a>
</h3>

```typescript
defaultMode: number;
```


Optional: mode bits to use on created files by default. Must be a value between 0 and 0777.
Defaults to 0644. Directories within the path are not affected by this setting. This might
be in conflict with other options that affect the file mode, like fsGroup, and the result
can be other mode bits set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8443">property items</a>
</h3>

```typescript
items: DownwardAPIVolumeFile[];
```


Items is a list of downward API volume file

<h2 class="pdoc-module-header" id="EmptyDirVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8451">interface EmptyDirVolumeSource</a>
</h2>

Represents an empty directory for a pod. Empty directory volumes support ownership management
and SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8457">property medium</a>
</h3>

```typescript
medium: string;
```


What type of storage medium should back this directory. The default is "" which means to
use the node's default medium. Must be an empty string (default) or Memory. More info:
https://kubernetes.io/docs/concepts/storage/volumes#emptydir

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8466">property sizeLimit</a>
</h3>

```typescript
sizeLimit: string;
```


Total amount of local storage required for this EmptyDir volume. The size limit is also
applicable for memory medium. The maximum usage on memory medium EmptyDir would be the
minimum value between the SizeLimit specified here and the sum of memory limits of all
containers in a pod. The default is nil which means that the limit is undefined. More info:
http://kubernetes.io/docs/user-guide/volumes#emptydir

<h2 class="pdoc-module-header" id="EndpointAddress">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8473">interface EndpointAddress</a>
</h2>

EndpointAddress is a tuple that describes single IP address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8477">property hostname</a>
</h3>

```typescript
hostname: string;
```


The Hostname of this endpoint

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8484">property ip</a>
</h3>

```typescript
ip: string;
```


The IP of this endpoint. May not be loopback (127.0.0.0/8), link-local (169.254.0.0/16), or
link-local multicast ((224.0.0.0/24). IPv6 is also accepted but not fully supported on all
platforms. Also, certain kubernetes components, like kube-proxy, are not IPv6 ready.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8490">property nodeName</a>
</h3>

```typescript
nodeName: string;
```


Optional: Node hosting this endpoint. This can be used to determine endpoints local to a
node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8495">property targetRef</a>
</h3>

```typescript
targetRef: ObjectReference;
```


Reference to object providing the endpoint.

<h2 class="pdoc-module-header" id="EndpointPort">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8502">interface EndpointPort</a>
</h2>

EndpointPort is a tuple that describes a single port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8507">property name</a>
</h3>

```typescript
name: string;
```


The name of this port (corresponds to ServicePort.Name). Must be a DNS_LABEL. Optional only
if one port is defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8512">property port</a>
</h3>

```typescript
port: number;
```


The port number of the endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8517">property protocol</a>
</h3>

```typescript
protocol: string;
```


The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.

<h2 class="pdoc-module-header" id="EndpointSubset">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8532">interface EndpointSubset</a>
</h2>

EndpointSubset is a group of addresses with a common set of ports. The expanded set of
endpoints is the Cartesian product of Addresses x Ports. For example, given:
  {
    Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
    Ports:     [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
  }
The resulting set of endpoints can be viewed as:
    a: [ 10.10.1.1:8675, 10.10.2.2:8675 ],
    b: [ 10.10.1.1:309, 10.10.2.2:309 ]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8537">property addresses</a>
</h3>

```typescript
addresses: EndpointAddress[];
```


IP addresses which offer the related ports that are marked as ready. These endpoints should
be considered safe for load balancers and clients to utilize.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8544">property notReadyAddresses</a>
</h3>

```typescript
notReadyAddresses: EndpointAddress[];
```


IP addresses which offer the related ports but are not currently marked as ready because
they have not yet finished starting, have recently failed a readiness check, or have
recently failed a liveness check.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8549">property ports</a>
</h3>

```typescript
ports: EndpointPort[];
```


Port numbers available on the related IP addresses.

<h2 class="pdoc-module-header" id="Endpoints">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8567">interface Endpoints</a>
</h2>

Endpoints is a collection of endpoints that implement the actual service. Example:
  Name: "mysvc",
  Subsets: [
    {
      Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
      Ports: [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
    },
    {
      Addresses: [{"ip": "10.10.3.3"}],
      Ports: [{"name": "a", "port": 93}, {"name": "b", "port": 76}]
    },
 ]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8574">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8582">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8588">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8598">property subsets</a>
</h3>

```typescript
subsets: EndpointSubset[];
```


The set of all endpoints is the union of all subsets. Addresses are placed into subsets
according to the IPs they share. A single address with multiple ports, some of which are
ready and some of which are not (because they come from different containers) will result
in the address being displayed in different subsets for the different ports. No address
will appear in both Addresses and NotReadyAddresses in the same subset. Sets of addresses
and ports that comprise a service.

<h2 class="pdoc-module-header" id="EndpointsList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8605">interface EndpointsList</a>
</h2>

EndpointsList is a list of endpoints.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8612">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8617">property items</a>
</h3>

```typescript
items: Endpoints[];
```


List of endpoints.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8625">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8631">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="EnvFromSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8638">interface EnvFromSource</a>
</h2>

EnvFromSource represents the source of a set of ConfigMaps

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8642">property configMapRef</a>
</h3>

```typescript
configMapRef: ConfigMapEnvSource;
```


The ConfigMap to select from

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8647">property prefix</a>
</h3>

```typescript
prefix: string;
```


An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8652">property secretRef</a>
</h3>

```typescript
secretRef: SecretEnvSource;
```


The Secret to select from

<h2 class="pdoc-module-header" id="EnvVar">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8659">interface EnvVar</a>
</h2>

EnvVar represents an environment variable present in a Container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8663">property name</a>
</h3>

```typescript
name: string;
```


Name of the environment variable. Must be a C_IDENTIFIER.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8672">property value</a>
</h3>

```typescript
value: string;
```


Variable references $(VAR_NAME) are expanded using the previous defined environment
variables in the container and any service environment variables. If a variable cannot be
resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can
be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded,
regardless of whether the variable exists or not. Defaults to "".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8677">property valueFrom</a>
</h3>

```typescript
valueFrom: EnvVarSource;
```


Source for the environment variable's value. Cannot be used if value is not empty.

<h2 class="pdoc-module-header" id="EnvVarSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8684">interface EnvVarSource</a>
</h2>

EnvVarSource represents a source for the value of an EnvVar.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8688">property configMapKeyRef</a>
</h3>

```typescript
configMapKeyRef: ConfigMapKeySelector;
```


Selects a key of a ConfigMap.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8694">property fieldRef</a>
</h3>

```typescript
fieldRef: ObjectFieldSelector;
```


Selects a field of the pod: supports metadata.name, metadata.namespace, metadata.labels,
metadata.annotations, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8701">property resourceFieldRef</a>
</h3>

```typescript
resourceFieldRef: ResourceFieldSelector;
```


Selects a resource of the container: only resources limits and requests (limits.cpu,
limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and
requests.ephemeral-storage) are currently supported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8706">property secretKeyRef</a>
</h3>

```typescript
secretKeyRef: SecretKeySelector;
```


Selects a key of a secret in the pod's namespace

<h2 class="pdoc-module-header" id="Event">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8713">interface Event</a>
</h2>

Event is a report of an event somewhere in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8717">property action</a>
</h3>

```typescript
action: string;
```


What action was taken/failed regarding to the Regarding object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8725">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8730">property count</a>
</h3>

```typescript
count: number;
```


The number of times this event has occurred.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8735">property eventTime</a>
</h3>

```typescript
eventTime: string;
```


Time when this Event was first observed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8740">property firstTimestamp</a>
</h3>

```typescript
firstTimestamp: string;
```


The time at which the event was first recorded. (Time of server receipt is in TypeMeta.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8745">property involvedObject</a>
</h3>

```typescript
involvedObject: ObjectReference;
```


The object that this event is about.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8753">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8758">property lastTimestamp</a>
</h3>

```typescript
lastTimestamp: string;
```


The time at which the most recent occurrence of this event was recorded.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8763">property message</a>
</h3>

```typescript
message: string;
```


A human-readable description of the status of this operation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8769">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8775">property reason</a>
</h3>

```typescript
reason: string;
```


This should be a short, machine understandable string that gives the reason for the
transition into the object's current status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8780">property related</a>
</h3>

```typescript
related: ObjectReference;
```


Optional secondary object for more complex actions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8785">property reportingComponent</a>
</h3>

```typescript
reportingComponent: string;
```


Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8790">property reportingInstance</a>
</h3>

```typescript
reportingInstance: string;
```


ID of the controller instance, e.g. `kubelet-xyzf`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8795">property series</a>
</h3>

```typescript
series: EventSeries;
```


Data about the Event series this event represents or nil if it's a singleton Event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8800">property source</a>
</h3>

```typescript
source: EventSource;
```


The component reporting this event. Should be a short machine understandable string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8805">property type</a>
</h3>

```typescript
type: string;
```


Type of this event (Normal, Warning), new types could be added in the future

<h2 class="pdoc-module-header" id="EventList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8812">interface EventList</a>
</h2>

EventList is a list of events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8819">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8824">property items</a>
</h3>

```typescript
items: Event[];
```


List of events

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8832">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8838">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="EventSeries">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8846">interface EventSeries</a>
</h2>

EventSeries contain information on series of events, i.e. thing that was/is happening
continuously for some time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8850">property count</a>
</h3>

```typescript
count: number;
```


Number of occurrences in this series up to the last heartbeat time

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8855">property lastObservedTime</a>
</h3>

```typescript
lastObservedTime: string;
```


Time of the last occurrence observed

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8860">property state</a>
</h3>

```typescript
state: string;
```


State of this Series: Ongoing or Finished

<h2 class="pdoc-module-header" id="EventSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8867">interface EventSource</a>
</h2>

EventSource contains information for an event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8871">property component</a>
</h3>

```typescript
component: string;
```


Component from which the event is generated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8876">property host</a>
</h3>

```typescript
host: string;
```


Node name on which the event is generated.

<h2 class="pdoc-module-header" id="ExecAction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8883">interface ExecAction</a>
</h2>

ExecAction describes a "run in container" action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8891">property command</a>
</h3>

```typescript
command: string[];
```


Command is the command line to execute inside the container, the working directory for the
command  is root ('/') in the container's filesystem. The command is simply exec'd, it is
not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a
shell, you need to explicitly call out to that shell. Exit status of 0 is treated as
live/healthy and non-zero is unhealthy.

<h2 class="pdoc-module-header" id="FCVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8899">interface FCVolumeSource</a>
</h2>

Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write
once. Fibre Channel volumes support ownership management and SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8904">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type to mount. Must be a filesystem type supported by the host operating system.
Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8909">property lun</a>
</h3>

```typescript
lun: number;
```


Optional: FC target lun number

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8915">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
VolumeMounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8920">property targetWWNs</a>
</h3>

```typescript
targetWWNs: string[];
```


Optional: FC target worldwide names (WWNs)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8926">property wwids</a>
</h3>

```typescript
wwids: string[];
```


Optional: FC volume world wide identifiers (wwids) Either wwids or combination of
targetWWNs and lun must be set, but not both simultaneously.

<h2 class="pdoc-module-header" id="FlexPersistentVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8934">interface FlexPersistentVolumeSource</a>
</h2>

FlexPersistentVolumeSource represents a generic persistent volume resource that is
provisioned/attached using an exec based plugin.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8938">property driver</a>
</h3>

```typescript
driver: string;
```


Driver is the name of the driver to use for this volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8944">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type to mount. Must be a filesystem type supported by the host operating system.
Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8949">property options</a>
</h3>

```typescript
options: { ... };
```


Optional: Extra command options if any.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8955">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
VolumeMounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8962">property secretRef</a>
</h3>

```typescript
secretRef: SecretReference;
```


Optional: SecretRef is reference to the secret object containing sensitive information to
pass to the plugin scripts. This may be empty if no secret object is specified. If the
secret object contains more than one secret, all secrets are passed to the plugin scripts.

<h2 class="pdoc-module-header" id="FlexVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8970">interface FlexVolumeSource</a>
</h2>

FlexVolume represents a generic volume resource that is provisioned/attached using an exec
based plugin.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8974">property driver</a>
</h3>

```typescript
driver: string;
```


Driver is the name of the driver to use for this volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8980">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type to mount. Must be a filesystem type supported by the host operating system.
Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8985">property options</a>
</h3>

```typescript
options: { ... };
```


Optional: Extra command options if any.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8991">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
VolumeMounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L8998">property secretRef</a>
</h3>

```typescript
secretRef: LocalObjectReference;
```


Optional: SecretRef is reference to the secret object containing sensitive information to
pass to the plugin scripts. This may be empty if no secret object is specified. If the
secret object contains more than one secret, all secrets are passed to the plugin scripts.

<h2 class="pdoc-module-header" id="FlockerVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9007">interface FlockerVolumeSource</a>
</h2>

Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and
datasetUUID should be set. Flocker volumes do not support ownership management or SELinux
relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9012">property datasetName</a>
</h3>

```typescript
datasetName: string;
```


Name of the dataset stored as metadata -> name on the dataset for Flocker should be
considered as deprecated

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9017">property datasetUUID</a>
</h3>

```typescript
datasetUUID: string;
```


UUID of the dataset. This is unique identifier of a Flocker dataset

<h2 class="pdoc-module-header" id="GCEPersistentDiskVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9028">interface GCEPersistentDiskVolumeSource</a>
</h2>

Represents a Persistent Disk resource in Google Compute Engine.

A GCE PD must exist before mounting to a container. The disk must also be in the same GCE
project and zone as the kubelet. A GCE PD can only be mounted as read/write once or read-only
many times. GCE PDs support ownership management and SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9035">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type
is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly
inferred to be "ext4" if unspecified. More info:
https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9043">property partition</a>
</h3>

```typescript
partition: number;
```


The partition in the volume that you want to mount. If omitted, the default is to mount by
volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly,
the volume partition for /dev/sda is "0" (or you can leave the property empty). More info:
https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9049">property pdName</a>
</h3>

```typescript
pdName: string;
```


Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info:
https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9055">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More
info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk

<h2 class="pdoc-module-header" id="GitRepoVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9067">interface GitRepoVolumeSource</a>
</h2>

Represents a volume that is populated with the contents of a git repository. Git repo volumes
do not support ownership management. Git repo volumes support SELinux relabeling.

DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an
EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into
the Pod's container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9073">property directory</a>
</h3>

```typescript
directory: string;
```


Target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume
directory will be the git repository.  Otherwise, if specified, the volume will contain the
git repository in the subdirectory with the given name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9078">property repository</a>
</h3>

```typescript
repository: string;
```


Repository URL

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9083">property revision</a>
</h3>

```typescript
revision: string;
```


Commit hash for the specified revision.

<h2 class="pdoc-module-header" id="GlusterfsVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9091">interface GlusterfsVolumeSource</a>
</h2>

Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not
support ownership management or SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9096">property endpoints</a>
</h3>

```typescript
endpoints: string;
```


EndpointsName is the endpoint name that details Glusterfs topology. More info:
https://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9102">property path</a>
</h3>

```typescript
path: string;
```


Path is the Glusterfs volume path. More info:
https://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9109">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions.
Defaults to false. More info:
https://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod

<h2 class="pdoc-module-header" id="HTTPGetAction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9116">interface HTTPGetAction</a>
</h2>

HTTPGetAction describes an action based on HTTP Get requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9121">property host</a>
</h3>

```typescript
host: string;
```


Host name to connect to, defaults to the pod IP. You probably want to set "Host" in
httpHeaders instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9126">property httpHeaders</a>
</h3>

```typescript
httpHeaders: HTTPHeader[];
```


Custom headers to set in the request. HTTP allows repeated headers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9131">property path</a>
</h3>

```typescript
path: string;
```


Path to access on the HTTP server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9137">property port</a>
</h3>

```typescript
port: number | string;
```


Name or number of the port to access on the container. Number must be in the range 1 to
65535. Name must be an IANA_SVC_NAME.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9142">property scheme</a>
</h3>

```typescript
scheme: string;
```


Scheme to use for connecting to the host. Defaults to HTTP.

<h2 class="pdoc-module-header" id="HTTPHeader">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9149">interface HTTPHeader</a>
</h2>

HTTPHeader describes a custom header to be used in HTTP probes

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9153">property name</a>
</h3>

```typescript
name: string;
```


The header field name

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9158">property value</a>
</h3>

```typescript
value: string;
```


The header field value

<h2 class="pdoc-module-header" id="Handler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9165">interface Handler</a>
</h2>

Handler defines a specific action that should be taken

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9169">property exec</a>
</h3>

```typescript
exec: ExecAction;
```


One and only one of the following should be specified. Exec specifies the action to take.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9174">property httpGet</a>
</h3>

```typescript
httpGet: HTTPGetAction;
```


HTTPGet specifies the http request to perform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9179">property tcpSocket</a>
</h3>

```typescript
tcpSocket: TCPSocketAction;
```


TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported

<h2 class="pdoc-module-header" id="HostAlias">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9187">interface HostAlias</a>
</h2>

HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the
pod's hosts file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9191">property hostnames</a>
</h3>

```typescript
hostnames: string[];
```


Hostnames for the above IP address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9196">property ip</a>
</h3>

```typescript
ip: string;
```


IP address of the host file entry.

<h2 class="pdoc-module-header" id="HostPathVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9204">interface HostPathVolumeSource</a>
</h2>

Represents a host path mapped into a pod. Host path volumes do not support ownership
management or SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9209">property path</a>
</h3>

```typescript
path: string;
```


Path of the directory on the host. If the path is a symlink, it will follow the link to the
real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9215">property type</a>
</h3>

```typescript
type: string;
```


Type for HostPath Volume Defaults to "" More info:
https://kubernetes.io/docs/concepts/storage/volumes#hostpath

<h2 class="pdoc-module-header" id="ISCSIPersistentVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9223">interface ISCSIPersistentVolumeSource</a>
</h2>

ISCSIPersistentVolumeSource represents an ISCSI disk. ISCSI volumes can only be mounted as
read/write once. ISCSI volumes support ownership management and SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9227">property chapAuthDiscovery</a>
</h3>

```typescript
chapAuthDiscovery: boolean;
```


whether support iSCSI Discovery CHAP authentication

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9232">property chapAuthSession</a>
</h3>

```typescript
chapAuthSession: boolean;
```


whether support iSCSI Session CHAP authentication

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9240">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type
is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly
inferred to be "ext4" if unspecified. More info:
https://kubernetes.io/docs/concepts/storage/volumes#iscsi

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9247">property initiatorName</a>
</h3>

```typescript
initiatorName: string;
```


Custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface
simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the
connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9252">property iqn</a>
</h3>

```typescript
iqn: string;
```


Target iSCSI Qualified Name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9257">property iscsiInterface</a>
</h3>

```typescript
iscsiInterface: string;
```


iSCSI Interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9262">property lun</a>
</h3>

```typescript
lun: number;
```


iSCSI Target Lun number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9268">property portals</a>
</h3>

```typescript
portals: string[];
```


iSCSI Target Portal List. The Portal is either an IP or ip_addr:port if the port is other
than default (typically TCP ports 860 and 3260).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9273">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9278">property secretRef</a>
</h3>

```typescript
secretRef: SecretReference;
```


CHAP Secret for iSCSI target and initiator authentication

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9284">property targetPortal</a>
</h3>

```typescript
targetPortal: string;
```


iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than
default (typically TCP ports 860 and 3260).

<h2 class="pdoc-module-header" id="ISCSIVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9292">interface ISCSIVolumeSource</a>
</h2>

Represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes
support ownership management and SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9296">property chapAuthDiscovery</a>
</h3>

```typescript
chapAuthDiscovery: boolean;
```


whether support iSCSI Discovery CHAP authentication

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9301">property chapAuthSession</a>
</h3>

```typescript
chapAuthSession: boolean;
```


whether support iSCSI Session CHAP authentication

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9309">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type
is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly
inferred to be "ext4" if unspecified. More info:
https://kubernetes.io/docs/concepts/storage/volumes#iscsi

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9316">property initiatorName</a>
</h3>

```typescript
initiatorName: string;
```


Custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface
simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the
connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9321">property iqn</a>
</h3>

```typescript
iqn: string;
```


Target iSCSI Qualified Name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9326">property iscsiInterface</a>
</h3>

```typescript
iscsiInterface: string;
```


iSCSI Interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9331">property lun</a>
</h3>

```typescript
lun: number;
```


iSCSI Target Lun number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9337">property portals</a>
</h3>

```typescript
portals: string[];
```


iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other
than default (typically TCP ports 860 and 3260).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9342">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9347">property secretRef</a>
</h3>

```typescript
secretRef: LocalObjectReference;
```


CHAP Secret for iSCSI target and initiator authentication

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9353">property targetPortal</a>
</h3>

```typescript
targetPortal: string;
```


iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than
default (typically TCP ports 860 and 3260).

<h2 class="pdoc-module-header" id="KeyToPath">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9360">interface KeyToPath</a>
</h2>

Maps a string key to a path within a volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9364">property key</a>
</h3>

```typescript
key: string;
```


The key to project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9371">property mode</a>
</h3>

```typescript
mode: number;
```


Optional: mode bits to use on this file, must be a value between 0 and 0777. If not
specified, the volume defaultMode will be used. This might be in conflict with other
options that affect the file mode, like fsGroup, and the result can be other mode bits set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9377">property path</a>
</h3>

```typescript
path: string;
```


The relative path of the file to map the key to. May not be an absolute path. May not
contain the path element '..'. May not start with the string '..'.

<h2 class="pdoc-module-header" id="Lifecycle">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9387">interface Lifecycle</a>
</h2>

Lifecycle describes actions that the management system should take in response to container
lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the
container blocks until the action is complete, unless the container process fails, in which
case the handler is aborted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9394">property postStart</a>
</h3>

```typescript
postStart: Handler;
```


PostStart is called immediately after a container is created. If the handler fails, the
container is terminated and restarted according to its restart policy. Other management of
the container blocks until the hook completes. More info:
https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9403">property preStop</a>
</h3>

```typescript
preStop: Handler;
```


PreStop is called immediately before a container is terminated. The container is terminated
after the handler completes. The reason for termination is passed to the handler.
Regardless of the outcome of the handler, the container is eventually terminated. Other
management of the container blocks until the hook completes. More info:
https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks

<h2 class="pdoc-module-header" id="LimitRange">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9410">interface LimitRange</a>
</h2>

LimitRange sets resource usage limits for each kind of resource in a Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9417">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9425">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9431">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9437">property spec</a>
</h3>

```typescript
spec: LimitRangeSpec;
```


Spec defines the limits enforced. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h2 class="pdoc-module-header" id="LimitRangeItem">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9444">interface LimitRangeItem</a>
</h2>

LimitRangeItem defines a min/max usage limit for any resource that matches on kind.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9448">property default</a>
</h3>

```typescript
default: object;
```


Default resource requirement limit value by resource name if resource limit is omitted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9454">property defaultRequest</a>
</h3>

```typescript
defaultRequest: object;
```


DefaultRequest is the default resource requirement request value by resource name if
resource request is omitted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9459">property max</a>
</h3>

```typescript
max: object;
```


Max usage constraints on this kind by resource name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9466">property maxLimitRequestRatio</a>
</h3>

```typescript
maxLimitRequestRatio: object;
```


MaxLimitRequestRatio if specified, the named resource must have a request and limit that
are both non-zero where limit divided by request is less than or equal to the enumerated
value; this represents the max burst for the named resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9471">property min</a>
</h3>

```typescript
min: object;
```


Min usage constraints on this kind by resource name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9476">property type</a>
</h3>

```typescript
type: string;
```


Type of resource that this limit applies to.

<h2 class="pdoc-module-header" id="LimitRangeList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9483">interface LimitRangeList</a>
</h2>

LimitRangeList is a list of LimitRange items.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9490">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9496">property items</a>
</h3>

```typescript
items: LimitRange[];
```


Items is a list of LimitRange objects. More info:
https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9504">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9510">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="LimitRangeSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9517">interface LimitRangeSpec</a>
</h2>

LimitRangeSpec defines a min/max usage limit for resources that match on kind.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9521">property limits</a>
</h3>

```typescript
limits: LimitRangeItem[];
```


Limits is the list of LimitRangeItem objects that are enforced.

<h2 class="pdoc-module-header" id="LoadBalancerIngress">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9529">interface LoadBalancerIngress</a>
</h2>

LoadBalancerIngress represents the status of a load-balancer ingress point: traffic intended
for the service should be sent to an ingress point.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9534">property hostname</a>
</h3>

```typescript
hostname: string;
```


Hostname is set for load-balancer ingress points that are DNS based (typically AWS
load-balancers)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9540">property ip</a>
</h3>

```typescript
ip: string;
```


IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack
load-balancers)

<h2 class="pdoc-module-header" id="LoadBalancerStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9547">interface LoadBalancerStatus</a>
</h2>

LoadBalancerStatus represents the status of a load-balancer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9552">property ingress</a>
</h3>

```typescript
ingress: LoadBalancerIngress[];
```


Ingress is a list containing ingress points for the load-balancer. Traffic intended for the
service should be sent to these ingress points.

<h2 class="pdoc-module-header" id="LocalObjectReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9560">interface LocalObjectReference</a>
</h2>

LocalObjectReference contains enough information to let you locate the referenced object
inside the same namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9565">property name</a>
</h3>

```typescript
name: string;
```


Name of the referent. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

<h2 class="pdoc-module-header" id="LocalVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9572">interface LocalVolumeSource</a>
</h2>

Local represents directly-attached storage with node affinity (Beta feature)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9578">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type to mount. It applies only when the Path is a block device. Must be a
filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The
default value is to auto-select a fileystem if unspecified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9584">property path</a>
</h3>

```typescript
path: string;
```


The full path to the volume on the node. It can be either a directory or block device
(disk, partition, ...).

<h2 class="pdoc-module-header" id="NFSVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9592">interface NFSVolumeSource</a>
</h2>

Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support
ownership management or SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9597">property path</a>
</h3>

```typescript
path: string;
```


Path that is exported by the NFS server. More info:
https://kubernetes.io/docs/concepts/storage/volumes#nfs

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9603">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


ReadOnly here will force the NFS export to be mounted with read-only permissions. Defaults
to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9609">property server</a>
</h3>

```typescript
server: string;
```


Server is the hostname or IP address of the NFS server. More info:
https://kubernetes.io/docs/concepts/storage/volumes#nfs

<h2 class="pdoc-module-header" id="Namespace">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9616">interface Namespace</a>
</h2>

Namespace provides a scope for Names. Use of multiple namespaces is optional.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9623">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9631">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9637">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9643">property spec</a>
</h3>

```typescript
spec: NamespaceSpec;
```


Spec defines the behavior of the Namespace. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9649">property status</a>
</h3>

```typescript
status: NamespaceStatus;
```


Status describes the current status of a Namespace. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h2 class="pdoc-module-header" id="NamespaceList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9656">interface NamespaceList</a>
</h2>

NamespaceList is a list of Namespaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9663">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9669">property items</a>
</h3>

```typescript
items: Namespace[];
```


Items is the list of Namespace objects in the list. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9677">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9683">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="NamespaceSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9690">interface NamespaceSpec</a>
</h2>

NamespaceSpec describes the attributes on a Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9695">property finalizers</a>
</h3>

```typescript
finalizers: string[];
```


Finalizers is an opaque list of values that must be empty to permanently remove object from
storage. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/

<h2 class="pdoc-module-header" id="NamespaceStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9702">interface NamespaceStatus</a>
</h2>

NamespaceStatus is information about the current status of a Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9707">property phase</a>
</h3>

```typescript
phase: string;
```


Phase is the current lifecycle phase of the namespace. More info:
https://kubernetes.io/docs/tasks/administer-cluster/namespaces/

<h2 class="pdoc-module-header" id="Node">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9715">interface Node</a>
</h2>

Node is a worker node in Kubernetes. Each node will have a unique identifier in the cache
(i.e. in etcd).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9722">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9730">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9736">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9742">property spec</a>
</h3>

```typescript
spec: NodeSpec;
```


Spec defines the behavior of a node.
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9748">property status</a>
</h3>

```typescript
status: NodeStatus;
```


Most recently observed status of the node. Populated by the system. Read-only. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h2 class="pdoc-module-header" id="NodeAddress">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9755">interface NodeAddress</a>
</h2>

NodeAddress contains information for the node's address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9759">property address</a>
</h3>

```typescript
address: string;
```


The node address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9764">property type</a>
</h3>

```typescript
type: string;
```


Node address type, one of Hostname, ExternalIP or InternalIP.

<h2 class="pdoc-module-header" id="NodeAffinity">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9771">interface NodeAffinity</a>
</h2>

Node affinity is a group of node affinity scheduling rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9781">property preferredDuringSchedulingIgnoredDuringExecution</a>
</h3>

```typescript
preferredDuringSchedulingIgnoredDuringExecution: PreferredSchedulingTerm[];
```


The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions
specified by this field, but it may choose a node that violates one or more of the
expressions. The node that is most preferred is the one with the greatest sum of weights,
i.e. for each node that meets all of the scheduling requirements (resource request,
requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through
the elements of this field and adding "weight" to the sum if the node matches the
corresponding matchExpressions; the node(s) with the highest sum are the most preferred.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9789">property requiredDuringSchedulingIgnoredDuringExecution</a>
</h3>

```typescript
requiredDuringSchedulingIgnoredDuringExecution: NodeSelector;
```


If the affinity requirements specified by this field are not met at scheduling time, the
pod will not be scheduled onto the node. If the affinity requirements specified by this
field cease to be met at some point during pod execution (e.g. due to an update), the
system may or may not try to eventually evict the pod from its node.

<h2 class="pdoc-module-header" id="NodeCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9796">interface NodeCondition</a>
</h2>

NodeCondition contains condition information for a node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9800">property lastHeartbeatTime</a>
</h3>

```typescript
lastHeartbeatTime: string;
```


Last time we got an update on a given condition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9805">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


Last time the condition transit from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9810">property message</a>
</h3>

```typescript
message: string;
```


Human readable message indicating details about last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9815">property reason</a>
</h3>

```typescript
reason: string;
```


(brief) reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9820">property status</a>
</h3>

```typescript
status: string;
```


Status of the condition, one of True, False, Unknown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9825">property type</a>
</h3>

```typescript
type: string;
```


Type of node condition.

<h2 class="pdoc-module-header" id="NodeConfigSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9833">interface NodeConfigSource</a>
</h2>

NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding
metadata) must be non-nil.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9837">property configMap</a>
</h3>

```typescript
configMap: ConfigMapNodeConfigSource;
```


ConfigMap is a reference to a Node's ConfigMap

<h2 class="pdoc-module-header" id="NodeConfigStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9844">interface NodeConfigStatus</a>
</h2>

NodeConfigStatus describes the status of the config assigned by Node.Spec.ConfigSource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9850">property active</a>
</h3>

```typescript
active: NodeConfigSource;
```


Active reports the checkpointed config the node is actively using. Active will represent
either the current version of the Assigned config, or the current LastKnownGood config,
depending on whether attempting to use the Assigned config results in an error.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9861">property assigned</a>
</h3>

```typescript
assigned: NodeConfigSource;
```


Assigned reports the checkpointed config the node will try to use. When
Node.Spec.ConfigSource is updated, the node checkpoints the associated config payload to
local disk, along with a record indicating intended config. The node refers to this record
to choose its config checkpoint, and reports this record in Assigned. Assigned only updates
in the status after the record has been checkpointed to disk. When the Kubelet is
restarted, it tries to make the Assigned config the Active config by loading and validating
the checkpointed payload identified by Assigned.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9877">property error</a>
</h3>

```typescript
error: string;
```


Error describes any problems reconciling the Spec.ConfigSource to the Active config. Errors
may occur, for example, attempting to checkpoint Spec.ConfigSource to the local Assigned
record, attempting to checkpoint the payload associated with Spec.ConfigSource, attempting
to load or validate the Assigned config, etc. Errors may occur at different points while
syncing config. Earlier errors (e.g. download or checkpointing errors) will not result in a
rollback to LastKnownGood, and may resolve across Kubelet retries. Later errors (e.g.
loading or validating a checkpointed config) will result in a rollback to LastKnownGood. In
the latter case, it is usually possible to resolve the error by fixing the config assigned
in Spec.ConfigSource. You can find additional information for debugging by searching the
error message in the Kubelet log. Error is a human-readable description of the error state;
machines can check whether or not Error is empty, but should not rely on the stability of
the Error text across Kubelet versions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9891">property lastKnownGood</a>
</h3>

```typescript
lastKnownGood: NodeConfigSource;
```


LastKnownGood reports the checkpointed config the node will fall back to when it encounters
an error attempting to use the Assigned config. The Assigned config becomes the
LastKnownGood config when the node determines that the Assigned config is stable and
correct. This is currently implemented as a 10-minute soak period starting when the local
record of Assigned config is updated. If the Assigned config is Active at the end of this
period, it becomes the LastKnownGood. Note that if Spec.ConfigSource is reset to nil (use
local defaults), the LastKnownGood is also immediately reset to nil, because the local
default config is always assumed good. You should not make assumptions about the node's
method of determining config stability and correctness, as this may change or become
configurable in the future.

<h2 class="pdoc-module-header" id="NodeDaemonEndpoints">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9898">interface NodeDaemonEndpoints</a>
</h2>

NodeDaemonEndpoints lists ports opened by daemons running on the Node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9902">property kubeletEndpoint</a>
</h3>

```typescript
kubeletEndpoint: DaemonEndpoint;
```


Endpoint on which Kubelet is listening.

<h2 class="pdoc-module-header" id="NodeList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9909">interface NodeList</a>
</h2>

NodeList is the whole list of all Nodes which have been registered with master.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9916">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9921">property items</a>
</h3>

```typescript
items: Node[];
```


List of nodes

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9929">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9935">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="NodeSelector">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9944">interface NodeSelector</a>
</h2>

A node selector represents the union of the results of one or more label queries over a set
of nodes; that is, it represents the OR of the selectors represented by the node selector
terms.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9948">property nodeSelectorTerms</a>
</h3>

```typescript
nodeSelectorTerms: NodeSelectorTerm[];
```


Required. A list of node selector terms. The terms are ORed.

<h2 class="pdoc-module-header" id="NodeSelectorRequirement">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9956">interface NodeSelectorRequirement</a>
</h2>

A node selector requirement is a selector that contains values, a key, and an operator that
relates the key and values.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9960">property key</a>
</h3>

```typescript
key: string;
```


The label key that the selector applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9966">property operator</a>
</h3>

```typescript
operator: string;
```


Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists,
DoesNotExist. Gt, and Lt.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9974">property values</a>
</h3>

```typescript
values: string[];
```


An array of string values. If the operator is In or NotIn, the values array must be
non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If
the operator is Gt or Lt, the values array must have a single element, which will be
interpreted as an integer. This array is replaced during a strategic merge patch.

<h2 class="pdoc-module-header" id="NodeSelectorTerm">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9982">interface NodeSelectorTerm</a>
</h2>

A null or empty node selector term matches no objects. The requirements of them are ANDed.
The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9986">property matchExpressions</a>
</h3>

```typescript
matchExpressions: NodeSelectorRequirement[];
```


A list of node selector requirements by node's labels.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9991">property matchFields</a>
</h3>

```typescript
matchFields: NodeSelectorRequirement[];
```


A list of node selector requirements by node's fields.

<h2 class="pdoc-module-header" id="NodeSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L9998">interface NodeSpec</a>
</h2>

NodeSpec describes the attributes that a node is created with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10003">property configSource</a>
</h3>

```typescript
configSource: NodeConfigSource;
```


If specified, the source to get node configuration from The DynamicKubeletConfig feature
gate must be enabled for the Kubelet to use this field

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10009">property externalID</a>
</h3>

```typescript
externalID: string;
```


Deprecated. Not all kubelets will set this field. Remove field after 1.13. see:
https://issues.k8s.io/61966

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10014">property podCIDR</a>
</h3>

```typescript
podCIDR: string;
```


PodCIDR represents the pod IP range assigned to the node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10020">property providerID</a>
</h3>

```typescript
providerID: string;
```


ID of the node assigned by the cloud provider in the format:
<ProviderName>://<ProviderSpecificNodeID>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10025">property taints</a>
</h3>

```typescript
taints: Taint[];
```


If specified, the node's taints.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10031">property unschedulable</a>
</h3>

```typescript
unschedulable: boolean;
```


Unschedulable controls node schedulability of new pods. By default, node is schedulable.
More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration

<h2 class="pdoc-module-header" id="NodeStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10038">interface NodeStatus</a>
</h2>

NodeStatus is information about the current status of a node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10043">property addresses</a>
</h3>

```typescript
addresses: NodeAddress[];
```


List of addresses reachable to the node. Queried from cloud provider, if available. More
info: https://kubernetes.io/docs/concepts/nodes/node/#addresses

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10049">property allocatable</a>
</h3>

```typescript
allocatable: object;
```


Allocatable represents the resources of a node that are available for scheduling. Defaults
to Capacity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10055">property capacity</a>
</h3>

```typescript
capacity: object;
```


Capacity represents the total resources of a node. More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10061">property conditions</a>
</h3>

```typescript
conditions: NodeCondition[];
```


Conditions is an array of current observed node conditions. More info:
https://kubernetes.io/docs/concepts/nodes/node/#condition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10066">property config</a>
</h3>

```typescript
config: NodeConfigStatus;
```


Status of the config assigned to the node via the dynamic Kubelet config feature.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10071">property daemonEndpoints</a>
</h3>

```typescript
daemonEndpoints: NodeDaemonEndpoints;
```


Endpoints of daemons running on the Node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10076">property images</a>
</h3>

```typescript
images: ContainerImage[];
```


List of container images on this node

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10082">property nodeInfo</a>
</h3>

```typescript
nodeInfo: NodeSystemInfo;
```


Set of ids/uuids to uniquely identify the node. More info:
https://kubernetes.io/docs/concepts/nodes/node/#info

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10089">property phase</a>
</h3>

```typescript
phase: string;
```


NodePhase is the recently observed lifecycle phase of the node. More info:
https://kubernetes.io/docs/concepts/nodes/node/#phase The field is never populated, and now
is deprecated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10094">property volumesAttached</a>
</h3>

```typescript
volumesAttached: AttachedVolume[];
```


List of volumes that are attached to the node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10099">property volumesInUse</a>
</h3>

```typescript
volumesInUse: string[];
```


List of attachable volumes in use (mounted) by the node.

<h2 class="pdoc-module-header" id="NodeSystemInfo">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10106">interface NodeSystemInfo</a>
</h2>

NodeSystemInfo is a set of ids/uuids to uniquely identify the node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10110">property architecture</a>
</h3>

```typescript
architecture: string;
```


The Architecture reported by the node

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10115">property bootID</a>
</h3>

```typescript
bootID: string;
```


Boot ID reported by the node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10121">property containerRuntimeVersion</a>
</h3>

```typescript
containerRuntimeVersion: string;
```


ContainerRuntime Version reported by the node through runtime remote API (e.g.
docker://1.5.0).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10126">property kernelVersion</a>
</h3>

```typescript
kernelVersion: string;
```


Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10131">property kubeProxyVersion</a>
</h3>

```typescript
kubeProxyVersion: string;
```


KubeProxy Version reported by the node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10136">property kubeletVersion</a>
</h3>

```typescript
kubeletVersion: string;
```


Kubelet Version reported by the node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10143">property machineID</a>
</h3>

```typescript
machineID: string;
```


MachineID reported by the node. For unique machine identification in the cluster this field
is preferred. Learn more from man(5) machine-id:
http://man7.org/linux/man-pages/man5/machine-id.5.html

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10148">property operatingSystem</a>
</h3>

```typescript
operatingSystem: string;
```


The Operating System reported by the node

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10153">property osImage</a>
</h3>

```typescript
osImage: string;
```


OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10160">property systemUUID</a>
</h3>

```typescript
systemUUID: string;
```


SystemUUID reported by the node. For unique machine identification MachineID is preferred.
This field is specific to Red Hat hosts
https://access.redhat.com/documentation/en-US/Red_Hat_Subscription_Management/1/html/RHSM/getting-system-uuid.html

<h2 class="pdoc-module-header" id="ObjectFieldSelector">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10167">interface ObjectFieldSelector</a>
</h2>

ObjectFieldSelector selects an APIVersioned field of an object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10171">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


Version of the schema the FieldPath is written in terms of, defaults to "v1".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10176">property fieldPath</a>
</h3>

```typescript
fieldPath: string;
```


Path of the field to select in the specified API version.

<h2 class="pdoc-module-header" id="ObjectReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10183">interface ObjectReference</a>
</h2>

ObjectReference contains enough information to let you inspect or modify the referred object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10187">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


API version of the referent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10198">property fieldPath</a>
</h3>

```typescript
fieldPath: string;
```


If referring to a piece of an object instead of an entire object, this string should
contain a valid JSON/Go field access statement, such as
desiredState.manifest.containers[2]. For example, if the object reference is to a container
within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers
to the name of the container that triggered the event) or if no container name is specified
"spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to
have some well-defined way of referencing a part of an object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10204">property kind</a>
</h3>

```typescript
kind: string;
```


Kind of the referent. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10210">property name</a>
</h3>

```typescript
name: string;
```


Name of the referent. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10216">property namespace</a>
</h3>

```typescript
namespace: string;
```


Namespace of the referent. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10222">property resourceVersion</a>
</h3>

```typescript
resourceVersion: string;
```


Specific resourceVersion to which this reference is made, if any. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10228">property uid</a>
</h3>

```typescript
uid: string;
```


UID of the referent. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids

<h2 class="pdoc-module-header" id="PersistentVolume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10236">interface PersistentVolume</a>
</h2>

PersistentVolume (PV) is a storage resource provisioned by an administrator. It is analogous
to a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10243">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10251">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10257">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10264">property spec</a>
</h3>

```typescript
spec: PersistentVolumeSpec;
```


Spec defines a specification of a persistent volume owned by the cluster. Provisioned by an
administrator. More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistent-volumes

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10271">property status</a>
</h3>

```typescript
status: PersistentVolumeStatus;
```


Status represents the current information/status for the persistent volume. Populated by
the system. Read-only. More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistent-volumes

<h2 class="pdoc-module-header" id="PersistentVolumeClaim">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10278">interface PersistentVolumeClaim</a>
</h2>

PersistentVolumeClaim is a user's request for and claim to a persistent volume

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10285">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10293">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10299">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10305">property spec</a>
</h3>

```typescript
spec: PersistentVolumeClaimSpec;
```


Spec defines the desired characteristics of a volume requested by a pod author. More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10312">property status</a>
</h3>

```typescript
status: PersistentVolumeClaimStatus;
```


Status represents the current information/status of a persistent volume claim. Read-only.
More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims

<h2 class="pdoc-module-header" id="PersistentVolumeClaimCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10319">interface PersistentVolumeClaimCondition</a>
</h2>

PersistentVolumeClaimCondition contails details about state of pvc

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10323">property lastProbeTime</a>
</h3>

```typescript
lastProbeTime: string;
```


Last time we probed the condition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10328">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


Last time the condition transitioned from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10333">property message</a>
</h3>

```typescript
message: string;
```


Human-readable message indicating details about last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10340">property reason</a>
</h3>

```typescript
reason: string;
```


Unique, this should be a short, machine understandable string that gives the reason for
condition's last transition. If it reports "ResizeStarted" that means the underlying
persistent volume is being resized.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10343">property status</a>
</h3>

```typescript
status: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10346">property type</a>
</h3>

```typescript
type: string;
```

<h2 class="pdoc-module-header" id="PersistentVolumeClaimList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10353">interface PersistentVolumeClaimList</a>
</h2>

PersistentVolumeClaimList is a list of PersistentVolumeClaim items.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10360">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10366">property items</a>
</h3>

```typescript
items: PersistentVolumeClaim[];
```


A list of persistent volume claims. More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10374">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10380">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="PersistentVolumeClaimSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10388">interface PersistentVolumeClaimSpec</a>
</h2>

PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a
Source for provider-specific attributes

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10393">property accessModes</a>
</h3>

```typescript
accessModes: string[];
```


AccessModes contains the desired access modes the volume should have. More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10403">property dataSource</a>
</h3>

```typescript
dataSource: TypedLocalObjectReference;
```


This field requires the VolumeSnapshotDataSource alpha feature gate to be enabled and
currently VolumeSnapshot is the only supported data source. If the provisioner can support
VolumeSnapshot data source, it will create a new volume and data will be restored to the
volume at the same time. If the provisioner does not support VolumeSnapshot data source,
volume will not be created and the failure will be reported as an event. In the future, we
plan to support more data source types and the behavior of the provisioner may change.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10409">property resources</a>
</h3>

```typescript
resources: ResourceRequirements;
```


Resources represents the minimum resources the volume should have. More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10414">property selector</a>
</h3>

```typescript
selector: LabelSelector;
```


A label query over volumes to consider for binding.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10420">property storageClassName</a>
</h3>

```typescript
storageClassName: string;
```


Name of the StorageClass required by the claim. More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10427">property volumeMode</a>
</h3>

```typescript
volumeMode: string;
```


volumeMode defines what type of volume is required by the claim. Value of Filesystem is
implied when not included in claim spec. This is an alpha feature and may change in the
future.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10432">property volumeName</a>
</h3>

```typescript
volumeName: string;
```


VolumeName is the binding reference to the PersistentVolume backing this claim.

<h2 class="pdoc-module-header" id="PersistentVolumeClaimStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10439">interface PersistentVolumeClaimStatus</a>
</h2>

PersistentVolumeClaimStatus is the current status of a persistent volume claim.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10444">property accessModes</a>
</h3>

```typescript
accessModes: string[];
```


AccessModes contains the actual access modes the volume backing the PVC has. More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10449">property capacity</a>
</h3>

```typescript
capacity: object;
```


Represents the actual resources of the underlying volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10455">property conditions</a>
</h3>

```typescript
conditions: PersistentVolumeClaimCondition[];
```


Current Condition of persistent volume claim. If underlying persistent volume is being
resized then the Condition will be set to 'ResizeStarted'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10460">property phase</a>
</h3>

```typescript
phase: string;
```


Phase represents the current phase of PersistentVolumeClaim.

<h2 class="pdoc-module-header" id="PersistentVolumeClaimVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10470">interface PersistentVolumeClaimVolumeSource</a>
</h2>

PersistentVolumeClaimVolumeSource references the user's PVC in the same namespace. This
volume finds the bound PV and mounts that volume for the pod. A
PersistentVolumeClaimVolumeSource is, essentially, a wrapper around another type of volume
that is owned by someone else (the system).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10476">property claimName</a>
</h3>

```typescript
claimName: string;
```


ClaimName is the name of a PersistentVolumeClaim in the same namespace as the pod using
this volume. More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10481">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Will force the ReadOnly setting in VolumeMounts. Default false.

<h2 class="pdoc-module-header" id="PersistentVolumeList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10488">interface PersistentVolumeList</a>
</h2>

PersistentVolumeList is a list of PersistentVolume items.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10495">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10501">property items</a>
</h3>

```typescript
items: PersistentVolume[];
```


List of persistent volumes. More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10509">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10515">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="PersistentVolumeSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10522">interface PersistentVolumeSpec</a>
</h2>

PersistentVolumeSpec is the specification of a persistent volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10527">property accessModes</a>
</h3>

```typescript
accessModes: string[];
```


AccessModes contains all ways the volume can be mounted. More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10534">property awsElasticBlockStore</a>
</h3>

```typescript
awsElasticBlockStore: AWSElasticBlockStoreVolumeSource;
```


AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host
machine and then exposed to the pod. More info:
https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10539">property azureDisk</a>
</h3>

```typescript
azureDisk: AzureDiskVolumeSource;
```


AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10544">property azureFile</a>
</h3>

```typescript
azureFile: AzureFilePersistentVolumeSource;
```


AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10550">property capacity</a>
</h3>

```typescript
capacity: object;
```


A description of the persistent volume's resources and capacity. More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10555">property cephfs</a>
</h3>

```typescript
cephfs: CephFSPersistentVolumeSource;
```


CephFS represents a Ceph FS mount on the host that shares a pod's lifetime

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10561">property cinder</a>
</h3>

```typescript
cinder: CinderPersistentVolumeSource;
```


Cinder represents a cinder volume attached and mounted on kubelets host machine More info:
https://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10569">property claimRef</a>
</h3>

```typescript
claimRef: ObjectReference;
```


ClaimRef is part of a bi-directional binding between PersistentVolume and
PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the
authoritative bind between PV and PVC. More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10574">property csi</a>
</h3>

```typescript
csi: CSIPersistentVolumeSource;
```


CSI represents storage that handled by an external CSI driver (Beta feature).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10580">property fc</a>
</h3>

```typescript
fc: FCVolumeSource;
```


FC represents a Fibre Channel resource that is attached to a kubelet's host machine and
then exposed to the pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10586">property flexVolume</a>
</h3>

```typescript
flexVolume: FlexPersistentVolumeSource;
```


FlexVolume represents a generic volume resource that is provisioned/attached using an exec
based plugin.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10592">property flocker</a>
</h3>

```typescript
flocker: FlockerVolumeSource;
```


Flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the
pod for its usage. This depends on the Flocker control service being running

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10599">property gcePersistentDisk</a>
</h3>

```typescript
gcePersistentDisk: GCEPersistentDiskVolumeSource;
```


GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host
machine and then exposed to the pod. Provisioned by an admin. More info:
https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10606">property glusterfs</a>
</h3>

```typescript
glusterfs: GlusterfsVolumeSource;
```


Glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod.
Provisioned by an admin. More info:
https://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10614">property hostPath</a>
</h3>

```typescript
hostPath: HostPathVolumeSource;
```


HostPath represents a directory on the host. Provisioned by a developer or tester. This is
useful for single-node development and testing only! On-host storage is not supported in
any way and WILL NOT WORK in a multi-node cluster. More info:
https://kubernetes.io/docs/concepts/storage/volumes#hostpath

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10620">property iscsi</a>
</h3>

```typescript
iscsi: ISCSIPersistentVolumeSource;
```


ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and
then exposed to the pod. Provisioned by an admin.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10625">property local</a>
</h3>

```typescript
local: LocalVolumeSource;
```


Local represents directly-attached storage with node affinity

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10632">property mountOptions</a>
</h3>

```typescript
mountOptions: string[];
```


A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one
is invalid. More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10638">property nfs</a>
</h3>

```typescript
nfs: NFSVolumeSource;
```


NFS represents an NFS mount on the host. Provisioned by an admin. More info:
https://kubernetes.io/docs/concepts/storage/volumes#nfs

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10644">property nodeAffinity</a>
</h3>

```typescript
nodeAffinity: VolumeNodeAffinity;
```


NodeAffinity defines constraints that limit what nodes this volume can be accessed from.
This field influences the scheduling of pods that use this volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10653">property persistentVolumeReclaimPolicy</a>
</h3>

```typescript
persistentVolumeReclaimPolicy: string;
```


What happens to a persistent volume when released from its claim. Valid options are Retain
(default for manually created PersistentVolumes), Delete (default for dynamically
provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the
volume plugin underlying this PersistentVolume. More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10659">property photonPersistentDisk</a>
</h3>

```typescript
photonPersistentDisk: PhotonPersistentDiskVolumeSource;
```


PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on
kubelets host machine

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10664">property portworxVolume</a>
</h3>

```typescript
portworxVolume: PortworxVolumeSource;
```


PortworxVolume represents a portworx volume attached and mounted on kubelets host machine

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10669">property quobyte</a>
</h3>

```typescript
quobyte: QuobyteVolumeSource;
```


Quobyte represents a Quobyte mount on the host that shares a pod's lifetime

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10675">property rbd</a>
</h3>

```typescript
rbd: RBDPersistentVolumeSource;
```


RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More
info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10680">property scaleIO</a>
</h3>

```typescript
scaleIO: ScaleIOPersistentVolumeSource;
```


ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10686">property storageClassName</a>
</h3>

```typescript
storageClassName: string;
```


Name of StorageClass to which this persistent volume belongs. Empty value means that this
volume does not belong to any StorageClass.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10693">property storageos</a>
</h3>

```typescript
storageos: StorageOSPersistentVolumeSource;
```


StorageOS represents a StorageOS volume that is attached to the kubelet's host machine and
mounted into the pod More info:
https://releases.k8s.io/HEAD/examples/volumes/storageos/README.md

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10700">property volumeMode</a>
</h3>

```typescript
volumeMode: string;
```


volumeMode defines if a volume is intended to be used with a formatted filesystem or to
remain in raw block state. Value of Filesystem is implied when not included in spec. This
is an alpha feature and may change in the future.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10705">property vsphereVolume</a>
</h3>

```typescript
vsphereVolume: VsphereVirtualDiskVolumeSource;
```


VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine

<h2 class="pdoc-module-header" id="PersistentVolumeStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10712">interface PersistentVolumeStatus</a>
</h2>

PersistentVolumeStatus is the current status of a persistent volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10716">property message</a>
</h3>

```typescript
message: string;
```


A human-readable message indicating details about why the volume is in this state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10722">property phase</a>
</h3>

```typescript
phase: string;
```


Phase indicates if a volume is available, bound to a claim, or released by a claim. More
info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10728">property reason</a>
</h3>

```typescript
reason: string;
```


Reason is a brief CamelCase string that describes any failure and is meant for machine
parsing and tidy display in the CLI.

<h2 class="pdoc-module-header" id="PhotonPersistentDiskVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10735">interface PhotonPersistentDiskVolumeSource</a>
</h2>

Represents a Photon Controller persistent disk resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10740">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type to mount. Must be a filesystem type supported by the host operating system.
Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10745">property pdID</a>
</h3>

```typescript
pdID: string;
```


ID that identifies Photon Controller persistent disk

<h2 class="pdoc-module-header" id="Pod">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10753">interface Pod</a>
</h2>

Pod is a collection of containers that can run on a host. This resource is created by clients
and scheduled onto hosts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10760">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10768">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10774">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10780">property spec</a>
</h3>

```typescript
spec: PodSpec;
```


Specification of the desired behavior of the pod. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10787">property status</a>
</h3>

```typescript
status: PodStatus;
```


Most recently observed status of the pod. This data may not be up to date. Populated by the
system. Read-only. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h2 class="pdoc-module-header" id="PodAffinity">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10794">interface PodAffinity</a>
</h2>

Pod affinity is a group of inter pod affinity scheduling rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10805">property preferredDuringSchedulingIgnoredDuringExecution</a>
</h3>

```typescript
preferredDuringSchedulingIgnoredDuringExecution: WeightedPodAffinityTerm[];
```


The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions
specified by this field, but it may choose a node that violates one or more of the
expressions. The node that is most preferred is the one with the greatest sum of weights,
i.e. for each node that meets all of the scheduling requirements (resource request,
requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through
the elements of this field and adding "weight" to the sum if the node has pods which
matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most
preferred.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10815">property requiredDuringSchedulingIgnoredDuringExecution</a>
</h3>

```typescript
requiredDuringSchedulingIgnoredDuringExecution: PodAffinityTerm[];
```


If the affinity requirements specified by this field are not met at scheduling time, the
pod will not be scheduled onto the node. If the affinity requirements specified by this
field cease to be met at some point during pod execution (e.g. due to a pod label update),
the system may or may not try to eventually evict the pod from its node. When there are
multiple elements, the lists of nodes corresponding to each podAffinityTerm are
intersected, i.e. all terms must be satisfied.

<h2 class="pdoc-module-header" id="PodAffinityTerm">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10825">interface PodAffinityTerm</a>
</h2>

Defines a set of pods (namely those matching the labelSelector relative to the given
namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity)
with, where co-located is defined as running on a node whose value of the label with key
<topologyKey> matches that of any node on which a pod of the set of pods is running

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10829">property labelSelector</a>
</h3>

```typescript
labelSelector: LabelSelector;
```


A label query over a set of resources, in this case pods.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10835">property namespaces</a>
</h3>

```typescript
namespaces: string[];
```


namespaces specifies which namespaces the labelSelector applies to (matches against); null
or empty list means "this pod's namespace"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10843">property topologyKey</a>
</h3>

```typescript
topologyKey: string;
```


This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods
matching the labelSelector in the specified namespaces, where co-located is defined as
running on a node whose value of the label with key topologyKey matches that of any node on
which any of the selected pods is running. Empty topologyKey is not allowed.

<h2 class="pdoc-module-header" id="PodAntiAffinity">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10850">interface PodAntiAffinity</a>
</h2>

Pod anti affinity is a group of inter pod anti affinity scheduling rules.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10861">property preferredDuringSchedulingIgnoredDuringExecution</a>
</h3>

```typescript
preferredDuringSchedulingIgnoredDuringExecution: WeightedPodAffinityTerm[];
```


The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity
expressions specified by this field, but it may choose a node that violates one or more of
the expressions. The node that is most preferred is the one with the greatest sum of
weights, i.e. for each node that meets all of the scheduling requirements (resource
request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by
iterating through the elements of this field and adding "weight" to the sum if the node has
pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are
the most preferred.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10871">property requiredDuringSchedulingIgnoredDuringExecution</a>
</h3>

```typescript
requiredDuringSchedulingIgnoredDuringExecution: PodAffinityTerm[];
```


If the anti-affinity requirements specified by this field are not met at scheduling time,
the pod will not be scheduled onto the node. If the anti-affinity requirements specified by
this field cease to be met at some point during pod execution (e.g. due to a pod label
update), the system may or may not try to eventually evict the pod from its node. When
there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are
intersected, i.e. all terms must be satisfied.

<h2 class="pdoc-module-header" id="PodCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10878">interface PodCondition</a>
</h2>

PodCondition contains details for the current condition of this pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10882">property lastProbeTime</a>
</h3>

```typescript
lastProbeTime: string;
```


Last time we probed the condition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10887">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


Last time the condition transitioned from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10892">property message</a>
</h3>

```typescript
message: string;
```


Human-readable message indicating details about last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10897">property reason</a>
</h3>

```typescript
reason: string;
```


Unique, one-word, CamelCase reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10903">property status</a>
</h3>

```typescript
status: string;
```


Status is the status of the condition. Can be True, False, Unknown. More info:
https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10909">property type</a>
</h3>

```typescript
type: string;
```


Type is the type of the condition. More info:
https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions

<h2 class="pdoc-module-header" id="PodDNSConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10917">interface PodDNSConfig</a>
</h2>

PodDNSConfig defines the DNS parameters of a pod in addition to those generated from
DNSPolicy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10922">property nameservers</a>
</h3>

```typescript
nameservers: string[];
```


A list of DNS name server IP addresses. This will be appended to the base nameservers
generated from DNSPolicy. Duplicated nameservers will be removed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10929">property options</a>
</h3>

```typescript
options: PodDNSConfigOption[];
```


A list of DNS resolver options. This will be merged with the base options generated from
DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will
override those that appear in the base DNSPolicy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10935">property searches</a>
</h3>

```typescript
searches: string[];
```


A list of DNS search domains for host-name lookup. This will be appended to the base search
paths generated from DNSPolicy. Duplicated search paths will be removed.

<h2 class="pdoc-module-header" id="PodDNSConfigOption">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10942">interface PodDNSConfigOption</a>
</h2>

PodDNSConfigOption defines DNS resolver options of a pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10946">property name</a>
</h3>

```typescript
name: string;
```


Required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10949">property value</a>
</h3>

```typescript
value: string;
```

<h2 class="pdoc-module-header" id="PodList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10956">interface PodList</a>
</h2>

PodList is a list of Pods.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10963">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10968">property items</a>
</h3>

```typescript
items: Pod[];
```


List of pods. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10976">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10982">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="PodReadinessGate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10989">interface PodReadinessGate</a>
</h2>

PodReadinessGate contains the reference to a pod condition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L10993">property conditionType</a>
</h3>

```typescript
conditionType: string;
```


ConditionType refers to a condition in the pod's condition list with matching type.

<h2 class="pdoc-module-header" id="PodSecurityContext">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11002">interface PodSecurityContext</a>
</h2>

PodSecurityContext holds pod-level security attributes and common container settings. Some
fields are also present in container.securityContext.  Field values of
container.securityContext take precedence over field values of PodSecurityContext.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11012">property fsGroup</a>
</h3>

```typescript
fsGroup: number;
```


A special supplemental group that applies to all containers in a pod. Some volume types
allow the Kubelet to change the ownership of that volume to be owned by the pod:

1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the
volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw----

If unset, the Kubelet will not modify the ownership and permissions of any volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11019">property runAsGroup</a>
</h3>

```typescript
runAsGroup: number;
```


The GID to run the entrypoint of the container process. Uses runtime default if unset. May
also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the
value specified in SecurityContext takes precedence for that container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11028">property runAsNonRoot</a>
</h3>

```typescript
runAsNonRoot: boolean;
```


Indicates that the container must run as a non-root user. If true, the Kubelet will
validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to
start the container if it does. If unset or false, no such validation will be performed.
May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext,
the value specified in SecurityContext takes precedence.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11036">property runAsUser</a>
</h3>

```typescript
runAsUser: number;
```


The UID to run the entrypoint of the container process. Defaults to user specified in image
metadata if unspecified. May also be set in SecurityContext.  If set in both
SecurityContext and PodSecurityContext, the value specified in SecurityContext takes
precedence for that container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11044">property seLinuxOptions</a>
</h3>

```typescript
seLinuxOptions: SELinuxOptions;
```


The SELinux context to be applied to all containers. If unspecified, the container runtime
will allocate a random SELinux context for each container.  May also be set in
SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value
specified in SecurityContext takes precedence for that container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11050">property supplementalGroups</a>
</h3>

```typescript
supplementalGroups: number[];
```


A list of groups applied to the first process run in each container, in addition to the
container's primary GID.  If unspecified, no groups will be added to any container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11056">property sysctls</a>
</h3>

```typescript
sysctls: Sysctl[];
```


Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls
(by the container runtime) might fail to launch.

<h2 class="pdoc-module-header" id="PodSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11063">interface PodSpec</a>
</h2>

PodSpec is a description of a pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11069">property activeDeadlineSeconds</a>
</h3>

```typescript
activeDeadlineSeconds: number;
```


Optional duration in seconds the pod may be active on the node relative to StartTime before
the system will actively try to mark it failed and kill associated containers. Value must
be a positive integer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11074">property affinity</a>
</h3>

```typescript
affinity: Affinity;
```


If specified, the pod's scheduling constraints

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11080">property automountServiceAccountToken</a>
</h3>

```typescript
automountServiceAccountToken: boolean;
```


AutomountServiceAccountToken indicates whether a service account token should be
automatically mounted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11086">property containers</a>
</h3>

```typescript
containers: Container[];
```


List of containers belonging to the pod. Containers cannot currently be added or removed.
There must be at least one container in a Pod. Cannot be updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11092">property dnsConfig</a>
</h3>

```typescript
dnsConfig: PodDNSConfig;
```


Specifies the DNS parameters of a pod. Parameters specified here will be merged to the
generated DNS configuration based on DNSPolicy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11101">property dnsPolicy</a>
</h3>

```typescript
dnsPolicy: string;
```


Set DNS policy for the pod. Defaults to "ClusterFirst". Valid values are
'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in
DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set
along with hostNetwork, you have to specify DNS policy explicitly to
'ClusterFirstWithHostNet'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11107">property hostAliases</a>
</h3>

```typescript
hostAliases: HostAlias[];
```


HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts
file if specified. This is only valid for non-hostNetwork pods.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11112">property hostIPC</a>
</h3>

```typescript
hostIPC: boolean;
```


Use the host's ipc namespace. Optional: Default to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11118">property hostNetwork</a>
</h3>

```typescript
hostNetwork: boolean;
```


Host networking requested for this pod. Use the host's network namespace. If this option is
set, the ports that will be used must be specified. Default to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11123">property hostPID</a>
</h3>

```typescript
hostPID: boolean;
```


Use the host's pid namespace. Optional: Default to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11129">property hostname</a>
</h3>

```typescript
hostname: string;
```


Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a
system-defined value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11138">property imagePullSecrets</a>
</h3>

```typescript
imagePullSecrets: LocalObjectReference[];
```


ImagePullSecrets is an optional list of references to secrets in the same namespace to use
for pulling any of the images used by this PodSpec. If specified, these secrets will be
passed to individual puller implementations for them to use. For example, in the case of
docker, only DockerConfig type secrets are honored. More info:
https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11152">property initContainers</a>
</h3>

```typescript
initContainers: Container[];
```


List of initialization containers belonging to the pod. Init containers are executed in
order prior to containers being started. If any init container fails, the pod is considered
to have failed and is handled according to its restartPolicy. The name for an init
container or normal container must be unique among all containers. Init containers may not
have Lifecycle actions, Readiness probes, or Liveness probes. The resourceRequirements of
an init container are taken into account during scheduling by finding the highest
request/limit for each resource type, and then using the max of of that value or the sum of
the normal containers. Limits are applied to init containers in a similar fashion. Init
containers cannot currently be added or removed. Cannot be updated. More info:
https://kubernetes.io/docs/concepts/workloads/pods/init-containers/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11159">property nodeName</a>
</h3>

```typescript
nodeName: string;
```


NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the
scheduler simply schedules this pod onto that node, assuming that it fits resource
requirements.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11166">property nodeSelector</a>
</h3>

```typescript
nodeSelector: { ... };
```


NodeSelector is a selector which must be true for the pod to fit on a node. Selector which
must match a node's labels for the pod to be scheduled on that node. More info:
https://kubernetes.io/docs/concepts/configuration/assign-pod-node/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11174">property priority</a>
</h3>

```typescript
priority: number;
```


The priority value. Various system components use this field to find the priority of the
pod. When Priority Admission Controller is enabled, it prevents users from setting this
field. The admission controller populates this field from PriorityClassName. The higher the
value, the higher the priority.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11183">property priorityClassName</a>
</h3>

```typescript
priorityClassName: string;
```


If specified, indicates the pod's priority. "system-node-critical" and
"system-cluster-critical" are two special keywords which indicate the highest priorities
with the former being the highest priority. Any other name must be defined by creating a
PriorityClass object with that name. If not specified, the pod priority will be default or
zero if there is no default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11191">property readinessGates</a>
</h3>

```typescript
readinessGates: PodReadinessGate[];
```


If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when
all its containers are ready AND all conditions specified in the readiness gates have
status equal to "True" More info:
https://github.com/kubernetes/community/blob/master/keps/sig-network/0007-pod-ready%2B%2B.md

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11198">property restartPolicy</a>
</h3>

```typescript
restartPolicy: string;
```


Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default
to Always. More info:
https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11208">property runtimeClassName</a>
</h3>

```typescript
runtimeClassName: string;
```


RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be
used to run this pod.  If no RuntimeClass resource matches the named class, the pod will
not be run. If unset or empty, the "legacy" RuntimeClass will be used, which is an implicit
class with an empty definition that uses the default runtime handler. More info:
https://github.com/kubernetes/community/blob/master/keps/sig-node/0014-runtime-class.md
This is an alpha feature and may change in the future.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11214">property schedulerName</a>
</h3>

```typescript
schedulerName: string;
```


If specified, the pod will be dispatched by specified scheduler. If not specified, the pod
will be dispatched by default scheduler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11220">property securityContext</a>
</h3>

```typescript
securityContext: PodSecurityContext;
```


SecurityContext holds pod-level security attributes and common container settings.
Optional: Defaults to empty.  See type description for default values of each field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11226">property serviceAccount</a>
</h3>

```typescript
serviceAccount: string;
```


DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use
serviceAccountName instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11232">property serviceAccountName</a>
</h3>

```typescript
serviceAccountName: string;
```


ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info:
https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11241">property shareProcessNamespace</a>
</h3>

```typescript
shareProcessNamespace: boolean;
```


Share a single process namespace between all of the containers in a pod. When this is set
containers will be able to view and signal processes from other containers in the same pod,
and the first process in each container will not be assigned PID 1. HostPID and
ShareProcessNamespace cannot both be set. Optional: Default to false. This field is
beta-level and may be disabled with the PodShareProcessNamespace feature.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11248">property subdomain</a>
</h3>

```typescript
subdomain: string;
```


If specified, the fully qualified Pod hostname will be "<hostname>.<subdomain>.<pod
namespace>.svc.<cluster domain>". If not specified, the pod will not have a domainname at
all.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11259">property terminationGracePeriodSeconds</a>
</h3>

```typescript
terminationGracePeriodSeconds: number;
```


Optional duration in seconds the pod needs to terminate gracefully. May be decreased in
delete request. Value must be non-negative integer. The value zero indicates delete
immediately. If this value is nil, the default grace period will be used instead. The grace
period is the duration in seconds after the processes running in the pod are sent a
termination signal and the time when the processes are forcibly halted with a kill signal.
Set this value longer than the expected cleanup time for your process. Defaults to 30
seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11264">property tolerations</a>
</h3>

```typescript
tolerations: Toleration[];
```


If specified, the pod's tolerations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11270">property volumes</a>
</h3>

```typescript
volumes: Volume[];
```


List of volumes that can be mounted by containers belonging to the pod. More info:
https://kubernetes.io/docs/concepts/storage/volumes

<h2 class="pdoc-module-header" id="PodStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11278">interface PodStatus</a>
</h2>

PodStatus represents information about the status of a pod. Status may trail the actual state
of a system, especially if the node that hosts the pod cannot contact the control plane.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11283">property conditions</a>
</h3>

```typescript
conditions: PodCondition[];
```


Current service state of pod. More info:
https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11290">property containerStatuses</a>
</h3>

```typescript
containerStatuses: ContainerStatus[];
```


The list has one entry per container in the manifest. Each entry is currently the output of
`docker inspect`. More info:
https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11295">property hostIP</a>
</h3>

```typescript
hostIP: string;
```


IP address of the host to which the pod is assigned. Empty if not yet scheduled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11303">property initContainerStatuses</a>
</h3>

```typescript
initContainerStatuses: ContainerStatus[];
```


The list has one entry per init container in the manifest. The most recent successful init
container will have ready = true, the most recently started container will have startTime
set. More info:
https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11308">property message</a>
</h3>

```typescript
message: string;
```


A human readable message indicating details about why the pod is in this condition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11319">property nominatedNodeName</a>
</h3>

```typescript
nominatedNodeName: string;
```


nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot
be scheduled right away as preemption victims receive their graceful termination periods.
This field does not guarantee that the pod will be scheduled on this node. Scheduler may
decide to place the pod elsewhere if other nodes become available sooner. Scheduler may
also decide to give the resources on this node to a higher priority pod that is created
after preemption. As a result, this field may be different than PodSpec.nodeName when the
pod is scheduled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11339">property phase</a>
</h3>

```typescript
phase: string;
```


The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle.
The conditions array, the reason and message fields, and the individual container status
arrays contain more detail about the pod's status. There are five possible phase values:

Pending: The pod has been accepted by the Kubernetes system, but one or more of the
container images has not been created. This includes time before being scheduled as well as
time spent downloading images over the network, which could take a while. Running: The pod
has been bound to a node, and all of the containers have been created. At least one
container is still running, or is in the process of starting or restarting. Succeeded: All
containers in the pod have terminated in success, and will not be restarted. Failed: All
containers in the pod have terminated, and at least one container has terminated in
failure. The container either exited with non-zero status or was terminated by the system.
Unknown: For some reason the state of the pod could not be obtained, typically due to an
error in communicating with the host of the pod.

More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11345">property podIP</a>
</h3>

```typescript
podIP: string;
```


IP address allocated to the pod. Routable at least within the cluster. Empty if not yet
allocated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11352">property qosClass</a>
</h3>

```typescript
qosClass: string;
```


The Quality of Service (QOS) classification assigned to the pod based on resource
requirements See PodQOSClass type for available QOS classes More info:
https://git.k8s.io/community/contributors/design-proposals/node/resource-qos.md

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11358">property reason</a>
</h3>

```typescript
reason: string;
```


A brief CamelCase message indicating details about why the pod is in this state. e.g.
'Evicted'

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11364">property startTime</a>
</h3>

```typescript
startTime: string;
```


RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before
the Kubelet pulled the container image(s) for the pod.

<h2 class="pdoc-module-header" id="PodTemplate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11371">interface PodTemplate</a>
</h2>

PodTemplate describes a template for creating copies of a predefined pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11378">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11386">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11392">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11398">property template</a>
</h3>

```typescript
template: PodTemplateSpec;
```


Template defines the pods that will be created from this pod template.
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h2 class="pdoc-module-header" id="PodTemplateList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11405">interface PodTemplateList</a>
</h2>

PodTemplateList is a list of PodTemplates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11412">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11417">property items</a>
</h3>

```typescript
items: PodTemplate[];
```


List of pod templates

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11425">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11431">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="PodTemplateSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11438">interface PodTemplateSpec</a>
</h2>

PodTemplateSpec describes the data a pod should have when created from a template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11443">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11449">property spec</a>
</h3>

```typescript
spec: PodSpec;
```


Specification of the desired behavior of the pod. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h2 class="pdoc-module-header" id="PortworxVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11456">interface PortworxVolumeSource</a>
</h2>

PortworxVolumeSource represents a Portworx volume resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11461">property fsType</a>
</h3>

```typescript
fsType: string;
```


FSType represents the filesystem type to mount Must be a filesystem type supported by the
host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11467">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
VolumeMounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11472">property volumeID</a>
</h3>

```typescript
volumeID: string;
```


VolumeID uniquely identifies a Portworx volume

<h2 class="pdoc-module-header" id="PreferredSchedulingTerm">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11480">interface PreferredSchedulingTerm</a>
</h2>

An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a
no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11484">property preference</a>
</h3>

```typescript
preference: NodeSelectorTerm;
```


A node selector term, associated with the corresponding weight.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11489">property weight</a>
</h3>

```typescript
weight: number;
```


Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.

<h2 class="pdoc-module-header" id="Probe">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11497">interface Probe</a>
</h2>

Probe describes a health check to be performed against a container to determine whether it is
alive or ready to receive traffic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11501">property exec</a>
</h3>

```typescript
exec: ExecAction;
```


One and only one of the following should be specified. Exec specifies the action to take.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11507">property failureThreshold</a>
</h3>

```typescript
failureThreshold: number;
```


Minimum consecutive failures for the probe to be considered failed after having succeeded.
Defaults to 3. Minimum value is 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11512">property httpGet</a>
</h3>

```typescript
httpGet: HTTPGetAction;
```


HTTPGet specifies the http request to perform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11519">property initialDelaySeconds</a>
</h3>

```typescript
initialDelaySeconds: number;
```


Number of seconds after the container has started before liveness probes are initiated.
More info:
https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11524">property periodSeconds</a>
</h3>

```typescript
periodSeconds: number;
```


How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11530">property successThreshold</a>
</h3>

```typescript
successThreshold: number;
```


Minimum consecutive successes for the probe to be considered successful after having
failed. Defaults to 1. Must be 1 for liveness. Minimum value is 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11535">property tcpSocket</a>
</h3>

```typescript
tcpSocket: TCPSocketAction;
```


TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11542">property timeoutSeconds</a>
</h3>

```typescript
timeoutSeconds: number;
```


Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is
1. More info:
https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes

<h2 class="pdoc-module-header" id="ProjectedVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11549">interface ProjectedVolumeSource</a>
</h2>

Represents a projected volume source

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11556">property defaultMode</a>
</h3>

```typescript
defaultMode: number;
```


Mode bits to use on created files by default. Must be a value between 0 and 0777.
Directories within the path are not affected by this setting. This might be in conflict
with other options that affect the file mode, like fsGroup, and the result can be other
mode bits set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11561">property sources</a>
</h3>

```typescript
sources: VolumeProjection[];
```


list of volume projections

<h2 class="pdoc-module-header" id="QuobyteVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11569">interface QuobyteVolumeSource</a>
</h2>

Represents a Quobyte mount that lasts the lifetime of a pod. Quobyte volumes do not support
ownership management or SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11573">property group</a>
</h3>

```typescript
group: string;
```


Group to map volume access to Default is no group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11579">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


ReadOnly here will force the Quobyte volume to be mounted with read-only permissions.
Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11586">property registry</a>
</h3>

```typescript
registry: string;
```


Registry represents a single or multiple Quobyte Registry services specified as a string as
host:port pair (multiple entries are separated with commas) which acts as the central
registry for volumes

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11591">property user</a>
</h3>

```typescript
user: string;
```


User to map volume access to Defaults to serivceaccount user

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11596">property volume</a>
</h3>

```typescript
volume: string;
```


Volume is a string that references an already created Quobyte volume by name.

<h2 class="pdoc-module-header" id="RBDPersistentVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11604">interface RBDPersistentVolumeSource</a>
</h2>

Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support
ownership management and SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11611">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type
is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly
inferred to be "ext4" if unspecified. More info:
https://kubernetes.io/docs/concepts/storage/volumes#rbd

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11617">property image</a>
</h3>

```typescript
image: string;
```


The rados image name. More info:
https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11623">property keyring</a>
</h3>

```typescript
keyring: string;
```


Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info:
https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11629">property monitors</a>
</h3>

```typescript
monitors: string[];
```


A collection of Ceph monitors. More info:
https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11635">property pool</a>
</h3>

```typescript
pool: string;
```


The rados pool name. Default is rbd. More info:
https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11641">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More
info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11648">property secretRef</a>
</h3>

```typescript
secretRef: SecretReference;
```


SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring.
Default is nil. More info:
https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11654">property user</a>
</h3>

```typescript
user: string;
```


The rados user name. Default is admin. More info:
https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

<h2 class="pdoc-module-header" id="RBDVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11662">interface RBDVolumeSource</a>
</h2>

Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support
ownership management and SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11669">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type
is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly
inferred to be "ext4" if unspecified. More info:
https://kubernetes.io/docs/concepts/storage/volumes#rbd

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11675">property image</a>
</h3>

```typescript
image: string;
```


The rados image name. More info:
https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11681">property keyring</a>
</h3>

```typescript
keyring: string;
```


Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info:
https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11687">property monitors</a>
</h3>

```typescript
monitors: string[];
```


A collection of Ceph monitors. More info:
https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11693">property pool</a>
</h3>

```typescript
pool: string;
```


The rados pool name. Default is rbd. More info:
https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11699">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More
info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11706">property secretRef</a>
</h3>

```typescript
secretRef: LocalObjectReference;
```


SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring.
Default is nil. More info:
https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11712">property user</a>
</h3>

```typescript
user: string;
```


The rados user name. Default is admin. More info:
https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

<h2 class="pdoc-module-header" id="ReplicationController">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11719">interface ReplicationController</a>
</h2>

ReplicationController represents the configuration of a replication controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11726">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11734">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11741">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


If the Labels of a ReplicationController are empty, they are defaulted to be the same as
the Pod(s) that the replication controller manages. Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11747">property spec</a>
</h3>

```typescript
spec: ReplicationControllerSpec;
```


Spec defines the specification of the desired behavior of the replication controller. More
info: https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11754">property status</a>
</h3>

```typescript
status: ReplicationControllerStatus;
```


Status is the most recently observed status of the replication controller. This data may be
out of date by some window of time. Populated by the system. Read-only. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h2 class="pdoc-module-header" id="ReplicationControllerCondition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11762">interface ReplicationControllerCondition</a>
</h2>

ReplicationControllerCondition describes the state of a replication controller at a certain
point.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11766">property lastTransitionTime</a>
</h3>

```typescript
lastTransitionTime: string;
```


The last time the condition transitioned from one status to another.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11771">property message</a>
</h3>

```typescript
message: string;
```


A human readable message indicating details about the transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11776">property reason</a>
</h3>

```typescript
reason: string;
```


The reason for the condition's last transition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11781">property status</a>
</h3>

```typescript
status: string;
```


Status of the condition, one of True, False, Unknown.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11786">property type</a>
</h3>

```typescript
type: string;
```


Type of replication controller condition.

<h2 class="pdoc-module-header" id="ReplicationControllerList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11793">interface ReplicationControllerList</a>
</h2>

ReplicationControllerList is a collection of replication controllers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11800">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11806">property items</a>
</h3>

```typescript
items: ReplicationController[];
```


List of replication controllers. More info:
https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11814">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11820">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="ReplicationControllerSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11827">interface ReplicationControllerSpec</a>
</h2>

ReplicationControllerSpec is the specification of a replication controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11833">property minReadySeconds</a>
</h3>

```typescript
minReadySeconds: number;
```


Minimum number of seconds for which a newly created pod should be ready without any of its
container crashing, for it to be considered available. Defaults to 0 (pod will be
considered available as soon as it is ready)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11840">property replicas</a>
</h3>

```typescript
replicas: number;
```


Replicas is the number of desired replicas. This is a pointer to distinguish between
explicit zero and unspecified. Defaults to 1. More info:
https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11849">property selector</a>
</h3>

```typescript
selector: { ... };
```


Selector is a label query over pods that should match the Replicas count. If Selector is
empty, it is defaulted to the labels present on the Pod template. Label keys and values
that must match in order to be controlled by this replication controller, if empty
defaulted to labels on Pod template. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11856">property template</a>
</h3>

```typescript
template: PodTemplateSpec;
```


Template is the object that describes the pod that will be created if insufficient replicas
are detected. This takes precedence over a TemplateRef. More info:
https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template

<h2 class="pdoc-module-header" id="ReplicationControllerStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11863">interface ReplicationControllerStatus</a>
</h2>

ReplicationControllerStatus represents the current status of a replication controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11868">property availableReplicas</a>
</h3>

```typescript
availableReplicas: number;
```


The number of available replicas (ready for at least minReadySeconds) for this replication
controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11873">property conditions</a>
</h3>

```typescript
conditions: ReplicationControllerCondition[];
```


Represents the latest available observations of a replication controller's current state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11879">property fullyLabeledReplicas</a>
</h3>

```typescript
fullyLabeledReplicas: number;
```


The number of pods that have labels matching the labels of the pod template of the
replication controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11885">property observedGeneration</a>
</h3>

```typescript
observedGeneration: number;
```


ObservedGeneration reflects the generation of the most recently observed replication
controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11890">property readyReplicas</a>
</h3>

```typescript
readyReplicas: number;
```


The number of ready replicas for this replication controller.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11896">property replicas</a>
</h3>

```typescript
replicas: number;
```


Replicas is the most recently oberved number of replicas. More info:
https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller

<h2 class="pdoc-module-header" id="ResourceFieldSelector">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11903">interface ResourceFieldSelector</a>
</h2>

ResourceFieldSelector represents container resources (cpu, memory) and their output format

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11907">property containerName</a>
</h3>

```typescript
containerName: string;
```


Container name: required for volumes, optional for env vars

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11912">property divisor</a>
</h3>

```typescript
divisor: string;
```


Specifies the output format of the exposed resources, defaults to "1"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11917">property resource</a>
</h3>

```typescript
resource: string;
```


Required: resource to select

<h2 class="pdoc-module-header" id="ResourceQuota">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11924">interface ResourceQuota</a>
</h2>

ResourceQuota sets aggregate quota restrictions enforced per namespace

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11931">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11939">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11945">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11951">property spec</a>
</h3>

```typescript
spec: ResourceQuotaSpec;
```


Spec defines the desired quota.
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11957">property status</a>
</h3>

```typescript
status: ResourceQuotaStatus;
```


Status defines the actual enforced quota and its current usage.
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h2 class="pdoc-module-header" id="ResourceQuotaList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11964">interface ResourceQuotaList</a>
</h2>

ResourceQuotaList is a list of ResourceQuota items.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11971">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11977">property items</a>
</h3>

```typescript
items: ResourceQuota[];
```


Items is a list of ResourceQuota objects. More info:
https://kubernetes.io/docs/concepts/policy/resource-quotas/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11985">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11991">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="ResourceQuotaSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L11998">interface ResourceQuotaSpec</a>
</h2>

ResourceQuotaSpec defines the desired hard limits to enforce for Quota.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12003">property hard</a>
</h3>

```typescript
hard: object;
```


hard is the set of desired hard limits for each named resource. More info:
https://kubernetes.io/docs/concepts/policy/resource-quotas/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12011">property scopeSelector</a>
</h3>

```typescript
scopeSelector: ScopeSelector;
```


scopeSelector is also a collection of filters like scopes that must match each object
tracked by a quota but expressed using ScopeSelectorOperator in combination with possible
values. For a resource to match, both scopes AND scopeSelector (if specified in spec), must
be matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12017">property scopes</a>
</h3>

```typescript
scopes: string[];
```


A collection of filters that must match each object tracked by a quota. If not specified,
the quota matches all objects.

<h2 class="pdoc-module-header" id="ResourceQuotaStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12024">interface ResourceQuotaStatus</a>
</h2>

ResourceQuotaStatus defines the enforced hard limits and observed use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12029">property hard</a>
</h3>

```typescript
hard: object;
```


Hard is the set of enforced hard limits for each named resource. More info:
https://kubernetes.io/docs/concepts/policy/resource-quotas/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12034">property used</a>
</h3>

```typescript
used: object;
```


Used is the current observed total usage of the resource in the namespace.

<h2 class="pdoc-module-header" id="ResourceRequirements">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12041">interface ResourceRequirements</a>
</h2>

ResourceRequirements describes the compute resource requirements.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12046">property limits</a>
</h3>

```typescript
limits: object;
```


Limits describes the maximum amount of compute resources allowed. More info:
https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12054">property requests</a>
</h3>

```typescript
requests: object;
```


Requests describes the minimum amount of compute resources required. If Requests is omitted
for a container, it defaults to Limits if that is explicitly specified, otherwise to an
implementation-defined value. More info:
https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/

<h2 class="pdoc-module-header" id="SELinuxOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12061">interface SELinuxOptions</a>
</h2>

SELinuxOptions are the labels to be applied to the container

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12065">property level</a>
</h3>

```typescript
level: string;
```


Level is SELinux level label that applies to the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12070">property role</a>
</h3>

```typescript
role: string;
```


Role is a SELinux role label that applies to the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12075">property type</a>
</h3>

```typescript
type: string;
```


Type is a SELinux type label that applies to the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12080">property user</a>
</h3>

```typescript
user: string;
```


User is a SELinux user label that applies to the container.

<h2 class="pdoc-module-header" id="ScaleIOPersistentVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12087">interface ScaleIOPersistentVolumeSource</a>
</h2>

ScaleIOPersistentVolumeSource represents a persistent ScaleIO volume

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12092">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type to mount. Must be a filesystem type supported by the host operating system.
Ex. "ext4", "xfs", "ntfs". Default is "xfs"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12097">property gateway</a>
</h3>

```typescript
gateway: string;
```


The host address of the ScaleIO API Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12102">property protectionDomain</a>
</h3>

```typescript
protectionDomain: string;
```


The name of the ScaleIO Protection Domain for the configured storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12108">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
VolumeMounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12114">property secretRef</a>
</h3>

```typescript
secretRef: SecretReference;
```


SecretRef references to the secret for ScaleIO user and other sensitive information. If
this is not provided, Login operation will fail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12119">property sslEnabled</a>
</h3>

```typescript
sslEnabled: boolean;
```


Flag to enable/disable SSL communication with Gateway, default false

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12125">property storageMode</a>
</h3>

```typescript
storageMode: string;
```


Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned.
Default is ThinProvisioned.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12130">property storagePool</a>
</h3>

```typescript
storagePool: string;
```


The ScaleIO Storage Pool associated with the protection domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12135">property system</a>
</h3>

```typescript
system: string;
```


The name of the storage system as configured in ScaleIO.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12141">property volumeName</a>
</h3>

```typescript
volumeName: string;
```


The name of a volume already created in the ScaleIO system that is associated with this
volume source.

<h2 class="pdoc-module-header" id="ScaleIOVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12148">interface ScaleIOVolumeSource</a>
</h2>

ScaleIOVolumeSource represents a persistent ScaleIO volume

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12153">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type to mount. Must be a filesystem type supported by the host operating system.
Ex. "ext4", "xfs", "ntfs". Default is "xfs".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12158">property gateway</a>
</h3>

```typescript
gateway: string;
```


The host address of the ScaleIO API Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12163">property protectionDomain</a>
</h3>

```typescript
protectionDomain: string;
```


The name of the ScaleIO Protection Domain for the configured storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12169">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
VolumeMounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12175">property secretRef</a>
</h3>

```typescript
secretRef: LocalObjectReference;
```


SecretRef references to the secret for ScaleIO user and other sensitive information. If
this is not provided, Login operation will fail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12180">property sslEnabled</a>
</h3>

```typescript
sslEnabled: boolean;
```


Flag to enable/disable SSL communication with Gateway, default false

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12186">property storageMode</a>
</h3>

```typescript
storageMode: string;
```


Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned.
Default is ThinProvisioned.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12191">property storagePool</a>
</h3>

```typescript
storagePool: string;
```


The ScaleIO Storage Pool associated with the protection domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12196">property system</a>
</h3>

```typescript
system: string;
```


The name of the storage system as configured in ScaleIO.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12202">property volumeName</a>
</h3>

```typescript
volumeName: string;
```


The name of a volume already created in the ScaleIO system that is associated with this
volume source.

<h2 class="pdoc-module-header" id="ScopeSelector">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12210">interface ScopeSelector</a>
</h2>

A scope selector represents the AND of the selectors represented by the scoped-resource
selector requirements.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12214">property matchExpressions</a>
</h3>

```typescript
matchExpressions: ScopedResourceSelectorRequirement[];
```


A list of scope selector requirements by scope of the resources.

<h2 class="pdoc-module-header" id="ScopedResourceSelectorRequirement">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12222">interface ScopedResourceSelectorRequirement</a>
</h2>

A scoped-resource selector requirement is a selector that contains values, a scope name, and
an operator that relates the scope name and values.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12227">property operator</a>
</h3>

```typescript
operator: string;
```


Represents a scope's relationship to a set of values. Valid operators are In, NotIn,
Exists, DoesNotExist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12232">property scopeName</a>
</h3>

```typescript
scopeName: string;
```


The name of the scope that the selector applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12239">property values</a>
</h3>

```typescript
values: string[];
```


An array of string values. If the operator is In or NotIn, the values array must be
non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This
array is replaced during a strategic merge patch.

<h2 class="pdoc-module-header" id="Secret">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12247">interface Secret</a>
</h2>

Secret holds secret data of a certain type. The total bytes of the values in the Data field
must be less than MaxSecretSize bytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12254">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12262">property data</a>
</h3>

```typescript
data: object;
```


Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_'
or '.'. The serialized form of the secret data is a base64 encoded string, representing the
arbitrary (possibly non-string) data value here. Described in
https://tools.ietf.org/html/rfc4648#section-4

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12270">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12276">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12283">property stringData</a>
</h3>

```typescript
stringData: { ... };
```


stringData allows specifying non-binary secret data in string form. It is provided as a
write-only convenience method. All keys and values are merged into the data field on write,
overwriting any existing values. It is never output when reading from the API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12288">property type</a>
</h3>

```typescript
type: string;
```


Used to facilitate programmatic handling of secret data.

<h2 class="pdoc-module-header" id="SecretEnvSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12298">interface SecretEnvSource</a>
</h2>

SecretEnvSource selects a Secret to populate the environment variables with.

The contents of the target Secret's Data field will represent the key-value pairs as
environment variables.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12303">property name</a>
</h3>

```typescript
name: string;
```


Name of the referent. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12308">property optional</a>
</h3>

```typescript
optional: boolean;
```


Specify whether the Secret must be defined

<h2 class="pdoc-module-header" id="SecretKeySelector">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12315">interface SecretKeySelector</a>
</h2>

SecretKeySelector selects a key of a Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12319">property key</a>
</h3>

```typescript
key: string;
```


The key of the secret to select from.  Must be a valid secret key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12325">property name</a>
</h3>

```typescript
name: string;
```


Name of the referent. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12330">property optional</a>
</h3>

```typescript
optional: boolean;
```


Specify whether the Secret or it's key must be defined

<h2 class="pdoc-module-header" id="SecretList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12337">interface SecretList</a>
</h2>

SecretList is a list of Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12344">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12350">property items</a>
</h3>

```typescript
items: Secret[];
```


Items is a list of secret objects. More info:
https://kubernetes.io/docs/concepts/configuration/secret

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12358">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12364">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="SecretProjection">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12375">interface SecretProjection</a>
</h2>

Adapts a secret into a projected volume.

The contents of the target Secret's Data field will be presented in a projected volume as
files using the keys in the Data field as the file names. Note that this is identical to a
secret volume source without the default mode.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12384">property items</a>
</h3>

```typescript
items: KeyToPath[];
```


If unspecified, each key-value pair in the Data field of the referenced Secret will be
projected into the volume as a file whose name is the key and content is the value. If
specified, the listed keys will be projected into the specified paths, and unlisted keys
will not be present. If a key is specified which is not present in the Secret, the volume
setup will error unless it is marked optional. Paths must be relative and may not contain
the '..' path or start with '..'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12390">property name</a>
</h3>

```typescript
name: string;
```


Name of the referent. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12395">property optional</a>
</h3>

```typescript
optional: boolean;
```


Specify whether the Secret or its key must be defined

<h2 class="pdoc-module-header" id="SecretReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12403">interface SecretReference</a>
</h2>

SecretReference represents a Secret Reference. It has enough information to retrieve secret
in any namespace

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12407">property name</a>
</h3>

```typescript
name: string;
```


Name is unique within a namespace to reference a secret resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12412">property namespace</a>
</h3>

```typescript
namespace: string;
```


Namespace defines the space within which the secret name must be unique.

<h2 class="pdoc-module-header" id="SecretVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12423">interface SecretVolumeSource</a>
</h2>

Adapts a Secret into a volume.

The contents of the target Secret's Data field will be presented in a volume as files using
the keys in the Data field as the file names. Secret volumes support ownership management and
SELinux relabeling.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12430">property defaultMode</a>
</h3>

```typescript
defaultMode: number;
```


Optional: mode bits to use on created files by default. Must be a value between 0 and 0777.
Defaults to 0644. Directories within the path are not affected by this setting. This might
be in conflict with other options that affect the file mode, like fsGroup, and the result
can be other mode bits set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12440">property items</a>
</h3>

```typescript
items: KeyToPath[];
```


If unspecified, each key-value pair in the Data field of the referenced Secret will be
projected into the volume as a file whose name is the key and content is the value. If
specified, the listed keys will be projected into the specified paths, and unlisted keys
will not be present. If a key is specified which is not present in the Secret, the volume
setup will error unless it is marked optional. Paths must be relative and may not contain
the '..' path or start with '..'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12445">property optional</a>
</h3>

```typescript
optional: boolean;
```


Specify whether the Secret or it's keys must be defined

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12451">property secretName</a>
</h3>

```typescript
secretName: string;
```


Name of the secret in the pod's namespace to use. More info:
https://kubernetes.io/docs/concepts/storage/volumes#secret

<h2 class="pdoc-module-header" id="SecurityContext">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12460">interface SecurityContext</a>
</h2>

SecurityContext holds security configuration that will be applied to a container. Some fields
are present in both SecurityContext and PodSecurityContext.  When both are set, the values in
SecurityContext take precedence.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12467">property allowPrivilegeEscalation</a>
</h3>

```typescript
allowPrivilegeEscalation: boolean;
```


AllowPrivilegeEscalation controls whether a process can gain more privileges than its
parent process. This bool directly controls if the no_new_privs flag will be set on the
container process. AllowPrivilegeEscalation is true always when the container is: 1) run as
Privileged 2) has CAP_SYS_ADMIN

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12473">property capabilities</a>
</h3>

```typescript
capabilities: Capabilities;
```


The capabilities to add/drop when running containers. Defaults to the default set of
capabilities granted by the container runtime.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12479">property privileged</a>
</h3>

```typescript
privileged: boolean;
```


Run container in privileged mode. Processes in privileged containers are essentially
equivalent to root on the host. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12486">property procMount</a>
</h3>

```typescript
procMount: string;
```


procMount denotes the type of proc mount to use for the containers. The default is
DefaultProcMount which uses the container runtime defaults for readonly paths and masked
paths. This requires the ProcMountType feature flag to be enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12491">property readOnlyRootFilesystem</a>
</h3>

```typescript
readOnlyRootFilesystem: boolean;
```


Whether this container has a read-only root filesystem. Default is false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12498">property runAsGroup</a>
</h3>

```typescript
runAsGroup: number;
```


The GID to run the entrypoint of the container process. Uses runtime default if unset. May
also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext,
the value specified in SecurityContext takes precedence.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12507">property runAsNonRoot</a>
</h3>

```typescript
runAsNonRoot: boolean;
```


Indicates that the container must run as a non-root user. If true, the Kubelet will
validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to
start the container if it does. If unset or false, no such validation will be performed.
May also be set in PodSecurityContext.  If set in both SecurityContext and
PodSecurityContext, the value specified in SecurityContext takes precedence.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12515">property runAsUser</a>
</h3>

```typescript
runAsUser: number;
```


The UID to run the entrypoint of the container process. Defaults to user specified in image
metadata if unspecified. May also be set in PodSecurityContext.  If set in both
SecurityContext and PodSecurityContext, the value specified in SecurityContext takes
precedence.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12523">property seLinuxOptions</a>
</h3>

```typescript
seLinuxOptions: SELinuxOptions;
```


The SELinux context to be applied to the container. If unspecified, the container runtime
will allocate a random SELinux context for each container.  May also be set in
PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value
specified in SecurityContext takes precedence.

<h2 class="pdoc-module-header" id="Service">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12532">interface Service</a>
</h2>

Service is a named abstraction of software service (for example, mysql) consisting of local
port (for example 3306) that the proxy listens on, and the selector that determines which
pods will answer requests sent through the proxy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12539">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12547">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12553">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12559">property spec</a>
</h3>

```typescript
spec: ServiceSpec;
```


Spec defines the behavior of a service.
https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12565">property status</a>
</h3>

```typescript
status: ServiceStatus;
```


Most recently observed status of the service. Populated by the system. Read-only. More
info: https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status

<h2 class="pdoc-module-header" id="ServiceAccount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12574">interface ServiceAccount</a>
</h2>

ServiceAccount binds together: * a name, understood by users, and perhaps by peripheral
systems, for an identity * a principal that can be authenticated and authorized * a set of
secrets

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12581">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12587">property automountServiceAccountToken</a>
</h3>

```typescript
automountServiceAccountToken: boolean;
```


AutomountServiceAccountToken indicates whether pods running as this service account should
have an API token automatically mounted. Can be overridden at the pod level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12596">property imagePullSecrets</a>
</h3>

```typescript
imagePullSecrets: LocalObjectReference[];
```


ImagePullSecrets is a list of references to secrets in the same namespace to use for
pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are
distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are
only accessed by the kubelet. More info:
https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12604">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12610">property metadata</a>
</h3>

```typescript
metadata: ObjectMeta;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12616">property secrets</a>
</h3>

```typescript
secrets: ObjectReference[];
```


Secrets is the list of secrets allowed to be used by pods running using this
ServiceAccount. More info: https://kubernetes.io/docs/concepts/configuration/secret

<h2 class="pdoc-module-header" id="ServiceAccountList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12623">interface ServiceAccountList</a>
</h2>

ServiceAccountList is a list of ServiceAccount objects

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12630">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12636">property items</a>
</h3>

```typescript
items: ServiceAccount[];
```


List of ServiceAccounts. More info:
https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12644">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12650">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="ServiceAccountTokenProjection">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12659">interface ServiceAccountTokenProjection</a>
</h2>

ServiceAccountTokenProjection represents a projected service account token volume. This
projection can be used to insert a service account token into the pods runtime filesystem for
use against APIs (Kubernetes API Server or otherwise).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12665">property audience</a>
</h3>

```typescript
audience: string;
```


Audience is the intended audience of the token. A recipient of a token must identify itself
with an identifier specified in the audience of the token, and otherwise should reject the
token. The audience defaults to the identifier of the apiserver.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12674">property expirationSeconds</a>
</h3>

```typescript
expirationSeconds: number;
```


ExpirationSeconds is the requested duration of validity of the service account token. As
the token approaches expiration, the kubelet volume plugin will proactively rotate the
service account token. The kubelet will start trying to rotate the token if the token is
older than 80 percent of its time to live or if the token is older than 24 hours.Defaults
to 1 hour and must be at least 10 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12679">property path</a>
</h3>

```typescript
path: string;
```


Path is the path relative to the mount point of the file to project the token into.

<h2 class="pdoc-module-header" id="ServiceList">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12686">interface ServiceList</a>
</h2>

ServiceList holds a list of services.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12693">property apiVersion</a>
</h3>

```typescript
apiVersion: string;
```


APIVersion defines the versioned schema of this representation of an object. Servers should
convert recognized schemas to the latest internal value, and may reject unrecognized
values. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12698">property items</a>
</h3>

```typescript
items: Service[];
```


List of services

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12706">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is a string value representing the REST resource this object represents. Servers may
infer this from the endpoint the client submits requests to. Cannot be updated. In
CamelCase. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12712">property metadata</a>
</h3>

```typescript
metadata: ListMeta;
```


Standard list metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

<h2 class="pdoc-module-header" id="ServicePort">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12719">interface ServicePort</a>
</h2>

ServicePort contains information on service's port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12725">property name</a>
</h3>

```typescript
name: string;
```


The name of this port within the service. This must be a DNS_LABEL. All ports within a
ServiceSpec must have unique names. This maps to the 'Name' field in EndpointPort objects.
Optional if only one ServicePort is defined on this service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12734">property nodePort</a>
</h3>

```typescript
nodePort: number;
```


The port on each node on which this service is exposed when type=NodePort or LoadBalancer.
Usually assigned by the system. If specified, it will be allocated to the service if unused
or else creation of the service will fail. Default is to auto-allocate a port if the
ServiceType of this Service requires one. More info:
https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12739">property port</a>
</h3>

```typescript
port: number;
```


The port that will be exposed by this service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12744">property protocol</a>
</h3>

```typescript
protocol: string;
```


The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12754">property targetPort</a>
</h3>

```typescript
targetPort: number | string;
```


Number or name of the port to access on the pods targeted by the service. Number must be in
the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked
up as a named port in the target Pod's container ports. If this is not specified, the value
of the 'port' field is used (an identity map). This field is ignored for services with
clusterIP=None, and should be omitted or set equal to the 'port' field. More info:
https://kubernetes.io/docs/concepts/services-networking/service/#defining-a-service

<h2 class="pdoc-module-header" id="ServiceSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12761">interface ServiceSpec</a>
</h2>

ServiceSpec describes the attributes that a user creates on a service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12771">property clusterIP</a>
</h3>

```typescript
clusterIP: string;
```


clusterIP is the IP address of the service and is usually assigned randomly by the master.
If an address is specified manually and is not in use by others, it will be allocated to
the service; otherwise, creation of the service will fail. This field can not be changed
through updates. Valid values are "None", empty string (""), or a valid IP address. "None"
can be specified for headless services when proxying is not required. Only applies to types
ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info:
https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12779">property externalIPs</a>
</h3>

```typescript
externalIPs: string[];
```


externalIPs is a list of IP addresses for which nodes in the cluster will also accept
traffic for this service.  These IPs are not managed by Kubernetes.  The user is
responsible for ensuring that traffic arrives at a node with this IP.  A common example is
external load-balancers that are not part of the Kubernetes system.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12786">property externalName</a>
</h3>

```typescript
externalName: string;
```


externalName is the external reference that kubedns or equivalent will return as a CNAME
record for this service. No proxying will be involved. Must be a valid RFC-1123 hostname
(https://tools.ietf.org/html/rfc1123) and requires Type to be ExternalName.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12795">property externalTrafficPolicy</a>
</h3>

```typescript
externalTrafficPolicy: string;
```


externalTrafficPolicy denotes if this Service desires to route external traffic to
node-local or cluster-wide endpoints. "Local" preserves the client source IP and avoids a
second hop for LoadBalancer and Nodeport type services, but risks potentially imbalanced
traffic spreading. "Cluster" obscures the client source IP and may cause a second hop to
another node, but should have good overall load-spreading.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12803">property healthCheckNodePort</a>
</h3>

```typescript
healthCheckNodePort: number;
```


healthCheckNodePort specifies the healthcheck nodePort for the service. If not specified,
HealthCheckNodePort is created by the service api backend with the allocated nodePort. Will
use user-specified nodePort value if specified by the client. Only effects when Type is set
to LoadBalancer and ExternalTrafficPolicy is set to Local.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12811">property loadBalancerIP</a>
</h3>

```typescript
loadBalancerIP: string;
```


Only applies to Service Type: LoadBalancer LoadBalancer will get created with the IP
specified in this field. This feature depends on whether the underlying cloud-provider
supports specifying the loadBalancerIP when a load balancer is created. This field will be
ignored if the cloud-provider does not support the feature.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12819">property loadBalancerSourceRanges</a>
</h3>

```typescript
loadBalancerSourceRanges: string[];
```


If specified and supported by the platform, this will restrict traffic through the
cloud-provider load-balancer will be restricted to the specified client IPs. This field
will be ignored if the cloud-provider does not support the feature." More info:
https://kubernetes.io/docs/tasks/access-application-cluster/configure-cloud-provider-firewall/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12825">property ports</a>
</h3>

```typescript
ports: ServicePort[];
```


The list of ports that are exposed by this service. More info:
https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12834">property publishNotReadyAddresses</a>
</h3>

```typescript
publishNotReadyAddresses: boolean;
```


publishNotReadyAddresses, when set to true, indicates that DNS implementations must publish
the notReadyAddresses of subsets for the Endpoints associated with the Service. The default
value is false. The primary use case for setting this field is to use a StatefulSet's
Headless Service to propagate SRV records for its Pods without respect to their readiness
for purpose of peer discovery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12843">property selector</a>
</h3>

```typescript
selector: { ... };
```


Route service traffic to pods with label keys and values matching this selector. If empty
or not present, the service is assumed to have an external process managing its endpoints,
which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and
LoadBalancer. Ignored if type is ExternalName. More info:
https://kubernetes.io/docs/concepts/services-networking/service/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12850">property sessionAffinity</a>
</h3>

```typescript
sessionAffinity: string;
```


Supports "ClientIP" and "None". Used to maintain session affinity. Enable client IP based
session affinity. Must be ClientIP or None. Defaults to None. More info:
https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12855">property sessionAffinityConfig</a>
</h3>

```typescript
sessionAffinityConfig: SessionAffinityConfig;
```


sessionAffinityConfig contains the configurations of session affinity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12869">property type</a>
</h3>

```typescript
type: string;
```


type determines how the Service is exposed. Defaults to ClusterIP. Valid options are
ExternalName, ClusterIP, NodePort, and LoadBalancer. "ExternalName" maps to the specified
externalName. "ClusterIP" allocates a cluster-internal IP address for load-balancing to
endpoints. Endpoints are determined by the selector or if that is not specified, by manual
construction of an Endpoints object. If clusterIP is "None", no virtual IP is allocated and
the endpoints are published as a set of endpoints rather than a stable IP. "NodePort"
builds on ClusterIP and allocates a port on every node which routes to the clusterIP.
"LoadBalancer" builds on NodePort and creates an external load-balancer (if supported in
the current cloud) which routes to the clusterIP. More info:
https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services---service-types

<h2 class="pdoc-module-header" id="ServiceStatus">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12876">interface ServiceStatus</a>
</h2>

ServiceStatus represents the current status of a service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12880">property loadBalancer</a>
</h3>

```typescript
loadBalancer: LoadBalancerStatus;
```


LoadBalancer contains the current status of the load-balancer, if one is present.

<h2 class="pdoc-module-header" id="SessionAffinityConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12887">interface SessionAffinityConfig</a>
</h2>

SessionAffinityConfig represents the configurations of session affinity.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12891">property clientIP</a>
</h3>

```typescript
clientIP: ClientIPConfig;
```


clientIP contains the configurations of Client IP based session affinity.

<h2 class="pdoc-module-header" id="StorageOSPersistentVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12898">interface StorageOSPersistentVolumeSource</a>
</h2>

Represents a StorageOS persistent volume resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12903">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type to mount. Must be a filesystem type supported by the host operating system.
Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12909">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
VolumeMounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12915">property secretRef</a>
</h3>

```typescript
secretRef: ObjectReference;
```


SecretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not
specified, default values will be attempted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12921">property volumeName</a>
</h3>

```typescript
volumeName: string;
```


VolumeName is the human-readable name of the StorageOS volume.  Volume names are only
unique within a namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12930">property volumeNamespace</a>
</h3>

```typescript
volumeNamespace: string;
```


VolumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is
specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping
to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to
override the default behaviour. Set to "default" if you are not using namespaces within
StorageOS. Namespaces that do not pre-exist within StorageOS will be created.

<h2 class="pdoc-module-header" id="StorageOSVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12937">interface StorageOSVolumeSource</a>
</h2>

Represents a StorageOS persistent volume resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12942">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type to mount. Must be a filesystem type supported by the host operating system.
Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12948">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
VolumeMounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12954">property secretRef</a>
</h3>

```typescript
secretRef: LocalObjectReference;
```


SecretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not
specified, default values will be attempted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12960">property volumeName</a>
</h3>

```typescript
volumeName: string;
```


VolumeName is the human-readable name of the StorageOS volume.  Volume names are only
unique within a namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12969">property volumeNamespace</a>
</h3>

```typescript
volumeNamespace: string;
```


VolumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is
specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping
to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to
override the default behaviour. Set to "default" if you are not using namespaces within
StorageOS. Namespaces that do not pre-exist within StorageOS will be created.

<h2 class="pdoc-module-header" id="Sysctl">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12976">interface Sysctl</a>
</h2>

Sysctl defines a kernel parameter to be set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12980">property name</a>
</h3>

```typescript
name: string;
```


Name of a property to set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12985">property value</a>
</h3>

```typescript
value: string;
```


Value of a property to set

<h2 class="pdoc-module-header" id="TCPSocketAction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12992">interface TCPSocketAction</a>
</h2>

TCPSocketAction describes an action based on opening a socket

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L12996">property host</a>
</h3>

```typescript
host: string;
```


Optional: Host name to connect to, defaults to the pod IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13002">property port</a>
</h3>

```typescript
port: number | string;
```


Number or name of the port to access on the container. Number must be in the range 1 to
65535. Name must be an IANA_SVC_NAME.

<h2 class="pdoc-module-header" id="Taint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13010">interface Taint</a>
</h2>

The node this Taint is attached to has the "effect" on any pod that does not tolerate the
Taint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13015">property effect</a>
</h3>

```typescript
effect: string;
```


Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are
NoSchedule, PreferNoSchedule and NoExecute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13020">property key</a>
</h3>

```typescript
key: string;
```


Required. The taint key to be applied to a node.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13026">property timeAdded</a>
</h3>

```typescript
timeAdded: string;
```


TimeAdded represents the time at which the taint was added. It is only written for
NoExecute taints.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13031">property value</a>
</h3>

```typescript
value: string;
```


Required. The taint value corresponding to the taint key.

<h2 class="pdoc-module-header" id="Toleration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13039">interface Toleration</a>
</h2>

The pod this Toleration is attached to tolerates any taint that matches the triple
<key,value,effect> using the matching operator <operator>.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13044">property effect</a>
</h3>

```typescript
effect: string;
```


Effect indicates the taint effect to match. Empty means match all taint effects. When
specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13051">property key</a>
</h3>

```typescript
key: string;
```


Key is the taint key that the toleration applies to. Empty means match all taint keys. If
the key is empty, operator must be Exists; this combination means to match all values and
all keys.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13058">property operator</a>
</h3>

```typescript
operator: string;
```


Operator represents a key's relationship to the value. Valid operators are Exists and
Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can
tolerate all taints of a particular category.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13066">property tolerationSeconds</a>
</h3>

```typescript
tolerationSeconds: number;
```


TolerationSeconds represents the period of time the toleration (which must be of effect
NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set,
which means tolerate the taint forever (do not evict). Zero and negative values will be
treated as 0 (evict immediately) by the system.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13072">property value</a>
</h3>

```typescript
value: string;
```


Value is the taint value the toleration matches to. If the operator is Exists, the value
should be empty, otherwise just a regular string.

<h2 class="pdoc-module-header" id="TopologySelectorLabelRequirement">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13080">interface TopologySelectorLabelRequirement</a>
</h2>

A topology selector requirement is a selector that matches given label. This is an alpha
feature and may change in the future.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13084">property key</a>
</h3>

```typescript
key: string;
```


The label key that the selector applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13090">property values</a>
</h3>

```typescript
values: string[];
```


An array of string values. One value must match the label to be selected. Each entry in
Values is ORed.

<h2 class="pdoc-module-header" id="TopologySelectorTerm">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13099">interface TopologySelectorTerm</a>
</h2>

A topology selector term represents the result of label queries. A null or empty topology
selector term matches no objects. The requirements of them are ANDed. It provides a subset of
functionality as NodeSelectorTerm. This is an alpha feature and may change in the future.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13103">property matchLabelExpressions</a>
</h3>

```typescript
matchLabelExpressions: TopologySelectorLabelRequirement[];
```


A list of topology selector requirements by labels.

<h2 class="pdoc-module-header" id="TypedLocalObjectReference">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13111">interface TypedLocalObjectReference</a>
</h2>

TypedLocalObjectReference contains enough information to let you locate the typed referenced
object inside the same namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13117">property apiGroup</a>
</h3>

```typescript
apiGroup: string;
```


APIGroup is the group for the resource being referenced. If APIGroup is not specified, the
specified Kind must be in the core API group. For any other third-party types, APIGroup is
required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13122">property kind</a>
</h3>

```typescript
kind: string;
```


Kind is the type of resource being referenced

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13127">property name</a>
</h3>

```typescript
name: string;
```


Name is the name of resource being referenced

<h2 class="pdoc-module-header" id="Volume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13134">interface Volume</a>
</h2>

Volume represents a named volume in a pod that may be accessed by any container in the pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13140">property awsElasticBlockStore</a>
</h3>

```typescript
awsElasticBlockStore: AWSElasticBlockStoreVolumeSource;
```


AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host
machine and then exposed to the pod. More info:
https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13145">property azureDisk</a>
</h3>

```typescript
azureDisk: AzureDiskVolumeSource;
```


AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13150">property azureFile</a>
</h3>

```typescript
azureFile: AzureFileVolumeSource;
```


AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13155">property cephfs</a>
</h3>

```typescript
cephfs: CephFSVolumeSource;
```


CephFS represents a Ceph FS mount on the host that shares a pod's lifetime

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13161">property cinder</a>
</h3>

```typescript
cinder: CinderVolumeSource;
```


Cinder represents a cinder volume attached and mounted on kubelets host machine More info:
https://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13166">property configMap</a>
</h3>

```typescript
configMap: ConfigMapVolumeSource;
```


ConfigMap represents a configMap that should populate this volume

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13171">property downwardAPI</a>
</h3>

```typescript
downwardAPI: DownwardAPIVolumeSource;
```


DownwardAPI represents downward API about the pod that should populate this volume

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13177">property emptyDir</a>
</h3>

```typescript
emptyDir: EmptyDirVolumeSource;
```


EmptyDir represents a temporary directory that shares a pod's lifetime. More info:
https://kubernetes.io/docs/concepts/storage/volumes#emptydir

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13183">property fc</a>
</h3>

```typescript
fc: FCVolumeSource;
```


FC represents a Fibre Channel resource that is attached to a kubelet's host machine and
then exposed to the pod.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13189">property flexVolume</a>
</h3>

```typescript
flexVolume: FlexVolumeSource;
```


FlexVolume represents a generic volume resource that is provisioned/attached using an exec
based plugin.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13195">property flocker</a>
</h3>

```typescript
flocker: FlockerVolumeSource;
```


Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on
the Flocker control service being running

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13202">property gcePersistentDisk</a>
</h3>

```typescript
gcePersistentDisk: GCEPersistentDiskVolumeSource;
```


GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host
machine and then exposed to the pod. More info:
https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13210">property gitRepo</a>
</h3>

```typescript
gitRepo: GitRepoVolumeSource;
```


GitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is
deprecated. To provision a container with a git repo, mount an EmptyDir into an
InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's
container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13216">property glusterfs</a>
</h3>

```typescript
glusterfs: GlusterfsVolumeSource;
```


Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info:
https://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13224">property hostPath</a>
</h3>

```typescript
hostPath: HostPathVolumeSource;
```


HostPath represents a pre-existing file or directory on the host machine that is directly
exposed to the container. This is generally used for system agents or other privileged
things that are allowed to see the host machine. Most containers will NOT need this. More
info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13231">property iscsi</a>
</h3>

```typescript
iscsi: ISCSIVolumeSource;
```


ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and
then exposed to the pod. More info:
https://releases.k8s.io/HEAD/examples/volumes/iscsi/README.md

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13237">property name</a>
</h3>

```typescript
name: string;
```


Volume's name. Must be a DNS_LABEL and unique within the pod. More info:
https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13243">property nfs</a>
</h3>

```typescript
nfs: NFSVolumeSource;
```


NFS represents an NFS mount on the host that shares a pod's lifetime More info:
https://kubernetes.io/docs/concepts/storage/volumes#nfs

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13250">property persistentVolumeClaim</a>
</h3>

```typescript
persistentVolumeClaim: PersistentVolumeClaimVolumeSource;
```


PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the
same namespace. More info:
https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13256">property photonPersistentDisk</a>
</h3>

```typescript
photonPersistentDisk: PhotonPersistentDiskVolumeSource;
```


PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on
kubelets host machine

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13261">property portworxVolume</a>
</h3>

```typescript
portworxVolume: PortworxVolumeSource;
```


PortworxVolume represents a portworx volume attached and mounted on kubelets host machine

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13266">property projected</a>
</h3>

```typescript
projected: ProjectedVolumeSource;
```


Items for all in one resources secrets, configmaps, and downward API

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13271">property quobyte</a>
</h3>

```typescript
quobyte: QuobyteVolumeSource;
```


Quobyte represents a Quobyte mount on the host that shares a pod's lifetime

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13277">property rbd</a>
</h3>

```typescript
rbd: RBDVolumeSource;
```


RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More
info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13282">property scaleIO</a>
</h3>

```typescript
scaleIO: ScaleIOVolumeSource;
```


ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13288">property secret</a>
</h3>

```typescript
secret: SecretVolumeSource;
```


Secret represents a secret that should populate this volume. More info:
https://kubernetes.io/docs/concepts/storage/volumes#secret

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13293">property storageos</a>
</h3>

```typescript
storageos: StorageOSVolumeSource;
```


StorageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13298">property vsphereVolume</a>
</h3>

```typescript
vsphereVolume: VsphereVirtualDiskVolumeSource;
```


VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine

<h2 class="pdoc-module-header" id="VolumeDevice">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13305">interface VolumeDevice</a>
</h2>

volumeDevice describes a mapping of a raw block device within a container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13309">property devicePath</a>
</h3>

```typescript
devicePath: string;
```


devicePath is the path inside of the container that the device will be mapped to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13314">property name</a>
</h3>

```typescript
name: string;
```


name must match the name of a persistentVolumeClaim in the pod

<h2 class="pdoc-module-header" id="VolumeMount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13321">interface VolumeMount</a>
</h2>

VolumeMount describes a mounting of a Volume within a container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13325">property mountPath</a>
</h3>

```typescript
mountPath: string;
```


Path within the container at which the volume should be mounted.  Must not contain ':'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13331">property mountPropagation</a>
</h3>

```typescript
mountPropagation: string;
```


mountPropagation determines how mounts are propagated from the host to container and the
other way around. When not set, MountPropagationNone is used. This field is beta in 1.10.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13336">property name</a>
</h3>

```typescript
name: string;
```


This must match the Name of a Volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13341">property readOnly</a>
</h3>

```typescript
readOnly: boolean;
```


Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13347">property subPath</a>
</h3>

```typescript
subPath: string;
```


Path within the volume from which the container's volume should be mounted. Defaults to ""
(volume's root).

<h2 class="pdoc-module-header" id="VolumeNodeAffinity">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13355">interface VolumeNodeAffinity</a>
</h2>

VolumeNodeAffinity defines constraints that limit what nodes this volume can be accessed
from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13359">property required</a>
</h3>

```typescript
required: NodeSelector;
```


Required specifies hard node constraints that must be met.

<h2 class="pdoc-module-header" id="VolumeProjection">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13366">interface VolumeProjection</a>
</h2>

Projection that may be projected along with other supported volume types

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13370">property configMap</a>
</h3>

```typescript
configMap: ConfigMapProjection;
```


information about the configMap data to project

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13375">property downwardAPI</a>
</h3>

```typescript
downwardAPI: DownwardAPIProjection;
```


information about the downwardAPI data to project

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13380">property secret</a>
</h3>

```typescript
secret: SecretProjection;
```


information about the secret data to project

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13385">property serviceAccountToken</a>
</h3>

```typescript
serviceAccountToken: ServiceAccountTokenProjection;
```


information about the serviceAccountToken data to project

<h2 class="pdoc-module-header" id="VsphereVirtualDiskVolumeSource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13392">interface VsphereVirtualDiskVolumeSource</a>
</h2>

Represents a vSphere volume resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13397">property fsType</a>
</h3>

```typescript
fsType: string;
```


Filesystem type to mount. Must be a filesystem type supported by the host operating system.
Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13402">property storagePolicyID</a>
</h3>

```typescript
storagePolicyID: string;
```


Storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13407">property storagePolicyName</a>
</h3>

```typescript
storagePolicyName: string;
```


Storage Policy Based Management (SPBM) profile name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13412">property volumePath</a>
</h3>

```typescript
volumePath: string;
```


Path that identifies vSphere volume vmdk

<h2 class="pdoc-module-header" id="WeightedPodAffinityTerm">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13420">interface WeightedPodAffinityTerm</a>
</h2>

The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find
the most preferred node(s)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13424">property podAffinityTerm</a>
</h3>

```typescript
podAffinityTerm: PodAffinityTerm;
```


Required. A pod affinity term, associated with the corresponding weight.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/types/output.ts#L13429">property weight</a>
</h3>

```typescript
weight: number;
```


weight associated with matching the corresponding podAffinityTerm, in the range 1-100.

