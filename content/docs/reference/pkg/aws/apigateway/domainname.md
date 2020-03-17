
---
title: "DomainName"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Registers a custom domain name for use with AWS API Gateway. Additional information about this functionality
can be found in the [API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html).

This resource just establishes ownership of and the TLS settings for
a particular domain name. An API can be attached to a particular path
under the registered domain name using
the `aws.apigateway.BasePathMapping` resource.

API Gateway domains can be defined as either 'edge-optimized' or 'regional'.  In an edge-optimized configuration,
API Gateway internally creates and manages a CloudFront distribution to route requests on the given hostname. In
addition to this resource it's necessary to create a DNS record corresponding to the given domain name which is an alias
(either Route53 alias or traditional CNAME) to the Cloudfront domain name exported in the `cloudfront_domain_name`
attribute.

In a regional configuration, API Gateway does not create a CloudFront distribution to route requests to the API, though
a distribution can be created if needed. In either case, it is necessary to create a DNS record corresponding to the
given domain name which is an alias (either Route53 alias or traditional CNAME) to the regional domain name exported in
the `regional_domain_name` attribute.

> **Note:** API Gateway requires the use of AWS Certificate Manager (ACM) certificates instead of Identity and Access Management (IAM) certificates in regions that support ACM. Regions that support ACM can be found in the [Regions and Endpoints Documentation](https://docs.aws.amazon.com/general/latest/gr/rande.html#acm_region). To import an existing private key and certificate into ACM or request an ACM certificate, see the [`aws.acm.Certificate` resource](https://www.terraform.io/docs/providers/aws/r/acm_certificate.html).

> **Note:** The `aws.apigateway.DomainName` resource expects dependency on the `aws.acm.CertificateValidation` as 
only verified certificates can be used. This can be made either explicitly by adding the 
`depends_on = [aws_acm_certificate_validation.cert]` attribute. Or implicitly by referring certificate ARN 
from the validation resource where it will be available after the resource creation: 
`regional_certificate_arn = aws_acm_certificate_validation.cert.certificate_arn`.

> **Note:** All arguments including the private key will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

## Example Usage

### Edge Optimized (ACM Certificate)

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleDomainName = new aws.apigateway.DomainName("example", {
    certificateArn: aws_acm_certificate_validation_example.certificateArn,
    domainName: "api.example.com",
});
// Example DNS record using Route53.
// Route53 is not specifically required; any DNS host can be used.
const exampleRecord = new aws.route53.Record("example", {
    aliases: [{
        evaluateTargetHealth: true,
        name: exampleDomainName.cloudfrontDomainName,
        zoneId: exampleDomainName.cloudfrontZoneId,
    }],
    name: exampleDomainName.domainName,
    type: "A",
    zoneId: aws_route53_zone_example.id,
});
```

### Edge Optimized (IAM Certificate)

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as fs from "fs";

const exampleDomainName = new aws.apigateway.DomainName("example", {
    certificateBody: fs.readFileSync(`./example.com/example.crt`, "utf-8"),
    certificateChain: fs.readFileSync(`./example.com/ca.crt`, "utf-8"),
    certificateName: "example-api",
    certificatePrivateKey: fs.readFileSync(`./example.com/example.key`, "utf-8"),
    domainName: "api.example.com",
});
// Example DNS record using Route53.
// Route53 is not specifically required; any DNS host can be used.
const exampleRecord = new aws.route53.Record("example", {
    aliases: [{
        evaluateTargetHealth: true,
        name: exampleDomainName.cloudfrontDomainName,
        zoneId: exampleDomainName.cloudfrontZoneId,
    }],
    name: exampleDomainName.domainName,
    type: "A",
    zoneId: aws_route53_zone_example.id, // See aws.route53.Zone for how to create this
});
```

### Regional (ACM Certificate)

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleDomainName = new aws.apigateway.DomainName("example", {
    domainName: "api.example.com",
    endpointConfiguration: {
        types: "REGIONAL",
    },
    regionalCertificateArn: aws_acm_certificate_validation_example.certificateArn,
});
// Example DNS record using Route53.
// Route53 is not specifically required; any DNS host can be used.
const exampleRecord = new aws.route53.Record("example", {
    aliases: [{
        evaluateTargetHealth: true,
        name: exampleDomainName.regionalDomainName,
        zoneId: exampleDomainName.regionalZoneId,
    }],
    name: exampleDomainName.domainName,
    type: "A",
    zoneId: aws_route53_zone_example.id,
});
```

### Regional (IAM Certificate)

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as fs from "fs";

const exampleDomainName = new aws.apigateway.DomainName("example", {
    certificateBody: fs.readFileSync(`./example.com/example.crt`, "utf-8"),
    certificateChain: fs.readFileSync(`./example.com/ca.crt`, "utf-8"),
    certificatePrivateKey: fs.readFileSync(`./example.com/example.key`, "utf-8"),
    domainName: "api.example.com",
    endpointConfiguration: {
        types: "REGIONAL",
    },
    regionalCertificateName: "example-api",
});
// Example DNS record using Route53.
// Route53 is not specifically required; any DNS host can be used.
const exampleRecord = new aws.route53.Record("example", {
    aliases: [{
        evaluateTargetHealth: true,
        name: exampleDomainName.regionalDomainName,
        zoneId: exampleDomainName.regionalZoneId,
    }],
    name: exampleDomainName.domainName,
    type: "A",
    zoneId: aws_route53_zone_example.id,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_domain_name.html.markdown.



## Create a DomainName Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#DomainName">DomainName</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#DomainNameArgs">DomainNameArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">DomainName</span><span class="p">(resource_name, opts=None, </span>certificate_arn=None<span class="p">, </span>certificate_body=None<span class="p">, </span>certificate_chain=None<span class="p">, </span>certificate_name=None<span class="p">, </span>certificate_private_key=None<span class="p">, </span>domain_name=None<span class="p">, </span>endpoint_configuration=None<span class="p">, </span>regional_certificate_arn=None<span class="p">, </span>regional_certificate_name=None<span class="p">, </span>security_policy=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDomainName<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#DomainNameArgs">DomainNameArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#DomainName">DomainName</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.DomainName.html">DomainName</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.DomainNameArgs.html">DomainNameArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a DomainName resource with the given unique name, arguments, and options.

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
            <td class="align-top">Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Body</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The certificate issued for the domain name
being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Chain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
`regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`. Required if `certificate_arn` is not set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Private<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The private key associated with the
domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The fully-qualified domain name to register
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#domainnameendpointconfiguration">Pulumi.<wbr>Aws.<wbr>Apigateway.<wbr>Domain<wbr>Name<wbr>Endpoint<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block defining API endpoint information including type. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and `certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Transport Layer Security (TLS) version &#43; cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2`. Must be configured to perform drift detection.
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
Key-value mapping of resource tags
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
            <td class="align-top">Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Body</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The certificate issued for the domain name
being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Chain</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
`regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`. Required if `certificate_arn` is not set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Private<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The private key associated with the
domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The fully-qualified domain name to register
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#domainnameendpointconfiguration">*apigateway.<wbr>Domain<wbr>Name<wbr>Endpoint<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block defining API endpoint information including type. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and `certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Policy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Transport Layer Security (TLS) version &#43; cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2`. Must be configured to perform drift detection.
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
Key-value mapping of resource tags
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
            <td class="align-top">certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate<wbr>Body</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The certificate issued for the domain name
being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate<wbr>Chain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
`regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`. Required if `certificate_arn` is not set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate<wbr>Private<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The private key associated with the
domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The fully-qualified domain name to register
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#domainnameendpointconfiguration">apigateway.<wbr>Domain<wbr>Name<wbr>Endpoint<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block defining API endpoint information including type. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional<wbr>Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and `certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional<wbr>Certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Transport Layer Security (TLS) version &#43; cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2`. Must be configured to perform drift detection.
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
Key-value mapping of resource tags
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
            <td class="align-top">certificate_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate_<wbr>body</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The certificate issued for the domain name
being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate_<wbr>chain</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
`regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`. Required if `certificate_arn` is not set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate_<wbr>private_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The private key associated with the
domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The fully-qualified domain name to register
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#domainnameendpointconfiguration">Dict[domain_<wbr>name_<wbr>endpoint_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block defining API endpoint information including type. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional_<wbr>certificate_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and `certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional_<wbr>certificate_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Transport Layer Security (TLS) version &#43; cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2`. Must be configured to perform drift detection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## DomainName Output Properties

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
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Body</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The certificate issued for the domain name
being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Chain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
`regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`. Required if `certificate_arn` is not set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Private<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The private key associated with the
domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Upload<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The upload date associated with the domain certificate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudfront<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The hostname created by Cloudfront to represent
the distribution that implements this domain name mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudfront<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} For convenience, the hosted zone ID (`Z2FDTNDATAQYW2`)
that can be used to create a Route53 alias record for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The fully-qualified domain name to register
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#domainnameendpointconfiguration">Pulumi.<wbr>Aws.<wbr>Apigateway.<wbr>Domain<wbr>Name<wbr>Endpoint<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block defining API endpoint information including type. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and `certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The hostname for the custom domain&#39;s regional endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Policy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Transport Layer Security (TLS) version &#43; cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2`. Must be configured to perform drift detection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
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
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Body</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The certificate issued for the domain name
being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Chain</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
`regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`. Required if `certificate_arn` is not set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Private<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The private key associated with the
domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Upload<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The upload date associated with the domain certificate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudfront<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The hostname created by Cloudfront to represent
the distribution that implements this domain name mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudfront<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} For convenience, the hosted zone ID (`Z2FDTNDATAQYW2`)
that can be used to create a Route53 alias record for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The fully-qualified domain name to register
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#domainnameendpointconfiguration">apigateway.<wbr>Domain<wbr>Name<wbr>Endpoint<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block defining API endpoint information including type. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and `certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The hostname for the custom domain&#39;s regional endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Policy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Transport Layer Security (TLS) version &#43; cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2`. Must be configured to perform drift detection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
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
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate<wbr>Body</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The certificate issued for the domain name
being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate<wbr>Chain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
`regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`. Required if `certificate_arn` is not set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate<wbr>Private<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The private key associated with the
domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate<wbr>Upload<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The upload date associated with the domain certificate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudfront<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The hostname created by Cloudfront to represent
the distribution that implements this domain name mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudfront<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} For convenience, the hosted zone ID (`Z2FDTNDATAQYW2`)
that can be used to create a Route53 alias record for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The fully-qualified domain name to register
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#domainnameendpointconfiguration">apigateway.<wbr>Domain<wbr>Name<wbr>Endpoint<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block defining API endpoint information including type. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional<wbr>Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and `certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional<wbr>Certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The hostname for the custom domain&#39;s regional endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Policy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Transport Layer Security (TLS) version &#43; cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2`. Must be configured to perform drift detection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
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
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate_<wbr>body</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The certificate issued for the domain name
being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate_<wbr>chain</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
`regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`. Required if `certificate_arn` is not set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate_<wbr>private_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The private key associated with the
domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate_<wbr>upload_<wbr>date</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The upload date associated with the domain certificate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudfront_<wbr>domain_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The hostname created by Cloudfront to represent
the distribution that implements this domain name mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudfront_<wbr>zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} For convenience, the hosted zone ID (`Z2FDTNDATAQYW2`)
that can be used to create a Route53 alias record for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The fully-qualified domain name to register
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#domainnameendpointconfiguration">Dict[domain_<wbr>name_<wbr>endpoint_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block defining API endpoint information including type. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional_<wbr>certificate_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and `certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional_<wbr>certificate_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional_<wbr>domain_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The hostname for the custom domain&#39;s regional endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional_<wbr>zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Transport Layer Security (TLS) version &#43; cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2`. Must be configured to perform drift detection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing DomainName Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#DomainNameState">DomainNameState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#DomainName">DomainName</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>certificate_arn=None<span class="p">, </span>certificate_body=None<span class="p">, </span>certificate_chain=None<span class="p">, </span>certificate_name=None<span class="p">, </span>certificate_private_key=None<span class="p">, </span>certificate_upload_date=None<span class="p">, </span>cloudfront_domain_name=None<span class="p">, </span>cloudfront_zone_id=None<span class="p">, </span>domain_name=None<span class="p">, </span>endpoint_configuration=None<span class="p">, </span>regional_certificate_arn=None<span class="p">, </span>regional_certificate_name=None<span class="p">, </span>regional_domain_name=None<span class="p">, </span>regional_zone_id=None<span class="p">, </span>security_policy=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetDomainName<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#DomainNameState">DomainNameState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#DomainName">DomainName</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.DomainName.html">DomainName</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.DomainNameState.html">DomainNameState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing DomainName resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
Amazon Resource Name (ARN)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Body</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The certificate issued for the domain name
being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Chain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
`regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`. Required if `certificate_arn` is not set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Private<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The private key associated with the
domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Upload<wbr>Date</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The upload date associated with the domain certificate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudfront<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hostname created by Cloudfront to represent
the distribution that implements this domain name mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudfront<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
For convenience, the hosted zone ID (`Z2FDTNDATAQYW2`)
that can be used to create a Route53 alias record for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The fully-qualified domain name to register
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#domainnameendpointconfiguration">Pulumi.<wbr>Aws.<wbr>Apigateway.<wbr>Domain<wbr>Name<wbr>Endpoint<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block defining API endpoint information including type. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and `certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hostname for the custom domain&#39;s regional endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Transport Layer Security (TLS) version &#43; cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2`. Must be configured to perform drift detection.
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
Key-value mapping of resource tags
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
Amazon Resource Name (ARN)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Body</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The certificate issued for the domain name
being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Chain</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
`regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`. Required if `certificate_arn` is not set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Private<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The private key associated with the
domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Certificate<wbr>Upload<wbr>Date</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The upload date associated with the domain certificate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudfront<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hostname created by Cloudfront to represent
the distribution that implements this domain name mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudfront<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
For convenience, the hosted zone ID (`Z2FDTNDATAQYW2`)
that can be used to create a Route53 alias record for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The fully-qualified domain name to register
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#domainnameendpointconfiguration">*apigateway.<wbr>Domain<wbr>Name<wbr>Endpoint<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block defining API endpoint information including type. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and `certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hostname for the custom domain&#39;s regional endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regional<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Policy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Transport Layer Security (TLS) version &#43; cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2`. Must be configured to perform drift detection.
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
Key-value mapping of resource tags
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
Amazon Resource Name (ARN)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate<wbr>Body</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The certificate issued for the domain name
being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate<wbr>Chain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
`regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`. Required if `certificate_arn` is not set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate<wbr>Private<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The private key associated with the
domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate<wbr>Upload<wbr>Date</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The upload date associated with the domain certificate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudfront<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hostname created by Cloudfront to represent
the distribution that implements this domain name mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudfront<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
For convenience, the hosted zone ID (`Z2FDTNDATAQYW2`)
that can be used to create a Route53 alias record for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The fully-qualified domain name to register
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#domainnameendpointconfiguration">apigateway.<wbr>Domain<wbr>Name<wbr>Endpoint<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block defining API endpoint information including type. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional<wbr>Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and `certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional<wbr>Certificate<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional<wbr>Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hostname for the custom domain&#39;s regional endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Transport Layer Security (TLS) version &#43; cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2`. Must be configured to perform drift detection.
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
Key-value mapping of resource tags
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
Amazon Resource Name (ARN)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with `certificate_name`, `certificate_body`, `certificate_chain`, `certificate_private_key`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate_<wbr>body</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The certificate issued for the domain name
being registered, in PEM format. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate_<wbr>chain</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`,
`regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with `certificate_arn`, `regional_certificate_arn`, and
`regional_certificate_name`. Required if `certificate_arn` is not set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate_<wbr>private_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The private key associated with the
domain certificate given in `certificate_body`. Only valid for `EDGE` endpoint configuration type. Conflicts with `certificate_arn`, `regional_certificate_arn`, and `regional_certificate_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">certificate_<wbr>upload_<wbr>date</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The upload date associated with the domain certificate.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudfront_<wbr>domain_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hostname created by Cloudfront to represent
the distribution that implements this domain name mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudfront_<wbr>zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
For convenience, the hosted zone ID (`Z2FDTNDATAQYW2`)
that can be used to create a Route53 alias record for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The fully-qualified domain name to register
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#domainnameendpointconfiguration">Dict[domain_<wbr>name_<wbr>endpoint_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block defining API endpoint information including type. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional_<wbr>certificate_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and `certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional_<wbr>certificate_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with `certificate_arn`, `certificate_name`, `certificate_body`, `certificate_chain`, and
`certificate_private_key`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional_<wbr>domain_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hostname for the custom domain&#39;s regional endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regional_<wbr>zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Transport Layer Security (TLS) version &#43; cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2`. Must be configured to perform drift detection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### DomainNameEndpointConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DomainNameEndpointConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DomainNameEndpointConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#DomainNameEndpointConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#DomainNameEndpointConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.DomainNameEndpointConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.DomainNameEndpointConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">Types</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of endpoint types. This resource currently only supports managing a single value. Valid values: `EDGE` or `REGIONAL`. If unspecified, defaults to `EDGE`. Must be declared as `REGIONAL` in non-Commercial partitions. Refer to the [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html) for more information on the difference between edge-optimized and regional APIs.
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
            <td class="align-top">Types</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of endpoint types. This resource currently only supports managing a single value. Valid values: `EDGE` or `REGIONAL`. If unspecified, defaults to `EDGE`. Must be declared as `REGIONAL` in non-Commercial partitions. Refer to the [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html) for more information on the difference between edge-optimized and regional APIs.
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
            <td class="align-top">types</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of endpoint types. This resource currently only supports managing a single value. Valid values: `EDGE` or `REGIONAL`. If unspecified, defaults to `EDGE`. Must be declared as `REGIONAL` in non-Commercial partitions. Refer to the [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html) for more information on the difference between edge-optimized and regional APIs.
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
            <td class="align-top">types</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of endpoint types. This resource currently only supports managing a single value. Valid values: `EDGE` or `REGIONAL`. If unspecified, defaults to `EDGE`. Must be declared as `REGIONAL` in non-Commercial partitions. Refer to the [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html) for more information on the difference between edge-optimized and regional APIs.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







