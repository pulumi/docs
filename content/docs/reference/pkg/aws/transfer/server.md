
---
title: "Server"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides a AWS Transfer Server resource.


```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const fooRole = new aws.iam.Role("foo", {
    assumeRolePolicy: `{
	"Version": "2012-10-17",
	"Statement": [
		{
		"Effect": "Allow",
		"Principal": {
			"Service": "transfer.amazonaws.com"
		},
		"Action": "sts:AssumeRole"
		}
	]
}
`,
});
const fooRolePolicy = new aws.iam.RolePolicy("foo", {
    policy: `{
	"Version": "2012-10-17",
	"Statement": [
		{
		"Sid": "AllowFullAccesstoCloudWatchLogs",
		"Effect": "Allow",
		"Action": [
			"logs:*"
		],
		"Resource": "*"
		}
	]
}
`,
    role: fooRole.id,
});
const fooServer = new aws.transfer.Server("foo", {
    identityProviderType: "SERVICE_MANAGED",
    loggingRole: fooRole.arn,
    tags: {
        ENV: "test",
        NAME: "tf-acc-test-transfer-server",
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/transfer_server.html.markdown.



## Create a Server Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/transfer/#Server">Server</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/transfer/#ServerArgs">ServerArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Server</span><span class="p">(resource_name, opts=None, </span>endpoint_details=None<span class="p">, </span>endpoint_type=None<span class="p">, </span>force_destroy=None<span class="p">, </span>host_key=None<span class="p">, </span>identity_provider_type=None<span class="p">, </span>invocation_role=None<span class="p">, </span>logging_role=None<span class="p">, </span>tags=None<span class="p">, </span>url=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewServer<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/transfer?tab=doc#ServerArgs">ServerArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/transfer?tab=doc#Server">Server</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Transfer.Server.html">Server</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Transfer.ServerArgs.html">ServerArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Server resource with the given unique name, arguments, and options.

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
            <td class="align-top">Endpoint<wbr>Details</td>
            <td class="align-top">
                
                <code><a href="#serverendpointdetails">Pulumi.<wbr>Aws.<wbr>Transfer.<wbr>Server<wbr>Endpoint<wbr>Details<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn&#39;t accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
RSA private key (e.g. as generated by the `ssh-keygen -N &#34;&#34; -f my-new-server-key` command).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Provider<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Invocation<wbr>Role</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Role</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
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
            <td class="align-top">Url</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
- URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.
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
            <td class="align-top">Endpoint<wbr>Details</td>
            <td class="align-top">
                
                <code><a href="#serverendpointdetails">*transfer.<wbr>Server<wbr>Endpoint<wbr>Details</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn&#39;t accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
RSA private key (e.g. as generated by the `ssh-keygen -N &#34;&#34; -f my-new-server-key` command).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Provider<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Invocation<wbr>Role</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Role</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
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
            <td class="align-top">Url</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
- URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.
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
            <td class="align-top">endpoint<wbr>Details</td>
            <td class="align-top">
                
                <code><a href="#serverendpointdetails">transfer.<wbr>Server<wbr>Endpoint<wbr>Details?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn&#39;t accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
RSA private key (e.g. as generated by the `ssh-keygen -N &#34;&#34; -f my-new-server-key` command).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity<wbr>Provider<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">invocation<wbr>Role</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging<wbr>Role</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
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
            <td class="align-top">url</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
- URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.
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
            <td class="align-top">endpoint_<wbr>details</td>
            <td class="align-top">
                
                <code><a href="#serverendpointdetails">Dict[Server<wbr>Endpoint<wbr>Details]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn&#39;t accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force_<wbr>destroy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
