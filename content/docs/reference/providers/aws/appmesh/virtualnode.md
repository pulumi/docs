
---
title: "VirtualNode"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides an AWS App Mesh virtual node resource.

## Breaking Changes

Because of backward incompatible API changes (read [here](https://github.com/awslabs/aws-app-mesh-examples/issues/92)), `aws.appmesh.VirtualNode` resource definitions created with provider versions earlier than v2.3.0 will need to be modified:

* Rename the `service_name` attribute of the `dns` object to `hostname`.

* Replace the `backends` attribute of the `spec` object with one or more `backend` configuration blocks,
setting `virtual_service_name` to the name of the service.

The state associated with existing resources will automatically be migrated.

## Example Usage

### Basic

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const serviceb1 = new aws.appmesh.VirtualNode("serviceb1", {
    meshName: aws_appmesh_mesh_simple.id,
    spec: {
        backends: [{
            virtualService: {
                virtualServiceName: "servicea.simpleapp.local",
            },
        }],
        listener: {
            portMapping: {
                port: 8080,
                protocol: "http",
            },
        },
        serviceDiscovery: {
            dns: {
                hostname: "serviceb.simpleapp.local",
            },
        },
    },
});
```

### AWS Cloud Map Service Discovery

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.servicediscovery.HttpNamespace("example", {});
const serviceb1 = new aws.appmesh.VirtualNode("serviceb1", {
    meshName: aws_appmesh_mesh_simple.id,
    spec: {
        backends: [{
            virtualService: {
                virtualServiceName: "servicea.simpleapp.local",
            },
        }],
        listener: {
            portMapping: {
                port: 8080,
                protocol: "http",
            },
        },
        serviceDiscovery: {
            awsCloudMap: {
                attributes: {
                    stack: "blue",
                },
                namespaceName: example.name,
                serviceName: "serviceb1",
            },
        },
    },
});
```

### Listener Health Check

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const serviceb1 = new aws.appmesh.VirtualNode("serviceb1", {
    meshName: aws_appmesh_mesh_simple.id,
    spec: {
        backends: [{
            virtualService: {
                virtualServiceName: "servicea.simpleapp.local",
            },
        }],
        listener: {
            healthCheck: {
                healthyThreshold: 2,
                intervalMillis: 5000,
                path: "/ping",
                protocol: "http",
                timeoutMillis: 2000,
                unhealthyThreshold: 2,
            },
            portMapping: {
                port: 8080,
                protocol: "http",
            },
        },
        serviceDiscovery: {
            dns: {
                hostname: "serviceb.simpleapp.local",
            },
        },
    },
});
```

### Logging

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const serviceb1 = new aws.appmesh.VirtualNode("serviceb1", {
    meshName: aws_appmesh_mesh_simple.id,
    spec: {
        backends: [{
            virtualService: {
                virtualServiceName: "servicea.simpleapp.local",
            },
        }],
        listener: {
            portMapping: {
                port: 8080,
                protocol: "http",
            },
        },
        logging: {
            accessLog: {
                file: {
                    path: "/dev/stdout",
                },
            },
        },
        serviceDiscovery: {
            dns: {
                hostname: "serviceb.simpleapp.local",
            },
        },
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appmesh_virtual_node.html.markdown.



## Create a VirtualNode Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appmesh/#VirtualNode">VirtualNode</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appmesh/#VirtualNodeArgs">VirtualNodeArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

```python
def VirtualNode(resource_name, id, opts=None, mesh_<wbr>name=None, name=None, spec=None, tags=None, __props__=None)
```

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewVirtualNode<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeArgs">VirtualNodeArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNode">VirtualNode</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNode.html">VirtualNode</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeArgs.html">VirtualNodeArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a VirtualNode resource with the given unique name, arguments, and options.

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
            <td class="align-top">Mesh<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the service mesh in which to create the virtual node.
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
The name to use for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spec</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespec">Pulumi.<wbr>Aws.<wbr>Appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The virtual node specification to apply.
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
            <td class="align-top">Mesh<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the service mesh in which to create the virtual node.
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
The name to use for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spec</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespec">appmesh.<wbr>Virtual<wbr>Node<wbr>Spec</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The virtual node specification to apply.
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
            <td class="align-top">mesh<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the service mesh in which to create the virtual node.
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
The name to use for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spec</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespec">appmesh.<wbr>Virtual<wbr>Node<wbr>Spec</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The virtual node specification to apply.
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
            <td class="align-top">mesh_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the service mesh in which to create the virtual node.
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
The name to use for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spec</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespec">dict{virtual_<wbr>node_<wbr>spec}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The virtual node specification to apply.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## VirtualNode Output Properties

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
            <td class="align-top">{{% md %}} The ARN of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Created<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The creation date of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Updated<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The last update date of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mesh<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the service mesh in which to create the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name to use for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spec</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespec">Pulumi.<wbr>Aws.<wbr>Appmesh.<wbr>Virtual<wbr>Node<wbr>Spec</a></code>
            </td>
            <td class="align-top">{{% md %}} The virtual node specification to apply.
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
            <td class="align-top">{{% md %}} The ARN of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Created<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The creation date of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Updated<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The last update date of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mesh<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the service mesh in which to create the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name to use for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spec</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespec">appmesh.<wbr>Virtual<wbr>Node<wbr>Spec</a></code>
            </td>
            <td class="align-top">{{% md %}} The virtual node specification to apply.
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
            <td class="align-top">{{% md %}} The ARN of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">created<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The creation date of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last<wbr>Updated<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The last update date of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mesh<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the service mesh in which to create the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name to use for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spec</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespec">appmesh.<wbr>Virtual<wbr>Node<wbr>Spec</a></code>
            </td>
            <td class="align-top">{{% md %}} The virtual node specification to apply.
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
            <td class="align-top">{{% md %}} The ARN of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">created_<wbr>date</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The creation date of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last_<wbr>updated_<wbr>date</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The last update date of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mesh_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the service mesh in which to create the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name to use for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spec</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespec">dict{virtual_<wbr>node_<wbr>spec}</a></code>
            </td>
            <td class="align-top">{{% md %}} The virtual node specification to apply.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing VirtualNode Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VirtualNodeState, opts?: pulumi.CustomResourceOptions): VirtualNode;
```

```python
def get(resource_name, id, opts=None, arn=None, created_<wbr>date=None, last_<wbr>updated_<wbr>date=None, mesh_<wbr>name=None, name=None, spec=None, tags=None)
```

```go
func GetVirtualNode(ctx *pulumi.Context, name string, id pulumi.IDInput, state *VirtualNodeState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static VirtualNode Get(string name, Input<string> id, VirtualNodeState? state = null, CustomResourceOptions? options = null);
```

Get an existing VirtualNode resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The ARN of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Created<wbr>Date</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The creation date of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Updated<wbr>Date</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The last update date of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mesh<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the service mesh in which to create the virtual node.
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
The name to use for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spec</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespec">Pulumi.<wbr>Aws.<wbr>Appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The virtual node specification to apply.
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
The ARN of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Created<wbr>Date</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The creation date of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Updated<wbr>Date</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The last update date of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mesh<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the service mesh in which to create the virtual node.
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
The name to use for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spec</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespec">*appmesh.<wbr>Virtual<wbr>Node<wbr>Spec</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The virtual node specification to apply.
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
The ARN of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">created<wbr>Date</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The creation date of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last<wbr>Updated<wbr>Date</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The last update date of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mesh<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the service mesh in which to create the virtual node.
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
The name to use for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spec</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespec">appmesh.<wbr>Virtual<wbr>Node<wbr>Spec?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The virtual node specification to apply.
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
The ARN of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">created_<wbr>date</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The creation date of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last_<wbr>updated_<wbr>date</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The last update date of the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mesh_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the service mesh in which to create the virtual node.
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
The name to use for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spec</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespec">dict{virtual_<wbr>node_<wbr>spec}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The virtual node specification to apply.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### VirtualNodeSpec
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#VirtualNodeSpec">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VirtualNodeSpec">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpec.html">output</a> API doc for this type.
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
            <td class="align-top">Backends</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecbackend">List&lt;Pulumi.<wbr>Aws.<wbr>Appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Backend<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The backends to which the virtual node is expected to send outbound traffic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Listener</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespeclistener">Pulumi.<wbr>Aws.<wbr>Appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Listener<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The listeners from which the virtual node is expected to receive inbound traffic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespeclogging">Pulumi.<wbr>Aws.<wbr>Appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Logging<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The inbound and outbound access logging information for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Discovery</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecservicediscovery">Pulumi.<wbr>Aws.<wbr>Appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Service<wbr>Discovery<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The service discovery information for the virtual node.
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
            <td class="align-top">Backends</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecbackend">[]appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Backend</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The backends to which the virtual node is expected to send outbound traffic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Listener</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespeclistener">*appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Listener</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The listeners from which the virtual node is expected to receive inbound traffic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespeclogging">*appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Logging</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The inbound and outbound access logging information for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Discovery</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecservicediscovery">*appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Service<wbr>Discovery</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The service discovery information for the virtual node.
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
            <td class="align-top">backends</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecbackend">appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Backend[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The backends to which the virtual node is expected to send outbound traffic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">listener</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespeclistener">appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Listener?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The listeners from which the virtual node is expected to receive inbound traffic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespeclogging">appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Logging?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The inbound and outbound access logging information for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Discovery</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecservicediscovery">appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Service<wbr>Discovery?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The service discovery information for the virtual node.
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
            <td class="align-top">backends</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecbackend">list[virtual_<wbr>node_<wbr>spec_<wbr>backend]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The backends to which the virtual node is expected to send outbound traffic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">listener</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespeclistener">dict{virtual_<wbr>node_<wbr>spec_<wbr>listener}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The listeners from which the virtual node is expected to receive inbound traffic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespeclogging">dict{virtual_<wbr>node_<wbr>spec_<wbr>logging}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The inbound and outbound access logging information for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>discovery</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecservicediscovery">dict{virtual_<wbr>node_<wbr>spec_<wbr>service_<wbr>discovery}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The service discovery information for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### VirtualNodeSpecBackend
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#VirtualNodeSpecBackend">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VirtualNodeSpecBackend">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecBackendArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecBackendOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecBackendArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecBackend.html">output</a> API doc for this type.
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
            <td class="align-top">Virtual<wbr>Service</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecbackendvirtualservice">Pulumi.<wbr>Aws.<wbr>Appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Backend<wbr>Virtual<wbr>Service<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies a virtual service to use as a backend for a virtual node.
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
            <td class="align-top">Virtual<wbr>Service</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecbackendvirtualservice">*appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Backend<wbr>Virtual<wbr>Service</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies a virtual service to use as a backend for a virtual node.
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
            <td class="align-top">virtual<wbr>Service</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecbackendvirtualservice">appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Backend<wbr>Virtual<wbr>Service?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies a virtual service to use as a backend for a virtual node.
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
            <td class="align-top">virtual_<wbr>service</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecbackendvirtualservice">dict{virtual_<wbr>node_<wbr>spec_<wbr>backend_<wbr>virtual_<wbr>service}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies a virtual service to use as a backend for a virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### VirtualNodeSpecBackendVirtualService
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#VirtualNodeSpecBackendVirtualService">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VirtualNodeSpecBackendVirtualService">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecBackendVirtualServiceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecBackendVirtualServiceOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecBackendVirtualServiceArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecBackendVirtualService.html">output</a> API doc for this type.
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
            <td class="align-top">Virtual<wbr>Service<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the virtual service that is acting as a virtual node backend.
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
            <td class="align-top">Virtual<wbr>Service<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the virtual service that is acting as a virtual node backend.
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
            <td class="align-top">virtual<wbr>Service<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the virtual service that is acting as a virtual node backend.
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
            <td class="align-top">virtual_<wbr>service_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the virtual service that is acting as a virtual node backend.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### VirtualNodeSpecListener
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#VirtualNodeSpecListener">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VirtualNodeSpecListener">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecListenerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecListenerOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecListenerArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecListener.html">output</a> API doc for this type.
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
            <td class="align-top">Health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespeclistenerhealthcheck">Pulumi.<wbr>Aws.<wbr>Appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Listener<wbr>Health<wbr>Check<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The health check information for the listener.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port<wbr>Mapping</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespeclistenerportmapping">Pulumi.<wbr>Aws.<wbr>Appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Listener<wbr>Port<wbr>Mapping<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The port mapping information for the listener.
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
            <td class="align-top">Health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespeclistenerhealthcheck">*appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Listener<wbr>Health<wbr>Check</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The health check information for the listener.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port<wbr>Mapping</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespeclistenerportmapping">appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Listener<wbr>Port<wbr>Mapping</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The port mapping information for the listener.
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
            <td class="align-top">health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespeclistenerhealthcheck">appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Listener<wbr>Health<wbr>Check?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The health check information for the listener.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port<wbr>Mapping</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespeclistenerportmapping">appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Listener<wbr>Port<wbr>Mapping</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The port mapping information for the listener.
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
            <td class="align-top">health_<wbr>check</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespeclistenerhealthcheck">dict{virtual_<wbr>node_<wbr>spec_<wbr>listener_<wbr>health_<wbr>check}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The health check information for the listener.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port_<wbr>mapping</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespeclistenerportmapping">dict{virtual_<wbr>node_<wbr>spec_<wbr>listener_<wbr>port_<wbr>mapping}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The port mapping information for the listener.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### VirtualNodeSpecListenerHealthCheck
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#VirtualNodeSpecListenerHealthCheck">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VirtualNodeSpecListenerHealthCheck">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecListenerHealthCheckArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecListenerHealthCheckOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecListenerHealthCheckArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecListenerHealthCheck.html">output</a> API doc for this type.
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
            <td class="align-top">Healthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of consecutive successful health checks that must occur before declaring listener healthy.
* `interval_millis`- (Required) The time period in milliseconds between each health check execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Interval<wbr>Millis</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
The destination path for the health check request. This is only required if the specified protocol is `http`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The destination port for the health check request. This port must match the port defined in the `port_mapping` for the listener.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol for the health check request. Valid values are `http` and `tcp`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timeout<wbr>Millis</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The amount of time to wait when receiving a response from the health check, in milliseconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Unhealthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.
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
            <td class="align-top">Healthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of consecutive successful health checks that must occur before declaring listener healthy.
* `interval_millis`- (Required) The time period in milliseconds between each health check execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Interval<wbr>Millis</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
The destination path for the health check request. This is only required if the specified protocol is `http`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The destination port for the health check request. This port must match the port defined in the `port_mapping` for the listener.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol for the health check request. Valid values are `http` and `tcp`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timeout<wbr>Millis</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The amount of time to wait when receiving a response from the health check, in milliseconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Unhealthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.
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
            <td class="align-top">healthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of consecutive successful health checks that must occur before declaring listener healthy.
* `interval_millis`- (Required) The time period in milliseconds between each health check execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">interval<wbr>Millis</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
The destination path for the health check request. This is only required if the specified protocol is `http`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The destination port for the health check request. This port must match the port defined in the `port_mapping` for the listener.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol for the health check request. Valid values are `http` and `tcp`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timeout<wbr>Millis</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The amount of time to wait when receiving a response from the health check, in milliseconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">unhealthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.
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
            <td class="align-top">healthy_<wbr>threshold</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of consecutive successful health checks that must occur before declaring listener healthy.
* `interval_millis`- (Required) The time period in milliseconds between each health check execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">interval_<wbr>millis</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
The destination path for the health check request. This is only required if the specified protocol is `http`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The destination port for the health check request. This port must match the port defined in the `port_mapping` for the listener.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol for the health check request. Valid values are `http` and `tcp`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timeout_<wbr>millis</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The amount of time to wait when receiving a response from the health check, in milliseconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">unhealthy_<wbr>threshold</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### VirtualNodeSpecListenerPortMapping
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#VirtualNodeSpecListenerPortMapping">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VirtualNodeSpecListenerPortMapping">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecListenerPortMappingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecListenerPortMappingOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecListenerPortMappingArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecListenerPortMapping.html">output</a> API doc for this type.
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
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The destination port for the health check request. This port must match the port defined in the `port_mapping` for the listener.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol for the health check request. Valid values are `http` and `tcp`.
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
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The destination port for the health check request. This port must match the port defined in the `port_mapping` for the listener.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol for the health check request. Valid values are `http` and `tcp`.
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
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The destination port for the health check request. This port must match the port defined in the `port_mapping` for the listener.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol for the health check request. Valid values are `http` and `tcp`.
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
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The destination port for the health check request. This port must match the port defined in the `port_mapping` for the listener.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol for the health check request. Valid values are `http` and `tcp`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### VirtualNodeSpecLogging
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#VirtualNodeSpecLogging">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VirtualNodeSpecLogging">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecLoggingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecLoggingOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecLoggingArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecLogging.html">output</a> API doc for this type.
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
            <td class="align-top">Access<wbr>Log</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecloggingaccesslog">Pulumi.<wbr>Aws.<wbr>Appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Logging<wbr>Access<wbr>Log<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The access log configuration for a virtual node.
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
            <td class="align-top">Access<wbr>Log</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecloggingaccesslog">*appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Logging<wbr>Access<wbr>Log</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The access log configuration for a virtual node.
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
            <td class="align-top">access<wbr>Log</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecloggingaccesslog">appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Logging<wbr>Access<wbr>Log?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The access log configuration for a virtual node.
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
            <td class="align-top">access_<wbr>log</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecloggingaccesslog">dict{virtual_<wbr>node_<wbr>spec_<wbr>logging_<wbr>access_<wbr>log}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The access log configuration for a virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### VirtualNodeSpecLoggingAccessLog
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#VirtualNodeSpecLoggingAccessLog">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VirtualNodeSpecLoggingAccessLog">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecLoggingAccessLogArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecLoggingAccessLogOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecLoggingAccessLogArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecLoggingAccessLog.html">output</a> API doc for this type.
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
            <td class="align-top">File</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecloggingaccesslogfile">Pulumi.<wbr>Aws.<wbr>Appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Logging<wbr>Access<wbr>Log<wbr>File<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The file object to send virtual node access logs to.
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
            <td class="align-top">File</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecloggingaccesslogfile">*appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Logging<wbr>Access<wbr>Log<wbr>File</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The file object to send virtual node access logs to.
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
            <td class="align-top">file</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecloggingaccesslogfile">appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Logging<wbr>Access<wbr>Log<wbr>File?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The file object to send virtual node access logs to.
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
            <td class="align-top">file</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecloggingaccesslogfile">dict{virtual_<wbr>node_<wbr>spec_<wbr>logging_<wbr>access_<wbr>log_<wbr>file}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The file object to send virtual node access logs to.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### VirtualNodeSpecLoggingAccessLogFile
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#VirtualNodeSpecLoggingAccessLogFile">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VirtualNodeSpecLoggingAccessLogFile">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecLoggingAccessLogFileArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecLoggingAccessLogFileOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecLoggingAccessLogFileArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecLoggingAccessLogFile.html">output</a> API doc for this type.
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
            <td class="align-top">Path</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The destination path for the health check request. This is only required if the specified protocol is `http`.
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
            <td class="align-top">Path</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The destination path for the health check request. This is only required if the specified protocol is `http`.
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
            <td class="align-top">path</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The destination path for the health check request. This is only required if the specified protocol is `http`.
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
            <td class="align-top">path</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The destination path for the health check request. This is only required if the specified protocol is `http`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### VirtualNodeSpecServiceDiscovery
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#VirtualNodeSpecServiceDiscovery">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VirtualNodeSpecServiceDiscovery">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecServiceDiscoveryArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecServiceDiscoveryOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecServiceDiscoveryArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecServiceDiscovery.html">output</a> API doc for this type.
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
            <td class="align-top">Aws<wbr>Cloud<wbr>Map</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecservicediscoveryawscloudmap">Pulumi.<wbr>Aws.<wbr>Appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Service<wbr>Discovery<wbr>Aws<wbr>Cloud<wbr>Map<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies any AWS Cloud Map information for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dns</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecservicediscoverydns">Pulumi.<wbr>Aws.<wbr>Appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Service<wbr>Discovery<wbr>Dns<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the DNS service name for the virtual node.
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
            <td class="align-top">Aws<wbr>Cloud<wbr>Map</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecservicediscoveryawscloudmap">*appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Service<wbr>Discovery<wbr>Aws<wbr>Cloud<wbr>Map</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies any AWS Cloud Map information for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dns</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecservicediscoverydns">*appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Service<wbr>Discovery<wbr>Dns</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the DNS service name for the virtual node.
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
            <td class="align-top">aws<wbr>Cloud<wbr>Map</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecservicediscoveryawscloudmap">appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Service<wbr>Discovery<wbr>Aws<wbr>Cloud<wbr>Map?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies any AWS Cloud Map information for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dns</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecservicediscoverydns">appmesh.<wbr>Virtual<wbr>Node<wbr>Spec<wbr>Service<wbr>Discovery<wbr>Dns?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the DNS service name for the virtual node.
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
            <td class="align-top">aws_<wbr>cloud_<wbr>map</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecservicediscoveryawscloudmap">dict{virtual_<wbr>node_<wbr>spec_<wbr>service_<wbr>discovery_<wbr>aws_<wbr>cloud_<wbr>map}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies any AWS Cloud Map information for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dns</td>
            <td class="align-top">
                
                <code><a href="#virtualnodespecservicediscoverydns">dict{virtual_<wbr>node_<wbr>spec_<wbr>service_<wbr>discovery_<wbr>dns}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the DNS service name for the virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### VirtualNodeSpecServiceDiscoveryAwsCloudMap
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#VirtualNodeSpecServiceDiscoveryAwsCloudMap">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VirtualNodeSpecServiceDiscoveryAwsCloudMap">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecServiceDiscoveryAwsCloudMapArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecServiceDiscoveryAwsCloudMapOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecServiceDiscoveryAwsCloudMapArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecServiceDiscoveryAwsCloudMap.html">output</a> API doc for this type.
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
            <td class="align-top">Attributes</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the AWS Cloud Map namespace to use.
Use the [`aws.servicediscovery.HttpNamespace`](https://www.terraform.io/docs/providers/aws/r/service_discovery_http_namespace.html) resource to configure a Cloud Map namespace.
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
The name of the AWS Cloud Map service to use. Use the [`aws.servicediscovery.Service`](https://www.terraform.io/docs/providers/aws/r/service_discovery_service.html) resource to configure a Cloud Map service.
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
            <td class="align-top">Attributes</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the AWS Cloud Map namespace to use.
Use the [`aws.servicediscovery.HttpNamespace`](https://www.terraform.io/docs/providers/aws/r/service_discovery_http_namespace.html) resource to configure a Cloud Map namespace.
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
The name of the AWS Cloud Map service to use. Use the [`aws.servicediscovery.Service`](https://www.terraform.io/docs/providers/aws/r/service_discovery_service.html) resource to configure a Cloud Map service.
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
            <td class="align-top">attributes</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the AWS Cloud Map namespace to use.
Use the [`aws.servicediscovery.HttpNamespace`](https://www.terraform.io/docs/providers/aws/r/service_discovery_http_namespace.html) resource to configure a Cloud Map namespace.
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
The name of the AWS Cloud Map service to use. Use the [`aws.servicediscovery.Service`](https://www.terraform.io/docs/providers/aws/r/service_discovery_service.html) resource to configure a Cloud Map service.
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
            <td class="align-top">attributes</td>
            <td class="align-top">
                
                <code>dict{string}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the AWS Cloud Map namespace to use.
Use the [`aws.servicediscovery.HttpNamespace`](https://www.terraform.io/docs/providers/aws/r/service_discovery_http_namespace.html) resource to configure a Cloud Map namespace.
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
The name of the AWS Cloud Map service to use. Use the [`aws.servicediscovery.Service`](https://www.terraform.io/docs/providers/aws/r/service_discovery_service.html) resource to configure a Cloud Map service.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### VirtualNodeSpecServiceDiscoveryDns
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#VirtualNodeSpecServiceDiscoveryDns">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#VirtualNodeSpecServiceDiscoveryDns">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecServiceDiscoveryDnsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appmesh?tab=doc#VirtualNodeSpecServiceDiscoveryDnsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecServiceDiscoveryDnsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appmesh.VirtualNodeSpecServiceDiscoveryDns.html">output</a> API doc for this type.
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
            <td class="align-top">Hostname</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The DNS host name for your virtual node.
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
            <td class="align-top">Hostname</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The DNS host name for your virtual node.
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
            <td class="align-top">hostname</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The DNS host name for your virtual node.
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
            <td class="align-top">hostname</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The DNS host name for your virtual node.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







