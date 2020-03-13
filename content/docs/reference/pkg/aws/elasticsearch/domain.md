
---
title: "Domain"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Manages an AWS Elasticsearch Domain.

## Example Usage

### Basic Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.elasticsearch.Domain("example", {
    clusterConfig: {
        instanceType: "r4.large.elasticsearch",
    },
    elasticsearchVersion: "1.5",
    snapshotOptions: {
        automatedSnapshotStartHour: 23,
    },
    tags: {
        Domain: "TestDomain",
    },
});
```

### Access Policy

> See also: [`aws.elasticsearch.DomainPolicy` resource](https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy.html)

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const config = new pulumi.Config();
const domain = config.get("domain") || "tf-test";

const currentCallerIdentity = aws.getCallerIdentity();
const currentRegion = aws.getRegion();
const example = new aws.elasticsearch.Domain("example", {
    accessPolicies: `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "es:*",
      "Principal": "*",
      "Effect": "Allow",
      "Resource": "arn:aws:es:${currentRegion.name!}:${currentCallerIdentity.accountId}:domain/${domain}/*",
      "Condition": {
        "IpAddress": {"aws:SourceIp": ["66.193.100.22/32"]}
      }
    }
  ]
}
`,
});
```

### Log Publishing to CloudWatch Logs

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleLogGroup = new aws.cloudwatch.LogGroup("example", {});
const exampleLogResourcePolicy = new aws.cloudwatch.LogResourcePolicy("example", {
    policyDocument: `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "es.amazonaws.com"
      },
      "Action": [
        "logs:PutLogEvents",
        "logs:PutLogEventsBatch",
        "logs:CreateLogStream"
      ],
      "Resource": "arn:aws:logs:*"
    }
  ]
}
`,
    policyName: "example",
});
const exampleDomain = new aws.elasticsearch.Domain("example", {
    logPublishingOptions: [{
        cloudwatchLogGroupArn: exampleLogGroup.arn,
        logType: "INDEX_SLOW_LOGS",
    }],
});
```

### VPC based ES

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const config = new pulumi.Config();
const domain = config.get("domain") || "tf-test";
const vpc = config.require("vpc");

const esServiceLinkedRole = new aws.iam.ServiceLinkedRole("es", {
    awsServiceName: "es.amazonaws.com",
});
const currentCallerIdentity = aws.getCallerIdentity();
const currentRegion = aws.getRegion();
const selectedVpc = aws.ec2.getVpc({
    tags: {
        Name: vpc,
    },
});
const selectedSubnetIds = aws.ec2.getSubnetIds({
    tags: {
        Tier: "private",
    },
    vpcId: selectedVpc.id!,
});
const esDomain = new aws.elasticsearch.Domain("es", {
    accessPolicies: `{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Action": "es:*",
			"Principal": "*",
			"Effect": "Allow",
			"Resource": "arn:aws:es:${currentRegion.name!}:${currentCallerIdentity.accountId}:domain/${domain}/*"
		}
	]
}
`,
    advancedOptions: {
        "rest.action.multi.allow_explicit_index": "true",
    },
    clusterConfig: {
        instanceType: "m4.large.elasticsearch",
    },
    elasticsearchVersion: "6.3",
    snapshotOptions: {
        automatedSnapshotStartHour: 23,
    },
    tags: {
        Domain: "TestDomain",
    },
    vpcOptions: {
        securityGroupIds: [aws_security_group_elasticsearch.id],
        subnetIds: [
            selectedSubnetIds.ids[0],
            selectedSubnetIds.ids[1],
        ],
    },
}, {dependsOn: [esServiceLinkedRole]});
const esSecurityGroup = new aws.ec2.SecurityGroup("es", {
    description: "Managed by Pulumi",
    ingress: [{
        cidrBlocks: [selectedVpc.cidrBlock!],
        fromPort: 443,
        protocol: "tcp",
        toPort: 443,
    }],
    vpcId: selectedVpc.id!,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elasticsearch_domain.html.markdown.



## Create a Domain Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elasticsearch/#Domain">Domain</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elasticsearch/#DomainArgs">DomainArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Domain</span><span class="p">(resource_name, id, opts=None, </span>access_policies=None<span class="p">, </span>advanced_options=None<span class="p">, </span>cluster_config=None<span class="p">, </span>cognito_options=None<span class="p">, </span>domain_endpoint_options=None<span class="p">, </span>domain_name=None<span class="p">, </span>ebs_options=None<span class="p">, </span>elasticsearch_version=None<span class="p">, </span>encrypt_at_rest=None<span class="p">, </span>log_publishing_options=None<span class="p">, </span>node_to_node_encryption=None<span class="p">, </span>snapshot_options=None<span class="p">, </span>tags=None<span class="p">, </span>vpc_options=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDomain<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainArgs">DomainArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#Domain">Domain</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.Domain.html">Domain</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainArgs.html">DomainArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Domain resource with the given unique name, arguments, and options.

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
            <td class="align-top">Access<wbr>Policies</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
IAM policy document specifying the access policies for the domain
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Advanced<wbr>Options</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value string pairs to specify advanced configuration options.
Note that the values for these configuration options must be strings (wrapped in quotes) or they
may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
domain on every apply.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#domainclusterconfig">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Cluster<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Cluster configuration of the domain, see below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cognito<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaincognitooptions">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Cognito<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Endpoint<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaindomainendpointoptions">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Domain<wbr>Endpoint<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Domain endpoint HTTP(S) related options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainebsoptions">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Ebs<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of Elasticsearch to deploy. Defaults to `1.5`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypt<wbr>At<wbr>Rest</td>
            <td class="align-top">
                
                <code><a href="#domainencryptatrest">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Encrypt<wbr>At<wbr>Rest<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Publishing<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainlogpublishingoption">List&lt;Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Log<wbr>Publishing<wbr>Option<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Options for publishing slow logs to CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>To<wbr>Node<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#domainnodetonodeencryption">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Node<wbr>To<wbr>Node<wbr>Encryption<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Node-to-node encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainsnapshotoptions">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Snapshot<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Snapshot related options, see below.
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
            <td class="align-top">Vpc<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainvpcoptions">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Vpc<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
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
            <td class="align-top">Access<wbr>Policies</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
IAM policy document specifying the access policies for the domain
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Advanced<wbr>Options</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value string pairs to specify advanced configuration options.
Note that the values for these configuration options must be strings (wrapped in quotes) or they
may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
domain on every apply.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#domainclusterconfig">*elasticsearch.<wbr>Domain<wbr>Cluster<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Cluster configuration of the domain, see below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cognito<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaincognitooptions">*elasticsearch.<wbr>Domain<wbr>Cognito<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Endpoint<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaindomainendpointoptions">*elasticsearch.<wbr>Domain<wbr>Domain<wbr>Endpoint<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Domain endpoint HTTP(S) related options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainebsoptions">*elasticsearch.<wbr>Domain<wbr>Ebs<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of Elasticsearch to deploy. Defaults to `1.5`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypt<wbr>At<wbr>Rest</td>
            <td class="align-top">
                
                <code><a href="#domainencryptatrest">*elasticsearch.<wbr>Domain<wbr>Encrypt<wbr>At<wbr>Rest</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Publishing<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainlogpublishingoption">[]elasticsearch.<wbr>Domain<wbr>Log<wbr>Publishing<wbr>Option</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Options for publishing slow logs to CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>To<wbr>Node<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#domainnodetonodeencryption">*elasticsearch.<wbr>Domain<wbr>Node<wbr>To<wbr>Node<wbr>Encryption</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Node-to-node encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainsnapshotoptions">*elasticsearch.<wbr>Domain<wbr>Snapshot<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Snapshot related options, see below.
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
            <td class="align-top">Vpc<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainvpcoptions">*elasticsearch.<wbr>Domain<wbr>Vpc<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
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
            <td class="align-top">access<wbr>Policies</td>
            <td class="align-top">
                
                <code>string | Policy<wbr>Document</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
IAM policy document specifying the access policies for the domain
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">advanced<wbr>Options</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value string pairs to specify advanced configuration options.
Note that the values for these configuration options must be strings (wrapped in quotes) or they
may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
domain on every apply.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#domainclusterconfig">elasticsearch.<wbr>Domain<wbr>Cluster<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Cluster configuration of the domain, see below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cognito<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaincognitooptions">elasticsearch.<wbr>Domain<wbr>Cognito<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Endpoint<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaindomainendpointoptions">elasticsearch.<wbr>Domain<wbr>Domain<wbr>Endpoint<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Domain endpoint HTTP(S) related options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainebsoptions">elasticsearch.<wbr>Domain<wbr>Ebs<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of Elasticsearch to deploy. Defaults to `1.5`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypt<wbr>At<wbr>Rest</td>
            <td class="align-top">
                
                <code><a href="#domainencryptatrest">elasticsearch.<wbr>Domain<wbr>Encrypt<wbr>At<wbr>Rest?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Publishing<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainlogpublishingoption">elasticsearch.<wbr>Domain<wbr>Log<wbr>Publishing<wbr>Option[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Options for publishing slow logs to CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node<wbr>To<wbr>Node<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#domainnodetonodeencryption">elasticsearch.<wbr>Domain<wbr>Node<wbr>To<wbr>Node<wbr>Encryption?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Node-to-node encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainsnapshotoptions">elasticsearch.<wbr>Domain<wbr>Snapshot<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Snapshot related options, see below.
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
            <td class="align-top">vpc<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainvpcoptions">elasticsearch.<wbr>Domain<wbr>Vpc<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
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
            <td class="align-top">access_<wbr>policies</td>
            <td class="align-top">
                
                <code>dict</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
IAM policy document specifying the access policies for the domain
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">advanced_<wbr>options</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value string pairs to specify advanced configuration options.
Note that the values for these configuration options must be strings (wrapped in quotes) or they
may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
domain on every apply.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#domainclusterconfig">dict{domain_<wbr>cluster_<wbr>config}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Cluster configuration of the domain, see below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cognito_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domaincognitooptions">dict{domain_<wbr>cognito_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>endpoint_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domaindomainendpointoptions">dict{domain_<wbr>domain_<wbr>endpoint_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Domain endpoint HTTP(S) related options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domainebsoptions">dict{domain_<wbr>ebs_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of Elasticsearch to deploy. Defaults to `1.5`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypt_<wbr>at_<wbr>rest</td>
            <td class="align-top">
                
                <code><a href="#domainencryptatrest">dict{domain_<wbr>encrypt_<wbr>at_<wbr>rest}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>publishing_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domainlogpublishingoption">list[domain_<wbr>log_<wbr>publishing_<wbr>option]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Options for publishing slow logs to CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node_<wbr>to_<wbr>node_<wbr>encryption</td>
            <td class="align-top">
                
                <code><a href="#domainnodetonodeencryption">dict{domain_<wbr>node_<wbr>to_<wbr>node_<wbr>encryption}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Node-to-node encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domainsnapshotoptions">dict{domain_<wbr>snapshot_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Snapshot related options, see below.
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
            <td class="align-top">vpc_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domainvpcoptions">dict{domain_<wbr>vpc_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Domain Output Properties

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
            <td class="align-top">Access<wbr>Policies</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} IAM policy document specifying the access policies for the domain
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Advanced<wbr>Options</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;</code>
            </td>
            <td class="align-top">{{% md %}} Key-value string pairs to specify advanced configuration options.
Note that the values for these configuration options must be strings (wrapped in quotes) or they
may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
domain on every apply.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#domainclusterconfig">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Cluster<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Cluster configuration of the domain, see below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cognito<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaincognitooptions">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Cognito<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Endpoint<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaindomainendpointoptions">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Domain<wbr>Endpoint<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} Domain endpoint HTTP(S) related options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Unique identifier for the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainebsoptions">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Ebs<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The version of Elasticsearch to deploy. Defaults to `1.5`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypt<wbr>At<wbr>Rest</td>
            <td class="align-top">
                
                <code><a href="#domainencryptatrest">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Encrypt<wbr>At<wbr>Rest</a></code>
            </td>
            <td class="align-top">{{% md %}} Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Domain-specific endpoint used to submit index, search, and data upload requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kibana<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Domain-specific endpoint for kibana without https scheme.
* `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
* `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Publishing<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainlogpublishingoption">List&lt;Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Log<wbr>Publishing<wbr>Option&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} Options for publishing slow logs to CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>To<wbr>Node<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#domainnodetonodeencryption">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Node<wbr>To<wbr>Node<wbr>Encryption</a></code>
            </td>
            <td class="align-top">{{% md %}} Node-to-node encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainsnapshotoptions">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Snapshot<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} Snapshot related options, see below.
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
            <td class="align-top">Vpc<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainvpcoptions">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Vpc<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
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
            <td class="align-top">Access<wbr>Policies</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} IAM policy document specifying the access policies for the domain
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Advanced<wbr>Options</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} Key-value string pairs to specify advanced configuration options.
Note that the values for these configuration options must be strings (wrapped in quotes) or they
may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
domain on every apply.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#domainclusterconfig">elasticsearch.<wbr>Domain<wbr>Cluster<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Cluster configuration of the domain, see below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cognito<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaincognitooptions">*elasticsearch.<wbr>Domain<wbr>Cognito<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Endpoint<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaindomainendpointoptions">elasticsearch.<wbr>Domain<wbr>Domain<wbr>Endpoint<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} Domain endpoint HTTP(S) related options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Unique identifier for the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainebsoptions">elasticsearch.<wbr>Domain<wbr>Ebs<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The version of Elasticsearch to deploy. Defaults to `1.5`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypt<wbr>At<wbr>Rest</td>
            <td class="align-top">
                
                <code><a href="#domainencryptatrest">elasticsearch.<wbr>Domain<wbr>Encrypt<wbr>At<wbr>Rest</a></code>
            </td>
            <td class="align-top">{{% md %}} Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Domain-specific endpoint used to submit index, search, and data upload requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kibana<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Domain-specific endpoint for kibana without https scheme.
* `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
* `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Publishing<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainlogpublishingoption">[]elasticsearch.<wbr>Domain<wbr>Log<wbr>Publishing<wbr>Option</a></code>
            </td>
            <td class="align-top">{{% md %}} Options for publishing slow logs to CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>To<wbr>Node<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#domainnodetonodeencryption">elasticsearch.<wbr>Domain<wbr>Node<wbr>To<wbr>Node<wbr>Encryption</a></code>
            </td>
            <td class="align-top">{{% md %}} Node-to-node encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainsnapshotoptions">*elasticsearch.<wbr>Domain<wbr>Snapshot<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} Snapshot related options, see below.
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
            <td class="align-top">Vpc<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainvpcoptions">*elasticsearch.<wbr>Domain<wbr>Vpc<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
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
            <td class="align-top">access<wbr>Policies</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} IAM policy document specifying the access policies for the domain
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">advanced<wbr>Options</td>
            <td class="align-top">
                
                <code>{[key: string]: any}</code>
            </td>
            <td class="align-top">{{% md %}} Key-value string pairs to specify advanced configuration options.
Note that the values for these configuration options must be strings (wrapped in quotes) or they
may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
domain on every apply.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#domainclusterconfig">elasticsearch.<wbr>Domain<wbr>Cluster<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Cluster configuration of the domain, see below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cognito<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaincognitooptions">elasticsearch.<wbr>Domain<wbr>Cognito<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Endpoint<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaindomainendpointoptions">elasticsearch.<wbr>Domain<wbr>Domain<wbr>Endpoint<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} Domain endpoint HTTP(S) related options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Unique identifier for the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainebsoptions">elasticsearch.<wbr>Domain<wbr>Ebs<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The version of Elasticsearch to deploy. Defaults to `1.5`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypt<wbr>At<wbr>Rest</td>
            <td class="align-top">
                
                <code><a href="#domainencryptatrest">elasticsearch.<wbr>Domain<wbr>Encrypt<wbr>At<wbr>Rest</a></code>
            </td>
            <td class="align-top">{{% md %}} Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Domain-specific endpoint used to submit index, search, and data upload requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kibana<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Domain-specific endpoint for kibana without https scheme.
* `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
* `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Publishing<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainlogpublishingoption">elasticsearch.<wbr>Domain<wbr>Log<wbr>Publishing<wbr>Option[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} Options for publishing slow logs to CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node<wbr>To<wbr>Node<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#domainnodetonodeencryption">elasticsearch.<wbr>Domain<wbr>Node<wbr>To<wbr>Node<wbr>Encryption</a></code>
            </td>
            <td class="align-top">{{% md %}} Node-to-node encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainsnapshotoptions">elasticsearch.<wbr>Domain<wbr>Snapshot<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} Snapshot related options, see below.
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
            <td class="align-top">vpc<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainvpcoptions">elasticsearch.<wbr>Domain<wbr>Vpc<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
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
            <td class="align-top">access_<wbr>policies</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} IAM policy document specifying the access policies for the domain
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">advanced_<wbr>options</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} Key-value string pairs to specify advanced configuration options.
Note that the values for these configuration options must be strings (wrapped in quotes) or they
may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
domain on every apply.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#domainclusterconfig">dict{domain_<wbr>cluster_<wbr>config}</a></code>
            </td>
            <td class="align-top">{{% md %}} Cluster configuration of the domain, see below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cognito_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domaincognitooptions">dict{domain_<wbr>cognito_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>endpoint_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domaindomainendpointoptions">dict{domain_<wbr>domain_<wbr>endpoint_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}} Domain endpoint HTTP(S) related options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Unique identifier for the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domainebsoptions">dict{domain_<wbr>ebs_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}} EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The version of Elasticsearch to deploy. Defaults to `1.5`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypt_<wbr>at_<wbr>rest</td>
            <td class="align-top">
                
                <code><a href="#domainencryptatrest">dict{domain_<wbr>encrypt_<wbr>at_<wbr>rest}</a></code>
            </td>
            <td class="align-top">{{% md %}} Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Domain-specific endpoint used to submit index, search, and data upload requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kibana_<wbr>endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Domain-specific endpoint for kibana without https scheme.
* `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
* `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>publishing_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domainlogpublishingoption">list[domain_<wbr>log_<wbr>publishing_<wbr>option]</a></code>
            </td>
            <td class="align-top">{{% md %}} Options for publishing slow logs to CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node_<wbr>to_<wbr>node_<wbr>encryption</td>
            <td class="align-top">
                
                <code><a href="#domainnodetonodeencryption">dict{domain_<wbr>node_<wbr>to_<wbr>node_<wbr>encryption}</a></code>
            </td>
            <td class="align-top">{{% md %}} Node-to-node encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domainsnapshotoptions">dict{domain_<wbr>snapshot_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}} Snapshot related options, see below.
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
            <td class="align-top">vpc_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domainvpcoptions">dict{domain_<wbr>vpc_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}} VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Domain Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DomainState, opts?: pulumi.CustomResourceOptions): Domain;
```

