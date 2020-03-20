
---
title: "GetPolicyDocument"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>






## Using GetPolicyDocument

{{< langchoose csharp nojavascript >}}


<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getPolicyDocument<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/iam/#GetPolicyDocumentArgs">GetPolicyDocumentArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#InvokeOptions">pulumi.InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/iam/#GetPolicyDocumentResult">GetPolicyDocumentResult</a></span>></span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_policy_document(</span>override_json=None<span class="p">, </span>policy_id=None<span class="p">, </span>source_json=None<span class="p">, </span>statements=None<span class="p">, </span>version=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupPolicyDocument<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#LookupPolicyDocumentArgs">LookupPolicyDocumentArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#LookupPolicyDocumentResult">LookupPolicyDocumentResult</a></span>, error)</span></code></pre></div>


<div class="highlight">
<pre class="chroma">
<code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetPolicyDocument </span><span class="p">{</span>
    <span class="k">public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iam.GetPolicyDocumentResult.html">Pulumi.Aws.Iam.GetPolicyDocumentResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iam.GetPolicyDocumentArgs.html">GetPolicyDocumentArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span>
<span class="p">}</span></code></pre>
</div>



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
            <td class="align-top">Override<wbr>Json</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An IAM policy document to import and override the
current policy document.  Statements with non-blank `sid`s in the override
document will overwrite statements with the same `sid` in the current document.
Statements without an `sid` cannot be overwritten.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An ID for the policy document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Json</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An IAM policy document to import as a base for the
current policy document.  Statements with non-blank `sid`s in the current
policy document will overwrite statements with the same `sid` in the source
json.  Statements without an `sid` cannot be overwritten.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Statements</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatement">List&lt;Pulumi.<wbr>Aws.<wbr>Iam.<wbr>Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A nested configuration block (described below)
configuring one *statement* to be included in the policy document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
IAM policy document version. Valid values: `2008-10-17`, `2012-10-17`. Defaults to `2012-10-17`. For more information, see the [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html).
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
            <td class="align-top">Override<wbr>Json</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An IAM policy document to import and override the
current policy document.  Statements with non-blank `sid`s in the override
document will overwrite statements with the same `sid` in the current document.
Statements without an `sid` cannot be overwritten.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An ID for the policy document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Json</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An IAM policy document to import as a base for the
current policy document.  Statements with non-blank `sid`s in the current
policy document will overwrite statements with the same `sid` in the source
json.  Statements without an `sid` cannot be overwritten.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Statements</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatement">[]Get<wbr>Policy<wbr>Document<wbr>Statement</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A nested configuration block (described below)
configuring one *statement* to be included in the policy document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
IAM policy document version. Valid values: `2008-10-17`, `2012-10-17`. Defaults to `2012-10-17`. For more information, see the [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html).
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
            <td class="align-top">override<wbr>Json</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An IAM policy document to import and override the
