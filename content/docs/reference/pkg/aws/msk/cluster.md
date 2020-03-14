
---
title: "Cluster"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Manages AWS Managed Streaming for Kafka cluster

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const kms = new aws.kms.Key("kms", {
    description: "example",
});
const vpc = new aws.ec2.Vpc("vpc", {
    cidrBlock: "192.168.0.0/22",
});
const sg = new aws.ec2.SecurityGroup("sg", {
    vpcId: vpc.id,
});
const azs = aws.getAvailabilityZones({
    state: "available",
});
const subnetAz1 = new aws.ec2.Subnet("subnet_az1", {
    availabilityZone: azs.names[0],
    cidrBlock: "192.168.0.0/24",
    vpcId: vpc.id,
});
const subnetAz2 = new aws.ec2.Subnet("subnet_az2", {
    availabilityZone: azs.names[1],
    cidrBlock: "192.168.1.0/24",
    vpcId: vpc.id,
});
const subnetAz3 = new aws.ec2.Subnet("subnet_az3", {
    availabilityZone: azs.names[2],
    cidrBlock: "192.168.2.0/24",
    vpcId: vpc.id,
});
const example = new aws.msk.Cluster("example", {
    brokerNodeGroupInfo: {
        clientSubnets: [
            subnetAz1.id,
            subnetAz2.id,
            subnetAz3.id,
        ],
        ebsVolumeSize: 1000,
        instanceType: "kafka.m5.large",
        securityGroups: [sg.id],
    },
    clusterName: "example",
    encryptionInfo: {
        encryptionAtRestKmsKeyArn: kms.arn,
    },
    kafkaVersion: "2.1.0",
    numberOfBrokerNodes: 3,
    openMonitoring: {
        prometheus: {
            jmxExporter: {
                enabledInBroker: true,
            },
            nodeExporter: {
                enabledInBroker: true,
            },
        },
    },
    tags: {
        foo: "bar",
    },
});

export const bootstrapBrokers = example.bootstrapBrokers;
export const bootstrapBrokersTls = example.bootstrapBrokersTls;
export const zookeeperConnectString = example.zookeeperConnectString;
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/msk_cluster.html.markdown.



