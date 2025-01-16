---
title: "Reference Kubernetes Resources Across Stacks"
title_tag: "Reference Kubernetes Resources Across Stacks"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Learn more about exporting and referencing stack outputs in Pulumi.

# A similar description used for search results and social-media previews.
meta_desc: Learn more about exporting and referencing stack outputs in Pulumi.  

# An image for the tutorial. It appears on tutorial page and in social-media previews.
meta_image: k8s-stack-ref-meta.png

# An optional video for the tutorial. When present, it appears at the top of the page, replacing
# the meta image. YouTube and HTML5 video sources are supported.
# video:
#     url: /blog/drift-detection/drift.mp4
#     youtube: Q8tw6YTD3ac

# The order in which the tutorial appears in most lists. Order is ascending, so higher numbers
# mean the tutorial will appear further down the list. Positive integers only.
weight: 999

# A brief summary of the tutorial. It appears at the top of the tutorial page. Markdown is fine.
summary: |
    In this tutorial, you will learn how to work with stack outputs, specifically how to export values from a stack and how to reference those values from another stack. You will do this by creating a simple Kubernetes deployment resource in one stack. You will then create a Kubernetes service resource in a second project/stack that will reference the deployment in the first stack.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to create a stack output
    - How to view the stack output
    - How to reference the output from a different stack

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
  - The [Pulumi CLI](/docs/install/)
  - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)
  - A running [Minikube](https://minikube.sigs.k8s.io/docs/start/) cluster
  - The Kubernetes command line tool [kubectl](https://kubernetes.io/docs/tasks/tools/) installed
  - Your desired [language runtime installed](/docs/iac/get-started/aws/begin/#install-language-runtime)

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 15

# An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
collections:
    - kubernetes
---

## Understanding stack outputs

Every Pulumi resource has outputs, which are properties of that resource whose values are generated during deployment. You can export these values as stack outputs, and they can be used for important values like resource IDs, computed IP addresses, and DNS names.

These outputs are shown during an update, can be easily retrieved with the Pulumi CLI, and are displayed in Pulumi Cloud. For the purposes of this tutorial, you will primarily be working from the CLI.

### Create a new project

```bash
# Example using Python
$ mkdir pulumi-tutorial-k8s
$ cd pulumi-tutorial-k8s
$ pulumi new kubernetes-python
```

Then replace the default code with the following code snippet to scaffold your project with the required imports and overall program structure:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="javascript" from="1" to="16" >}}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="typescript" from="1" to="16" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="python" from="1" to="17" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="go" from="1" to="39" >}}

{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="go" from="63" to="66" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="csharp" from="1" to="52" >}}

{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="csharp" from="73" to="73" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="yaml" from="1" to="23" >}}
```

{{% /choosable %}}

This baseline code defines the following on your behalf:

- a [Kubernetes Deployment](/registry/packages/kubernetes/api-docs/apps/v1/deployment/)

Then configure the Pulumi CLI to [access your Kubernetes Minikube cluster](tutorials/creating-resources-kubernetes/#configure-kubernetes-access).

## Export resource values

As mentioned in the [Creating Resources on Kubernetes tutorial](/tutorials/creating-resources-kubernetes/), every resource has various properties. For any resources that you define in your Pulumi projects, you can [export the values](/docs/iac/concepts/stacks/#outputs) of its properties from your program as outputs. You can view a list of available properties that can be exported by referring to the resource properties section of a particular resource's API documentation (e.g. [Deployment resource properties](/registry/packages/kubernetes/api-docs/apps/v1/deployment/#properties)). The `export` syntax is as follows:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
exports.<output-name> = <output-value>;
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
export const <output-name> = <output-value>;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
pulumi.export("<output-name>", <output-value>)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
ctx.Export("<output-name>", <output-value>)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
return await Pulumi.Deployment.RunAsync(() =>
{

    return new Dictionary<string, object?>
    {
        ["<output-name>"] = <output-value>
    };

});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
outputs:
  <output-name>: ${<output-value>}
```

{{% /choosable %}}

When defining these exports, you'll need to provide two arguments:

| Argument | Description |
|--------------|-------------|
| Output name | This is the name you will use as the identifier of your output value |
| Output value | This is the actual value of your output |

To demonstrate how this works, let's export the name of your deployment which can be found in the deployment's metadata. By referring to the documentation, you can see that the metadata of the deployment can be referenced via its `metadata` property, so update your code to reflect that as shown below:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="javascript" from="1" to="16" >}}

