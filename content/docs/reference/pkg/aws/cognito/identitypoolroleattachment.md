
---
title: "IdentityPoolRoleAttachment"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides an AWS Cognito Identity Pool Roles Attachment.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const mainIdentityPool = new aws.cognito.IdentityPool("main", {
    allowUnauthenticatedIdentities: false,
    identityPoolName: "identity pool",
    supportedLoginProviders: {
        "graph.facebook.com": "7346241598935555",
    },
});
const authenticatedRole = new aws.iam.Role("authenticated", {
    assumeRolePolicy: pulumi.interpolate`{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "cognito-identity.amazonaws.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "cognito-identity.amazonaws.com:aud": "${mainIdentityPool.id}"
        },
        "ForAnyValue:StringLike": {
          "cognito-identity.amazonaws.com:amr": "authenticated"
        }
      }
    }
  ]
}
`,
});
const mainIdentityPoolRoleAttachment = new aws.cognito.IdentityPoolRoleAttachment("main", {
    identityPoolId: mainIdentityPool.id,
    roleMappings: [{
        ambiguousRoleResolution: "AuthenticatedRole",
        identityProvider: "graph.facebook.com",
        mappingRules: [{
            claim: "isAdmin",
            matchType: "Equals",
            roleArn: authenticatedRole.arn,
            value: "paid",
        }],
        type: "Rules",
    }],
    roles: {
        authenticated: authenticatedRole.arn,
    },
});
const authenticatedRolePolicy = new aws.iam.RolePolicy("authenticated", {
    policy: `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "mobileanalytics:PutEvents",
        "cognito-sync:*",
        "cognito-identity:*"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}
`,
    role: authenticatedRole.id,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_pool_roles_attachment.markdown.



## Create a IdentityPoolRoleAttachment Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cognito/#IdentityPoolRoleAttachment">IdentityPoolRoleAttachment</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cognito/#IdentityPoolRoleAttachmentArgs">IdentityPoolRoleAttachmentArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">IdentityPoolRoleAttachment</span><span class="p">(resource_name, opts=None, </span>identity_pool_id=None<span class="p">, </span>role_mappings=None<span class="p">, </span>roles=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewIdentityPoolRoleAttachment<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPoolRoleAttachmentArgs">IdentityPoolRoleAttachmentArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPoolRoleAttachment">IdentityPoolRoleAttachment</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPoolRoleAttachment.html">IdentityPoolRoleAttachment</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPoolRoleAttachmentArgs.html">IdentityPoolRoleAttachmentArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a IdentityPoolRoleAttachment resource with the given unique name, arguments, and options.

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
            <td class="align-top">Identity<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An identity pool ID in the format REGION:GUID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentrolemapping">List&lt;Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Role<wbr>Mapping<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A List of Role Mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Roles</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentroles">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Roles<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The map of roles associated with this pool. For a given role, the key will be either &#34;authenticated&#34; or &#34;unauthenticated&#34; and the value will be the Role ARN.
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
            <td class="align-top">Identity<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An identity pool ID in the format REGION:GUID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentrolemapping">[]cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Role<wbr>Mapping</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A List of Role Mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Roles</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentroles">cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Roles</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The map of roles associated with this pool. For a given role, the key will be either &#34;authenticated&#34; or &#34;unauthenticated&#34; and the value will be the Role ARN.
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
            <td class="align-top">identity<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An identity pool ID in the format REGION:GUID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentrolemapping">cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Role<wbr>Mapping[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A List of Role Mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">roles</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentroles">cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Roles</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The map of roles associated with this pool. For a given role, the key will be either &#34;authenticated&#34; or &#34;unauthenticated&#34; and the value will be the Role ARN.
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
            <td class="align-top">identity_<wbr>pool_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An identity pool ID in the format REGION:GUID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>mappings</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentrolemapping">list[identity_<wbr>pool_<wbr>role_<wbr>attachment_<wbr>role_<wbr>mapping]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A List of Role Mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">roles</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentroles">dict{identity_<wbr>pool_<wbr>role_<wbr>attachment_<wbr>roles}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The map of roles associated with this pool. For a given role, the key will be either &#34;authenticated&#34; or &#34;unauthenticated&#34; and the value will be the Role ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## IdentityPoolRoleAttachment Output Properties

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
            <td class="align-top">Identity<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} An identity pool ID in the format REGION:GUID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentrolemapping">List&lt;Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Role<wbr>Mapping&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A List of Role Mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Roles</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentroles">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Roles</a></code>
            </td>
            <td class="align-top">{{% md %}} The map of roles associated with this pool. For a given role, the key will be either &#34;authenticated&#34; or &#34;unauthenticated&#34; and the value will be the Role ARN.
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
            <td class="align-top">Identity<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} An identity pool ID in the format REGION:GUID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentrolemapping">[]cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Role<wbr>Mapping</a></code>
            </td>
            <td class="align-top">{{% md %}} A List of Role Mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Roles</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentroles">cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Roles</a></code>
            </td>
            <td class="align-top">{{% md %}} The map of roles associated with this pool. For a given role, the key will be either &#34;authenticated&#34; or &#34;unauthenticated&#34; and the value will be the Role ARN.
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
            <td class="align-top">identity<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} An identity pool ID in the format REGION:GUID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentrolemapping">cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Role<wbr>Mapping[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A List of Role Mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">roles</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentroles">cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Roles</a></code>
            </td>
            <td class="align-top">{{% md %}} The map of roles associated with this pool. For a given role, the key will be either &#34;authenticated&#34; or &#34;unauthenticated&#34; and the value will be the Role ARN.
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
            <td class="align-top">identity_<wbr>pool_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} An identity pool ID in the format REGION:GUID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>mappings</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentrolemapping">list[identity_<wbr>pool_<wbr>role_<wbr>attachment_<wbr>role_<wbr>mapping]</a></code>
            </td>
            <td class="align-top">{{% md %}} A List of Role Mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">roles</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentroles">dict{identity_<wbr>pool_<wbr>role_<wbr>attachment_<wbr>roles}</a></code>
            </td>
            <td class="align-top">{{% md %}} The map of roles associated with this pool. For a given role, the key will be either &#34;authenticated&#34; or &#34;unauthenticated&#34; and the value will be the Role ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing IdentityPoolRoleAttachment Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cognito/#IdentityPoolRoleAttachmentState">IdentityPoolRoleAttachmentState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cognito/#IdentityPoolRoleAttachment">IdentityPoolRoleAttachment</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>identity_pool_id=None<span class="p">, </span>role_mappings=None<span class="p">, </span>roles=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetIdentityPoolRoleAttachment<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPoolRoleAttachmentState">IdentityPoolRoleAttachmentState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPoolRoleAttachment">IdentityPoolRoleAttachment</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPoolRoleAttachment.html">IdentityPoolRoleAttachment</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPoolRoleAttachmentState.html">IdentityPoolRoleAttachmentState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing IdentityPoolRoleAttachment resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Identity<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An identity pool ID in the format REGION:GUID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentrolemapping">List&lt;Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Role<wbr>Mapping<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A List of Role Mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Roles</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentroles">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Roles<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The map of roles associated with this pool. For a given role, the key will be either &#34;authenticated&#34; or &#34;unauthenticated&#34; and the value will be the Role ARN.
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
            <td class="align-top">Identity<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An identity pool ID in the format REGION:GUID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentrolemapping">[]cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Role<wbr>Mapping</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A List of Role Mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Roles</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentroles">*cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Roles</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The map of roles associated with this pool. For a given role, the key will be either &#34;authenticated&#34; or &#34;unauthenticated&#34; and the value will be the Role ARN.
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
            <td class="align-top">identity<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An identity pool ID in the format REGION:GUID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentrolemapping">cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Role<wbr>Mapping[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A List of Role Mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">roles</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentroles">cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Roles?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The map of roles associated with this pool. For a given role, the key will be either &#34;authenticated&#34; or &#34;unauthenticated&#34; and the value will be the Role ARN.
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
            <td class="align-top">identity_<wbr>pool_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An identity pool ID in the format REGION:GUID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>mappings</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentrolemapping">list[identity_<wbr>pool_<wbr>role_<wbr>attachment_<wbr>role_<wbr>mapping]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A List of Role Mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">roles</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentroles">dict{identity_<wbr>pool_<wbr>role_<wbr>attachment_<wbr>roles}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The map of roles associated with this pool. For a given role, the key will be either &#34;authenticated&#34; or &#34;unauthenticated&#34; and the value will be the Role ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### IdentityPoolRoleAttachmentRoleMapping
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#IdentityPoolRoleAttachmentRoleMapping">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#IdentityPoolRoleAttachmentRoleMapping">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPoolRoleAttachmentRoleMappingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPoolRoleAttachmentRoleMappingOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPoolRoleAttachmentRoleMappingArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPoolRoleAttachmentRoleMapping.html">output</a> API doc for this type.
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
            <td class="align-top">Ambiguous<wbr>Role<wbr>Resolution</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the action to be taken if either no rules match the claim value for the Rules type, or there is no cognito:preferred_role claim and there are multiple cognito:roles matches for the Token type. `Required` if you specify Token or Rules as the Type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Provider</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A string identifying the identity provider, for example, &#34;graph.facebook.com&#34; or &#34;cognito-idp.us-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mapping<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentrolemappingmappingrule">List&lt;Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Role<wbr>Mapping<wbr>Mapping<wbr>Rule<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Rules Configuration to be used for mapping users to roles. You can specify up to 25 rules per identity provider. Rules are evaluated in order. The first one to match specifies the role.
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
The role mapping type.
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
            <td class="align-top">Ambiguous<wbr>Role<wbr>Resolution</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the action to be taken if either no rules match the claim value for the Rules type, or there is no cognito:preferred_role claim and there are multiple cognito:roles matches for the Token type. `Required` if you specify Token or Rules as the Type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Provider</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A string identifying the identity provider, for example, &#34;graph.facebook.com&#34; or &#34;cognito-idp.us-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mapping<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentrolemappingmappingrule">[]cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Role<wbr>Mapping<wbr>Mapping<wbr>Rule</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Rules Configuration to be used for mapping users to roles. You can specify up to 25 rules per identity provider. Rules are evaluated in order. The first one to match specifies the role.
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
The role mapping type.
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
            <td class="align-top">ambiguous<wbr>Role<wbr>Resolution</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the action to be taken if either no rules match the claim value for the Rules type, or there is no cognito:preferred_role claim and there are multiple cognito:roles matches for the Token type. `Required` if you specify Token or Rules as the Type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity<wbr>Provider</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A string identifying the identity provider, for example, &#34;graph.facebook.com&#34; or &#34;cognito-idp.us-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mapping<wbr>Rules</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentrolemappingmappingrule">cognito.<wbr>Identity<wbr>Pool<wbr>Role<wbr>Attachment<wbr>Role<wbr>Mapping<wbr>Mapping<wbr>Rule[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Rules Configuration to be used for mapping users to roles. You can specify up to 25 rules per identity provider. Rules are evaluated in order. The first one to match specifies the role.
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
The role mapping type.
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
            <td class="align-top">ambiguous_<wbr>role_<wbr>resolution</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the action to be taken if either no rules match the claim value for the Rules type, or there is no cognito:preferred_role claim and there are multiple cognito:roles matches for the Token type. `Required` if you specify Token or Rules as the Type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity_<wbr>provider</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A string identifying the identity provider, for example, &#34;graph.facebook.com&#34; or &#34;cognito-idp.us-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mapping_<wbr>rules</td>
            <td class="align-top">
                
                <code><a href="#identitypoolroleattachmentrolemappingmappingrule">list[identity_<wbr>pool_<wbr>role_<wbr>attachment_<wbr>role_<wbr>mapping_<wbr>mapping_<wbr>rule]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Rules Configuration to be used for mapping users to roles. You can specify up to 25 rules per identity provider. Rules are evaluated in order. The first one to match specifies the role.
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
The role mapping type.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### IdentityPoolRoleAttachmentRoleMappingMappingRule
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#IdentityPoolRoleAttachmentRoleMappingMappingRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#IdentityPoolRoleAttachmentRoleMappingMappingRule">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPoolRoleAttachmentRoleMappingMappingRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPoolRoleAttachmentRoleMappingMappingRuleOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPoolRoleAttachmentRoleMappingMappingRuleArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPoolRoleAttachmentRoleMappingMappingRule.html">output</a> API doc for this type.
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
            <td class="align-top">Claim</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The claim name that must be present in the token, for example, &#34;isAdmin&#34; or &#34;paid&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Match<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The match condition that specifies how closely the claim value in the IdP token must match Value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role ARN.
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
A brief string that the claim must match, for example, &#34;paid&#34; or &#34;yes&#34;.
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
            <td class="align-top">Claim</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The claim name that must be present in the token, for example, &#34;isAdmin&#34; or &#34;paid&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Match<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The match condition that specifies how closely the claim value in the IdP token must match Value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role ARN.
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
A brief string that the claim must match, for example, &#34;paid&#34; or &#34;yes&#34;.
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
            <td class="align-top">claim</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The claim name that must be present in the token, for example, &#34;isAdmin&#34; or &#34;paid&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">match<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The match condition that specifies how closely the claim value in the IdP token must match Value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role ARN.
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
A brief string that the claim must match, for example, &#34;paid&#34; or &#34;yes&#34;.
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
            <td class="align-top">claim</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The claim name that must be present in the token, for example, &#34;isAdmin&#34; or &#34;paid&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">match_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The match condition that specifies how closely the claim value in the IdP token must match Value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role ARN.
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
A brief string that the claim must match, for example, &#34;paid&#34; or &#34;yes&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### IdentityPoolRoleAttachmentRoles
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#IdentityPoolRoleAttachmentRoles">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#IdentityPoolRoleAttachmentRoles">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPoolRoleAttachmentRolesArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPoolRoleAttachmentRolesOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPoolRoleAttachmentRolesArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPoolRoleAttachmentRoles.html">output</a> API doc for this type.
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
            <td class="align-top">Authenticated</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Unauthenticated</td>
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
            <td class="align-top">Authenticated</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Unauthenticated</td>
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
            <td class="align-top">authenticated</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">unauthenticated</td>
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
            <td class="align-top">authenticated</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">unauthenticated</td>
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







