---
title: Deploy Cluster Services
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-cluster-svcs
    weight: 7
---

{{< cloudchoose >}}

Cluster services are general services scoped at the Kubernetes cluster level.
These services tend to include logging and monitoring at a minimum for the
whole cluster, or a subset of apps and workloads. It could also include
policy enforcement and service meshes.

## Overview

We'll explore how to setup:

  * [Logging](#logging)
  * [Monitoring](#monitoring)

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

The full code for this stack is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/aws/04-cluster-services
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

The full code for this stack is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/azure/04-cluster-services

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

The full code for this stack is on [GitHub][gh-repo-stack].
[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/gcp/04-cluster-services

{{% /md %}}
</div>

## Logging

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

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

[crosswalk-control-plane]: {{< relref "/docs/guides/crosswalk/kubernetes/control-plane" >}}
[crosswalk-control-plane-recommended]: {{< relref "/docs/guides/crosswalk/kubernetes/control-plane#recommended-settings" >}}
[crosswalk-k8s-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/identity#create-iam-roles-for-eks-node-groups" >}}
[aws-cw-console]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingSetup.html#ConsoleSignIn
[aws-cw-logs]: https://aws.amazon.com/cloudwatch/features/

{{< k8s-language nokx >}}

<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}

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

[crosswalk-control-plane]: {{< relref "/docs/guides/crosswalk/kubernetes/control-plane" >}}
[k8s-ds]: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
[k8s-logs-samples]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-logs.html
[aws-cw-console]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingSetup.html#ConsoleSignIn
[crosswalk-k8s-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/identity#create-iam-roles-for-eks-node-groups" >}}
[aws-cw-logs]: https://aws.amazon.com/cloudwatch/features/
{{% /md %}}
</div>

<div class="k8s-language-prologue-pulumi-k8s"></div>
<div class="mt">
{{% md %}}

Using the [Helm chart][fluentd-helm], we can provision `fluentd-cloudwatch`
in Pulumi to run as a [DaemonSet][k8s-ds] and send worker and app logs to [CloudWatch
Logs][aws-cw-logs].

#### Install fluentd

Deploy the Chart into the `cluster-svcs` namespace created in [Configure
Cluster Defaults][crosswalk-k8s-defaults] .

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create a new provider to the cluster using the cluster's kubeconfig.
const eksProvider = new k8s.Provider("eksProvider", {kubeconfig: config.kubeconfig.apply(JSON.stringify)});

// Create a new CloudWatch Log group for fluentd-cloudwatch.
const fluentdCloudWatchLogGroup = new aws.cloudwatch.LogGroup(name);
export let fluentdCloudWatchLogGroupName = fluentdCloudWatchLogGroup.name;

// Deploy fluentd-cloudwatch using the Helm chart.
const fluentdCloudwatch = new k8s.helm.v2.Chart(name,
    {
        namespace: config.clusterSvcsNamespaceName,
        chart: "fluentd-cloudwatch",
        version: "0.11.0",
        fetchOpts: {
            repo: "https://kubernetes-charts-incubator.storage.googleapis.com/",
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
    {providers: { kubernetes: eksProvider }},
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

[crosswalk-k8s-identity]: {{< relref "/docs/guides/crosswalk/kubernetes/identity#create-iam-roles-for-eks-node-groups" >}}
[aws-cw-console]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingSetup.html#ConsoleSignIn
[crosswalk-k8s-defaults]: {{< relref "/docs/guides/crosswalk/kubernetes/configure-defaults#namespaces" >}}
[aws-cw-logs]: https://aws.amazon.com/cloudwatch/features/
[k8s-ds]: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
[fluentd-helm]: https://github.com/helm/charts/tree/master/incubator/fluentd-cloudwatch
{{% /md %}}
</div>

See the [official AWS docs][k8s-logs-docs] for more details.

Note, CloudWatch is rate limited and often times the size of the
data being sent can cause `fluentd-cloudwatch` to experience
`ThrottlingException error="Rate exceeded"`. This can cause a delay in logs
showing up in CloudWatch. Request a limit increase, or alter
the data being sent. See the [CloudWatch limits][aws-cw-limits] for more details.

[k8s-logs-docs]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html
[aws-cw-limits]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_limits.html
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

{{< k8s-language nokx >}}

<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}
AZURE YAML TODO
{{% /md %}}
</div>

<div class="k8s-language-prologue-pulumi-k8s"></div>
<div class="mt">
{{% md %}}
AZURE pulumi-k8s TODO
{{% /md %}}
</div>

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

{{< k8s-language nokx >}}

<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}
GCP YAML TODO
{{% /md %}}
</div>

<div class="k8s-language-prologue-pulumi-k8s"></div>
<div class="mt">
{{% md %}}
GCP pulumi-k8s TODO
{{% /md %}}
</div>

{{% /md %}}
</div>

## Monitoring

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

Using the YAML manifests in the [AWS samples][aws-metrics-samples], we can provision the CloudWatch Agent
to run as a [DaemonSet][k8s-ds] and send metrics to [CloudWatch][aws-cw].

[aws-cw]: https://aws.amazon.com/cloudwatch
[k8s-ds]: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
[aws-metrics-samples]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-metrics.html

{{< k8s-language yaml-only >}}

#### Install CloudWatch Agent

<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}

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

[crosswalk-control-plane]: {{< relref "/docs/guides/crosswalk/kubernetes/control-plane" >}}
[aws-cw-console]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingSetup.html#ConsoleSignIn

{{% /md %}}
</div>

{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

{{< k8s-language nokx >}}

<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}
AZURE YAML TODO
{{% /md %}}
</div>

<div class="k8s-language-prologue-pulumi-k8s"></div>
<div class="mt">
{{% md %}}
AZURE pulumi-k8s TODO
{{% /md %}}
</div>

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

{{< k8s-language nokx >}}

<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}
GCP YAML TODO
{{% /md %}}
</div>

<div class="k8s-language-prologue-pulumi-k8s"></div>
<div class="mt">
{{% md %}}
GCP pulumi-k8s TODO
{{% /md %}}
</div>

{{% /md %}}
</div>