```python
def get(resource_name, id, opts=None, access_<wbr>policies=None, advanced_<wbr>options=None, arn=None, cluster_<wbr>config=None, cognito_<wbr>options=None, domain_<wbr>endpoint_<wbr>options=None, domain_<wbr>id=None, domain_<wbr>name=None, ebs_<wbr>options=None, elasticsearch_<wbr>version=None, encrypt_<wbr>at_<wbr>rest=None, endpoint=None, kibana_<wbr>endpoint=None, log_<wbr>publishing_<wbr>options=None, node_<wbr>to_<wbr>node_<wbr>encryption=None, snapshot_<wbr>options=None, tags=None, vpc_<wbr>options=None)
```

```go
func GetDomain(ctx *pulumi.Context, name string, id pulumi.IDInput, state *DomainState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static Domain Get(string name, Input<string> id, DomainState? state = null, CustomResourceOptions? options = null);
```

Get an existing Domain resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Access<wbr>Policies</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
IAM policy document specifying the access policies for the domain
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Advanced<wbr>Options</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value string pairs to specify advanced configuration options.
Note that the values for these configuration options must be strings (wrapped in quotes) or they
may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
domain on every apply.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#domainclusterconfig">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Cluster<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Cluster configuration of the domain, see below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cognito<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaincognitooptions">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Cognito<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Endpoint<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaindomainendpointoptions">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Domain<wbr>Endpoint<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Domain endpoint HTTP(S) related options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Unique identifier for the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainebsoptions">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Ebs<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of Elasticsearch to deploy. Defaults to `1.5`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypt<wbr>At<wbr>Rest</td>
            <td class="align-top">
                
                <code><a href="#domainencryptatrest">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Encrypt<wbr>At<wbr>Rest<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Domain-specific endpoint used to submit index, search, and data upload requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kibana<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Domain-specific endpoint for kibana without https scheme.
