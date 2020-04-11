
---
title: "GetJobQueue"
block_external_search_index: true
---



The Batch Job Queue data source allows access to details of a specific
job queue within AWS Batch.

{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const test_queue = pulumi.output(aws.batch.getJobQueue({
    name: "tf-test-batch-job-queue",
}, { async: true }));
```

{{% /example %}}
{{% /examples %}}





## Using GetJobQueue

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getJobQueue<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/batch/#GetJobQueueArgs">GetJobQueueArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/batch/#GetJobQueueResult">GetJobQueueResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_job_queue(</span>name=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupJobQueue<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/batch?tab=doc#LookupJobQueueArgs">LookupJobQueueArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/batch?tab=doc#LookupJobQueueResult">LookupJobQueueResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetJobQueue </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Batch.GetJobQueueResult.html">GetJobQueueResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Batch.GetJobQueueArgs.html">GetJobQueueArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the job queue.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the job queue.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the job queue.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the job queue.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetJobQueue Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the job queue.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Compute<wbr>Environment<wbr>Orders</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getjobqueuecomputeenvironmentorder">List&lt;Get<wbr>Job<wbr>Queue<wbr>Compute<wbr>Environment<wbr>Order&gt;</a></span>
    </dt>
    <dd>{{% md %}}The compute environments that are attached to the job queue and the order in
which job placement is preferred. Compute environments are selected for job placement in ascending order.
* `compute_environment_order.#.order` - The order of the compute environment.
* `compute_environment_order.#.compute_environment` - The ARN of the compute environment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The priority of the job queue. Job queues with a higher priority are evaluated first when
associated with the same compute environment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Describes the ability of the queue to accept new jobs (for example, `ENABLED` or `DISABLED`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The current status of the job queue (for example, `CREATING` or `VALID`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status<wbr>Reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A short, human-readable string to provide additional details about the current status
of the job queue.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the job queue.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Compute<wbr>Environment<wbr>Orders</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getjobqueuecomputeenvironmentorder">[]Get<wbr>Job<wbr>Queue<wbr>Compute<wbr>Environment<wbr>Order</a></span>
    </dt>
    <dd>{{% md %}}The compute environments that are attached to the job queue and the order in
which job placement is preferred. Compute environments are selected for job placement in ascending order.
* `compute_environment_order.#.order` - The order of the compute environment.
* `compute_environment_order.#.compute_environment` - The ARN of the compute environment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The priority of the job queue. Job queues with a higher priority are evaluated first when
associated with the same compute environment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Describes the ability of the queue to accept new jobs (for example, `ENABLED` or `DISABLED`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The current status of the job queue (for example, `CREATING` or `VALID`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status<wbr>Reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A short, human-readable string to provide additional details about the current status
of the job queue.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the job queue.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>compute<wbr>Environment<wbr>Orders</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getjobqueuecomputeenvironmentorder">Get<wbr>Job<wbr>Queue<wbr>Compute<wbr>Environment<wbr>Order[]</a></span>
    </dt>
    <dd>{{% md %}}The compute environments that are attached to the job queue and the order in
which job placement is preferred. Compute environments are selected for job placement in ascending order.
* `compute_environment_order.#.order` - The order of the compute environment.
* `compute_environment_order.#.compute_environment` - The ARN of the compute environment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The priority of the job queue. Job queues with a higher priority are evaluated first when
associated with the same compute environment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Describes the ability of the queue to accept new jobs (for example, `ENABLED` or `DISABLED`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The current status of the job queue (for example, `CREATING` or `VALID`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status<wbr>Reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A short, human-readable string to provide additional details about the current status
of the job queue.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the job queue.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>compute_<wbr>environment_<wbr>orders</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getjobqueuecomputeenvironmentorder">List[Get<wbr>Job<wbr>Queue<wbr>Compute<wbr>Environment<wbr>Order]</a></span>
    </dt>
    <dd>{{% md %}}The compute environments that are attached to the job queue and the order in
which job placement is preferred. Compute environments are selected for job placement in ascending order.
* `compute_environment_order.#.order` - The order of the compute environment.
* `compute_environment_order.#.compute_environment` - The ARN of the compute environment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The priority of the job queue. Job queues with a higher priority are evaluated first when
associated with the same compute environment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Describes the ability of the queue to accept new jobs (for example, `ENABLED` or `DISABLED`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The current status of the job queue (for example, `CREATING` or `VALID`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status_<wbr>reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A short, human-readable string to provide additional details about the current status
of the job queue.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Job<wbr>Queue<wbr>Compute<wbr>Environment<wbr>Order</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetJobQueueComputeEnvironmentOrder">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/batch?tab=doc#GetJobQueueComputeEnvironmentOrder">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Compute<wbr>Environment</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Order</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Compute<wbr>Environment</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Order</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>compute<wbr>Environment</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>order</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>compute<wbr>Environment</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>order</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}







