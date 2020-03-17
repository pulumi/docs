
---
title: "Distribution"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Creates an Amazon CloudFront web distribution.

For information about CloudFront distributions, see the
[Amazon CloudFront Developer Guide][1]. For specific information about creating
CloudFront web distributions, see the [POST Distribution][2] page in the Amazon
CloudFront API Reference.

> **NOTE:** CloudFront distributions take about 15 minutes to a deployed state
after creation or modification. During this time, deletes to resources will be
blocked. If you need to delete a distribution that is enabled and you do not
want to wait, you need to use the `retain_on_delete` flag.

## Example Usage

The following example below creates a CloudFront distribution with an S3 origin.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("b", {
    acl: "private",
    tags: {
        Name: "My bucket",
    },
});
const s3OriginId = "myS3Origin";
const s3Distribution = new aws.cloudfront.Distribution("s3_distribution", {
    aliases: [
        "mysite.example.com",
        "yoursite.example.com",
    ],
    comment: "Some comment",
    defaultCacheBehavior: {
        allowedMethods: [
            "DELETE",
            "GET",
            "HEAD",
            "OPTIONS",
            "PATCH",
            "POST",
            "PUT",
        ],
        cachedMethods: [
            "GET",
            "HEAD",
        ],
        defaultTtl: 3600,
        forwardedValues: {
            cookies: {
                forward: "none",
            },
            queryString: false,
        },
        maxTtl: 86400,
        minTtl: 0,
        targetOriginId: s3OriginId,
        viewerProtocolPolicy: "allow-all",
    },
    defaultRootObject: "index.html",
    enabled: true,
    isIpv6Enabled: true,
    loggingConfig: {
        bucket: "mylogs.s3.amazonaws.com",
        includeCookies: false,
        prefix: "myprefix",
    },
    orderedCacheBehaviors: [
        // Cache behavior with precedence 0
        {
            allowedMethods: [
                "GET",
                "HEAD",
                "OPTIONS",
            ],
            cachedMethods: [
                "GET",
                "HEAD",
                "OPTIONS",
            ],
            compress: true,
            defaultTtl: 86400,
            forwardedValues: {
                cookies: {
                    forward: "none",
                },
                headers: ["Origin"],
                queryString: false,
            },
            maxTtl: 31536000,
            minTtl: 0,
            pathPattern: "/content/immutable/*",
            targetOriginId: s3OriginId,
            viewerProtocolPolicy: "redirect-to-https",
        },
        // Cache behavior with precedence 1
        {
            allowedMethods: [
                "GET",
                "HEAD",
                "OPTIONS",
            ],
            cachedMethods: [
                "GET",
                "HEAD",
            ],
            compress: true,
            defaultTtl: 3600,
            forwardedValues: {
                cookies: {
                    forward: "none",
                },
                queryString: false,
            },
            maxTtl: 86400,
            minTtl: 0,
            pathPattern: "/content/*",
            targetOriginId: s3OriginId,
            viewerProtocolPolicy: "redirect-to-https",
        },
    ],
    origins: [{
        domainName: bucket.bucketRegionalDomainName,
        originId: s3OriginId,
        s3OriginConfig: {
            originAccessIdentity: "origin-access-identity/cloudfront/ABCDEFG1234567",
        },
    }],
    priceClass: "PriceClass_200",
    restrictions: {
        geoRestriction: {
            locations: [
                "US",
                "CA",
                "GB",
                "DE",
            ],
            restrictionType: "whitelist",
        },
    },
    tags: {
        Environment: "production",
    },
    viewerCertificate: {
        cloudfrontDefaultCertificate: true,
    },
});
```

The following example below creates a Cloudfront distribution with an origin group for failover routing:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const s3Distribution = new aws.cloudfront.Distribution("s3_distribution", {
    defaultCacheBehavior: {
        // ... other configuration ...
        targetOriginId: "groupS3",
    },
    origins: [
        {
            domainName: aws_s3_bucket_primary.bucketRegionalDomainName,
            originId: "primaryS3",
            s3OriginConfig: {
                originAccessIdentity: aws_cloudfront_origin_access_identity_default.cloudfrontAccessIdentityPath,
            },
        },
        {
            domainName: aws_s3_bucket_failover.bucketRegionalDomainName,
            originId: "failoverS3",
            s3OriginConfig: {
                originAccessIdentity: aws_cloudfront_origin_access_identity_default.cloudfrontAccessIdentityPath,
            },
        },
    ],
    originGroups: [{
        failoverCriteria: {
            statusCodes: [
                403,
                404,
                500,
                502,
            ],
        },
        members: [
            {
                originId: "primaryS3",
            },
            {
                originId: "failoverS3",
            },
        ],
        originId: "groupS3",
    }],
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudfront_distribution.html.markdown.



## Create a Distribution Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cloudfront/#Distribution">Distribution</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cloudfront/#DistributionArgs">DistributionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Distribution</span><span class="p">(resource_name, opts=None, </span>aliases=None<span class="p">, </span>comment=None<span class="p">, </span>custom_error_responses=None<span class="p">, </span>default_cache_behavior=None<span class="p">, </span>default_root_object=None<span class="p">, </span>enabled=None<span class="p">, </span>http_version=None<span class="p">, </span>is_ipv6_enabled=None<span class="p">, </span>logging_config=None<span class="p">, </span>ordered_cache_behaviors=None<span class="p">, </span>origin_groups=None<span class="p">, </span>origins=None<span class="p">, </span>price_class=None<span class="p">, </span>restrictions=None<span class="p">, </span>retain_on_delete=None<span class="p">, </span>tags=None<span class="p">, </span>viewer_certificate=None<span class="p">, </span>wait_for_deployment=None<span class="p">, </span>web_acl_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDistribution<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionArgs">DistributionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#Distribution">Distribution</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.Distribution.html">Distribution</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionArgs.html">DistributionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Distribution resource with the given unique name, arguments, and options.

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
            <td class="align-top">Aliases</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Extra CNAMEs (alternate domain names), if any, for
this distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Any comments you want to include about the
distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Error<wbr>Responses</td>
            <td class="align-top">
                
                <code><a href="#distributioncustomerrorresponse">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Custom<wbr>Error<wbr>Response<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more custom error response elements (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Cache<wbr>Behavior</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehavior">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The default cache behavior for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Root<wbr>Object</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the distribution is enabled to accept end
user requests for content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Http<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum HTTP version to support on the
distribution. Allowed values are `http1.1` and `http2`. The default is
`http2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Is<wbr>Ipv6Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the IPv6 is enabled for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#distributionloggingconfig">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Logging<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The logging
configuration that controls how logs are written
to your distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ordered<wbr>Cache<wbr>Behaviors</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehavior">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Groups</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroup">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Origin<wbr>Group<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more origin_group for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origins</td>
            <td class="align-top">
                
                <code><a href="#distributionorigin">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Origin<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One or more origins for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Price<wbr>Class</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The price class for this distribution. One of
`PriceClass_All`, `PriceClass_200`, `PriceClass_100`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Restrictions</td>
            <td class="align-top">
                
                <code><a href="#distributionrestrictions">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Restrictions<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The restriction
configuration for this distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retain<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: `false`.
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
    
        <tr>
            <td class="align-top">Viewer<wbr>Certificate</td>
            <td class="align-top">
                
                <code><a href="#distributionviewercertificate">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Viewer<wbr>Certificate<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The SSL
configuration for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Deployment</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If enabled, the resource will wait for
the distribution status to change from `InProgress` to `Deployed`. Setting
this to`false` will skip the process. Default: `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you&#39;re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
`waf:GetWebACL` permissions assigned.
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
            <td class="align-top">Aliases</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Extra CNAMEs (alternate domain names), if any, for
this distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Any comments you want to include about the
distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Error<wbr>Responses</td>
            <td class="align-top">
                
                <code><a href="#distributioncustomerrorresponse">[]cloudfront.<wbr>Distribution<wbr>Custom<wbr>Error<wbr>Response</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more custom error response elements (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Cache<wbr>Behavior</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehavior">cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The default cache behavior for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Root<wbr>Object</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the distribution is enabled to accept end
user requests for content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Http<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum HTTP version to support on the
distribution. Allowed values are `http1.1` and `http2`. The default is
`http2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Is<wbr>Ipv6Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the IPv6 is enabled for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#distributionloggingconfig">*cloudfront.<wbr>Distribution<wbr>Logging<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The logging
configuration that controls how logs are written
to your distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ordered<wbr>Cache<wbr>Behaviors</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehavior">[]cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Groups</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroup">[]cloudfront.<wbr>Distribution<wbr>Origin<wbr>Group</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more origin_group for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origins</td>
            <td class="align-top">
                
                <code><a href="#distributionorigin">[]cloudfront.<wbr>Distribution<wbr>Origin</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One or more origins for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Price<wbr>Class</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The price class for this distribution. One of
`PriceClass_All`, `PriceClass_200`, `PriceClass_100`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Restrictions</td>
            <td class="align-top">
                
                <code><a href="#distributionrestrictions">cloudfront.<wbr>Distribution<wbr>Restrictions</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The restriction
configuration for this distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retain<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: `false`.
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
    
        <tr>
            <td class="align-top">Viewer<wbr>Certificate</td>
            <td class="align-top">
                
                <code><a href="#distributionviewercertificate">cloudfront.<wbr>Distribution<wbr>Viewer<wbr>Certificate</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The SSL
