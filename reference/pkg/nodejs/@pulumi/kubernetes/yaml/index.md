---
title: Module yaml
---

<a href="../index.html">@pulumi/kubernetes</a> &gt; yaml

<h2 class="pdoc-module-header">Index</h2>

* <a href="#CollectionComponentResource">class CollectionComponentResource</a>
* <a href="#ConfigFile">class ConfigFile</a>
* <a href="#ConfigGroup">class ConfigGroup</a>
* <a href="#parse">function parse</a>
* <a href="#parseYamlDocument">function parseYamlDocument</a>
* <a href="#parseYamlObject">function parseYamlObject</a>
* <a href="#ConfigFileOpts">interface ConfigFileOpts</a>
* <a href="#ConfigGroupOpts">interface ConfigGroupOpts</a>
* <a href="#ConfigOpts">interface ConfigOpts</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts">provider.ts</a> 


<h2 class="pdoc-module-header" id="CollectionComponentResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L80">class CollectionComponentResource</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L81">constructor</a>
</h3>

```typescript
new CollectionComponentResource(resourceType: string, name: string, config: any, opts?: pulumi.ComponentResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L89">method getResource</a>
</h3>

```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1alpha1/InitializerConfiguration, name: string): InitializerConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1alpha1/InitializerConfiguration, namespace: string, name: string): InitializerConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1alpha1/InitializerConfigurationList, name: string): InitializerConfigurationList
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1alpha1/InitializerConfigurationList, namespace: string, name: string): InitializerConfigurationList
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/MutatingWebhookConfiguration, name: string): MutatingWebhookConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/MutatingWebhookConfiguration, namespace: string, name: string): MutatingWebhookConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/MutatingWebhookConfigurationList, name: string): MutatingWebhookConfigurationList
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/MutatingWebhookConfigurationList, namespace: string, name: string): MutatingWebhookConfigurationList
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/ValidatingWebhookConfiguration, name: string): ValidatingWebhookConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/ValidatingWebhookConfiguration, namespace: string, name: string): ValidatingWebhookConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/ValidatingWebhookConfigurationList, name: string): ValidatingWebhookConfigurationList
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/ValidatingWebhookConfigurationList, namespace: string, name: string): ValidatingWebhookConfigurationList
```


```typescript
public getResource(groupVersionKind: apiextensions.k8s.io/v1beta1/CustomResourceDefinition, name: string): CustomResourceDefinition
```


```typescript
public getResource(groupVersionKind: apiextensions.k8s.io/v1beta1/CustomResourceDefinition, namespace: string, name: string): CustomResourceDefinition
```


```typescript
public getResource(groupVersionKind: apiextensions.k8s.io/v1beta1/CustomResourceDefinitionList, name: string): CustomResourceDefinitionList
```


```typescript
public getResource(groupVersionKind: apiextensions.k8s.io/v1beta1/CustomResourceDefinitionList, namespace: string, name: string): CustomResourceDefinitionList
```


```typescript
public getResource(groupVersionKind: apiregistration/v1beta1/APIService, name: string): APIService
```


```typescript
public getResource(groupVersionKind: apiregistration/v1beta1/APIService, namespace: string, name: string): APIService
```


```typescript
public getResource(groupVersionKind: apiregistration/v1beta1/APIServiceList, name: string): APIServiceList
```


```typescript
public getResource(groupVersionKind: apiregistration/v1beta1/APIServiceList, namespace: string, name: string): APIServiceList
```


```typescript
public getResource(groupVersionKind: apps/v1/ControllerRevision, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1/ControllerRevision, namespace: string, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1/ControllerRevisionList, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1/ControllerRevisionList, namespace: string, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1/DaemonSet, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: apps/v1/DaemonSet, namespace: string, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: apps/v1/DaemonSetList, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: apps/v1/DaemonSetList, namespace: string, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: apps/v1/Deployment, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1/Deployment, namespace: string, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1/DeploymentList, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1/DeploymentList, namespace: string, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1/ReplicaSet, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: apps/v1/ReplicaSet, namespace: string, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: apps/v1/ReplicaSetList, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: apps/v1/ReplicaSetList, namespace: string, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: apps/v1/StatefulSet, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1/StatefulSet, namespace: string, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1/StatefulSetList, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: apps/v1/StatefulSetList, namespace: string, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/ControllerRevision, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/ControllerRevision, namespace: string, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/ControllerRevisionList, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/ControllerRevisionList, namespace: string, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/Deployment, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/Deployment, namespace: string, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/DeploymentList, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/DeploymentList, namespace: string, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/DeploymentRollback, name: string): DeploymentRollback
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/DeploymentRollback, namespace: string, name: string): DeploymentRollback
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/Scale, name: string): Scale
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/Scale, namespace: string, name: string): Scale
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/StatefulSet, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/StatefulSet, namespace: string, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/StatefulSetList, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/StatefulSetList, namespace: string, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ControllerRevision, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ControllerRevision, namespace: string, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ControllerRevisionList, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ControllerRevisionList, namespace: string, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DaemonSet, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DaemonSet, namespace: string, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DaemonSetList, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DaemonSetList, namespace: string, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/Deployment, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/Deployment, namespace: string, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DeploymentList, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DeploymentList, namespace: string, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ReplicaSet, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ReplicaSet, namespace: string, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ReplicaSetList, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ReplicaSetList, namespace: string, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/Scale, name: string): Scale
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/Scale, namespace: string, name: string): Scale
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/StatefulSet, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/StatefulSet, namespace: string, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/StatefulSetList, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/StatefulSetList, namespace: string, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: authentication.k8s.io/v1/TokenReview, name: string): TokenReview
```


```typescript
public getResource(groupVersionKind: authentication.k8s.io/v1/TokenReview, namespace: string, name: string): TokenReview
```


```typescript
public getResource(groupVersionKind: authentication.k8s.io/v1beta1/TokenReview, name: string): TokenReview
```


```typescript
public getResource(groupVersionKind: authentication.k8s.io/v1beta1/TokenReview, namespace: string, name: string): TokenReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/LocalSubjectAccessReview, name: string): LocalSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/LocalSubjectAccessReview, namespace: string, name: string): LocalSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SelfSubjectAccessReview, name: string): SelfSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SelfSubjectAccessReview, namespace: string, name: string): SelfSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SelfSubjectRulesReview, name: string): SelfSubjectRulesReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SelfSubjectRulesReview, namespace: string, name: string): SelfSubjectRulesReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SubjectAccessReview, name: string): SubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SubjectAccessReview, namespace: string, name: string): SubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/LocalSubjectAccessReview, name: string): LocalSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/LocalSubjectAccessReview, namespace: string, name: string): LocalSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SelfSubjectAccessReview, name: string): SelfSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SelfSubjectAccessReview, namespace: string, name: string): SelfSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SelfSubjectRulesReview, name: string): SelfSubjectRulesReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SelfSubjectRulesReview, namespace: string, name: string): SelfSubjectRulesReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SubjectAccessReview, name: string): SubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SubjectAccessReview, namespace: string, name: string): SubjectAccessReview
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/CrossVersionObjectReference, name: string): CrossVersionObjectReference
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/CrossVersionObjectReference, namespace: string, name: string): CrossVersionObjectReference
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/HorizontalPodAutoscaler, name: string): HorizontalPodAutoscaler
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/HorizontalPodAutoscaler, namespace: string, name: string): HorizontalPodAutoscaler
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/HorizontalPodAutoscalerList, name: string): HorizontalPodAutoscalerList
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/HorizontalPodAutoscalerList, namespace: string, name: string): HorizontalPodAutoscalerList
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/Scale, name: string): Scale
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/Scale, namespace: string, name: string): Scale
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/CrossVersionObjectReference, name: string): CrossVersionObjectReference
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/CrossVersionObjectReference, namespace: string, name: string): CrossVersionObjectReference
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/HorizontalPodAutoscaler, name: string): HorizontalPodAutoscaler
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/HorizontalPodAutoscaler, namespace: string, name: string): HorizontalPodAutoscaler
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/HorizontalPodAutoscalerList, name: string): HorizontalPodAutoscalerList
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/HorizontalPodAutoscalerList, namespace: string, name: string): HorizontalPodAutoscalerList
```


```typescript
public getResource(groupVersionKind: batch/v1/Job, name: string): Job
```


```typescript
public getResource(groupVersionKind: batch/v1/Job, namespace: string, name: string): Job
```


```typescript
public getResource(groupVersionKind: batch/v1/JobList, name: string): JobList
```


```typescript
public getResource(groupVersionKind: batch/v1/JobList, namespace: string, name: string): JobList
```


```typescript
public getResource(groupVersionKind: batch/v1beta1/CronJob, name: string): CronJob
```


```typescript
public getResource(groupVersionKind: batch/v1beta1/CronJob, namespace: string, name: string): CronJob
```


```typescript
public getResource(groupVersionKind: batch/v1beta1/CronJobList, name: string): CronJobList
```


```typescript
public getResource(groupVersionKind: batch/v1beta1/CronJobList, namespace: string, name: string): CronJobList
```


```typescript
public getResource(groupVersionKind: batch/v2alpha1/CronJob, name: string): CronJob
```


```typescript
public getResource(groupVersionKind: batch/v2alpha1/CronJob, namespace: string, name: string): CronJob
```


```typescript
public getResource(groupVersionKind: batch/v2alpha1/CronJobList, name: string): CronJobList
```


```typescript
public getResource(groupVersionKind: batch/v2alpha1/CronJobList, namespace: string, name: string): CronJobList
```


```typescript
public getResource(groupVersionKind: certificates.k8s.io/v1beta1/CertificateSigningRequest, name: string): CertificateSigningRequest
```


```typescript
public getResource(groupVersionKind: certificates.k8s.io/v1beta1/CertificateSigningRequest, namespace: string, name: string): CertificateSigningRequest
```


```typescript
public getResource(groupVersionKind: certificates.k8s.io/v1beta1/CertificateSigningRequestList, name: string): CertificateSigningRequestList
```


```typescript
public getResource(groupVersionKind: certificates.k8s.io/v1beta1/CertificateSigningRequestList, namespace: string, name: string): CertificateSigningRequestList
```


```typescript
public getResource(groupVersionKind: v1/Binding, name: string): Binding
```


```typescript
public getResource(groupVersionKind: v1/Binding, namespace: string, name: string): Binding
```


```typescript
public getResource(groupVersionKind: v1/ComponentStatus, name: string): ComponentStatus
```


```typescript
public getResource(groupVersionKind: v1/ComponentStatus, namespace: string, name: string): ComponentStatus
```


```typescript
public getResource(groupVersionKind: v1/ComponentStatusList, name: string): ComponentStatusList
```


```typescript
public getResource(groupVersionKind: v1/ComponentStatusList, namespace: string, name: string): ComponentStatusList
```


```typescript
public getResource(groupVersionKind: v1/ConfigMap, name: string): ConfigMap
```


```typescript
public getResource(groupVersionKind: v1/ConfigMap, namespace: string, name: string): ConfigMap
```


```typescript
public getResource(groupVersionKind: v1/ConfigMapList, name: string): ConfigMapList
```


```typescript
public getResource(groupVersionKind: v1/ConfigMapList, namespace: string, name: string): ConfigMapList
```


```typescript
public getResource(groupVersionKind: v1/Endpoints, name: string): Endpoints
```


```typescript
public getResource(groupVersionKind: v1/Endpoints, namespace: string, name: string): Endpoints
```


```typescript
public getResource(groupVersionKind: v1/EndpointsList, name: string): EndpointsList
```


```typescript
public getResource(groupVersionKind: v1/EndpointsList, namespace: string, name: string): EndpointsList
```


```typescript
public getResource(groupVersionKind: v1/Event, name: string): Event
```


```typescript
public getResource(groupVersionKind: v1/Event, namespace: string, name: string): Event
```


```typescript
public getResource(groupVersionKind: v1/EventList, name: string): EventList
```


```typescript
public getResource(groupVersionKind: v1/EventList, namespace: string, name: string): EventList
```


```typescript
public getResource(groupVersionKind: v1/LimitRange, name: string): LimitRange
```


```typescript
public getResource(groupVersionKind: v1/LimitRange, namespace: string, name: string): LimitRange
```


```typescript
public getResource(groupVersionKind: v1/LimitRangeList, name: string): LimitRangeList
```


```typescript
public getResource(groupVersionKind: v1/LimitRangeList, namespace: string, name: string): LimitRangeList
```


```typescript
public getResource(groupVersionKind: v1/Namespace, name: string): Namespace
```


```typescript
public getResource(groupVersionKind: v1/Namespace, namespace: string, name: string): Namespace
```


```typescript
public getResource(groupVersionKind: v1/NamespaceList, name: string): NamespaceList
```


```typescript
public getResource(groupVersionKind: v1/NamespaceList, namespace: string, name: string): NamespaceList
```


```typescript
public getResource(groupVersionKind: v1/Node, name: string): Node
```


```typescript
public getResource(groupVersionKind: v1/Node, namespace: string, name: string): Node
```


```typescript
public getResource(groupVersionKind: v1/NodeConfigSource, name: string): NodeConfigSource
```


```typescript
public getResource(groupVersionKind: v1/NodeConfigSource, namespace: string, name: string): NodeConfigSource
```


```typescript
public getResource(groupVersionKind: v1/NodeList, name: string): NodeList
```


```typescript
public getResource(groupVersionKind: v1/NodeList, namespace: string, name: string): NodeList
```


```typescript
public getResource(groupVersionKind: core/v1/ObjectReference, name: string): ObjectReference
```


```typescript
public getResource(groupVersionKind: core/v1/ObjectReference, namespace: string, name: string): ObjectReference
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolume, name: string): PersistentVolume
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolume, namespace: string, name: string): PersistentVolume
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeClaim, name: string): PersistentVolumeClaim
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeClaim, namespace: string, name: string): PersistentVolumeClaim
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeClaimList, name: string): PersistentVolumeClaimList
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeClaimList, namespace: string, name: string): PersistentVolumeClaimList
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeList, name: string): PersistentVolumeList
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeList, namespace: string, name: string): PersistentVolumeList
```


```typescript
public getResource(groupVersionKind: v1/Pod, name: string): Pod
```


```typescript
public getResource(groupVersionKind: v1/Pod, namespace: string, name: string): Pod
```


```typescript
public getResource(groupVersionKind: v1/PodList, name: string): PodList
```


```typescript
public getResource(groupVersionKind: v1/PodList, namespace: string, name: string): PodList
```


```typescript
public getResource(groupVersionKind: v1/PodTemplate, name: string): PodTemplate
```


```typescript
public getResource(groupVersionKind: v1/PodTemplate, namespace: string, name: string): PodTemplate
```


```typescript
public getResource(groupVersionKind: v1/PodTemplateList, name: string): PodTemplateList
```


```typescript
public getResource(groupVersionKind: v1/PodTemplateList, namespace: string, name: string): PodTemplateList
```


```typescript
public getResource(groupVersionKind: v1/ReplicationController, name: string): ReplicationController
```


```typescript
public getResource(groupVersionKind: v1/ReplicationController, namespace: string, name: string): ReplicationController
```


```typescript
public getResource(groupVersionKind: v1/ReplicationControllerList, name: string): ReplicationControllerList
```


```typescript
public getResource(groupVersionKind: v1/ReplicationControllerList, namespace: string, name: string): ReplicationControllerList
```


```typescript
public getResource(groupVersionKind: v1/ResourceQuota, name: string): ResourceQuota
```


```typescript
public getResource(groupVersionKind: v1/ResourceQuota, namespace: string, name: string): ResourceQuota
```


```typescript
public getResource(groupVersionKind: v1/ResourceQuotaList, name: string): ResourceQuotaList
```


```typescript
public getResource(groupVersionKind: v1/ResourceQuotaList, namespace: string, name: string): ResourceQuotaList
```


```typescript
public getResource(groupVersionKind: v1/Secret, name: string): Secret
```


```typescript
public getResource(groupVersionKind: v1/Secret, namespace: string, name: string): Secret
```


```typescript
public getResource(groupVersionKind: v1/SecretList, name: string): SecretList
```


```typescript
public getResource(groupVersionKind: v1/SecretList, namespace: string, name: string): SecretList
```


```typescript
public getResource(groupVersionKind: v1/Service, name: string): Service
```


```typescript
public getResource(groupVersionKind: v1/Service, namespace: string, name: string): Service
```


```typescript
public getResource(groupVersionKind: v1/ServiceAccount, name: string): ServiceAccount
```


```typescript
public getResource(groupVersionKind: v1/ServiceAccount, namespace: string, name: string): ServiceAccount
```


```typescript
public getResource(groupVersionKind: v1/ServiceAccountList, name: string): ServiceAccountList
```


```typescript
public getResource(groupVersionKind: v1/ServiceAccountList, namespace: string, name: string): ServiceAccountList
```


```typescript
public getResource(groupVersionKind: v1/ServiceList, name: string): ServiceList
```


```typescript
public getResource(groupVersionKind: v1/ServiceList, namespace: string, name: string): ServiceList
```


```typescript
public getResource(groupVersionKind: events.k8s.io/v1beta1/Event, name: string): Event
```


```typescript
public getResource(groupVersionKind: events.k8s.io/v1beta1/Event, namespace: string, name: string): Event
```


```typescript
public getResource(groupVersionKind: events.k8s.io/v1beta1/EventList, name: string): EventList
```


```typescript
public getResource(groupVersionKind: events.k8s.io/v1beta1/EventList, namespace: string, name: string): EventList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DaemonSet, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DaemonSet, namespace: string, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DaemonSetList, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DaemonSetList, namespace: string, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Deployment, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Deployment, namespace: string, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DeploymentList, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DeploymentList, namespace: string, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DeploymentRollback, name: string): DeploymentRollback
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DeploymentRollback, namespace: string, name: string): DeploymentRollback
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Ingress, name: string): Ingress
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Ingress, namespace: string, name: string): Ingress
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/IngressList, name: string): IngressList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/IngressList, namespace: string, name: string): IngressList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/NetworkPolicy, name: string): NetworkPolicy
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/NetworkPolicy, namespace: string, name: string): NetworkPolicy
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/NetworkPolicyList, name: string): NetworkPolicyList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/NetworkPolicyList, namespace: string, name: string): NetworkPolicyList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/PodSecurityPolicy, name: string): PodSecurityPolicy
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/PodSecurityPolicy, namespace: string, name: string): PodSecurityPolicy
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/PodSecurityPolicyList, name: string): PodSecurityPolicyList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/PodSecurityPolicyList, namespace: string, name: string): PodSecurityPolicyList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/ReplicaSet, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/ReplicaSet, namespace: string, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/ReplicaSetList, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/ReplicaSetList, namespace: string, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Scale, name: string): Scale
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Scale, namespace: string, name: string): Scale
```


```typescript
public getResource(groupVersionKind: v1/APIGroup, name: string): APIGroup
```


```typescript
public getResource(groupVersionKind: v1/APIGroup, namespace: string, name: string): APIGroup
```


```typescript
public getResource(groupVersionKind: v1/APIGroupList, name: string): APIGroupList
```


```typescript
public getResource(groupVersionKind: v1/APIGroupList, namespace: string, name: string): APIGroupList
```


```typescript
public getResource(groupVersionKind: v1/APIResourceList, name: string): APIResourceList
```


```typescript
public getResource(groupVersionKind: v1/APIResourceList, namespace: string, name: string): APIResourceList
```


```typescript
public getResource(groupVersionKind: v1/APIVersions, name: string): APIVersions
```


```typescript
public getResource(groupVersionKind: v1/APIVersions, namespace: string, name: string): APIVersions
```


```typescript
public getResource(groupVersionKind: v1/DeleteOptions, name: string): DeleteOptions
```


```typescript
public getResource(groupVersionKind: v1/DeleteOptions, namespace: string, name: string): DeleteOptions
```


```typescript
public getResource(groupVersionKind: meta/v1/OwnerReference, name: string): OwnerReference
```


```typescript
public getResource(groupVersionKind: meta/v1/OwnerReference, namespace: string, name: string): OwnerReference
```


```typescript
public getResource(groupVersionKind: v1/Status, name: string): Status
```


```typescript
public getResource(groupVersionKind: v1/Status, namespace: string, name: string): Status
```


```typescript
public getResource(groupVersionKind: networking.k8s.io/v1/NetworkPolicy, name: string): NetworkPolicy
```


```typescript
public getResource(groupVersionKind: networking.k8s.io/v1/NetworkPolicy, namespace: string, name: string): NetworkPolicy
```


```typescript
public getResource(groupVersionKind: networking.k8s.io/v1/NetworkPolicyList, name: string): NetworkPolicyList
```


```typescript
public getResource(groupVersionKind: networking.k8s.io/v1/NetworkPolicyList, namespace: string, name: string): NetworkPolicyList
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/Eviction, name: string): Eviction
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/Eviction, namespace: string, name: string): Eviction
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/PodDisruptionBudget, name: string): PodDisruptionBudget
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/PodDisruptionBudget, namespace: string, name: string): PodDisruptionBudget
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/PodDisruptionBudgetList, name: string): PodDisruptionBudgetList
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/PodDisruptionBudgetList, namespace: string, name: string): PodDisruptionBudgetList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRole, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRole, namespace: string, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleBinding, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleBinding, namespace: string, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleBindingList, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleBindingList, namespace: string, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleList, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleList, namespace: string, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/Role, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/Role, namespace: string, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleBinding, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleBinding, namespace: string, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleBindingList, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleBindingList, namespace: string, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleList, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleList, namespace: string, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRole, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRole, namespace: string, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleBinding, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleBinding, namespace: string, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleBindingList, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleBindingList, namespace: string, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleList, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleList, namespace: string, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/Role, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/Role, namespace: string, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleBinding, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleBinding, namespace: string, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleBindingList, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleBindingList, namespace: string, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleList, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleList, namespace: string, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: rbac/v1alpha1/Subject, name: string): Subject
```


```typescript
public getResource(groupVersionKind: rbac/v1alpha1/Subject, namespace: string, name: string): Subject
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRole, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRole, namespace: string, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleBinding, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleBinding, namespace: string, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleBindingList, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleBindingList, namespace: string, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleList, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleList, namespace: string, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/Role, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/Role, namespace: string, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleBinding, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleBinding, namespace: string, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleBindingList, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleBindingList, namespace: string, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleList, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleList, namespace: string, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: scheduling.k8s.io/v1alpha1/PriorityClass, name: string): PriorityClass
```


```typescript
public getResource(groupVersionKind: scheduling.k8s.io/v1alpha1/PriorityClass, namespace: string, name: string): PriorityClass
```


```typescript
public getResource(groupVersionKind: scheduling.k8s.io/v1alpha1/PriorityClassList, name: string): PriorityClassList
```


```typescript
public getResource(groupVersionKind: scheduling.k8s.io/v1alpha1/PriorityClassList, namespace: string, name: string): PriorityClassList
```


```typescript
public getResource(groupVersionKind: settings.k8s.io/v1alpha1/PodPreset, name: string): PodPreset
```


```typescript
public getResource(groupVersionKind: settings.k8s.io/v1alpha1/PodPreset, namespace: string, name: string): PodPreset
```


```typescript
public getResource(groupVersionKind: settings.k8s.io/v1alpha1/PodPresetList, name: string): PodPresetList
```


```typescript
public getResource(groupVersionKind: settings.k8s.io/v1alpha1/PodPresetList, namespace: string, name: string): PodPresetList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1/StorageClass, name: string): StorageClass
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1/StorageClass, namespace: string, name: string): StorageClass
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1/StorageClassList, name: string): StorageClassList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1/StorageClassList, namespace: string, name: string): StorageClassList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1alpha1/VolumeAttachment, name: string): VolumeAttachment
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1alpha1/VolumeAttachment, namespace: string, name: string): VolumeAttachment
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1alpha1/VolumeAttachmentList, name: string): VolumeAttachmentList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1alpha1/VolumeAttachmentList, namespace: string, name: string): VolumeAttachmentList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1beta1/StorageClass, name: string): StorageClass
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1beta1/StorageClass, namespace: string, name: string): StorageClass
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1beta1/StorageClassList, name: string): StorageClassList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1beta1/StorageClassList, namespace: string, name: string): StorageClassList
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L81">property resources</a>
</h3>