exports.deploymentName = deployment.metadata["name"];
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="typescript" from="1" to="16" >}}

expors const deploymentName = deployment.metadata["name"]
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="python" from="1" to="17" >}}

pulumi.export("deploymentName", deployment.metadata["name"])
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="go" from="1" to="39" >}}

        ctx.Export("deploymentName", deployment.Metadata["name"])
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="go" from="63" to="66" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="csharp" from="1" to="52" >}}

    return new Dictionary<string, object?>
    {
        ["deploymentName"] = deployment.Metadata["name"],

    };
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="csharp" from="73" to="73" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="yaml" from="1" to="23" >}}

outputs:
  deploymentName: ${deployment.metadata["name"]}
```

{{% /choosable %}}

## Deploy your resources

Now save your file and run the `pulumi up` command to preview and deploy the resources you've just defined in your project.

```bash
$ pulumi up -y
Previewing update (infra)

     Type                              Name              Plan
 +   pulumi:pulumi:Stack               k8s-stackref-dev  create
 +   └─ kubernetes:apps/v1:Deployment  nginx             create

Outputs:
    name: "nginx-f575adcf"

Resources:
    + 2 to create

Updating (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/v-torian-pulumi-corp/k8s-stackref/dev/updates/3

     Type                              Name              Status
 +   pulumi:pulumi:Stack               k8s-stackref-dev  created (5s)
 +   └─ kubernetes:apps/v1:Deployment  nginx             created (3s)

Outputs:
    name: "nginx-a3731b33"

Resources:
    + 2 created

Duration: 7s
```

You can see that the output you've created has been provided as a part of the update details. You will learn the different ways you can access this output in the next steps of the tutorial.

## Access outputs via the CLI

Now that your resources are deployed, you can access your output values either via the CLI or via your Pulumi program code. To access it via the CLI, you can use the [`pulumi stack output` command](/docs/iac/cli/commands/pulumi_stack_output/). Running this command by itself will list the names and values of all of the exports in your program:

```bash
$ pulumi stack output

Current stack outputs (1):
    OUTPUT          VALUE
    deploymentName  nginx-a3731b33
```

If you want to retrieve a specific output value, you will need to provide the name of your desired output as shown below:

```bash
$ pulumi stack output deploymentName

nginx-a3731b33
```

This can be especially useful if you have any workflow scripts that depend on the outputs of your program. For example, if you wanted to view the details of your deployment using the Kubernetes CLI, you can do so by running the [`kubectl get deployment` command](https://kubernetes.io/docs/reference/kubectl/quick-reference/#viewing-and-finding-resources) and passing the output of `deploymentName` as shown below:

```bash
$ kubectl get deployment $(pulumi stack output deploymentName)

NAME             READY   UP-TO-DATE   AVAILABLE   AGE
nginx-a3731b33   1/1     1            1           4m52s
```

You have seen how you can reference your output values from the CLI. Now let’s take a look at how you can do the same from within another Pulumi program stack.

## Access outputs via stack reference

Stack references allow you to access the outputs of one stack from another stack. This enables developers to create resources even when there are inter-stack dependencies. For this section, you are going to create a new Pulumi program that will access stack output values from your existing program.

### Reference deployment name

Start by making a new Pulumi project in a new directory. In this new program, you will need to add the code that will reference an output value from your first program. This can be done using Pulumi's [Stack Reference functionality](/docs/concepts/stack/#stackreferences). When defining a stack reference in code, you will need to pass in the fully qualified name of the stack as an argument. This name is comprised of the [organization](/docs/pulumi-cloud/organizations/), [project](/docs/iac/concepts/projects/), and [stack](/docs/iac/concepts/stacks/) names in the format of `<organization>/<project>/<stack>`

For example, if the name of your organization is `acmecorp`, the name of your first program is `infra`, and the name of your stack is `dev`, then your fully qualified name will be `acmecorp/infra/dev`.

With that being said, a stack reference will look like the following in your code:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");

const stackRef = new pulumi.StackReference("acmecorp/infra/dev");
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

const stackRef = new pulumi.StackReference("acmecorp/infra/dev");
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi

stack_ref = pulumi.StackReference("acmecorp/infra/dev")
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
        stackRef, err := pulumi.NewStackReference(ctx, "acmecorp/infra/dev", nil)
        if err != nil {
            return err
        }

		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;

return await Pulumi.Deployment.RunAsync(() =>
{

    var stackRef = new StackReference("acmecorp/infra/dev");

});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: my-second-app-dev
runtime: yaml
description: A program to create a Stack Reference

resources:
  stack-ref:
    type: pulumi:pulumi:StackReference
    properties:
      name: acmecorp/infra/dev
```

{{% /choosable %}}

{{% notes type="info" %}}

Make sure that the fully qualified name in the example above is populated with the values that are specific to your Pulumi organization, project, and stack.

{{% /notes %}}

You will now create an export in your second program that will output the value of the deployment name from your first program. This is to demonstrate how to retrieve output values from another stack for use in your program.

For the value of your export, you can retrieve it by taking your stack reference variable and using a Stack Reference function called getOutput() against it.

Update your code with the following:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");

const stackRef = new pulumi.StackReference("acmecorp/infra/dev");

// Retrieve deployment name from the first stack
// using the stack reference above
const deploymentName = stackRef.getOutput("deploymentName");

exports.deploymentName = deploymentName;
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

const stackRef = new pulumi.StackReference("acmecorp/infra/dev");

// Retrieve deployment name from the first stack
// using the stack reference above
const deploymentName = stackRef.getOutput("deploymentName");

export const deploymentName = deploymentName;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi

stack_ref = pulumi.StackReference("acmecorp/infra/dev")

# Retrieve deployment name from the first stack
# using the stack reference above
deployment_name = stack_ref.get_output("deploymentName")

pulumi.export("deploymentName", deployment_nam)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
        stackRef, err := pulumi.NewStackReference(ctx, "acmecorp/infra/dev", nil)
        if err != nil {
            return err
        }

        // Retrieve deployment name from the first stack
        // using the stack reference above
        deploymentName := stackRef.GetOutput(pulumi.String("deploymentName"))

        ctx.Export("deploymentName", deploymentName)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;

return await Pulumi.Deployment.RunAsync(() =>
{

    var stackRef = new StackReference("acmecorp/infra/dev");

    // Retrieve deployment name from the first stack
    // using the stack reference above
    var deploymentName = stackRef.GetOutput("deploymentName");

    return new Dictionary<string, object?>
    {
        ["deploymentName"] = deploymentName
    };

});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: my-second-app-dev
runtime: yaml
description: A program to create a Stack Reference

resources:
  stack-ref:
    type: pulumi:pulumi:StackReference
    properties:
      name: acmecorp/infra/dev

variables:
  deploymentName: ${stack-ref.outputs["deploymentName"]}

outputs:
  deploymentName: ${deploymentName}
```

{{% /choosable %}}

To verify that your stack reference is working, run `pulumi up`.

```bash
$ pulumi up -y

Previewing update (dev):

     Type                      Name                     Plan
 +   pulumi:pulumi:Stack  my-second-app-dev             create

Outputs:
    deploymentName: output<string>

Resources:
    + 4 to create

Do you want to perform this update? yes
Updating (dev):

     Type                      Name                     Status
 +   pulumi:pulumi:Stack  my-second-app-dev             created (2s)

Outputs:
    deploymentName: "nginx-a3731b33"

Resources:
    + 1 created

Duration: 3s
```

You should see the name of your deployment from your first program successfully outputted in the update details of your second program.

## Use stack reference in resource definition

In this section, you will use everything you have learned in this tutorial to define a resource that uses a stack reference in the resource definition. In your second program, you will be defining Kubernetes Service resource that will reference the `labels` value in the metadata of the deployment resource that was created in your first program. Use the following steps as a guide for adding the Service resource:

- Navigate to the [Kubernetes Registry documentation page](/registry/packages/kubernetes/)
- Search for the `kubernetes.core/v1.Service` resource
- Define the Service resource in your second program code, making sure to define the `labels` sub-property of the `metadata` property
- Export required property values in your first program code
- Import required property values in your second program
- Save and deploy your first program code
- Then save and deploy your second program code

Once you have completed these steps, forward the Nginx service to make it accessible from localhost. First, retrieve the name and port of your service using the following command:

```bash
$ kubectl get service
NAME             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
kubernetes       ClusterIP   10.96.0.1        <none>        443/TCP   44h
nginx-9e5d5cd4   ClusterIP   10.103.199.118   <none>        80/TCP    6m47s
```

In the example above, the name of the service is `nginx-9e5d5cd4`. Then run the following command to perform the forwarding, making sure to provide the name and port of your own Nginx service in your own environment:

```bash
$ kubectl port-forward service/nginx-9e5d5cd4 8080:80
 Forwarding from 127.0.0.1:8080 -> 80
 Forwarding from [::1]:8080 -> 80
```

In a new terminal, verify that Nginx is running and accessible by running curl against the localhost as shown in the below example:

```bash
curl "http://localhost:8080"

<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

You should be greated with the HTML code of the Nginx landing page as shown above.

## View complete solution

You can view the code for the complete solution below.

### First program code

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="javascript" from="1" to="16" >}}

