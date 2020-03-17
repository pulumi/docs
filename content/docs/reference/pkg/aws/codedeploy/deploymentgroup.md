
---
title: "DeploymentGroup"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides a CodeDeploy Deployment Group for a CodeDeploy Application

> **NOTE on blue/green deployments:** When using `green_fleet_provisioning_option` with the `COPY_AUTO_SCALING_GROUP` action, CodeDeploy will create a new ASG with a different name. This ASG is _not_ managed by this provider and will conflict with existing configuration and state. You may want to use a different approach to managing deployments that involve multiple ASG, such as `DISCOVER_EXISTING` with separate blue and green ASG.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleRole = new aws.iam.Role("example", {
    assumeRolePolicy: `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "codedeploy.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
`,
});
const aWSCodeDeployRole = new aws.iam.RolePolicyAttachment("AWSCodeDeployRole", {
    policyArn: "arn:aws:iam::aws:policy/service-role/AWSCodeDeployRole",
    role: exampleRole.name,
});
const exampleApplication = new aws.codedeploy.Application("example", {});
const exampleTopic = new aws.sns.Topic("example", {});
const exampleDeploymentGroup = new aws.codedeploy.DeploymentGroup("example", {
    alarmConfiguration: {
        alarms: ["my-alarm-name"],
        enabled: true,
    },
    appName: exampleApplication.name,
    autoRollbackConfiguration: {
        enabled: true,
        events: ["DEPLOYMENT_FAILURE"],
    },
    deploymentGroupName: "example-group",
    ec2TagSets: [{
        ec2TagFilters: [
            {
                key: "filterkey1",
                type: "KEY_AND_VALUE",
                value: "filtervalue",
            },
            {
                key: "filterkey2",
                type: "KEY_AND_VALUE",
                value: "filtervalue",
            },
        ],
    }],
    serviceRoleArn: exampleRole.arn,
    triggerConfigurations: [{
        triggerEvents: ["DeploymentFailure"],
        triggerName: "example-trigger",
        triggerTargetArn: exampleTopic.arn,
    }],
});
```

### Blue Green Deployments with ECS

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleApplication = new aws.codedeploy.Application("example", {
    computePlatform: "ECS",
});
const exampleDeploymentGroup = new aws.codedeploy.DeploymentGroup("example", {
    appName: exampleApplication.name,
    autoRollbackConfiguration: {
        enabled: true,
        events: ["DEPLOYMENT_FAILURE"],
    },
    blueGreenDeploymentConfig: {
        deploymentReadyOption: {
            actionOnTimeout: "CONTINUE_DEPLOYMENT",
        },
        terminateBlueInstancesOnDeploymentSuccess: {
            action: "TERMINATE",
            terminationWaitTimeInMinutes: 5,
        },
    },
    deploymentConfigName: "CodeDeployDefault.ECSAllAtOnce",
    deploymentGroupName: "example",
    deploymentStyle: {
        deploymentOption: "WITH_TRAFFIC_CONTROL",
        deploymentType: "BLUE_GREEN",
    },
    ecsService: {
        clusterName: aws_ecs_cluster_example.name,
        serviceName: aws_ecs_service_example.name,
    },
    loadBalancerInfo: {
        targetGroupPairInfo: {
            prodTrafficRoute: {
                listenerArns: [aws_lb_listener_example.arn],
            },
            targetGroups: [
                {
                    name: aws_lb_target_group_blue.name,
                },
                {
                    name: aws_lb_target_group_green.name,
                },
            ],
        },
    },
    serviceRoleArn: aws_iam_role_example.arn,
});
```

