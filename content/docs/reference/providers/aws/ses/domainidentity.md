
---
title: "DomainIdentity"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides an SES domain identity resource

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.ses.DomainIdentity("example", {
    domain: "example.com",
});
const exampleAmazonsesVerificationRecord = new aws.route53.Record("example_amazonses_verification_record", {
    name: "_amazonses.example.com",
    records: [example.verificationToken],
    ttl: 600,
    type: "TXT",
    zoneId: "ABCDEFGHIJ123",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_domain_identity.html.markdown.



## Create a DomainIdentity Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ses/#DomainIdentity">DomainIdentity</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ses/#DomainIdentityArgs">DomainIdentityArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">DomainIdentity</span><span class="p">(resource_name, id, opts=None, </span>domain=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDomainIdentity<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#DomainIdentityArgs">DomainIdentityArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ses?tab=doc#DomainIdentity">DomainIdentity</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.DomainIdentity.html">DomainIdentity</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ses.DomainIdentityArgs.html">DomainIdentityArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a DomainIdentity resource with the given unique name, arguments, and options.

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
            <td class="align-top">Domain</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The domain name to assign to SES
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
            <td class="align-top">Domain</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The domain name to assign to SES
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
            <td class="align-top">domain</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The domain name to assign to SES
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
            <td class="align-top">domain</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The domain name to assign to SES
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## DomainIdentity Output Properties

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
            <td class="align-top">{{% md %}} The ARN of the domain identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The domain name to assign to SES
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Verification<wbr>Token</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A code which when added to the domain as a TXT record
will signal to SES that the owner of the domain has authorised SES to act on
their behalf. The domain identity will be in state &#34;verification pending&#34;
until this is done. See below for an example of how this might be achieved
when the domain is hosted in Route 53 and managed by this provider.  Find out
more about verifying domains in Amazon SES in the [AWS SES
docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html).
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
            <td class="align-top">{{% md %}} The ARN of the domain identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The domain name to assign to SES
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Verification<wbr>Token</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A code which when added to the domain as a TXT record
will signal to SES that the owner of the domain has authorised SES to act on
their behalf. The domain identity will be in state &#34;verification pending&#34;
until this is done. See below for an example of how this might be achieved
when the domain is hosted in Route 53 and managed by this provider.  Find out
more about verifying domains in Amazon SES in the [AWS SES
docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html).
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
            <td class="align-top">{{% md %}} The ARN of the domain identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The domain name to assign to SES
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">verification<wbr>Token</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A code which when added to the domain as a TXT record
will signal to SES that the owner of the domain has authorised SES to act on
their behalf. The domain identity will be in state &#34;verification pending&#34;
until this is done. See below for an example of how this might be achieved
when the domain is hosted in Route 53 and managed by this provider.  Find out
more about verifying domains in Amazon SES in the [AWS SES
docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html).
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
            <td class="align-top">{{% md %}} The ARN of the domain identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The domain name to assign to SES
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">verification_<wbr>token</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A code which when added to the domain as a TXT record
will signal to SES that the owner of the domain has authorised SES to act on
their behalf. The domain identity will be in state &#34;verification pending&#34;
until this is done. See below for an example of how this might be achieved
when the domain is hosted in Route 53 and managed by this provider.  Find out
more about verifying domains in Amazon SES in the [AWS SES
docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing DomainIdentity Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DomainIdentityState, opts?: pulumi.CustomResourceOptions): DomainIdentity;
```

```python
def get(resource_name, id, opts=None, arn=None, domain=None, verification_<wbr>token=None)
```

```go
func GetDomainIdentity(ctx *pulumi.Context, name string, id pulumi.IDInput, state *DomainIdentityState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static DomainIdentity Get(string name, Input<string> id, DomainIdentityState? state = null, CustomResourceOptions? options = null);
```

Get an existing DomainIdentity resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The ARN of the domain identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The domain name to assign to SES
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Verification<wbr>Token</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A code which when added to the domain as a TXT record
will signal to SES that the owner of the domain has authorised SES to act on
their behalf. The domain identity will be in state &#34;verification pending&#34;
until this is done. See below for an example of how this might be achieved
when the domain is hosted in Route 53 and managed by this provider.  Find out
more about verifying domains in Amazon SES in the [AWS SES
docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html).
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
The ARN of the domain identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The domain name to assign to SES
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Verification<wbr>Token</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A code which when added to the domain as a TXT record
will signal to SES that the owner of the domain has authorised SES to act on
their behalf. The domain identity will be in state &#34;verification pending&#34;
until this is done. See below for an example of how this might be achieved
when the domain is hosted in Route 53 and managed by this provider.  Find out
more about verifying domains in Amazon SES in the [AWS SES
docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html).
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
The ARN of the domain identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The domain name to assign to SES
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">verification<wbr>Token</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A code which when added to the domain as a TXT record
will signal to SES that the owner of the domain has authorised SES to act on
their behalf. The domain identity will be in state &#34;verification pending&#34;
until this is done. See below for an example of how this might be achieved
when the domain is hosted in Route 53 and managed by this provider.  Find out
more about verifying domains in Amazon SES in the [AWS SES
docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html).
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
The ARN of the domain identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The domain name to assign to SES
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">verification_<wbr>token</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A code which when added to the domain as a TXT record
will signal to SES that the owner of the domain has authorised SES to act on
their behalf. The domain identity will be in state &#34;verification pending&#34;
until this is done. See below for an example of how this might be achieved
when the domain is hosted in Route 53 and managed by this provider.  Find out
more about verifying domains in Amazon SES in the [AWS SES
docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}