exports.deploymentName = deployment.metadata["name"];
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="typescript" from="1" to="16" >}}

expors const deploymentName = deployment.metadata["name"]
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="python" from="1" to="17" >}}

pulumi.export("deploymentName", deployment.metadata["name"])
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="go" from="1" to="39" >}}

        ctx.Export("deploymentName", deployment.Metadata["name"])
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="go" from="63" to="66" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="csharp" from="1" to="52" >}}

    return new Dictionary<string, object?>
    {
        ["deploymentName"] = deployment.Metadata["name"],

    };
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="csharp" from="73" to="73" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="yaml" from="1" to="23" >}}

outputs:
  deploymentName: ${deployment.metadata["name"]}
```

{{% /choosable %}}

### Second program code

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");

const stackRef = new pulumi.StackReference("acmecorp/infra/dev");

const deploymentName = stackRef.getOutput("deploymentName");
const storageAccountName = stackRef.getOutput("storageAccountName");
const blobContainerName = stackRef.getOutput("blobContainerName");

{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="javascript" from="25" to="32" >}}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

const stackRef = new pulumi.StackReference("acmecorp/infra/dev");

const deploymentName2 = stackRef.getOutput("deploymentName");
const storageAccountName2 = stackRef.getOutput("storageAccountName");
const blobContainerName2 = stackRef.getOutput("blobContainerName");

{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="typescript" from="24" to="31" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi

stack_ref = pulumi.StackReference("acmecorp/infra/dev")

resource_group_name = stack_ref.get_output("deploymentName")
storage_account_name = stack_ref.get_output("storageAccountName")
blob_container_name = stack_ref.get_output("blobContainerName")

{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="python" from="24" to="31" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
        stackRef, err := pulumi.NewStackReference(ctx, "acmecorp/infra/dev", nil)
        if err != nil {
            return err
        }

        deploymentName := stackRef.GetOutput(pulumi.String("deploymentName"))
        storageAccountName := stackRef.GetOutput(pulumi.String("storageAccountName"))
        blobContainerName := stackRef.GetOutput(pulumi.String("blobContainerName"))

{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="go" from="39" to="46" >}}

		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;

return await Pulumi.Deployment.RunAsync(() =>
{

    var stackRef = new StackReference("acmecorp/infra/dev");

    var deploymentName = stackRef.GetOutput("deploymentName");
    var storageAccountName = stackRef.GetOutput("storageAccountName");
    var blobContainerName = stackRef.GetOutput("blobContainerName");

{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="csharp" from="31" to="39" >}}

});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: infra
runtime: yaml
description: A program to create a Stack Reference

resources:
  stack-ref:
    type: pulumi:pulumi:StackReference
    properties:
      name: acmecorp/infra/dev

{{< example-program-snippet path="k8s-deployment-service-for-minikube" language="yaml" from="20" to="29" >}}

variables:
  deploymentName: ${stack-ref.outputs["deploymentName"]}
  storageAccountName: ${stack-ref.outputs["storageAccountName"]}
  blobContainerName: ${stack-ref.outputs["blobContainerName"]}
```

{{% /choosable %}}

## Clean up

{{< cleanup >}}

## Next steps

In this tutorial, you created an Azure Blob Storage and Container resource. You also referenced the documentation to create a Blob object that would upload a file to the container. You exported resource properties into stack outputs, and referenced those outputs across stacks using stack references.

To learn more about creating and managing resources in Pulumi, take a look at the following resources:

- Learn more about creating resources in the [Creating Resources on Azure tutorial](/tutorials/creating-resources-azure/).
- Learn more about [stack outputs and references](/docs/concepts/stack/#stackreferences) in the Pulumi documentation.
- Learn more about [Pulumi inputs and outputs](/docs/concepts/inputs-outputs/) in the Pulumi documentation.
