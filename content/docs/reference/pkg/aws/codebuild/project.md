
---
title: "Project"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides a CodeBuild Project resource. See also the [`aws.codebuild.Webhook` resource](https://www.terraform.io/docs/providers/aws/r/codebuild_webhook.html), which manages the webhook to the source (e.g. the "rebuild every time a code change is pushed" option in the CodeBuild web console).

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleBucket = new aws.s3.Bucket("example", {
    acl: "private",
});
const exampleRole = new aws.iam.Role("example", {
    assumeRolePolicy: `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "codebuild.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
`,
});
const exampleRolePolicy = new aws.iam.RolePolicy("example", {
    policy: pulumi.interpolate`{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Resource": [
        "*"
      ],
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:DescribeDhcpOptions",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DeleteNetworkInterface",
        "ec2:DescribeSubnets",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeVpcs"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkInterfacePermission"
      ],
      "Resource": [
        "arn:aws:ec2:us-east-1:123456789012:network-interface/*"
      ],
      "Condition": {
        "StringEquals": {
          "ec2:Subnet": [
            "${aws_subnet_example1.arn}",
            "${aws_subnet_example2.arn}"
          ],
          "ec2:AuthorizedService": "codebuild.amazonaws.com"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:*"
      ],
      "Resource": [
        "${exampleBucket.arn}",
        "${exampleBucket.arn}/*"
      ]
    }
  ]
}
`,
    role: exampleRole.name,
});
const exampleProject = new aws.codebuild.Project("example", {
    artifacts: {
        type: "NO_ARTIFACTS",
    },
    buildTimeout: 5,
    cache: {
        location: exampleBucket.bucket,
        type: "S3",
    },
    description: "test_codebuild_project",
    environment: {
        computeType: "BUILD_GENERAL1_SMALL",
        environmentVariables: [
            {
                name: "SOME_KEY1",
                value: "SOME_VALUE1",
            },
            {
                name: "SOME_KEY2",
                type: "PARAMETER_STORE",
                value: "SOME_VALUE2",
            },
        ],
        image: "aws/codebuild/standard:1.0",
        imagePullCredentialsType: "CODEBUILD",
        type: "LINUX_CONTAINER",
    },
    logsConfig: {
        cloudwatchLogs: {
            groupName: "log-group",
            streamName: "log-stream",
        },
        s3Logs: {
            location: pulumi.interpolate`${exampleBucket.id}/build-log`,
            status: "ENABLED",
        },
    },
    serviceRole: exampleRole.arn,
    source: {
        gitCloneDepth: 1,
        gitSubmodulesConfig: {
            fetchSubmodules: true,
        },
        location: "https://github.com/mitchellh/packer.git",
        type: "GITHUB",
    },
    sourceVersion: "master",
    tags: {
        Environment: "Test",
    },
    vpcConfig: {
        securityGroupIds: [
            aws_security_group_example1.id,
            aws_security_group_example2.id,
        ],
        subnets: [
            aws_subnet_example1.id,
            aws_subnet_example2.id,
        ],
        vpcId: aws_vpc_example.id,
    },
});
const project_with_cache = new aws.codebuild.Project("project-with-cache", {
    artifacts: {
        type: "NO_ARTIFACTS",
    },
    buildTimeout: 5,
    cache: {
        modes: [
            "LOCAL_DOCKER_LAYER_CACHE",
            "LOCAL_SOURCE_CACHE",
        ],
        type: "LOCAL",
    },
    description: "test_codebuild_project_cache",
    environment: {
        computeType: "BUILD_GENERAL1_SMALL",
        environmentVariables: [{
            name: "SOME_KEY1",
            value: "SOME_VALUE1",
        }],
        image: "aws/codebuild/standard:1.0",
        imagePullCredentialsType: "CODEBUILD",
        type: "LINUX_CONTAINER",
    },
    queuedTimeout: 5,
    serviceRole: exampleRole.arn,
    source: {
        gitCloneDepth: 1,
        location: "https://github.com/mitchellh/packer.git",
        type: "GITHUB",
    },
    tags: {
        Environment: "Test",
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codebuild_project.html.markdown.



## Create a Project Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/codebuild/#Project">Project</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/codebuild/#ProjectArgs">ProjectArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Project</span><span class="p">(resource_name, opts=None, </span>artifacts=None<span class="p">, </span>badge_enabled=None<span class="p">, </span>build_timeout=None<span class="p">, </span>cache=None<span class="p">, </span>description=None<span class="p">, </span>encryption_key=None<span class="p">, </span>environment=None<span class="p">, </span>logs_config=None<span class="p">, </span>name=None<span class="p">, </span>queued_timeout=None<span class="p">, </span>secondary_artifacts=None<span class="p">, </span>secondary_sources=None<span class="p">, </span>service_role=None<span class="p">, </span>source=None<span class="p">, </span>source_version=None<span class="p">, </span>tags=None<span class="p">, </span>vpc_config=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewProject<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectArgs">ProjectArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#Project">Project</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.Project.html">Project</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectArgs.html">ProjectArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Project resource with the given unique name, arguments, and options.

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
            <td class="align-top">Artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectartifacts">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Artifacts<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Information about the project&#39;s build output artifacts. Artifact blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Badge<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Build<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cache</td>
            <td class="align-top">
                
                <code><a href="#projectcache">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Cache<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the cache storage for the project. Cache blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A short description of the project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project&#39;s build output artifacts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code><a href="#projectenvironment">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Environment<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Information about the project&#39;s build environment. Environment blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logs<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfig">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Logs<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to store log data to CloudWatch or S3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queued<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How long in minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it times out. The default is 8 hours.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Secondary<wbr>Artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectsecondaryartifact">List&lt;Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Secondary<wbr>Artifact<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Secondary<wbr>Sources</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysource">List&lt;Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Secondary<wbr>Source<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source</td>
            <td class="align-top">
                
                <code><a href="#projectsource">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Source<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Information about the project&#39;s input source code. Source blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A version of the build input to be built for this project. If not specified, the latest version is used.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectvpcconfig">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Vpc<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to run inside a VPC. VPC config blocks are documented below.
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
            <td class="align-top">Artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectartifacts">codebuild.<wbr>Project<wbr>Artifacts</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Information about the project&#39;s build output artifacts. Artifact blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Badge<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Build<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cache</td>
            <td class="align-top">
                
                <code><a href="#projectcache">*codebuild.<wbr>Project<wbr>Cache</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the cache storage for the project. Cache blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A short description of the project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project&#39;s build output artifacts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code><a href="#projectenvironment">codebuild.<wbr>Project<wbr>Environment</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Information about the project&#39;s build environment. Environment blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logs<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfig">*codebuild.<wbr>Project<wbr>Logs<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to store log data to CloudWatch or S3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queued<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How long in minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it times out. The default is 8 hours.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Secondary<wbr>Artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectsecondaryartifact">[]codebuild.<wbr>Project<wbr>Secondary<wbr>Artifact</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Secondary<wbr>Sources</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysource">[]codebuild.<wbr>Project<wbr>Secondary<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source</td>
            <td class="align-top">
                
                <code><a href="#projectsource">codebuild.<wbr>Project<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Information about the project&#39;s input source code. Source blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A version of the build input to be built for this project. If not specified, the latest version is used.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectvpcconfig">*codebuild.<wbr>Project<wbr>Vpc<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to run inside a VPC. VPC config blocks are documented below.
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
            <td class="align-top">artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectartifacts">codebuild.<wbr>Project<wbr>Artifacts</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Information about the project&#39;s build output artifacts. Artifact blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">badge<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">build<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cache</td>
            <td class="align-top">
                
                <code><a href="#projectcache">codebuild.<wbr>Project<wbr>Cache?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the cache storage for the project. Cache blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A short description of the project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project&#39;s build output artifacts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code><a href="#projectenvironment">codebuild.<wbr>Project<wbr>Environment</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Information about the project&#39;s build environment. Environment blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logs<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfig">codebuild.<wbr>Project<wbr>Logs<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to store log data to CloudWatch or S3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queued<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How long in minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it times out. The default is 8 hours.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">secondary<wbr>Artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectsecondaryartifact">codebuild.<wbr>Project<wbr>Secondary<wbr>Artifact[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">secondary<wbr>Sources</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysource">codebuild.<wbr>Project<wbr>Secondary<wbr>Source[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source</td>
            <td class="align-top">
                
                <code><a href="#projectsource">codebuild.<wbr>Project<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Information about the project&#39;s input source code. Source blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A version of the build input to be built for this project. If not specified, the latest version is used.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectvpcconfig">codebuild.<wbr>Project<wbr>Vpc<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to run inside a VPC. VPC config blocks are documented below.
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
            <td class="align-top">artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectartifacts">Dict[Project<wbr>Artifacts]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Information about the project&#39;s build output artifacts. Artifact blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">badge_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">build_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cache</td>
            <td class="align-top">
                
                <code><a href="#projectcache">Dict[Project<wbr>Cache]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the cache storage for the project. Cache blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A short description of the project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project&#39;s build output artifacts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code><a href="#projectenvironment">Dict[Project<wbr>Environment]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Information about the project&#39;s build environment. Environment blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logs_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfig">Dict[Project<wbr>Logs<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to store log data to CloudWatch or S3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queued_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How long in minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it times out. The default is 8 hours.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">secondary_<wbr>artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectsecondaryartifact">List[Project<wbr>Secondary<wbr>Artifact]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">secondary_<wbr>sources</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysource">List[Project<wbr>Secondary<wbr>Source]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>role</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source</td>
            <td class="align-top">
                
                <code><a href="#projectsource">Dict[Project<wbr>Source]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Information about the project&#39;s input source code. Source blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A version of the build input to be built for this project. If not specified, the latest version is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#projectvpcconfig">Dict[Project<wbr>Vpc<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to run inside a VPC. VPC config blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Project Output Properties

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
            <td class="align-top">{{% md %}} The ARN of the CodeBuild project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectartifacts">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Artifacts</a></code>
            </td>
            <td class="align-top">{{% md %}} Information about the project&#39;s build output artifacts. Artifact blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Badge<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Badge<wbr>Url</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The URL of the build badge when `badge_enabled` is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Build<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cache</td>
            <td class="align-top">
                
                <code><a href="#projectcache">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Cache?</a></code>
            </td>
            <td class="align-top">{{% md %}} Information about the cache storage for the project. Cache blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A short description of the project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project&#39;s build output artifacts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code><a href="#projectenvironment">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Environment</a></code>
            </td>
            <td class="align-top">{{% md %}} Information about the project&#39;s build environment. Environment blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logs<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfig">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Logs<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration for the builds to store log data to CloudWatch or S3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queued<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} How long in minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it times out. The default is 8 hours.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Secondary<wbr>Artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectsecondaryartifact">List&lt;Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Secondary<wbr>Artifact&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Secondary<wbr>Sources</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysource">List&lt;Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Secondary<wbr>Source&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source</td>
            <td class="align-top">
                
                <code><a href="#projectsource">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} Information about the project&#39;s input source code. Source blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A version of the build input to be built for this project. If not specified, the latest version is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectvpcconfig">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Vpc<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration for the builds to run inside a VPC. VPC config blocks are documented below.
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
            <td class="align-top">{{% md %}} The ARN of the CodeBuild project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectartifacts">codebuild.<wbr>Project<wbr>Artifacts</a></code>
            </td>
            <td class="align-top">{{% md %}} Information about the project&#39;s build output artifacts. Artifact blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Badge<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Badge<wbr>Url</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The URL of the build badge when `badge_enabled` is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Build<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cache</td>
            <td class="align-top">
                
                <code><a href="#projectcache">*codebuild.<wbr>Project<wbr>Cache</a></code>
            </td>
            <td class="align-top">{{% md %}} Information about the cache storage for the project. Cache blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A short description of the project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project&#39;s build output artifacts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code><a href="#projectenvironment">codebuild.<wbr>Project<wbr>Environment</a></code>
            </td>
            <td class="align-top">{{% md %}} Information about the project&#39;s build environment. Environment blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logs<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfig">*codebuild.<wbr>Project<wbr>Logs<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration for the builds to store log data to CloudWatch or S3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queued<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} How long in minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it times out. The default is 8 hours.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Secondary<wbr>Artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectsecondaryartifact">[]codebuild.<wbr>Project<wbr>Secondary<wbr>Artifact</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Secondary<wbr>Sources</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysource">[]codebuild.<wbr>Project<wbr>Secondary<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source</td>
            <td class="align-top">
                
                <code><a href="#projectsource">codebuild.<wbr>Project<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} Information about the project&#39;s input source code. Source blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} A version of the build input to be built for this project. If not specified, the latest version is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectvpcconfig">*codebuild.<wbr>Project<wbr>Vpc<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration for the builds to run inside a VPC. VPC config blocks are documented below.
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
            <td class="align-top">{{% md %}} The ARN of the CodeBuild project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectartifacts">codebuild.<wbr>Project<wbr>Artifacts</a></code>
            </td>
            <td class="align-top">{{% md %}} Information about the project&#39;s build output artifacts. Artifact blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">badge<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">badge<wbr>Url</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The URL of the build badge when `badge_enabled` is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">build<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cache</td>
            <td class="align-top">
                
                <code><a href="#projectcache">codebuild.<wbr>Project<wbr>Cache?</a></code>
            </td>
            <td class="align-top">{{% md %}} Information about the cache storage for the project. Cache blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A short description of the project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project&#39;s build output artifacts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code><a href="#projectenvironment">codebuild.<wbr>Project<wbr>Environment</a></code>
            </td>
            <td class="align-top">{{% md %}} Information about the project&#39;s build environment. Environment blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logs<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfig">codebuild.<wbr>Project<wbr>Logs<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration for the builds to store log data to CloudWatch or S3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queued<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} How long in minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it times out. The default is 8 hours.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">secondary<wbr>Artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectsecondaryartifact">codebuild.<wbr>Project<wbr>Secondary<wbr>Artifact[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">secondary<wbr>Sources</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysource">codebuild.<wbr>Project<wbr>Secondary<wbr>Source[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Role</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source</td>
            <td class="align-top">
                
                <code><a href="#projectsource">codebuild.<wbr>Project<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} Information about the project&#39;s input source code. Source blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A version of the build input to be built for this project. If not specified, the latest version is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectvpcconfig">codebuild.<wbr>Project<wbr>Vpc<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration for the builds to run inside a VPC. VPC config blocks are documented below.
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
            <td class="align-top">{{% md %}} The ARN of the CodeBuild project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectartifacts">Dict[Project<wbr>Artifacts]</a></code>
            </td>
            <td class="align-top">{{% md %}} Information about the project&#39;s build output artifacts. Artifact blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">badge_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">badge_<wbr>url</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The URL of the build badge when `badge_enabled` is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">build_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cache</td>
            <td class="align-top">
                
                <code><a href="#projectcache">Dict[Project<wbr>Cache]</a></code>
            </td>
            <td class="align-top">{{% md %}} Information about the cache storage for the project. Cache blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A short description of the project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project&#39;s build output artifacts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code><a href="#projectenvironment">Dict[Project<wbr>Environment]</a></code>
            </td>
            <td class="align-top">{{% md %}} Information about the project&#39;s build environment. Environment blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logs_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfig">Dict[Project<wbr>Logs<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration for the builds to store log data to CloudWatch or S3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queued_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} How long in minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it times out. The default is 8 hours.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">secondary_<wbr>artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectsecondaryartifact">List[Project<wbr>Secondary<wbr>Artifact]</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">secondary_<wbr>sources</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysource">List[Project<wbr>Secondary<wbr>Source]</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>role</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source</td>
            <td class="align-top">
                
                <code><a href="#projectsource">Dict[Project<wbr>Source]</a></code>
            </td>
            <td class="align-top">{{% md %}} Information about the project&#39;s input source code. Source blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A version of the build input to be built for this project. If not specified, the latest version is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#projectvpcconfig">Dict[Project<wbr>Vpc<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration for the builds to run inside a VPC. VPC config blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Project Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/codebuild/#ProjectState">ProjectState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/codebuild/#Project">Project</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>artifacts=None<span class="p">, </span>badge_enabled=None<span class="p">, </span>badge_url=None<span class="p">, </span>build_timeout=None<span class="p">, </span>cache=None<span class="p">, </span>description=None<span class="p">, </span>encryption_key=None<span class="p">, </span>environment=None<span class="p">, </span>logs_config=None<span class="p">, </span>name=None<span class="p">, </span>queued_timeout=None<span class="p">, </span>secondary_artifacts=None<span class="p">, </span>secondary_sources=None<span class="p">, </span>service_role=None<span class="p">, </span>source=None<span class="p">, </span>source_version=None<span class="p">, </span>tags=None<span class="p">, </span>vpc_config=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetProject<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectState">ProjectState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#Project">Project</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.Project.html">Project</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectState.html">ProjectState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Project resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The ARN of the CodeBuild project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectartifacts">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Artifacts<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the project&#39;s build output artifacts. Artifact blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Badge<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Badge<wbr>Url</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The URL of the build badge when `badge_enabled` is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Build<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cache</td>
            <td class="align-top">
                
                <code><a href="#projectcache">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Cache<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the cache storage for the project. Cache blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A short description of the project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project&#39;s build output artifacts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code><a href="#projectenvironment">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Environment<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the project&#39;s build environment. Environment blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logs<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfig">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Logs<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to store log data to CloudWatch or S3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queued<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How long in minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it times out. The default is 8 hours.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Secondary<wbr>Artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectsecondaryartifact">List&lt;Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Secondary<wbr>Artifact<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Secondary<wbr>Sources</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysource">List&lt;Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Secondary<wbr>Source<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source</td>
            <td class="align-top">
                
                <code><a href="#projectsource">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Source<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the project&#39;s input source code. Source blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A version of the build input to be built for this project. If not specified, the latest version is used.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectvpcconfig">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Vpc<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to run inside a VPC. VPC config blocks are documented below.
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
The ARN of the CodeBuild project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectartifacts">*codebuild.<wbr>Project<wbr>Artifacts</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the project&#39;s build output artifacts. Artifact blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Badge<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Badge<wbr>Url</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The URL of the build badge when `badge_enabled` is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Build<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cache</td>
            <td class="align-top">
                
                <code><a href="#projectcache">*codebuild.<wbr>Project<wbr>Cache</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the cache storage for the project. Cache blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A short description of the project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project&#39;s build output artifacts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code><a href="#projectenvironment">*codebuild.<wbr>Project<wbr>Environment</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the project&#39;s build environment. Environment blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logs<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfig">*codebuild.<wbr>Project<wbr>Logs<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to store log data to CloudWatch or S3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queued<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How long in minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it times out. The default is 8 hours.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Secondary<wbr>Artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectsecondaryartifact">[]codebuild.<wbr>Project<wbr>Secondary<wbr>Artifact</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Secondary<wbr>Sources</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysource">[]codebuild.<wbr>Project<wbr>Secondary<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source</td>
            <td class="align-top">
                
                <code><a href="#projectsource">*codebuild.<wbr>Project<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the project&#39;s input source code. Source blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A version of the build input to be built for this project. If not specified, the latest version is used.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectvpcconfig">*codebuild.<wbr>Project<wbr>Vpc<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to run inside a VPC. VPC config blocks are documented below.
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
The ARN of the CodeBuild project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectartifacts">codebuild.<wbr>Project<wbr>Artifacts?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the project&#39;s build output artifacts. Artifact blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">badge<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">badge<wbr>Url</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The URL of the build badge when `badge_enabled` is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">build<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cache</td>
            <td class="align-top">
                
                <code><a href="#projectcache">codebuild.<wbr>Project<wbr>Cache?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the cache storage for the project. Cache blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A short description of the project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project&#39;s build output artifacts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code><a href="#projectenvironment">codebuild.<wbr>Project<wbr>Environment?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the project&#39;s build environment. Environment blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logs<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfig">codebuild.<wbr>Project<wbr>Logs<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to store log data to CloudWatch or S3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queued<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How long in minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it times out. The default is 8 hours.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">secondary<wbr>Artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectsecondaryartifact">codebuild.<wbr>Project<wbr>Secondary<wbr>Artifact[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">secondary<wbr>Sources</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysource">codebuild.<wbr>Project<wbr>Secondary<wbr>Source[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Role</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source</td>
            <td class="align-top">
                
                <code><a href="#projectsource">codebuild.<wbr>Project<wbr>Source?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the project&#39;s input source code. Source blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A version of the build input to be built for this project. If not specified, the latest version is used.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectvpcconfig">codebuild.<wbr>Project<wbr>Vpc<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to run inside a VPC. VPC config blocks are documented below.
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
The ARN of the CodeBuild project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectartifacts">Dict[Project<wbr>Artifacts]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the project&#39;s build output artifacts. Artifact blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">badge_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">badge_<wbr>url</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The URL of the build badge when `badge_enabled` is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">build_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cache</td>
            <td class="align-top">
                
                <code><a href="#projectcache">Dict[Project<wbr>Cache]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the cache storage for the project. Cache blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A short description of the project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project&#39;s build output artifacts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code><a href="#projectenvironment">Dict[Project<wbr>Environment]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the project&#39;s build environment. Environment blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logs_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfig">Dict[Project<wbr>Logs<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to store log data to CloudWatch or S3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queued_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How long in minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it times out. The default is 8 hours.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">secondary_<wbr>artifacts</td>
            <td class="align-top">
                
                <code><a href="#projectsecondaryartifact">List[Project<wbr>Secondary<wbr>Artifact]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">secondary_<wbr>sources</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysource">List[Project<wbr>Secondary<wbr>Source]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>role</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source</td>
            <td class="align-top">
                
                <code><a href="#projectsource">Dict[Project<wbr>Source]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the project&#39;s input source code. Source blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A version of the build input to be built for this project. If not specified, the latest version is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#projectvpcconfig">Dict[Project<wbr>Vpc<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to run inside a VPC. VPC config blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### ProjectArtifacts
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ProjectArtifacts">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ProjectArtifacts">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectArtifactsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectArtifactsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectArtifactsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectArtifacts.html">output</a> API doc for this type.
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
            <td class="align-top">Artifact<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Disabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The namespace to use in storing build artifacts. If `type` is set to `S3`, then valid values for this parameter are: `BUILD_ID` or `NONE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Override<wbr>Artifact<wbr>Name</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, a name specified in the build spec file overrides the artifact name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Packaging</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of build output artifact to create. If `type` is set to `S3`, valid values for this parameter are: `NONE` or `ZIP`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `type` is set to `S3`, this is the path to the output artifact
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">Artifact<wbr>Identifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Disabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The namespace to use in storing build artifacts. If `type` is set to `S3`, then valid values for this parameter are: `BUILD_ID` or `NONE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Override<wbr>Artifact<wbr>Name</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, a name specified in the build spec file overrides the artifact name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Packaging</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of build output artifact to create. If `type` is set to `S3`, valid values for this parameter are: `NONE` or `ZIP`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Path</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `type` is set to `S3`, this is the path to the output artifact
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">artifact<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption<wbr>Disabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The namespace to use in storing build artifacts. If `type` is set to `S3`, then valid values for this parameter are: `BUILD_ID` or `NONE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">override<wbr>Artifact<wbr>Name</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, a name specified in the build spec file overrides the artifact name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">packaging</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of build output artifact to create. If `type` is set to `S3`, valid values for this parameter are: `NONE` or `ZIP`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `type` is set to `S3`, this is the path to the output artifact
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">artifact<wbr>Identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption<wbr>Disabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace<wbr>Type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The namespace to use in storing build artifacts. If `type` is set to `S3`, then valid values for this parameter are: `BUILD_ID` or `NONE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">override<wbr>Artifact<wbr>Name</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, a name specified in the build spec file overrides the artifact name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">packaging</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of build output artifact to create. If `type` is set to `S3`, valid values for this parameter are: `NONE` or `ZIP`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">path</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `type` is set to `S3`, this is the path to the output artifact
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ProjectCache
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ProjectCache">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ProjectCache">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectCacheArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectCacheOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectCacheArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectCache.html">output</a> API doc for this type.
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
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Modes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies settings that AWS CodeBuild uses to store and reuse build dependencies. Valid values:  `LOCAL_SOURCE_CACHE`, `LOCAL_DOCKER_LAYER_CACHE`, and `LOCAL_CUSTOM_CACHE`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Modes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies settings that AWS CodeBuild uses to store and reuse build dependencies. Valid values:  `LOCAL_SOURCE_CACHE`, `LOCAL_DOCKER_LAYER_CACHE`, and `LOCAL_CUSTOM_CACHE`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">modes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies settings that AWS CodeBuild uses to store and reuse build dependencies. Valid values:  `LOCAL_SOURCE_CACHE`, `LOCAL_DOCKER_LAYER_CACHE`, and `LOCAL_CUSTOM_CACHE`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">modes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies settings that AWS CodeBuild uses to store and reuse build dependencies. Valid values:  `LOCAL_SOURCE_CACHE`, `LOCAL_DOCKER_LAYER_CACHE`, and `LOCAL_CUSTOM_CACHE`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ProjectEnvironment
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ProjectEnvironment">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ProjectEnvironment">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectEnvironmentArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectEnvironmentOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectEnvironmentArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectEnvironment.html">output</a> API doc for this type.
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
            <td class="align-top">Certificate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the S3 bucket, path prefix and object key that contains the PEM-encoded certificate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compute<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Information about the compute resources the build project will use. Available values for this parameter are: `BUILD_GENERAL1_SMALL`, `BUILD_GENERAL1_MEDIUM`, `BUILD_GENERAL1_LARGE` or `BUILD_GENERAL1_2XLARGE`. `BUILD_GENERAL1_SMALL` is only valid if `type` is set to `LINUX_CONTAINER`. When `type` is set to `LINUX_GPU_CONTAINER`, `compute_type` need to be `BUILD_GENERAL1_LARGE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment<wbr>Variables</td>
            <td class="align-top">
                
                <code><a href="#projectenvironmentenvironmentvariable">List&lt;Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Environment<wbr>Environment<wbr>Variable<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of environment variables to make available to builds for this build project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Docker image to use for this build project. Valid values include [Docker images provided by CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html) (e.g `aws/codebuild/standard:2.0`), [Docker Hub images](https://hub.docker.com/) (e.g. `nginx:latest`), and full Docker repository URIs such as those for ECR (e.g. `137112412989.dkr.ecr.us-west-2.amazonaws.com/amazonlinux:latest`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Pull<wbr>Credentials<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of credentials AWS CodeBuild uses to pull images in your build. Available values for this parameter are `CODEBUILD` or `SERVICE_ROLE`. When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials. Default to `CODEBUILD`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Privileged<wbr>Mode</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, enables running the Docker daemon inside a Docker container. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Registry<wbr>Credential</td>
            <td class="align-top">
                
                <code><a href="#projectenvironmentregistrycredential">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Environment<wbr>Registry<wbr>Credential<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about credentials for access to a private Docker registry. Registry Credential config blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">Certificate</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the S3 bucket, path prefix and object key that contains the PEM-encoded certificate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compute<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Information about the compute resources the build project will use. Available values for this parameter are: `BUILD_GENERAL1_SMALL`, `BUILD_GENERAL1_MEDIUM`, `BUILD_GENERAL1_LARGE` or `BUILD_GENERAL1_2XLARGE`. `BUILD_GENERAL1_SMALL` is only valid if `type` is set to `LINUX_CONTAINER`. When `type` is set to `LINUX_GPU_CONTAINER`, `compute_type` need to be `BUILD_GENERAL1_LARGE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment<wbr>Variables</td>
            <td class="align-top">
                
                <code><a href="#projectenvironmentenvironmentvariable">[]codebuild.<wbr>Project<wbr>Environment<wbr>Environment<wbr>Variable</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of environment variables to make available to builds for this build project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Docker image to use for this build project. Valid values include [Docker images provided by CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html) (e.g `aws/codebuild/standard:2.0`), [Docker Hub images](https://hub.docker.com/) (e.g. `nginx:latest`), and full Docker repository URIs such as those for ECR (e.g. `137112412989.dkr.ecr.us-west-2.amazonaws.com/amazonlinux:latest`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Pull<wbr>Credentials<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of credentials AWS CodeBuild uses to pull images in your build. Available values for this parameter are `CODEBUILD` or `SERVICE_ROLE`. When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials. Default to `CODEBUILD`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Privileged<wbr>Mode</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, enables running the Docker daemon inside a Docker container. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Registry<wbr>Credential</td>
            <td class="align-top">
                
                <code><a href="#projectenvironmentregistrycredential">*codebuild.<wbr>Project<wbr>Environment<wbr>Registry<wbr>Credential</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about credentials for access to a private Docker registry. Registry Credential config blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">certificate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the S3 bucket, path prefix and object key that contains the PEM-encoded certificate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compute<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Information about the compute resources the build project will use. Available values for this parameter are: `BUILD_GENERAL1_SMALL`, `BUILD_GENERAL1_MEDIUM`, `BUILD_GENERAL1_LARGE` or `BUILD_GENERAL1_2XLARGE`. `BUILD_GENERAL1_SMALL` is only valid if `type` is set to `LINUX_CONTAINER`. When `type` is set to `LINUX_GPU_CONTAINER`, `compute_type` need to be `BUILD_GENERAL1_LARGE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment<wbr>Variables</td>
            <td class="align-top">
                
                <code><a href="#projectenvironmentenvironmentvariable">codebuild.<wbr>Project<wbr>Environment<wbr>Environment<wbr>Variable[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of environment variables to make available to builds for this build project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Docker image to use for this build project. Valid values include [Docker images provided by CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html) (e.g `aws/codebuild/standard:2.0`), [Docker Hub images](https://hub.docker.com/) (e.g. `nginx:latest`), and full Docker repository URIs such as those for ECR (e.g. `137112412989.dkr.ecr.us-west-2.amazonaws.com/amazonlinux:latest`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image<wbr>Pull<wbr>Credentials<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of credentials AWS CodeBuild uses to pull images in your build. Available values for this parameter are `CODEBUILD` or `SERVICE_ROLE`. When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials. Default to `CODEBUILD`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">privileged<wbr>Mode</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, enables running the Docker daemon inside a Docker container. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">registry<wbr>Credential</td>
            <td class="align-top">
                
                <code><a href="#projectenvironmentregistrycredential">codebuild.<wbr>Project<wbr>Environment<wbr>Registry<wbr>Credential?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about credentials for access to a private Docker registry. Registry Credential config blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">certificate</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the S3 bucket, path prefix and object key that contains the PEM-encoded certificate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compute<wbr>Type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Information about the compute resources the build project will use. Available values for this parameter are: `BUILD_GENERAL1_SMALL`, `BUILD_GENERAL1_MEDIUM`, `BUILD_GENERAL1_LARGE` or `BUILD_GENERAL1_2XLARGE`. `BUILD_GENERAL1_SMALL` is only valid if `type` is set to `LINUX_CONTAINER`. When `type` is set to `LINUX_GPU_CONTAINER`, `compute_type` need to be `BUILD_GENERAL1_LARGE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment<wbr>Variables</td>
            <td class="align-top">
                
                <code><a href="#projectenvironmentenvironmentvariable">List[Project<wbr>Environment<wbr>Environment<wbr>Variable]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of environment variables to make available to builds for this build project.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Docker image to use for this build project. Valid values include [Docker images provided by CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html) (e.g `aws/codebuild/standard:2.0`), [Docker Hub images](https://hub.docker.com/) (e.g. `nginx:latest`), and full Docker repository URIs such as those for ECR (e.g. `137112412989.dkr.ecr.us-west-2.amazonaws.com/amazonlinux:latest`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image<wbr>Pull<wbr>Credentials<wbr>Type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of credentials AWS CodeBuild uses to pull images in your build. Available values for this parameter are `CODEBUILD` or `SERVICE_ROLE`. When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials. Default to `CODEBUILD`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">privileged<wbr>Mode</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, enables running the Docker daemon inside a Docker container. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">registry<wbr>Credential</td>
            <td class="align-top">
                
                <code><a href="#projectenvironmentregistrycredential">Dict[Project<wbr>Environment<wbr>Registry<wbr>Credential]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about credentials for access to a private Docker registry. Registry Credential config blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ProjectEnvironmentEnvironmentVariable
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ProjectEnvironmentEnvironmentVariable">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ProjectEnvironmentEnvironmentVariable">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectEnvironmentEnvironmentVariableArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectEnvironmentEnvironmentVariableOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectEnvironmentEnvironmentVariableArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectEnvironmentEnvironmentVariable.html">output</a> API doc for this type.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The environment variable&#39;s value.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The environment variable&#39;s value.
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The environment variable&#39;s value.
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The environment variable&#39;s value.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ProjectEnvironmentRegistryCredential
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ProjectEnvironmentRegistryCredential">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ProjectEnvironmentRegistryCredential">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectEnvironmentRegistryCredentialArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectEnvironmentRegistryCredentialOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectEnvironmentRegistryCredentialArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectEnvironmentRegistryCredential.html">output</a> API doc for this type.
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
            <td class="align-top">Credential</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Credential<wbr>Provider</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.
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
            <td class="align-top">Credential</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Credential<wbr>Provider</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.
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
            <td class="align-top">credential</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">credential<wbr>Provider</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.
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
            <td class="align-top">credential</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">credential<wbr>Provider</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ProjectLogsConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ProjectLogsConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ProjectLogsConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectLogsConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectLogsConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectLogsConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectLogsConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Cloudwatch<wbr>Logs</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfigcloudwatchlogs">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Logs<wbr>Config<wbr>Cloudwatch<wbr>Logs<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to store logs to CloudWatch
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Logs</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfigs3logs">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Logs<wbr>Config<wbr>S3Logs<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to store logs to S3.
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
            <td class="align-top">Cloudwatch<wbr>Logs</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfigcloudwatchlogs">*codebuild.<wbr>Project<wbr>Logs<wbr>Config<wbr>Cloudwatch<wbr>Logs</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to store logs to CloudWatch
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Logs</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfigs3logs">*codebuild.<wbr>Project<wbr>Logs<wbr>Config<wbr>S3Logs</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to store logs to S3.
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
            <td class="align-top">cloudwatch<wbr>Logs</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfigcloudwatchlogs">codebuild.<wbr>Project<wbr>Logs<wbr>Config<wbr>Cloudwatch<wbr>Logs?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to store logs to CloudWatch
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Logs</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfigs3logs">codebuild.<wbr>Project<wbr>Logs<wbr>Config<wbr>S3Logs?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to store logs to S3.
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
            <td class="align-top">cloudwatch<wbr>Logs</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfigcloudwatchlogs">Dict[Project<wbr>Logs<wbr>Config<wbr>Cloudwatch<wbr>Logs]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to store logs to CloudWatch
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Logs</td>
            <td class="align-top">
                
                <code><a href="#projectlogsconfigs3logs">Dict[Project<wbr>Logs<wbr>Config<wbr>S3Logs]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration for the builds to store logs to S3.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ProjectLogsConfigCloudwatchLogs
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ProjectLogsConfigCloudwatchLogs">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ProjectLogsConfigCloudwatchLogs">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectLogsConfigCloudwatchLogsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectLogsConfigCloudwatchLogsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectLogsConfigCloudwatchLogsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectLogsConfigCloudwatchLogs.html">output</a> API doc for this type.
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
            <td class="align-top">Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The group name of the logs in CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Current status of logs in S3 for a build project. Valid values: `ENABLED`, `DISABLED`. Defaults to `DISABLED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The stream name of the logs in CloudWatch Logs.
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
            <td class="align-top">Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The group name of the logs in CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Current status of logs in S3 for a build project. Valid values: `ENABLED`, `DISABLED`. Defaults to `DISABLED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The stream name of the logs in CloudWatch Logs.
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
            <td class="align-top">group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The group name of the logs in CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Current status of logs in S3 for a build project. Valid values: `ENABLED`, `DISABLED`. Defaults to `DISABLED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The stream name of the logs in CloudWatch Logs.
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
            <td class="align-top">group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The group name of the logs in CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Current status of logs in S3 for a build project. Valid values: `ENABLED`, `DISABLED`. Defaults to `DISABLED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream<wbr>Name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The stream name of the logs in CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ProjectLogsConfigS3Logs
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ProjectLogsConfigS3Logs">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ProjectLogsConfigS3Logs">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectLogsConfigS3LogsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectLogsConfigS3LogsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectLogsConfigS3LogsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectLogsConfigS3Logs.html">output</a> API doc for this type.
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
            <td class="align-top">Encryption<wbr>Disabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Current status of logs in S3 for a build project. Valid values: `ENABLED`, `DISABLED`. Defaults to `DISABLED`.
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
            <td class="align-top">Encryption<wbr>Disabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Current status of logs in S3 for a build project. Valid values: `ENABLED`, `DISABLED`. Defaults to `DISABLED`.
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
            <td class="align-top">encryption<wbr>Disabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Current status of logs in S3 for a build project. Valid values: `ENABLED`, `DISABLED`. Defaults to `DISABLED`.
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
            <td class="align-top">encryption<wbr>Disabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Current status of logs in S3 for a build project. Valid values: `ENABLED`, `DISABLED`. Defaults to `DISABLED`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ProjectSecondaryArtifact
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ProjectSecondaryArtifact">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ProjectSecondaryArtifact">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectSecondaryArtifactArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectSecondaryArtifactOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectSecondaryArtifactArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectSecondaryArtifact.html">output</a> API doc for this type.
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
            <td class="align-top">Artifact<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Disabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The namespace to use in storing build artifacts. If `type` is set to `S3`, then valid values for this parameter are: `BUILD_ID` or `NONE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Override<wbr>Artifact<wbr>Name</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, a name specified in the build spec file overrides the artifact name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Packaging</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of build output artifact to create. If `type` is set to `S3`, valid values for this parameter are: `NONE` or `ZIP`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `type` is set to `S3`, this is the path to the output artifact
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">Artifact<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Disabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The namespace to use in storing build artifacts. If `type` is set to `S3`, then valid values for this parameter are: `BUILD_ID` or `NONE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Override<wbr>Artifact<wbr>Name</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, a name specified in the build spec file overrides the artifact name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Packaging</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of build output artifact to create. If `type` is set to `S3`, valid values for this parameter are: `NONE` or `ZIP`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Path</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `type` is set to `S3`, this is the path to the output artifact
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">artifact<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption<wbr>Disabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The namespace to use in storing build artifacts. If `type` is set to `S3`, then valid values for this parameter are: `BUILD_ID` or `NONE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">override<wbr>Artifact<wbr>Name</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, a name specified in the build spec file overrides the artifact name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">packaging</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of build output artifact to create. If `type` is set to `S3`, valid values for this parameter are: `NONE` or `ZIP`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `type` is set to `S3`, this is the path to the output artifact
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">artifact<wbr>Identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption<wbr>Disabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace<wbr>Type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The namespace to use in storing build artifacts. If `type` is set to `S3`, then valid values for this parameter are: `BUILD_ID` or `NONE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">override<wbr>Artifact<wbr>Name</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If set to true, a name specified in the build spec file overrides the artifact name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">packaging</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of build output artifact to create. If `type` is set to `S3`, valid values for this parameter are: `NONE` or `ZIP`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">path</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `type` is set to `S3`, this is the path to the output artifact
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ProjectSecondarySource
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ProjectSecondarySource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ProjectSecondarySource">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectSecondarySourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectSecondarySourceOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectSecondarySourceArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectSecondarySource.html">output</a> API doc for this type.
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
            <td class="align-top">Auths</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysourceauth">List&lt;Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Secondary<wbr>Source<wbr>Auth<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buildspec</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The build spec declaration to use for this build project&#39;s related builds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Git<wbr>Clone<wbr>Depth</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Truncate git history to this many commits.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Git<wbr>Submodules<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysourcegitsubmodulesconfig">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Secondary<wbr>Source<wbr>Git<wbr>Submodules<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the `type` is `CODECOMMIT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Insecure<wbr>Ssl</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Ignore SSL warnings when connecting to source control.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Report<wbr>Build<wbr>Status</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to report the status of a build&#39;s start and finish to your source provider. This option is only valid when your source provider is `GITHUB`, `BITBUCKET`, or `GITHUB_ENTERPRISE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The source identifier. Source data will be put inside a folder named as this parameter inside AWS CodeBuild source directory
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">Auths</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysourceauth">[]codebuild.<wbr>Project<wbr>Secondary<wbr>Source<wbr>Auth</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buildspec</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The build spec declaration to use for this build project&#39;s related builds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Git<wbr>Clone<wbr>Depth</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Truncate git history to this many commits.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Git<wbr>Submodules<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysourcegitsubmodulesconfig">*codebuild.<wbr>Project<wbr>Secondary<wbr>Source<wbr>Git<wbr>Submodules<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the `type` is `CODECOMMIT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Insecure<wbr>Ssl</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Ignore SSL warnings when connecting to source control.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Report<wbr>Build<wbr>Status</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to report the status of a build&#39;s start and finish to your source provider. This option is only valid when your source provider is `GITHUB`, `BITBUCKET`, or `GITHUB_ENTERPRISE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The source identifier. Source data will be put inside a folder named as this parameter inside AWS CodeBuild source directory
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">auths</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysourceauth">codebuild.<wbr>Project<wbr>Secondary<wbr>Source<wbr>Auth[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buildspec</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The build spec declaration to use for this build project&#39;s related builds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">git<wbr>Clone<wbr>Depth</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Truncate git history to this many commits.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">git<wbr>Submodules<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysourcegitsubmodulesconfig">codebuild.<wbr>Project<wbr>Secondary<wbr>Source<wbr>Git<wbr>Submodules<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the `type` is `CODECOMMIT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">insecure<wbr>Ssl</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Ignore SSL warnings when connecting to source control.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">report<wbr>Build<wbr>Status</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to report the status of a build&#39;s start and finish to your source provider. This option is only valid when your source provider is `GITHUB`, `BITBUCKET`, or `GITHUB_ENTERPRISE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The source identifier. Source data will be put inside a folder named as this parameter inside AWS CodeBuild source directory
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">auths</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysourceauth">List[Project<wbr>Secondary<wbr>Source<wbr>Auth]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buildspec</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The build spec declaration to use for this build project&#39;s related builds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">git<wbr>Clone<wbr>Depth</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Truncate git history to this many commits.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">git<wbr>Submodules<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectsecondarysourcegitsubmodulesconfig">Dict[Project<wbr>Secondary<wbr>Source<wbr>Git<wbr>Submodules<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the `type` is `CODECOMMIT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">insecure<wbr>Ssl</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Ignore SSL warnings when connecting to source control.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">report<wbr>Build<wbr>Status</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to report the status of a build&#39;s start and finish to your source provider. This option is only valid when your source provider is `GITHUB`, `BITBUCKET`, or `GITHUB_ENTERPRISE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The source identifier. Source data will be put inside a folder named as this parameter inside AWS CodeBuild source directory
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ProjectSecondarySourceAuth
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ProjectSecondarySourceAuth">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ProjectSecondarySourceAuth">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectSecondarySourceAuthArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectSecondarySourceAuthOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectSecondarySourceAuthArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectSecondarySourceAuth.html">output</a> API doc for this type.
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
            <td class="align-top">Resource</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The resource value that applies to the specified authorization type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">Resource</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The resource value that applies to the specified authorization type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">resource</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The resource value that applies to the specified authorization type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">resource</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The resource value that applies to the specified authorization type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ProjectSecondarySourceGitSubmodulesConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ProjectSecondarySourceGitSubmodulesConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ProjectSecondarySourceGitSubmodulesConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectSecondarySourceGitSubmodulesConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectSecondarySourceGitSubmodulesConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectSecondarySourceGitSubmodulesConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectSecondarySourceGitSubmodulesConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Fetch<wbr>Submodules</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
If set to true, fetches Git submodules for the AWS CodeBuild build project.
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
            <td class="align-top">Fetch<wbr>Submodules</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
If set to true, fetches Git submodules for the AWS CodeBuild build project.
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
            <td class="align-top">fetch<wbr>Submodules</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
If set to true, fetches Git submodules for the AWS CodeBuild build project.
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
            <td class="align-top">fetch<wbr>Submodules</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
If set to true, fetches Git submodules for the AWS CodeBuild build project.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ProjectSource
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ProjectSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ProjectSource">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectSourceOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectSourceArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectSource.html">output</a> API doc for this type.
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
            <td class="align-top">Auths</td>
            <td class="align-top">
                
                <code><a href="#projectsourceauth">List&lt;Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Source<wbr>Auth<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buildspec</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The build spec declaration to use for this build project&#39;s related builds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Git<wbr>Clone<wbr>Depth</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Truncate git history to this many commits.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Git<wbr>Submodules<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectsourcegitsubmodulesconfig">Pulumi.<wbr>Aws.<wbr>Codebuild.<wbr>Project<wbr>Source<wbr>Git<wbr>Submodules<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the `type` is `CODECOMMIT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Insecure<wbr>Ssl</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Ignore SSL warnings when connecting to source control.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Report<wbr>Build<wbr>Status</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to report the status of a build&#39;s start and finish to your source provider. This option is only valid when your source provider is `GITHUB`, `BITBUCKET`, or `GITHUB_ENTERPRISE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">Auths</td>
            <td class="align-top">
                
                <code><a href="#projectsourceauth">[]codebuild.<wbr>Project<wbr>Source<wbr>Auth</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buildspec</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The build spec declaration to use for this build project&#39;s related builds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Git<wbr>Clone<wbr>Depth</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Truncate git history to this many commits.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Git<wbr>Submodules<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectsourcegitsubmodulesconfig">*codebuild.<wbr>Project<wbr>Source<wbr>Git<wbr>Submodules<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the `type` is `CODECOMMIT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Insecure<wbr>Ssl</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Ignore SSL warnings when connecting to source control.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Report<wbr>Build<wbr>Status</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to report the status of a build&#39;s start and finish to your source provider. This option is only valid when your source provider is `GITHUB`, `BITBUCKET`, or `GITHUB_ENTERPRISE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">auths</td>
            <td class="align-top">
                
                <code><a href="#projectsourceauth">codebuild.<wbr>Project<wbr>Source<wbr>Auth[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buildspec</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The build spec declaration to use for this build project&#39;s related builds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">git<wbr>Clone<wbr>Depth</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Truncate git history to this many commits.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">git<wbr>Submodules<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectsourcegitsubmodulesconfig">codebuild.<wbr>Project<wbr>Source<wbr>Git<wbr>Submodules<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the `type` is `CODECOMMIT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">insecure<wbr>Ssl</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Ignore SSL warnings when connecting to source control.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">report<wbr>Build<wbr>Status</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to report the status of a build&#39;s start and finish to your source provider. This option is only valid when your source provider is `GITHUB`, `BITBUCKET`, or `GITHUB_ENTERPRISE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">auths</td>
            <td class="align-top">
                
                <code><a href="#projectsourceauth">List[Project<wbr>Source<wbr>Auth]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buildspec</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The build spec declaration to use for this build project&#39;s related builds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">git<wbr>Clone<wbr>Depth</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Truncate git history to this many commits.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">git<wbr>Submodules<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#projectsourcegitsubmodulesconfig">Dict[Project<wbr>Source<wbr>Git<wbr>Submodules<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the `type` is `CODECOMMIT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">insecure<wbr>Ssl</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Ignore SSL warnings when connecting to source control.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the source code from git or s3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">report<wbr>Build<wbr>Status</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to report the status of a build&#39;s start and finish to your source provider. This option is only valid when your source provider is `GITHUB`, `BITBUCKET`, or `GITHUB_ENTERPRISE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ProjectSourceAuth
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ProjectSourceAuth">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ProjectSourceAuth">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectSourceAuthArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectSourceAuthOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectSourceAuthArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectSourceAuth.html">output</a> API doc for this type.
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
            <td class="align-top">Resource</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The resource value that applies to the specified authorization type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">Resource</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The resource value that applies to the specified authorization type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">resource</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The resource value that applies to the specified authorization type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
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
            <td class="align-top">resource</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The resource value that applies to the specified authorization type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ProjectSourceGitSubmodulesConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ProjectSourceGitSubmodulesConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ProjectSourceGitSubmodulesConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectSourceGitSubmodulesConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectSourceGitSubmodulesConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectSourceGitSubmodulesConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectSourceGitSubmodulesConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Fetch<wbr>Submodules</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
If set to true, fetches Git submodules for the AWS CodeBuild build project.
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
            <td class="align-top">Fetch<wbr>Submodules</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
If set to true, fetches Git submodules for the AWS CodeBuild build project.
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
            <td class="align-top">fetch<wbr>Submodules</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
If set to true, fetches Git submodules for the AWS CodeBuild build project.
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
            <td class="align-top">fetch<wbr>Submodules</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
If set to true, fetches Git submodules for the AWS CodeBuild build project.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ProjectVpcConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ProjectVpcConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ProjectVpcConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectVpcConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codebuild?tab=doc#ProjectVpcConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectVpcConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codebuild.ProjectVpcConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The security group IDs to assign to running builds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnets</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The subnet IDs within which to run builds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the VPC within which to run builds.
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
            <td class="align-top">Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The security group IDs to assign to running builds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnets</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The subnet IDs within which to run builds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the VPC within which to run builds.
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
            <td class="align-top">security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The security group IDs to assign to running builds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnets</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The subnet IDs within which to run builds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the VPC within which to run builds.
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
            <td class="align-top">security_<wbr>group_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The security group IDs to assign to running builds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnets</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The subnet IDs within which to run builds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the VPC within which to run builds.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







