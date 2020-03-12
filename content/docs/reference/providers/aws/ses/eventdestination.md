
---
title: "EventDestination"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides an SES event destination

## Example Usage

### CloudWatch Destination

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const cloudwatch = new aws.ses.EventDestination("cloudwatch", {
    cloudwatchDestinations: [{
        defaultValue: "default",
        dimensionName: "dimension",
        valueSource: "emailHeader",
    }],
    configurationSetName: aws_ses_configuration_set_example.name,
    enabled: true,
    matchingTypes: [
        "bounce",
        "send",
    ],
});
```

### Kinesis Destination

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const kinesis = new aws.ses.EventDestination("kinesis", {
    configurationSetName: aws_ses_configuration_set_example.name,
    enabled: true,
    kinesisDestination: {
        roleArn: aws_iam_role_example.arn,
        streamArn: aws_kinesis_firehose_delivery_stream_example.arn,
    },
    matchingTypes: [
        "bounce",
        "send",
    ],
});
```

### SNS Destination

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const sns = new aws.ses.EventDestination("sns", {
    configurationSetName: aws_ses_configuration_set_example.name,
    enabled: true,
    matchingTypes: [
        "bounce",
        "send",
    ],
    snsDestination: {
        topicArn: aws_sns_topic_example.arn,
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_event_destination.markdown.



## Create a EventDestination Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ses/#EventDestination">EventDestination</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ses/#EventDestinationArgs">EventDestinationArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

```python
def EventDestination(resource_name, id, opts=None, cloudwatch_<wbr>destinations=None, configuration_<wbr>set_<wbr>name=None, enabled=None, kinesis_<wbr>destination=None, matching_<wbr>types=None, name=None, sns_<wbr>destination=None, __props__=None)
```

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewEventDestination<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#EventDestinationArgs">EventDestinationArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#EventDestination">EventDestination</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.EventDestination.html">EventDestination</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.EventDestinationArgs.html">EventDestinationArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a EventDestination resource with the given unique name, arguments, and options.

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
            <td class="align-top">Cloudwatch<wbr>Destinations</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationcloudwatchdestination">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Event<wbr>Destination<wbr>Cloudwatch<wbr>Destination<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
CloudWatch destination for the events
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the configuration set
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
If true, the event destination will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationkinesisdestination">Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Event<wbr>Destination<wbr>Kinesis<wbr>Destination<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Send the events to a kinesis firehose destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Matching<wbr>Types</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of matching types. May be any of `&#34;send&#34;`, `&#34;reject&#34;`, `&#34;bounce&#34;`, `&#34;complaint&#34;`, `&#34;delivery&#34;`, `&#34;open&#34;`, `&#34;click&#34;`, or `&#34;renderingFailure&#34;`.
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
The name of the event destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationsnsdestination">Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Event<wbr>Destination<wbr>Sns<wbr>Destination<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Send the events to an SNS Topic destination
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
            <td class="align-top">Cloudwatch<wbr>Destinations</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationcloudwatchdestination">[]ses.<wbr>Event<wbr>Destination<wbr>Cloudwatch<wbr>Destination</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
CloudWatch destination for the events
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the configuration set
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
If true, the event destination will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationkinesisdestination">*ses.<wbr>Event<wbr>Destination<wbr>Kinesis<wbr>Destination</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Send the events to a kinesis firehose destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Matching<wbr>Types</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of matching types. May be any of `&#34;send&#34;`, `&#34;reject&#34;`, `&#34;bounce&#34;`, `&#34;complaint&#34;`, `&#34;delivery&#34;`, `&#34;open&#34;`, `&#34;click&#34;`, or `&#34;renderingFailure&#34;`.
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
The name of the event destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationsnsdestination">*ses.<wbr>Event<wbr>Destination<wbr>Sns<wbr>Destination</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Send the events to an SNS Topic destination
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
            <td class="align-top">cloudwatch<wbr>Destinations</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationcloudwatchdestination">ses.<wbr>Event<wbr>Destination<wbr>Cloudwatch<wbr>Destination[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
CloudWatch destination for the events
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the configuration set
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
If true, the event destination will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationkinesisdestination">ses.<wbr>Event<wbr>Destination<wbr>Kinesis<wbr>Destination?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Send the events to a kinesis firehose destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">matching<wbr>Types</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of matching types. May be any of `&#34;send&#34;`, `&#34;reject&#34;`, `&#34;bounce&#34;`, `&#34;complaint&#34;`, `&#34;delivery&#34;`, `&#34;open&#34;`, `&#34;click&#34;`, or `&#34;renderingFailure&#34;`.
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
The name of the event destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationsnsdestination">ses.<wbr>Event<wbr>Destination<wbr>Sns<wbr>Destination?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Send the events to an SNS Topic destination
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
            <td class="align-top">cloudwatch_<wbr>destinations</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationcloudwatchdestination">list[event_<wbr>destination_<wbr>cloudwatch_<wbr>destination]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
CloudWatch destination for the events
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration_<wbr>set_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the configuration set
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
If true, the event destination will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis_<wbr>destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationkinesisdestination">dict{event_<wbr>destination_<wbr>kinesis_<wbr>destination}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Send the events to a kinesis firehose destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">matching_<wbr>types</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of matching types. May be any of `&#34;send&#34;`, `&#34;reject&#34;`, `&#34;bounce&#34;`, `&#34;complaint&#34;`, `&#34;delivery&#34;`, `&#34;open&#34;`, `&#34;click&#34;`, or `&#34;renderingFailure&#34;`.
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
The name of the event destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns_<wbr>destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationsnsdestination">dict{event_<wbr>destination_<wbr>sns_<wbr>destination}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Send the events to an SNS Topic destination
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## EventDestination Output Properties

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
            <td class="align-top">Cloudwatch<wbr>Destinations</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationcloudwatchdestination">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Event<wbr>Destination<wbr>Cloudwatch<wbr>Destination&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} CloudWatch destination for the events
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the configuration set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} If true, the event destination will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationkinesisdestination">Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Event<wbr>Destination<wbr>Kinesis<wbr>Destination?</a></code>
            </td>
            <td class="align-top">{{% md %}} Send the events to a kinesis firehose destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Matching<wbr>Types</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} A list of matching types. May be any of `&#34;send&#34;`, `&#34;reject&#34;`, `&#34;bounce&#34;`, `&#34;complaint&#34;`, `&#34;delivery&#34;`, `&#34;open&#34;`, `&#34;click&#34;`, or `&#34;renderingFailure&#34;`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the event destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationsnsdestination">Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Event<wbr>Destination<wbr>Sns<wbr>Destination?</a></code>
            </td>
            <td class="align-top">{{% md %}} Send the events to an SNS Topic destination
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
            <td class="align-top">Cloudwatch<wbr>Destinations</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationcloudwatchdestination">[]ses.<wbr>Event<wbr>Destination<wbr>Cloudwatch<wbr>Destination</a></code>
            </td>
            <td class="align-top">{{% md %}} CloudWatch destination for the events
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the configuration set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} If true, the event destination will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationkinesisdestination">*ses.<wbr>Event<wbr>Destination<wbr>Kinesis<wbr>Destination</a></code>
            </td>
            <td class="align-top">{{% md %}} Send the events to a kinesis firehose destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Matching<wbr>Types</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of matching types. May be any of `&#34;send&#34;`, `&#34;reject&#34;`, `&#34;bounce&#34;`, `&#34;complaint&#34;`, `&#34;delivery&#34;`, `&#34;open&#34;`, `&#34;click&#34;`, or `&#34;renderingFailure&#34;`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the event destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationsnsdestination">*ses.<wbr>Event<wbr>Destination<wbr>Sns<wbr>Destination</a></code>
            </td>
            <td class="align-top">{{% md %}} Send the events to an SNS Topic destination
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
            <td class="align-top">cloudwatch<wbr>Destinations</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationcloudwatchdestination">ses.<wbr>Event<wbr>Destination<wbr>Cloudwatch<wbr>Destination[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} CloudWatch destination for the events
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the configuration set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} If true, the event destination will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationkinesisdestination">ses.<wbr>Event<wbr>Destination<wbr>Kinesis<wbr>Destination?</a></code>
            </td>
            <td class="align-top">{{% md %}} Send the events to a kinesis firehose destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">matching<wbr>Types</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} A list of matching types. May be any of `&#34;send&#34;`, `&#34;reject&#34;`, `&#34;bounce&#34;`, `&#34;complaint&#34;`, `&#34;delivery&#34;`, `&#34;open&#34;`, `&#34;click&#34;`, or `&#34;renderingFailure&#34;`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the event destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationsnsdestination">ses.<wbr>Event<wbr>Destination<wbr>Sns<wbr>Destination?</a></code>
            </td>
            <td class="align-top">{{% md %}} Send the events to an SNS Topic destination
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
            <td class="align-top">cloudwatch_<wbr>destinations</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationcloudwatchdestination">list[event_<wbr>destination_<wbr>cloudwatch_<wbr>destination]</a></code>
            </td>
            <td class="align-top">{{% md %}} CloudWatch destination for the events
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration_<wbr>set_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the configuration set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If true, the event destination will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis_<wbr>destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationkinesisdestination">dict{event_<wbr>destination_<wbr>kinesis_<wbr>destination}</a></code>
            </td>
            <td class="align-top">{{% md %}} Send the events to a kinesis firehose destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">matching_<wbr>types</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} A list of matching types. May be any of `&#34;send&#34;`, `&#34;reject&#34;`, `&#34;bounce&#34;`, `&#34;complaint&#34;`, `&#34;delivery&#34;`, `&#34;open&#34;`, `&#34;click&#34;`, or `&#34;renderingFailure&#34;`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the event destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns_<wbr>destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationsnsdestination">dict{event_<wbr>destination_<wbr>sns_<wbr>destination}</a></code>
            </td>
            <td class="align-top">{{% md %}} Send the events to an SNS Topic destination
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing EventDestination Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventDestinationState, opts?: pulumi.CustomResourceOptions): EventDestination;
```

```python
def get(resource_name, id, opts=None, cloudwatch_<wbr>destinations=None, configuration_<wbr>set_<wbr>name=None, enabled=None, kinesis_<wbr>destination=None, matching_<wbr>types=None, name=None, sns_<wbr>destination=None)
```

```go
func GetEventDestination(ctx *pulumi.Context, name string, id pulumi.IDInput, state *EventDestinationState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static EventDestination Get(string name, Input<string> id, EventDestinationState? state = null, CustomResourceOptions? options = null);
```

Get an existing EventDestination resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Cloudwatch<wbr>Destinations</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationcloudwatchdestination">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Event<wbr>Destination<wbr>Cloudwatch<wbr>Destination<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
CloudWatch destination for the events
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the configuration set
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
If true, the event destination will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationkinesisdestination">Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Event<wbr>Destination<wbr>Kinesis<wbr>Destination<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Send the events to a kinesis firehose destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Matching<wbr>Types</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of matching types. May be any of `&#34;send&#34;`, `&#34;reject&#34;`, `&#34;bounce&#34;`, `&#34;complaint&#34;`, `&#34;delivery&#34;`, `&#34;open&#34;`, `&#34;click&#34;`, or `&#34;renderingFailure&#34;`.
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
The name of the event destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationsnsdestination">Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Event<wbr>Destination<wbr>Sns<wbr>Destination<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Send the events to an SNS Topic destination
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
            <td class="align-top">Cloudwatch<wbr>Destinations</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationcloudwatchdestination">[]ses.<wbr>Event<wbr>Destination<wbr>Cloudwatch<wbr>Destination</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
CloudWatch destination for the events
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the configuration set
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
If true, the event destination will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationkinesisdestination">*ses.<wbr>Event<wbr>Destination<wbr>Kinesis<wbr>Destination</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Send the events to a kinesis firehose destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Matching<wbr>Types</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of matching types. May be any of `&#34;send&#34;`, `&#34;reject&#34;`, `&#34;bounce&#34;`, `&#34;complaint&#34;`, `&#34;delivery&#34;`, `&#34;open&#34;`, `&#34;click&#34;`, or `&#34;renderingFailure&#34;`.
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
The name of the event destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationsnsdestination">*ses.<wbr>Event<wbr>Destination<wbr>Sns<wbr>Destination</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Send the events to an SNS Topic destination
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
            <td class="align-top">cloudwatch<wbr>Destinations</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationcloudwatchdestination">ses.<wbr>Event<wbr>Destination<wbr>Cloudwatch<wbr>Destination[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
CloudWatch destination for the events
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the configuration set
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
If true, the event destination will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationkinesisdestination">ses.<wbr>Event<wbr>Destination<wbr>Kinesis<wbr>Destination?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Send the events to a kinesis firehose destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">matching<wbr>Types</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of matching types. May be any of `&#34;send&#34;`, `&#34;reject&#34;`, `&#34;bounce&#34;`, `&#34;complaint&#34;`, `&#34;delivery&#34;`, `&#34;open&#34;`, `&#34;click&#34;`, or `&#34;renderingFailure&#34;`.
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
The name of the event destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns<wbr>Destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationsnsdestination">ses.<wbr>Event<wbr>Destination<wbr>Sns<wbr>Destination?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Send the events to an SNS Topic destination
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
            <td class="align-top">cloudwatch_<wbr>destinations</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationcloudwatchdestination">list[event_<wbr>destination_<wbr>cloudwatch_<wbr>destination]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
CloudWatch destination for the events
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration_<wbr>set_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the configuration set
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
If true, the event destination will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis_<wbr>destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationkinesisdestination">dict{event_<wbr>destination_<wbr>kinesis_<wbr>destination}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Send the events to a kinesis firehose destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">matching_<wbr>types</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of matching types. May be any of `&#34;send&#34;`, `&#34;reject&#34;`, `&#34;bounce&#34;`, `&#34;complaint&#34;`, `&#34;delivery&#34;`, `&#34;open&#34;`, `&#34;click&#34;`, or `&#34;renderingFailure&#34;`.
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
The name of the event destination
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns_<wbr>destination</td>
            <td class="align-top">
                
                <code><a href="#eventdestinationsnsdestination">dict{event_<wbr>destination_<wbr>sns_<wbr>destination}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Send the events to an SNS Topic destination
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### EventDestinationCloudwatchDestination
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#EventDestinationCloudwatchDestination">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#EventDestinationCloudwatchDestination">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#EventDestinationCloudwatchDestinationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#EventDestinationCloudwatchDestinationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.EventDestinationCloudwatchDestinationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.EventDestinationCloudwatchDestination.html">output</a> API doc for this type.
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
            <td class="align-top">Default<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The default value for the event
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dimension<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name for the dimension
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value<wbr>Source</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The source for the value. It can be either `&#34;messageTag&#34;` or `&#34;emailHeader&#34;`
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
            <td class="align-top">Default<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The default value for the event
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dimension<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name for the dimension
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value<wbr>Source</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The source for the value. It can be either `&#34;messageTag&#34;` or `&#34;emailHeader&#34;`
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
            <td class="align-top">default<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The default value for the event
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dimension<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name for the dimension
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value<wbr>Source</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The source for the value. It can be either `&#34;messageTag&#34;` or `&#34;emailHeader&#34;`
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
            <td class="align-top">default_<wbr>value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The default value for the event
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dimension_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name for the dimension
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value_<wbr>source</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The source for the value. It can be either `&#34;messageTag&#34;` or `&#34;emailHeader&#34;`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### EventDestinationKinesisDestination
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#EventDestinationKinesisDestination">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#EventDestinationKinesisDestination">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#EventDestinationKinesisDestinationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#EventDestinationKinesisDestinationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.EventDestinationKinesisDestinationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.EventDestinationKinesisDestination.html">output</a> API doc for this type.
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
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the role that has permissions to access the Kinesis Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Kinesis Stream
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
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the role that has permissions to access the Kinesis Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Kinesis Stream
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
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the role that has permissions to access the Kinesis Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Kinesis Stream
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
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the role that has permissions to access the Kinesis Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Kinesis Stream
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### EventDestinationSnsDestination
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#EventDestinationSnsDestination">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#EventDestinationSnsDestination">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#EventDestinationSnsDestinationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#EventDestinationSnsDestinationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.EventDestinationSnsDestinationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.EventDestinationSnsDestination.html">output</a> API doc for this type.
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
            <td class="align-top">Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the SNS topic
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
            <td class="align-top">Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the SNS topic
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
            <td class="align-top">topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the SNS topic
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
            <td class="align-top">topic_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the SNS topic
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