configuration for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Deployment</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If enabled, the resource will wait for
the distribution status to change from `InProgress` to `Deployed`. Setting
this to`false` will skip the process. Default: `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you&#39;re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
`waf:GetWebACL` permissions assigned.
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
            <td class="align-top">aliases</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Extra CNAMEs (alternate domain names), if any, for
this distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Any comments you want to include about the
distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Error<wbr>Responses</td>
            <td class="align-top">
                
                <code><a href="#distributioncustomerrorresponse">cloudfront.<wbr>Distribution<wbr>Custom<wbr>Error<wbr>Response[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more custom error response elements (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Cache<wbr>Behavior</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehavior">cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The default cache behavior for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Root<wbr>Object</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the distribution is enabled to accept end
user requests for content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">http<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum HTTP version to support on the
distribution. Allowed values are `http1.1` and `http2`. The default is
`http2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">is<wbr>Ipv6Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the IPv6 is enabled for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#distributionloggingconfig">cloudfront.<wbr>Distribution<wbr>Logging<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The logging
configuration that controls how logs are written
to your distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ordered<wbr>Cache<wbr>Behaviors</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehavior">cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin<wbr>Groups</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroup">cloudfront.<wbr>Distribution<wbr>Origin<wbr>Group[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more origin_group for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origins</td>
            <td class="align-top">
                
                <code><a href="#distributionorigin">cloudfront.<wbr>Distribution<wbr>Origin[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One or more origins for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">price<wbr>Class</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The price class for this distribution. One of
`PriceClass_All`, `PriceClass_200`, `PriceClass_100`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">restrictions</td>
            <td class="align-top">
                
                <code><a href="#distributionrestrictions">cloudfront.<wbr>Distribution<wbr>Restrictions</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The restriction
configuration for this distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retain<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: `false`.
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
    
        <tr>
            <td class="align-top">viewer<wbr>Certificate</td>
            <td class="align-top">
                
                <code><a href="#distributionviewercertificate">cloudfront.<wbr>Distribution<wbr>Viewer<wbr>Certificate</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The SSL
configuration for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait<wbr>For<wbr>Deployment</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If enabled, the resource will wait for
the distribution status to change from `InProgress` to `Deployed`. Setting
this to`false` will skip the process. Default: `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you&#39;re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
`waf:GetWebACL` permissions assigned.
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
            <td class="align-top">aliases</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Extra CNAMEs (alternate domain names), if any, for
this distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Any comments you want to include about the
distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>error_<wbr>responses</td>
            <td class="align-top">
                
                <code><a href="#distributioncustomerrorresponse">List[distribution_<wbr>custom_<wbr>error_<wbr>response]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more custom error response elements (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>cache_<wbr>behavior</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehavior">Dict[distribution_<wbr>default_<wbr>cache_<wbr>behavior]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The default cache behavior for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>root_<wbr>object</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the distribution is enabled to accept end
user requests for content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">http_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum HTTP version to support on the
distribution. Allowed values are `http1.1` and `http2`. The default is
`http2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">is_<wbr>ipv6_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the IPv6 is enabled for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#distributionloggingconfig">Dict[distribution_<wbr>logging_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The logging
configuration that controls how logs are written
to your distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ordered_<wbr>cache_<wbr>behaviors</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehavior">List[distribution_<wbr>ordered_<wbr>cache_<wbr>behavior]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin_<wbr>groups</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroup">List[distribution_<wbr>origin_<wbr>group]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more origin_group for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origins</td>
            <td class="align-top">
                
                <code><a href="#distributionorigin">List[distribution_<wbr>origin]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One or more origins for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">price_<wbr>class</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The price class for this distribution. One of
`PriceClass_All`, `PriceClass_200`, `PriceClass_100`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">restrictions</td>
            <td class="align-top">
                
                <code><a href="#distributionrestrictions">Dict[distribution_<wbr>restrictions]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The restriction
configuration for this distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retain_<wbr>on_<wbr>delete</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">viewer_<wbr>certificate</td>
            <td class="align-top">
                
                <code><a href="#distributionviewercertificate">Dict[distribution_<wbr>viewer_<wbr>certificate]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The SSL
configuration for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait_<wbr>for_<wbr>deployment</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If enabled, the resource will wait for
the distribution status to change from `InProgress` to `Deployed`. Setting
this to`false` will skip the process. Default: `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">web_<wbr>acl_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you&#39;re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
`waf:GetWebACL` permissions assigned.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Distribution Output Properties

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
            <td class="align-top">Active<wbr>Trusted<wbr>Signers</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;</code>
            </td>
            <td class="align-top">{{% md %}} The key pair IDs that CloudFront is aware of for
each trusted signer, if the distribution is set up to serve private content
with signed URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Aliases</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} Extra CNAMEs (alternate domain names), if any, for
this distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Caller<wbr>Reference</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Internal value used by CloudFront to allow future
updates to the distribution configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Any comments you want to include about the
distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Error<wbr>Responses</td>
            <td class="align-top">
                
                <code><a href="#distributioncustomerrorresponse">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Custom<wbr>Error<wbr>Response&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more custom error response elements (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Cache<wbr>Behavior</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehavior">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior</a></code>
            </td>
            <td class="align-top">{{% md %}} The default cache behavior for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Root<wbr>Object</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS domain name of either the S3 bucket, or
web site of your custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether the distribution is enabled to accept end
user requests for content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Etag</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The current version of the distribution&#39;s information. For example:
`E2QWRUHAPOMQZL`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The CloudFront Route 53 zone ID that can be used to
route an [Alias Resource Record Set][7] to. This attribute is simply an
alias for the zone ID `Z2FDTNDATAQYW2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Http<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The maximum HTTP version to support on the
distribution. Allowed values are `http1.1` and `http2`. The default is
`http2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">In<wbr>Progress<wbr>Validation<wbr>Batches</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The number of invalidation batches
currently in progress.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Is<wbr>Ipv6Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether the IPv6 is enabled for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Modified<wbr>Time</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date and time the distribution was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#distributionloggingconfig">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Logging<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} The logging
configuration that controls how logs are written
to your distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ordered<wbr>Cache<wbr>Behaviors</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehavior">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Groups</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroup">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Origin<wbr>Group&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more origin_group for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origins</td>
            <td class="align-top">
                
                <code><a href="#distributionorigin">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Origin&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more origins for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Price<wbr>Class</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The price class for this distribution. One of
`PriceClass_All`, `PriceClass_200`, `PriceClass_100`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Restrictions</td>
            <td class="align-top">
                
                <code><a href="#distributionrestrictions">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Restrictions</a></code>
            </td>
            <td class="align-top">{{% md %}} The restriction
configuration for this distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retain<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The current status of the distribution. `Deployed` if the
distribution&#39;s information is fully propagated throughout the Amazon
CloudFront system.
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
    
        <tr>
            <td class="align-top">Viewer<wbr>Certificate</td>
            <td class="align-top">
                
                <code><a href="#distributionviewercertificate">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Viewer<wbr>Certificate</a></code>
            </td>
            <td class="align-top">{{% md %}} The SSL
configuration for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Deployment</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} If enabled, the resource will wait for
the distribution status to change from `InProgress` to `Deployed`. Setting
this to`false` will skip the process. Default: `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} If you&#39;re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
`waf:GetWebACL` permissions assigned.
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
            <td class="align-top">Active<wbr>Trusted<wbr>Signers</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} The key pair IDs that CloudFront is aware of for
each trusted signer, if the distribution is set up to serve private content
with signed URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Aliases</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} Extra CNAMEs (alternate domain names), if any, for
this distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Caller<wbr>Reference</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Internal value used by CloudFront to allow future
updates to the distribution configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Any comments you want to include about the
distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Error<wbr>Responses</td>
            <td class="align-top">
                
                <code><a href="#distributioncustomerrorresponse">[]cloudfront.<wbr>Distribution<wbr>Custom<wbr>Error<wbr>Response</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more custom error response elements (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Cache<wbr>Behavior</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehavior">cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior</a></code>
            </td>
            <td class="align-top">{{% md %}} The default cache behavior for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Root<wbr>Object</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS domain name of either the S3 bucket, or
web site of your custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether the distribution is enabled to accept end
user requests for content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Etag</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The current version of the distribution&#39;s information. For example:
`E2QWRUHAPOMQZL`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The CloudFront Route 53 zone ID that can be used to
route an [Alias Resource Record Set][7] to. This attribute is simply an
alias for the zone ID `Z2FDTNDATAQYW2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Http<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The maximum HTTP version to support on the
distribution. Allowed values are `http1.1` and `http2`. The default is
`http2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">In<wbr>Progress<wbr>Validation<wbr>Batches</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The number of invalidation batches
currently in progress.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Is<wbr>Ipv6Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether the IPv6 is enabled for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Modified<wbr>Time</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date and time the distribution was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#distributionloggingconfig">*cloudfront.<wbr>Distribution<wbr>Logging<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} The logging
configuration that controls how logs are written
to your distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ordered<wbr>Cache<wbr>Behaviors</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehavior">[]cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior</a></code>
            </td>
            <td class="align-top">{{% md %}} An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Groups</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroup">[]cloudfront.<wbr>Distribution<wbr>Origin<wbr>Group</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more origin_group for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origins</td>
            <td class="align-top">
                
                <code><a href="#distributionorigin">[]cloudfront.<wbr>Distribution<wbr>Origin</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more origins for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Price<wbr>Class</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The price class for this distribution. One of
`PriceClass_All`, `PriceClass_200`, `PriceClass_100`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Restrictions</td>
            <td class="align-top">
                
                <code><a href="#distributionrestrictions">cloudfront.<wbr>Distribution<wbr>Restrictions</a></code>
            </td>
            <td class="align-top">{{% md %}} The restriction
configuration for this distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retain<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The current status of the distribution. `Deployed` if the
distribution&#39;s information is fully propagated throughout the Amazon
CloudFront system.
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
    
        <tr>
            <td class="align-top">Viewer<wbr>Certificate</td>
            <td class="align-top">
                
                <code><a href="#distributionviewercertificate">cloudfront.<wbr>Distribution<wbr>Viewer<wbr>Certificate</a></code>
            </td>
            <td class="align-top">{{% md %}} The SSL
configuration for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Deployment</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} If enabled, the resource will wait for
the distribution status to change from `InProgress` to `Deployed`. Setting
this to`false` will skip the process. Default: `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} If you&#39;re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
`waf:GetWebACL` permissions assigned.
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
            <td class="align-top">active<wbr>Trusted<wbr>Signers</td>
            <td class="align-top">
                
                <code>{[key: string]: any}</code>
            </td>
            <td class="align-top">{{% md %}} The key pair IDs that CloudFront is aware of for
each trusted signer, if the distribution is set up to serve private content
with signed URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">aliases</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} Extra CNAMEs (alternate domain names), if any, for
this distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">caller<wbr>Reference</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Internal value used by CloudFront to allow future
updates to the distribution configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Any comments you want to include about the
distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Error<wbr>Responses</td>
            <td class="align-top">
                
                <code><a href="#distributioncustomerrorresponse">cloudfront.<wbr>Distribution<wbr>Custom<wbr>Error<wbr>Response[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more custom error response elements (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Cache<wbr>Behavior</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehavior">cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior</a></code>
            </td>
            <td class="align-top">{{% md %}} The default cache behavior for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Root<wbr>Object</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS domain name of either the S3 bucket, or
web site of your custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Whether the distribution is enabled to accept end
user requests for content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">etag</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The current version of the distribution&#39;s information. For example:
`E2QWRUHAPOMQZL`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The CloudFront Route 53 zone ID that can be used to
route an [Alias Resource Record Set][7] to. This attribute is simply an
alias for the zone ID `Z2FDTNDATAQYW2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">http<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The maximum HTTP version to support on the
distribution. Allowed values are `http1.1` and `http2`. The default is
`http2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">in<wbr>Progress<wbr>Validation<wbr>Batches</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The number of invalidation batches
currently in progress.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">is<wbr>Ipv6Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether the IPv6 is enabled for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last<wbr>Modified<wbr>Time</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date and time the distribution was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#distributionloggingconfig">cloudfront.<wbr>Distribution<wbr>Logging<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} The logging
configuration that controls how logs are written
to your distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ordered<wbr>Cache<wbr>Behaviors</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehavior">cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin<wbr>Groups</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroup">cloudfront.<wbr>Distribution<wbr>Origin<wbr>Group[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more origin_group for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origins</td>
            <td class="align-top">
                
                <code><a href="#distributionorigin">cloudfront.<wbr>Distribution<wbr>Origin[]</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more origins for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">price<wbr>Class</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The price class for this distribution. One of
`PriceClass_All`, `PriceClass_200`, `PriceClass_100`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">restrictions</td>
            <td class="align-top">
                
                <code><a href="#distributionrestrictions">cloudfront.<wbr>Distribution<wbr>Restrictions</a></code>
            </td>
            <td class="align-top">{{% md %}} The restriction
configuration for this distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retain<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The current status of the distribution. `Deployed` if the
distribution&#39;s information is fully propagated throughout the Amazon
CloudFront system.
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
    
        <tr>
            <td class="align-top">viewer<wbr>Certificate</td>
            <td class="align-top">
                
                <code><a href="#distributionviewercertificate">cloudfront.<wbr>Distribution<wbr>Viewer<wbr>Certificate</a></code>
            </td>
            <td class="align-top">{{% md %}} The SSL
configuration for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait<wbr>For<wbr>Deployment</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} If enabled, the resource will wait for
the distribution status to change from `InProgress` to `Deployed`. Setting
this to`false` will skip the process. Default: `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} If you&#39;re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
`waf:GetWebACL` permissions assigned.
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
            <td class="align-top">active_<wbr>trusted_<wbr>signers</td>
            <td class="align-top">
                
                <code>Dict[str, any]</code>
            </td>
            <td class="align-top">{{% md %}} The key pair IDs that CloudFront is aware of for
