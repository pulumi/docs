
---
title: "SmsPreferences"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides a way to set SNS SMS preferences.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const updateSmsPrefs = new aws.sns.SmsPreferences("update_sms_prefs", {});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sns_sms_preferences.html.markdown.



## Create a SmsPreferences Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/sns/#SmsPreferences">SmsPreferences</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/sns/#SmsPreferencesArgs">SmsPreferencesArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

```python
def SmsPreferences(resource_name, id, opts=None, default_<wbr>sender_<wbr>id=None, default_<wbr>sms_<wbr>type=None, delivery_<wbr>status_<wbr>iam_<wbr>role_<wbr>arn=None, delivery_<wbr>status_<wbr>success_<wbr>sampling_<wbr>rate=None, monthly_<wbr>spend_<wbr>limit=None, usage_<wbr>report_<wbr>s3_<wbr>bucket=None, __props__=None)
```

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewSmsPreferences<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sns?tab=doc#SmsPreferencesArgs">SmsPreferencesArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sns?tab=doc#SmsPreferences">SmsPreferences</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Sns.SmsPreferences.html">SmsPreferences</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Sns.SmsPreferencesArgs.html">SmsPreferencesArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a SmsPreferences resource with the given unique name, arguments, and options.

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
            <td class="align-top">Default<wbr>Sender<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string, such as your business brand, that is displayed as the sender on the receiving device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Sms<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of SMS message that you will send by default. Possible values are: Promotional, Transactional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delivery<wbr>Status<wbr>Iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delivery<wbr>Status<wbr>Success<wbr>Sampling<wbr>Rate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monthly<wbr>Spend<wbr>Limit</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount in USD that you are willing to spend each month to send SMS messages.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Usage<wbr>Report<wbr>S3Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.
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
            <td class="align-top">Default<wbr>Sender<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string, such as your business brand, that is displayed as the sender on the receiving device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Sms<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of SMS message that you will send by default. Possible values are: Promotional, Transactional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delivery<wbr>Status<wbr>Iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delivery<wbr>Status<wbr>Success<wbr>Sampling<wbr>Rate</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monthly<wbr>Spend<wbr>Limit</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount in USD that you are willing to spend each month to send SMS messages.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Usage<wbr>Report<wbr>S3Bucket</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.
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
            <td class="align-top">default<wbr>Sender<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string, such as your business brand, that is displayed as the sender on the receiving device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Sms<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of SMS message that you will send by default. Possible values are: Promotional, Transactional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delivery<wbr>Status<wbr>Iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delivery<wbr>Status<wbr>Success<wbr>Sampling<wbr>Rate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monthly<wbr>Spend<wbr>Limit</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount in USD that you are willing to spend each month to send SMS messages.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">usage<wbr>Report<wbr>S3Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.
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
            <td class="align-top">default_<wbr>sender_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string, such as your business brand, that is displayed as the sender on the receiving device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>sms_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of SMS message that you will send by default. Possible values are: Promotional, Transactional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delivery_<wbr>status_<wbr>iam_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delivery_<wbr>status_<wbr>success_<wbr>sampling_<wbr>rate</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monthly_<wbr>spend_<wbr>limit</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount in USD that you are willing to spend each month to send SMS messages.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">usage_<wbr>report_<wbr>s3_<wbr>bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## SmsPreferences Output Properties

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
            <td class="align-top">Default<wbr>Sender<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A string, such as your business brand, that is displayed as the sender on the receiving device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Sms<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The type of SMS message that you will send by default. Possible values are: Promotional, Transactional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delivery<wbr>Status<wbr>Iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delivery<wbr>Status<wbr>Success<wbr>Sampling<wbr>Rate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monthly<wbr>Spend<wbr>Limit</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The maximum amount in USD that you are willing to spend each month to send SMS messages.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Usage<wbr>Report<wbr>S3Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.
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
            <td class="align-top">Default<wbr>Sender<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} A string, such as your business brand, that is displayed as the sender on the receiving device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Sms<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The type of SMS message that you will send by default. Possible values are: Promotional, Transactional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delivery<wbr>Status<wbr>Iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delivery<wbr>Status<wbr>Success<wbr>Sampling<wbr>Rate</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monthly<wbr>Spend<wbr>Limit</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The maximum amount in USD that you are willing to spend each month to send SMS messages.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Usage<wbr>Report<wbr>S3Bucket</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.
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
            <td class="align-top">default<wbr>Sender<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A string, such as your business brand, that is displayed as the sender on the receiving device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Sms<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The type of SMS message that you will send by default. Possible values are: Promotional, Transactional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delivery<wbr>Status<wbr>Iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delivery<wbr>Status<wbr>Success<wbr>Sampling<wbr>Rate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monthly<wbr>Spend<wbr>Limit</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The maximum amount in USD that you are willing to spend each month to send SMS messages.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">usage<wbr>Report<wbr>S3Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.
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
            <td class="align-top">default_<wbr>sender_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A string, such as your business brand, that is displayed as the sender on the receiving device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>sms_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type of SMS message that you will send by default. Possible values are: Promotional, Transactional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delivery_<wbr>status_<wbr>iam_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delivery_<wbr>status_<wbr>success_<wbr>sampling_<wbr>rate</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monthly_<wbr>spend_<wbr>limit</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The maximum amount in USD that you are willing to spend each month to send SMS messages.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">usage_<wbr>report_<wbr>s3_<wbr>bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing SmsPreferences Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SmsPreferencesState, opts?: pulumi.CustomResourceOptions): SmsPreferences;
