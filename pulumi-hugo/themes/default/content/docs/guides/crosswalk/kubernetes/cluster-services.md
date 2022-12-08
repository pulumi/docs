---
title_tag: Deploying Kubernetes Cluster Services | Crosswalk
title: Deploying Kubernetes Cluster Services
meta_desc: This page will provide an overview on how to deploy Kubernetes Cluster Services.
no_on_this_page: true
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-cluster-svcs
    weight: 7
---

{{< chooser cloud "aws,azure,gcp" / >}}

Cluster services are general services scoped at the Kubernetes cluster level.
These services tend to include logging and monitoring at a minimum for the
whole cluster, or a subset of apps and workloads. It could also include
policy enforcement and service meshes.

{{% choosable cloud aws %}}

The full code for the AWS cluster services is on [GitHub][gh-repo-stack].

<!-- markdownlint-disable url -->
[gh-repo-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/aws/04-cluster-services
<!-- markdownlint-enable url -->

{{% /choosable %}}

{{% choosable cloud azure %}}

The full code for the Azure cluster services is on [GitHub][gh-repo-stack].

<!-- markdownlint-disable url -->
[gh-repo-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/azure/04-cluster-services
<!-- markdownlint-enable url -->

{{% /choosable %}}

{{% choosable cloud gcp %}}

GKE logging and monitoring is managed by GCP through StackDriver.

The repo for the GCP cluster services is on [GitHub][gh-repo-stack], but it is empty since no extra steps are required after cluster and Node Pool creation in the [Cluster Configuration][crosswalk-k8s-cluster] stack.

<!-- markdownlint-disable url -->
[crosswalk-k8s-cluster]: https://github.com/pulumi/kubernetes-guides/tree/master/gcp/03-cluster-configuration
[gh-repo-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/gcp/04-cluster-services
<!-- markdownlint-enable url -->

{{% /choosable %}}

The full code for the general cluster services is on [GitHub][gh-repo-stack].

<!-- markdownlint-disable url -->
[gh-repo-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/general-cluster-services
<!-- markdownlint-enable url -->

{{% choosable cloud aws %}}

## Overview

We'll explore how to setup:

* [AWS Logging](#aws-logging)
* [AWS Monitoring](#aws-monitoring)
* [Datadog](#datadog)

See the [official AWS docs][k8s-logs-docs] for more details.

## Prerequisites

Authenticate as the `admins` role from the [Identity][aws-admin-identity-stack] stack.

```bash
$ aws sts assume-role --role-arn `pulumi stack output adminsIamRoleArn` --role-session-name k8s-admin
$ export KUBECONFIG=`pwd`/kubeconfig-admin.json
```

[aws-admin-identity-stack]: /docs/guides/crosswalk/kubernetes/identity/#create-an-iam-role-for-admins

## AWS Logging

### Control Plane

In the [Recommended Settings][crosswalk-control-plane-recommended] of
Creating the Control Plane, we enabled cluster logging for the various
controllers of the control plane.

To view these logs, go to the [CloudWatch console][aws-cw-console],
navigate to the logs in your region, and look for the following group.

```
/aws/eks/Cluster_Name/cluster
```

The cluster name can be retrieved from the [cluster stack][crosswalk-control-plane] output.

```bash
$ pulumi stack output clusterName
```

### Worker Nodes and Pods

#### Configure Worker Node IAM Policy

To work with [Cloudwatch Logs][aws-cw-logs], the identities created in
[Identity][crosswalk-k8s-identity] for each worker node group must have the
proper permissions in IAM.

Attach the permissions to the IAM role for each nodegroup.

```typescript
import * as aws from "@pulumi/aws";

// Parse out the role names e.g. `roleName-123456` from `arn:aws:iam::123456789012:role/roleName-123456`
const stdNodegroupIamRoleName = config.stdNodegroupIamRoleArn.apply(s => s.split("/")).apply(s => s[1])
const perfNodegroupIamRoleName = config.perfNodegroupIamRoleArn.apply(s => s.split("/")).apply(s => s[1])

// Create a new IAM Policy for fluentd-cloudwatch to manage CloudWatch Logs.
const name = "fluentd-cloudwatch";
const fluentdCloudWatchPolicy = new aws.iam.Policy(name,
    {
        description: "Allows fluentd-cloudwatch to work with CloudWatch Logs.",
        policy: JSON.stringify(
            {
                Version: "2012-10-17",
                Statement: [{Effect: "Allow", Action: ["logs:*"], Resource: ["arn:aws:logs:*:*:*"]}]
            }
        )
    },
);

// Attach CloudWatch Logs policies to a role.
function attachLogPolicies(name: string, arn: pulumi.Input<aws.ARN>) {
    new aws.iam.RolePolicyAttachment(name,
        { policyArn: fluentdCloudWatchPolicy.arn, role: arn},
    );
}

attachLogPolicies("stdRpa", stdNodegroupIamRoleName);
attachLogPolicies("perfRpa", perfNodegroupIamRoleName);
```

<!-- markdownlint-disable url -->
[crosswalk-control-plane]: /docs/guides/crosswalk/kubernetes/control-plane/
[crosswalk-control-plane-recommended]: /docs/guides/crosswalk/kubernetes/control-plane/#recommended-settings
[crosswalk-k8s-identity]: /docs/guides/crosswalk/kubernetes/identity/#create-iam-roles-for-eks-node-groups
[aws-cw-console]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingSetup.html#ConsoleSignIn
[aws-cw-logs]: https://aws.amazon.com/cloudwatch/features/
<!-- markdownlint-enable url -->

{{< chooser k8s-language "typescript,yaml" / >}}

{{< choosable k8s-language yaml >}}

Using the YAML manifests in the [AWS samples][k8s-logs-samples], we can provision `fluentd-cloudwatch`
to run as a [DaemonSet][k8s-ds] and send worker and app logs to [CloudWatch
Logs][aws-cw-logs].

#### Install fluentd

Create a Namespace.

```bash
$ kubectl apply -f https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/master/k8s-yaml-templates/cloudwatch-namespace.yaml
```

Create a ConfigMap.

```bash
$ kubectl create configmap cluster-info --from-literal=cluster.name=`pulumi stack output clusterName` --from-literal=logs.region=`pulumi stack output region` -n amazon-cloudwatch
```

Deploy the DaemonSet.

```bash
$ kubectl apply -f https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/master/k8s-yaml-templates/fluentd/fluentd.yaml
```

Validate the deployment.

```bash
$ kubectl get pods -n amazon-cloudwatch
```

Verify the fluentd setup in the [CloudWatch console][aws-cw-console] by
navigating to the logs in your region, and looking for the following groups.

```
/aws/containerinsights/Cluster_Name/application
/aws/containerinsights/Cluster_Name/host
/aws/containerinsights/Cluster_Name/dataplane
```

The cluster name can be retrieved from the [cluster stack][crosswalk-control-plane] output.

```bash
$ pulumi stack output clusterName
```

Clean Up.

```bash
$ kubectl delete ns amazon-cloudwatch
```

<!-- markdownlint-disable url -->
[crosswalk-control-plane]: /docs/guides/crosswalk/kubernetes/control-plane/
[k8s-ds]: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
[k8s-logs-samples]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-logs.html
[aws-cw-console]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingSetup.html#ConsoleSignIn
[crosswalk-k8s-identity]: /docs/guides/crosswalk/kubernetes/identity/#create-iam-roles-for-eks-node-groups
[aws-cw-logs]: https://aws.amazon.com/cloudwatch/features/
<!-- markdownlint-enable url -->

{{< /choosable >}}

{{< choosable k8s-language typescript >}}

Using the [Helm chart][fluentd-helm], we can provision `fluentd-cloudwatch`
in Pulumi to run as a [DaemonSet][k8s-ds] and send worker and app logs to [CloudWatch
Logs][aws-cw-logs].

#### Install fluentd

Deploy the Chart into the `cluster-svcs` namespace created in [Configure
Cluster Defaults][crosswalk-k8s-defaults] .

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create a new provider to the cluster using the cluster's kubeconfig.
const provider = new k8s.Provider("provider", {kubeconfig: config.kubeconfig});

// Create a new CloudWatch Log group for fluentd-cloudwatch.
const fluentdCloudWatchLogGroup = new aws.cloudwatch.LogGroup(name);
export let fluentdCloudWatchLogGroupName = fluentdCloudWatchLogGroup.name;

// Deploy fluentd-cloudwatch using the Helm chart.
const fluentdCloudwatch = new k8s.helm.v3.Chart(name,
    {
        namespace: config.clusterSvcsNamespaceName,
        chart: "fluentd-cloudwatch",
        version: "0.11.0",
        fetchOpts: {
            repo: "https://charts.helm.sh/incubator",
        },
        values: {
            extraVars: [ "{ name: FLUENT_UID, value: '0' }" ],
            rbac: {create: true},
            awsRegion: aws.config.region,
            logGroupName: fluentdCloudWatchLogGroup.name,
        },
        transformations: [
            (obj: any) => {
                // Do transformations on the YAML to set the namespace
                if (obj.metadata) {
                    obj.metadata.namespace = config.clusterSvcsNamespaceName;
                }
            },
        ],
    },
    {providers: { kubernetes: provider }},
);
```

Validate the deployment.

```bash
$ kubectl get pods -n `pulumi stack output clusterSvcsNamespaceName`
```

Verify the fluentd setup in the [CloudWatch console][aws-cw-console] by
navigating to the logs in your region, and looking for the following group.

```bash
$ pulumi stack output fluentdCloudWatchLogGroupName
```

<!-- markdownlint-disable url -->
[crosswalk-k8s-identity]: /docs/guides/crosswalk/kubernetes/identity/#create-iam-roles-for-eks-node-groups
[aws-cw-console]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingSetup.html#ConsoleSignIn
[crosswalk-k8s-defaults]: /docs/guides/crosswalk/kubernetes/configure-defaults/#namespaces
[aws-cw-logs]: https://aws.amazon.com/cloudwatch/features/
[k8s-ds]: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
[fluentd-helm]: https://github.com/helm/charts/tree/master/incubator/fluentd-cloudwatch
<!-- markdownlint-enable url -->

{{< /choosable >}}

> Note: CloudWatch is rate limited and often times the size of the
data being sent can cause `ThrottlingException error="Rate exceeded"`. This can cause a delay in logs showing up in CloudWatch. Request a limit increase, or alter
the data being sent, if necessary.  See the [CloudWatch limits][aws-cw-limits] for more details.

<!-- markdownlint-disable url -->
[k8s-logs-docs]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html
[aws-cw-limits]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_limits.html
<!-- markdownlint-enable url -->

{{% /choosable %}}

{{% choosable cloud azure %}}

## Overview

We'll explore how to setup:

* [Azure Logging and Monitoring](#azure-logging-and-monitoring)
* [Datadog](#datadog)

See the official [Azure Monitor][azure-monitor-overview] and [AKS][aks-logs] docs for more details.

## Azure Logging and Monitoring

AKS monitoring is managed by Azure through [Log Analytics][azure-la].

Once enabled, in the Azure portal visit the cluster's Kubernetes service details,
and [analyze its Azure Monitor][azure-monitor-analyze] information in the Monitoring section's: Insights, Logs, and Metrics.

### Enable Azure Monitor for the Cluster

Enable the Log Analytics agent on the AKS cluster in the
[Cluster Configuration][crosswalk-k8s-cluster] stack.

```ts
import * as azure from "@pulumi/azure";

// Create the AKS cluster with LogAnalytics enabled in the given workspace.
const cluster = new azure.containerservice.KubernetesCluster(`${name}`, {
    ...
    resourceGroupName: config.resourceGroupName,
    addonProfile: {
        omsAgent: {
            enabled: true,
            logAnalyticsWorkspaceId: config.logAnalyticsWorkspaceId,
        },
    },
});
```

Enable logging for the control plane, and monitoring of all metrics in the
[Cluster Services][crosswalk-aks-cluster-svcs] stack.

```ts
import * as azure from "@pulumi/azure";

// Enable the Monitoring Diagonostic control plane component logs and AllMetrics
const azMonitoringDiagnostic = new azure.monitoring.DiagnosticSetting(name, {
    logAnalyticsWorkspaceId: config.logAnalyticsWorkspaceId,
    targetResourceId: config.clusterId,
    logs: ["kube-apiserver", "kube-controller-manager", "kube-scheduler", "kube-audit", "cluster-autoscaler"]
        .map(category => ({
            category,
            enabled : true,
            retentionPolicy: { enabled: true },
        })),
    metrics: [{
        category: "AllMetrics",
        retentionPolicy: { enabled: true },
    }],
});

```

### Worker Nodes

To get the Worker kubelet logs you need to SSH into the nodes.

Use the node admin username and SSH key used in the
[Cluster Configuration][crosswalk-k8s-cluster] stack.

```ts
import * as azure from "@pulumi/azure";

// Create the AKS cluster with LogAnalytics enabled in the given workspace.
const cluster = new azure.containerservice.KubernetesCluster(`${name}`, {
    ...
    resourceGroupName: config.resourceGroupName,
    linuxProfile: {
        adminUsername: "aksuser",
        sshKey: {
            keyData: sshPublicKey,
        },
    },
});
```

See the official [AKS docs][aks-kubelet-logs] for more details.

<!-- markdownlint-disable url -->
[azure-monitor-analyze]: https://docs.microsoft.com/en-us/azure/azure-monitor/insights/container-insights-analyze
[azure-la]: https://docs.microsoft.com/en-us/azure/azure-monitor/log-query/get-started-portal
[aks-kubelet-logs]: https://docs.microsoft.com/en-us/azure/aks/kubelet-logs
[azure-monitor-overview]: https://docs.microsoft.com/en-us/azure/azure-monitor/insights/container-insights-overview
[aks-logs]: https://docs.microsoft.com/en-us/azure/aks/view-master-logs
[crosswalk-k8s-cluster]: https://github.com/pulumi/kubernetes-guides/tree/master/azure/03-cluster-configuration
[crosswalk-aks-cluster-svcs]: https://github.com/pulumi/kubernetes-guides/tree/master/azure/04-cluster-services
<!-- markdownlint-enable url -->

{{% /choosable %}}

{{% choosable cloud gcp %}}

## Overview

We'll explore how to setup:

* [GCP Logging and Monitoring](#azure-logging-and-monitoring)
* [Datadog](#datadog)

See the official [GKE][gke-logs] and [StackDriver Observing][gke-sd-observe] docs for more details.

## GCP Logging and Monitoring

GKE monitoring is managed by GCP through [StackDriver][gke-sd].

Stackdriver Kubernetes Engine Monitoring is the default logging option for GKE
clusters, and it comes automatically enabled for all clusters starting with version 1.14.

### Enable the Node Pool

Enable the cluster's Node Pool with the proper logging and monitoring
permission in the [Cluster Configuration][crosswalk-k8s-cluster] stack.

```ts
import * as gcp from "@pulumi/gcp";

// Create a GKE cluster.
// Versions >= 1.14 have Stackdriver Monitoring enabled by default.
const cluster = new gcp.container.Cluster(`${name}`, {
    ...
    minMasterVersion: "1.14.7-gke.17",
}

// Create the GKE Node Pool with OAuth scopes enabled for logging and monitoring.
const standardNodes = new gcp.container.NodePool("standard-nodes", {
    ...
    cluster: cluster.name,
    version: "1.14.7-gke.17",
    nodeConfig: {
        machineType: "n1-standard-1",
        oauthScopes: [
            "https://www.googleapis.com/auth/compute",
            "https://www.googleapis.com/auth/devstorage.read_only",
            "https://www.googleapis.com/auth/logging.write",
            "https://www.googleapis.com/auth/monitoring",
        ],
    },
});
```

<!-- markdownlint-disable url -->
[gke-sd]: https://app.google.stackdriver.com/
[gke-logs]: https://cloud.google.com/monitoring/kubernetes-engine/
[gke-sd-observe]: https://cloud.google.com/monitoring/kubernetes-engine/observing
[crosswalk-k8s-cluster]: https://github.com/pulumi/kubernetes-guides/tree/master/gcp/03-cluster-configuration
<!-- markdownlint-enable url -->

{{% /choosable %}}

{{% choosable cloud aws %}}

## AWS Monitoring

Using the YAML manifests in the [AWS samples][aws-metrics-samples], we can provision the CloudWatch Agent
to run as a [DaemonSet][k8s-ds] and send metrics to [CloudWatch][aws-cw].

<!-- markdownlint-disable url -->
[aws-cw]: https://aws.amazon.com/cloudwatch
[k8s-ds]: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
[aws-metrics-samples]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-metrics.html
<!-- markdownlint-enable url -->

### Install CloudWatch Agent

Create a Namespace.

```bash
$ kubectl apply -f https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/master/k8s-yaml-templates/cloudwatch-namespace.yaml

```

Create a ServiceAccount.

```bash
$ kubectl apply -f https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/master/k8s-yaml-templates/cwagent-kubernetes-monitoring/cwagent-serviceaccount.yaml
```

Create a ConfigMap.

```bash
$ curl -s https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/master/k8s-yaml-templates/cwagent-kubernetes-monitoring/cwagent-configmap.yaml | sed -e "s#{{cluster_name}}#`pulumi stack output clusterName`#g" | kubectl apply -f -
```

Deploy the DaemonSet.

```bash
$ kubectl apply -f https://raw.githubusercontent.com/aws-samples/amazon-cloudwatch-container-insights/master/k8s-yaml-templates/cwagent-kubernetes-monitoring/cwagent-daemonset.yaml
```

Validate the deployment.

```bash
$ kubectl get pods -n amazon-cloudwatch
```

Verify the metrics setup in the [CloudWatch console][aws-cw-console] by
navigating to Logs in your region, and looking for the following group.

```
/aws/containerinsights/Cluster_Name/performance
```

The cluster name can be retrieved from the [cluster stack][crosswalk-control-plane] output.

```bash
$ pulumi stack output clusterName
```

You can also examine the stats in the [CloudWatch console][aws-cw-console] by
navigating to Metrics in your region, and looking for the ContainerInsights for
your cluster by its name.

Clean Up.

```bash
$ kubectl delete ns amazon-cloudwatch
```

[crosswalk-control-plane]: /docs/guides/crosswalk/kubernetes/control-plane/

<!-- markdownlint-disable url -->
[aws-cw-console]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingSetup.html#ConsoleSignIn
<!-- markdownlint-enable url -->

{{% /choosable %}}

## Datadog

Deploy [Datadog][k8s-datadog] as a DaemonSet to aggregate Kubernetes, node, and container metrics and events, in addition to provider managed logging and monitoring.

The full code for this app stack is on [GitHub][gh-dd-stack].

<!-- markdownlint-disable url -->
[gh-dd-stack]: https://github.com/pulumi/kubernetes-guides/tree/master/general-cluster-services/datadog-daemonset
<!-- markdownlint-enable url -->

```ts
import * as k8s from "@pulumi/kubernetes";

const appName = "datadog";
const appLabels = { app: appName };

// Create a DataDog DaemonSet.
const datadog = new k8s.apps.v1.DaemonSet(appName, {
    metadata: { labels: appLabels},
    spec: {
        selector: {
            matchLabels: appLabels,
        },
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [
                    {
                        image: "datadog/agent:latest",
                        name: "nginx",
                        resources: {limits: {memory: "512Mi"}, requests: {memory: "512Mi"}},
                        env: [
                            {
                                name: "DD_KUBERNETES_KUBELET_HOST",
                                valueFrom: {
                                    fieldRef: {
                                        fieldPath: "status.hostIP",
                                    },
                                },
                            },
                            {
                                name: "DD_API_KEY",
                                valueFrom: {
                                    configMapKeyRef: {
                                        name: ddConfigMap.metadata.name,
                                        key: "DD_API_KEY",
                                    },
                                },
                            },
                            {
                                name: "DD_PROCESS_AGENT_ENABLED",
                                valueFrom: {
                                    configMapKeyRef: {
                                        name: ddConfigMap.metadata.name,
                                        key: "DD_PROCESS_AGENT_ENABLED",
                                    },
                                },
                            },
                            {
                                name: "DD_LOGS_CONFIG_CONTAINER_COLLECT_ALL",
                                valueFrom: {
                                    configMapKeyRef: {
                                        name: ddConfigMap.metadata.name,
                                        key: "DD_LOGS_CONFIG_CONTAINER_COLLECT_ALL",
                                    },
                                },
                            },
                            {
                                name: "DD_COLLECT_KUBERNETES_EVENTS",
                                valueFrom: {
                                    configMapKeyRef: {
                                        name: ddConfigMap.metadata.name,
                                        key: "DD_COLLECT_KUBERNETES_EVENTS",
                                    },
                                },
                            },
                            ...
                        ],
                        volumeMounts: [
                            {name: "dockersocket", mountPath: "/var/run/docker.sock"},
                            {name: "proc", mountPath: "/host/proc"},
                            {name: "cgroup", mountPath: "/host/sys/fs/cgroup"},
                        ],
                    },
                ],
                volumes: [
                    {name: "dockersocket", hostPath: {path: "/var/run/docker.sock"}},
                    {name: "proc", hostPath: {path: "/proc"}},
                    {name: "cgroup", hostPath: {path: "/sys/fs/cgroup"}},
                ],
            },
        },
    },
}, { provider: provider });
```

[k8s-datadog]: https://docs.datadoghq.com/integrations/kubernetes/
