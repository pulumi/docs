
---
title: "getFunction"
title_tag: "aws.cloudtrail.getFunction"
meta_desc: "Documentation for the aws.cloudtrail.getFunction function with examples, input properties, output properties, and supporting types."
---



<!-- WARNING: this file was generated by Pulumi Docs Generator. -->
<!-- Do not edit by hand unless you're certain you know what you are doing! -->

Provides information about a CloudFront Function.


{{% examples %}}

## Example Usage

{{< chooser language "typescript,python,go,csharp" / >}}





{{< example csharp >}}

```csharp
using Pulumi;
using Aws = Pulumi.Aws;

class MyStack : Stack
{
    public MyStack()
    {
        var config = new Config();
        var functionName = config.Require("functionName");
        var existing = Output.Create(Aws.CloudTrail.GetFunction.InvokeAsync(new Aws.CloudTrail.GetFunctionArgs
        {
            Name = functionName,
        }));
    }

}
```


{{< /example >}}


{{< example go >}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v4/go/aws/cloudtrail"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		cfg := config.New(ctx, "")
		functionName := cfg.Require("functionName")
		_, err := cloudtrail.GetFunction(ctx, &cloudtrail.GetFunctionArgs{
			Name: functionName,
		}, nil)
		if err != nil {
			return err
		}
		return nil
	})
}
```


{{< /example >}}


{{< example python >}}

```python
import pulumi
import pulumi_aws as aws