* `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
* `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Publishing<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainlogpublishingoption">List&lt;Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Log<wbr>Publishing<wbr>Option<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Options for publishing slow logs to CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>To<wbr>Node<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#domainnodetonodeencryption">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Node<wbr>To<wbr>Node<wbr>Encryption<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Node-to-node encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainsnapshotoptions">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Snapshot<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Snapshot related options, see below.
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
            <td class="align-top">Vpc<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainvpcoptions">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Vpc<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
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
            <td class="align-top">Access<wbr>Policies</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
IAM policy document specifying the access policies for the domain
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Advanced<wbr>Options</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value string pairs to specify advanced configuration options.
Note that the values for these configuration options must be strings (wrapped in quotes) or they
may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
domain on every apply.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#domainclusterconfig">*elasticsearch.<wbr>Domain<wbr>Cluster<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Cluster configuration of the domain, see below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cognito<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaincognitooptions">*elasticsearch.<wbr>Domain<wbr>Cognito<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Endpoint<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaindomainendpointoptions">*elasticsearch.<wbr>Domain<wbr>Domain<wbr>Endpoint<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Domain endpoint HTTP(S) related options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Unique identifier for the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainebsoptions">*elasticsearch.<wbr>Domain<wbr>Ebs<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of Elasticsearch to deploy. Defaults to `1.5`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypt<wbr>At<wbr>Rest</td>
            <td class="align-top">
                
                <code><a href="#domainencryptatrest">*elasticsearch.<wbr>Domain<wbr>Encrypt<wbr>At<wbr>Rest</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Domain-specific endpoint used to submit index, search, and data upload requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kibana<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Domain-specific endpoint for kibana without https scheme.
