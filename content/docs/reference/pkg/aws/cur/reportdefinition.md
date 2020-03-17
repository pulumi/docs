
---
title: "ReportDefinition"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


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

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cur/#ReportDefinition">ReportDefinition</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cur/#ReportDefinitionArgs">ReportDefinitionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">ReportDefinition</span><span class="p">(resource_name, opts=None, </span>additional_artifacts=None<span class="p">, </span>additional_schema_elements=None<span class="p">, </span>compression=None<span class="p">, </span>format=None<span class="p">, </span>report_name=None<span class="p">, </span>s3_bucket=None<span class="p">, </span>s3_prefix=None<span class="p">, </span>s3_region=None<span class="p">, </span>time_unit=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewReportDefinition<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cur?tab=doc#ReportDefinitionArgs">ReportDefinitionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cur?tab=doc#ReportDefinition">ReportDefinition</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cur.ReportDefinition.html">ReportDefinition</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cur.ReportDefinitionArgs.html">ReportDefinitionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a ReportDefinition resource with the given unique name, arguments, and options.

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
            <td class="align-top">Additional<wbr>Artifacts</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Additional<wbr>Schema<wbr>Elements</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of schema elements. Valid values are: RESOURCES.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Compression format for report. Valid values are: GZIP, ZIP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Format</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Format for report. Valid values are: textORcsv.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Report<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Report path prefix. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Region of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Time<wbr>Unit</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
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
            <td class="align-top">Additional<wbr>Artifacts</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Additional<wbr>Schema<wbr>Elements</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of schema elements. Valid values are: RESOURCES.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Compression format for report. Valid values are: GZIP, ZIP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Format</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Format for report. Valid values are: textORcsv.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Report<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Report path prefix. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Region of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Time<wbr>Unit</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
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
            <td class="align-top">additional<wbr>Artifacts</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">additional<wbr>Schema<wbr>Elements</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of schema elements. Valid values are: RESOURCES.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Compression format for report. Valid values are: GZIP, ZIP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">format</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Format for report. Valid values are: textORcsv.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">report<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Report path prefix. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Region of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">time<wbr>Unit</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
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
            <td class="align-top">additional_<wbr>artifacts</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">additional_<wbr>schema_<wbr>elements</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of schema elements. Valid values are: RESOURCES.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Compression format for report. Valid values are: GZIP, ZIP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">format</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Format for report. Valid values are: textORcsv.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">report_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Report path prefix. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Region of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">time_<wbr>unit</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## ReportDefinition Output Properties

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
            <td class="align-top">Additional<wbr>Artifacts</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Additional<wbr>Schema<wbr>Elements</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} A list of schema elements. Valid values are: RESOURCES.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Compression format for report. Valid values are: GZIP, ZIP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Format</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Format for report. Valid values are: textORcsv.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Report<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Report path prefix. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Region of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Time<wbr>Unit</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
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
            <td class="align-top">Additional<wbr>Artifacts</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Additional<wbr>Schema<wbr>Elements</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of schema elements. Valid values are: RESOURCES.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Compression format for report. Valid values are: GZIP, ZIP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Format</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Format for report. Valid values are: textORcsv.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Report<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Report path prefix. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Region of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Time<wbr>Unit</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
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
            <td class="align-top">additional<wbr>Artifacts</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">additional<wbr>Schema<wbr>Elements</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} A list of schema elements. Valid values are: RESOURCES.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Compression format for report. Valid values are: GZIP, ZIP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">format</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Format for report. Valid values are: textORcsv.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">report<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Report path prefix. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Region of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">time<wbr>Unit</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
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
            <td class="align-top">additional_<wbr>artifacts</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">additional_<wbr>schema_<wbr>elements</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} A list of schema elements. Valid values are: RESOURCES.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Compression format for report. Valid values are: GZIP, ZIP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">format</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Format for report. Valid values are: textORcsv.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">report_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Report path prefix. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Region of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">time_<wbr>unit</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing ReportDefinition Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cur/#ReportDefinitionState">ReportDefinitionState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cur/#ReportDefinition">ReportDefinition</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>additional_artifacts=None<span class="p">, </span>additional_schema_elements=None<span class="p">, </span>compression=None<span class="p">, </span>format=None<span class="p">, </span>report_name=None<span class="p">, </span>s3_bucket=None<span class="p">, </span>s3_prefix=None<span class="p">, </span>s3_region=None<span class="p">, </span>time_unit=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetReportDefinition<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cur?tab=doc#ReportDefinitionState">ReportDefinitionState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cur?tab=doc#ReportDefinition">ReportDefinition</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cur.ReportDefinition.html">ReportDefinition</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cur.ReportDefinitionState.html">ReportDefinitionState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing ReportDefinition resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Additional<wbr>Artifacts</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Additional<wbr>Schema<wbr>Elements</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of schema elements. Valid values are: RESOURCES.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Compression format for report. Valid values are: GZIP, ZIP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Format for report. Valid values are: textORcsv.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Report<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Report path prefix. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Region of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Time<wbr>Unit</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
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
            <td class="align-top">Additional<wbr>Artifacts</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Additional<wbr>Schema<wbr>Elements</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of schema elements. Valid values are: RESOURCES.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Compression format for report. Valid values are: GZIP, ZIP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Format</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Format for report. Valid values are: textORcsv.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Report<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Bucket</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Report path prefix. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Region</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Region of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Time<wbr>Unit</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
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
            <td class="align-top">additional<wbr>Artifacts</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">additional<wbr>Schema<wbr>Elements</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of schema elements. Valid values are: RESOURCES.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Compression format for report. Valid values are: GZIP, ZIP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Format for report. Valid values are: textORcsv.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">report<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Report path prefix. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Region of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">time<wbr>Unit</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
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
            <td class="align-top">additional_<wbr>artifacts</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of additional artifacts. Valid values are: REDSHIFT, QUICKSIGHT.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">additional_<wbr>schema_<wbr>elements</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of schema elements. Valid values are: RESOURCES.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Compression format for report. Valid values are: GZIP, ZIP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">format</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Format for report. Valid values are: textORcsv.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">report_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Unique name for the report. Must start with a number/letter and is case sensitive. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Report path prefix. Limited to 256 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Region of the existing S3 bucket to hold generated reports.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">time_<wbr>unit</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frequency on which report data are measured and displayed.  Valid values are: HOURLY, DAILY.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}