```

```python
def get(resource_name, id, opts=None, default_<wbr>sender_<wbr>id=None, default_<wbr>sms_<wbr>type=None, delivery_<wbr>status_<wbr>iam_<wbr>role_<wbr>arn=None, delivery_<wbr>status_<wbr>success_<wbr>sampling_<wbr>rate=None, monthly_<wbr>spend_<wbr>limit=None, usage_<wbr>report_<wbr>s3_<wbr>bucket=None)
```

```go
func GetSmsPreferences(ctx *pulumi.Context, name string, id pulumi.IDInput, state *SmsPreferencesState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static SmsPreferences Get(string name, Input<string> id, SmsPreferencesState? state = null, CustomResourceOptions? options = null);
```

Get an existing SmsPreferences resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Default<wbr>Sender<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string, such as your business brand, that is displayed as the sender on the receiving device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Sms<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of SMS message that you will send by default. Possible values are: Promotional, Transactional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delivery<wbr>Status<wbr>Iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delivery<wbr>Status<wbr>Success<wbr>Sampling<wbr>Rate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monthly<wbr>Spend<wbr>Limit</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount in USD that you are willing to spend each month to send SMS messages.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Usage<wbr>Report<wbr>S3Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.
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
            <td class="align-top">Default<wbr>Sender<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string, such as your business brand, that is displayed as the sender on the receiving device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Sms<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of SMS message that you will send by default. Possible values are: Promotional, Transactional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delivery<wbr>Status<wbr>Iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delivery<wbr>Status<wbr>Success<wbr>Sampling<wbr>Rate</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monthly<wbr>Spend<wbr>Limit</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount in USD that you are willing to spend each month to send SMS messages.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Usage<wbr>Report<wbr>S3Bucket</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.
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
            <td class="align-top">default<wbr>Sender<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string, such as your business brand, that is displayed as the sender on the receiving device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Sms<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of SMS message that you will send by default. Possible values are: Promotional, Transactional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delivery<wbr>Status<wbr>Iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delivery<wbr>Status<wbr>Success<wbr>Sampling<wbr>Rate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monthly<wbr>Spend<wbr>Limit</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount in USD that you are willing to spend each month to send SMS messages.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">usage<wbr>Report<wbr>S3Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.
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
            <td class="align-top">default_<wbr>sender_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string, such as your business brand, that is displayed as the sender on the receiving device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>sms_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of SMS message that you will send by default. Possible values are: Promotional, Transactional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delivery_<wbr>status_<wbr>iam_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delivery_<wbr>status_<wbr>success_<wbr>sampling_<wbr>rate</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monthly_<wbr>spend_<wbr>limit</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount in USD that you are willing to spend each month to send SMS messages.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">usage_<wbr>report_<wbr>s3_<wbr>bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}