* `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
* `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Publishing<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainlogpublishingoption">[]elasticsearch.<wbr>Domain<wbr>Log<wbr>Publishing<wbr>Option</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Options for publishing slow logs to CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>To<wbr>Node<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#domainnodetonodeencryption">*elasticsearch.<wbr>Domain<wbr>Node<wbr>To<wbr>Node<wbr>Encryption</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Node-to-node encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainsnapshotoptions">*elasticsearch.<wbr>Domain<wbr>Snapshot<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Snapshot related options, see below.
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
            <td class="align-top">Vpc<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainvpcoptions">*elasticsearch.<wbr>Domain<wbr>Vpc<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
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
            <td class="align-top">access<wbr>Policies</td>
            <td class="align-top">
                
                <code>string | Policy<wbr>Document</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
IAM policy document specifying the access policies for the domain
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">advanced<wbr>Options</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value string pairs to specify advanced configuration options.
Note that the values for these configuration options must be strings (wrapped in quotes) or they
may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
domain on every apply.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#domainclusterconfig">elasticsearch.<wbr>Domain<wbr>Cluster<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Cluster configuration of the domain, see below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cognito<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaincognitooptions">elasticsearch.<wbr>Domain<wbr>Cognito<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Endpoint<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domaindomainendpointoptions">elasticsearch.<wbr>Domain<wbr>Domain<wbr>Endpoint<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Domain endpoint HTTP(S) related options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Unique identifier for the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainebsoptions">elasticsearch.<wbr>Domain<wbr>Ebs<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of Elasticsearch to deploy. Defaults to `1.5`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypt<wbr>At<wbr>Rest</td>
            <td class="align-top">
                
                <code><a href="#domainencryptatrest">elasticsearch.<wbr>Domain<wbr>Encrypt<wbr>At<wbr>Rest?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Domain-specific endpoint used to submit index, search, and data upload requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kibana<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Domain-specific endpoint for kibana without https scheme.