current policy document.  Statements with non-blank `sid`s in the override
document will overwrite statements with the same `sid` in the current document.
Statements without an `sid` cannot be overwritten.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An ID for the policy document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Json</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An IAM policy document to import as a base for the
current policy document.  Statements with non-blank `sid`s in the current
policy document will overwrite statements with the same `sid` in the source
json.  Statements without an `sid` cannot be overwritten.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">statements</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatement">iam.<wbr>Get<wbr>Policy<wbr>Document<wbr>Statement[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A nested configuration block (described below)
configuring one *statement* to be included in the policy document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
IAM policy document version. Valid values: `2008-10-17`, `2012-10-17`. Defaults to `2012-10-17`. For more information, see the [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html).
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
            <td class="align-top">override_<wbr>json</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An IAM policy document to import and override the
current policy document.  Statements with non-blank `sid`s in the override
document will overwrite statements with the same `sid` in the current document.
Statements without an `sid` cannot be overwritten.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An ID for the policy document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>json</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An IAM policy document to import as a base for the
current policy document.  Statements with non-blank `sid`s in the current
policy document will overwrite statements with the same `sid` in the source
json.  Statements without an `sid` cannot be overwritten.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">statements</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatement">List[Get<wbr>Policy<wbr>Document<wbr>Statement]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A nested configuration block (described below)
configuring one *statement* to be included in the policy document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
IAM policy document version. Valid values: `2008-10-17`, `2012-10-17`. Defaults to `2012-10-17`. For more information, see the [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## GetPolicyDocument Result

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
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Json</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The above arguments serialized as a standard JSON policy document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Override<wbr>Json</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Json</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Statements</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatement">List&lt;Pulumi.<wbr>Aws.<wbr>Iam.<wbr>Get<wbr>Policy<wbr>Document<wbr>Statement&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Json</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The above arguments serialized as a standard JSON policy document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Override<wbr>Json</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Json</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Statements</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatement">[]Get<wbr>Policy<wbr>Document<wbr>Statement</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">json</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The above arguments serialized as a standard JSON policy document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">override<wbr>Json</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Json</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">statements</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatement">iam.<wbr>Get<wbr>Policy<wbr>Document<wbr>Statement[]?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">json</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The above arguments serialized as a standard JSON policy document.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">override_<wbr>json</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>json</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">statements</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatement">List[Get<wbr>Policy<wbr>Document<wbr>Statement]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Supporting Types

#### GetPolicyDocumentStatement
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetPolicyDocumentStatement">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetPolicyDocumentStatement">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#GetPolicyDocumentStatementArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#GetPolicyDocumentStatement">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iam.GetPolicyDocumentStatementArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iam.GetPolicyDocumentStatement.html">output</a> API doc for this type.
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
            <td class="align-top">Actions</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of actions that this statement either allows
or denies. For example, ``[&#34;ec2:RunInstances&#34;, &#34;s3:*&#34;]``.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Conditions</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatementcondition">List&lt;Pulumi.<wbr>Aws.<wbr>Iam.<wbr>Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Condition<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A nested configuration block (described below)
that defines a further, possibly-service-specific condition that constrains
whether this statement applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Effect</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Either &#34;Allow&#34; or &#34;Deny&#34;, to specify whether this
statement allows or denies the given actions. The default is &#34;Allow&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Not<wbr>Actions</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of actions that this statement does *not*
apply to. Used to apply a policy statement to all actions *except* those
listed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Not<wbr>Principals</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatementnotprincipal">List&lt;Pulumi.<wbr>Aws.<wbr>Iam.<wbr>Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Not<wbr>Principal<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Like `principals` except gives resources that
the statement does *not* apply to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Not<wbr>Resources</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of resource ARNs that this statement
does *not* apply to. Used to apply a policy statement to all resources
*except* those listed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Principals</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatementprincipal">List&lt;Pulumi.<wbr>Aws.<wbr>Iam.<wbr>Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Principal<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A nested configuration block (described below)
specifying a resource (or resource pattern) to which this statement applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resources</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of resource ARNs that this statement applies
to. This is required by AWS if used for an IAM policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sid</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An ID for the policy statement.
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
            <td class="align-top">Actions</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of actions that this statement either allows
or denies. For example, ``[&#34;ec2:RunInstances&#34;, &#34;s3:*&#34;]``.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Conditions</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatementcondition">[]Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Condition</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A nested configuration block (described below)
that defines a further, possibly-service-specific condition that constrains
whether this statement applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Effect</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Either &#34;Allow&#34; or &#34;Deny&#34;, to specify whether this
statement allows or denies the given actions. The default is &#34;Allow&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Not<wbr>Actions</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of actions that this statement does *not*
apply to. Used to apply a policy statement to all actions *except* those
listed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Not<wbr>Principals</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatementnotprincipal">[]Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Not<wbr>Principal</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Like `principals` except gives resources that
the statement does *not* apply to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Not<wbr>Resources</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of resource ARNs that this statement
does *not* apply to. Used to apply a policy statement to all resources
*except* those listed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Principals</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatementprincipal">[]Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Principal</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A nested configuration block (described below)
specifying a resource (or resource pattern) to which this statement applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resources</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of resource ARNs that this statement applies
to. This is required by AWS if used for an IAM policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sid</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An ID for the policy statement.
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
            <td class="align-top">actions</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of actions that this statement either allows
or denies. For example, ``[&#34;ec2:RunInstances&#34;, &#34;s3:*&#34;]``.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">conditions</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatementcondition">iam.<wbr>Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Condition[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A nested configuration block (described below)
that defines a further, possibly-service-specific condition that constrains
whether this statement applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">effect</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Either &#34;Allow&#34; or &#34;Deny&#34;, to specify whether this
statement allows or denies the given actions. The default is &#34;Allow&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">not<wbr>Actions</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of actions that this statement does *not*
apply to. Used to apply a policy statement to all actions *except* those
listed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">not<wbr>Principals</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatementnotprincipal">iam.<wbr>Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Not<wbr>Principal[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Like `principals` except gives resources that
the statement does *not* apply to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">not<wbr>Resources</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of resource ARNs that this statement
does *not* apply to. Used to apply a policy statement to all resources
*except* those listed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">principals</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatementprincipal">iam.<wbr>Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Principal[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A nested configuration block (described below)
specifying a resource (or resource pattern) to which this statement applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resources</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of resource ARNs that this statement applies
to. This is required by AWS if used for an IAM policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sid</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An ID for the policy statement.
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
            <td class="align-top">actions</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of actions that this statement either allows
or denies. For example, ``[&#34;ec2:RunInstances&#34;, &#34;s3:*&#34;]``.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">conditions</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatementcondition">List[Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Condition]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A nested configuration block (described below)
that defines a further, possibly-service-specific condition that constrains
whether this statement applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">effect</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Either &#34;Allow&#34; or &#34;Deny&#34;, to specify whether this
statement allows or denies the given actions. The default is &#34;Allow&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">not<wbr>Actions</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of actions that this statement does *not*
apply to. Used to apply a policy statement to all actions *except* those
listed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">not<wbr>Principals</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatementnotprincipal">List[Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Not<wbr>Principal]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Like `principals` except gives resources that
the statement does *not* apply to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">not<wbr>Resources</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of resource ARNs that this statement
does *not* apply to. Used to apply a policy statement to all resources
*except* those listed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">principals</td>
            <td class="align-top">
                
                <code><a href="#getpolicydocumentstatementprincipal">List[Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Principal]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A nested configuration block (described below)
specifying a resource (or resource pattern) to which this statement applies.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resources</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of resource ARNs that this statement applies
to. This is required by AWS if used for an IAM policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sid</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An ID for the policy statement.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GetPolicyDocumentStatementCondition
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetPolicyDocumentStatementCondition">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetPolicyDocumentStatementCondition">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#GetPolicyDocumentStatementConditionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#GetPolicyDocumentStatementCondition">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iam.GetPolicyDocumentStatementConditionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iam.GetPolicyDocumentStatementCondition.html">output</a> API doc for this type.
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
            <td class="align-top">Test</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the
[IAM condition operator](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html)
to evaluate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The values to evaluate the condition against. If multiple
values are provided, the condition matches if at least one of them applies.
(That is, the tests are combined with the &#34;OR&#34; boolean operation.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Variable</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of a
[Context Variable](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys)
to apply the condition to. Context variables may either be standard AWS
variables starting with `aws:`, or service-specific variables prefixed with
the service name.
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
            <td class="align-top">Test</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the
[IAM condition operator](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html)
to evaluate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The values to evaluate the condition against. If multiple
values are provided, the condition matches if at least one of them applies.
(That is, the tests are combined with the &#34;OR&#34; boolean operation.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Variable</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of a
[Context Variable](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys)
to apply the condition to. Context variables may either be standard AWS
variables starting with `aws:`, or service-specific variables prefixed with
the service name.
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
            <td class="align-top">test</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the
[IAM condition operator](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html)
to evaluate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The values to evaluate the condition against. If multiple
values are provided, the condition matches if at least one of them applies.
(That is, the tests are combined with the &#34;OR&#34; boolean operation.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">variable</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of a
[Context Variable](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys)
to apply the condition to. Context variables may either be standard AWS
variables starting with `aws:`, or service-specific variables prefixed with
the service name.
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
            <td class="align-top">test</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the
[IAM condition operator](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html)
to evaluate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The values to evaluate the condition against. If multiple
values are provided, the condition matches if at least one of them applies.
(That is, the tests are combined with the &#34;OR&#34; boolean operation.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">variable</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of a
[Context Variable](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys)
to apply the condition to. Context variables may either be standard AWS
variables starting with `aws:`, or service-specific variables prefixed with
the service name.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GetPolicyDocumentStatementNotPrincipal
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetPolicyDocumentStatementNotPrincipal">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetPolicyDocumentStatementNotPrincipal">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#GetPolicyDocumentStatementNotPrincipalArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#GetPolicyDocumentStatementNotPrincipal">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iam.GetPolicyDocumentStatementNotPrincipalArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iam.GetPolicyDocumentStatementNotPrincipal.html">output</a> API doc for this type.
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
            <td class="align-top">Identifiers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of identifiers for principals. When `type`
is &#34;AWS&#34;, these are IAM user or role ARNs.  When `type` is &#34;Service&#34;, these are AWS Service roles e.g. `lambda.amazonaws.com`.
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
The type of principal. For AWS ARNs this is &#34;AWS&#34;.  For AWS services (e.g. Lambda), this is &#34;Service&#34;.
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
            <td class="align-top">Identifiers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of identifiers for principals. When `type`
is &#34;AWS&#34;, these are IAM user or role ARNs.  When `type` is &#34;Service&#34;, these are AWS Service roles e.g. `lambda.amazonaws.com`.
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
The type of principal. For AWS ARNs this is &#34;AWS&#34;.  For AWS services (e.g. Lambda), this is &#34;Service&#34;.
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
            <td class="align-top">identifiers</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of identifiers for principals. When `type`
is &#34;AWS&#34;, these are IAM user or role ARNs.  When `type` is &#34;Service&#34;, these are AWS Service roles e.g. `lambda.amazonaws.com`.
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
The type of principal. For AWS ARNs this is &#34;AWS&#34;.  For AWS services (e.g. Lambda), this is &#34;Service&#34;.
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
            <td class="align-top">identifiers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of identifiers for principals. When `type`
is &#34;AWS&#34;, these are IAM user or role ARNs.  When `type` is &#34;Service&#34;, these are AWS Service roles e.g. `lambda.amazonaws.com`.
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
The type of principal. For AWS ARNs this is &#34;AWS&#34;.  For AWS services (e.g. Lambda), this is &#34;Service&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GetPolicyDocumentStatementPrincipal
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetPolicyDocumentStatementPrincipal">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetPolicyDocumentStatementPrincipal">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#GetPolicyDocumentStatementPrincipalArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#GetPolicyDocumentStatementPrincipal">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iam.GetPolicyDocumentStatementPrincipalArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iam.GetPolicyDocumentStatementPrincipal.html">output</a> API doc for this type.
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
            <td class="align-top">Identifiers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of identifiers for principals. When `type`
is &#34;AWS&#34;, these are IAM user or role ARNs.  When `type` is &#34;Service&#34;, these are AWS Service roles e.g. `lambda.amazonaws.com`.
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
The type of principal. For AWS ARNs this is &#34;AWS&#34;.  For AWS services (e.g. Lambda), this is &#34;Service&#34;.
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
            <td class="align-top">Identifiers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of identifiers for principals. When `type`
is &#34;AWS&#34;, these are IAM user or role ARNs.  When `type` is &#34;Service&#34;, these are AWS Service roles e.g. `lambda.amazonaws.com`.
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
The type of principal. For AWS ARNs this is &#34;AWS&#34;.  For AWS services (e.g. Lambda), this is &#34;Service&#34;.
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
            <td class="align-top">identifiers</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of identifiers for principals. When `type`
is &#34;AWS&#34;, these are IAM user or role ARNs.  When `type` is &#34;Service&#34;, these are AWS Service roles e.g. `lambda.amazonaws.com`.
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
The type of principal. For AWS ARNs this is &#34;AWS&#34;.  For AWS services (e.g. Lambda), this is &#34;Service&#34;.
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
            <td class="align-top">identifiers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of identifiers for principals. When `type`
is &#34;AWS&#34;, these are IAM user or role ARNs.  When `type` is &#34;Service&#34;, these are AWS Service roles e.g. `lambda.amazonaws.com`.
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
The type of principal. For AWS ARNs this is &#34;AWS&#34;.  For AWS services (e.g. Lambda), this is &#34;Service&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