each trusted signer, if the distribution is set up to serve private content
with signed URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">aliases</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} Extra CNAMEs (alternate domain names), if any, for
this distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">caller_<wbr>reference</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Internal value used by CloudFront to allow future
updates to the distribution configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Any comments you want to include about the
distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>error_<wbr>responses</td>
            <td class="align-top">
                
                <code><a href="#distributioncustomerrorresponse">List[distribution_<wbr>custom_<wbr>error_<wbr>response]</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more custom error response elements (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>cache_<wbr>behavior</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehavior">Dict[distribution_<wbr>default_<wbr>cache_<wbr>behavior]</a></code>
            </td>
            <td class="align-top">{{% md %}} The default cache behavior for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>root_<wbr>object</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The DNS domain name of either the S3 bucket, or
web site of your custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether the distribution is enabled to accept end
user requests for content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">etag</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The current version of the distribution&#39;s information. For example:
`E2QWRUHAPOMQZL`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hosted_<wbr>zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The CloudFront Route 53 zone ID that can be used to
route an [Alias Resource Record Set][7] to. This attribute is simply an
alias for the zone ID `Z2FDTNDATAQYW2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">http_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The maximum HTTP version to support on the
distribution. Allowed values are `http1.1` and `http2`. The default is
`http2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">in_<wbr>progress_<wbr>validation_<wbr>batches</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The number of invalidation batches
currently in progress.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">is_<wbr>ipv6_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether the IPv6 is enabled for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last_<wbr>modified_<wbr>time</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The date and time the distribution was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#distributionloggingconfig">Dict[distribution_<wbr>logging_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} The logging
configuration that controls how logs are written
to your distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ordered_<wbr>cache_<wbr>behaviors</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehavior">List[distribution_<wbr>ordered_<wbr>cache_<wbr>behavior]</a></code>
            </td>
            <td class="align-top">{{% md %}} An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin_<wbr>groups</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroup">List[distribution_<wbr>origin_<wbr>group]</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more origin_group for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origins</td>
            <td class="align-top">
                
                <code><a href="#distributionorigin">List[distribution_<wbr>origin]</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more origins for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">price_<wbr>class</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The price class for this distribution. One of
`PriceClass_All`, `PriceClass_200`, `PriceClass_100`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">restrictions</td>
            <td class="align-top">
                
                <code><a href="#distributionrestrictions">Dict[distribution_<wbr>restrictions]</a></code>
            </td>
            <td class="align-top">{{% md %}} The restriction
configuration for this distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retain_<wbr>on_<wbr>delete</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The current status of the distribution. `Deployed` if the
distribution&#39;s information is fully propagated throughout the Amazon
CloudFront system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">viewer_<wbr>certificate</td>
            <td class="align-top">
                
                <code><a href="#distributionviewercertificate">Dict[distribution_<wbr>viewer_<wbr>certificate]</a></code>
            </td>
            <td class="align-top">{{% md %}} The SSL
configuration for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait_<wbr>for_<wbr>deployment</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If enabled, the resource will wait for
the distribution status to change from `InProgress` to `Deployed`. Setting
this to`false` will skip the process. Default: `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">web_<wbr>acl_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} If you&#39;re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
`waf:GetWebACL` permissions assigned.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Distribution Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cloudfront/#DistributionState">DistributionState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cloudfront/#Distribution">Distribution</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>active_trusted_signers=None<span class="p">, </span>aliases=None<span class="p">, </span>arn=None<span class="p">, </span>caller_reference=None<span class="p">, </span>comment=None<span class="p">, </span>custom_error_responses=None<span class="p">, </span>default_cache_behavior=None<span class="p">, </span>default_root_object=None<span class="p">, </span>domain_name=None<span class="p">, </span>enabled=None<span class="p">, </span>etag=None<span class="p">, </span>hosted_zone_id=None<span class="p">, </span>http_version=None<span class="p">, </span>in_progress_validation_batches=None<span class="p">, </span>is_ipv6_enabled=None<span class="p">, </span>last_modified_time=None<span class="p">, </span>logging_config=None<span class="p">, </span>ordered_cache_behaviors=None<span class="p">, </span>origin_groups=None<span class="p">, </span>origins=None<span class="p">, </span>price_class=None<span class="p">, </span>restrictions=None<span class="p">, </span>retain_on_delete=None<span class="p">, </span>status=None<span class="p">, </span>tags=None<span class="p">, </span>viewer_certificate=None<span class="p">, </span>wait_for_deployment=None<span class="p">, </span>web_acl_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetDistribution<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionState">DistributionState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#Distribution">Distribution</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.Distribution.html">Distribution</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionState.html">DistributionState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Distribution resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Active<wbr>Trusted<wbr>Signers</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key pair IDs that CloudFront is aware of for
each trusted signer, if the distribution is set up to serve private content
with signed URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Aliases</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Extra CNAMEs (alternate domain names), if any, for
this distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Caller<wbr>Reference</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Internal value used by CloudFront to allow future
updates to the distribution configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Any comments you want to include about the
distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Error<wbr>Responses</td>
            <td class="align-top">
                
                <code><a href="#distributioncustomerrorresponse">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Custom<wbr>Error<wbr>Response<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more custom error response elements (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Cache<wbr>Behavior</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehavior">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default cache behavior for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Root<wbr>Object</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.
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
The DNS domain name of either the S3 bucket, or
web site of your custom origin.
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
Whether the distribution is enabled to accept end
user requests for content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Etag</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The current version of the distribution&#39;s information. For example:
`E2QWRUHAPOMQZL`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudFront Route 53 zone ID that can be used to
route an [Alias Resource Record Set][7] to. This attribute is simply an
alias for the zone ID `Z2FDTNDATAQYW2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Http<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum HTTP version to support on the
distribution. Allowed values are `http1.1` and `http2`. The default is
`http2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">In<wbr>Progress<wbr>Validation<wbr>Batches</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of invalidation batches
currently in progress.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Is<wbr>Ipv6Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the IPv6 is enabled for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Modified<wbr>Time</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date and time the distribution was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#distributionloggingconfig">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Logging<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The logging
configuration that controls how logs are written
to your distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ordered<wbr>Cache<wbr>Behaviors</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehavior">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Groups</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroup">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Origin<wbr>Group<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more origin_group for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origins</td>
            <td class="align-top">
                
                <code><a href="#distributionorigin">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Origin<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more origins for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Price<wbr>Class</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The price class for this distribution. One of
`PriceClass_All`, `PriceClass_200`, `PriceClass_100`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Restrictions</td>
            <td class="align-top">
                
                <code><a href="#distributionrestrictions">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Restrictions<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The restriction
configuration for this distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retain<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The current status of the distribution. `Deployed` if the
distribution&#39;s information is fully propagated throughout the Amazon
CloudFront system.
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
    
        <tr>
            <td class="align-top">Viewer<wbr>Certificate</td>
            <td class="align-top">
                
                <code><a href="#distributionviewercertificate">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Viewer<wbr>Certificate<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SSL
configuration for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Deployment</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If enabled, the resource will wait for
the distribution status to change from `InProgress` to `Deployed`. Setting
this to`false` will skip the process. Default: `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you&#39;re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
`waf:GetWebACL` permissions assigned.
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
            <td class="align-top">Active<wbr>Trusted<wbr>Signers</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key pair IDs that CloudFront is aware of for
each trusted signer, if the distribution is set up to serve private content
with signed URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Aliases</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Extra CNAMEs (alternate domain names), if any, for
this distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Caller<wbr>Reference</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Internal value used by CloudFront to allow future
updates to the distribution configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Any comments you want to include about the
distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Error<wbr>Responses</td>
            <td class="align-top">
                
                <code><a href="#distributioncustomerrorresponse">[]cloudfront.<wbr>Distribution<wbr>Custom<wbr>Error<wbr>Response</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more custom error response elements (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Cache<wbr>Behavior</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehavior">*cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default cache behavior for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Root<wbr>Object</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.
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
The DNS domain name of either the S3 bucket, or
web site of your custom origin.
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
Whether the distribution is enabled to accept end
user requests for content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Etag</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The current version of the distribution&#39;s information. For example:
`E2QWRUHAPOMQZL`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudFront Route 53 zone ID that can be used to
route an [Alias Resource Record Set][7] to. This attribute is simply an
alias for the zone ID `Z2FDTNDATAQYW2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Http<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum HTTP version to support on the
distribution. Allowed values are `http1.1` and `http2`. The default is
`http2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">In<wbr>Progress<wbr>Validation<wbr>Batches</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of invalidation batches
currently in progress.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Is<wbr>Ipv6Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the IPv6 is enabled for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Modified<wbr>Time</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date and time the distribution was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#distributionloggingconfig">*cloudfront.<wbr>Distribution<wbr>Logging<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The logging
configuration that controls how logs are written
to your distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ordered<wbr>Cache<wbr>Behaviors</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehavior">[]cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Groups</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroup">[]cloudfront.<wbr>Distribution<wbr>Origin<wbr>Group</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more origin_group for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origins</td>
            <td class="align-top">
                
                <code><a href="#distributionorigin">[]cloudfront.<wbr>Distribution<wbr>Origin</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more origins for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Price<wbr>Class</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The price class for this distribution. One of
`PriceClass_All`, `PriceClass_200`, `PriceClass_100`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Restrictions</td>
            <td class="align-top">
                
                <code><a href="#distributionrestrictions">*cloudfront.<wbr>Distribution<wbr>Restrictions</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The restriction
configuration for this distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retain<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The current status of the distribution. `Deployed` if the
distribution&#39;s information is fully propagated throughout the Amazon
CloudFront system.
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
    
        <tr>
            <td class="align-top">Viewer<wbr>Certificate</td>
            <td class="align-top">
                
                <code><a href="#distributionviewercertificate">*cloudfront.<wbr>Distribution<wbr>Viewer<wbr>Certificate</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SSL
configuration for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Deployment</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If enabled, the resource will wait for
the distribution status to change from `InProgress` to `Deployed`. Setting
this to`false` will skip the process. Default: `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you&#39;re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
`waf:GetWebACL` permissions assigned.
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
            <td class="align-top">active<wbr>Trusted<wbr>Signers</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key pair IDs that CloudFront is aware of for
each trusted signer, if the distribution is set up to serve private content
with signed URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">aliases</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Extra CNAMEs (alternate domain names), if any, for
this distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">caller<wbr>Reference</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Internal value used by CloudFront to allow future
updates to the distribution configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Any comments you want to include about the
distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Error<wbr>Responses</td>
            <td class="align-top">
                
                <code><a href="#distributioncustomerrorresponse">cloudfront.<wbr>Distribution<wbr>Custom<wbr>Error<wbr>Response[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more custom error response elements (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Cache<wbr>Behavior</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehavior">cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default cache behavior for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Root<wbr>Object</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.
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
The DNS domain name of either the S3 bucket, or
web site of your custom origin.
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
Whether the distribution is enabled to accept end
user requests for content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">etag</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The current version of the distribution&#39;s information. For example:
`E2QWRUHAPOMQZL`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hosted<wbr>Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudFront Route 53 zone ID that can be used to
route an [Alias Resource Record Set][7] to. This attribute is simply an
alias for the zone ID `Z2FDTNDATAQYW2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">http<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum HTTP version to support on the
distribution. Allowed values are `http1.1` and `http2`. The default is
`http2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">in<wbr>Progress<wbr>Validation<wbr>Batches</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of invalidation batches
currently in progress.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">is<wbr>Ipv6Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the IPv6 is enabled for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last<wbr>Modified<wbr>Time</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date and time the distribution was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#distributionloggingconfig">cloudfront.<wbr>Distribution<wbr>Logging<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The logging
configuration that controls how logs are written
to your distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ordered<wbr>Cache<wbr>Behaviors</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehavior">cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin<wbr>Groups</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroup">cloudfront.<wbr>Distribution<wbr>Origin<wbr>Group[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more origin_group for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origins</td>
            <td class="align-top">
                
                <code><a href="#distributionorigin">cloudfront.<wbr>Distribution<wbr>Origin[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more origins for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">price<wbr>Class</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The price class for this distribution. One of
`PriceClass_All`, `PriceClass_200`, `PriceClass_100`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">restrictions</td>
            <td class="align-top">
                
                <code><a href="#distributionrestrictions">cloudfront.<wbr>Distribution<wbr>Restrictions?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The restriction
configuration for this distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retain<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The current status of the distribution. `Deployed` if the
distribution&#39;s information is fully propagated throughout the Amazon
CloudFront system.
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
    
        <tr>
            <td class="align-top">viewer<wbr>Certificate</td>
            <td class="align-top">
                
                <code><a href="#distributionviewercertificate">cloudfront.<wbr>Distribution<wbr>Viewer<wbr>Certificate?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SSL
configuration for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait<wbr>For<wbr>Deployment</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If enabled, the resource will wait for
the distribution status to change from `InProgress` to `Deployed`. Setting
this to`false` will skip the process. Default: `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">web<wbr>Acl<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you&#39;re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
`waf:GetWebACL` permissions assigned.
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
            <td class="align-top">active_<wbr>trusted_<wbr>signers</td>
            <td class="align-top">
                
                <code>Dict[str, any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key pair IDs that CloudFront is aware of for
each trusted signer, if the distribution is set up to serve private content
with signed URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">aliases</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Extra CNAMEs (alternate domain names), if any, for
this distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">caller_<wbr>reference</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Internal value used by CloudFront to allow future
updates to the distribution configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Any comments you want to include about the
distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>error_<wbr>responses</td>
            <td class="align-top">
                
                <code><a href="#distributioncustomerrorresponse">List[distribution_<wbr>custom_<wbr>error_<wbr>response]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more custom error response elements (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>cache_<wbr>behavior</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehavior">Dict[distribution_<wbr>default_<wbr>cache_<wbr>behavior]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default cache behavior for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>root_<wbr>object</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The object that you want CloudFront to
return (for example, index.html) when an end user requests the root URL.
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
The DNS domain name of either the S3 bucket, or
web site of your custom origin.
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
Whether the distribution is enabled to accept end
user requests for content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">etag</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The current version of the distribution&#39;s information. For example:
`E2QWRUHAPOMQZL`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hosted_<wbr>zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudFront Route 53 zone ID that can be used to
route an [Alias Resource Record Set][7] to. This attribute is simply an
alias for the zone ID `Z2FDTNDATAQYW2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">http_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum HTTP version to support on the
distribution. Allowed values are `http1.1` and `http2`. The default is
`http2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">in_<wbr>progress_<wbr>validation_<wbr>batches</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of invalidation batches
currently in progress.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">is_<wbr>ipv6_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the IPv6 is enabled for the distribution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last_<wbr>modified_<wbr>time</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date and time the distribution was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#distributionloggingconfig">Dict[distribution_<wbr>logging_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The logging
configuration that controls how logs are written
to your distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ordered_<wbr>cache_<wbr>behaviors</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehavior">List[distribution_<wbr>ordered_<wbr>cache_<wbr>behavior]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An ordered list of cache behaviors
resource for this distribution. List from top to bottom
in order of precedence. The topmost cache behavior will have precedence 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin_<wbr>groups</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroup">List[distribution_<wbr>origin_<wbr>group]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more origin_group for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origins</td>
            <td class="align-top">
                
                <code><a href="#distributionorigin">List[distribution_<wbr>origin]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more origins for this
distribution (multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">price_<wbr>class</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The price class for this distribution. One of
`PriceClass_All`, `PriceClass_200`, `PriceClass_100`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">restrictions</td>
            <td class="align-top">
                
                <code><a href="#distributionrestrictions">Dict[distribution_<wbr>restrictions]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The restriction
configuration for this distribution (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retain_<wbr>on_<wbr>delete</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Disables the distribution instead of
deleting it when destroying the resource. If this is set,
the distribution needs to be deleted manually afterwards. Default: `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The current status of the distribution. `Deployed` if the
distribution&#39;s information is fully propagated throughout the Amazon
CloudFront system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">viewer_<wbr>certificate</td>
            <td class="align-top">
                
                <code><a href="#distributionviewercertificate">Dict[distribution_<wbr>viewer_<wbr>certificate]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SSL
configuration for this distribution (maximum
one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait_<wbr>for_<wbr>deployment</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If enabled, the resource will wait for
the distribution status to change from `InProgress` to `Deployed`. Setting
this to`false` will skip the process. Default: `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">web_<wbr>acl_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you&#39;re using AWS WAF to filter CloudFront
requests, the Id of the AWS WAF web ACL that is associated with the
distribution. The WAF Web ACL must exist in the WAF Global (CloudFront)
region and the credentials configuring this argument must have
`waf:GetWebACL` permissions assigned.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### DistributionCustomErrorResponse
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionCustomErrorResponse">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionCustomErrorResponse">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionCustomErrorResponseArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionCustomErrorResponseOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionCustomErrorResponseArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionCustomErrorResponse.html">output</a> API doc for this type.
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
            <td class="align-top">Error<wbr>Caching<wbr>Min<wbr>Ttl</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum amount of time you want
HTTP error codes to stay in CloudFront caches before CloudFront queries your
origin to see whether the object has been updated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Error<wbr>Code</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The 4xx or 5xx HTTP status code that you want to
customize.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Code</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP status code that you want CloudFront
to return with the custom error page to the viewer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Page<wbr>Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path of the custom error page (for
example, `/custom_404.html`).
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
            <td class="align-top">Error<wbr>Caching<wbr>Min<wbr>Ttl</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum amount of time you want
HTTP error codes to stay in CloudFront caches before CloudFront queries your
origin to see whether the object has been updated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Error<wbr>Code</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The 4xx or 5xx HTTP status code that you want to
customize.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Code</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP status code that you want CloudFront
to return with the custom error page to the viewer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Page<wbr>Path</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path of the custom error page (for
example, `/custom_404.html`).
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
            <td class="align-top">error<wbr>Caching<wbr>Min<wbr>Ttl</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum amount of time you want
HTTP error codes to stay in CloudFront caches before CloudFront queries your
origin to see whether the object has been updated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">error<wbr>Code</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The 4xx or 5xx HTTP status code that you want to
customize.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response<wbr>Code</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP status code that you want CloudFront
to return with the custom error page to the viewer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response<wbr>Page<wbr>Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path of the custom error page (for
example, `/custom_404.html`).
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
            <td class="align-top">error_<wbr>caching_<wbr>min_<wbr>ttl</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum amount of time you want
HTTP error codes to stay in CloudFront caches before CloudFront queries your
origin to see whether the object has been updated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">error_<wbr>code</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The 4xx or 5xx HTTP status code that you want to
customize.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response_<wbr>code</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP status code that you want CloudFront
to return with the custom error page to the viewer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response_<wbr>page_<wbr>path</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path of the custom error page (for
example, `/custom_404.html`).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionDefaultCacheBehavior
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionDefaultCacheBehavior">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionDefaultCacheBehavior">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionDefaultCacheBehaviorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionDefaultCacheBehaviorOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionDefaultCacheBehaviorArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionDefaultCacheBehavior.html">output</a> API doc for this type.
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
            <td class="align-top">Allowed<wbr>Methods</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Controls which HTTP methods CloudFront
processes and forwards to your Amazon S3 bucket or your custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cached<wbr>Methods</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Controls whether CloudFront caches the
response to requests using the specified HTTP methods.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compress</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you want CloudFront to automatically
compress content for web requests that include `Accept-Encoding: gzip` in
the request header (default: `false`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Ttl</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
in the absence of an `Cache-Control max-age` or `Expires` header. Defaults to
1 day.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Field<wbr>Level<wbr>Encryption<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Field level encryption configuration ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Forwarded<wbr>Values</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehaviorforwardedvalues">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior<wbr>Forwarded<wbr>Values<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The forwarded values configuration that specifies how CloudFront
handles query strings, cookies and headers (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Function<wbr>Associations</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehaviorlambdafunctionassociation">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior<wbr>Lambda<wbr>Function<wbr>Association<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A config block that triggers a lambda function with
specific actions. Defined below, maximum 4.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Ttl</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
to your origin to determine whether the object has been updated. Only
effective in the presence of `Cache-Control max-age`, `Cache-Control
s-maxage`, and `Expires` headers. Defaults to 365 days.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Ttl</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum amount of time that you want objects to
stay in CloudFront caches before CloudFront queries your origin to see
whether the object has been updated. Defaults to 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Smooth<wbr>Streaming</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether you want to distribute
media files in Microsoft Smooth Streaming format using the origin that is
associated with this cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Origin<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The value of ID for the origin that you want
CloudFront to route requests to when a request matches the path pattern
either for a cache behavior or for the default cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Trusted<wbr>Signers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS accounts, if any, that you want to
allow to create signed URLs for private content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Viewer<wbr>Protocol<wbr>Policy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Use this element to specify the
protocol that users can use to access the files in the origin specified by
TargetOriginId when a request matches the path pattern in PathPattern. One
of `allow-all`, `https-only`, or `redirect-to-https`.
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
            <td class="align-top">Allowed<wbr>Methods</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Controls which HTTP methods CloudFront
processes and forwards to your Amazon S3 bucket or your custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cached<wbr>Methods</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Controls whether CloudFront caches the
response to requests using the specified HTTP methods.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compress</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you want CloudFront to automatically
compress content for web requests that include `Accept-Encoding: gzip` in
the request header (default: `false`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Ttl</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
in the absence of an `Cache-Control max-age` or `Expires` header. Defaults to
1 day.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Field<wbr>Level<wbr>Encryption<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Field level encryption configuration ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Forwarded<wbr>Values</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehaviorforwardedvalues">cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior<wbr>Forwarded<wbr>Values</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The forwarded values configuration that specifies how CloudFront
handles query strings, cookies and headers (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Function<wbr>Associations</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehaviorlambdafunctionassociation">[]cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior<wbr>Lambda<wbr>Function<wbr>Association</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A config block that triggers a lambda function with
specific actions. Defined below, maximum 4.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Ttl</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
to your origin to determine whether the object has been updated. Only
effective in the presence of `Cache-Control max-age`, `Cache-Control
s-maxage`, and `Expires` headers. Defaults to 365 days.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Ttl</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum amount of time that you want objects to
stay in CloudFront caches before CloudFront queries your origin to see
whether the object has been updated. Defaults to 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Smooth<wbr>Streaming</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether you want to distribute
media files in Microsoft Smooth Streaming format using the origin that is
associated with this cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Origin<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The value of ID for the origin that you want
CloudFront to route requests to when a request matches the path pattern
either for a cache behavior or for the default cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Trusted<wbr>Signers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS accounts, if any, that you want to
allow to create signed URLs for private content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Viewer<wbr>Protocol<wbr>Policy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Use this element to specify the
protocol that users can use to access the files in the origin specified by
TargetOriginId when a request matches the path pattern in PathPattern. One
of `allow-all`, `https-only`, or `redirect-to-https`.
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
            <td class="align-top">allowed<wbr>Methods</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Controls which HTTP methods CloudFront
processes and forwards to your Amazon S3 bucket or your custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cached<wbr>Methods</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Controls whether CloudFront caches the
response to requests using the specified HTTP methods.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compress</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you want CloudFront to automatically
compress content for web requests that include `Accept-Encoding: gzip` in
the request header (default: `false`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Ttl</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
in the absence of an `Cache-Control max-age` or `Expires` header. Defaults to
1 day.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">field<wbr>Level<wbr>Encryption<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Field level encryption configuration ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">forwarded<wbr>Values</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehaviorforwardedvalues">cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior<wbr>Forwarded<wbr>Values</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The forwarded values configuration that specifies how CloudFront
handles query strings, cookies and headers (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Function<wbr>Associations</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehaviorlambdafunctionassociation">cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior<wbr>Lambda<wbr>Function<wbr>Association[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A config block that triggers a lambda function with
specific actions. Defined below, maximum 4.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Ttl</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
to your origin to determine whether the object has been updated. Only
effective in the presence of `Cache-Control max-age`, `Cache-Control
s-maxage`, and `Expires` headers. Defaults to 365 days.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Ttl</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum amount of time that you want objects to
stay in CloudFront caches before CloudFront queries your origin to see
whether the object has been updated. Defaults to 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">smooth<wbr>Streaming</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether you want to distribute
media files in Microsoft Smooth Streaming format using the origin that is
associated with this cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Origin<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The value of ID for the origin that you want
CloudFront to route requests to when a request matches the path pattern
either for a cache behavior or for the default cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">trusted<wbr>Signers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS accounts, if any, that you want to
allow to create signed URLs for private content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">viewer<wbr>Protocol<wbr>Policy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Use this element to specify the
protocol that users can use to access the files in the origin specified by
TargetOriginId when a request matches the path pattern in PathPattern. One
of `allow-all`, `https-only`, or `redirect-to-https`.
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
            <td class="align-top">allowed_<wbr>methods</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Controls which HTTP methods CloudFront
processes and forwards to your Amazon S3 bucket or your custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cached_<wbr>methods</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Controls whether CloudFront caches the
response to requests using the specified HTTP methods.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compress</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you want CloudFront to automatically
compress content for web requests that include `Accept-Encoding: gzip` in
the request header (default: `false`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>ttl</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
in the absence of an `Cache-Control max-age` or `Expires` header. Defaults to
1 day.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">field_<wbr>level_<wbr>encryption_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Field level encryption configuration ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">forwarded_<wbr>values</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehaviorforwardedvalues">Dict[distribution_<wbr>default_<wbr>cache_<wbr>behavior_<wbr>forwarded_<wbr>values]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The forwarded values configuration that specifies how CloudFront
handles query strings, cookies and headers (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>function_<wbr>associations</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehaviorlambdafunctionassociation">List[distribution_<wbr>default_<wbr>cache_<wbr>behavior_<wbr>lambda_<wbr>function_<wbr>association]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A config block that triggers a lambda function with
specific actions. Defined below, maximum 4.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>ttl</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
to your origin to determine whether the object has been updated. Only
effective in the presence of `Cache-Control max-age`, `Cache-Control
s-maxage`, and `Expires` headers. Defaults to 365 days.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min_<wbr>ttl</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum amount of time that you want objects to
stay in CloudFront caches before CloudFront queries your origin to see
whether the object has been updated. Defaults to 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">smooth_<wbr>streaming</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether you want to distribute
media files in Microsoft Smooth Streaming format using the origin that is
associated with this cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>origin_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The value of ID for the origin that you want
CloudFront to route requests to when a request matches the path pattern
either for a cache behavior or for the default cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">trusted_<wbr>signers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS accounts, if any, that you want to
allow to create signed URLs for private content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">viewer_<wbr>protocol_<wbr>policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Use this element to specify the
protocol that users can use to access the files in the origin specified by
TargetOriginId when a request matches the path pattern in PathPattern. One
of `allow-all`, `https-only`, or `redirect-to-https`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionDefaultCacheBehaviorForwardedValues
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionDefaultCacheBehaviorForwardedValues">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionDefaultCacheBehaviorForwardedValues">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionDefaultCacheBehaviorForwardedValuesArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionDefaultCacheBehaviorForwardedValuesOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionDefaultCacheBehaviorForwardedValuesArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionDefaultCacheBehaviorForwardedValues.html">output</a> API doc for this type.
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
            <td class="align-top">Cookies</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehaviorforwardedvaluescookies">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior<wbr>Forwarded<wbr>Values<wbr>Cookies<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The forwarded values cookies
that specifies how CloudFront handles cookies (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Headers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the Headers, if any, that you want
CloudFront to vary upon for this cache behavior. Specify `*` to include all
headers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Query<wbr>String</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether you want CloudFront to forward
query strings to the origin that is associated with this cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Query<wbr>String<wbr>Cache<wbr>Keys</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When specified, along with a value of
`true` for `query_string`, all query strings are forwarded, however only the
query string keys listed in this argument are cached. When omitted with a
value of `true` for `query_string`, all query string keys are cached.
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
            <td class="align-top">Cookies</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehaviorforwardedvaluescookies">cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior<wbr>Forwarded<wbr>Values<wbr>Cookies</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The forwarded values cookies
that specifies how CloudFront handles cookies (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Headers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the Headers, if any, that you want
CloudFront to vary upon for this cache behavior. Specify `*` to include all
headers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Query<wbr>String</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether you want CloudFront to forward
query strings to the origin that is associated with this cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Query<wbr>String<wbr>Cache<wbr>Keys</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When specified, along with a value of
`true` for `query_string`, all query strings are forwarded, however only the
query string keys listed in this argument are cached. When omitted with a
value of `true` for `query_string`, all query string keys are cached.
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
            <td class="align-top">cookies</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehaviorforwardedvaluescookies">cloudfront.<wbr>Distribution<wbr>Default<wbr>Cache<wbr>Behavior<wbr>Forwarded<wbr>Values<wbr>Cookies</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The forwarded values cookies
that specifies how CloudFront handles cookies (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">headers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the Headers, if any, that you want
CloudFront to vary upon for this cache behavior. Specify `*` to include all
headers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">query<wbr>String</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether you want CloudFront to forward
query strings to the origin that is associated with this cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">query<wbr>String<wbr>Cache<wbr>Keys</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When specified, along with a value of
`true` for `query_string`, all query strings are forwarded, however only the
query string keys listed in this argument are cached. When omitted with a
value of `true` for `query_string`, all query string keys are cached.
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
            <td class="align-top">cookies</td>
            <td class="align-top">
                
                <code><a href="#distributiondefaultcachebehaviorforwardedvaluescookies">Dict[distribution_<wbr>default_<wbr>cache_<wbr>behavior_<wbr>forwarded_<wbr>values_<wbr>cookies]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The forwarded values cookies
that specifies how CloudFront handles cookies (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">headers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the Headers, if any, that you want
CloudFront to vary upon for this cache behavior. Specify `*` to include all
headers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">query_<wbr>string</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether you want CloudFront to forward
query strings to the origin that is associated with this cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">query_<wbr>string_<wbr>cache_<wbr>keys</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When specified, along with a value of
`true` for `query_string`, all query strings are forwarded, however only the
query string keys listed in this argument are cached. When omitted with a
value of `true` for `query_string`, all query string keys are cached.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionDefaultCacheBehaviorForwardedValuesCookies
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionDefaultCacheBehaviorForwardedValuesCookies">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionDefaultCacheBehaviorForwardedValuesCookies">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionDefaultCacheBehaviorForwardedValuesCookiesArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionDefaultCacheBehaviorForwardedValuesCookiesOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionDefaultCacheBehaviorForwardedValuesCookiesArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionDefaultCacheBehaviorForwardedValuesCookies.html">output</a> API doc for this type.
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
            <td class="align-top">Forward</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether you want CloudFront to forward
cookies to the origin that is associated with this cache behavior. You can
specify `all`, `none` or `whitelist`. If `whitelist`, you must include the
subsequent `whitelisted_names`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Whitelisted<wbr>Names</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you have specified `whitelist` to
`forward`, the whitelisted cookies that you want CloudFront to forward to
your origin.
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
            <td class="align-top">Forward</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether you want CloudFront to forward
cookies to the origin that is associated with this cache behavior. You can
specify `all`, `none` or `whitelist`. If `whitelist`, you must include the
subsequent `whitelisted_names`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Whitelisted<wbr>Names</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you have specified `whitelist` to
`forward`, the whitelisted cookies that you want CloudFront to forward to
your origin.
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
            <td class="align-top">forward</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether you want CloudFront to forward
cookies to the origin that is associated with this cache behavior. You can
specify `all`, `none` or `whitelist`. If `whitelist`, you must include the
subsequent `whitelisted_names`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">whitelisted<wbr>Names</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you have specified `whitelist` to
`forward`, the whitelisted cookies that you want CloudFront to forward to
your origin.
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
            <td class="align-top">forward</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether you want CloudFront to forward
cookies to the origin that is associated with this cache behavior. You can
specify `all`, `none` or `whitelist`. If `whitelist`, you must include the
subsequent `whitelisted_names`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">whitelisted_<wbr>names</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you have specified `whitelist` to
`forward`, the whitelisted cookies that you want CloudFront to forward to
your origin.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionDefaultCacheBehaviorLambdaFunctionAssociation
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionDefaultCacheBehaviorLambdaFunctionAssociation">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionDefaultCacheBehaviorLambdaFunctionAssociation">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionDefaultCacheBehaviorLambdaFunctionAssociationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionDefaultCacheBehaviorLambdaFunctionAssociationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionDefaultCacheBehaviorLambdaFunctionAssociationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionDefaultCacheBehaviorLambdaFunctionAssociation.html">output</a> API doc for this type.
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
            <td class="align-top">Event<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The specific event to trigger this function.
Valid values: `viewer-request`, `origin-request`, `viewer-response`,
`origin-response`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Include<wbr>Body</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to true it exposes the request body to the lambda function. Defaults to false. Valid values: `true`, `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the Lambda function.
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
            <td class="align-top">Event<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The specific event to trigger this function.
Valid values: `viewer-request`, `origin-request`, `viewer-response`,
`origin-response`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Include<wbr>Body</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to true it exposes the request body to the lambda function. Defaults to false. Valid values: `true`, `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the Lambda function.
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
            <td class="align-top">event<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The specific event to trigger this function.
Valid values: `viewer-request`, `origin-request`, `viewer-response`,
`origin-response`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">include<wbr>Body</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to true it exposes the request body to the lambda function. Defaults to false. Valid values: `true`, `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the Lambda function.
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
            <td class="align-top">event_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The specific event to trigger this function.
Valid values: `viewer-request`, `origin-request`, `viewer-response`,
`origin-response`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">include_<wbr>body</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to true it exposes the request body to the lambda function. Defaults to false. Valid values: `true`, `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionLoggingConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionLoggingConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionLoggingConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionLoggingConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionLoggingConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionLoggingConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionLoggingConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon S3 bucket to store the access logs in, for
example, `myawslogbucket.s3.amazonaws.com`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Include<wbr>Cookies</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether you want CloudFront to
include cookies in access logs (default: `false`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional string that you want CloudFront to prefix
to the access log filenames for this distribution, for example, `myprefix/`.
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
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon S3 bucket to store the access logs in, for
example, `myawslogbucket.s3.amazonaws.com`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Include<wbr>Cookies</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether you want CloudFront to
include cookies in access logs (default: `false`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional string that you want CloudFront to prefix
to the access log filenames for this distribution, for example, `myprefix/`.
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
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon S3 bucket to store the access logs in, for
example, `myawslogbucket.s3.amazonaws.com`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">include<wbr>Cookies</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether you want CloudFront to
include cookies in access logs (default: `false`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional string that you want CloudFront to prefix
to the access log filenames for this distribution, for example, `myprefix/`.
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
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon S3 bucket to store the access logs in, for
example, `myawslogbucket.s3.amazonaws.com`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">include_<wbr>cookies</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether you want CloudFront to
include cookies in access logs (default: `false`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional string that you want CloudFront to prefix
to the access log filenames for this distribution, for example, `myprefix/`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionOrderedCacheBehavior
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionOrderedCacheBehavior">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionOrderedCacheBehavior">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOrderedCacheBehaviorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOrderedCacheBehaviorOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOrderedCacheBehaviorArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOrderedCacheBehavior.html">output</a> API doc for this type.
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
            <td class="align-top">Allowed<wbr>Methods</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Controls which HTTP methods CloudFront
processes and forwards to your Amazon S3 bucket or your custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cached<wbr>Methods</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Controls whether CloudFront caches the
response to requests using the specified HTTP methods.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compress</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you want CloudFront to automatically
compress content for web requests that include `Accept-Encoding: gzip` in
the request header (default: `false`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Ttl</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
in the absence of an `Cache-Control max-age` or `Expires` header. Defaults to
1 day.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Field<wbr>Level<wbr>Encryption<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Field level encryption configuration ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Forwarded<wbr>Values</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehaviorforwardedvalues">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior<wbr>Forwarded<wbr>Values<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The forwarded values configuration that specifies how CloudFront
handles query strings, cookies and headers (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Function<wbr>Associations</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehaviorlambdafunctionassociation">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior<wbr>Lambda<wbr>Function<wbr>Association<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A config block that triggers a lambda function with
specific actions. Defined below, maximum 4.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Ttl</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
to your origin to determine whether the object has been updated. Only
effective in the presence of `Cache-Control max-age`, `Cache-Control
s-maxage`, and `Expires` headers. Defaults to 365 days.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Ttl</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum amount of time that you want objects to
stay in CloudFront caches before CloudFront queries your origin to see
whether the object has been updated. Defaults to 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Path<wbr>Pattern</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The pattern (for example, `images/*.jpg)` that
specifies which requests you want this cache behavior to apply to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Smooth<wbr>Streaming</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether you want to distribute
media files in Microsoft Smooth Streaming format using the origin that is
associated with this cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Origin<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The value of ID for the origin that you want
CloudFront to route requests to when a request matches the path pattern
either for a cache behavior or for the default cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Trusted<wbr>Signers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS accounts, if any, that you want to
allow to create signed URLs for private content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Viewer<wbr>Protocol<wbr>Policy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Use this element to specify the
protocol that users can use to access the files in the origin specified by
TargetOriginId when a request matches the path pattern in PathPattern. One
of `allow-all`, `https-only`, or `redirect-to-https`.
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
            <td class="align-top">Allowed<wbr>Methods</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Controls which HTTP methods CloudFront
processes and forwards to your Amazon S3 bucket or your custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cached<wbr>Methods</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Controls whether CloudFront caches the
response to requests using the specified HTTP methods.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compress</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you want CloudFront to automatically
compress content for web requests that include `Accept-Encoding: gzip` in
the request header (default: `false`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Ttl</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
in the absence of an `Cache-Control max-age` or `Expires` header. Defaults to
1 day.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Field<wbr>Level<wbr>Encryption<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Field level encryption configuration ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Forwarded<wbr>Values</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehaviorforwardedvalues">cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior<wbr>Forwarded<wbr>Values</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The forwarded values configuration that specifies how CloudFront
handles query strings, cookies and headers (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Function<wbr>Associations</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehaviorlambdafunctionassociation">[]cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior<wbr>Lambda<wbr>Function<wbr>Association</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A config block that triggers a lambda function with
specific actions. Defined below, maximum 4.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Ttl</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
to your origin to determine whether the object has been updated. Only
effective in the presence of `Cache-Control max-age`, `Cache-Control
s-maxage`, and `Expires` headers. Defaults to 365 days.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Ttl</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum amount of time that you want objects to
stay in CloudFront caches before CloudFront queries your origin to see
whether the object has been updated. Defaults to 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Path<wbr>Pattern</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The pattern (for example, `images/*.jpg)` that
specifies which requests you want this cache behavior to apply to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Smooth<wbr>Streaming</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether you want to distribute
media files in Microsoft Smooth Streaming format using the origin that is
associated with this cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Origin<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The value of ID for the origin that you want
CloudFront to route requests to when a request matches the path pattern
either for a cache behavior or for the default cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Trusted<wbr>Signers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS accounts, if any, that you want to
allow to create signed URLs for private content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Viewer<wbr>Protocol<wbr>Policy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Use this element to specify the
protocol that users can use to access the files in the origin specified by
TargetOriginId when a request matches the path pattern in PathPattern. One
of `allow-all`, `https-only`, or `redirect-to-https`.
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
            <td class="align-top">allowed<wbr>Methods</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Controls which HTTP methods CloudFront
processes and forwards to your Amazon S3 bucket or your custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cached<wbr>Methods</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Controls whether CloudFront caches the
response to requests using the specified HTTP methods.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compress</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you want CloudFront to automatically
compress content for web requests that include `Accept-Encoding: gzip` in
the request header (default: `false`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Ttl</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
in the absence of an `Cache-Control max-age` or `Expires` header. Defaults to
1 day.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">field<wbr>Level<wbr>Encryption<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Field level encryption configuration ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">forwarded<wbr>Values</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehaviorforwardedvalues">cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior<wbr>Forwarded<wbr>Values</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The forwarded values configuration that specifies how CloudFront
handles query strings, cookies and headers (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Function<wbr>Associations</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehaviorlambdafunctionassociation">cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior<wbr>Lambda<wbr>Function<wbr>Association[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A config block that triggers a lambda function with
specific actions. Defined below, maximum 4.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Ttl</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
to your origin to determine whether the object has been updated. Only
effective in the presence of `Cache-Control max-age`, `Cache-Control
s-maxage`, and `Expires` headers. Defaults to 365 days.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Ttl</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum amount of time that you want objects to
stay in CloudFront caches before CloudFront queries your origin to see
whether the object has been updated. Defaults to 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">path<wbr>Pattern</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The pattern (for example, `images/*.jpg)` that
specifies which requests you want this cache behavior to apply to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">smooth<wbr>Streaming</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether you want to distribute
media files in Microsoft Smooth Streaming format using the origin that is
associated with this cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Origin<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The value of ID for the origin that you want
CloudFront to route requests to when a request matches the path pattern
either for a cache behavior or for the default cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">trusted<wbr>Signers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS accounts, if any, that you want to
allow to create signed URLs for private content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">viewer<wbr>Protocol<wbr>Policy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Use this element to specify the
protocol that users can use to access the files in the origin specified by
TargetOriginId when a request matches the path pattern in PathPattern. One
of `allow-all`, `https-only`, or `redirect-to-https`.
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
            <td class="align-top">allowed_<wbr>methods</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Controls which HTTP methods CloudFront
processes and forwards to your Amazon S3 bucket or your custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cached_<wbr>methods</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Controls whether CloudFront caches the
response to requests using the specified HTTP methods.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compress</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you want CloudFront to automatically
compress content for web requests that include `Accept-Encoding: gzip` in
the request header (default: `false`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>ttl</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
in the absence of an `Cache-Control max-age` or `Expires` header. Defaults to
1 day.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">field_<wbr>level_<wbr>encryption_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Field level encryption configuration ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">forwarded_<wbr>values</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehaviorforwardedvalues">Dict[distribution_<wbr>ordered_<wbr>cache_<wbr>behavior_<wbr>forwarded_<wbr>values]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The forwarded values configuration that specifies how CloudFront
handles query strings, cookies and headers (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>function_<wbr>associations</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehaviorlambdafunctionassociation">List[distribution_<wbr>ordered_<wbr>cache_<wbr>behavior_<wbr>lambda_<wbr>function_<wbr>association]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A config block that triggers a lambda function with
specific actions. Defined below, maximum 4.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>ttl</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of time (in seconds) that an
object is in a CloudFront cache before CloudFront forwards another request
to your origin to determine whether the object has been updated. Only
effective in the presence of `Cache-Control max-age`, `Cache-Control
s-maxage`, and `Expires` headers. Defaults to 365 days.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min_<wbr>ttl</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum amount of time that you want objects to
stay in CloudFront caches before CloudFront queries your origin to see
whether the object has been updated. Defaults to 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">path_<wbr>pattern</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The pattern (for example, `images/*.jpg)` that
specifies which requests you want this cache behavior to apply to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">smooth_<wbr>streaming</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether you want to distribute
media files in Microsoft Smooth Streaming format using the origin that is
associated with this cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>origin_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The value of ID for the origin that you want
CloudFront to route requests to when a request matches the path pattern
either for a cache behavior or for the default cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">trusted_<wbr>signers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS accounts, if any, that you want to
allow to create signed URLs for private content.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">viewer_<wbr>protocol_<wbr>policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Use this element to specify the
protocol that users can use to access the files in the origin specified by
TargetOriginId when a request matches the path pattern in PathPattern. One
of `allow-all`, `https-only`, or `redirect-to-https`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionOrderedCacheBehaviorForwardedValues
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionOrderedCacheBehaviorForwardedValues">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionOrderedCacheBehaviorForwardedValues">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOrderedCacheBehaviorForwardedValuesArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOrderedCacheBehaviorForwardedValuesOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOrderedCacheBehaviorForwardedValuesArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOrderedCacheBehaviorForwardedValues.html">output</a> API doc for this type.
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
            <td class="align-top">Cookies</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehaviorforwardedvaluescookies">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior<wbr>Forwarded<wbr>Values<wbr>Cookies<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The forwarded values cookies
that specifies how CloudFront handles cookies (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Headers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the Headers, if any, that you want
CloudFront to vary upon for this cache behavior. Specify `*` to include all
headers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Query<wbr>String</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether you want CloudFront to forward
query strings to the origin that is associated with this cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Query<wbr>String<wbr>Cache<wbr>Keys</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When specified, along with a value of
`true` for `query_string`, all query strings are forwarded, however only the
query string keys listed in this argument are cached. When omitted with a
value of `true` for `query_string`, all query string keys are cached.
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
            <td class="align-top">Cookies</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehaviorforwardedvaluescookies">cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior<wbr>Forwarded<wbr>Values<wbr>Cookies</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The forwarded values cookies
that specifies how CloudFront handles cookies (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Headers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the Headers, if any, that you want
CloudFront to vary upon for this cache behavior. Specify `*` to include all
headers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Query<wbr>String</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether you want CloudFront to forward
query strings to the origin that is associated with this cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Query<wbr>String<wbr>Cache<wbr>Keys</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When specified, along with a value of
`true` for `query_string`, all query strings are forwarded, however only the
query string keys listed in this argument are cached. When omitted with a
value of `true` for `query_string`, all query string keys are cached.
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
            <td class="align-top">cookies</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehaviorforwardedvaluescookies">cloudfront.<wbr>Distribution<wbr>Ordered<wbr>Cache<wbr>Behavior<wbr>Forwarded<wbr>Values<wbr>Cookies</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The forwarded values cookies
that specifies how CloudFront handles cookies (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">headers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the Headers, if any, that you want
CloudFront to vary upon for this cache behavior. Specify `*` to include all
headers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">query<wbr>String</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether you want CloudFront to forward
query strings to the origin that is associated with this cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">query<wbr>String<wbr>Cache<wbr>Keys</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When specified, along with a value of
`true` for `query_string`, all query strings are forwarded, however only the
query string keys listed in this argument are cached. When omitted with a
value of `true` for `query_string`, all query string keys are cached.
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
            <td class="align-top">cookies</td>
            <td class="align-top">
                
                <code><a href="#distributionorderedcachebehaviorforwardedvaluescookies">Dict[distribution_<wbr>ordered_<wbr>cache_<wbr>behavior_<wbr>forwarded_<wbr>values_<wbr>cookies]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The forwarded values cookies
that specifies how CloudFront handles cookies (maximum one).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">headers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the Headers, if any, that you want
CloudFront to vary upon for this cache behavior. Specify `*` to include all
headers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">query_<wbr>string</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether you want CloudFront to forward
query strings to the origin that is associated with this cache behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">query_<wbr>string_<wbr>cache_<wbr>keys</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When specified, along with a value of
`true` for `query_string`, all query strings are forwarded, however only the
query string keys listed in this argument are cached. When omitted with a
value of `true` for `query_string`, all query string keys are cached.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionOrderedCacheBehaviorForwardedValuesCookies
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionOrderedCacheBehaviorForwardedValuesCookies">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionOrderedCacheBehaviorForwardedValuesCookies">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOrderedCacheBehaviorForwardedValuesCookiesArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOrderedCacheBehaviorForwardedValuesCookiesOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOrderedCacheBehaviorForwardedValuesCookiesArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOrderedCacheBehaviorForwardedValuesCookies.html">output</a> API doc for this type.
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
            <td class="align-top">Forward</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether you want CloudFront to forward
cookies to the origin that is associated with this cache behavior. You can
specify `all`, `none` or `whitelist`. If `whitelist`, you must include the
subsequent `whitelisted_names`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Whitelisted<wbr>Names</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you have specified `whitelist` to
`forward`, the whitelisted cookies that you want CloudFront to forward to
your origin.
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
            <td class="align-top">Forward</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether you want CloudFront to forward
cookies to the origin that is associated with this cache behavior. You can
specify `all`, `none` or `whitelist`. If `whitelist`, you must include the
subsequent `whitelisted_names`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Whitelisted<wbr>Names</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you have specified `whitelist` to
`forward`, the whitelisted cookies that you want CloudFront to forward to
your origin.
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
            <td class="align-top">forward</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether you want CloudFront to forward
cookies to the origin that is associated with this cache behavior. You can
specify `all`, `none` or `whitelist`. If `whitelist`, you must include the
subsequent `whitelisted_names`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">whitelisted<wbr>Names</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you have specified `whitelist` to
`forward`, the whitelisted cookies that you want CloudFront to forward to
your origin.
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
            <td class="align-top">forward</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether you want CloudFront to forward
cookies to the origin that is associated with this cache behavior. You can
specify `all`, `none` or `whitelist`. If `whitelist`, you must include the
subsequent `whitelisted_names`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">whitelisted_<wbr>names</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you have specified `whitelist` to
`forward`, the whitelisted cookies that you want CloudFront to forward to
your origin.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionOrderedCacheBehaviorLambdaFunctionAssociation
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionOrderedCacheBehaviorLambdaFunctionAssociation">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionOrderedCacheBehaviorLambdaFunctionAssociation">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOrderedCacheBehaviorLambdaFunctionAssociationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOrderedCacheBehaviorLambdaFunctionAssociationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOrderedCacheBehaviorLambdaFunctionAssociationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOrderedCacheBehaviorLambdaFunctionAssociation.html">output</a> API doc for this type.
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
            <td class="align-top">Event<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The specific event to trigger this function.
Valid values: `viewer-request`, `origin-request`, `viewer-response`,
`origin-response`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Include<wbr>Body</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to true it exposes the request body to the lambda function. Defaults to false. Valid values: `true`, `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the Lambda function.
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
            <td class="align-top">Event<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The specific event to trigger this function.
Valid values: `viewer-request`, `origin-request`, `viewer-response`,
`origin-response`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Include<wbr>Body</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to true it exposes the request body to the lambda function. Defaults to false. Valid values: `true`, `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the Lambda function.
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
            <td class="align-top">event<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The specific event to trigger this function.
Valid values: `viewer-request`, `origin-request`, `viewer-response`,
`origin-response`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">include<wbr>Body</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to true it exposes the request body to the lambda function. Defaults to false. Valid values: `true`, `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the Lambda function.
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
            <td class="align-top">event_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The specific event to trigger this function.
Valid values: `viewer-request`, `origin-request`, `viewer-response`,
`origin-response`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">include_<wbr>body</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to true it exposes the request body to the lambda function. Defaults to false. Valid values: `true`, `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionOrigin
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionOrigin">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionOrigin">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOriginArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOriginOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOriginArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOrigin.html">output</a> API doc for this type.
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
            <td class="align-top">Custom<wbr>Headers</td>
            <td class="align-top">
                
                <code><a href="#distributionorigincustomheader">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Origin<wbr>Custom<wbr>Header<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more sub-resources with `name` and
`value` parameters that specify header data that will be sent to the origin
(multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Origin<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#distributionorigincustomoriginconfig">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Origin<wbr>Custom<wbr>Origin<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudFront custom
origin configuration information. If an S3
origin is required, use `s3_origin_config` instead.
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
The DNS domain name of either the S3 bucket, or
web site of your custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The unique identifier of the member origin
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional element that causes CloudFront to
request your content from a directory in your Amazon S3 bucket or your
custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Origin<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#distributionorigins3originconfig">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Origin<wbr>S3Origin<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudFront S3 origin
configuration information. If a custom origin is required, use
`custom_origin_config` instead.
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
            <td class="align-top">Custom<wbr>Headers</td>
            <td class="align-top">
                
                <code><a href="#distributionorigincustomheader">[]cloudfront.<wbr>Distribution<wbr>Origin<wbr>Custom<wbr>Header</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more sub-resources with `name` and
`value` parameters that specify header data that will be sent to the origin
(multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Origin<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#distributionorigincustomoriginconfig">*cloudfront.<wbr>Distribution<wbr>Origin<wbr>Custom<wbr>Origin<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudFront custom
origin configuration information. If an S3
origin is required, use `s3_origin_config` instead.
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
The DNS domain name of either the S3 bucket, or
web site of your custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The unique identifier of the member origin
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Path</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional element that causes CloudFront to
request your content from a directory in your Amazon S3 bucket or your
custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Origin<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#distributionorigins3originconfig">*cloudfront.<wbr>Distribution<wbr>Origin<wbr>S3Origin<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudFront S3 origin
configuration information. If a custom origin is required, use
`custom_origin_config` instead.
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
            <td class="align-top">custom<wbr>Headers</td>
            <td class="align-top">
                
                <code><a href="#distributionorigincustomheader">cloudfront.<wbr>Distribution<wbr>Origin<wbr>Custom<wbr>Header[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more sub-resources with `name` and
`value` parameters that specify header data that will be sent to the origin
(multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Origin<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#distributionorigincustomoriginconfig">cloudfront.<wbr>Distribution<wbr>Origin<wbr>Custom<wbr>Origin<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudFront custom
origin configuration information. If an S3
origin is required, use `s3_origin_config` instead.
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
The DNS domain name of either the S3 bucket, or
web site of your custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The unique identifier of the member origin
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin<wbr>Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional element that causes CloudFront to
request your content from a directory in your Amazon S3 bucket or your
custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Origin<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#distributionorigins3originconfig">cloudfront.<wbr>Distribution<wbr>Origin<wbr>S3Origin<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudFront S3 origin
configuration information. If a custom origin is required, use
`custom_origin_config` instead.
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
            <td class="align-top">custom_<wbr>headers</td>
            <td class="align-top">
                
                <code><a href="#distributionorigincustomheader">List[distribution_<wbr>origin_<wbr>custom_<wbr>header]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more sub-resources with `name` and
`value` parameters that specify header data that will be sent to the origin
(multiples allowed).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>origin_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#distributionorigincustomoriginconfig">Dict[distribution_<wbr>origin_<wbr>custom_<wbr>origin_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudFront custom
origin configuration information. If an S3
origin is required, use `s3_origin_config` instead.
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
The DNS domain name of either the S3 bucket, or
web site of your custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The unique identifier of the member origin
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin_<wbr>path</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional element that causes CloudFront to
request your content from a directory in your Amazon S3 bucket or your
custom origin.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>origin_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#distributionorigins3originconfig">Dict[distribution_<wbr>origin_<wbr>s3_<wbr>origin_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudFront S3 origin
configuration information. If a custom origin is required, use
`custom_origin_config` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionOriginCustomHeader
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionOriginCustomHeader">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionOriginCustomHeader">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOriginCustomHeaderArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOriginCustomHeaderOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOriginCustomHeaderArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOriginCustomHeader.html">output</a> API doc for this type.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionOriginCustomOriginConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionOriginCustomOriginConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionOriginCustomOriginConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOriginCustomOriginConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOriginCustomOriginConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOriginCustomOriginConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOriginCustomOriginConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Http<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP port the custom origin listens on.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Https<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTPS port the custom origin listens on.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Keepalive<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Custom KeepAlive timeout, in seconds. By default, AWS enforces a limit of `60`. But you can request an [increase](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-request-timeout).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Protocol<wbr>Policy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The origin protocol policy to apply to
your origin. One of `http-only`, `https-only`, or `match-viewer`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Read<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Custom Read timeout, in seconds. By default, AWS enforces a limit of `60`. But you can request an [increase](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-request-timeout).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Ssl<wbr>Protocols</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The SSL/TLS protocols that you want
CloudFront to use when communicating with your origin over HTTPS. A list of
one or more of `SSLv3`, `TLSv1`, `TLSv1.1`, and `TLSv1.2`.
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
            <td class="align-top">Http<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP port the custom origin listens on.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Https<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTPS port the custom origin listens on.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Keepalive<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Custom KeepAlive timeout, in seconds. By default, AWS enforces a limit of `60`. But you can request an [increase](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-request-timeout).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Protocol<wbr>Policy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The origin protocol policy to apply to
your origin. One of `http-only`, `https-only`, or `match-viewer`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Read<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Custom Read timeout, in seconds. By default, AWS enforces a limit of `60`. But you can request an [increase](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-request-timeout).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Ssl<wbr>Protocols</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The SSL/TLS protocols that you want
CloudFront to use when communicating with your origin over HTTPS. A list of
one or more of `SSLv3`, `TLSv1`, `TLSv1.1`, and `TLSv1.2`.
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
            <td class="align-top">http<wbr>Port</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP port the custom origin listens on.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">https<wbr>Port</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTPS port the custom origin listens on.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin<wbr>Keepalive<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Custom KeepAlive timeout, in seconds. By default, AWS enforces a limit of `60`. But you can request an [increase](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-request-timeout).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin<wbr>Protocol<wbr>Policy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The origin protocol policy to apply to
your origin. One of `http-only`, `https-only`, or `match-viewer`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin<wbr>Read<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Custom Read timeout, in seconds. By default, AWS enforces a limit of `60`. But you can request an [increase](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-request-timeout).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin<wbr>Ssl<wbr>Protocols</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The SSL/TLS protocols that you want
CloudFront to use when communicating with your origin over HTTPS. A list of
one or more of `SSLv3`, `TLSv1`, `TLSv1.1`, and `TLSv1.2`.
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
            <td class="align-top">http_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP port the custom origin listens on.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">https_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTPS port the custom origin listens on.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin_<wbr>keepalive_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Custom KeepAlive timeout, in seconds. By default, AWS enforces a limit of `60`. But you can request an [increase](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-request-timeout).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin_<wbr>protocol_<wbr>policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The origin protocol policy to apply to
your origin. One of `http-only`, `https-only`, or `match-viewer`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin_<wbr>read_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Custom Read timeout, in seconds. By default, AWS enforces a limit of `60`. But you can request an [increase](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-request-timeout).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin_<wbr>ssl_<wbr>protocols</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The SSL/TLS protocols that you want
CloudFront to use when communicating with your origin over HTTPS. A list of
one or more of `SSLv3`, `TLSv1`, `TLSv1.1`, and `TLSv1.2`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionOriginGroup
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionOriginGroup">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionOriginGroup">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOriginGroupArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOriginGroupOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOriginGroupArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOriginGroup.html">output</a> API doc for this type.
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
            <td class="align-top">Failover<wbr>Criteria</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroupfailovercriteria">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Origin<wbr>Group<wbr>Failover<wbr>Criteria<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The failover criteria for when to failover to the secondary origin
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Members</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroupmember">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Origin<wbr>Group<wbr>Member<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Ordered member configuration blocks assigned to the origin group, where the first member is the primary origin. You must specify two members.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The unique identifier of the member origin
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
            <td class="align-top">Failover<wbr>Criteria</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroupfailovercriteria">cloudfront.<wbr>Distribution<wbr>Origin<wbr>Group<wbr>Failover<wbr>Criteria</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The failover criteria for when to failover to the secondary origin
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Members</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroupmember">[]cloudfront.<wbr>Distribution<wbr>Origin<wbr>Group<wbr>Member</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Ordered member configuration blocks assigned to the origin group, where the first member is the primary origin. You must specify two members.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Origin<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The unique identifier of the member origin
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
            <td class="align-top">failover<wbr>Criteria</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroupfailovercriteria">cloudfront.<wbr>Distribution<wbr>Origin<wbr>Group<wbr>Failover<wbr>Criteria</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The failover criteria for when to failover to the secondary origin
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">members</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroupmember">cloudfront.<wbr>Distribution<wbr>Origin<wbr>Group<wbr>Member[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Ordered member configuration blocks assigned to the origin group, where the first member is the primary origin. You must specify two members.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The unique identifier of the member origin
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
            <td class="align-top">failover_<wbr>criteria</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroupfailovercriteria">Dict[distribution_<wbr>origin_<wbr>group_<wbr>failover_<wbr>criteria]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The failover criteria for when to failover to the secondary origin
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">members</td>
            <td class="align-top">
                
                <code><a href="#distributionorigingroupmember">List[distribution_<wbr>origin_<wbr>group_<wbr>member]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Ordered member configuration blocks assigned to the origin group, where the first member is the primary origin. You must specify two members.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">origin_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The unique identifier of the member origin
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionOriginGroupFailoverCriteria
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionOriginGroupFailoverCriteria">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionOriginGroupFailoverCriteria">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOriginGroupFailoverCriteriaArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOriginGroupFailoverCriteriaOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOriginGroupFailoverCriteriaArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOriginGroupFailoverCriteria.html">output</a> API doc for this type.
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
            <td class="align-top">Status<wbr>Codes</td>
            <td class="align-top">
                
                <code>List&lt;int&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of HTTP status codes for the origin group
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
            <td class="align-top">Status<wbr>Codes</td>
            <td class="align-top">
                
                <code>[]int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of HTTP status codes for the origin group
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
            <td class="align-top">status<wbr>Codes</td>
            <td class="align-top">
                
                <code>number[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of HTTP status codes for the origin group
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
            <td class="align-top">status_<wbr>codes</td>
            <td class="align-top">
                
                <code>List[integer]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of HTTP status codes for the origin group
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionOriginGroupMember
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionOriginGroupMember">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionOriginGroupMember">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOriginGroupMemberArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOriginGroupMemberOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOriginGroupMemberArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOriginGroupMember.html">output</a> API doc for this type.
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
            <td class="align-top">Origin<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The unique identifier of the member origin
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
            <td class="align-top">Origin<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The unique identifier of the member origin
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
            <td class="align-top">origin<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The unique identifier of the member origin
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
            <td class="align-top">origin_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The unique identifier of the member origin
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionOriginS3OriginConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionOriginS3OriginConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionOriginS3OriginConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOriginS3OriginConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionOriginS3OriginConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOriginS3OriginConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionOriginS3OriginConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Origin<wbr>Access<wbr>Identity</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The [CloudFront origin access
identity][5] to associate with the origin.
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
            <td class="align-top">Origin<wbr>Access<wbr>Identity</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The [CloudFront origin access
identity][5] to associate with the origin.
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
            <td class="align-top">origin<wbr>Access<wbr>Identity</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The [CloudFront origin access
identity][5] to associate with the origin.
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
            <td class="align-top">origin_<wbr>access_<wbr>identity</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The [CloudFront origin access
identity][5] to associate with the origin.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionRestrictions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionRestrictions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionRestrictions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionRestrictionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionRestrictionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionRestrictionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionRestrictions.html">output</a> API doc for this type.
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
            <td class="align-top">Geo<wbr>Restriction</td>
            <td class="align-top">
                
                <code><a href="#distributionrestrictionsgeorestriction">Pulumi.<wbr>Aws.<wbr>Cloudfront.<wbr>Distribution<wbr>Restrictions<wbr>Geo<wbr>Restriction<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">Geo<wbr>Restriction</td>
            <td class="align-top">
                
                <code><a href="#distributionrestrictionsgeorestriction">cloudfront.<wbr>Distribution<wbr>Restrictions<wbr>Geo<wbr>Restriction</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">geo<wbr>Restriction</td>
            <td class="align-top">
                
                <code><a href="#distributionrestrictionsgeorestriction">cloudfront.<wbr>Distribution<wbr>Restrictions<wbr>Geo<wbr>Restriction</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">geo_<wbr>restriction</td>
            <td class="align-top">
                
                <code><a href="#distributionrestrictionsgeorestriction">Dict[distribution_<wbr>restrictions_<wbr>geo_<wbr>restriction]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionRestrictionsGeoRestriction
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionRestrictionsGeoRestriction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionRestrictionsGeoRestriction">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionRestrictionsGeoRestrictionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionRestrictionsGeoRestrictionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionRestrictionsGeoRestrictionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionRestrictionsGeoRestriction.html">output</a> API doc for this type.
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
            <td class="align-top">Locations</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [ISO 3166-1-alpha-2 codes][4] for which you
want CloudFront either to distribute your content (`whitelist`) or not
distribute your content (`blacklist`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Restriction<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The method that you want to use to restrict
distribution of your content by country: `none`, `whitelist`, or
`blacklist`.
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
            <td class="align-top">Locations</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [ISO 3166-1-alpha-2 codes][4] for which you
want CloudFront either to distribute your content (`whitelist`) or not
distribute your content (`blacklist`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Restriction<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The method that you want to use to restrict
distribution of your content by country: `none`, `whitelist`, or
`blacklist`.
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
            <td class="align-top">locations</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [ISO 3166-1-alpha-2 codes][4] for which you
want CloudFront either to distribute your content (`whitelist`) or not
distribute your content (`blacklist`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">restriction<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The method that you want to use to restrict
distribution of your content by country: `none`, `whitelist`, or
`blacklist`.
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
            <td class="align-top">locations</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [ISO 3166-1-alpha-2 codes][4] for which you
want CloudFront either to distribute your content (`whitelist`) or not
distribute your content (`blacklist`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">restriction_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The method that you want to use to restrict
distribution of your content by country: `none`, `whitelist`, or
`blacklist`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DistributionViewerCertificate
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DistributionViewerCertificate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DistributionViewerCertificate">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionViewerCertificateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudfront?tab=doc#DistributionViewerCertificateOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionViewerCertificateArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudfront.DistributionViewerCertificate.html">output</a> API doc for this type.
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
            <td class="align-top">Acm<wbr>Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the [AWS Certificate Manager][6]
certificate that you wish to use with this distribution. Specify this,
`cloudfront_default_certificate`, or `iam_certificate_id`.  The ACM
certificate must be in  US-EAST-1.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudfront<wbr>Default<wbr>Certificate</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
`true` if you want viewers to use HTTPS
to request your objects and you&#39;re using the CloudFront domain name for your
distribution. Specify this, `acm_certificate_arn`, or `iam_certificate_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Certificate<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM certificate identifier of the custom viewer
certificate for this distribution if you are using a custom domain. Specify
this, `acm_certificate_arn`, or `cloudfront_default_certificate`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Minimum<wbr>Protocol<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum version of the SSL protocol that
you want CloudFront to use for HTTPS connections. Can only be set if
`cloudfront_default_certificate = false`. One of `SSLv3`, `TLSv1`,
`TLSv1_2016`, `TLSv1.1_2016` or `TLSv1.2_2018`. Default: `TLSv1`. **NOTE**:
If you are using a custom certificate (specified with `acm_certificate_arn`
or `iam_certificate_id`), and have specified `sni-only` in
`ssl_support_method`, `TLSv1` or later must be specified. If you have
specified `vip` in `ssl_support_method`, only `SSLv3` or `TLSv1` can be
specified. If you have specified `cloudfront_default_certificate`, `TLSv1`
must be specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ssl<wbr>Support<wbr>Method</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">Acm<wbr>Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the [AWS Certificate Manager][6]
certificate that you wish to use with this distribution. Specify this,
`cloudfront_default_certificate`, or `iam_certificate_id`.  The ACM
certificate must be in  US-EAST-1.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudfront<wbr>Default<wbr>Certificate</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
`true` if you want viewers to use HTTPS
to request your objects and you&#39;re using the CloudFront domain name for your
distribution. Specify this, `acm_certificate_arn`, or `iam_certificate_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Certificate<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM certificate identifier of the custom viewer
certificate for this distribution if you are using a custom domain. Specify
this, `acm_certificate_arn`, or `cloudfront_default_certificate`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Minimum<wbr>Protocol<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum version of the SSL protocol that
you want CloudFront to use for HTTPS connections. Can only be set if
`cloudfront_default_certificate = false`. One of `SSLv3`, `TLSv1`,
`TLSv1_2016`, `TLSv1.1_2016` or `TLSv1.2_2018`. Default: `TLSv1`. **NOTE**:
If you are using a custom certificate (specified with `acm_certificate_arn`
or `iam_certificate_id`), and have specified `sni-only` in
`ssl_support_method`, `TLSv1` or later must be specified. If you have
specified `vip` in `ssl_support_method`, only `SSLv3` or `TLSv1` can be
specified. If you have specified `cloudfront_default_certificate`, `TLSv1`
must be specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ssl<wbr>Support<wbr>Method</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">acm<wbr>Certificate<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the [AWS Certificate Manager][6]
certificate that you wish to use with this distribution. Specify this,
`cloudfront_default_certificate`, or `iam_certificate_id`.  The ACM
certificate must be in  US-EAST-1.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudfront<wbr>Default<wbr>Certificate</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
`true` if you want viewers to use HTTPS
to request your objects and you&#39;re using the CloudFront domain name for your
distribution. Specify this, `acm_certificate_arn`, or `iam_certificate_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Certificate<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM certificate identifier of the custom viewer
certificate for this distribution if you are using a custom domain. Specify
this, `acm_certificate_arn`, or `cloudfront_default_certificate`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">minimum<wbr>Protocol<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum version of the SSL protocol that
you want CloudFront to use for HTTPS connections. Can only be set if
`cloudfront_default_certificate = false`. One of `SSLv3`, `TLSv1`,
`TLSv1_2016`, `TLSv1.1_2016` or `TLSv1.2_2018`. Default: `TLSv1`. **NOTE**:
If you are using a custom certificate (specified with `acm_certificate_arn`
or `iam_certificate_id`), and have specified `sni-only` in
`ssl_support_method`, `TLSv1` or later must be specified. If you have
specified `vip` in `ssl_support_method`, only `SSLv3` or `TLSv1` can be
specified. If you have specified `cloudfront_default_certificate`, `TLSv1`
must be specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ssl<wbr>Support<wbr>Method</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">acm_<wbr>certificate_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the [AWS Certificate Manager][6]
certificate that you wish to use with this distribution. Specify this,
`cloudfront_default_certificate`, or `iam_certificate_id`.  The ACM
certificate must be in  US-EAST-1.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudfront_<wbr>default_<wbr>certificate</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
`true` if you want viewers to use HTTPS
to request your objects and you&#39;re using the CloudFront domain name for your
distribution. Specify this, `acm_certificate_arn`, or `iam_certificate_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>certificate_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM certificate identifier of the custom viewer
certificate for this distribution if you are using a custom domain. Specify
this, `acm_certificate_arn`, or `cloudfront_default_certificate`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">minimum_<wbr>protocol_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum version of the SSL protocol that
you want CloudFront to use for HTTPS connections. Can only be set if
`cloudfront_default_certificate = false`. One of `SSLv3`, `TLSv1`,
`TLSv1_2016`, `TLSv1.1_2016` or `TLSv1.2_2018`. Default: `TLSv1`. **NOTE**:
If you are using a custom certificate (specified with `acm_certificate_arn`
or `iam_certificate_id`), and have specified `sni-only` in
`ssl_support_method`, `TLSv1` or later must be specified. If you have
specified `vip` in `ssl_support_method`, only `SSLv3` or `TLSv1` can be
specified. If you have specified `cloudfront_default_certificate`, `TLSv1`
must be specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ssl_<wbr>support_<wbr>method</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