### Blue Green Deployments with Servers and Classic ELB

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleApplication = new aws.codedeploy.Application("example", {});
const exampleDeploymentGroup = new aws.codedeploy.DeploymentGroup("example", {
    appName: exampleApplication.name,
    blueGreenDeploymentConfig: {
        deploymentReadyOption: {
            actionOnTimeout: "STOP_DEPLOYMENT",
            waitTimeInMinutes: 60,
        },
        greenFleetProvisioningOption: {
            action: "DISCOVER_EXISTING",
        },
        terminateBlueInstancesOnDeploymentSuccess: {
            action: "KEEP_ALIVE",
        },
    },
    deploymentGroupName: "example-group",
    deploymentStyle: {
        deploymentOption: "WITH_TRAFFIC_CONTROL",
        deploymentType: "BLUE_GREEN",
    },
    loadBalancerInfo: {
        elbInfos: [{
            name: aws_elb_example.name,
        }],
    },
    serviceRoleArn: aws_iam_role_example.arn,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codedeploy_deployment_group.html.markdown.



## Create a DeploymentGroup Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/codedeploy/#DeploymentGroup">DeploymentGroup</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/codedeploy/#DeploymentGroupArgs">DeploymentGroupArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">DeploymentGroup</span><span class="p">(resource_name, opts=None, </span>alarm_configuration=None<span class="p">, </span>app_name=None<span class="p">, </span>auto_rollback_configuration=None<span class="p">, </span>autoscaling_groups=None<span class="p">, </span>blue_green_deployment_config=None<span class="p">, </span>deployment_config_name=None<span class="p">, </span>deployment_group_name=None<span class="p">, </span>deployment_style=None<span class="p">, </span>ec2_tag_filters=None<span class="p">, </span>ec2_tag_sets=None<span class="p">, </span>ecs_service=None<span class="p">, </span>load_balancer_info=None<span class="p">, </span>on_premises_instance_tag_filters=None<span class="p">, </span>service_role_arn=None<span class="p">, </span>trigger_configurations=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDeploymentGroup<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupArgs">DeploymentGroupArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroup">DeploymentGroup</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroup.html">DeploymentGroup</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupArgs.html">DeploymentGroupArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a DeploymentGroup resource with the given unique name, arguments, and options.

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
            <td class="align-top">Alarm<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupalarmconfiguration">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Alarm<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of alarms associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">App<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the application.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Rollback<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupautorollbackconfiguration">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Auto<wbr>Rollback<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Autoscaling groups associated with the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Blue<wbr>Green<wbr>Deployment<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfig">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the blue/green deployment options for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the group&#39;s deployment config. The default is &#34;CodeDeployDefault.OneAtATime&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Style</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupdeploymentstyle">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Deployment<wbr>Style<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ec2Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagfilter">List&lt;Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Filter<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tag filters associated with the deployment group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ec2Tag<wbr>Sets</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagset">List&lt;Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Set<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ecs<wbr>Service</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupecsservice">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Ecs<wbr>Service<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of the ECS services for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancer<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfo">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Single configuration block of the load balancer to use in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">On<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouponpremisesinstancetagfilter">List&lt;Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>On<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filter<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
On premise tag filters associated with the group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The service role ARN that allows deployments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Trigger<wbr>Configurations</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouptriggerconfiguration">List&lt;Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Trigger<wbr>Configuration<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of the triggers for the deployment group (documented below).
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
            <td class="align-top">Alarm<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupalarmconfiguration">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Alarm<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of alarms associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">App<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the application.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Rollback<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupautorollbackconfiguration">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Auto<wbr>Rollback<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Autoscaling groups associated with the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Blue<wbr>Green<wbr>Deployment<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfig">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the blue/green deployment options for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the group&#39;s deployment config. The default is &#34;CodeDeployDefault.OneAtATime&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Style</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupdeploymentstyle">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Deployment<wbr>Style</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ec2Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagfilter">[]codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Filter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tag filters associated with the deployment group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ec2Tag<wbr>Sets</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagset">[]codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Set</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ecs<wbr>Service</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupecsservice">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Ecs<wbr>Service</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of the ECS services for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancer<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfo">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Single configuration block of the load balancer to use in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">On<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouponpremisesinstancetagfilter">[]codedeploy.<wbr>Deployment<wbr>Group<wbr>On<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
On premise tag filters associated with the group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The service role ARN that allows deployments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Trigger<wbr>Configurations</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouptriggerconfiguration">[]codedeploy.<wbr>Deployment<wbr>Group<wbr>Trigger<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of the triggers for the deployment group (documented below).
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
            <td class="align-top">alarm<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupalarmconfiguration">codedeploy.<wbr>Deployment<wbr>Group<wbr>Alarm<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of alarms associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">app<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the application.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Rollback<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupautorollbackconfiguration">codedeploy.<wbr>Deployment<wbr>Group<wbr>Auto<wbr>Rollback<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Autoscaling groups associated with the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">blue<wbr>Green<wbr>Deployment<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfig">codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the blue/green deployment options for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the group&#39;s deployment config. The default is &#34;CodeDeployDefault.OneAtATime&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Style</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupdeploymentstyle">codedeploy.<wbr>Deployment<wbr>Group<wbr>Deployment<wbr>Style?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ec2Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagfilter">codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Filter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tag filters associated with the deployment group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ec2Tag<wbr>Sets</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagset">codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Set[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ecs<wbr>Service</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupecsservice">codedeploy.<wbr>Deployment<wbr>Group<wbr>Ecs<wbr>Service?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of the ECS services for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load<wbr>Balancer<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfo">codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Single configuration block of the load balancer to use in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">on<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouponpremisesinstancetagfilter">codedeploy.<wbr>Deployment<wbr>Group<wbr>On<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
On premise tag filters associated with the group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The service role ARN that allows deployments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">trigger<wbr>Configurations</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouptriggerconfiguration">codedeploy.<wbr>Deployment<wbr>Group<wbr>Trigger<wbr>Configuration[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of the triggers for the deployment group (documented below).
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
            <td class="align-top">alarm_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupalarmconfiguration">Dict[deployment_<wbr>group_<wbr>alarm_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of alarms associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">app_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the application.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>rollback_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupautorollbackconfiguration">Dict[deployment_<wbr>group_<wbr>auto_<wbr>rollback_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling_<wbr>groups</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Autoscaling groups associated with the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">blue_<wbr>green_<wbr>deployment_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfig">Dict[deployment_<wbr>group_<wbr>blue_<wbr>green_<wbr>deployment_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the blue/green deployment options for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>config_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the group&#39;s deployment config. The default is &#34;CodeDeployDefault.OneAtATime&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>style</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupdeploymentstyle">Dict[deployment_<wbr>group_<wbr>deployment_<wbr>style]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ec2_<wbr>tag_<wbr>filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagfilter">List[deployment_<wbr>group_<wbr>ec2_<wbr>tag_<wbr>filter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tag filters associated with the deployment group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ec2_<wbr>tag_<wbr>sets</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagset">List[deployment_<wbr>group_<wbr>ec2_<wbr>tag_<wbr>set]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ecs_<wbr>service</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupecsservice">Dict[deployment_<wbr>group_<wbr>ecs_<wbr>service]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of the ECS services for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load_<wbr>balancer_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfo">Dict[deployment_<wbr>group_<wbr>load_<wbr>balancer_<wbr>info]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Single configuration block of the load balancer to use in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">on_<wbr>premises_<wbr>instance_<wbr>tag_<wbr>filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouponpremisesinstancetagfilter">List[deployment_<wbr>group_<wbr>on_<wbr>premises_<wbr>instance_<wbr>tag_<wbr>filter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
On premise tag filters associated with the group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The service role ARN that allows deployments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">trigger_<wbr>configurations</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouptriggerconfiguration">List[deployment_<wbr>group_<wbr>trigger_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of the triggers for the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## DeploymentGroup Output Properties

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
            <td class="align-top">Alarm<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupalarmconfiguration">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Alarm<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block of alarms associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">App<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the application.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Rollback<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupautorollbackconfiguration">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Auto<wbr>Rollback<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} Autoscaling groups associated with the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Blue<wbr>Green<wbr>Deployment<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfig">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block of the blue/green deployment options for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the group&#39;s deployment config. The default is &#34;CodeDeployDefault.OneAtATime&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Style</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupdeploymentstyle">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Deployment<wbr>Style?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ec2Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagfilter">List&lt;Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Filter&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} Tag filters associated with the deployment group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ec2Tag<wbr>Sets</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagset">List&lt;Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Set&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ecs<wbr>Service</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupecsservice">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Ecs<wbr>Service?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) of the ECS services for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancer<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfo">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} Single configuration block of the load balancer to use in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">On<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouponpremisesinstancetagfilter">List&lt;Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>On<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filter&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} On premise tag filters associated with the group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The service role ARN that allows deployments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Trigger<wbr>Configurations</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouptriggerconfiguration">List&lt;Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Trigger<wbr>Configuration&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) of the triggers for the deployment group (documented below).
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
            <td class="align-top">Alarm<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupalarmconfiguration">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Alarm<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block of alarms associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">App<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the application.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Rollback<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupautorollbackconfiguration">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Auto<wbr>Rollback<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} Autoscaling groups associated with the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Blue<wbr>Green<wbr>Deployment<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfig">codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block of the blue/green deployment options for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the group&#39;s deployment config. The default is &#34;CodeDeployDefault.OneAtATime&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Style</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupdeploymentstyle">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Deployment<wbr>Style</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ec2Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagfilter">[]codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Filter</a></code>
            </td>
            <td class="align-top">{{% md %}} Tag filters associated with the deployment group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ec2Tag<wbr>Sets</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagset">[]codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Set</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ecs<wbr>Service</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupecsservice">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Ecs<wbr>Service</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) of the ECS services for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancer<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfo">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} Single configuration block of the load balancer to use in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">On<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouponpremisesinstancetagfilter">[]codedeploy.<wbr>Deployment<wbr>Group<wbr>On<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filter</a></code>
            </td>
            <td class="align-top">{{% md %}} On premise tag filters associated with the group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The service role ARN that allows deployments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Trigger<wbr>Configurations</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouptriggerconfiguration">[]codedeploy.<wbr>Deployment<wbr>Group<wbr>Trigger<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) of the triggers for the deployment group (documented below).
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
            <td class="align-top">alarm<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupalarmconfiguration">codedeploy.<wbr>Deployment<wbr>Group<wbr>Alarm<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block of alarms associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">app<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the application.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Rollback<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupautorollbackconfiguration">codedeploy.<wbr>Deployment<wbr>Group<wbr>Auto<wbr>Rollback<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} Autoscaling groups associated with the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">blue<wbr>Green<wbr>Deployment<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfig">codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block of the blue/green deployment options for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the group&#39;s deployment config. The default is &#34;CodeDeployDefault.OneAtATime&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Style</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupdeploymentstyle">codedeploy.<wbr>Deployment<wbr>Group<wbr>Deployment<wbr>Style?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ec2Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagfilter">codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Filter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} Tag filters associated with the deployment group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ec2Tag<wbr>Sets</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagset">codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Set[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ecs<wbr>Service</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupecsservice">codedeploy.<wbr>Deployment<wbr>Group<wbr>Ecs<wbr>Service?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) of the ECS services for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load<wbr>Balancer<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfo">codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} Single configuration block of the load balancer to use in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">on<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouponpremisesinstancetagfilter">codedeploy.<wbr>Deployment<wbr>Group<wbr>On<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} On premise tag filters associated with the group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The service role ARN that allows deployments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">trigger<wbr>Configurations</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouptriggerconfiguration">codedeploy.<wbr>Deployment<wbr>Group<wbr>Trigger<wbr>Configuration[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) of the triggers for the deployment group (documented below).
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
            <td class="align-top">alarm_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupalarmconfiguration">Dict[deployment_<wbr>group_<wbr>alarm_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block of alarms associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">app_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the application.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>rollback_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupautorollbackconfiguration">Dict[deployment_<wbr>group_<wbr>auto_<wbr>rollback_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling_<wbr>groups</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} Autoscaling groups associated with the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">blue_<wbr>green_<wbr>deployment_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfig">Dict[deployment_<wbr>group_<wbr>blue_<wbr>green_<wbr>deployment_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block of the blue/green deployment options for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>config_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the group&#39;s deployment config. The default is &#34;CodeDeployDefault.OneAtATime&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>style</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupdeploymentstyle">Dict[deployment_<wbr>group_<wbr>deployment_<wbr>style]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ec2_<wbr>tag_<wbr>filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagfilter">List[deployment_<wbr>group_<wbr>ec2_<wbr>tag_<wbr>filter]</a></code>
            </td>
            <td class="align-top">{{% md %}} Tag filters associated with the deployment group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ec2_<wbr>tag_<wbr>sets</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagset">List[deployment_<wbr>group_<wbr>ec2_<wbr>tag_<wbr>set]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ecs_<wbr>service</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupecsservice">Dict[deployment_<wbr>group_<wbr>ecs_<wbr>service]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) of the ECS services for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load_<wbr>balancer_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfo">Dict[deployment_<wbr>group_<wbr>load_<wbr>balancer_<wbr>info]</a></code>
            </td>
            <td class="align-top">{{% md %}} Single configuration block of the load balancer to use in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">on_<wbr>premises_<wbr>instance_<wbr>tag_<wbr>filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouponpremisesinstancetagfilter">List[deployment_<wbr>group_<wbr>on_<wbr>premises_<wbr>instance_<wbr>tag_<wbr>filter]</a></code>
            </td>
            <td class="align-top">{{% md %}} On premise tag filters associated with the group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The service role ARN that allows deployments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">trigger_<wbr>configurations</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouptriggerconfiguration">List[deployment_<wbr>group_<wbr>trigger_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) of the triggers for the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing DeploymentGroup Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/codedeploy/#DeploymentGroupState">DeploymentGroupState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/codedeploy/#DeploymentGroup">DeploymentGroup</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>alarm_configuration=None<span class="p">, </span>app_name=None<span class="p">, </span>auto_rollback_configuration=None<span class="p">, </span>autoscaling_groups=None<span class="p">, </span>blue_green_deployment_config=None<span class="p">, </span>deployment_config_name=None<span class="p">, </span>deployment_group_name=None<span class="p">, </span>deployment_style=None<span class="p">, </span>ec2_tag_filters=None<span class="p">, </span>ec2_tag_sets=None<span class="p">, </span>ecs_service=None<span class="p">, </span>load_balancer_info=None<span class="p">, </span>on_premises_instance_tag_filters=None<span class="p">, </span>service_role_arn=None<span class="p">, </span>trigger_configurations=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetDeploymentGroup<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupState">DeploymentGroupState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroup">DeploymentGroup</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroup.html">DeploymentGroup</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupState.html">DeploymentGroupState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing DeploymentGroup resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Alarm<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupalarmconfiguration">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Alarm<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of alarms associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">App<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the application.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Rollback<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupautorollbackconfiguration">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Auto<wbr>Rollback<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Autoscaling groups associated with the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Blue<wbr>Green<wbr>Deployment<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfig">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the blue/green deployment options for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the group&#39;s deployment config. The default is &#34;CodeDeployDefault.OneAtATime&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Style</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupdeploymentstyle">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Deployment<wbr>Style<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ec2Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagfilter">List&lt;Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Filter<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tag filters associated with the deployment group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ec2Tag<wbr>Sets</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagset">List&lt;Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Set<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ecs<wbr>Service</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupecsservice">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Ecs<wbr>Service<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of the ECS services for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancer<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfo">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Single configuration block of the load balancer to use in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">On<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouponpremisesinstancetagfilter">List&lt;Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>On<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filter<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
On premise tag filters associated with the group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The service role ARN that allows deployments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Trigger<wbr>Configurations</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouptriggerconfiguration">List&lt;Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Trigger<wbr>Configuration<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of the triggers for the deployment group (documented below).
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
            <td class="align-top">Alarm<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupalarmconfiguration">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Alarm<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of alarms associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">App<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the application.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Rollback<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupautorollbackconfiguration">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Auto<wbr>Rollback<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Autoscaling groups associated with the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Blue<wbr>Green<wbr>Deployment<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfig">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the blue/green deployment options for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the group&#39;s deployment config. The default is &#34;CodeDeployDefault.OneAtATime&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Style</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupdeploymentstyle">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Deployment<wbr>Style</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ec2Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagfilter">[]codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Filter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tag filters associated with the deployment group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ec2Tag<wbr>Sets</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagset">[]codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Set</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ecs<wbr>Service</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupecsservice">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Ecs<wbr>Service</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of the ECS services for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancer<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfo">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Single configuration block of the load balancer to use in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">On<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouponpremisesinstancetagfilter">[]codedeploy.<wbr>Deployment<wbr>Group<wbr>On<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
On premise tag filters associated with the group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The service role ARN that allows deployments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Trigger<wbr>Configurations</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouptriggerconfiguration">[]codedeploy.<wbr>Deployment<wbr>Group<wbr>Trigger<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of the triggers for the deployment group (documented below).
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
            <td class="align-top">alarm<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupalarmconfiguration">codedeploy.<wbr>Deployment<wbr>Group<wbr>Alarm<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of alarms associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">app<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the application.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Rollback<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupautorollbackconfiguration">codedeploy.<wbr>Deployment<wbr>Group<wbr>Auto<wbr>Rollback<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Autoscaling groups associated with the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">blue<wbr>Green<wbr>Deployment<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfig">codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the blue/green deployment options for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the group&#39;s deployment config. The default is &#34;CodeDeployDefault.OneAtATime&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Style</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupdeploymentstyle">codedeploy.<wbr>Deployment<wbr>Group<wbr>Deployment<wbr>Style?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ec2Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagfilter">codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Filter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tag filters associated with the deployment group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ec2Tag<wbr>Sets</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagset">codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Set[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ecs<wbr>Service</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupecsservice">codedeploy.<wbr>Deployment<wbr>Group<wbr>Ecs<wbr>Service?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of the ECS services for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load<wbr>Balancer<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfo">codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Single configuration block of the load balancer to use in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">on<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouponpremisesinstancetagfilter">codedeploy.<wbr>Deployment<wbr>Group<wbr>On<wbr>Premises<wbr>Instance<wbr>Tag<wbr>Filter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
On premise tag filters associated with the group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The service role ARN that allows deployments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">trigger<wbr>Configurations</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouptriggerconfiguration">codedeploy.<wbr>Deployment<wbr>Group<wbr>Trigger<wbr>Configuration[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of the triggers for the deployment group (documented below).
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
            <td class="align-top">alarm_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupalarmconfiguration">Dict[deployment_<wbr>group_<wbr>alarm_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of alarms associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">app_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the application.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>rollback_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupautorollbackconfiguration">Dict[deployment_<wbr>group_<wbr>auto_<wbr>rollback_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling_<wbr>groups</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Autoscaling groups associated with the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">blue_<wbr>green_<wbr>deployment_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfig">Dict[deployment_<wbr>group_<wbr>blue_<wbr>green_<wbr>deployment_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the blue/green deployment options for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>config_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the group&#39;s deployment config. The default is &#34;CodeDeployDefault.OneAtATime&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>style</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupdeploymentstyle">Dict[deployment_<wbr>group_<wbr>deployment_<wbr>style]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ec2_<wbr>tag_<wbr>filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagfilter">List[deployment_<wbr>group_<wbr>ec2_<wbr>tag_<wbr>filter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tag filters associated with the deployment group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ec2_<wbr>tag_<wbr>sets</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagset">List[deployment_<wbr>group_<wbr>ec2_<wbr>tag_<wbr>set]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ecs_<wbr>service</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupecsservice">Dict[deployment_<wbr>group_<wbr>ecs_<wbr>service]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of the ECS services for a deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load_<wbr>balancer_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfo">Dict[deployment_<wbr>group_<wbr>load_<wbr>balancer_<wbr>info]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Single configuration block of the load balancer to use in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">on_<wbr>premises_<wbr>instance_<wbr>tag_<wbr>filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouponpremisesinstancetagfilter">List[deployment_<wbr>group_<wbr>on_<wbr>premises_<wbr>instance_<wbr>tag_<wbr>filter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
On premise tag filters associated with the group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The service role ARN that allows deployments.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">trigger_<wbr>configurations</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouptriggerconfiguration">List[deployment_<wbr>group_<wbr>trigger_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) of the triggers for the deployment group (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### DeploymentGroupAlarmConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupAlarmConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupAlarmConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupAlarmConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupAlarmConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupAlarmConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupAlarmConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">Alarms</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of alarms configured for the deployment group. _A maximum of 10 alarms can be added to a deployment group_.
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
Indicates whether a defined automatic rollback configuration is currently enabled for this Deployment Group. If you enable automatic rollback, you must specify at least one event type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ignore<wbr>Poll<wbr>Alarm<wbr>Failure</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from CloudWatch. The default value is `false`.
* `true`: The deployment will proceed even if alarm status information can&#39;t be retrieved.
* `false`: The deployment will stop if alarm status information can&#39;t be retrieved.
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
            <td class="align-top">Alarms</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of alarms configured for the deployment group. _A maximum of 10 alarms can be added to a deployment group_.
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
Indicates whether a defined automatic rollback configuration is currently enabled for this Deployment Group. If you enable automatic rollback, you must specify at least one event type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ignore<wbr>Poll<wbr>Alarm<wbr>Failure</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from CloudWatch. The default value is `false`.
* `true`: The deployment will proceed even if alarm status information can&#39;t be retrieved.
* `false`: The deployment will stop if alarm status information can&#39;t be retrieved.
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
            <td class="align-top">alarms</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of alarms configured for the deployment group. _A maximum of 10 alarms can be added to a deployment group_.
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
Indicates whether a defined automatic rollback configuration is currently enabled for this Deployment Group. If you enable automatic rollback, you must specify at least one event type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ignore<wbr>Poll<wbr>Alarm<wbr>Failure</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from CloudWatch. The default value is `false`.
* `true`: The deployment will proceed even if alarm status information can&#39;t be retrieved.
* `false`: The deployment will stop if alarm status information can&#39;t be retrieved.
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
            <td class="align-top">alarms</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of alarms configured for the deployment group. _A maximum of 10 alarms can be added to a deployment group_.
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
Indicates whether a defined automatic rollback configuration is currently enabled for this Deployment Group. If you enable automatic rollback, you must specify at least one event type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ignore_<wbr>poll_<wbr>alarm_<wbr>failure</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from CloudWatch. The default value is `false`.
* `true`: The deployment will proceed even if alarm status information can&#39;t be retrieved.
* `false`: The deployment will stop if alarm status information can&#39;t be retrieved.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupAutoRollbackConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupAutoRollbackConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupAutoRollbackConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupAutoRollbackConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupAutoRollbackConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupAutoRollbackConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupAutoRollbackConfiguration.html">output</a> API doc for this type.
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
Indicates whether a defined automatic rollback configuration is currently enabled for this Deployment Group. If you enable automatic rollback, you must specify at least one event type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Events</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The event type or types that trigger a rollback. Supported types are `DEPLOYMENT_FAILURE` and `DEPLOYMENT_STOP_ON_ALARM`.
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
Indicates whether a defined automatic rollback configuration is currently enabled for this Deployment Group. If you enable automatic rollback, you must specify at least one event type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Events</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The event type or types that trigger a rollback. Supported types are `DEPLOYMENT_FAILURE` and `DEPLOYMENT_STOP_ON_ALARM`.
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
Indicates whether a defined automatic rollback configuration is currently enabled for this Deployment Group. If you enable automatic rollback, you must specify at least one event type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">events</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The event type or types that trigger a rollback. Supported types are `DEPLOYMENT_FAILURE` and `DEPLOYMENT_STOP_ON_ALARM`.
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
Indicates whether a defined automatic rollback configuration is currently enabled for this Deployment Group. If you enable automatic rollback, you must specify at least one event type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">events</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The event type or types that trigger a rollback. Supported types are `DEPLOYMENT_FAILURE` and `DEPLOYMENT_STOP_ON_ALARM`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupBlueGreenDeploymentConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupBlueGreenDeploymentConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupBlueGreenDeploymentConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupBlueGreenDeploymentConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupBlueGreenDeploymentConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupBlueGreenDeploymentConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupBlueGreenDeploymentConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Deployment<wbr>Ready<wbr>Option</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfigdeploymentreadyoption">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config<wbr>Deployment<wbr>Ready<wbr>Option<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Green<wbr>Fleet<wbr>Provisioning<wbr>Option</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfiggreenfleetprovisioningoption">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config<wbr>Green<wbr>Fleet<wbr>Provisioning<wbr>Option<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about how instances are provisioned for a replacement environment in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Terminate<wbr>Blue<wbr>Instances<wbr>On<wbr>Deployment<wbr>Success</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfigterminateblueinstancesondeploymentsuccess">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config<wbr>Terminate<wbr>Blue<wbr>Instances<wbr>On<wbr>Deployment<wbr>Success<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about whether to terminate instances in the original fleet during a blue/green deployment (documented below).
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
            <td class="align-top">Deployment<wbr>Ready<wbr>Option</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfigdeploymentreadyoption">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config<wbr>Deployment<wbr>Ready<wbr>Option</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Green<wbr>Fleet<wbr>Provisioning<wbr>Option</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfiggreenfleetprovisioningoption">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config<wbr>Green<wbr>Fleet<wbr>Provisioning<wbr>Option</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about how instances are provisioned for a replacement environment in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Terminate<wbr>Blue<wbr>Instances<wbr>On<wbr>Deployment<wbr>Success</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfigterminateblueinstancesondeploymentsuccess">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config<wbr>Terminate<wbr>Blue<wbr>Instances<wbr>On<wbr>Deployment<wbr>Success</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about whether to terminate instances in the original fleet during a blue/green deployment (documented below).
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
            <td class="align-top">deployment<wbr>Ready<wbr>Option</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfigdeploymentreadyoption">codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config<wbr>Deployment<wbr>Ready<wbr>Option?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">green<wbr>Fleet<wbr>Provisioning<wbr>Option</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfiggreenfleetprovisioningoption">codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config<wbr>Green<wbr>Fleet<wbr>Provisioning<wbr>Option?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about how instances are provisioned for a replacement environment in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">terminate<wbr>Blue<wbr>Instances<wbr>On<wbr>Deployment<wbr>Success</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfigterminateblueinstancesondeploymentsuccess">codedeploy.<wbr>Deployment<wbr>Group<wbr>Blue<wbr>Green<wbr>Deployment<wbr>Config<wbr>Terminate<wbr>Blue<wbr>Instances<wbr>On<wbr>Deployment<wbr>Success?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about whether to terminate instances in the original fleet during a blue/green deployment (documented below).
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
            <td class="align-top">deployment_<wbr>ready_<wbr>option</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfigdeploymentreadyoption">Dict[deployment_<wbr>group_<wbr>blue_<wbr>green_<wbr>deployment_<wbr>config_<wbr>deployment_<wbr>ready_<wbr>option]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">green_<wbr>fleet_<wbr>provisioning_<wbr>option</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfiggreenfleetprovisioningoption">Dict[deployment_<wbr>group_<wbr>blue_<wbr>green_<wbr>deployment_<wbr>config_<wbr>green_<wbr>fleet_<wbr>provisioning_<wbr>option]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about how instances are provisioned for a replacement environment in a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">terminate_<wbr>blue_<wbr>instances_<wbr>on_<wbr>deployment_<wbr>success</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupbluegreendeploymentconfigterminateblueinstancesondeploymentsuccess">Dict[deployment_<wbr>group_<wbr>blue_<wbr>green_<wbr>deployment_<wbr>config_<wbr>terminate_<wbr>blue_<wbr>instances_<wbr>on_<wbr>deployment_<wbr>success]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about whether to terminate instances in the original fleet during a blue/green deployment (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption.html">output</a> API doc for this type.
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
            <td class="align-top">Action<wbr>On<wbr>Timeout</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When to reroute traffic from an original environment to a replacement environment in a blue/green deployment.
* `CONTINUE_DEPLOYMENT`: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.
* `STOP_DEPLOYMENT`: Do not register new instances with load balancer unless traffic is rerouted manually. If traffic is not rerouted manually before the end of the specified wait period, the deployment status is changed to Stopped.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>Time<wbr>In<wbr>Minutes</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of minutes to wait before the status of a blue/green deployment changed to Stopped if rerouting is not started manually. Applies only to the `STOP_DEPLOYMENT` option for `action_on_timeout`.
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
            <td class="align-top">Action<wbr>On<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When to reroute traffic from an original environment to a replacement environment in a blue/green deployment.
* `CONTINUE_DEPLOYMENT`: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.
* `STOP_DEPLOYMENT`: Do not register new instances with load balancer unless traffic is rerouted manually. If traffic is not rerouted manually before the end of the specified wait period, the deployment status is changed to Stopped.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>Time<wbr>In<wbr>Minutes</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of minutes to wait before the status of a blue/green deployment changed to Stopped if rerouting is not started manually. Applies only to the `STOP_DEPLOYMENT` option for `action_on_timeout`.
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
            <td class="align-top">action<wbr>On<wbr>Timeout</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When to reroute traffic from an original environment to a replacement environment in a blue/green deployment.
* `CONTINUE_DEPLOYMENT`: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.
* `STOP_DEPLOYMENT`: Do not register new instances with load balancer unless traffic is rerouted manually. If traffic is not rerouted manually before the end of the specified wait period, the deployment status is changed to Stopped.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait<wbr>Time<wbr>In<wbr>Minutes</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of minutes to wait before the status of a blue/green deployment changed to Stopped if rerouting is not started manually. Applies only to the `STOP_DEPLOYMENT` option for `action_on_timeout`.
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
            <td class="align-top">action_<wbr>on_<wbr>timeout</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When to reroute traffic from an original environment to a replacement environment in a blue/green deployment.
* `CONTINUE_DEPLOYMENT`: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.
* `STOP_DEPLOYMENT`: Do not register new instances with load balancer unless traffic is rerouted manually. If traffic is not rerouted manually before the end of the specified wait period, the deployment status is changed to Stopped.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait_<wbr>time_<wbr>in_<wbr>minutes</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of minutes to wait before the status of a blue/green deployment changed to Stopped if rerouting is not started manually. Applies only to the `STOP_DEPLOYMENT` option for `action_on_timeout`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption.html">output</a> API doc for this type.
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
            <td class="align-top">Action</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action to take on instances in the original environment after a successful blue/green deployment.
* `TERMINATE`: Instances are terminated after a specified wait time.
* `KEEP_ALIVE`: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.
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
            <td class="align-top">Action</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action to take on instances in the original environment after a successful blue/green deployment.
* `TERMINATE`: Instances are terminated after a specified wait time.
* `KEEP_ALIVE`: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.
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
            <td class="align-top">action</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action to take on instances in the original environment after a successful blue/green deployment.
* `TERMINATE`: Instances are terminated after a specified wait time.
* `KEEP_ALIVE`: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.
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
            <td class="align-top">action</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action to take on instances in the original environment after a successful blue/green deployment.
* `TERMINATE`: Instances are terminated after a specified wait time.
* `KEEP_ALIVE`: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess.html">output</a> API doc for this type.
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
            <td class="align-top">Action</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action to take on instances in the original environment after a successful blue/green deployment.
* `TERMINATE`: Instances are terminated after a specified wait time.
* `KEEP_ALIVE`: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Termination<wbr>Wait<wbr>Time<wbr>In<wbr>Minutes</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.
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
            <td class="align-top">Action</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action to take on instances in the original environment after a successful blue/green deployment.
* `TERMINATE`: Instances are terminated after a specified wait time.
* `KEEP_ALIVE`: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Termination<wbr>Wait<wbr>Time<wbr>In<wbr>Minutes</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.
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
            <td class="align-top">action</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action to take on instances in the original environment after a successful blue/green deployment.
* `TERMINATE`: Instances are terminated after a specified wait time.
* `KEEP_ALIVE`: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">termination<wbr>Wait<wbr>Time<wbr>In<wbr>Minutes</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.
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
            <td class="align-top">action</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action to take on instances in the original environment after a successful blue/green deployment.
* `TERMINATE`: Instances are terminated after a specified wait time.
* `KEEP_ALIVE`: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">termination_<wbr>wait_<wbr>time_<wbr>in_<wbr>minutes</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupDeploymentStyle
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupDeploymentStyle">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupDeploymentStyle">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupDeploymentStyleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupDeploymentStyleOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupDeploymentStyleArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupDeploymentStyle.html">output</a> API doc for this type.
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
            <td class="align-top">Deployment<wbr>Option</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether to route deployment traffic behind a load balancer. Valid Values are `WITH_TRAFFIC_CONTROL` or `WITHOUT_TRAFFIC_CONTROL`. Default is `WITHOUT_TRAFFIC_CONTROL`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether to run an in-place deployment or a blue/green deployment. Valid Values are `IN_PLACE` or `BLUE_GREEN`. Default is `IN_PLACE`.
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
            <td class="align-top">Deployment<wbr>Option</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether to route deployment traffic behind a load balancer. Valid Values are `WITH_TRAFFIC_CONTROL` or `WITHOUT_TRAFFIC_CONTROL`. Default is `WITHOUT_TRAFFIC_CONTROL`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether to run an in-place deployment or a blue/green deployment. Valid Values are `IN_PLACE` or `BLUE_GREEN`. Default is `IN_PLACE`.
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
            <td class="align-top">deployment<wbr>Option</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether to route deployment traffic behind a load balancer. Valid Values are `WITH_TRAFFIC_CONTROL` or `WITHOUT_TRAFFIC_CONTROL`. Default is `WITHOUT_TRAFFIC_CONTROL`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether to run an in-place deployment or a blue/green deployment. Valid Values are `IN_PLACE` or `BLUE_GREEN`. Default is `IN_PLACE`.
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
            <td class="align-top">deployment_<wbr>option</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether to route deployment traffic behind a load balancer. Valid Values are `WITH_TRAFFIC_CONTROL` or `WITHOUT_TRAFFIC_CONTROL`. Default is `WITHOUT_TRAFFIC_CONTROL`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether to run an in-place deployment or a blue/green deployment. Valid Values are `IN_PLACE` or `BLUE_GREEN`. Default is `IN_PLACE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupEc2TagFilter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupEc2TagFilter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupEc2TagFilter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupEc2TagFilterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupEc2TagFilterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupEc2TagFilterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupEc2TagFilter.html">output</a> API doc for this type.
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
            <td class="align-top">Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key of the tag filter.
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
The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the tag filter.
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
            <td class="align-top">Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key of the tag filter.
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
The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the tag filter.
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
            <td class="align-top">key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key of the tag filter.
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
The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the tag filter.
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
            <td class="align-top">key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key of the tag filter.
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
The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the tag filter.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupEc2TagSet
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupEc2TagSet">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupEc2TagSet">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupEc2TagSetArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupEc2TagSetOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupEc2TagSetArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupEc2TagSet.html">output</a> API doc for this type.
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
            <td class="align-top">Ec2Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagsetec2tagfilter">List&lt;Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Set<wbr>Ec2Tag<wbr>Filter<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tag filters associated with the deployment group. See the AWS docs for details.
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
            <td class="align-top">Ec2Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagsetec2tagfilter">[]codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Set<wbr>Ec2Tag<wbr>Filter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tag filters associated with the deployment group. See the AWS docs for details.
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
            <td class="align-top">ec2Tag<wbr>Filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagsetec2tagfilter">codedeploy.<wbr>Deployment<wbr>Group<wbr>Ec2Tag<wbr>Set<wbr>Ec2Tag<wbr>Filter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tag filters associated with the deployment group. See the AWS docs for details.
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
            <td class="align-top">ec2_<wbr>tag_<wbr>filters</td>
            <td class="align-top">
                
                <code><a href="#deploymentgroupec2tagsetec2tagfilter">List[deployment_<wbr>group_<wbr>ec2_<wbr>tag_<wbr>set_<wbr>ec2_<wbr>tag_<wbr>filter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Tag filters associated with the deployment group. See the AWS docs for details.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupEc2TagSetEc2TagFilter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupEc2TagSetEc2TagFilter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupEc2TagSetEc2TagFilter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupEc2TagSetEc2TagFilterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupEc2TagSetEc2TagFilterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupEc2TagSetEc2TagFilterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupEc2TagSetEc2TagFilter.html">output</a> API doc for this type.
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
            <td class="align-top">Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key of the tag filter.
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
The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the tag filter.
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
            <td class="align-top">Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key of the tag filter.
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
The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the tag filter.
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
            <td class="align-top">key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key of the tag filter.
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
The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the tag filter.
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
            <td class="align-top">key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key of the tag filter.
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
The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the tag filter.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupEcsService
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupEcsService">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupEcsService">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupEcsServiceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupEcsServiceOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupEcsServiceArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupEcsService.html">output</a> API doc for this type.
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
            <td class="align-top">Cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the ECS cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the ECS service.
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
            <td class="align-top">Cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the ECS cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the ECS service.
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
            <td class="align-top">cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the ECS cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the ECS service.
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
            <td class="align-top">cluster_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the ECS cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the ECS service.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupLoadBalancerInfo
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupLoadBalancerInfo">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupLoadBalancerInfo">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupLoadBalancerInfoArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupLoadBalancerInfoOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupLoadBalancerInfoArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupLoadBalancerInfo.html">output</a> API doc for this type.
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
            <td class="align-top">Elb<wbr>Infos</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfoelbinfo">List&lt;Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Elb<wbr>Info<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Classic Elastic Load Balancer to use in a deployment. Conflicts with `target_group_info` and `target_group_pair_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Group<wbr>Infos</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgroupinfo">List&lt;Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Target<wbr>Group<wbr>Info<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The (Application/Network Load Balancer) target group to use in a deployment. Conflicts with `elb_info` and `target_group_pair_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Group<wbr>Pair<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgrouppairinfo">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Target<wbr>Group<wbr>Pair<wbr>Info<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The (Application/Network Load Balancer) target group pair to use in a deployment. Conflicts with `elb_info` and `target_group_info`.
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
            <td class="align-top">Elb<wbr>Infos</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfoelbinfo">[]codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Elb<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Classic Elastic Load Balancer to use in a deployment. Conflicts with `target_group_info` and `target_group_pair_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Group<wbr>Infos</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgroupinfo">[]codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Target<wbr>Group<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The (Application/Network Load Balancer) target group to use in a deployment. Conflicts with `elb_info` and `target_group_pair_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Group<wbr>Pair<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgrouppairinfo">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Target<wbr>Group<wbr>Pair<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The (Application/Network Load Balancer) target group pair to use in a deployment. Conflicts with `elb_info` and `target_group_info`.
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
            <td class="align-top">elb<wbr>Infos</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfoelbinfo">codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Elb<wbr>Info[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Classic Elastic Load Balancer to use in a deployment. Conflicts with `target_group_info` and `target_group_pair_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Group<wbr>Infos</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgroupinfo">codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Target<wbr>Group<wbr>Info[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The (Application/Network Load Balancer) target group to use in a deployment. Conflicts with `elb_info` and `target_group_pair_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Group<wbr>Pair<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgrouppairinfo">codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Target<wbr>Group<wbr>Pair<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The (Application/Network Load Balancer) target group pair to use in a deployment. Conflicts with `elb_info` and `target_group_info`.
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
            <td class="align-top">elb_<wbr>infos</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfoelbinfo">List[deployment_<wbr>group_<wbr>load_<wbr>balancer_<wbr>info_<wbr>elb_<wbr>info]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Classic Elastic Load Balancer to use in a deployment. Conflicts with `target_group_info` and `target_group_pair_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>group_<wbr>infos</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgroupinfo">List[deployment_<wbr>group_<wbr>load_<wbr>balancer_<wbr>info_<wbr>target_<wbr>group_<wbr>info]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The (Application/Network Load Balancer) target group to use in a deployment. Conflicts with `elb_info` and `target_group_pair_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>group_<wbr>pair_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgrouppairinfo">Dict[deployment_<wbr>group_<wbr>load_<wbr>balancer_<wbr>info_<wbr>target_<wbr>group_<wbr>pair_<wbr>info]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The (Application/Network Load Balancer) target group pair to use in a deployment. Conflicts with `elb_info` and `target_group_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupLoadBalancerInfoElbInfo
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupLoadBalancerInfoElbInfo">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupLoadBalancerInfoElbInfo">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupLoadBalancerInfoElbInfoArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupLoadBalancerInfoElbInfoOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupLoadBalancerInfoElbInfoArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupLoadBalancerInfoElbInfo.html">output</a> API doc for this type.
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
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the target group.
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
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the target group.
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
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the target group.
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
 (Optional)
Name of the target group.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupLoadBalancerInfoTargetGroupInfo
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupLoadBalancerInfoTargetGroupInfo">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupLoadBalancerInfoTargetGroupInfo">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupLoadBalancerInfoTargetGroupInfoArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupLoadBalancerInfoTargetGroupInfoOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupLoadBalancerInfoTargetGroupInfoArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupLoadBalancerInfoTargetGroupInfo.html">output</a> API doc for this type.
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
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the target group.
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
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the target group.
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
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the target group.
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
 (Optional)
Name of the target group.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupLoadBalancerInfoTargetGroupPairInfo
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupLoadBalancerInfoTargetGroupPairInfo">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupLoadBalancerInfoTargetGroupPairInfo">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupLoadBalancerInfoTargetGroupPairInfoArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupLoadBalancerInfoTargetGroupPairInfoOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupLoadBalancerInfoTargetGroupPairInfo.html">output</a> API doc for this type.
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
            <td class="align-top">Prod<wbr>Traffic<wbr>Route</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgrouppairinfoprodtrafficroute">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Target<wbr>Group<wbr>Pair<wbr>Info<wbr>Prod<wbr>Traffic<wbr>Route<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block for the production traffic route (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Groups</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgrouppairinfotargetgroup">List&lt;Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Target<wbr>Group<wbr>Pair<wbr>Info<wbr>Target<wbr>Group<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration blocks for a target group within a target group pair (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Test<wbr>Traffic<wbr>Route</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgrouppairinfotesttrafficroute">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Target<wbr>Group<wbr>Pair<wbr>Info<wbr>Test<wbr>Traffic<wbr>Route<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for the test traffic route (documented below).
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
            <td class="align-top">Prod<wbr>Traffic<wbr>Route</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgrouppairinfoprodtrafficroute">codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Target<wbr>Group<wbr>Pair<wbr>Info<wbr>Prod<wbr>Traffic<wbr>Route</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block for the production traffic route (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Groups</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgrouppairinfotargetgroup">[]codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Target<wbr>Group<wbr>Pair<wbr>Info<wbr>Target<wbr>Group</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration blocks for a target group within a target group pair (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Test<wbr>Traffic<wbr>Route</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgrouppairinfotesttrafficroute">*codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Target<wbr>Group<wbr>Pair<wbr>Info<wbr>Test<wbr>Traffic<wbr>Route</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for the test traffic route (documented below).
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
            <td class="align-top">prod<wbr>Traffic<wbr>Route</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgrouppairinfoprodtrafficroute">codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Target<wbr>Group<wbr>Pair<wbr>Info<wbr>Prod<wbr>Traffic<wbr>Route</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block for the production traffic route (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Groups</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgrouppairinfotargetgroup">codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Target<wbr>Group<wbr>Pair<wbr>Info<wbr>Target<wbr>Group[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration blocks for a target group within a target group pair (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">test<wbr>Traffic<wbr>Route</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgrouppairinfotesttrafficroute">codedeploy.<wbr>Deployment<wbr>Group<wbr>Load<wbr>Balancer<wbr>Info<wbr>Target<wbr>Group<wbr>Pair<wbr>Info<wbr>Test<wbr>Traffic<wbr>Route?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for the test traffic route (documented below).
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
            <td class="align-top">prod_<wbr>traffic_<wbr>route</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgrouppairinfoprodtrafficroute">Dict[deployment_<wbr>group_<wbr>load_<wbr>balancer_<wbr>info_<wbr>target_<wbr>group_<wbr>pair_<wbr>info_<wbr>prod_<wbr>traffic_<wbr>route]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block for the production traffic route (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>groups</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgrouppairinfotargetgroup">List[deployment_<wbr>group_<wbr>load_<wbr>balancer_<wbr>info_<wbr>target_<wbr>group_<wbr>pair_<wbr>info_<wbr>target_<wbr>group]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration blocks for a target group within a target group pair (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">test_<wbr>traffic_<wbr>route</td>
            <td class="align-top">
                
                <code><a href="#deploymentgrouploadbalancerinfotargetgrouppairinfotesttrafficroute">Dict[deployment_<wbr>group_<wbr>load_<wbr>balancer_<wbr>info_<wbr>target_<wbr>group_<wbr>pair_<wbr>info_<wbr>test_<wbr>traffic_<wbr>route]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for the test traffic route (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute.html">output</a> API doc for this type.
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
            <td class="align-top">Listener<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of Amazon Resource Names (ARNs) of the load balancer listeners.
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
            <td class="align-top">Listener<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of Amazon Resource Names (ARNs) of the load balancer listeners.
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
            <td class="align-top">listener<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of Amazon Resource Names (ARNs) of the load balancer listeners.
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
            <td class="align-top">listener_<wbr>arns</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of Amazon Resource Names (ARNs) of the load balancer listeners.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup.html">output</a> API doc for this type.
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
Name of the target group.
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
Name of the target group.
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
Name of the target group.
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
Name of the target group.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute.html">output</a> API doc for this type.
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
            <td class="align-top">Listener<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of Amazon Resource Names (ARNs) of the load balancer listeners.
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
            <td class="align-top">Listener<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of Amazon Resource Names (ARNs) of the load balancer listeners.
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
            <td class="align-top">listener<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of Amazon Resource Names (ARNs) of the load balancer listeners.
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
            <td class="align-top">listener_<wbr>arns</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of Amazon Resource Names (ARNs) of the load balancer listeners.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupOnPremisesInstanceTagFilter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupOnPremisesInstanceTagFilter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupOnPremisesInstanceTagFilter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupOnPremisesInstanceTagFilterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupOnPremisesInstanceTagFilterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupOnPremisesInstanceTagFilterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupOnPremisesInstanceTagFilter.html">output</a> API doc for this type.
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
            <td class="align-top">Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key of the tag filter.
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
The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the tag filter.
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
            <td class="align-top">Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key of the tag filter.
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
The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the tag filter.
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
            <td class="align-top">key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key of the tag filter.
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
The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the tag filter.
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
            <td class="align-top">key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key of the tag filter.
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
The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the tag filter.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentGroupTriggerConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentGroupTriggerConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentGroupTriggerConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupTriggerConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentGroupTriggerConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupTriggerConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentGroupTriggerConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">Trigger<wbr>Events</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The event type or types for which notifications are triggered. Some values that are supported: `DeploymentStart`, `DeploymentSuccess`, `DeploymentFailure`, `DeploymentStop`, `DeploymentRollback`, `InstanceStart`, `InstanceSuccess`, `InstanceFailure`.  See [the CodeDeploy documentation][1] for all possible values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Trigger<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the notification trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Trigger<wbr>Target<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the SNS topic through which notifications are sent.
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
            <td class="align-top">Trigger<wbr>Events</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The event type or types for which notifications are triggered. Some values that are supported: `DeploymentStart`, `DeploymentSuccess`, `DeploymentFailure`, `DeploymentStop`, `DeploymentRollback`, `InstanceStart`, `InstanceSuccess`, `InstanceFailure`.  See [the CodeDeploy documentation][1] for all possible values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Trigger<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the notification trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Trigger<wbr>Target<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the SNS topic through which notifications are sent.
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
            <td class="align-top">trigger<wbr>Events</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The event type or types for which notifications are triggered. Some values that are supported: `DeploymentStart`, `DeploymentSuccess`, `DeploymentFailure`, `DeploymentStop`, `DeploymentRollback`, `InstanceStart`, `InstanceSuccess`, `InstanceFailure`.  See [the CodeDeploy documentation][1] for all possible values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">trigger<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the notification trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">trigger<wbr>Target<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the SNS topic through which notifications are sent.
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
            <td class="align-top">trigger_<wbr>events</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The event type or types for which notifications are triggered. Some values that are supported: `DeploymentStart`, `DeploymentSuccess`, `DeploymentFailure`, `DeploymentStop`, `DeploymentRollback`, `InstanceStart`, `InstanceSuccess`, `InstanceFailure`.  See [the CodeDeploy documentation][1] for all possible values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">trigger_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the notification trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">trigger_<wbr>target_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the SNS topic through which notifications are sent.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







