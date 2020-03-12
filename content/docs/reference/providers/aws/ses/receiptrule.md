
---
title: "ReceiptRule"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides an SES receipt rule resource

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Add a header to the email and store it in S3
const store = new aws.ses.ReceiptRule("store", {
    addHeaderActions: [{
        headerName: "Custom-Header",
        headerValue: "Added by SES",
        position: 1,
    }],
    enabled: true,
    recipients: ["karen@example.com"],
    ruleSetName: "default-rule-set",
    s3Actions: [{
        bucketName: "emails",
        position: 2,
    }],
    scanEnabled: true,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_receipt_rule.html.markdown.



## Create a ReceiptRule Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ses/#ReceiptRule">ReceiptRule</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ses/#ReceiptRuleArgs">ReceiptRuleArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

```python
def ReceiptRule(resource_name, id, opts=None, add_<wbr>header_<wbr>actions=None, after=None, bounce_<wbr>actions=None, enabled=None, lambda_<wbr>actions=None, name=None, recipients=None, rule_<wbr>set_<wbr>name=None, s3_<wbr>actions=None, scan_<wbr>enabled=None, sns_<wbr>actions=None, stop_<wbr>actions=None, tls_<wbr>policy=None, workmail_<wbr>actions=None, __props__=None)
```

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewReceiptRule<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#ReceiptRuleArgs">ReceiptRuleArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#ReceiptRule">ReceiptRule</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.ReceiptRule.html">ReceiptRule</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.ReceiptRuleArgs.html">ReceiptRuleArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a ReceiptRule resource with the given unique name, arguments, and options.

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
            <td class="align-top">Add<wbr>Header<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleaddheaderaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Add<wbr>Header<wbr>Action<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Add Header Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">After</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule to place this rule after
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bounce<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulebounceaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Bounce<wbr>Action<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Bounce Action blocks. Documented below.
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
If true, the rule will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulelambdaaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Lambda<wbr>Action<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Lambda Action blocks. Documented below.
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
The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Recipients</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of email addresses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the rule set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrules3action">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>S3Action<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of S3 Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scan<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, incoming emails will be scanned for spam and viruses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulesnsaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Sns<wbr>Action<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of SNS Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stop<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulestopaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Stop<wbr>Action<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Stop Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tls<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Require or Optional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Workmail<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleworkmailaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Workmail<wbr>Action<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of WorkMail Action blocks. Documented below.
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
            <td class="align-top">Add<wbr>Header<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleaddheaderaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Add<wbr>Header<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Add Header Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">After</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule to place this rule after
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bounce<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulebounceaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Bounce<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Bounce Action blocks. Documented below.
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
If true, the rule will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulelambdaaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Lambda<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Lambda Action blocks. Documented below.
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
The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Recipients</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of email addresses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the rule set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrules3action">[]ses.<wbr>Receipt<wbr>Rule<wbr>S3Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of S3 Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scan<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, incoming emails will be scanned for spam and viruses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulesnsaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Sns<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of SNS Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stop<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulestopaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Stop<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Stop Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tls<wbr>Policy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Require or Optional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Workmail<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleworkmailaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Workmail<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of WorkMail Action blocks. Documented below.
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
            <td class="align-top">add<wbr>Header<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleaddheaderaction">ses.<wbr>Receipt<wbr>Rule<wbr>Add<wbr>Header<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Add Header Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">after</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule to place this rule after
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bounce<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulebounceaction">ses.<wbr>Receipt<wbr>Rule<wbr>Bounce<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Bounce Action blocks. Documented below.
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
If true, the rule will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulelambdaaction">ses.<wbr>Receipt<wbr>Rule<wbr>Lambda<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Lambda Action blocks. Documented below.
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
The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">recipients</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of email addresses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the rule set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrules3action">ses.<wbr>Receipt<wbr>Rule<wbr>S3Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of S3 Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scan<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, incoming emails will be scanned for spam and viruses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulesnsaction">ses.<wbr>Receipt<wbr>Rule<wbr>Sns<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of SNS Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stop<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulestopaction">ses.<wbr>Receipt<wbr>Rule<wbr>Stop<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Stop Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tls<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Require or Optional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">workmail<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleworkmailaction">ses.<wbr>Receipt<wbr>Rule<wbr>Workmail<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of WorkMail Action blocks. Documented below.
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
            <td class="align-top">add_<wbr>header_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleaddheaderaction">list[receipt_<wbr>rule_<wbr>add_<wbr>header_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Add Header Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">after</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule to place this rule after
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bounce_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulebounceaction">list[receipt_<wbr>rule_<wbr>bounce_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Bounce Action blocks. Documented below.
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
If true, the rule will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulelambdaaction">list[receipt_<wbr>rule_<wbr>lambda_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Lambda Action blocks. Documented below.
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
The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">recipients</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of email addresses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule_<wbr>set_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the rule set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrules3action">list[receipt_<wbr>rule_<wbr>s3_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of S3 Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scan_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, incoming emails will be scanned for spam and viruses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulesnsaction">list[receipt_<wbr>rule_<wbr>sns_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of SNS Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stop_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulestopaction">list[receipt_<wbr>rule_<wbr>stop_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Stop Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tls_<wbr>policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Require or Optional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">workmail_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleworkmailaction">list[receipt_<wbr>rule_<wbr>workmail_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of WorkMail Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## ReceiptRule Output Properties

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
            <td class="align-top">Add<wbr>Header<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleaddheaderaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Add<wbr>Header<wbr>Action&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of Add Header Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">After</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule to place this rule after
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bounce<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulebounceaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Bounce<wbr>Action&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of Bounce Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If true, the rule will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulelambdaaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Lambda<wbr>Action&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of Lambda Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Recipients</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A list of email addresses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrules3action">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>S3Action&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of S3 Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scan<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If true, incoming emails will be scanned for spam and viruses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulesnsaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Sns<wbr>Action&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of SNS Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stop<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulestopaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Stop<wbr>Action&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of Stop Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tls<wbr>Policy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Require or Optional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Workmail<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleworkmailaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Workmail<wbr>Action&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of WorkMail Action blocks. Documented below.
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
            <td class="align-top">Add<wbr>Header<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleaddheaderaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Add<wbr>Header<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of Add Header Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">After</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule to place this rule after
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bounce<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulebounceaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Bounce<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of Bounce Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If true, the rule will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulelambdaaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Lambda<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of Lambda Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Recipients</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of email addresses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrules3action">[]ses.<wbr>Receipt<wbr>Rule<wbr>S3Action</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of S3 Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scan<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If true, incoming emails will be scanned for spam and viruses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulesnsaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Sns<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of SNS Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stop<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulestopaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Stop<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of Stop Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tls<wbr>Policy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Require or Optional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Workmail<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleworkmailaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Workmail<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of WorkMail Action blocks. Documented below.
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
            <td class="align-top">add<wbr>Header<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleaddheaderaction">ses.<wbr>Receipt<wbr>Rule<wbr>Add<wbr>Header<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of Add Header Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">after</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule to place this rule after
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bounce<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulebounceaction">ses.<wbr>Receipt<wbr>Rule<wbr>Bounce<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of Bounce Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} If true, the rule will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulelambdaaction">ses.<wbr>Receipt<wbr>Rule<wbr>Lambda<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of Lambda Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">recipients</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} A list of email addresses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrules3action">ses.<wbr>Receipt<wbr>Rule<wbr>S3Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of S3 Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scan<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} If true, incoming emails will be scanned for spam and viruses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulesnsaction">ses.<wbr>Receipt<wbr>Rule<wbr>Sns<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of SNS Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stop<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulestopaction">ses.<wbr>Receipt<wbr>Rule<wbr>Stop<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of Stop Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tls<wbr>Policy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Require or Optional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">workmail<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleworkmailaction">ses.<wbr>Receipt<wbr>Rule<wbr>Workmail<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of WorkMail Action blocks. Documented below.
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
            <td class="align-top">add_<wbr>header_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleaddheaderaction">list[receipt_<wbr>rule_<wbr>add_<wbr>header_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of Add Header Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">after</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule to place this rule after
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bounce_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulebounceaction">list[receipt_<wbr>rule_<wbr>bounce_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of Bounce Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If true, the rule will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulelambdaaction">list[receipt_<wbr>rule_<wbr>lambda_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of Lambda Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">recipients</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} A list of email addresses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule_<wbr>set_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrules3action">list[receipt_<wbr>rule_<wbr>s3_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of S3 Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scan_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If true, incoming emails will be scanned for spam and viruses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulesnsaction">list[receipt_<wbr>rule_<wbr>sns_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of SNS Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stop_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulestopaction">list[receipt_<wbr>rule_<wbr>stop_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of Stop Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tls_<wbr>policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Require or Optional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">workmail_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleworkmailaction">list[receipt_<wbr>rule_<wbr>workmail_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of WorkMail Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing ReceiptRule Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ReceiptRuleState, opts?: pulumi.CustomResourceOptions): ReceiptRule;
```

```python
def get(resource_name, id, opts=None, add_<wbr>header_<wbr>actions=None, after=None, bounce_<wbr>actions=None, enabled=None, lambda_<wbr>actions=None, name=None, recipients=None, rule_<wbr>set_<wbr>name=None, s3_<wbr>actions=None, scan_<wbr>enabled=None, sns_<wbr>actions=None, stop_<wbr>actions=None, tls_<wbr>policy=None, workmail_<wbr>actions=None)
```

```go
func GetReceiptRule(ctx *pulumi.Context, name string, id pulumi.IDInput, state *ReceiptRuleState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static ReceiptRule Get(string name, Input<string> id, ReceiptRuleState? state = null, CustomResourceOptions? options = null);
```

Get an existing ReceiptRule resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Add<wbr>Header<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleaddheaderaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Add<wbr>Header<wbr>Action<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Add Header Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">After</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule to place this rule after
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bounce<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulebounceaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Bounce<wbr>Action<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Bounce Action blocks. Documented below.
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
If true, the rule will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulelambdaaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Lambda<wbr>Action<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Lambda Action blocks. Documented below.
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
The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Recipients</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of email addresses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrules3action">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>S3Action<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of S3 Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scan<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, incoming emails will be scanned for spam and viruses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulesnsaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Sns<wbr>Action<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of SNS Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stop<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulestopaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Stop<wbr>Action<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Stop Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tls<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Require or Optional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Workmail<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleworkmailaction">List&lt;Pulumi.<wbr>Aws.<wbr>Ses.<wbr>Receipt<wbr>Rule<wbr>Workmail<wbr>Action<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of WorkMail Action blocks. Documented below.
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
            <td class="align-top">Add<wbr>Header<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleaddheaderaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Add<wbr>Header<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Add Header Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">After</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule to place this rule after
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bounce<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulebounceaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Bounce<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Bounce Action blocks. Documented below.
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
If true, the rule will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulelambdaaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Lambda<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Lambda Action blocks. Documented below.
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
The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Recipients</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of email addresses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrules3action">[]ses.<wbr>Receipt<wbr>Rule<wbr>S3Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of S3 Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scan<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, incoming emails will be scanned for spam and viruses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulesnsaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Sns<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of SNS Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stop<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulestopaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Stop<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Stop Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tls<wbr>Policy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Require or Optional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Workmail<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleworkmailaction">[]ses.<wbr>Receipt<wbr>Rule<wbr>Workmail<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of WorkMail Action blocks. Documented below.
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
            <td class="align-top">add<wbr>Header<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleaddheaderaction">ses.<wbr>Receipt<wbr>Rule<wbr>Add<wbr>Header<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Add Header Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">after</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule to place this rule after
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bounce<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulebounceaction">ses.<wbr>Receipt<wbr>Rule<wbr>Bounce<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Bounce Action blocks. Documented below.
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
If true, the rule will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulelambdaaction">ses.<wbr>Receipt<wbr>Rule<wbr>Lambda<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Lambda Action blocks. Documented below.
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
The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">recipients</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of email addresses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule<wbr>Set<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrules3action">ses.<wbr>Receipt<wbr>Rule<wbr>S3Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of S3 Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scan<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, incoming emails will be scanned for spam and viruses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulesnsaction">ses.<wbr>Receipt<wbr>Rule<wbr>Sns<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of SNS Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stop<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulestopaction">ses.<wbr>Receipt<wbr>Rule<wbr>Stop<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Stop Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tls<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Require or Optional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">workmail<wbr>Actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleworkmailaction">ses.<wbr>Receipt<wbr>Rule<wbr>Workmail<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of WorkMail Action blocks. Documented below.
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
            <td class="align-top">add_<wbr>header_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleaddheaderaction">list[receipt_<wbr>rule_<wbr>add_<wbr>header_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Add Header Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">after</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule to place this rule after
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bounce_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulebounceaction">list[receipt_<wbr>rule_<wbr>bounce_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Bounce Action blocks. Documented below.
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
If true, the rule will be enabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulelambdaaction">list[receipt_<wbr>rule_<wbr>lambda_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Lambda Action blocks. Documented below.
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
The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">recipients</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of email addresses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule_<wbr>set_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule set
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrules3action">list[receipt_<wbr>rule_<wbr>s3_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of S3 Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scan_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, incoming emails will be scanned for spam and viruses
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulesnsaction">list[receipt_<wbr>rule_<wbr>sns_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of SNS Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stop_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptrulestopaction">list[receipt_<wbr>rule_<wbr>stop_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Stop Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tls_<wbr>policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Require or Optional
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">workmail_<wbr>actions</td>
            <td class="align-top">
                
                <code><a href="#receiptruleworkmailaction">list[receipt_<wbr>rule_<wbr>workmail_<wbr>action]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of WorkMail Action blocks. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### ReceiptRuleAddHeaderAction
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ReceiptRuleAddHeaderAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ReceiptRuleAddHeaderAction">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#ReceiptRuleAddHeaderActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#ReceiptRuleAddHeaderActionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.ReceiptRuleAddHeaderActionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.ReceiptRuleAddHeaderAction.html">output</a> API doc for this type.
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
            <td class="align-top">Header<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the header to add
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Header<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The value of the header to add
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Position</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
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
            <td class="align-top">Header<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the header to add
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Header<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The value of the header to add
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Position</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
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
            <td class="align-top">header<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the header to add
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">header<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The value of the header to add
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">position</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
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
            <td class="align-top">header_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the header to add
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">header_<wbr>value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The value of the header to add
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">position</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ReceiptRuleBounceAction
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ReceiptRuleBounceAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ReceiptRuleBounceAction">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#ReceiptRuleBounceActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#ReceiptRuleBounceActionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.ReceiptRuleBounceActionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.ReceiptRuleBounceAction.html">output</a> API doc for this type.
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
            <td class="align-top">Message</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The message to send
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Position</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sender</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The email address of the sender
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Smtp<wbr>Reply<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The RFC 5321 SMTP reply code
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 3463 SMTP enhanced status code
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
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
            <td class="align-top">Message</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The message to send
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Position</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sender</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The email address of the sender
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Smtp<wbr>Reply<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The RFC 5321 SMTP reply code
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status<wbr>Code</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 3463 SMTP enhanced status code
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
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
            <td class="align-top">message</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The message to send
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">position</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sender</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The email address of the sender
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">smtp<wbr>Reply<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The RFC 5321 SMTP reply code
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 3463 SMTP enhanced status code
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
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
            <td class="align-top">message</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The message to send
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">position</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sender</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The email address of the sender
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">smtp_<wbr>reply_<wbr>code</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The RFC 5321 SMTP reply code
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status_<wbr>code</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The RFC 3463 SMTP enhanced status code
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topic_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ReceiptRuleLambdaAction
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ReceiptRuleLambdaAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ReceiptRuleLambdaAction">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#ReceiptRuleLambdaActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#ReceiptRuleLambdaActionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.ReceiptRuleLambdaActionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.ReceiptRuleLambdaAction.html">output</a> API doc for this type.
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
            <td class="align-top">Function<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Lambda function to invoke
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Invocation<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Event or RequestResponse
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Position</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
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
            <td class="align-top">Function<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Lambda function to invoke
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Invocation<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Event or RequestResponse
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Position</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
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
            <td class="align-top">function<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Lambda function to invoke
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">invocation<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Event or RequestResponse
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">position</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
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
            <td class="align-top">function_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Lambda function to invoke
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">invocation_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Event or RequestResponse
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">position</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topic_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ReceiptRuleS3Action
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ReceiptRuleS3Action">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ReceiptRuleS3Action">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#ReceiptRuleS3ActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#ReceiptRuleS3ActionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.ReceiptRuleS3ActionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.ReceiptRuleS3Action.html">output</a> API doc for this type.
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
            <td class="align-top">Bucket<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the KMS key
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Object<wbr>Key<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key prefix of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Position</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
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
            <td class="align-top">Bucket<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the KMS key
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Object<wbr>Key<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key prefix of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Position</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
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
            <td class="align-top">bucket<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the KMS key
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">object<wbr>Key<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key prefix of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">position</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
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
            <td class="align-top">bucket_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the KMS key
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">object_<wbr>key_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key prefix of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">position</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topic_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ReceiptRuleSnsAction
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ReceiptRuleSnsAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ReceiptRuleSnsAction">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#ReceiptRuleSnsActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#ReceiptRuleSnsActionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.ReceiptRuleSnsActionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.ReceiptRuleSnsAction.html">output</a> API doc for this type.
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
            <td class="align-top">Position</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of an SNS topic to notify
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
            <td class="align-top">Position</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of an SNS topic to notify
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
            <td class="align-top">position</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of an SNS topic to notify
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
            <td class="align-top">position</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topic_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of an SNS topic to notify
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ReceiptRuleStopAction
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ReceiptRuleStopAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ReceiptRuleStopAction">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#ReceiptRuleStopActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#ReceiptRuleStopActionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.ReceiptRuleStopActionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.ReceiptRuleStopAction.html">output</a> API doc for this type.
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
            <td class="align-top">Position</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scope</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The scope to apply
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
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
            <td class="align-top">Position</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scope</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The scope to apply
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
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
            <td class="align-top">position</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scope</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The scope to apply
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
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
            <td class="align-top">position</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scope</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The scope to apply
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topic_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ReceiptRuleWorkmailAction
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ReceiptRuleWorkmailAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ReceiptRuleWorkmailAction">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#ReceiptRuleWorkmailActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#ReceiptRuleWorkmailActionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.ReceiptRuleWorkmailActionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.ReceiptRuleWorkmailAction.html">output</a> API doc for this type.
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
            <td class="align-top">Organization<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the WorkMail organization
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Position</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
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
            <td class="align-top">Organization<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the WorkMail organization
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Position</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
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
            <td class="align-top">organization<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the WorkMail organization
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">position</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
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
            <td class="align-top">organization_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the WorkMail organization
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">position</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The position of the action in the receipt rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topic_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SNS topic to notify
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







