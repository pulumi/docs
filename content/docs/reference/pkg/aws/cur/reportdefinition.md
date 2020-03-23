
---
title: "ReportDefinition"
block_external_search_index: true
---

Manages Cost and Usage Report Definitions.

> *NOTE:* The AWS Cost and Usage Report service is only available in `us-east-1` currently.

> *NOTE:* If AWS Organizations is enabled, only the master account can use this resource.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleCurReportDefinition = new aws.cur.ReportDefinition("example_cur_report_definition", {
    additionalArtifacts: [
        "REDSHIFT",
        "QUICKSIGHT",
    ],
    additionalSchemaElements: ["RESOURCES"],
    compression: "GZIP",
    format: "textORcsv",
    reportName: "example-cur-report-definition",
    s3Bucket: "example-bucket-name",
    s3Region: "us-east-1",
    timeUnit: "HOURLY",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cur_report_definition.html.markdown.



## Create a ReportDefinition Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cur/#ReportDefinition">ReportDefinition</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cur/#ReportDefinitionArgs">ReportDefinitionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">ReportDefinition</span><span class="p">(resource_name, opts=None, </span>additional_artifacts=None<span class="p">, </span>additional_schema_elements=None<span class="p">, </span>compression=None<span class="p">, </span>format=None<span class="p">, </span>report_name=None<span class="p">, </span>s3_bucket=None<span class="p">, </span>s3_prefix=None<span class="p">, </span>s3_region=None<span class="p">, </span>time_unit=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewReportDefinition<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cur?tab=doc#ReportDefinitionArgs">ReportDefinitionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cur?tab=doc#ReportDefinition">ReportDefinition</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cur.ReportDefinition.html">ReportDefinition</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cur.Inputs.ReportDefinitionArgs.html">ReportDefinitionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

#### Resource Arguments




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Artifacts</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Additional<wbr>Schema<wbr>Elements</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of schema elements. Valid values are: RESOURCES.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Compression</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Compression format for report. Valid values are: GZIP, ZIP.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Format for report. Valid values are: textORcsv.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Report<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>S3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Report path prefix. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>S3Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Region of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Time<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Artifacts</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Additional<wbr>Schema<wbr>Elements</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of schema elements. Valid values are: RESOURCES.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Compression</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Compression format for report. Valid values are: GZIP, ZIP.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Format for report. Valid values are: textORcsv.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Report<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>S3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Report path prefix. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>S3Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Region of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Time<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>additional<wbr>Artifacts</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>additional<wbr>Schema<wbr>Elements</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of schema elements. Valid values are: RESOURCES.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>compression</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Compression format for report. Valid values are: GZIP, ZIP.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Format for report. Valid values are: textORcsv.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>report<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>s3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Report path prefix. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>s3Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Region of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>time<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>additional_<wbr>artifacts</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>additional_<wbr>schema_<wbr>elements</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of schema elements. Valid values are: RESOURCES.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>compression</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Compression format for report. Valid values are: GZIP, ZIP.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>format</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Format for report. Valid values are: textORcsv.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>report_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>s3_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Report path prefix. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>s3_<wbr>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Region of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>time_<wbr>unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## ReportDefinition Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Additional<wbr>Artifacts</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Additional<wbr>Schema<wbr>Elements</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of schema elements. Valid values are: RESOURCES.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Compression</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Compression format for report. Valid values are: GZIP, ZIP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Format for report. Valid values are: textORcsv.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Report<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>S3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>S3Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Report path prefix. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>S3Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Region of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Time<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Additional<wbr>Artifacts</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Additional<wbr>Schema<wbr>Elements</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of schema elements. Valid values are: RESOURCES.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Compression</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Compression format for report. Valid values are: GZIP, ZIP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Format for report. Valid values are: textORcsv.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Report<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>S3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>S3Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Report path prefix. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>S3Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Region of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Time<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>additional<wbr>Artifacts</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>additional<wbr>Schema<wbr>Elements</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of schema elements. Valid values are: RESOURCES.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>compression</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Compression format for report. Valid values are: GZIP, ZIP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Format for report. Valid values are: textORcsv.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>report<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>s3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>s3Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Report path prefix. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>s3Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Region of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>time<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>additional_<wbr>artifacts</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>additional_<wbr>schema_<wbr>elements</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of schema elements. Valid values are: RESOURCES.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>compression</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Compression format for report. Valid values are: GZIP, ZIP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>format</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Format for report. Valid values are: textORcsv.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>report_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>s3_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>s3_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Report path prefix. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>s3_<wbr>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Region of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>time_<wbr>unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing ReportDefinition Resource

Get an existing ReportDefinition resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cur/#ReportDefinitionState">ReportDefinitionState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cur/#ReportDefinition">ReportDefinition</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>additional_artifacts=None<span class="p">, </span>additional_schema_elements=None<span class="p">, </span>compression=None<span class="p">, </span>format=None<span class="p">, </span>report_name=None<span class="p">, </span>s3_bucket=None<span class="p">, </span>s3_prefix=None<span class="p">, </span>s3_region=None<span class="p">, </span>time_unit=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetReportDefinition<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cur?tab=doc#ReportDefinitionState">ReportDefinitionState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cur?tab=doc#ReportDefinition">ReportDefinition</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cur.ReportDefinition.html">ReportDefinition</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cur.ReportDefinitionState.html">ReportDefinitionState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>resource_name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

The following state arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Artifacts</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Schema<wbr>Elements</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of schema elements. Valid values are: RESOURCES.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Compression</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Compression format for report. Valid values are: GZIP, ZIP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Format for report. Valid values are: textORcsv.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Report<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Report path prefix. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Region of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Artifacts</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Schema<wbr>Elements</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of schema elements. Valid values are: RESOURCES.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Compression</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Compression format for report. Valid values are: GZIP, ZIP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Format for report. Valid values are: textORcsv.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Report<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Report path prefix. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Region of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>additional<wbr>Artifacts</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>additional<wbr>Schema<wbr>Elements</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of schema elements. Valid values are: RESOURCES.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>compression</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Compression format for report. Valid values are: GZIP, ZIP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Format for report. Valid values are: textORcsv.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>report<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Report path prefix. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Region of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>additional_<wbr>artifacts</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>additional_<wbr>schema_<wbr>elements</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of schema elements. Valid values are: RESOURCES.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>compression</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Compression format for report. Valid values are: GZIP, ZIP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>format</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Format for report. Valid values are: textORcsv.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>report_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Report path prefix. Limited to 256 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3_<wbr>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Region of the existing S3 bucket to hold generated reports.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time_<wbr>unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