## Create a Cluster Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/msk/#Cluster">Cluster</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/msk/#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Cluster</span><span class="p">(resource_name, opts=None, </span>broker_node_group_info=None<span class="p">, </span>client_authentication=None<span class="p">, </span>cluster_name=None<span class="p">, </span>configuration_info=None<span class="p">, </span>encryption_info=None<span class="p">, </span>enhanced_monitoring=None<span class="p">, </span>kafka_version=None<span class="p">, </span>number_of_broker_nodes=None<span class="p">, </span>open_monitoring=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#Cluster">Cluster</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.Cluster.html">Cluster</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterArgs.html">ClusterArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Cluster resource with the given unique name, arguments, and options.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Broker<wbr>Node<wbr>Group<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterbrokernodegroupinfo">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Broker<wbr>Node<wbr>Group<wbr>Info<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block for the broker nodes of the Kafka cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Authentication</td>
            <td class="align-top">
                
                <code><a href="#clusterclientauthentication">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Client<wbr>Authentication<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying a client authentication. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the MSK cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterconfigurationinfo">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Configuration<wbr>Info<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterencryptioninfo">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Encryption<wbr>Info<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying encryption. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enhanced<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the desired enhanced MSK CloudWatch monitoring level.  See [Monitoring Amazon MSK with Amazon CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kafka<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specify the desired Kafka software version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Number<wbr>Of<wbr>Broker<wbr>Nodes</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Open<wbr>Monitoring</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoring">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Open<wbr>Monitoring<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for JMX and Node monitoring for the MSK cluster. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Broker<wbr>Node<wbr>Group<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterbrokernodegroupinfo">msk.<wbr>Cluster<wbr>Broker<wbr>Node<wbr>Group<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block for the broker nodes of the Kafka cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Authentication</td>
            <td class="align-top">
                
                <code><a href="#clusterclientauthentication">*msk.<wbr>Cluster<wbr>Client<wbr>Authentication</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying a client authentication. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the MSK cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterconfigurationinfo">*msk.<wbr>Cluster<wbr>Configuration<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterencryptioninfo">*msk.<wbr>Cluster<wbr>Encryption<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying encryption. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enhanced<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the desired enhanced MSK CloudWatch monitoring level.  See [Monitoring Amazon MSK with Amazon CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kafka<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specify the desired Kafka software version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Number<wbr>Of<wbr>Broker<wbr>Nodes</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Open<wbr>Monitoring</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoring">*msk.<wbr>Cluster<wbr>Open<wbr>Monitoring</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for JMX and Node monitoring for the MSK cluster. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">broker<wbr>Node<wbr>Group<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterbrokernodegroupinfo">msk.<wbr>Cluster<wbr>Broker<wbr>Node<wbr>Group<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block for the broker nodes of the Kafka cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client<wbr>Authentication</td>
            <td class="align-top">
                
                <code><a href="#clusterclientauthentication">msk.<wbr>Cluster<wbr>Client<wbr>Authentication?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying a client authentication. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the MSK cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterconfigurationinfo">msk.<wbr>Cluster<wbr>Configuration<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterencryptioninfo">msk.<wbr>Cluster<wbr>Encryption<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying encryption. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enhanced<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the desired enhanced MSK CloudWatch monitoring level.  See [Monitoring Amazon MSK with Amazon CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kafka<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specify the desired Kafka software version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">number<wbr>Of<wbr>Broker<wbr>Nodes</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">open<wbr>Monitoring</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoring">msk.<wbr>Cluster<wbr>Open<wbr>Monitoring?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for JMX and Node monitoring for the MSK cluster. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">broker_<wbr>node_<wbr>group_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#clusterbrokernodegroupinfo">dict{cluster_<wbr>broker_<wbr>node_<wbr>group_<wbr>info}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block for the broker nodes of the Kafka cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client_<wbr>authentication</td>
            <td class="align-top">
                
                <code><a href="#clusterclientauthentication">dict{cluster_<wbr>client_<wbr>authentication}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying a client authentication. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the MSK cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#clusterconfigurationinfo">dict{cluster_<wbr>configuration_<wbr>info}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#clusterencryptioninfo">dict{cluster_<wbr>encryption_<wbr>info}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying encryption. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enhanced_<wbr>monitoring</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the desired enhanced MSK CloudWatch monitoring level.  See [Monitoring Amazon MSK with Amazon CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kafka_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specify the desired Kafka software version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">number_<wbr>of_<wbr>broker_<wbr>nodes</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">open_<wbr>monitoring</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoring">dict{cluster_<wbr>open_<wbr>monitoring}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for JMX and Node monitoring for the MSK cluster. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Cluster Output Properties

The following output properties are available:



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bootstrap<wbr>Brokers</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A comma separated list of one or more hostname:port pairs of kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if `client_broker` encryption in transit is set to `PLAINTEXT` or `TLS_PLAINTEXT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bootstrap<wbr>Brokers<wbr>Tls</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if `client_broker` encryption in transit is set to `TLS_PLAINTEXT` or `TLS`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Broker<wbr>Node<wbr>Group<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterbrokernodegroupinfo">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Broker<wbr>Node<wbr>Group<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for the broker nodes of the Kafka cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Authentication</td>
            <td class="align-top">
                
                <code><a href="#clusterclientauthentication">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Client<wbr>Authentication?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for specifying a client authentication. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the MSK cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterconfigurationinfo">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Configuration<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Current<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Current version of the MSK Cluster used for updates, e.g. `K13V1IB3VIYZZH`
* `encryption_info.0.encryption_at_rest_kms_key_arn` - The ARN of the KMS key used for encryption at rest of the broker data volumes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterencryptioninfo">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Encryption<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for specifying encryption. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enhanced<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Specify the desired enhanced MSK CloudWatch monitoring level.  See [Monitoring Amazon MSK with Amazon CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kafka<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specify the desired Kafka software version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Number<wbr>Of<wbr>Broker<wbr>Nodes</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Open<wbr>Monitoring</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoring">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Open<wbr>Monitoring?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for JMX and Node monitoring for the MSK cluster. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zookeeper<wbr>Connect<wbr>String</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A comma separated list of one or more hostname:port pairs to use to connect to the Apache Zookeeper cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bootstrap<wbr>Brokers</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A comma separated list of one or more hostname:port pairs of kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if `client_broker` encryption in transit is set to `PLAINTEXT` or `TLS_PLAINTEXT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bootstrap<wbr>Brokers<wbr>Tls</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if `client_broker` encryption in transit is set to `TLS_PLAINTEXT` or `TLS`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Broker<wbr>Node<wbr>Group<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterbrokernodegroupinfo">msk.<wbr>Cluster<wbr>Broker<wbr>Node<wbr>Group<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for the broker nodes of the Kafka cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Authentication</td>
            <td class="align-top">
                
                <code><a href="#clusterclientauthentication">*msk.<wbr>Cluster<wbr>Client<wbr>Authentication</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for specifying a client authentication. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the MSK cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterconfigurationinfo">*msk.<wbr>Cluster<wbr>Configuration<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Current<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Current version of the MSK Cluster used for updates, e.g. `K13V1IB3VIYZZH`
* `encryption_info.0.encryption_at_rest_kms_key_arn` - The ARN of the KMS key used for encryption at rest of the broker data volumes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterencryptioninfo">*msk.<wbr>Cluster<wbr>Encryption<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for specifying encryption. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enhanced<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Specify the desired enhanced MSK CloudWatch monitoring level.  See [Monitoring Amazon MSK with Amazon CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kafka<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specify the desired Kafka software version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Number<wbr>Of<wbr>Broker<wbr>Nodes</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Open<wbr>Monitoring</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoring">*msk.<wbr>Cluster<wbr>Open<wbr>Monitoring</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for JMX and Node monitoring for the MSK cluster. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zookeeper<wbr>Connect<wbr>String</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A comma separated list of one or more hostname:port pairs to use to connect to the Apache Zookeeper cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bootstrap<wbr>Brokers</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A comma separated list of one or more hostname:port pairs of kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if `client_broker` encryption in transit is set to `PLAINTEXT` or `TLS_PLAINTEXT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bootstrap<wbr>Brokers<wbr>Tls</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if `client_broker` encryption in transit is set to `TLS_PLAINTEXT` or `TLS`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">broker<wbr>Node<wbr>Group<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterbrokernodegroupinfo">msk.<wbr>Cluster<wbr>Broker<wbr>Node<wbr>Group<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for the broker nodes of the Kafka cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client<wbr>Authentication</td>
            <td class="align-top">
                
                <code><a href="#clusterclientauthentication">msk.<wbr>Cluster<wbr>Client<wbr>Authentication?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for specifying a client authentication. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the MSK cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterconfigurationinfo">msk.<wbr>Cluster<wbr>Configuration<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">current<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Current version of the MSK Cluster used for updates, e.g. `K13V1IB3VIYZZH`
* `encryption_info.0.encryption_at_rest_kms_key_arn` - The ARN of the KMS key used for encryption at rest of the broker data volumes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterencryptioninfo">msk.<wbr>Cluster<wbr>Encryption<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for specifying encryption. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enhanced<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Specify the desired enhanced MSK CloudWatch monitoring level.  See [Monitoring Amazon MSK with Amazon CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kafka<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specify the desired Kafka software version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">number<wbr>Of<wbr>Broker<wbr>Nodes</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">open<wbr>Monitoring</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoring">msk.<wbr>Cluster<wbr>Open<wbr>Monitoring?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for JMX and Node monitoring for the MSK cluster. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zookeeper<wbr>Connect<wbr>String</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A comma separated list of one or more hostname:port pairs to use to connect to the Apache Zookeeper cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bootstrap_<wbr>brokers</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A comma separated list of one or more hostname:port pairs of kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if `client_broker` encryption in transit is set to `PLAINTEXT` or `TLS_PLAINTEXT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bootstrap_<wbr>brokers_<wbr>tls</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if `client_broker` encryption in transit is set to `TLS_PLAINTEXT` or `TLS`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">broker_<wbr>node_<wbr>group_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#clusterbrokernodegroupinfo">dict{cluster_<wbr>broker_<wbr>node_<wbr>group_<wbr>info}</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for the broker nodes of the Kafka cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client_<wbr>authentication</td>
            <td class="align-top">
                
                <code><a href="#clusterclientauthentication">dict{cluster_<wbr>client_<wbr>authentication}</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for specifying a client authentication. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of the MSK cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#clusterconfigurationinfo">dict{cluster_<wbr>configuration_<wbr>info}</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">current_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Current version of the MSK Cluster used for updates, e.g. `K13V1IB3VIYZZH`
* `encryption_info.0.encryption_at_rest_kms_key_arn` - The ARN of the KMS key used for encryption at rest of the broker data volumes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#clusterencryptioninfo">dict{cluster_<wbr>encryption_<wbr>info}</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for specifying encryption. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enhanced_<wbr>monitoring</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Specify the desired enhanced MSK CloudWatch monitoring level.  See [Monitoring Amazon MSK with Amazon CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kafka_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Specify the desired Kafka software version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">number_<wbr>of_<wbr>broker_<wbr>nodes</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">open_<wbr>monitoring</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoring">dict{cluster_<wbr>open_<wbr>monitoring}</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for JMX and Node monitoring for the MSK cluster. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zookeeper_<wbr>connect_<wbr>string</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A comma separated list of one or more hostname:port pairs to use to connect to the Apache Zookeeper cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Cluster Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/msk/#ClusterState">ClusterState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/msk/#Cluster">Cluster</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>bootstrap_brokers=None<span class="p">, </span>bootstrap_brokers_tls=None<span class="p">, </span>broker_node_group_info=None<span class="p">, </span>client_authentication=None<span class="p">, </span>cluster_name=None<span class="p">, </span>configuration_info=None<span class="p">, </span>current_version=None<span class="p">, </span>encryption_info=None<span class="p">, </span>enhanced_monitoring=None<span class="p">, </span>kafka_version=None<span class="p">, </span>number_of_broker_nodes=None<span class="p">, </span>open_monitoring=None<span class="p">, </span>tags=None<span class="p">, </span>zookeeper_connect_string=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterState">ClusterState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#Cluster">Cluster</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.Cluster.html">Cluster</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterState.html">ClusterState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Cluster resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following state arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bootstrap<wbr>Brokers</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comma separated list of one or more hostname:port pairs of kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if `client_broker` encryption in transit is set to `PLAINTEXT` or `TLS_PLAINTEXT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bootstrap<wbr>Brokers<wbr>Tls</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if `client_broker` encryption in transit is set to `TLS_PLAINTEXT` or `TLS`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Broker<wbr>Node<wbr>Group<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterbrokernodegroupinfo">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Broker<wbr>Node<wbr>Group<wbr>Info<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for the broker nodes of the Kafka cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Authentication</td>
            <td class="align-top">
                
                <code><a href="#clusterclientauthentication">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Client<wbr>Authentication<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying a client authentication. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the MSK cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterconfigurationinfo">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Configuration<wbr>Info<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Current<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Current version of the MSK Cluster used for updates, e.g. `K13V1IB3VIYZZH`
* `encryption_info.0.encryption_at_rest_kms_key_arn` - The ARN of the KMS key used for encryption at rest of the broker data volumes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterencryptioninfo">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Encryption<wbr>Info<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying encryption. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enhanced<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the desired enhanced MSK CloudWatch monitoring level.  See [Monitoring Amazon MSK with Amazon CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kafka<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the desired Kafka software version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Number<wbr>Of<wbr>Broker<wbr>Nodes</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Open<wbr>Monitoring</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoring">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Open<wbr>Monitoring<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for JMX and Node monitoring for the MSK cluster. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zookeeper<wbr>Connect<wbr>String</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comma separated list of one or more hostname:port pairs to use to connect to the Apache Zookeeper cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bootstrap<wbr>Brokers</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comma separated list of one or more hostname:port pairs of kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if `client_broker` encryption in transit is set to `PLAINTEXT` or `TLS_PLAINTEXT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bootstrap<wbr>Brokers<wbr>Tls</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if `client_broker` encryption in transit is set to `TLS_PLAINTEXT` or `TLS`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Broker<wbr>Node<wbr>Group<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterbrokernodegroupinfo">*msk.<wbr>Cluster<wbr>Broker<wbr>Node<wbr>Group<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for the broker nodes of the Kafka cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Authentication</td>
            <td class="align-top">
                
                <code><a href="#clusterclientauthentication">*msk.<wbr>Cluster<wbr>Client<wbr>Authentication</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying a client authentication. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the MSK cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterconfigurationinfo">*msk.<wbr>Cluster<wbr>Configuration<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Current<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Current version of the MSK Cluster used for updates, e.g. `K13V1IB3VIYZZH`
* `encryption_info.0.encryption_at_rest_kms_key_arn` - The ARN of the KMS key used for encryption at rest of the broker data volumes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterencryptioninfo">*msk.<wbr>Cluster<wbr>Encryption<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying encryption. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enhanced<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the desired enhanced MSK CloudWatch monitoring level.  See [Monitoring Amazon MSK with Amazon CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kafka<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the desired Kafka software version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Number<wbr>Of<wbr>Broker<wbr>Nodes</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Open<wbr>Monitoring</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoring">*msk.<wbr>Cluster<wbr>Open<wbr>Monitoring</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for JMX and Node monitoring for the MSK cluster. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zookeeper<wbr>Connect<wbr>String</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comma separated list of one or more hostname:port pairs to use to connect to the Apache Zookeeper cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bootstrap<wbr>Brokers</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comma separated list of one or more hostname:port pairs of kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if `client_broker` encryption in transit is set to `PLAINTEXT` or `TLS_PLAINTEXT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bootstrap<wbr>Brokers<wbr>Tls</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if `client_broker` encryption in transit is set to `TLS_PLAINTEXT` or `TLS`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">broker<wbr>Node<wbr>Group<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterbrokernodegroupinfo">msk.<wbr>Cluster<wbr>Broker<wbr>Node<wbr>Group<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for the broker nodes of the Kafka cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client<wbr>Authentication</td>
            <td class="align-top">
                
                <code><a href="#clusterclientauthentication">msk.<wbr>Cluster<wbr>Client<wbr>Authentication?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying a client authentication. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the MSK cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterconfigurationinfo">msk.<wbr>Cluster<wbr>Configuration<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">current<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Current version of the MSK Cluster used for updates, e.g. `K13V1IB3VIYZZH`
* `encryption_info.0.encryption_at_rest_kms_key_arn` - The ARN of the KMS key used for encryption at rest of the broker data volumes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#clusterencryptioninfo">msk.<wbr>Cluster<wbr>Encryption<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying encryption. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enhanced<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the desired enhanced MSK CloudWatch monitoring level.  See [Monitoring Amazon MSK with Amazon CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kafka<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the desired Kafka software version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">number<wbr>Of<wbr>Broker<wbr>Nodes</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">open<wbr>Monitoring</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoring">msk.<wbr>Cluster<wbr>Open<wbr>Monitoring?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for JMX and Node monitoring for the MSK cluster. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zookeeper<wbr>Connect<wbr>String</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comma separated list of one or more hostname:port pairs to use to connect to the Apache Zookeeper cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bootstrap_<wbr>brokers</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comma separated list of one or more hostname:port pairs of kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if `client_broker` encryption in transit is set to `PLAINTEXT` or `TLS_PLAINTEXT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bootstrap_<wbr>brokers_<wbr>tls</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if `client_broker` encryption in transit is set to `TLS_PLAINTEXT` or `TLS`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">broker_<wbr>node_<wbr>group_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#clusterbrokernodegroupinfo">dict{cluster_<wbr>broker_<wbr>node_<wbr>group_<wbr>info}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for the broker nodes of the Kafka cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client_<wbr>authentication</td>
            <td class="align-top">
                
                <code><a href="#clusterclientauthentication">dict{cluster_<wbr>client_<wbr>authentication}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying a client authentication. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the MSK cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#clusterconfigurationinfo">dict{cluster_<wbr>configuration_<wbr>info}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">current_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Current version of the MSK Cluster used for updates, e.g. `K13V1IB3VIYZZH`
* `encryption_info.0.encryption_at_rest_kms_key_arn` - The ARN of the KMS key used for encryption at rest of the broker data volumes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#clusterencryptioninfo">dict{cluster_<wbr>encryption_<wbr>info}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying encryption. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enhanced_<wbr>monitoring</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the desired enhanced MSK CloudWatch monitoring level.  See [Monitoring Amazon MSK with Amazon CloudWatch](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kafka_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify the desired Kafka software version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">number_<wbr>of_<wbr>broker_<wbr>nodes</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">open_<wbr>monitoring</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoring">dict{cluster_<wbr>open_<wbr>monitoring}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for JMX and Node monitoring for the MSK cluster. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zookeeper_<wbr>connect_<wbr>string</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A comma separated list of one or more hostname:port pairs to use to connect to the Apache Zookeeper cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### ClusterBrokerNodeGroupInfo
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClusterBrokerNodeGroupInfo">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClusterBrokerNodeGroupInfo">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterBrokerNodeGroupInfoArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterBrokerNodeGroupInfoOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterBrokerNodeGroupInfoArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterBrokerNodeGroupInfo.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Az<wbr>Distribution</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The distribution of broker nodes across availability zones ([documentation](https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#clusters-model-brokerazdistribution)). Currently the only valid value is `DEFAULT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Subnets</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of subnets to connect to in client VPC ([documentation](https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#clusters-prop-brokernodegroupinfo-clientsubnets)).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Volume<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The size in GiB of the EBS volume for the data drive on each broker node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specify the instance type to use for the kafka brokers. e.g. kafka.m5.large. ([Pricing info](https://aws.amazon.com/msk/pricing/))
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of the security groups to associate with the elastic network interfaces to control who can communicate with the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Az<wbr>Distribution</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The distribution of broker nodes across availability zones ([documentation](https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#clusters-model-brokerazdistribution)). Currently the only valid value is `DEFAULT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Subnets</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of subnets to connect to in client VPC ([documentation](https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#clusters-prop-brokernodegroupinfo-clientsubnets)).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Volume<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The size in GiB of the EBS volume for the data drive on each broker node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specify the instance type to use for the kafka brokers. e.g. kafka.m5.large. ([Pricing info](https://aws.amazon.com/msk/pricing/))
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of the security groups to associate with the elastic network interfaces to control who can communicate with the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">az<wbr>Distribution</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The distribution of broker nodes across availability zones ([documentation](https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#clusters-model-brokerazdistribution)). Currently the only valid value is `DEFAULT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client<wbr>Subnets</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of subnets to connect to in client VPC ([documentation](https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#clusters-prop-brokernodegroupinfo-clientsubnets)).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Volume<wbr>Size</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The size in GiB of the EBS volume for the data drive on each broker node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specify the instance type to use for the kafka brokers. e.g. kafka.m5.large. ([Pricing info](https://aws.amazon.com/msk/pricing/))
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of the security groups to associate with the elastic network interfaces to control who can communicate with the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">az_<wbr>distribution</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The distribution of broker nodes across availability zones ([documentation](https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#clusters-model-brokerazdistribution)). Currently the only valid value is `DEFAULT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client_<wbr>subnets</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of subnets to connect to in client VPC ([documentation](https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#clusters-prop-brokernodegroupinfo-clientsubnets)).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>volume_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The size in GiB of the EBS volume for the data drive on each broker node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specify the instance type to use for the kafka brokers. e.g. kafka.m5.large. ([Pricing info](https://aws.amazon.com/msk/pricing/))
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>groups</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of the security groups to associate with the elastic network interfaces to control who can communicate with the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ClusterClientAuthentication
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClusterClientAuthentication">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClusterClientAuthentication">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterClientAuthenticationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterClientAuthenticationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterClientAuthenticationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterClientAuthentication.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Tls</td>
            <td class="align-top">
                
                <code><a href="#clusterclientauthenticationtls">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Client<wbr>Authentication<wbr>Tls<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying TLS client authentication. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Tls</td>
            <td class="align-top">
                
                <code><a href="#clusterclientauthenticationtls">*msk.<wbr>Cluster<wbr>Client<wbr>Authentication<wbr>Tls</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying TLS client authentication. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">tls</td>
            <td class="align-top">
                
                <code><a href="#clusterclientauthenticationtls">msk.<wbr>Cluster<wbr>Client<wbr>Authentication<wbr>Tls?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying TLS client authentication. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">tls</td>
            <td class="align-top">
                
                <code><a href="#clusterclientauthenticationtls">dict{cluster_<wbr>client_<wbr>authentication_<wbr>tls}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for specifying TLS client authentication. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ClusterClientAuthenticationTls
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClusterClientAuthenticationTls">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClusterClientAuthenticationTls">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterClientAuthenticationTlsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterClientAuthenticationTlsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterClientAuthenticationTlsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterClientAuthenticationTls.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Certificate<wbr>Authority<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of ACM Certificate Authority Amazon Resource Names (ARNs).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Certificate<wbr>Authority<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of ACM Certificate Authority Amazon Resource Names (ARNs).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">certificate<wbr>Authority<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of ACM Certificate Authority Amazon Resource Names (ARNs).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">certificate_<wbr>authority_<wbr>arns</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of ACM Certificate Authority Amazon Resource Names (ARNs).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ClusterConfigurationInfo
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClusterConfigurationInfo">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClusterConfigurationInfo">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterConfigurationInfoArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterConfigurationInfoOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterConfigurationInfoArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterConfigurationInfo.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Revision</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Revision of the MSK Configuration to use in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Revision</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Revision of the MSK Configuration to use in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">revision</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Revision of the MSK Configuration to use in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">revision</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Revision of the MSK Configuration to use in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ClusterEncryptionInfo
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClusterEncryptionInfo">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClusterEncryptionInfo">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterEncryptionInfoArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterEncryptionInfoOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterEncryptionInfoArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterEncryptionInfo.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Encryption<wbr>At<wbr>Rest<wbr>Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
You may specify a KMS key short ID or ARN (it will always output an ARN) to use for encrypting your data at rest.  If no key is specified, an AWS managed KMS (&#39;aws/msk&#39; managed service) key will be used for encrypting the data at rest.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>In<wbr>Transit</td>
            <td class="align-top">
                
                <code><a href="#clusterencryptioninfoencryptionintransit">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Encryption<wbr>Info<wbr>Encryption<wbr>In<wbr>Transit<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to specify encryption in transit. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Encryption<wbr>At<wbr>Rest<wbr>Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
You may specify a KMS key short ID or ARN (it will always output an ARN) to use for encrypting your data at rest.  If no key is specified, an AWS managed KMS (&#39;aws/msk&#39; managed service) key will be used for encrypting the data at rest.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>In<wbr>Transit</td>
            <td class="align-top">
                
                <code><a href="#clusterencryptioninfoencryptionintransit">*msk.<wbr>Cluster<wbr>Encryption<wbr>Info<wbr>Encryption<wbr>In<wbr>Transit</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to specify encryption in transit. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">encryption<wbr>At<wbr>Rest<wbr>Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
You may specify a KMS key short ID or ARN (it will always output an ARN) to use for encrypting your data at rest.  If no key is specified, an AWS managed KMS (&#39;aws/msk&#39; managed service) key will be used for encrypting the data at rest.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption<wbr>In<wbr>Transit</td>
            <td class="align-top">
                
                <code><a href="#clusterencryptioninfoencryptionintransit">msk.<wbr>Cluster<wbr>Encryption<wbr>Info<wbr>Encryption<wbr>In<wbr>Transit?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to specify encryption in transit. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">encryption_<wbr>at_<wbr>rest_<wbr>kms_<wbr>key_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
You may specify a KMS key short ID or ARN (it will always output an ARN) to use for encrypting your data at rest.  If no key is specified, an AWS managed KMS (&#39;aws/msk&#39; managed service) key will be used for encrypting the data at rest.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption_<wbr>in_<wbr>transit</td>
            <td class="align-top">
                
                <code><a href="#clusterencryptioninfoencryptionintransit">dict{cluster_<wbr>encryption_<wbr>info_<wbr>encryption_<wbr>in_<wbr>transit}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to specify encryption in transit. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ClusterEncryptionInfoEncryptionInTransit
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClusterEncryptionInfoEncryptionInTransit">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClusterEncryptionInfoEncryptionInTransit">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterEncryptionInfoEncryptionInTransitArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterEncryptionInfoEncryptionInTransitOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterEncryptionInfoEncryptionInTransitArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterEncryptionInfoEncryptionInTransit.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Client<wbr>Broker</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encryption setting for data in transit between clients and brokers. Valid values: `TLS`, `TLS_PLAINTEXT`, and `PLAINTEXT`. Default value is `TLS_PLAINTEXT` when `encryption_in_transit` block defined, but `TLS` when `encryption_in_transit` block omitted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">In<wbr>Cluster</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether data communication among broker nodes is encrypted. Default value: `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Client<wbr>Broker</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encryption setting for data in transit between clients and brokers. Valid values: `TLS`, `TLS_PLAINTEXT`, and `PLAINTEXT`. Default value is `TLS_PLAINTEXT` when `encryption_in_transit` block defined, but `TLS` when `encryption_in_transit` block omitted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">In<wbr>Cluster</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether data communication among broker nodes is encrypted. Default value: `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">client<wbr>Broker</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encryption setting for data in transit between clients and brokers. Valid values: `TLS`, `TLS_PLAINTEXT`, and `PLAINTEXT`. Default value is `TLS_PLAINTEXT` when `encryption_in_transit` block defined, but `TLS` when `encryption_in_transit` block omitted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">in<wbr>Cluster</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether data communication among broker nodes is encrypted. Default value: `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">client_<wbr>broker</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encryption setting for data in transit between clients and brokers. Valid values: `TLS`, `TLS_PLAINTEXT`, and `PLAINTEXT`. Default value is `TLS_PLAINTEXT` when `encryption_in_transit` block defined, but `TLS` when `encryption_in_transit` block omitted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">in_<wbr>cluster</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether data communication among broker nodes is encrypted. Default value: `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ClusterOpenMonitoring
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClusterOpenMonitoring">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClusterOpenMonitoring">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterOpenMonitoringArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterOpenMonitoringOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterOpenMonitoringArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterOpenMonitoring.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Prometheus</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoringprometheus">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Open<wbr>Monitoring<wbr>Prometheus<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block for Prometheus settings for open monitoring. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Prometheus</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoringprometheus">msk.<wbr>Cluster<wbr>Open<wbr>Monitoring<wbr>Prometheus</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block for Prometheus settings for open monitoring. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">prometheus</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoringprometheus">msk.<wbr>Cluster<wbr>Open<wbr>Monitoring<wbr>Prometheus</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block for Prometheus settings for open monitoring. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">prometheus</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoringprometheus">dict{cluster_<wbr>open_<wbr>monitoring_<wbr>prometheus}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block for Prometheus settings for open monitoring. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ClusterOpenMonitoringPrometheus
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClusterOpenMonitoringPrometheus">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClusterOpenMonitoringPrometheus">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterOpenMonitoringPrometheusArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterOpenMonitoringPrometheusOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterOpenMonitoringPrometheusArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterOpenMonitoringPrometheus.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Jmx<wbr>Exporter</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoringprometheusjmxexporter">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Open<wbr>Monitoring<wbr>Prometheus<wbr>Jmx<wbr>Exporter<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for JMX Exporter. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Exporter</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoringprometheusnodeexporter">Pulumi.<wbr>Aws.<wbr>Msk.<wbr>Cluster<wbr>Open<wbr>Monitoring<wbr>Prometheus<wbr>Node<wbr>Exporter<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for Node Exporter. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Jmx<wbr>Exporter</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoringprometheusjmxexporter">*msk.<wbr>Cluster<wbr>Open<wbr>Monitoring<wbr>Prometheus<wbr>Jmx<wbr>Exporter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for JMX Exporter. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Exporter</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoringprometheusnodeexporter">*msk.<wbr>Cluster<wbr>Open<wbr>Monitoring<wbr>Prometheus<wbr>Node<wbr>Exporter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for Node Exporter. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">jmx<wbr>Exporter</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoringprometheusjmxexporter">msk.<wbr>Cluster<wbr>Open<wbr>Monitoring<wbr>Prometheus<wbr>Jmx<wbr>Exporter?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for JMX Exporter. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node<wbr>Exporter</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoringprometheusnodeexporter">msk.<wbr>Cluster<wbr>Open<wbr>Monitoring<wbr>Prometheus<wbr>Node<wbr>Exporter?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for Node Exporter. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">jmx_<wbr>exporter</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoringprometheusjmxexporter">dict{cluster_<wbr>open_<wbr>monitoring_<wbr>prometheus_<wbr>jmx_<wbr>exporter}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for JMX Exporter. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node_<wbr>exporter</td>
            <td class="align-top">
                
                <code><a href="#clusteropenmonitoringprometheusnodeexporter">dict{cluster_<wbr>open_<wbr>monitoring_<wbr>prometheus_<wbr>node_<wbr>exporter}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for Node Exporter. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ClusterOpenMonitoringPrometheusJmxExporter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClusterOpenMonitoringPrometheusJmxExporter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClusterOpenMonitoringPrometheusJmxExporter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterOpenMonitoringPrometheusJmxExporterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterOpenMonitoringPrometheusJmxExporterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterOpenMonitoringPrometheusJmxExporterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterOpenMonitoringPrometheusJmxExporter.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled<wbr>In<wbr>Broker</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether you want to enable or disable the Node Exporter.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled<wbr>In<wbr>Broker</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether you want to enable or disable the Node Exporter.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled<wbr>In<wbr>Broker</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether you want to enable or disable the Node Exporter.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled_<wbr>in_<wbr>broker</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether you want to enable or disable the Node Exporter.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ClusterOpenMonitoringPrometheusNodeExporter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClusterOpenMonitoringPrometheusNodeExporter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClusterOpenMonitoringPrometheusNodeExporter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterOpenMonitoringPrometheusNodeExporterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/msk?tab=doc#ClusterOpenMonitoringPrometheusNodeExporterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterOpenMonitoringPrometheusNodeExporterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Msk.ClusterOpenMonitoringPrometheusNodeExporter.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled<wbr>In<wbr>Broker</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether you want to enable or disable the Node Exporter.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled<wbr>In<wbr>Broker</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether you want to enable or disable the Node Exporter.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled<wbr>In<wbr>Broker</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether you want to enable or disable the Node Exporter.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled_<wbr>in_<wbr>broker</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether you want to enable or disable the Node Exporter.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