* `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
* `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Publishing<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainlogpublishingoption">elasticsearch.<wbr>Domain<wbr>Log<wbr>Publishing<wbr>Option[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Options for publishing slow logs to CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node<wbr>To<wbr>Node<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#domainnodetonodeencryption">elasticsearch.<wbr>Domain<wbr>Node<wbr>To<wbr>Node<wbr>Encryption?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Node-to-node encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainsnapshotoptions">elasticsearch.<wbr>Domain<wbr>Snapshot<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Snapshot related options, see below.
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
            <td class="align-top">vpc<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#domainvpcoptions">elasticsearch.<wbr>Domain<wbr>Vpc<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
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
            <td class="align-top">access_<wbr>policies</td>
            <td class="align-top">
                
                <code>dict</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
IAM policy document specifying the access policies for the domain
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">advanced_<wbr>options</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value string pairs to specify advanced configuration options.
Note that the values for these configuration options must be strings (wrapped in quotes) or they
may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
domain on every apply.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#domainclusterconfig">dict{domain_<wbr>cluster_<wbr>config}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Cluster configuration of the domain, see below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cognito_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domaincognitooptions">dict{domain_<wbr>cognito_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>endpoint_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domaindomainendpointoptions">dict{domain_<wbr>domain_<wbr>endpoint_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Domain endpoint HTTP(S) related options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Unique identifier for the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domainebsoptions">dict{domain_<wbr>ebs_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of Elasticsearch to deploy. Defaults to `1.5`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypt_<wbr>at_<wbr>rest</td>
            <td class="align-top">
                
                <code><a href="#domainencryptatrest">dict{domain_<wbr>encrypt_<wbr>at_<wbr>rest}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Domain-specific endpoint used to submit index, search, and data upload requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kibana_<wbr>endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Domain-specific endpoint for kibana without https scheme.
