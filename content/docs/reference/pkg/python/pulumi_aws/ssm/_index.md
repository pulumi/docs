---
---

<div class="section" id="ssm">
<h1>ssm<a class="headerlink" href="#ssm" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.ssm"></span><dl class="class">
<dt id="pulumi_aws.ssm.Activation">
<em class="property">class </em><code class="descclassname">pulumi_aws.ssm.</code><code class="descname">Activation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>expiration_date=None</em>, <em>iam_role=None</em>, <em>name=None</em>, <em>registration_limit=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Activation" title="Permalink to this definition">¶</a></dt>
<dd><p>Registers an on-premises server or virtual machine with Amazon EC2 so that it can be managed using Run Command.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the resource that you want to register.</li>
<li><strong>expiration_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A timestamp in <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339 format</a> by which this activation request should expire. The default value is 24 hours from resource creation time.</li>
<li><strong>iam_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM Role to attach to the managed instance.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default name of the registered managed instance.</li>
<li><strong>registration_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of managed instances you want to register. The default value is 1 instance.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the object.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_activation.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_activation.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ssm.Activation.activation_code">
<code class="descname">activation_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.activation_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The code the system generates when it processes the activation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Activation.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the resource that you want to register.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Activation.expiration_date">
<code class="descname">expiration_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.expiration_date" title="Permalink to this definition">¶</a></dt>
<dd><p>A timestamp in <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339 format</a> by which this activation request should expire. The default value is 24 hours from resource creation time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Activation.expired">
<code class="descname">expired</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.expired" title="Permalink to this definition">¶</a></dt>
<dd><p>If the current activation has expired.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Activation.iam_role">
<code class="descname">iam_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.iam_role" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM Role to attach to the managed instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Activation.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The default name of the registered managed instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Activation.registration_count">
<code class="descname">registration_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.registration_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of managed instances that are currently registered using this activation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Activation.registration_limit">
<code class="descname">registration_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.registration_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of managed instances you want to register. The default value is 1 instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Activation.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Activation.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.Activation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Activation.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.Activation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Activation.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ssm.Association">
<em class="property">class </em><code class="descclassname">pulumi_aws.ssm.</code><code class="descname">Association</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>association_name=None</em>, <em>compliance_severity=None</em>, <em>document_version=None</em>, <em>instance_id=None</em>, <em>max_concurrency=None</em>, <em>max_errors=None</em>, <em>name=None</em>, <em>output_location=None</em>, <em>parameters=None</em>, <em>schedule_expression=None</em>, <em>targets=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Association" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates an SSM Document to an instance or EC2 tag.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>association_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The descriptive name for the association.</li>
<li><strong>compliance_severity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compliance severity for the association. Can be one of the following: <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>, <code class="docutils literal notranslate"><span class="pre">LOW</span></code>, <code class="docutils literal notranslate"><span class="pre">MEDIUM</span></code>, <code class="docutils literal notranslate"><span class="pre">HIGH</span></code> or <code class="docutils literal notranslate"><span class="pre">CRITICAL</span></code></li>
<li><strong>document_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The document version you want to associate with the target(s). Can be a specific version or the default version.</li>
<li><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance ID to apply an SSM document to. Use <code class="docutils literal notranslate"><span class="pre">targets</span></code> with key <code class="docutils literal notranslate"><span class="pre">InstanceIds</span></code> for document schema versions 2.0 and above.</li>
<li><strong>max_concurrency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%.</li>
<li><strong>max_errors</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify a number, for example 10, or a percentage of the target set, for example 10%.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SSM document to apply.</li>
<li><strong>output_location</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An output location block. Output Location is documented below.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A block of arbitrary string parameters to pass to the SSM document.</li>
<li><strong>schedule_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A cron expression when the association will be applied to the target(s).</li>
<li><strong>targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block containing the targets of the SSM association. Targets are documented below. AWS currently supports a maximum of 5 targets.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_association.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ssm.Association.association_name">
<code class="descname">association_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.association_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The descriptive name for the association.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Association.compliance_severity">
<code class="descname">compliance_severity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.compliance_severity" title="Permalink to this definition">¶</a></dt>
<dd><p>The compliance severity for the association. Can be one of the following: <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>, <code class="docutils literal notranslate"><span class="pre">LOW</span></code>, <code class="docutils literal notranslate"><span class="pre">MEDIUM</span></code>, <code class="docutils literal notranslate"><span class="pre">HIGH</span></code> or <code class="docutils literal notranslate"><span class="pre">CRITICAL</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Association.document_version">
<code class="descname">document_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.document_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The document version you want to associate with the target(s). Can be a specific version or the default version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Association.instance_id">
<code class="descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance ID to apply an SSM document to. Use <code class="docutils literal notranslate"><span class="pre">targets</span></code> with key <code class="docutils literal notranslate"><span class="pre">InstanceIds</span></code> for document schema versions 2.0 and above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Association.max_concurrency">
<code class="descname">max_concurrency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.max_concurrency" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Association.max_errors">
<code class="descname">max_errors</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.max_errors" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify a number, for example 10, or a percentage of the target set, for example 10%.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Association.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SSM document to apply.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Association.output_location">
<code class="descname">output_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.output_location" title="Permalink to this definition">¶</a></dt>
<dd><p>An output location block. Output Location is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Association.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A block of arbitrary string parameters to pass to the SSM document.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Association.schedule_expression">
<code class="descname">schedule_expression</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.schedule_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>A cron expression when the association will be applied to the target(s).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Association.targets">
<code class="descname">targets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Association.targets" title="Permalink to this definition">¶</a></dt>
<dd><p>A block containing the targets of the SSM association. Targets are documented below. AWS currently supports a maximum of 5 targets.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.Association.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Association.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.Association.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Association.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ssm.Document">
<em class="property">class </em><code class="descclassname">pulumi_aws.ssm.</code><code class="descname">Document</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>content=None</em>, <em>document_format=None</em>, <em>document_type=None</em>, <em>name=None</em>, <em>permissions=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Document" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SSM Document resource</p>
<blockquote>
<div><strong>NOTE on updating SSM documents:</strong> Only documents with a schema version of 2.0
or greater can update their content once created, see [SSM Schema Features][1]. To update a document with an older
schema version you must recreate the resource.</div></blockquote>
<p>The permissions attribute specifies how you want to share the document. If you share a document privately,
you must specify the AWS user account IDs for those people who can use the document. If you share a document
publicly, you must specify All as the account ID.</p>
<p>The permissions mapping supports the following:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">type</span></code> - The permission type for the document. The permission type can be <code class="docutils literal notranslate"><span class="pre">Share</span></code>.</li>
<li><code class="docutils literal notranslate"><span class="pre">account_ids</span></code> - The AWS user accounts that should have access to the document. The account IDs can either be a group of account IDs or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JSON or YAML content of the document.</li>
<li><strong>document_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of the document. Valid document types include: <code class="docutils literal notranslate"><span class="pre">JSON</span></code> and <code class="docutils literal notranslate"><span class="pre">YAML</span></code></li>
<li><strong>document_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the document. Valid document types include: <code class="docutils literal notranslate"><span class="pre">Command</span></code>, <code class="docutils literal notranslate"><span class="pre">Policy</span></code>, <code class="docutils literal notranslate"><span class="pre">Automation</span></code> and <code class="docutils literal notranslate"><span class="pre">Session</span></code></li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the document.</li>
<li><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Additional Permissions to attach to the document. See Permissions below for details.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the object.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_document.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_document.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ssm.Document.content">
<code class="descname">content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The JSON or YAML content of the document.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Document.created_date">
<code class="descname">created_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the document was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Document.default_version">
<code class="descname">default_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.default_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The default version of the document.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Document.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the document.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Document.document_format">
<code class="descname">document_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.document_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The format of the document. Valid document types include: <code class="docutils literal notranslate"><span class="pre">JSON</span></code> and <code class="docutils literal notranslate"><span class="pre">YAML</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Document.document_type">
<code class="descname">document_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.document_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the document. Valid document types include: <code class="docutils literal notranslate"><span class="pre">Command</span></code>, <code class="docutils literal notranslate"><span class="pre">Policy</span></code>, <code class="docutils literal notranslate"><span class="pre">Automation</span></code> and <code class="docutils literal notranslate"><span class="pre">Session</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Document.hash">
<code class="descname">hash</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.hash" title="Permalink to this definition">¶</a></dt>
<dd><p>The sha1 or sha256 of the document content</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Document.hash_type">
<code class="descname">hash_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.hash_type" title="Permalink to this definition">¶</a></dt>
<dd><p>“Sha1” “Sha256”. The hashing algorithm used when hashing the content.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Document.latest_version">
<code class="descname">latest_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.latest_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest version of the document.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Document.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the document.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Document.owner">
<code class="descname">owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS user account of the person who created the document.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Document.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>The parameters that are available to this document.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Document.permissions">
<code class="descname">permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional Permissions to attach to the document. See Permissions below for details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Document.platform_types">
<code class="descname">platform_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.platform_types" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of OS platforms compatible with this SSM document, either “Windows” or “Linux”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Document.schema_version">
<code class="descname">schema_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.schema_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The schema version of the document.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Document.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.status" title="Permalink to this definition">¶</a></dt>
<dd><p>“Creating”, “Active” or “Deleting”. The current status of the document.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Document.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Document.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.Document.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Document.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.Document.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Document.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ssm.GetDocumentResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ssm.</code><code class="descname">GetDocumentResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>content=None</em>, <em>document_format=None</em>, <em>document_type=None</em>, <em>document_version=None</em>, <em>name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.GetDocumentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDocument.</p>
<dl class="attribute">
<dt id="pulumi_aws.ssm.GetDocumentResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.GetDocumentResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the document.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.GetDocumentResult.content">
<code class="descname">content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.GetDocumentResult.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The contents of the document.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.GetDocumentResult.document_type">
<code class="descname">document_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.GetDocumentResult.document_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the document.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.GetDocumentResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.GetDocumentResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ssm.GetParameterResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ssm.</code><code class="descname">GetParameterResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>name=None</em>, <em>type=None</em>, <em>value=None</em>, <em>version=None</em>, <em>with_decryption=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.GetParameterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getParameter.</p>
<dl class="attribute">
<dt id="pulumi_aws.ssm.GetParameterResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.GetParameterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ssm.MaintenanceWindow">
<em class="property">class </em><code class="descclassname">pulumi_aws.ssm.</code><code class="descname">MaintenanceWindow</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allow_unassociated_targets=None</em>, <em>cutoff=None</em>, <em>duration=None</em>, <em>enabled=None</em>, <em>end_date=None</em>, <em>name=None</em>, <em>schedule=None</em>, <em>schedule_timezone=None</em>, <em>start_date=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SSM Maintenance Window resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allow_unassociated_targets</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.</li>
<li><strong>cutoff</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.</li>
<li><strong>duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration of the Maintenance Window in hours.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the maintenance window is enabled. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Timestamp in <a class="reference external" href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO-8601 extended format</a> when to no longer run the maintenance window.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the maintenance window.</li>
<li><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The schedule of the Maintenance Window in the form of a <a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-cron.html">cron</a> or rate expression.</li>
<li><strong>schedule_timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Timezone for schedule in <a class="reference external" href="https://www.iana.org/time-zones">Internet Assigned Numbers Authority (IANA) Time Zone Database format</a>. For example: <code class="docutils literal notranslate"><span class="pre">America/Los_Angeles</span></code>, <code class="docutils literal notranslate"><span class="pre">etc/UTC</span></code>, or <code class="docutils literal notranslate"><span class="pre">Asia/Seoul</span></code>.</li>
<li><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Timestamp in <a class="reference external" href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO-8601 extended format</a> when to begin the maintenance window.</p>
</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_maintenance_window.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_maintenance_window.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.allow_unassociated_targets">
<code class="descname">allow_unassociated_targets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.allow_unassociated_targets" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.cutoff">
<code class="descname">cutoff</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.cutoff" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.duration">
<code class="descname">duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration of the Maintenance Window in hours.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the maintenance window is enabled. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.end_date">
<code class="descname">end_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.end_date" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in <a class="reference external" href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO-8601 extended format</a> when to no longer run the maintenance window.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the maintenance window.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.schedule">
<code class="descname">schedule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>The schedule of the Maintenance Window in the form of a <a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-cron.html">cron</a> or rate expression.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.schedule_timezone">
<code class="descname">schedule_timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.schedule_timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>Timezone for schedule in <a class="reference external" href="https://www.iana.org/time-zones">Internet Assigned Numbers Authority (IANA) Time Zone Database format</a>. For example: <code class="docutils literal notranslate"><span class="pre">America/Los_Angeles</span></code>, <code class="docutils literal notranslate"><span class="pre">etc/UTC</span></code>, or <code class="docutils literal notranslate"><span class="pre">Asia/Seoul</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.start_date">
<code class="descname">start_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.start_date" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in <a class="reference external" href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO-8601 extended format</a> when to begin the maintenance window.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindow.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.MaintenanceWindow.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.MaintenanceWindow.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindow.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget">
<em class="property">class </em><code class="descclassname">pulumi_aws.ssm.</code><code class="descname">MaintenanceWindowTarget</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>owner_information=None</em>, <em>resource_type=None</em>, <em>targets=None</em>, <em>window_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SSM Maintenance Window Target resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the maintenance window target.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the maintenance window target.</li>
<li><strong>owner_information</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.</li>
<li><strong>resource_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of target being registered with the Maintenance Window. Possible values <code class="docutils literal notranslate"><span class="pre">INSTANCE</span></code>.</li>
<li><strong>targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The targets (either instances or tags). Instances are specified using Key=InstanceIds,Values=InstanceId1,InstanceId2. Tags are specified using Key=tag name,Values=tag value.</li>
<li><strong>window_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of the maintenance window to register the target with.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_maintenance_window_target.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_maintenance_window_target.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the maintenance window target.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the maintenance window target.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget.owner_information">
<code class="descname">owner_information</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget.owner_information" title="Permalink to this definition">¶</a></dt>
<dd><p>User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget.resource_type">
<code class="descname">resource_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget.resource_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of target being registered with the Maintenance Window. Possible values <code class="docutils literal notranslate"><span class="pre">INSTANCE</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget.targets">
<code class="descname">targets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget.targets" title="Permalink to this definition">¶</a></dt>
<dd><p>The targets (either instances or tags). Instances are specified using Key=InstanceIds,Values=InstanceId1,InstanceId2. Tags are specified using Key=tag name,Values=tag value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget.window_id">
<code class="descname">window_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget.window_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of the maintenance window to register the target with.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.MaintenanceWindowTarget.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTarget.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask">
<em class="property">class </em><code class="descclassname">pulumi_aws.ssm.</code><code class="descname">MaintenanceWindowTask</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>logging_info=None</em>, <em>max_concurrency=None</em>, <em>max_errors=None</em>, <em>name=None</em>, <em>priority=None</em>, <em>service_role_arn=None</em>, <em>targets=None</em>, <em>task_arn=None</em>, <em>task_parameters=None</em>, <em>task_type=None</em>, <em>window_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SSM Maintenance Window Task resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the maintenance window task.</li>
<li><strong>logging_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A structure containing information about an Amazon S3 bucket to write instance-level logs to. Documented below.</li>
<li><strong>max_concurrency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum number of targets this task can be run for in parallel.</li>
<li><strong>max_errors</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum number of errors allowed before this task stops being scheduled.</li>
<li><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.</li>
<li><strong>service_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be assumed when executing the task.</li>
<li><strong>targets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.</li>
<li><strong>task_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the task to execute.</li>
<li><strong>task_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A structure containing information about parameters required by the particular <code class="docutils literal notranslate"><span class="pre">task_arn</span></code>. Documented below.</li>
<li><strong>task_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of task being registered. The only allowed value is <code class="docutils literal notranslate"><span class="pre">RUN_COMMAND</span></code>.</li>
<li><strong>window_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of the maintenance window to register the task with.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_maintenance_window_task.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_maintenance_window_task.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the maintenance window task.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.logging_info">
<code class="descname">logging_info</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.logging_info" title="Permalink to this definition">¶</a></dt>
<dd><p>A structure containing information about an Amazon S3 bucket to write instance-level logs to. Documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.max_concurrency">
<code class="descname">max_concurrency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.max_concurrency" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of targets this task can be run for in parallel.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.max_errors">
<code class="descname">max_errors</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.max_errors" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of errors allowed before this task stops being scheduled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.priority">
<code class="descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.service_role_arn">
<code class="descname">service_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.service_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be assumed when executing the task.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.targets">
<code class="descname">targets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.targets" title="Permalink to this definition">¶</a></dt>
<dd><p>The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.task_arn">
<code class="descname">task_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.task_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the task to execute.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.task_parameters">
<code class="descname">task_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.task_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A structure containing information about parameters required by the particular <code class="docutils literal notranslate"><span class="pre">task_arn</span></code>. Documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.task_type">
<code class="descname">task_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.task_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of task being registered. The only allowed value is <code class="docutils literal notranslate"><span class="pre">RUN_COMMAND</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.window_id">
<code class="descname">window_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.window_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of the maintenance window to register the task with.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.MaintenanceWindowTask.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.MaintenanceWindowTask.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ssm.Parameter">
<em class="property">class </em><code class="descclassname">pulumi_aws.ssm.</code><code class="descname">Parameter</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allowed_pattern=None</em>, <em>arn=None</em>, <em>description=None</em>, <em>key_id=None</em>, <em>name=None</em>, <em>overwrite=None</em>, <em>tags=None</em>, <em>tier=None</em>, <em>type=None</em>, <em>value=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Parameter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SSM Parameter resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allowed_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression used to validate the parameter value.</li>
<li><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the parameter.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the parameter.</li>
<li><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The KMS key id or arn for encrypting a SecureString.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the parameter. If the name contains a path (e.g. any forward slashes (<code class="docutils literal notranslate"><span class="pre">/</span></code>)), it must be fully qualified with a leading forward slash (<code class="docutils literal notranslate"><span class="pre">/</span></code>). For additional requirements and constraints, see the <a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-parameter-name-constraints.html">AWS SSM User Guide</a>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the object.</li>
<li><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tier of the parameter. If not specified, will default to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Valid tiers are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Advanced</span></code>. For more information on parameter tiers, see the <a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html">AWS SSM Parameter tier comparison and guide</a>.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the parameter. Valid types are <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">StringList</span></code> and <code class="docutils literal notranslate"><span class="pre">SecureString</span></code>.</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the parameter.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_parameter.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_parameter.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ssm.Parameter.allowed_pattern">
<code class="descname">allowed_pattern</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.allowed_pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>A regular expression used to validate the parameter value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Parameter.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the parameter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Parameter.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the parameter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Parameter.key_id">
<code class="descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The KMS key id or arn for encrypting a SecureString.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Parameter.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the parameter. If the name contains a path (e.g. any forward slashes (<code class="docutils literal notranslate"><span class="pre">/</span></code>)), it must be fully qualified with a leading forward slash (<code class="docutils literal notranslate"><span class="pre">/</span></code>). For additional requirements and constraints, see the <a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-parameter-name-constraints.html">AWS SSM User Guide</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Parameter.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Parameter.tier">
<code class="descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The tier of the parameter. If not specified, will default to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Valid tiers are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Advanced</span></code>. For more information on parameter tiers, see the <a class="reference external" href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html">AWS SSM Parameter tier comparison and guide</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Parameter.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the parameter. Valid types are <code class="docutils literal notranslate"><span class="pre">String</span></code>, <code class="docutils literal notranslate"><span class="pre">StringList</span></code> and <code class="docutils literal notranslate"><span class="pre">SecureString</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Parameter.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the parameter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.Parameter.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.Parameter.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the parameter.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.Parameter.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Parameter.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.Parameter.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.Parameter.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ssm.PatchBaseline">
<em class="property">class </em><code class="descclassname">pulumi_aws.ssm.</code><code class="descname">PatchBaseline</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>approval_rules=None</em>, <em>approved_patches=None</em>, <em>approved_patches_compliance_level=None</em>, <em>description=None</em>, <em>global_filters=None</em>, <em>name=None</em>, <em>operating_system=None</em>, <em>rejected_patches=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SSM Patch Baseline resource</p>
<blockquote>
<div><strong>NOTE on Patch Baselines:</strong> The <code class="docutils literal notranslate"><span class="pre">approved_patches</span></code> and <code class="docutils literal notranslate"><span class="pre">approval_rule</span></code> are 
both marked as optional fields, but the Patch Baseline requires that at least one
of them is specified.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>approval_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of rules used to include patches in the baseline. up to 10 approval rules can be specified. Each approval_rule block requires the fields documented below.</li>
<li><strong>approved_patches</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of explicitly approved patches for the baseline.</li>
<li><strong>approved_patches_compliance_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. Valid compliance levels include the following: <code class="docutils literal notranslate"><span class="pre">CRITICAL</span></code>, <code class="docutils literal notranslate"><span class="pre">HIGH</span></code>, <code class="docutils literal notranslate"><span class="pre">MEDIUM</span></code>, <code class="docutils literal notranslate"><span class="pre">LOW</span></code>, <code class="docutils literal notranslate"><span class="pre">INFORMATIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the patch baseline.</li>
<li><strong>global_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of global filters used to exclude patches from the baseline. Up to 4 global filters can be specified using Key/Value pairs. Valid Keys are <code class="docutils literal notranslate"><span class="pre">PRODUCT</span> <span class="pre">|</span> <span class="pre">CLASSIFICATION</span> <span class="pre">|</span> <span class="pre">MSRC_SEVERITY</span> <span class="pre">|</span> <span class="pre">PATCH_ID</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the patch baseline.</li>
<li><strong>operating_system</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the operating system the patch baseline applies to. Supported operating systems include <code class="docutils literal notranslate"><span class="pre">WINDOWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_LINUX</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_LINUX_2</span></code>, <code class="docutils literal notranslate"><span class="pre">SUSE</span></code>, <code class="docutils literal notranslate"><span class="pre">UBUNTU</span></code>, <code class="docutils literal notranslate"><span class="pre">CENTOS</span></code>, and <code class="docutils literal notranslate"><span class="pre">REDHAT_ENTERPRISE_LINUX</span></code>. The Default value is <code class="docutils literal notranslate"><span class="pre">WINDOWS</span></code>.</li>
<li><strong>rejected_patches</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of rejected patches.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_patch_baseline.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_patch_baseline.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ssm.PatchBaseline.approval_rules">
<code class="descname">approval_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.approval_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of rules used to include patches in the baseline. up to 10 approval rules can be specified. Each approval_rule block requires the fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.PatchBaseline.approved_patches">
<code class="descname">approved_patches</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.approved_patches" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of explicitly approved patches for the baseline.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.PatchBaseline.approved_patches_compliance_level">
<code class="descname">approved_patches_compliance_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.approved_patches_compliance_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. Valid compliance levels include the following: <code class="docutils literal notranslate"><span class="pre">CRITICAL</span></code>, <code class="docutils literal notranslate"><span class="pre">HIGH</span></code>, <code class="docutils literal notranslate"><span class="pre">MEDIUM</span></code>, <code class="docutils literal notranslate"><span class="pre">LOW</span></code>, <code class="docutils literal notranslate"><span class="pre">INFORMATIONAL</span></code>, <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">UNSPECIFIED</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.PatchBaseline.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the patch baseline.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.PatchBaseline.global_filters">
<code class="descname">global_filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.global_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of global filters used to exclude patches from the baseline. Up to 4 global filters can be specified using Key/Value pairs. Valid Keys are <code class="docutils literal notranslate"><span class="pre">PRODUCT</span> <span class="pre">|</span> <span class="pre">CLASSIFICATION</span> <span class="pre">|</span> <span class="pre">MSRC_SEVERITY</span> <span class="pre">|</span> <span class="pre">PATCH_ID</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.PatchBaseline.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the patch baseline.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.PatchBaseline.operating_system">
<code class="descname">operating_system</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.operating_system" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the operating system the patch baseline applies to. Supported operating systems include <code class="docutils literal notranslate"><span class="pre">WINDOWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_LINUX</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_LINUX_2</span></code>, <code class="docutils literal notranslate"><span class="pre">SUSE</span></code>, <code class="docutils literal notranslate"><span class="pre">UBUNTU</span></code>, <code class="docutils literal notranslate"><span class="pre">CENTOS</span></code>, and <code class="docutils literal notranslate"><span class="pre">REDHAT_ENTERPRISE_LINUX</span></code>. The Default value is <code class="docutils literal notranslate"><span class="pre">WINDOWS</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.PatchBaseline.rejected_patches">
<code class="descname">rejected_patches</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.rejected_patches" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of rejected patches.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.PatchBaseline.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.PatchBaseline.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.PatchBaseline.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ssm.PatchGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.ssm.</code><code class="descname">PatchGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>baseline_id=None</em>, <em>patch_group=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.PatchGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SSM Patch Group resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>baseline_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the patch baseline to register the patch group with.</li>
<li><strong>patch_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the patch group that should be registered with the patch baseline.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_patch_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_patch_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ssm.PatchGroup.baseline_id">
<code class="descname">baseline_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchGroup.baseline_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the patch baseline to register the patch group with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.PatchGroup.patch_group">
<code class="descname">patch_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.PatchGroup.patch_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the patch group that should be registered with the patch baseline.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.PatchGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.PatchGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.PatchGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.PatchGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ssm.ResourceDataSync">
<em class="property">class </em><code class="descclassname">pulumi_aws.ssm.</code><code class="descname">ResourceDataSync</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>s3_destination=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.ResourceDataSync" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a SSM resource data sync.</p>
<p><code class="docutils literal notranslate"><span class="pre">s3_destination</span></code> supports the following:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">bucket_name</span></code> - (Required) Name of S3 bucket where the aggregated data is stored.</li>
<li><code class="docutils literal notranslate"><span class="pre">region</span></code> - (Required) Region with the bucket targeted by the Resource Data Sync.</li>
<li><code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code> - (Optional) ARN of an encryption key for a destination in Amazon S3.</li>
<li><code class="docutils literal notranslate"><span class="pre">prefix</span></code> - (Optional) Prefix for the bucket.</li>
<li><code class="docutils literal notranslate"><span class="pre">sync_format</span></code> - (Optional) A supported sync format. Only JsonSerDe is currently supported. Defaults to JsonSerDe.</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name for the configuration.</li>
<li><strong>s3_destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Amazon S3 configuration details for the sync.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_resource_data_sync.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_resource_data_sync.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ssm.ResourceDataSync.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.ResourceDataSync.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name for the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ssm.ResourceDataSync.s3_destination">
<code class="descname">s3_destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ssm.ResourceDataSync.s3_destination" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon S3 configuration details for the sync.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.ResourceDataSync.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.ResourceDataSync.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ssm.ResourceDataSync.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.ResourceDataSync.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ssm.get_document">
<code class="descclassname">pulumi_aws.ssm.</code><code class="descname">get_document</code><span class="sig-paren">(</span><em>document_format=None</em>, <em>document_version=None</em>, <em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.get_document" title="Permalink to this definition">¶</a></dt>
<dd><p>Gets the contents of the specified Systems Manager document.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ssm_document.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ssm_document.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ssm.get_parameter">
<code class="descclassname">pulumi_aws.ssm.</code><code class="descname">get_parameter</code><span class="sig-paren">(</span><em>name=None</em>, <em>with_decryption=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ssm.get_parameter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SSM Parameter data source.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ssm_parameter.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ssm_parameter.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
