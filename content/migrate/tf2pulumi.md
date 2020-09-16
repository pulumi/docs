---
title: Convert Your Terraform to a Modern Language
url: /tf2pulumi
layout: tf2pulumi
meta_desc: See what your Terraform HCL would look like in a modern language thanks to Pulumi.
form:
    hubspot_form_id: 8381e562-5fdf-4736-bb10-86096705e4ee
---

<!-- Load up various Prism JS/CSS files needed to dynamically colorize results -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.20.0/prism.min.js" data-manual></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.20.0/components/prism-javascript.min.js" data-manual></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.20.0/components/prism-typescript.min.js" data-manual></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.20.0/components/prism-python.min.js" data-manual></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.20.0/components/prism-python.min.js" data-manual></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.20.0/components/prism-go.min.js" data-manual></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.20.0/components/prism-csharp.min.js" data-manual></script>
<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.20.0/themes/prism.min.css" />
<!-- JS for dynamically creating and downloading source as zips. -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.5.0/jszip.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.2/FileSaver.min.js"></script>

<div class="w-full mx-auto md:flex">

<div class="md:w-1/2 md:mr-2">

<h3 class="text-gray-700 text-center">Enter your Terraform</h3>
<div class="text-gray-500 text-center m-1 -mb-2 text-xs">
    (Don't worry, we send it over SSL and don't store it on our servers.)
</div>

{{< chooser input-kind "code,url,upload" >}}

{{% choosable input-kind "code" %}}

<p class="m-0 -mt-4 p-2 bg-purple-300 text-white font-bold font-mono font-xs"
    style="font-size: 0.75rem !important; color: #fff !important">main.tf</p>
<textarea id="terraform-code" rows="27"
    class="w-full px-6 py-4 text-gray-700 text-sm font-mono overflow-y-scroll overflow-x-hidden whitespace-pre"
    title="Enter a single-file HCL program's text; see the 'UPLOAD' tab for multi-file programs">
</textarea>

<p class="text-gray-700 text-xs mb-1">
    Canned Examples:
</p>
<select id="terraform-canned-example" class="text-gray-700 text-xs">
    <option id=""></option>
    <option id="aws_ec2" selected>AWS EC2 instance running Ubuntu</option>
    <option id="azure_vm">Azure Virtual Machine running Ubuntu</option>
    <option id="google_gke">Google Kubernetes Engine cluster</option>
</select>

{{% /choosable %}}

{{% choosable input-kind "url" %}}

<input id="terraform-url" type="text" class="px-6 py-4 text-gray-700 text-sm w-full" value="https://"
    title="Enter a URL to a single HCL file (e.g., https://raw.githubusercontent.com/pulumi/tf2pulumi/master/tests/terraform/aws/ec2/main.tf); see the 'UPLOAD' tab for multiple files">
</input>

{{% /choosable %}}

{{% choosable input-kind "upload" %}}

<input id="terraform-upload" type="file" multiple class="px-6 py-4 text-gray-700 text-sm w-full">
</input>

{{% /choosable %}}

{{< /chooser >}}

</div>

<div class="md:w-1/2 md:ml-2">

<h3 class="text-gray-700 text-center">Choose your Pulumi Language</h3>
<div class="text-gray-500 text-center m-1 -mb-2 text-xs">
    &nbsp;
</div>

<div id="pulumi-code-download-icon" class="float-right mt-4 mr-1 hidden">
    <button class="copy-button" onclick="downloadCode()"><i class="fa fa-download text-xl" title="Download"></i></button>
</div>

{{< chooser language "typescript,javascript,python,go,csharp" >}}

{{% choosable language "typescript" %}}

<div id="pulumi-code-typescript-files" class="m-0 p-0"></div>

{{% /choosable %}}

{{% choosable language "javascript" %}}

<div id="pulumi-code-javascript-files" class="m-0 p-0"></div>

{{% /choosable %}}

{{% choosable language "python" %}}

<div id="pulumi-code-python-files" class="m-0 p-0"></div>

{{% /choosable %}}

{{% choosable language "go" %}}

<div id="pulumi-code-go-files" class="m-0 p-0"></div>

{{% /choosable %}}

{{% choosable language "csharp" %}}

<div id="pulumi-code-csharp-files" class="m-0 p-0"></div>

{{% /choosable %}}

{{< /chooser >}}

</div>

</div>

<pre id="pulumi-errors" class="text-center text-xs font-bold font-mono bg-gray-200 border-0 hidden" style="color:#ff0000"></pre>
<pre id="pulumi-warnings" class="text-center text-xs font-bold font-mono bg-gray-200 border-0 hidden" style="color:#cc6600"></pre>

<div class="text-center py-8">
    <a id="pulumi-code-download-button"
        class="btn btn-lg mr-4 opacity-50 cursor-not-allowed" onclick="downloadCode()">Download Code</a>
</div>