* `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
* `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>publishing_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domainlogpublishingoption">list[domain_<wbr>log_<wbr>publishing_<wbr>option]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Options for publishing slow logs to CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node_<wbr>to_<wbr>node_<wbr>encryption</td>
            <td class="align-top">
                
                <code><a href="#domainnodetonodeencryption">dict{domain_<wbr>node_<wbr>to_<wbr>node_<wbr>encryption}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Node-to-node encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domainsnapshotoptions">dict{domain_<wbr>snapshot_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Snapshot related options, see below.
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
            <td class="align-top">vpc_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#domainvpcoptions">dict{domain_<wbr>vpc_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### DomainClusterConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DomainClusterConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DomainClusterConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainClusterConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainClusterConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainClusterConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainClusterConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Dedicated<wbr>Master<wbr>Count</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of dedicated master nodes in the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dedicated<wbr>Master<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether dedicated master nodes are enabled for the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dedicated<wbr>Master<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instance type of the dedicated master nodes in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Count</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of instances in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instance type of data nodes in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zone<wbr>Awareness<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#domainclusterconfigzoneawarenessconfig">Pulumi.<wbr>Aws.<wbr>Elasticsearch.<wbr>Domain<wbr>Cluster<wbr>Config<wbr>Zone<wbr>Awareness<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing zone awareness settings. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zone<wbr>Awareness<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether zone awareness is enabled. To enable awareness with three Availability Zones, the `availability_zone_count` within the `zone_awareness_config` must be set to `3`.
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
            <td class="align-top">Dedicated<wbr>Master<wbr>Count</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of dedicated master nodes in the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dedicated<wbr>Master<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether dedicated master nodes are enabled for the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dedicated<wbr>Master<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instance type of the dedicated master nodes in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Count</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of instances in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instance type of data nodes in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zone<wbr>Awareness<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#domainclusterconfigzoneawarenessconfig">*elasticsearch.<wbr>Domain<wbr>Cluster<wbr>Config<wbr>Zone<wbr>Awareness<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing zone awareness settings. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Zone<wbr>Awareness<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether zone awareness is enabled. To enable awareness with three Availability Zones, the `availability_zone_count` within the `zone_awareness_config` must be set to `3`.
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
            <td class="align-top">dedicated<wbr>Master<wbr>Count</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of dedicated master nodes in the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dedicated<wbr>Master<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether dedicated master nodes are enabled for the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dedicated<wbr>Master<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instance type of the dedicated master nodes in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Count</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of instances in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instance type of data nodes in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone<wbr>Awareness<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#domainclusterconfigzoneawarenessconfig">elasticsearch.<wbr>Domain<wbr>Cluster<wbr>Config<wbr>Zone<wbr>Awareness<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing zone awareness settings. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone<wbr>Awareness<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether zone awareness is enabled. To enable awareness with three Availability Zones, the `availability_zone_count` within the `zone_awareness_config` must be set to `3`.
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
            <td class="align-top">dedicated_<wbr>master_<wbr>count</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of dedicated master nodes in the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dedicated_<wbr>master_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether dedicated master nodes are enabled for the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dedicated_<wbr>master_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instance type of the dedicated master nodes in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>count</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of instances in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instance type of data nodes in the cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone_<wbr>awareness_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#domainclusterconfigzoneawarenessconfig">dict{domain_<wbr>cluster_<wbr>config_<wbr>zone_<wbr>awareness_<wbr>config}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing zone awareness settings. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone_<wbr>awareness_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether zone awareness is enabled. To enable awareness with three Availability Zones, the `availability_zone_count` within the `zone_awareness_config` must be set to `3`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DomainClusterConfigZoneAwarenessConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DomainClusterConfigZoneAwarenessConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DomainClusterConfigZoneAwarenessConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainClusterConfigZoneAwarenessConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainClusterConfigZoneAwarenessConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainClusterConfigZoneAwarenessConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainClusterConfigZoneAwarenessConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Availability<wbr>Zone<wbr>Count</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of Availability Zones for the domain to use with `zone_awareness_enabled`. Defaults to `2`. Valid values: `2` or `3`.
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
            <td class="align-top">Availability<wbr>Zone<wbr>Count</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of Availability Zones for the domain to use with `zone_awareness_enabled`. Defaults to `2`. Valid values: `2` or `3`.
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
            <td class="align-top">availability<wbr>Zone<wbr>Count</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of Availability Zones for the domain to use with `zone_awareness_enabled`. Defaults to `2`. Valid values: `2` or `3`.
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
            <td class="align-top">availability_<wbr>zone_<wbr>count</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of Availability Zones for the domain to use with `zone_awareness_enabled`. Defaults to `2`. Valid values: `2` or `3`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DomainCognitoOptions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DomainCognitoOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DomainCognitoOptions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainCognitoOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainCognitoOptionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainCognitoOptionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainCognitoOptions.html">output</a> API doc for this type.
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
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether Amazon Cognito authentication with Kibana is enabled or not
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ID of the Cognito Identity Pool to use
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the IAM role that has the AmazonESCognitoAccess policy attached
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ID of the Cognito User Pool to use
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
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether Amazon Cognito authentication with Kibana is enabled or not
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ID of the Cognito Identity Pool to use
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the IAM role that has the AmazonESCognitoAccess policy attached
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ID of the Cognito User Pool to use
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
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether Amazon Cognito authentication with Kibana is enabled or not
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ID of the Cognito Identity Pool to use
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the IAM role that has the AmazonESCognitoAccess policy attached
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ID of the Cognito User Pool to use
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
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether Amazon Cognito authentication with Kibana is enabled or not
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity_<wbr>pool_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ID of the Cognito Identity Pool to use
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the IAM role that has the AmazonESCognitoAccess policy attached
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>pool_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ID of the Cognito User Pool to use
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DomainDomainEndpointOptions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DomainDomainEndpointOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DomainDomainEndpointOptions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainDomainEndpointOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainDomainEndpointOptionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainDomainEndpointOptionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainDomainEndpointOptions.html">output</a> API doc for this type.
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
            <td class="align-top">Enforce<wbr>Https</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether or not to require HTTPS
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tls<wbr>Security<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">Enforce<wbr>Https</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether or not to require HTTPS
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tls<wbr>Security<wbr>Policy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">enforce<wbr>Https</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether or not to require HTTPS
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tls<wbr>Security<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">enforce_<wbr>https</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether or not to require HTTPS
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tls_<wbr>security_<wbr>policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DomainEbsOptions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DomainEbsOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DomainEbsOptions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainEbsOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainEbsOptionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainEbsOptionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainEbsOptions.html">output</a> API doc for this type.
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
            <td class="align-top">Ebs<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether EBS volumes are attached to data nodes in the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The baseline input/output (I/O) performance of EBS volumes