RSA private key (e.g. as generated by the `ssh-keygen -N &#34;&#34; -f my-new-server-key` command).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity_<wbr>provider_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">invocation_<wbr>role</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging_<wbr>role</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">url</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
- URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Server Output Properties

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
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of Transfer Server
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Details</td>
            <td class="align-top">
                
                <code><a href="#serverendpointdetails">Pulumi.<wbr>Aws.<wbr>Transfer.<wbr>Server<wbr>Endpoint<wbr>Details?</a></code>
            </td>
            <td class="align-top">{{% md %}} The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn&#39;t accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} RSA private key (e.g. as generated by the `ssh-keygen -N &#34;&#34; -f my-new-server-key` command).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Key<wbr>Fingerprint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} This value contains the message-digest algorithm (MD5) hash of the server&#39;s host key. This value is equivalent to the output of the `ssh-keygen -l -E md5 -f my-new-server-key` command.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Provider<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Invocation<wbr>Role</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Role</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
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
            <td class="align-top">Url</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} - URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.
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
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of Transfer Server
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Details</td>
            <td class="align-top">
                
                <code><a href="#serverendpointdetails">*transfer.<wbr>Server<wbr>Endpoint<wbr>Details</a></code>
            </td>
            <td class="align-top">{{% md %}} The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn&#39;t accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} RSA private key (e.g. as generated by the `ssh-keygen -N &#34;&#34; -f my-new-server-key` command).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Key<wbr>Fingerprint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} This value contains the message-digest algorithm (MD5) hash of the server&#39;s host key. This value is equivalent to the output of the `ssh-keygen -l -E md5 -f my-new-server-key` command.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Provider<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Invocation<wbr>Role</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Role</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
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
            <td class="align-top">Url</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} - URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.
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
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of Transfer Server
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint<wbr>Details</td>
            <td class="align-top">
                
                <code><a href="#serverendpointdetails">transfer.<wbr>Server<wbr>Endpoint<wbr>Details?</a></code>
            </td>
            <td class="align-top">{{% md %}} The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn&#39;t accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} RSA private key (e.g. as generated by the `ssh-keygen -N &#34;&#34; -f my-new-server-key` command).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host<wbr>Key<wbr>Fingerprint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} This value contains the message-digest algorithm (MD5) hash of the server&#39;s host key. This value is equivalent to the output of the `ssh-keygen -l -E md5 -f my-new-server-key` command.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity<wbr>Provider<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">invocation<wbr>Role</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging<wbr>Role</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
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
            <td class="align-top">url</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} - URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.
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
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of Transfer Server
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint_<wbr>details</td>
            <td class="align-top">
                
                <code><a href="#serverendpointdetails">Dict[Server<wbr>Endpoint<wbr>Details]</a></code>
            </td>
            <td class="align-top">{{% md %}} The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn&#39;t accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force_<wbr>destroy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} RSA private key (e.g. as generated by the `ssh-keygen -N &#34;&#34; -f my-new-server-key` command).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host_<wbr>key_<wbr>fingerprint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} This value contains the message-digest algorithm (MD5) hash of the server&#39;s host key. This value is equivalent to the output of the `ssh-keygen -l -E md5 -f my-new-server-key` command.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity_<wbr>provider_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">invocation_<wbr>role</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging_<wbr>role</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">url</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} - URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Server Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/transfer/#ServerState">ServerState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/transfer/#Server">Server</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>endpoint=None<span class="p">, </span>endpoint_details=None<span class="p">, </span>endpoint_type=None<span class="p">, </span>force_destroy=None<span class="p">, </span>host_key=None<span class="p">, </span>host_key_fingerprint=None<span class="p">, </span>identity_provider_type=None<span class="p">, </span>invocation_role=None<span class="p">, </span>logging_role=None<span class="p">, </span>tags=None<span class="p">, </span>url=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetServer<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/transfer?tab=doc#ServerState">ServerState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/transfer?tab=doc#Server">Server</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Transfer.Server.html">Server</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Transfer.ServerState.html">ServerState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Server resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
Amazon Resource Name (ARN) of Transfer Server
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Details</td>
            <td class="align-top">
                
                <code><a href="#serverendpointdetails">Pulumi.<wbr>Aws.<wbr>Transfer.<wbr>Server<wbr>Endpoint<wbr>Details<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn&#39;t accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
RSA private key (e.g. as generated by the `ssh-keygen -N &#34;&#34; -f my-new-server-key` command).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Key<wbr>Fingerprint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This value contains the message-digest algorithm (MD5) hash of the server&#39;s host key. This value is equivalent to the output of the `ssh-keygen -l -E md5 -f my-new-server-key` command.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Provider<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Invocation<wbr>Role</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Role</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
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
            <td class="align-top">Url</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
- URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.
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
Amazon Resource Name (ARN) of Transfer Server
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Details</td>
            <td class="align-top">
                
                <code><a href="#serverendpointdetails">*transfer.<wbr>Server<wbr>Endpoint<wbr>Details</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn&#39;t accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
RSA private key (e.g. as generated by the `ssh-keygen -N &#34;&#34; -f my-new-server-key` command).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Key<wbr>Fingerprint</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This value contains the message-digest algorithm (MD5) hash of the server&#39;s host key. This value is equivalent to the output of the `ssh-keygen -l -E md5 -f my-new-server-key` command.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Provider<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Invocation<wbr>Role</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Role</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
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
            <td class="align-top">Url</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
- URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.
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
Amazon Resource Name (ARN) of Transfer Server
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint<wbr>Details</td>
            <td class="align-top">
                
                <code><a href="#serverendpointdetails">transfer.<wbr>Server<wbr>Endpoint<wbr>Details?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn&#39;t accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force<wbr>Destroy</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
RSA private key (e.g. as generated by the `ssh-keygen -N &#34;&#34; -f my-new-server-key` command).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host<wbr>Key<wbr>Fingerprint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This value contains the message-digest algorithm (MD5) hash of the server&#39;s host key. This value is equivalent to the output of the `ssh-keygen -l -E md5 -f my-new-server-key` command.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity<wbr>Provider<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">invocation<wbr>Role</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging<wbr>Role</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
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
            <td class="align-top">url</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
- URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.
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
Amazon Resource Name (ARN) of Transfer Server
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint_<wbr>details</td>
            <td class="align-top">
                
                <code><a href="#serverendpointdetails">Dict[Server<wbr>Endpoint<wbr>Details]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn&#39;t accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force_<wbr>destroy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
RSA private key (e.g. as generated by the `ssh-keygen -N &#34;&#34; -f my-new-server-key` command).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host_<wbr>key_<wbr>fingerprint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This value contains the message-digest algorithm (MD5) hash of the server&#39;s host key. This value is equivalent to the output of the `ssh-keygen -l -E md5 -f my-new-server-key` command.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity_<wbr>provider_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">invocation_<wbr>role</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging_<wbr>role</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">url</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
- URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### ServerEndpointDetails
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ServerEndpointDetails">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ServerEndpointDetails">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/transfer?tab=doc#ServerEndpointDetailsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/transfer?tab=doc#ServerEndpointDetailsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Transfer.ServerEndpointDetailsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Transfer.ServerEndpointDetails.html">output</a> API doc for this type.
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
            <td class="align-top">Vpc<wbr>Endpoint<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the VPC endpoint.
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
            <td class="align-top">Vpc<wbr>Endpoint<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the VPC endpoint.
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
            <td class="align-top">vpc<wbr>Endpoint<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the VPC endpoint.
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
            <td class="align-top">vpc_<wbr>endpoint_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the VPC endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







