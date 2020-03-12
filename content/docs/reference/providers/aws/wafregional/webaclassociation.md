
---
title: "WebAclAssociation"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Manages an association with WAF Regional Web ACL.

> **Note:** An Application Load Balancer can only be associated with one WAF Regional WebACL.

## Application Load Balancer Association Example

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const fooVpc = new aws.ec2.Vpc("foo", {
    cidrBlock: "10.1.0.0/16",
});
const available = aws.getAvailabilityZones();
const bar = new aws.ec2.Subnet("bar", {
    availabilityZone: available.names[1],
    cidrBlock: "10.1.2.0/24",
    vpcId: fooVpc.id,
});
const fooSubnet = new aws.ec2.Subnet("foo", {
    availabilityZone: available.names[0],
    cidrBlock: "10.1.1.0/24",
    vpcId: fooVpc.id,
});
const fooLoadBalancer = new aws.alb.LoadBalancer("foo", {
    internal: true,
    subnets: [
        fooSubnet.id,
        bar.id,
    ],
});
const ipset = new aws.wafregional.IpSet("ipset", {
    ipSetDescriptors: [{
        type: "IPV4",
        value: "192.0.7.0/24",
    }],
});
const fooRule = new aws.wafregional.Rule("foo", {
    metricName: "tfWAFRule",
    predicates: [{
        dataId: ipset.id,
        negated: false,
        type: "IPMatch",
    }],
});
const fooWebAcl = new aws.wafregional.WebAcl("foo", {
    defaultAction: {
        type: "ALLOW",
    },
    metricName: "foo",
    rules: [{
        action: {
            type: "BLOCK",
        },
        priority: 1,
        ruleId: fooRule.id,
    }],
});
const fooWebAclAssociation = new aws.wafregional.WebAclAssociation("foo", {
    resourceArn: fooLoadBalancer.arn,
    webAclId: fooWebAcl.id,
});
```

## API Gateway Association Example

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const testRestApi = new aws.apigateway.RestApi("test", {});
const testResource = new aws.apigateway.Resource("test", {
    parentId: testRestApi.rootResourceId,
    pathPart: "test",
    restApi: testRestApi.id,
});
const testMethod = new aws.apigateway.Method("test", {
    authorization: "NONE",
    httpMethod: "GET",
    resourceId: testResource.id,
    restApi: testRestApi.id,
});
const testIntegration = new aws.apigateway.Integration("test", {
    httpMethod: testMethod.httpMethod,
    integrationHttpMethod: "GET",
    resourceId: testResource.id,
    restApi: testRestApi.id,
    type: "HTTP",
    uri: "http://www.example.com",
});
const testMethodResponse = new aws.apigateway.MethodResponse("test", {
    httpMethod: testMethod.httpMethod,
    resourceId: testResource.id,
    restApi: testRestApi.id,
    statusCode: "400",
});
const testIntegrationResponse = new aws.apigateway.IntegrationResponse("test", {
    httpMethod: testIntegration.httpMethod,
    resourceId: testResource.id,
    restApi: testRestApi.id,
    statusCode: testMethodResponse.statusCode,
});
const testDeployment = new aws.apigateway.Deployment("test", {
    restApi: testRestApi.id,
}, {dependsOn: [testIntegrationResponse]});
const testStage = new aws.apigateway.Stage("test", {
    deployment: testDeployment.id,
    restApi: testRestApi.id,
    stageName: "test",
});
const ipset = new aws.wafregional.IpSet("ipset", {
    ipSetDescriptors: [{
        type: "IPV4",
        value: "192.0.7.0/24",
    }],
});
const fooRule = new aws.wafregional.Rule("foo", {
    metricName: "tfWAFRule",
    predicates: [{
        dataId: ipset.id,
        negated: false,
        type: "IPMatch",
    }],
});
const fooWebAcl = new aws.wafregional.WebAcl("foo", {
    defaultAction: {
        type: "ALLOW",
    },
    metricName: "foo",
    rules: [{
        action: {
            type: "BLOCK",
        },
        priority: 1,
        ruleId: fooRule.id,
    }],
});
const association = new aws.wafregional.WebAclAssociation("association", {
    resourceArn: testStage.arn,
    webAclId: fooWebAcl.id,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_web_acl_association.html.markdown.



## Create a WebAclAssociation Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/wafregional/#WebAclAssociation">WebAclAssociation</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/wafregional/#WebAclAssociationArgs">WebAclAssociationArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

```python
def WebAclAssociation(resource_name, id, opts=None, resource_<wbr>arn=None, web_<wbr>acl_<wbr>id=None, __props__=None)
```

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewWebAclAssociation<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#WebAclAssociationArgs">WebAclAssociationArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/wafregional?tab=doc#WebAclAssociation">WebAclAssociation</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.WebAclAssociation.html">WebAclAssociation</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Wafregional.WebAclAssociationArgs.html">WebAclAssociationArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a WebAclAssociation resource with the given unique name, arguments, and options.

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
            <td class="align-top">Resource<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the WAF Regional WebACL to create an association.
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
            <td class="align-top">Resource<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the WAF Regional WebACL to create an association.
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
            <td class="align-top">resource<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the WAF Regional WebACL to create an association.
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
            <td class="align-top">resource_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">web_<wbr>acl_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the WAF Regional WebACL to create an association.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## WebAclAssociation Output Properties

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
            <td class="align-top">Resource<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the WAF Regional WebACL to create an association.
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
            <td class="align-top">Resource<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the WAF Regional WebACL to create an association.
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
            <td class="align-top">resource<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the WAF Regional WebACL to create an association.
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
            <td class="align-top">resource_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">web_<wbr>acl_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the WAF Regional WebACL to create an association.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing WebAclAssociation Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WebAclAssociationState, opts?: pulumi.CustomResourceOptions): WebAclAssociation;
```

```python
def get(resource_name, id, opts=None, resource_<wbr>arn=None, web_<wbr>acl_<wbr>id=None)
```

```go
func GetWebAclAssociation(ctx *pulumi.Context, name string, id pulumi.IDInput, state *WebAclAssociationState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static WebAclAssociation Get(string name, Input<string> id, WebAclAssociationState? state = null, CustomResourceOptions? options = null);
```

Get an existing WebAclAssociation resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Resource<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the WAF Regional WebACL to create an association.
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
            <td class="align-top">Resource<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the WAF Regional WebACL to create an association.
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
            <td class="align-top">resource<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the WAF Regional WebACL to create an association.
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
            <td class="align-top">resource_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ARN of the resource to associate with. For example, an Application Load Balancer or API Gateway Stage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">web_<wbr>acl_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the WAF Regional WebACL to create an association.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}