attached to data nodes. Applicable only for the Provisioned IOPS EBS volume type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The size of EBS volumes attached to data nodes (in GB).
**Required** if `ebs_enabled` is set to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of EBS volumes attached to data nodes.
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
            <td class="align-top">Ebs<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether EBS volumes are attached to data nodes in the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The baseline input/output (I/O) performance of EBS volumes
attached to data nodes. Applicable only for the Provisioned IOPS EBS volume type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The size of EBS volumes attached to data nodes (in GB).
**Required** if `ebs_enabled` is set to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of EBS volumes attached to data nodes.
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
            <td class="align-top">ebs<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether EBS volumes are attached to data nodes in the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The baseline input/output (I/O) performance of EBS volumes
attached to data nodes. Applicable only for the Provisioned IOPS EBS volume type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The size of EBS volumes attached to data nodes (in GB).
**Required** if `ebs_enabled` is set to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of EBS volumes attached to data nodes.
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
            <td class="align-top">ebs_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether EBS volumes are attached to data nodes in the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The baseline input/output (I/O) performance of EBS volumes
attached to data nodes. Applicable only for the Provisioned IOPS EBS volume type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The size of EBS volumes attached to data nodes (in GB).
**Required** if `ebs_enabled` is set to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of EBS volumes attached to data nodes.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DomainEncryptAtRest
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DomainEncryptAtRest">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DomainEncryptAtRest">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainEncryptAtRestArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainEncryptAtRestOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainEncryptAtRestArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainEncryptAtRest.html">output</a> API doc for this type.
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
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether Amazon Cognito authentication with Kibana is enabled or not
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The KMS key id to encrypt the Elasticsearch domain with. If not specified then it defaults to using the `aws/es` service KMS key.
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
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether Amazon Cognito authentication with Kibana is enabled or not
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The KMS key id to encrypt the Elasticsearch domain with. If not specified then it defaults to using the `aws/es` service KMS key.
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
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether Amazon Cognito authentication with Kibana is enabled or not
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The KMS key id to encrypt the Elasticsearch domain with. If not specified then it defaults to using the `aws/es` service KMS key.
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
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether Amazon Cognito authentication with Kibana is enabled or not
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The KMS key id to encrypt the Elasticsearch domain with. If not specified then it defaults to using the `aws/es` service KMS key.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DomainLogPublishingOption
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DomainLogPublishingOption">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DomainLogPublishingOption">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainLogPublishingOptionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainLogPublishingOptionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainLogPublishingOptionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainLogPublishingOption.html">output</a> API doc for this type.
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
            <td class="align-top">Cloudwatch<wbr>Log<wbr>Group<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the Cloudwatch log group to which log needs to be published.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether Amazon Cognito authentication with Kibana is enabled or not
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A type of Elasticsearch log. Valid values: INDEX_SLOW_LOGS, SEARCH_SLOW_LOGS, ES_APPLICATION_LOGS
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
            <td class="align-top">Cloudwatch<wbr>Log<wbr>Group<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the Cloudwatch log group to which log needs to be published.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether Amazon Cognito authentication with Kibana is enabled or not
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A type of Elasticsearch log. Valid values: INDEX_SLOW_LOGS, SEARCH_SLOW_LOGS, ES_APPLICATION_LOGS
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
            <td class="align-top">cloudwatch<wbr>Log<wbr>Group<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the Cloudwatch log group to which log needs to be published.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether Amazon Cognito authentication with Kibana is enabled or not
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A type of Elasticsearch log. Valid values: INDEX_SLOW_LOGS, SEARCH_SLOW_LOGS, ES_APPLICATION_LOGS
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
            <td class="align-top">cloudwatch_<wbr>log_<wbr>group_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the Cloudwatch log group to which log needs to be published.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether Amazon Cognito authentication with Kibana is enabled or not
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A type of Elasticsearch log. Valid values: INDEX_SLOW_LOGS, SEARCH_SLOW_LOGS, ES_APPLICATION_LOGS
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DomainNodeToNodeEncryption
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DomainNodeToNodeEncryption">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DomainNodeToNodeEncryption">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainNodeToNodeEncryptionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainNodeToNodeEncryptionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainNodeToNodeEncryptionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainNodeToNodeEncryption.html">output</a> API doc for this type.
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
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether Amazon Cognito authentication with Kibana is enabled or not
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
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether Amazon Cognito authentication with Kibana is enabled or not
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
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether Amazon Cognito authentication with Kibana is enabled or not
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
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether Amazon Cognito authentication with Kibana is enabled or not
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DomainSnapshotOptions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DomainSnapshotOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DomainSnapshotOptions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainSnapshotOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainSnapshotOptionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainSnapshotOptionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainSnapshotOptions.html">output</a> API doc for this type.
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
            <td class="align-top">Automated<wbr>Snapshot<wbr>Start<wbr>Hour</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Hour during which the service takes an automated daily