```typescript
resources: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ConfigFile">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L453">class ConfigFile</a>
</h2>

ConfigFile creates a set of Kubernetes resources from Kubernetes YAML file. If `config.name`
is not specified, `ConfigFile` assumes the argument `name` is the filename.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L453">constructor</a>
</h3>

```typescript
new ConfigFile(name: string, config?: ConfigFileOpts, opts?: pulumi.ComponentResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L89">method getResource</a>
</h3>

```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1alpha1/InitializerConfiguration, name: string): InitializerConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1alpha1/InitializerConfiguration, namespace: string, name: string): InitializerConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1alpha1/InitializerConfigurationList, name: string): InitializerConfigurationList
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1alpha1/InitializerConfigurationList, namespace: string, name: string): InitializerConfigurationList
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/MutatingWebhookConfiguration, name: string): MutatingWebhookConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/MutatingWebhookConfiguration, namespace: string, name: string): MutatingWebhookConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/MutatingWebhookConfigurationList, name: string): MutatingWebhookConfigurationList
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/MutatingWebhookConfigurationList, namespace: string, name: string): MutatingWebhookConfigurationList
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/ValidatingWebhookConfiguration, name: string): ValidatingWebhookConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/ValidatingWebhookConfiguration, namespace: string, name: string): ValidatingWebhookConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/ValidatingWebhookConfigurationList, name: string): ValidatingWebhookConfigurationList
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/ValidatingWebhookConfigurationList, namespace: string, name: string): ValidatingWebhookConfigurationList
```


```typescript
public getResource(groupVersionKind: apiextensions.k8s.io/v1beta1/CustomResourceDefinition, name: string): CustomResourceDefinition
```


```typescript
public getResource(groupVersionKind: apiextensions.k8s.io/v1beta1/CustomResourceDefinition, namespace: string, name: string): CustomResourceDefinition
```


```typescript
public getResource(groupVersionKind: apiextensions.k8s.io/v1beta1/CustomResourceDefinitionList, name: string): CustomResourceDefinitionList
```


```typescript
public getResource(groupVersionKind: apiextensions.k8s.io/v1beta1/CustomResourceDefinitionList, namespace: string, name: string): CustomResourceDefinitionList
```


```typescript
public getResource(groupVersionKind: apiregistration/v1beta1/APIService, name: string): APIService
```


```typescript
public getResource(groupVersionKind: apiregistration/v1beta1/APIService, namespace: string, name: string): APIService
```


```typescript
public getResource(groupVersionKind: apiregistration/v1beta1/APIServiceList, name: string): APIServiceList
```


```typescript
public getResource(groupVersionKind: apiregistration/v1beta1/APIServiceList, namespace: string, name: string): APIServiceList
```


```typescript
public getResource(groupVersionKind: apps/v1/ControllerRevision, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1/ControllerRevision, namespace: string, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1/ControllerRevisionList, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1/ControllerRevisionList, namespace: string, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1/DaemonSet, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: apps/v1/DaemonSet, namespace: string, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: apps/v1/DaemonSetList, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: apps/v1/DaemonSetList, namespace: string, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: apps/v1/Deployment, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1/Deployment, namespace: string, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1/DeploymentList, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1/DeploymentList, namespace: string, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1/ReplicaSet, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: apps/v1/ReplicaSet, namespace: string, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: apps/v1/ReplicaSetList, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: apps/v1/ReplicaSetList, namespace: string, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: apps/v1/StatefulSet, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1/StatefulSet, namespace: string, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1/StatefulSetList, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: apps/v1/StatefulSetList, namespace: string, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/ControllerRevision, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/ControllerRevision, namespace: string, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/ControllerRevisionList, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/ControllerRevisionList, namespace: string, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/Deployment, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/Deployment, namespace: string, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/DeploymentList, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/DeploymentList, namespace: string, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/DeploymentRollback, name: string): DeploymentRollback
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/DeploymentRollback, namespace: string, name: string): DeploymentRollback
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/Scale, name: string): Scale
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/Scale, namespace: string, name: string): Scale
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/StatefulSet, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/StatefulSet, namespace: string, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/StatefulSetList, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/StatefulSetList, namespace: string, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ControllerRevision, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ControllerRevision, namespace: string, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ControllerRevisionList, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ControllerRevisionList, namespace: string, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DaemonSet, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DaemonSet, namespace: string, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DaemonSetList, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DaemonSetList, namespace: string, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/Deployment, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/Deployment, namespace: string, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DeploymentList, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DeploymentList, namespace: string, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ReplicaSet, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ReplicaSet, namespace: string, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ReplicaSetList, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ReplicaSetList, namespace: string, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/Scale, name: string): Scale
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/Scale, namespace: string, name: string): Scale
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/StatefulSet, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/StatefulSet, namespace: string, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/StatefulSetList, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/StatefulSetList, namespace: string, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: authentication.k8s.io/v1/TokenReview, name: string): TokenReview
```


```typescript
public getResource(groupVersionKind: authentication.k8s.io/v1/TokenReview, namespace: string, name: string): TokenReview
```


```typescript
public getResource(groupVersionKind: authentication.k8s.io/v1beta1/TokenReview, name: string): TokenReview
```


```typescript
public getResource(groupVersionKind: authentication.k8s.io/v1beta1/TokenReview, namespace: string, name: string): TokenReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/LocalSubjectAccessReview, name: string): LocalSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/LocalSubjectAccessReview, namespace: string, name: string): LocalSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SelfSubjectAccessReview, name: string): SelfSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SelfSubjectAccessReview, namespace: string, name: string): SelfSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SelfSubjectRulesReview, name: string): SelfSubjectRulesReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SelfSubjectRulesReview, namespace: string, name: string): SelfSubjectRulesReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SubjectAccessReview, name: string): SubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SubjectAccessReview, namespace: string, name: string): SubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/LocalSubjectAccessReview, name: string): LocalSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/LocalSubjectAccessReview, namespace: string, name: string): LocalSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SelfSubjectAccessReview, name: string): SelfSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SelfSubjectAccessReview, namespace: string, name: string): SelfSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SelfSubjectRulesReview, name: string): SelfSubjectRulesReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SelfSubjectRulesReview, namespace: string, name: string): SelfSubjectRulesReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SubjectAccessReview, name: string): SubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SubjectAccessReview, namespace: string, name: string): SubjectAccessReview
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/CrossVersionObjectReference, name: string): CrossVersionObjectReference
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/CrossVersionObjectReference, namespace: string, name: string): CrossVersionObjectReference
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/HorizontalPodAutoscaler, name: string): HorizontalPodAutoscaler
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/HorizontalPodAutoscaler, namespace: string, name: string): HorizontalPodAutoscaler
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/HorizontalPodAutoscalerList, name: string): HorizontalPodAutoscalerList
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/HorizontalPodAutoscalerList, namespace: string, name: string): HorizontalPodAutoscalerList
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/Scale, name: string): Scale
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/Scale, namespace: string, name: string): Scale
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/CrossVersionObjectReference, name: string): CrossVersionObjectReference
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/CrossVersionObjectReference, namespace: string, name: string): CrossVersionObjectReference
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/HorizontalPodAutoscaler, name: string): HorizontalPodAutoscaler
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/HorizontalPodAutoscaler, namespace: string, name: string): HorizontalPodAutoscaler
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/HorizontalPodAutoscalerList, name: string): HorizontalPodAutoscalerList
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/HorizontalPodAutoscalerList, namespace: string, name: string): HorizontalPodAutoscalerList
```


```typescript
public getResource(groupVersionKind: batch/v1/Job, name: string): Job
```


```typescript
public getResource(groupVersionKind: batch/v1/Job, namespace: string, name: string): Job
```


```typescript
public getResource(groupVersionKind: batch/v1/JobList, name: string): JobList
```


```typescript
public getResource(groupVersionKind: batch/v1/JobList, namespace: string, name: string): JobList
```


```typescript
public getResource(groupVersionKind: batch/v1beta1/CronJob, name: string): CronJob
```


```typescript
public getResource(groupVersionKind: batch/v1beta1/CronJob, namespace: string, name: string): CronJob
```


```typescript
public getResource(groupVersionKind: batch/v1beta1/CronJobList, name: string): CronJobList
```


```typescript
public getResource(groupVersionKind: batch/v1beta1/CronJobList, namespace: string, name: string): CronJobList
```


```typescript
public getResource(groupVersionKind: batch/v2alpha1/CronJob, name: string): CronJob
```


```typescript
public getResource(groupVersionKind: batch/v2alpha1/CronJob, namespace: string, name: string): CronJob
```


```typescript
public getResource(groupVersionKind: batch/v2alpha1/CronJobList, name: string): CronJobList
```


```typescript
public getResource(groupVersionKind: batch/v2alpha1/CronJobList, namespace: string, name: string): CronJobList
```


```typescript
public getResource(groupVersionKind: certificates.k8s.io/v1beta1/CertificateSigningRequest, name: string): CertificateSigningRequest
```


```typescript
public getResource(groupVersionKind: certificates.k8s.io/v1beta1/CertificateSigningRequest, namespace: string, name: string): CertificateSigningRequest
```


```typescript
public getResource(groupVersionKind: certificates.k8s.io/v1beta1/CertificateSigningRequestList, name: string): CertificateSigningRequestList
```


```typescript
public getResource(groupVersionKind: certificates.k8s.io/v1beta1/CertificateSigningRequestList, namespace: string, name: string): CertificateSigningRequestList
```


```typescript
public getResource(groupVersionKind: v1/Binding, name: string): Binding
```


```typescript
public getResource(groupVersionKind: v1/Binding, namespace: string, name: string): Binding
```


```typescript
public getResource(groupVersionKind: v1/ComponentStatus, name: string): ComponentStatus
```


```typescript
public getResource(groupVersionKind: v1/ComponentStatus, namespace: string, name: string): ComponentStatus
```


```typescript
public getResource(groupVersionKind: v1/ComponentStatusList, name: string): ComponentStatusList
```


```typescript
public getResource(groupVersionKind: v1/ComponentStatusList, namespace: string, name: string): ComponentStatusList
```


```typescript
public getResource(groupVersionKind: v1/ConfigMap, name: string): ConfigMap
```


```typescript
public getResource(groupVersionKind: v1/ConfigMap, namespace: string, name: string): ConfigMap
```


```typescript
public getResource(groupVersionKind: v1/ConfigMapList, name: string): ConfigMapList
```


```typescript
public getResource(groupVersionKind: v1/ConfigMapList, namespace: string, name: string): ConfigMapList
```


```typescript
public getResource(groupVersionKind: v1/Endpoints, name: string): Endpoints
```


```typescript
public getResource(groupVersionKind: v1/Endpoints, namespace: string, name: string): Endpoints
```


```typescript
public getResource(groupVersionKind: v1/EndpointsList, name: string): EndpointsList
```


```typescript
public getResource(groupVersionKind: v1/EndpointsList, namespace: string, name: string): EndpointsList
```


```typescript
public getResource(groupVersionKind: v1/Event, name: string): Event
```


```typescript
public getResource(groupVersionKind: v1/Event, namespace: string, name: string): Event
```


```typescript
public getResource(groupVersionKind: v1/EventList, name: string): EventList
```


```typescript
public getResource(groupVersionKind: v1/EventList, namespace: string, name: string): EventList
```


```typescript
public getResource(groupVersionKind: v1/LimitRange, name: string): LimitRange
```


```typescript
public getResource(groupVersionKind: v1/LimitRange, namespace: string, name: string): LimitRange
```


```typescript
public getResource(groupVersionKind: v1/LimitRangeList, name: string): LimitRangeList
```


```typescript
public getResource(groupVersionKind: v1/LimitRangeList, namespace: string, name: string): LimitRangeList
```


```typescript
public getResource(groupVersionKind: v1/Namespace, name: string): Namespace
```


```typescript
public getResource(groupVersionKind: v1/Namespace, namespace: string, name: string): Namespace
```


```typescript
public getResource(groupVersionKind: v1/NamespaceList, name: string): NamespaceList
```


```typescript
public getResource(groupVersionKind: v1/NamespaceList, namespace: string, name: string): NamespaceList
```


```typescript
public getResource(groupVersionKind: v1/Node, name: string): Node
```


```typescript
public getResource(groupVersionKind: v1/Node, namespace: string, name: string): Node
```


```typescript
public getResource(groupVersionKind: v1/NodeConfigSource, name: string): NodeConfigSource
```


```typescript
public getResource(groupVersionKind: v1/NodeConfigSource, namespace: string, name: string): NodeConfigSource
```


```typescript
public getResource(groupVersionKind: v1/NodeList, name: string): NodeList
```


```typescript
public getResource(groupVersionKind: v1/NodeList, namespace: string, name: string): NodeList
```


```typescript
public getResource(groupVersionKind: core/v1/ObjectReference, name: string): ObjectReference
```


```typescript
public getResource(groupVersionKind: core/v1/ObjectReference, namespace: string, name: string): ObjectReference
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolume, name: string): PersistentVolume
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolume, namespace: string, name: string): PersistentVolume
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeClaim, name: string): PersistentVolumeClaim
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeClaim, namespace: string, name: string): PersistentVolumeClaim
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeClaimList, name: string): PersistentVolumeClaimList
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeClaimList, namespace: string, name: string): PersistentVolumeClaimList
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeList, name: string): PersistentVolumeList
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeList, namespace: string, name: string): PersistentVolumeList
```


```typescript
public getResource(groupVersionKind: v1/Pod, name: string): Pod
```


```typescript
public getResource(groupVersionKind: v1/Pod, namespace: string, name: string): Pod
```


```typescript
public getResource(groupVersionKind: v1/PodList, name: string): PodList
```


```typescript
public getResource(groupVersionKind: v1/PodList, namespace: string, name: string): PodList
```


```typescript
public getResource(groupVersionKind: v1/PodTemplate, name: string): PodTemplate
```


```typescript
public getResource(groupVersionKind: v1/PodTemplate, namespace: string, name: string): PodTemplate
```


```typescript
public getResource(groupVersionKind: v1/PodTemplateList, name: string): PodTemplateList
```


```typescript
public getResource(groupVersionKind: v1/PodTemplateList, namespace: string, name: string): PodTemplateList
```


```typescript
public getResource(groupVersionKind: v1/ReplicationController, name: string): ReplicationController
```


```typescript
public getResource(groupVersionKind: v1/ReplicationController, namespace: string, name: string): ReplicationController
```


```typescript
public getResource(groupVersionKind: v1/ReplicationControllerList, name: string): ReplicationControllerList
```


```typescript
public getResource(groupVersionKind: v1/ReplicationControllerList, namespace: string, name: string): ReplicationControllerList
```


```typescript
public getResource(groupVersionKind: v1/ResourceQuota, name: string): ResourceQuota
```


```typescript
public getResource(groupVersionKind: v1/ResourceQuota, namespace: string, name: string): ResourceQuota
```


```typescript
public getResource(groupVersionKind: v1/ResourceQuotaList, name: string): ResourceQuotaList
```


```typescript
public getResource(groupVersionKind: v1/ResourceQuotaList, namespace: string, name: string): ResourceQuotaList
```


```typescript
public getResource(groupVersionKind: v1/Secret, name: string): Secret
```


```typescript
public getResource(groupVersionKind: v1/Secret, namespace: string, name: string): Secret
```


```typescript
public getResource(groupVersionKind: v1/SecretList, name: string): SecretList
```


```typescript
public getResource(groupVersionKind: v1/SecretList, namespace: string, name: string): SecretList
```


```typescript
public getResource(groupVersionKind: v1/Service, name: string): Service
```


```typescript
public getResource(groupVersionKind: v1/Service, namespace: string, name: string): Service
```


```typescript
public getResource(groupVersionKind: v1/ServiceAccount, name: string): ServiceAccount
```


```typescript
public getResource(groupVersionKind: v1/ServiceAccount, namespace: string, name: string): ServiceAccount
```


```typescript
public getResource(groupVersionKind: v1/ServiceAccountList, name: string): ServiceAccountList
```


```typescript
public getResource(groupVersionKind: v1/ServiceAccountList, namespace: string, name: string): ServiceAccountList
```


```typescript
public getResource(groupVersionKind: v1/ServiceList, name: string): ServiceList
```


```typescript
public getResource(groupVersionKind: v1/ServiceList, namespace: string, name: string): ServiceList
```


```typescript
public getResource(groupVersionKind: events.k8s.io/v1beta1/Event, name: string): Event
```


```typescript
public getResource(groupVersionKind: events.k8s.io/v1beta1/Event, namespace: string, name: string): Event
```


```typescript
public getResource(groupVersionKind: events.k8s.io/v1beta1/EventList, name: string): EventList
```


```typescript
public getResource(groupVersionKind: events.k8s.io/v1beta1/EventList, namespace: string, name: string): EventList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DaemonSet, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DaemonSet, namespace: string, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DaemonSetList, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DaemonSetList, namespace: string, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Deployment, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Deployment, namespace: string, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DeploymentList, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DeploymentList, namespace: string, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DeploymentRollback, name: string): DeploymentRollback
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DeploymentRollback, namespace: string, name: string): DeploymentRollback
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Ingress, name: string): Ingress
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Ingress, namespace: string, name: string): Ingress
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/IngressList, name: string): IngressList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/IngressList, namespace: string, name: string): IngressList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/NetworkPolicy, name: string): NetworkPolicy
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/NetworkPolicy, namespace: string, name: string): NetworkPolicy
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/NetworkPolicyList, name: string): NetworkPolicyList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/NetworkPolicyList, namespace: string, name: string): NetworkPolicyList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/PodSecurityPolicy, name: string): PodSecurityPolicy
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/PodSecurityPolicy, namespace: string, name: string): PodSecurityPolicy
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/PodSecurityPolicyList, name: string): PodSecurityPolicyList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/PodSecurityPolicyList, namespace: string, name: string): PodSecurityPolicyList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/ReplicaSet, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/ReplicaSet, namespace: string, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/ReplicaSetList, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/ReplicaSetList, namespace: string, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Scale, name: string): Scale
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Scale, namespace: string, name: string): Scale
```


```typescript
public getResource(groupVersionKind: v1/APIGroup, name: string): APIGroup
```


```typescript
public getResource(groupVersionKind: v1/APIGroup, namespace: string, name: string): APIGroup
```


```typescript
public getResource(groupVersionKind: v1/APIGroupList, name: string): APIGroupList
```


```typescript
public getResource(groupVersionKind: v1/APIGroupList, namespace: string, name: string): APIGroupList
```


```typescript
public getResource(groupVersionKind: v1/APIResourceList, name: string): APIResourceList
```


```typescript
public getResource(groupVersionKind: v1/APIResourceList, namespace: string, name: string): APIResourceList
```


```typescript
public getResource(groupVersionKind: v1/APIVersions, name: string): APIVersions
```


```typescript
public getResource(groupVersionKind: v1/APIVersions, namespace: string, name: string): APIVersions
```


```typescript
public getResource(groupVersionKind: v1/DeleteOptions, name: string): DeleteOptions
```


```typescript
public getResource(groupVersionKind: v1/DeleteOptions, namespace: string, name: string): DeleteOptions
```


```typescript
public getResource(groupVersionKind: meta/v1/OwnerReference, name: string): OwnerReference
```


```typescript
public getResource(groupVersionKind: meta/v1/OwnerReference, namespace: string, name: string): OwnerReference
```


```typescript
public getResource(groupVersionKind: v1/Status, name: string): Status
```


```typescript
public getResource(groupVersionKind: v1/Status, namespace: string, name: string): Status
```


```typescript
public getResource(groupVersionKind: networking.k8s.io/v1/NetworkPolicy, name: string): NetworkPolicy
```


```typescript
public getResource(groupVersionKind: networking.k8s.io/v1/NetworkPolicy, namespace: string, name: string): NetworkPolicy
```


```typescript
public getResource(groupVersionKind: networking.k8s.io/v1/NetworkPolicyList, name: string): NetworkPolicyList
```


```typescript
public getResource(groupVersionKind: networking.k8s.io/v1/NetworkPolicyList, namespace: string, name: string): NetworkPolicyList
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/Eviction, name: string): Eviction
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/Eviction, namespace: string, name: string): Eviction
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/PodDisruptionBudget, name: string): PodDisruptionBudget
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/PodDisruptionBudget, namespace: string, name: string): PodDisruptionBudget
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/PodDisruptionBudgetList, name: string): PodDisruptionBudgetList
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/PodDisruptionBudgetList, namespace: string, name: string): PodDisruptionBudgetList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRole, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRole, namespace: string, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleBinding, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleBinding, namespace: string, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleBindingList, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleBindingList, namespace: string, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleList, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleList, namespace: string, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/Role, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/Role, namespace: string, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleBinding, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleBinding, namespace: string, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleBindingList, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleBindingList, namespace: string, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleList, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleList, namespace: string, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRole, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRole, namespace: string, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleBinding, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleBinding, namespace: string, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleBindingList, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleBindingList, namespace: string, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleList, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleList, namespace: string, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/Role, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/Role, namespace: string, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleBinding, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleBinding, namespace: string, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleBindingList, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleBindingList, namespace: string, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleList, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleList, namespace: string, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: rbac/v1alpha1/Subject, name: string): Subject
```


```typescript
public getResource(groupVersionKind: rbac/v1alpha1/Subject, namespace: string, name: string): Subject
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRole, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRole, namespace: string, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleBinding, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleBinding, namespace: string, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleBindingList, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleBindingList, namespace: string, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleList, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleList, namespace: string, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/Role, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/Role, namespace: string, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleBinding, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleBinding, namespace: string, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleBindingList, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleBindingList, namespace: string, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleList, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleList, namespace: string, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: scheduling.k8s.io/v1alpha1/PriorityClass, name: string): PriorityClass
```


```typescript
public getResource(groupVersionKind: scheduling.k8s.io/v1alpha1/PriorityClass, namespace: string, name: string): PriorityClass
```


```typescript
public getResource(groupVersionKind: scheduling.k8s.io/v1alpha1/PriorityClassList, name: string): PriorityClassList
```


```typescript
public getResource(groupVersionKind: scheduling.k8s.io/v1alpha1/PriorityClassList, namespace: string, name: string): PriorityClassList
```


```typescript
public getResource(groupVersionKind: settings.k8s.io/v1alpha1/PodPreset, name: string): PodPreset
```


```typescript
public getResource(groupVersionKind: settings.k8s.io/v1alpha1/PodPreset, namespace: string, name: string): PodPreset
```


```typescript
public getResource(groupVersionKind: settings.k8s.io/v1alpha1/PodPresetList, name: string): PodPresetList
```


```typescript
public getResource(groupVersionKind: settings.k8s.io/v1alpha1/PodPresetList, namespace: string, name: string): PodPresetList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1/StorageClass, name: string): StorageClass
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1/StorageClass, namespace: string, name: string): StorageClass
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1/StorageClassList, name: string): StorageClassList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1/StorageClassList, namespace: string, name: string): StorageClassList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1alpha1/VolumeAttachment, name: string): VolumeAttachment
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1alpha1/VolumeAttachment, namespace: string, name: string): VolumeAttachment
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1alpha1/VolumeAttachmentList, name: string): VolumeAttachmentList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1alpha1/VolumeAttachmentList, namespace: string, name: string): VolumeAttachmentList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1beta1/StorageClass, name: string): StorageClass
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1beta1/StorageClass, namespace: string, name: string): StorageClass
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1beta1/StorageClassList, name: string): StorageClassList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1beta1/StorageClassList, namespace: string, name: string): StorageClassList
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L81">property resources</a>
</h3>

```typescript
resources: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ConfigGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L442">class ConfigGroup</a>
</h2>

ConfigGroup creates a set of Kubernetes resources from Kubernetes YAML text. The YAML text
may be supplied using any of the following `ConfigGroupOpts`:

  1. Using a filename or a list of filenames:
       a. `{files: "foo.yaml"}`
       b. `{files: ["foo.yaml", "bar.yaml"]}`
  2. Using a file pattern or a list of file patterns:
       a. `{files: "*.yaml"}`
       b. `{files: ["foo/*.yaml", "bar/*.yaml"]}`
  3. Using a literal string containing YAML, or a list of such strings:
       a. `{yaml: "(LITERAL YAML HERE)"}`
       b. `{yaml: ["(LITERAL YAML HERE)", "(MORE YAML)"]}`
  4. Any combination of files, patterns, or YAML strings:
       a. `{files: "foo.yaml", yaml: "(LITERAL YAML HERE)"}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L442">constructor</a>
</h3>

```typescript
new ConfigGroup(name: string, config: ConfigGroupOpts, opts?: pulumi.ComponentResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L89">method getResource</a>
</h3>

```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1alpha1/InitializerConfiguration, name: string): InitializerConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1alpha1/InitializerConfiguration, namespace: string, name: string): InitializerConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1alpha1/InitializerConfigurationList, name: string): InitializerConfigurationList
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1alpha1/InitializerConfigurationList, namespace: string, name: string): InitializerConfigurationList
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/MutatingWebhookConfiguration, name: string): MutatingWebhookConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/MutatingWebhookConfiguration, namespace: string, name: string): MutatingWebhookConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/MutatingWebhookConfigurationList, name: string): MutatingWebhookConfigurationList
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/MutatingWebhookConfigurationList, namespace: string, name: string): MutatingWebhookConfigurationList
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/ValidatingWebhookConfiguration, name: string): ValidatingWebhookConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/ValidatingWebhookConfiguration, namespace: string, name: string): ValidatingWebhookConfiguration
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/ValidatingWebhookConfigurationList, name: string): ValidatingWebhookConfigurationList
```


```typescript
public getResource(groupVersionKind: admissionregistration.k8s.io/v1beta1/ValidatingWebhookConfigurationList, namespace: string, name: string): ValidatingWebhookConfigurationList
```


```typescript
public getResource(groupVersionKind: apiextensions.k8s.io/v1beta1/CustomResourceDefinition, name: string): CustomResourceDefinition
```


```typescript
public getResource(groupVersionKind: apiextensions.k8s.io/v1beta1/CustomResourceDefinition, namespace: string, name: string): CustomResourceDefinition
```


```typescript
public getResource(groupVersionKind: apiextensions.k8s.io/v1beta1/CustomResourceDefinitionList, name: string): CustomResourceDefinitionList
```


```typescript
public getResource(groupVersionKind: apiextensions.k8s.io/v1beta1/CustomResourceDefinitionList, namespace: string, name: string): CustomResourceDefinitionList
```


```typescript
public getResource(groupVersionKind: apiregistration/v1beta1/APIService, name: string): APIService
```


```typescript
public getResource(groupVersionKind: apiregistration/v1beta1/APIService, namespace: string, name: string): APIService
```


```typescript
public getResource(groupVersionKind: apiregistration/v1beta1/APIServiceList, name: string): APIServiceList
```


```typescript
public getResource(groupVersionKind: apiregistration/v1beta1/APIServiceList, namespace: string, name: string): APIServiceList
```


```typescript
public getResource(groupVersionKind: apps/v1/ControllerRevision, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1/ControllerRevision, namespace: string, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1/ControllerRevisionList, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1/ControllerRevisionList, namespace: string, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1/DaemonSet, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: apps/v1/DaemonSet, namespace: string, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: apps/v1/DaemonSetList, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: apps/v1/DaemonSetList, namespace: string, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: apps/v1/Deployment, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1/Deployment, namespace: string, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1/DeploymentList, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1/DeploymentList, namespace: string, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1/ReplicaSet, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: apps/v1/ReplicaSet, namespace: string, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: apps/v1/ReplicaSetList, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: apps/v1/ReplicaSetList, namespace: string, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: apps/v1/StatefulSet, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1/StatefulSet, namespace: string, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1/StatefulSetList, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: apps/v1/StatefulSetList, namespace: string, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/ControllerRevision, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/ControllerRevision, namespace: string, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/ControllerRevisionList, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/ControllerRevisionList, namespace: string, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/Deployment, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/Deployment, namespace: string, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/DeploymentList, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/DeploymentList, namespace: string, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/DeploymentRollback, name: string): DeploymentRollback
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/DeploymentRollback, namespace: string, name: string): DeploymentRollback
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/Scale, name: string): Scale
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/Scale, namespace: string, name: string): Scale
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/StatefulSet, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/StatefulSet, namespace: string, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/StatefulSetList, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta1/StatefulSetList, namespace: string, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ControllerRevision, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ControllerRevision, namespace: string, name: string): ControllerRevision
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ControllerRevisionList, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ControllerRevisionList, namespace: string, name: string): ControllerRevisionList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DaemonSet, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DaemonSet, namespace: string, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DaemonSetList, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DaemonSetList, namespace: string, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/Deployment, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/Deployment, namespace: string, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DeploymentList, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/DeploymentList, namespace: string, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ReplicaSet, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ReplicaSet, namespace: string, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ReplicaSetList, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/ReplicaSetList, namespace: string, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/Scale, name: string): Scale
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/Scale, namespace: string, name: string): Scale
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/StatefulSet, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/StatefulSet, namespace: string, name: string): StatefulSet
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/StatefulSetList, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: apps/v1beta2/StatefulSetList, namespace: string, name: string): StatefulSetList
```


```typescript
public getResource(groupVersionKind: authentication.k8s.io/v1/TokenReview, name: string): TokenReview
```


```typescript
public getResource(groupVersionKind: authentication.k8s.io/v1/TokenReview, namespace: string, name: string): TokenReview
```


```typescript
public getResource(groupVersionKind: authentication.k8s.io/v1beta1/TokenReview, name: string): TokenReview
```


```typescript
public getResource(groupVersionKind: authentication.k8s.io/v1beta1/TokenReview, namespace: string, name: string): TokenReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/LocalSubjectAccessReview, name: string): LocalSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/LocalSubjectAccessReview, namespace: string, name: string): LocalSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SelfSubjectAccessReview, name: string): SelfSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SelfSubjectAccessReview, namespace: string, name: string): SelfSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SelfSubjectRulesReview, name: string): SelfSubjectRulesReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SelfSubjectRulesReview, namespace: string, name: string): SelfSubjectRulesReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SubjectAccessReview, name: string): SubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1/SubjectAccessReview, namespace: string, name: string): SubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/LocalSubjectAccessReview, name: string): LocalSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/LocalSubjectAccessReview, namespace: string, name: string): LocalSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SelfSubjectAccessReview, name: string): SelfSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SelfSubjectAccessReview, namespace: string, name: string): SelfSubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SelfSubjectRulesReview, name: string): SelfSubjectRulesReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SelfSubjectRulesReview, namespace: string, name: string): SelfSubjectRulesReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SubjectAccessReview, name: string): SubjectAccessReview
```


```typescript
public getResource(groupVersionKind: authorization.k8s.io/v1beta1/SubjectAccessReview, namespace: string, name: string): SubjectAccessReview
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/CrossVersionObjectReference, name: string): CrossVersionObjectReference
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/CrossVersionObjectReference, namespace: string, name: string): CrossVersionObjectReference
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/HorizontalPodAutoscaler, name: string): HorizontalPodAutoscaler
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/HorizontalPodAutoscaler, namespace: string, name: string): HorizontalPodAutoscaler
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/HorizontalPodAutoscalerList, name: string): HorizontalPodAutoscalerList
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/HorizontalPodAutoscalerList, namespace: string, name: string): HorizontalPodAutoscalerList
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/Scale, name: string): Scale
```


```typescript
public getResource(groupVersionKind: autoscaling/v1/Scale, namespace: string, name: string): Scale
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/CrossVersionObjectReference, name: string): CrossVersionObjectReference
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/CrossVersionObjectReference, namespace: string, name: string): CrossVersionObjectReference
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/HorizontalPodAutoscaler, name: string): HorizontalPodAutoscaler
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/HorizontalPodAutoscaler, namespace: string, name: string): HorizontalPodAutoscaler
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/HorizontalPodAutoscalerList, name: string): HorizontalPodAutoscalerList
```


```typescript
public getResource(groupVersionKind: autoscaling/v2beta1/HorizontalPodAutoscalerList, namespace: string, name: string): HorizontalPodAutoscalerList
```


```typescript
public getResource(groupVersionKind: batch/v1/Job, name: string): Job
```


```typescript
public getResource(groupVersionKind: batch/v1/Job, namespace: string, name: string): Job
```


```typescript
public getResource(groupVersionKind: batch/v1/JobList, name: string): JobList
```


```typescript
public getResource(groupVersionKind: batch/v1/JobList, namespace: string, name: string): JobList
```


```typescript
public getResource(groupVersionKind: batch/v1beta1/CronJob, name: string): CronJob
```


```typescript
public getResource(groupVersionKind: batch/v1beta1/CronJob, namespace: string, name: string): CronJob
```


```typescript
public getResource(groupVersionKind: batch/v1beta1/CronJobList, name: string): CronJobList
```


```typescript
public getResource(groupVersionKind: batch/v1beta1/CronJobList, namespace: string, name: string): CronJobList
```


```typescript
public getResource(groupVersionKind: batch/v2alpha1/CronJob, name: string): CronJob
```


```typescript
public getResource(groupVersionKind: batch/v2alpha1/CronJob, namespace: string, name: string): CronJob
```


```typescript
public getResource(groupVersionKind: batch/v2alpha1/CronJobList, name: string): CronJobList
```


```typescript
public getResource(groupVersionKind: batch/v2alpha1/CronJobList, namespace: string, name: string): CronJobList
```


```typescript
public getResource(groupVersionKind: certificates.k8s.io/v1beta1/CertificateSigningRequest, name: string): CertificateSigningRequest
```


```typescript
public getResource(groupVersionKind: certificates.k8s.io/v1beta1/CertificateSigningRequest, namespace: string, name: string): CertificateSigningRequest
```


```typescript
public getResource(groupVersionKind: certificates.k8s.io/v1beta1/CertificateSigningRequestList, name: string): CertificateSigningRequestList
```


```typescript
public getResource(groupVersionKind: certificates.k8s.io/v1beta1/CertificateSigningRequestList, namespace: string, name: string): CertificateSigningRequestList
```


```typescript
public getResource(groupVersionKind: v1/Binding, name: string): Binding
```


```typescript
public getResource(groupVersionKind: v1/Binding, namespace: string, name: string): Binding
```


```typescript
public getResource(groupVersionKind: v1/ComponentStatus, name: string): ComponentStatus
```


```typescript
public getResource(groupVersionKind: v1/ComponentStatus, namespace: string, name: string): ComponentStatus
```


```typescript
public getResource(groupVersionKind: v1/ComponentStatusList, name: string): ComponentStatusList
```


```typescript
public getResource(groupVersionKind: v1/ComponentStatusList, namespace: string, name: string): ComponentStatusList
```


```typescript
public getResource(groupVersionKind: v1/ConfigMap, name: string): ConfigMap
```


```typescript
public getResource(groupVersionKind: v1/ConfigMap, namespace: string, name: string): ConfigMap
```


```typescript
public getResource(groupVersionKind: v1/ConfigMapList, name: string): ConfigMapList
```


```typescript
public getResource(groupVersionKind: v1/ConfigMapList, namespace: string, name: string): ConfigMapList
```


```typescript
public getResource(groupVersionKind: v1/Endpoints, name: string): Endpoints
```


```typescript
public getResource(groupVersionKind: v1/Endpoints, namespace: string, name: string): Endpoints
```


```typescript
public getResource(groupVersionKind: v1/EndpointsList, name: string): EndpointsList
```


```typescript
public getResource(groupVersionKind: v1/EndpointsList, namespace: string, name: string): EndpointsList
```


```typescript
public getResource(groupVersionKind: v1/Event, name: string): Event
```


```typescript
public getResource(groupVersionKind: v1/Event, namespace: string, name: string): Event
```


```typescript
public getResource(groupVersionKind: v1/EventList, name: string): EventList
```


```typescript
public getResource(groupVersionKind: v1/EventList, namespace: string, name: string): EventList
```


```typescript
public getResource(groupVersionKind: v1/LimitRange, name: string): LimitRange
```


```typescript
public getResource(groupVersionKind: v1/LimitRange, namespace: string, name: string): LimitRange
```


```typescript
public getResource(groupVersionKind: v1/LimitRangeList, name: string): LimitRangeList
```


```typescript
public getResource(groupVersionKind: v1/LimitRangeList, namespace: string, name: string): LimitRangeList
```


```typescript
public getResource(groupVersionKind: v1/Namespace, name: string): Namespace
```


```typescript
public getResource(groupVersionKind: v1/Namespace, namespace: string, name: string): Namespace
```


```typescript
public getResource(groupVersionKind: v1/NamespaceList, name: string): NamespaceList
```


```typescript
public getResource(groupVersionKind: v1/NamespaceList, namespace: string, name: string): NamespaceList
```


```typescript
public getResource(groupVersionKind: v1/Node, name: string): Node
```


```typescript
public getResource(groupVersionKind: v1/Node, namespace: string, name: string): Node
```


```typescript
public getResource(groupVersionKind: v1/NodeConfigSource, name: string): NodeConfigSource
```


```typescript
public getResource(groupVersionKind: v1/NodeConfigSource, namespace: string, name: string): NodeConfigSource
```


```typescript
public getResource(groupVersionKind: v1/NodeList, name: string): NodeList
```


```typescript
public getResource(groupVersionKind: v1/NodeList, namespace: string, name: string): NodeList
```


```typescript
public getResource(groupVersionKind: core/v1/ObjectReference, name: string): ObjectReference
```


```typescript
public getResource(groupVersionKind: core/v1/ObjectReference, namespace: string, name: string): ObjectReference
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolume, name: string): PersistentVolume
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolume, namespace: string, name: string): PersistentVolume
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeClaim, name: string): PersistentVolumeClaim
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeClaim, namespace: string, name: string): PersistentVolumeClaim
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeClaimList, name: string): PersistentVolumeClaimList
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeClaimList, namespace: string, name: string): PersistentVolumeClaimList
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeList, name: string): PersistentVolumeList
```


```typescript
public getResource(groupVersionKind: v1/PersistentVolumeList, namespace: string, name: string): PersistentVolumeList
```


```typescript
public getResource(groupVersionKind: v1/Pod, name: string): Pod
```


```typescript
public getResource(groupVersionKind: v1/Pod, namespace: string, name: string): Pod
```


```typescript
public getResource(groupVersionKind: v1/PodList, name: string): PodList
```


```typescript
public getResource(groupVersionKind: v1/PodList, namespace: string, name: string): PodList
```


```typescript
public getResource(groupVersionKind: v1/PodTemplate, name: string): PodTemplate
```


```typescript
public getResource(groupVersionKind: v1/PodTemplate, namespace: string, name: string): PodTemplate
```


```typescript
public getResource(groupVersionKind: v1/PodTemplateList, name: string): PodTemplateList
```


```typescript
public getResource(groupVersionKind: v1/PodTemplateList, namespace: string, name: string): PodTemplateList
```


```typescript
public getResource(groupVersionKind: v1/ReplicationController, name: string): ReplicationController
```


```typescript
public getResource(groupVersionKind: v1/ReplicationController, namespace: string, name: string): ReplicationController
```


```typescript
public getResource(groupVersionKind: v1/ReplicationControllerList, name: string): ReplicationControllerList
```


```typescript
public getResource(groupVersionKind: v1/ReplicationControllerList, namespace: string, name: string): ReplicationControllerList
```


```typescript
public getResource(groupVersionKind: v1/ResourceQuota, name: string): ResourceQuota
```


```typescript
public getResource(groupVersionKind: v1/ResourceQuota, namespace: string, name: string): ResourceQuota
```


```typescript
public getResource(groupVersionKind: v1/ResourceQuotaList, name: string): ResourceQuotaList
```


```typescript
public getResource(groupVersionKind: v1/ResourceQuotaList, namespace: string, name: string): ResourceQuotaList
```


```typescript
public getResource(groupVersionKind: v1/Secret, name: string): Secret
```


```typescript
public getResource(groupVersionKind: v1/Secret, namespace: string, name: string): Secret
```


```typescript
public getResource(groupVersionKind: v1/SecretList, name: string): SecretList
```


```typescript
public getResource(groupVersionKind: v1/SecretList, namespace: string, name: string): SecretList
```


```typescript
public getResource(groupVersionKind: v1/Service, name: string): Service
```


```typescript
public getResource(groupVersionKind: v1/Service, namespace: string, name: string): Service
```


```typescript
public getResource(groupVersionKind: v1/ServiceAccount, name: string): ServiceAccount
```


```typescript
public getResource(groupVersionKind: v1/ServiceAccount, namespace: string, name: string): ServiceAccount
```


```typescript
public getResource(groupVersionKind: v1/ServiceAccountList, name: string): ServiceAccountList
```


```typescript
public getResource(groupVersionKind: v1/ServiceAccountList, namespace: string, name: string): ServiceAccountList
```


```typescript
public getResource(groupVersionKind: v1/ServiceList, name: string): ServiceList
```


```typescript
public getResource(groupVersionKind: v1/ServiceList, namespace: string, name: string): ServiceList
```


```typescript
public getResource(groupVersionKind: events.k8s.io/v1beta1/Event, name: string): Event
```


```typescript
public getResource(groupVersionKind: events.k8s.io/v1beta1/Event, namespace: string, name: string): Event
```


```typescript
public getResource(groupVersionKind: events.k8s.io/v1beta1/EventList, name: string): EventList
```


```typescript
public getResource(groupVersionKind: events.k8s.io/v1beta1/EventList, namespace: string, name: string): EventList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DaemonSet, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DaemonSet, namespace: string, name: string): DaemonSet
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DaemonSetList, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DaemonSetList, namespace: string, name: string): DaemonSetList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Deployment, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Deployment, namespace: string, name: string): Deployment
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DeploymentList, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DeploymentList, namespace: string, name: string): DeploymentList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DeploymentRollback, name: string): DeploymentRollback
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/DeploymentRollback, namespace: string, name: string): DeploymentRollback
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Ingress, name: string): Ingress
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Ingress, namespace: string, name: string): Ingress
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/IngressList, name: string): IngressList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/IngressList, namespace: string, name: string): IngressList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/NetworkPolicy, name: string): NetworkPolicy
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/NetworkPolicy, namespace: string, name: string): NetworkPolicy
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/NetworkPolicyList, name: string): NetworkPolicyList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/NetworkPolicyList, namespace: string, name: string): NetworkPolicyList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/PodSecurityPolicy, name: string): PodSecurityPolicy
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/PodSecurityPolicy, namespace: string, name: string): PodSecurityPolicy
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/PodSecurityPolicyList, name: string): PodSecurityPolicyList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/PodSecurityPolicyList, namespace: string, name: string): PodSecurityPolicyList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/ReplicaSet, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/ReplicaSet, namespace: string, name: string): ReplicaSet
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/ReplicaSetList, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/ReplicaSetList, namespace: string, name: string): ReplicaSetList
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Scale, name: string): Scale
```


```typescript
public getResource(groupVersionKind: extensions/v1beta1/Scale, namespace: string, name: string): Scale
```


```typescript
public getResource(groupVersionKind: v1/APIGroup, name: string): APIGroup
```


```typescript
public getResource(groupVersionKind: v1/APIGroup, namespace: string, name: string): APIGroup
```


```typescript
public getResource(groupVersionKind: v1/APIGroupList, name: string): APIGroupList
```


```typescript
public getResource(groupVersionKind: v1/APIGroupList, namespace: string, name: string): APIGroupList
```


```typescript
public getResource(groupVersionKind: v1/APIResourceList, name: string): APIResourceList
```


```typescript
public getResource(groupVersionKind: v1/APIResourceList, namespace: string, name: string): APIResourceList
```


```typescript
public getResource(groupVersionKind: v1/APIVersions, name: string): APIVersions
```


```typescript
public getResource(groupVersionKind: v1/APIVersions, namespace: string, name: string): APIVersions
```


```typescript
public getResource(groupVersionKind: v1/DeleteOptions, name: string): DeleteOptions
```


```typescript
public getResource(groupVersionKind: v1/DeleteOptions, namespace: string, name: string): DeleteOptions
```


```typescript
public getResource(groupVersionKind: meta/v1/OwnerReference, name: string): OwnerReference
```


```typescript
public getResource(groupVersionKind: meta/v1/OwnerReference, namespace: string, name: string): OwnerReference
```


```typescript
public getResource(groupVersionKind: v1/Status, name: string): Status
```


```typescript
public getResource(groupVersionKind: v1/Status, namespace: string, name: string): Status
```


```typescript
public getResource(groupVersionKind: networking.k8s.io/v1/NetworkPolicy, name: string): NetworkPolicy
```


```typescript
public getResource(groupVersionKind: networking.k8s.io/v1/NetworkPolicy, namespace: string, name: string): NetworkPolicy
```


```typescript
public getResource(groupVersionKind: networking.k8s.io/v1/NetworkPolicyList, name: string): NetworkPolicyList
```


```typescript
public getResource(groupVersionKind: networking.k8s.io/v1/NetworkPolicyList, namespace: string, name: string): NetworkPolicyList
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/Eviction, name: string): Eviction
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/Eviction, namespace: string, name: string): Eviction
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/PodDisruptionBudget, name: string): PodDisruptionBudget
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/PodDisruptionBudget, namespace: string, name: string): PodDisruptionBudget
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/PodDisruptionBudgetList, name: string): PodDisruptionBudgetList
```


```typescript
public getResource(groupVersionKind: policy/v1beta1/PodDisruptionBudgetList, namespace: string, name: string): PodDisruptionBudgetList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRole, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRole, namespace: string, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleBinding, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleBinding, namespace: string, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleBindingList, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleBindingList, namespace: string, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleList, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/ClusterRoleList, namespace: string, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/Role, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/Role, namespace: string, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleBinding, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleBinding, namespace: string, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleBindingList, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleBindingList, namespace: string, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleList, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1/RoleList, namespace: string, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRole, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRole, namespace: string, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleBinding, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleBinding, namespace: string, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleBindingList, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleBindingList, namespace: string, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleList, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/ClusterRoleList, namespace: string, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/Role, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/Role, namespace: string, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleBinding, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleBinding, namespace: string, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleBindingList, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleBindingList, namespace: string, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleList, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1alpha1/RoleList, namespace: string, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: rbac/v1alpha1/Subject, name: string): Subject
```


```typescript
public getResource(groupVersionKind: rbac/v1alpha1/Subject, namespace: string, name: string): Subject
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRole, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRole, namespace: string, name: string): ClusterRole
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleBinding, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleBinding, namespace: string, name: string): ClusterRoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleBindingList, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleBindingList, namespace: string, name: string): ClusterRoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleList, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/ClusterRoleList, namespace: string, name: string): ClusterRoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/Role, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/Role, namespace: string, name: string): Role
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleBinding, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleBinding, namespace: string, name: string): RoleBinding
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleBindingList, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleBindingList, namespace: string, name: string): RoleBindingList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleList, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: rbac.authorization.k8s.io/v1beta1/RoleList, namespace: string, name: string): RoleList
```


```typescript
public getResource(groupVersionKind: scheduling.k8s.io/v1alpha1/PriorityClass, name: string): PriorityClass
```


```typescript
public getResource(groupVersionKind: scheduling.k8s.io/v1alpha1/PriorityClass, namespace: string, name: string): PriorityClass
```


```typescript
public getResource(groupVersionKind: scheduling.k8s.io/v1alpha1/PriorityClassList, name: string): PriorityClassList
```


```typescript
public getResource(groupVersionKind: scheduling.k8s.io/v1alpha1/PriorityClassList, namespace: string, name: string): PriorityClassList
```


```typescript
public getResource(groupVersionKind: settings.k8s.io/v1alpha1/PodPreset, name: string): PodPreset
```


```typescript
public getResource(groupVersionKind: settings.k8s.io/v1alpha1/PodPreset, namespace: string, name: string): PodPreset
```


```typescript
public getResource(groupVersionKind: settings.k8s.io/v1alpha1/PodPresetList, name: string): PodPresetList
```


```typescript
public getResource(groupVersionKind: settings.k8s.io/v1alpha1/PodPresetList, namespace: string, name: string): PodPresetList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1/StorageClass, name: string): StorageClass
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1/StorageClass, namespace: string, name: string): StorageClass
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1/StorageClassList, name: string): StorageClassList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1/StorageClassList, namespace: string, name: string): StorageClassList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1alpha1/VolumeAttachment, name: string): VolumeAttachment
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1alpha1/VolumeAttachment, namespace: string, name: string): VolumeAttachment
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1alpha1/VolumeAttachmentList, name: string): VolumeAttachmentList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1alpha1/VolumeAttachmentList, namespace: string, name: string): VolumeAttachmentList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1beta1/StorageClass, name: string): StorageClass
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1beta1/StorageClass, namespace: string, name: string): StorageClass
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1beta1/StorageClassList, name: string): StorageClassList
```


```typescript
public getResource(groupVersionKind: storage.k8s.io/v1beta1/StorageClassList, namespace: string, name: string): StorageClassList
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L81">property resources</a>
</h3>

```typescript
resources: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="parse">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L30">function parse</a>
</h2>

```typescript
parse(config: ConfigGroupOpts, opts?: pulumi.CustomResourceOptions): { ... }
```

<h2 class="pdoc-module-header" id="parseYamlDocument">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L465">function parseYamlDocument</a>
</h2>

```typescript
parseYamlDocument(config: ConfigOpts, opts?: pulumi.CustomResourceOptions): { ... }
```

<h2 class="pdoc-module-header" id="parseYamlObject">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L480">function parseYamlObject</a>
</h2>

```typescript
parseYamlObject(obj: any, transformations?: { ... }[], opts?: pulumi.CustomResourceOptions): { ... }[]
```

<h2 class="pdoc-module-header" id="ConfigFileOpts">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L20">interface ConfigFileOpts</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L21">property file</a>
</h3>

```typescript
file?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L22">property transformations</a>
</h3>

```typescript
transformations?: { ... }[];
```

<h2 class="pdoc-module-header" id="ConfigGroupOpts">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L13">interface ConfigGroupOpts</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L14">property files</a>
</h3>

```typescript
files?: string[] | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L16">property objs</a>
</h3>

```typescript
objs?: any[] | any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L17">property transformations</a>
</h3>

```typescript
transformations?: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L15">property yaml</a>
</h3>

```typescript
yaml?: string[] | string;
```

<h2 class="pdoc-module-header" id="ConfigOpts">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L25">interface ConfigOpts</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L26">property objs</a>
</h3>

```typescript
objs: any[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L27">property transformations</a>
</h3>

```typescript
transformations?: { ... }[];
```

