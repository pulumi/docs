
---
title: "GetPolicyDocument"
block_external_search_index: true
---

Generates an IAM policy document in JSON format.

This is a data source which can be used to construct a JSON representation of
an IAM policy document, for use with resources which expect policy documents,
such as the `aws.iam.Policy` resource.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const examplePolicyDocument = aws.iam.getPolicyDocument({
    statements: [
        {
            actions: [
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation",
            ],
            resources: ["arn:aws:s3:::*"],
            sid: "1",
        },
        {
            actions: ["s3:ListBucket"],
            conditions: [{
                test: "StringLike",
                values: [
                    "",
                    "home/",
                    "home/&{aws:username}/",
                ],
                variable: "s3:prefix",
            }],
            resources: [`arn:aws:s3:::${var_s3_bucket_name}`],
        },
        {
            actions: ["s3:*"],
            resources: [
                `arn:aws:s3:::${var_s3_bucket_name}/home/&{aws:username}`,
                `arn:aws:s3:::${var_s3_bucket_name}/home/&{aws:username}/*`,
            ],
        },
    ],
});
const examplePolicy = new aws.iam.Policy("example", {
    path: "/",
    policy: examplePolicyDocument.json,
});
```

Using this data source to generate policy documents is *optional*. It is also
valid to use literal JSON strings within your configuration, or to use the
`file` interpolation function to read a raw JSON policy document from a file.

## Context Variable Interpolation

The IAM policy document format allows context variables to be interpolated
into various strings within a statement. The native IAM policy document format
uses `${...}`-style syntax that is in conflict with interpolation
syntax, so this data source instead uses `&{...}` syntax for interpolations that
should be processed by AWS rather than by this provider.

## Wildcard Principal

In order to define wildcard principal (a.k.a. anonymous user) use `type = "*"` and
`identifiers = ["*"]`. In that case the rendered json will contain `"Principal": "*"`.
Note, that even though the [IAM Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html)
states that `"Principal": "*"` and `"Principal": {"AWS": "*"}` are equivalent,
those principals have different behavior for IAM Role Trust Policy. Therefore
this provider will normalize the principal field only in above-mentioned case and principals
like `type = "AWS"` and `identifiers = ["*"]` will be rendered as `"Principal": {"AWS": "*"}`.

## Example with Multiple Principals

Showing how you can use this as an assume role policy as well as showing how you can specify multiple principal blocks with different types.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const eventStreamBucketRoleAssumeRolePolicy = aws.iam.getPolicyDocument({
    statements: [{
        actions: ["sts:AssumeRole"],
        principals: [
            {
                identifiers: ["firehose.amazonaws.com"],
                type: "Service",
            },
            {
                identifiers: [var_trusted_role_arn],
                type: "AWS",
            },
        ],
    }],
});
```

## Example with Source and Override

Showing how you can use `source_json` and `override_json`

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const source = aws.iam.getPolicyDocument({
    statements: [
        {
            actions: ["ec2:*"],
            resources: ["*"],
        },
        {
            actions: ["s3:*"],
            resources: ["*"],
            sid: "SidToOverwrite",
        },
    ],
});
const sourceJsonExample = aws.iam.getPolicyDocument({
    sourceJson: source.json,
    statements: [{
        actions: ["s3:*"],
        resources: [
            "arn:aws:s3:::somebucket",
            "arn:aws:s3:::somebucket/*",
        ],
        sid: "SidToOverwrite",
    }],
});
const override = aws.iam.getPolicyDocument({
    statements: [{
        actions: ["s3:*"],
        resources: ["*"],
        sid: "SidToOverwrite",
    }],
});
const overrideJsonExample = aws.iam.getPolicyDocument({
    overrideJson: override.json,
    statements: [
        {
            actions: ["ec2:*"],
            resources: ["*"],
        },
        {
            actions: ["s3:*"],
            resources: [
                "arn:aws:s3:::somebucket",
                "arn:aws:s3:::somebucket/*",
            ],
            sid: "SidToOverwrite",
        },
    ],
});
```

`data.aws_iam_policy_document.source_json_example.json` will evaluate to:

```typescript
import * as pulumi from "@pulumi/pulumi";
```

`data.aws_iam_policy_document.override_json_example.json` will evaluate to:

```typescript
import * as pulumi from "@pulumi/pulumi";
```

You can also combine `source_json` and `override_json` in the same document.

## Example without Statement

Use without a `statement`:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const source = aws.iam.getPolicyDocument({
    statements: [{
        actions: ["ec2:DescribeAccountAttributes"],
        resources: ["*"],
        sid: "OverridePlaceholder",
    }],
});
const override = aws.iam.getPolicyDocument({
    statements: [{
        actions: ["s3:GetObject"],
        resources: ["*"],
        sid: "OverridePlaceholder",
    }],
});
const politik = aws.iam.getPolicyDocument({
    overrideJson: override.json,
    sourceJson: source.json,
});
```