snapshot of the indices in the domain.
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
            <td class="align-top">Automated<wbr>Snapshot<wbr>Start<wbr>Hour</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Hour during which the service takes an automated daily
snapshot of the indices in the domain.
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
            <td class="align-top">automated<wbr>Snapshot<wbr>Start<wbr>Hour</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Hour during which the service takes an automated daily
snapshot of the indices in the domain.
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
            <td class="align-top">automated_<wbr>snapshot_<wbr>start_<wbr>hour</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Hour during which the service takes an automated daily
snapshot of the indices in the domain.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DomainVpcOptions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DomainVpcOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DomainVpcOptions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainVpcOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticsearch?tab=doc#DomainVpcOptionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainVpcOptionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticsearch.DomainVpcOptions.html">output</a> API doc for this type.
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
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of VPC Security Group IDs to be applied to the Elasticsearch domain endpoints. If omitted, the default Security Group for the VPC will be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of VPC Subnet IDs for the Elasticsearch domain endpoints to be created in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of VPC Security Group IDs to be applied to the Elasticsearch domain endpoints. If omitted, the default Security Group for the VPC will be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of VPC Subnet IDs for the Elasticsearch domain endpoints to be created in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of VPC Security Group IDs to be applied to the Elasticsearch domain endpoints. If omitted, the default Security Group for the VPC will be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of VPC Subnet IDs for the Elasticsearch domain endpoints to be created in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">availability_<wbr>zones</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>group_<wbr>ids</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of VPC Security Group IDs to be applied to the Elasticsearch domain endpoints. If omitted, the default Security Group for the VPC will be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>ids</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of VPC Subnet IDs for the Elasticsearch domain endpoints to be created in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