config = pulumi.Config()
function_name = config.require("functionName")
existing = aws.cloudtrail.get_function(name=function_name)
```


{{< /example >}}


{{< example typescript >}}


```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const config = new pulumi.Config();
const functionName = config.require("functionName");
const existing = aws.cloudtrail.getFunction({
    name: functionName,
});
```


{{< /example >}}





{{% /examples %}}




## Using getFunction {#using}

{{< chooser language "typescript,python,go,csharp" / >}}


{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getFunction<span class="p">(</span><span class="nx">args</span><span class="p">:</span> <span class="nx">GetFunctionArgs</span><span class="p">,</span> <span class="nx">opts</span><span class="p">?:</span> <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="#result">GetFunctionResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span>get_function(</span><span class="nx">name</span><span class="p">:</span> <span class="nx">Optional[str]</span> = None<span class="p">,</span>
                 <span class="nx">stage</span><span class="p">:</span> <span class="nx">Optional[str]</span> = None<span class="p">,</span>
                 <span class="nx">opts</span><span class="p">:</span> <span class="nx"><a href="/docs/reference/pkg/python/pulumi/#pulumi.InvokeOptions">Optional[InvokeOptions]</a></span> = None<span class="p">) -&gt;</span> GetFunctionResult</code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetFunction<span class="p">(</span><span class="nx">ctx</span><span class="p"> *</span><span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">,</span> <span class="nx">args</span><span class="p"> *</span><span class="nx">GetFunctionArgs</span><span class="p">,</span> <span class="nx">opts</span><span class="p"> ...</span><span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="#result">GetFunctionResult</a></span>, error)</span></code></pre></div>

> Note: This function is named `GetFunction` in the Go SDK.

{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetFunction </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="#result">GetFunctionResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx">GetFunctionArgs</span><span class="p"> </span><span class="nx">args<span class="p">,</span> <span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span><span class="p">? </span><span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:


{{% choosable language csharp %}}
<dl class="resources-properties"><dt class="property-required"
            title="Required">
        <span id="name_csharp">
<a href="#name_csharp" style="color: inherit; text-decoration: inherit;">Name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the CloudFront function.
{{% /md %}}</dd><dt class="property-required"
            title="Required">
        <span id="stage_csharp">
<a href="#stage_csharp" style="color: inherit; text-decoration: inherit;">Stage</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The function’s stage, either `DEVELOPMENT` or `LIVE`.
{{% /md %}}</dd></dl>
{{% /choosable %}}

{{% choosable language go %}}
<dl class="resources-properties"><dt class="property-required"
            title="Required">
        <span id="name_go">
<a href="#name_go" style="color: inherit; text-decoration: inherit;">Name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the CloudFront function.
{{% /md %}}</dd><dt class="property-required"
            title="Required">
        <span id="stage_go">
<a href="#stage_go" style="color: inherit; text-decoration: inherit;">Stage</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The function’s stage, either `DEVELOPMENT` or `LIVE`.
{{% /md %}}</dd></dl>
{{% /choosable %}}

{{% choosable language nodejs %}}
<dl class="resources-properties"><dt class="property-required"
            title="Required">
        <span id="name_nodejs">
<a href="#name_nodejs" style="color: inherit; text-decoration: inherit;">name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the CloudFront function.
{{% /md %}}</dd><dt class="property-required"
            title="Required">
        <span id="stage_nodejs">
<a href="#stage_nodejs" style="color: inherit; text-decoration: inherit;">stage</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The function’s stage, either `DEVELOPMENT` or `LIVE`.
{{% /md %}}</dd></dl>
{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties"><dt class="property-required"
            title="Required">
        <span id="name_python">
<a href="#name_python" style="color: inherit; text-decoration: inherit;">name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the CloudFront function.
{{% /md %}}</dd><dt class="property-required"
            title="Required">
        <span id="stage_python">
<a href="#stage_python" style="color: inherit; text-decoration: inherit;">stage</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The function’s stage, either `DEVELOPMENT` or `LIVE`.
{{% /md %}}</dd></dl>
{{% /choosable %}}




## getFunction Result {#result}

The following output properties are available:



{{% choosable language csharp %}}
<dl class="resources-properties"><dt class="property-"
            title="">
        <span id="arn_csharp">
<a href="#arn_csharp" style="color: inherit; text-decoration: inherit;">Arn</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name (ARN) identifying your CloudFront Function.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="code_csharp">
<a href="#code_csharp" style="color: inherit; text-decoration: inherit;">Code</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Source code of the function
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="comment_csharp">
<a href="#comment_csharp" style="color: inherit; text-decoration: inherit;">Comment</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Comment.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="etag_csharp">
<a href="#etag_csharp" style="color: inherit; text-decoration: inherit;">Etag</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ETag hash of the function
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="id_csharp">
<a href="#id_csharp" style="color: inherit; text-decoration: inherit;">Id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The provider-assigned unique ID for this managed resource.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="lastmodifiedtime_csharp">
<a href="#lastmodifiedtime_csharp" style="color: inherit; text-decoration: inherit;">Last<wbr>Modified<wbr>Time</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}When this resource was last modified.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="name_csharp">
<a href="#name_csharp" style="color: inherit; text-decoration: inherit;">Name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="runtime_csharp">
<a href="#runtime_csharp" style="color: inherit; text-decoration: inherit;">Runtime</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Identifier of the function's runtime.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="stage_csharp">
<a href="#stage_csharp" style="color: inherit; text-decoration: inherit;">Stage</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="status_csharp">
<a href="#status_csharp" style="color: inherit; text-decoration: inherit;">Status</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Status of the function. Can be `UNPUBLISHED`, `UNASSOCIATED` or `ASSOCIATED`.
{{% /md %}}</dd></dl>
{{% /choosable %}}

{{% choosable language go %}}
<dl class="resources-properties"><dt class="property-"
            title="">
        <span id="arn_go">
<a href="#arn_go" style="color: inherit; text-decoration: inherit;">Arn</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name (ARN) identifying your CloudFront Function.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="code_go">
<a href="#code_go" style="color: inherit; text-decoration: inherit;">Code</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Source code of the function
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="comment_go">
<a href="#comment_go" style="color: inherit; text-decoration: inherit;">Comment</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Comment.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="etag_go">
<a href="#etag_go" style="color: inherit; text-decoration: inherit;">Etag</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ETag hash of the function
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="id_go">
<a href="#id_go" style="color: inherit; text-decoration: inherit;">Id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The provider-assigned unique ID for this managed resource.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="lastmodifiedtime_go">
<a href="#lastmodifiedtime_go" style="color: inherit; text-decoration: inherit;">Last<wbr>Modified<wbr>Time</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}When this resource was last modified.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="name_go">
<a href="#name_go" style="color: inherit; text-decoration: inherit;">Name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="runtime_go">
<a href="#runtime_go" style="color: inherit; text-decoration: inherit;">Runtime</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Identifier of the function's runtime.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="stage_go">
<a href="#stage_go" style="color: inherit; text-decoration: inherit;">Stage</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="status_go">
<a href="#status_go" style="color: inherit; text-decoration: inherit;">Status</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Status of the function. Can be `UNPUBLISHED`, `UNASSOCIATED` or `ASSOCIATED`.
{{% /md %}}</dd></dl>
{{% /choosable %}}

{{% choosable language nodejs %}}
<dl class="resources-properties"><dt class="property-"
            title="">
        <span id="arn_nodejs">
<a href="#arn_nodejs" style="color: inherit; text-decoration: inherit;">arn</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name (ARN) identifying your CloudFront Function.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="code_nodejs">
<a href="#code_nodejs" style="color: inherit; text-decoration: inherit;">code</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Source code of the function
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="comment_nodejs">
<a href="#comment_nodejs" style="color: inherit; text-decoration: inherit;">comment</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Comment.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="etag_nodejs">
<a href="#etag_nodejs" style="color: inherit; text-decoration: inherit;">etag</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ETag hash of the function
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="id_nodejs">
<a href="#id_nodejs" style="color: inherit; text-decoration: inherit;">id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The provider-assigned unique ID for this managed resource.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="lastmodifiedtime_nodejs">
<a href="#lastmodifiedtime_nodejs" style="color: inherit; text-decoration: inherit;">last<wbr>Modified<wbr>Time</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}When this resource was last modified.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="name_nodejs">
<a href="#name_nodejs" style="color: inherit; text-decoration: inherit;">name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="runtime_nodejs">
<a href="#runtime_nodejs" style="color: inherit; text-decoration: inherit;">runtime</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Identifier of the function's runtime.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="stage_nodejs">
<a href="#stage_nodejs" style="color: inherit; text-decoration: inherit;">stage</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="status_nodejs">
<a href="#status_nodejs" style="color: inherit; text-decoration: inherit;">status</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Status of the function. Can be `UNPUBLISHED`, `UNASSOCIATED` or `ASSOCIATED`.
{{% /md %}}</dd></dl>
{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties"><dt class="property-"
            title="">
        <span id="arn_python">
<a href="#arn_python" style="color: inherit; text-decoration: inherit;">arn</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name (ARN) identifying your CloudFront Function.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="code_python">
<a href="#code_python" style="color: inherit; text-decoration: inherit;">code</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Source code of the function
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="comment_python">
<a href="#comment_python" style="color: inherit; text-decoration: inherit;">comment</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Comment.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="etag_python">
<a href="#etag_python" style="color: inherit; text-decoration: inherit;">etag</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ETag hash of the function
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="id_python">
<a href="#id_python" style="color: inherit; text-decoration: inherit;">id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The provider-assigned unique ID for this managed resource.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="last_modified_time_python">
<a href="#last_modified_time_python" style="color: inherit; text-decoration: inherit;">last_<wbr>modified_<wbr>time</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}When this resource was last modified.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="name_python">
<a href="#name_python" style="color: inherit; text-decoration: inherit;">name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="runtime_python">
<a href="#runtime_python" style="color: inherit; text-decoration: inherit;">runtime</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Identifier of the function's runtime.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="stage_python">
<a href="#stage_python" style="color: inherit; text-decoration: inherit;">stage</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="status_python">
<a href="#status_python" style="color: inherit; text-decoration: inherit;">status</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Status of the function. Can be `UNPUBLISHED`, `UNASSOCIATED` or `ASSOCIATED`.
{{% /md %}}</dd></dl>
{{% /choosable %}}





<h2 id="package-details">Package Details</h2>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-aws">https://github.com/pulumi/pulumi-aws</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
	<dt>Notes</dt>
	<dd>{{% md %}}This Pulumi package is based on the [`aws` Terraform Provider](https://github.com/terraform-providers/terraform-provider-aws).{{% /md %}}</dd>
</dl>