`data.aws_iam_policy_document.politik.json` will evaluate to:

```typescript
import * as pulumi from "@pulumi/pulumi";
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_policy_document.html.markdown.





## Using GetPolicyDocument

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getPolicyDocument<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/iam/#GetPolicyDocumentArgs">GetPolicyDocumentArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">pulumi.InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/iam/#GetPolicyDocumentResult">GetPolicyDocumentResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_policy_document(</span>override_json=None<span class="p">, </span>policy_id=None<span class="p">, </span>source_json=None<span class="p">, </span>statements=None<span class="p">, </span>version=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupPolicyDocument<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#LookupPolicyDocumentArgs">LookupPolicyDocumentArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#LookupPolicyDocumentResult">LookupPolicyDocumentResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetPolicyDocument </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iam.GetPolicyDocumentResult.html">GetPolicyDocumentResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iam.Inputs.GetPolicyDocumentArgs.html">GetPolicyDocumentArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">Pulumi.InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Override<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An IAM policy document to import and override the
current policy document.  Statements with non-blank `sid`s in the override
document will overwrite statements with the same `sid` in the current document.
Statements without an `sid` cannot be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An ID for the policy document.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An IAM policy document to import as a base for the
current policy document.  Statements with non-blank `sid`s in the current
policy document will overwrite statements with the same `sid` in the source
json.  Statements without an `sid` cannot be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatement">List&lt;Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block (described below)
configuring one *statement* to be included in the policy document.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IAM policy document version. Valid values: `2008-10-17`, `2012-10-17`. Defaults to `2012-10-17`. For more information, see the [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Override<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An IAM policy document to import and override the
current policy document.  Statements with non-blank `sid`s in the override
document will overwrite statements with the same `sid` in the current document.
Statements without an `sid` cannot be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An ID for the policy document.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An IAM policy document to import as a base for the
current policy document.  Statements with non-blank `sid`s in the current
policy document will overwrite statements with the same `sid` in the source
json.  Statements without an `sid` cannot be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatement">[]Get<wbr>Policy<wbr>Document<wbr>Statement</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block (described below)
configuring one *statement* to be included in the policy document.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}IAM policy document version. Valid values: `2008-10-17`, `2012-10-17`. Defaults to `2012-10-17`. For more information, see the [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>override<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An IAM policy document to import and override the
current policy document.  Statements with non-blank `sid`s in the override
document will overwrite statements with the same `sid` in the current document.
Statements without an `sid` cannot be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An ID for the policy document.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An IAM policy document to import as a base for the
current policy document.  Statements with non-blank `sid`s in the current
policy document will overwrite statements with the same `sid` in the source
json.  Statements without an `sid` cannot be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatement">Get<wbr>Policy<wbr>Document<wbr>Statement[]?</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block (described below)
configuring one *statement* to be included in the policy document.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IAM policy document version. Valid values: `2008-10-17`, `2012-10-17`. Defaults to `2012-10-17`. For more information, see the [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>override_<wbr>json</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An IAM policy document to import and override the
current policy document.  Statements with non-blank `sid`s in the override
document will overwrite statements with the same `sid` in the current document.
Statements without an `sid` cannot be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policy_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An ID for the policy document.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>json</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An IAM policy document to import as a base for the
current policy document.  Statements with non-blank `sid`s in the current
policy document will overwrite statements with the same `sid` in the source
json.  Statements without an `sid` cannot be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatement">List[Get<wbr>Policy<wbr>Document<wbr>Statement]</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block (described below)
configuring one *statement* to be included in the policy document.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}IAM policy document version. Valid values: `2008-10-17`, `2012-10-17`. Defaults to `2012-10-17`. For more information, see the [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetPolicyDocument Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

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
        <span>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The above arguments serialized as a standard JSON policy document.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Override<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatement">List&lt;Get<wbr>Policy<wbr>Document<wbr>Statement&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

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
        <span>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The above arguments serialized as a standard JSON policy document.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Override<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatement">[]Get<wbr>Policy<wbr>Document<wbr>Statement</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

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
        <span>json</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The above arguments serialized as a standard JSON policy document.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>override<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatement">Get<wbr>Policy<wbr>Document<wbr>Statement[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

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
        <span>json</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The above arguments serialized as a standard JSON policy document.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>override_<wbr>json</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>policy_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source_<wbr>json</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatement">List[Get<wbr>Policy<wbr>Document<wbr>Statement]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Policy<wbr>Document<wbr>Statement</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetPolicyDocumentStatement">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetPolicyDocumentStatement">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#GetPolicyDocumentStatementArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#GetPolicyDocumentStatement">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Actions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of actions that this statement either allows
or denies. For example, ``["ec2:RunInstances", "s3:*"]``.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatementcondition">List&lt;Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Condition<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block (described below)
that defines a further, possibly-service-specific condition that constrains
whether this statement applies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Either "Allow" or "Deny", to specify whether this
statement allows or denies the given actions. The default is "Allow".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Not<wbr>Actions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of actions that this statement does *not*
apply to. Used to apply a policy statement to all actions *except* those
listed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Not<wbr>Principals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatementnotprincipal">List&lt;Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Not<wbr>Principal<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Like `principals` except gives resources that
the statement does *not* apply to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Not<wbr>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of resource ARNs that this statement
does *not* apply to. Used to apply a policy statement to all resources
*except* those listed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Principals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatementprincipal">List&lt;Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Principal<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block (described below)
specifying a resource (or resource pattern) to which this statement applies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of resource ARNs that this statement applies
to. This is required by AWS if used for an IAM policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An ID for the policy statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Actions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of actions that this statement either allows
or denies. For example, ``["ec2:RunInstances", "s3:*"]``.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatementcondition">[]Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Condition</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block (described below)
that defines a further, possibly-service-specific condition that constrains
whether this statement applies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Either "Allow" or "Deny", to specify whether this
statement allows or denies the given actions. The default is "Allow".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Not<wbr>Actions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of actions that this statement does *not*
apply to. Used to apply a policy statement to all actions *except* those
listed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Not<wbr>Principals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatementnotprincipal">[]Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Not<wbr>Principal</a></span>
    </dt>
    <dd>{{% md %}}Like `principals` except gives resources that
the statement does *not* apply to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Not<wbr>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of resource ARNs that this statement
does *not* apply to. Used to apply a policy statement to all resources
*except* those listed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Principals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatementprincipal">[]Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Principal</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block (described below)
specifying a resource (or resource pattern) to which this statement applies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of resource ARNs that this statement applies
to. This is required by AWS if used for an IAM policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sid</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An ID for the policy statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>actions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of actions that this statement either allows
or denies. For example, ``["ec2:RunInstances", "s3:*"]``.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatementcondition">Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Condition[]?</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block (described below)
that defines a further, possibly-service-specific condition that constrains
whether this statement applies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Either "Allow" or "Deny", to specify whether this
statement allows or denies the given actions. The default is "Allow".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>not<wbr>Actions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of actions that this statement does *not*
apply to. Used to apply a policy statement to all actions *except* those
listed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>not<wbr>Principals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatementnotprincipal">Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Not<wbr>Principal[]?</a></span>
    </dt>
    <dd>{{% md %}}Like `principals` except gives resources that
the statement does *not* apply to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>not<wbr>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of resource ARNs that this statement
does *not* apply to. Used to apply a policy statement to all resources
*except* those listed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>principals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatementprincipal">Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Principal[]?</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block (described below)
specifying a resource (or resource pattern) to which this statement applies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resources</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of resource ARNs that this statement applies
to. This is required by AWS if used for an IAM policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An ID for the policy statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>actions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of actions that this statement either allows
or denies. For example, ``["ec2:RunInstances", "s3:*"]``.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatementcondition">List[Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Condition]</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block (described below)
that defines a further, possibly-service-specific condition that constrains
whether this statement applies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Either "Allow" or "Deny", to specify whether this
statement allows or denies the given actions. The default is "Allow".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>not<wbr>Actions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of actions that this statement does *not*
apply to. Used to apply a policy statement to all actions *except* those
listed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>not<wbr>Principals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatementnotprincipal">List[Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Not<wbr>Principal]</a></span>
    </dt>
    <dd>{{% md %}}Like `principals` except gives resources that
the statement does *not* apply to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>not<wbr>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of resource ARNs that this statement
does *not* apply to. Used to apply a policy statement to all resources
*except* those listed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>principals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpolicydocumentstatementprincipal">List[Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Principal]</a></span>
    </dt>
    <dd>{{% md %}}A nested configuration block (described below)
specifying a resource (or resource pattern) to which this statement applies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resources</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of resource ARNs that this statement applies
to. This is required by AWS if used for an IAM policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sid</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An ID for the policy statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Condition</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetPolicyDocumentStatementCondition">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetPolicyDocumentStatementCondition">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#GetPolicyDocumentStatementConditionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#GetPolicyDocumentStatementCondition">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Test</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the
[IAM condition operator](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html)
to evaluate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The values to evaluate the condition against. If multiple
values are provided, the condition matches if at least one of them applies.
(That is, the tests are combined with the "OR" boolean operation.)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of a
[Context Variable](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys)
to apply the condition to. Context variables may either be standard AWS
variables starting with `aws:`, or service-specific variables prefixed with
the service name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Test</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the
[IAM condition operator](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html)
to evaluate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The values to evaluate the condition against. If multiple
values are provided, the condition matches if at least one of them applies.
(That is, the tests are combined with the "OR" boolean operation.)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of a
[Context Variable](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys)
to apply the condition to. Context variables may either be standard AWS
variables starting with `aws:`, or service-specific variables prefixed with
the service name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>test</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the
[IAM condition operator](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html)
to evaluate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The values to evaluate the condition against. If multiple
values are provided, the condition matches if at least one of them applies.
(That is, the tests are combined with the "OR" boolean operation.)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of a
[Context Variable](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys)
to apply the condition to. Context variables may either be standard AWS
variables starting with `aws:`, or service-specific variables prefixed with
the service name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>test</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the
[IAM condition operator](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html)
to evaluate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The values to evaluate the condition against. If multiple
values are provided, the condition matches if at least one of them applies.
(That is, the tests are combined with the "OR" boolean operation.)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of a
[Context Variable](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys)
to apply the condition to. Context variables may either be standard AWS
variables starting with `aws:`, or service-specific variables prefixed with
the service name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Not<wbr>Principal</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetPolicyDocumentStatementNotPrincipal">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetPolicyDocumentStatementNotPrincipal">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#GetPolicyDocumentStatementNotPrincipalArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#GetPolicyDocumentStatementNotPrincipal">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}List of identifiers for principals. When `type`
is "AWS", these are IAM user or role ARNs.  When `type` is "Service", these are AWS Service roles e.g. `lambda.amazonaws.com`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of principal. For AWS ARNs this is "AWS".  For AWS services (e.g. Lambda), this is "Service".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of identifiers for principals. When `type`
is "AWS", these are IAM user or role ARNs.  When `type` is "Service", these are AWS Service roles e.g. `lambda.amazonaws.com`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of principal. For AWS ARNs this is "AWS".  For AWS services (e.g. Lambda), this is "Service".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}List of identifiers for principals. When `type`
is "AWS", these are IAM user or role ARNs.  When `type` is "Service", these are AWS Service roles e.g. `lambda.amazonaws.com`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of principal. For AWS ARNs this is "AWS".  For AWS services (e.g. Lambda), this is "Service".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of identifiers for principals. When `type`
is "AWS", these are IAM user or role ARNs.  When `type` is "Service", these are AWS Service roles e.g. `lambda.amazonaws.com`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of principal. For AWS ARNs this is "AWS".  For AWS services (e.g. Lambda), this is "Service".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Policy<wbr>Document<wbr>Statement<wbr>Principal</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetPolicyDocumentStatementPrincipal">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetPolicyDocumentStatementPrincipal">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#GetPolicyDocumentStatementPrincipalArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#GetPolicyDocumentStatementPrincipal">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}List of identifiers for principals. When `type`
is "AWS", these are IAM user or role ARNs.  When `type` is "Service", these are AWS Service roles e.g. `lambda.amazonaws.com`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of principal. For AWS ARNs this is "AWS".  For AWS services (e.g. Lambda), this is "Service".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of identifiers for principals. When `type`
is "AWS", these are IAM user or role ARNs.  When `type` is "Service", these are AWS Service roles e.g. `lambda.amazonaws.com`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of principal. For AWS ARNs this is "AWS".  For AWS services (e.g. Lambda), this is "Service".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}List of identifiers for principals. When `type`
is "AWS", these are IAM user or role ARNs.  When `type` is "Service", these are AWS Service roles e.g. `lambda.amazonaws.com`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of principal. For AWS ARNs this is "AWS".  For AWS services (e.g. Lambda), this is "Service".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>identifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of identifiers for principals. When `type`
is "AWS", these are IAM user or role ARNs.  When `type` is "Service", these are AWS Service roles e.g. `lambda.amazonaws.com`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of principal. For AWS ARNs this is "AWS".  For AWS services (e.g. Lambda), this is "Service".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







