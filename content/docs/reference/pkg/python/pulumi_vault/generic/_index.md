---
title: Module generic
title_tag: Module generic | Package pulumi_vault | Python SDK
linktitle: generic
notitle: true
---

<div class="section" id="generic">
<h1>generic<a class="headerlink" href="#generic" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.generic"></span><dl class="class">
<dt id="pulumi_vault.generic.AwaitableGetSecretResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.generic.</code><code class="sig-name descname">AwaitableGetSecretResult</code><span class="sig-paren">(</span><em class="sig-param">data=None</em>, <em class="sig-param">data_json=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">lease_duration=None</em>, <em class="sig-param">lease_id=None</em>, <em class="sig-param">lease_renewable=None</em>, <em class="sig-param">lease_start_time=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.generic.AwaitableGetSecretResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_vault.generic.Endpoint">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.generic.</code><code class="sig-name descname">Endpoint</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">data_json=None</em>, <em class="sig-param">disable_delete=None</em>, <em class="sig-param">disable_read=None</em>, <em class="sig-param">ignore_absent_fields=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">write_fields=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.generic.Endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Endpoint resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] data_json: String containing a JSON-encoded object that will be</p>
<blockquote>
<div><p>written to the given path as the secret data.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>disable_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Don’t attempt to delete the path from Vault if true</p></li>
<li><p><strong>disable_read</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – True/false. Set this to true if your vault
authentication is not able to read the data or if the endpoint does
not support the <code class="docutils literal notranslate"><span class="pre">GET</span></code> method. Setting this to <code class="docutils literal notranslate"><span class="pre">true</span></code> will break drift
detection. You should set this to <code class="docutils literal notranslate"><span class="pre">true</span></code> for endpoints that are
write-only. Defaults to false.</p></li>
<li><p><strong>ignore_absent_fields</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When reading, disregard fields not present in data_json</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full logical path at which to write the given
data. Consult each backend’s documentation to see which endpoints
support the <code class="docutils literal notranslate"><span class="pre">PUT</span></code> methods and to determine whether they also support
<code class="docutils literal notranslate"><span class="pre">DELETE</span></code> and <code class="docutils literal notranslate"><span class="pre">GET</span></code>.</p></li>
<li><p><strong>write_fields</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Top-level fields returned by write to persist in state</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_vault.generic.Endpoint.data_json">
<code class="sig-name descname">data_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.generic.Endpoint.data_json" title="Permalink to this definition">¶</a></dt>
<dd><p>String containing a JSON-encoded object that will be
written to the given path as the secret data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.generic.Endpoint.disable_delete">
<code class="sig-name descname">disable_delete</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.generic.Endpoint.disable_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>Don’t attempt to delete the path from Vault if true</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.generic.Endpoint.disable_read">
<code class="sig-name descname">disable_read</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.generic.Endpoint.disable_read" title="Permalink to this definition">¶</a></dt>
<dd><p>True/false. Set this to true if your vault
authentication is not able to read the data or if the endpoint does
not support the <code class="docutils literal notranslate"><span class="pre">GET</span></code> method. Setting this to <code class="docutils literal notranslate"><span class="pre">true</span></code> will break drift
detection. You should set this to <code class="docutils literal notranslate"><span class="pre">true</span></code> for endpoints that are
write-only. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.generic.Endpoint.ignore_absent_fields">
<code class="sig-name descname">ignore_absent_fields</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.generic.Endpoint.ignore_absent_fields" title="Permalink to this definition">¶</a></dt>
<dd><p>When reading, disregard fields not present in data_json</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.generic.Endpoint.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.generic.Endpoint.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The full logical path at which to write the given
data. Consult each backend’s documentation to see which endpoints
support the <code class="docutils literal notranslate"><span class="pre">PUT</span></code> methods and to determine whether they also support
<code class="docutils literal notranslate"><span class="pre">DELETE</span></code> and <code class="docutils literal notranslate"><span class="pre">GET</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.generic.Endpoint.write_data">
<code class="sig-name descname">write_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.generic.Endpoint.write_data" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of strings returned by write operation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.generic.Endpoint.write_data_json">
<code class="sig-name descname">write_data_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.generic.Endpoint.write_data_json" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON data returned by write operation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.generic.Endpoint.write_fields">
<code class="sig-name descname">write_fields</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.generic.Endpoint.write_fields" title="Permalink to this definition">¶</a></dt>
<dd><p>Top-level fields returned by write to persist in state</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.generic.Endpoint.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">data_json=None</em>, <em class="sig-param">disable_delete=None</em>, <em class="sig-param">disable_read=None</em>, <em class="sig-param">ignore_absent_fields=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">write_data=None</em>, <em class="sig-param">write_data_json=None</em>, <em class="sig-param">write_fields=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.generic.Endpoint.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Endpoint resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String containing a JSON-encoded object that will be
written to the given path as the secret data.</p></li>
<li><p><strong>disable_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Don’t attempt to delete the path from Vault if true</p></li>
<li><p><strong>disable_read</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – True/false. Set this to true if your vault
authentication is not able to read the data or if the endpoint does
not support the <code class="docutils literal notranslate"><span class="pre">GET</span></code> method. Setting this to <code class="docutils literal notranslate"><span class="pre">true</span></code> will break drift
detection. You should set this to <code class="docutils literal notranslate"><span class="pre">true</span></code> for endpoints that are
write-only. Defaults to false.</p></li>
<li><p><strong>ignore_absent_fields</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When reading, disregard fields not present in data_json</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full logical path at which to write the given
data. Consult each backend’s documentation to see which endpoints
support the <code class="docutils literal notranslate"><span class="pre">PUT</span></code> methods and to determine whether they also support
<code class="docutils literal notranslate"><span class="pre">DELETE</span></code> and <code class="docutils literal notranslate"><span class="pre">GET</span></code>.</p></li>
<li><p><strong>write_data</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of strings returned by write operation</p></li>
<li><p><strong>write_data_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON data returned by write operation</p></li>
<li><p><strong>write_fields</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Top-level fields returned by write to persist in state</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.generic.Endpoint.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.generic.Endpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.generic.Endpoint.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.generic.Endpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_vault.generic.GetSecretResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.generic.</code><code class="sig-name descname">GetSecretResult</code><span class="sig-paren">(</span><em class="sig-param">data=None</em>, <em class="sig-param">data_json=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">lease_duration=None</em>, <em class="sig-param">lease_id=None</em>, <em class="sig-param">lease_renewable=None</em>, <em class="sig-param">lease_start_time=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.generic.GetSecretResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecret.</p>
<dl class="attribute">
<dt id="pulumi_vault.generic.GetSecretResult.data">
<code class="sig-name descname">data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.generic.GetSecretResult.data" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping whose keys are the top-level data keys returned from
Vault and whose values are the corresponding values. This map can only
represent string data, so any non-string values returned from Vault are
serialized as JSON.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.generic.GetSecretResult.data_json">
<code class="sig-name descname">data_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.generic.GetSecretResult.data_json" title="Permalink to this definition">¶</a></dt>
<dd><p>A string containing the full data payload retrieved from
Vault, serialized in JSON format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.generic.GetSecretResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.generic.GetSecretResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.generic.GetSecretResult.lease_duration">
<code class="sig-name descname">lease_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.generic.GetSecretResult.lease_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration of the secret lease, in seconds relative
to the time the data was requested. Once this time has passed any plan
generated with this data may fail to apply.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.generic.GetSecretResult.lease_id">
<code class="sig-name descname">lease_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.generic.GetSecretResult.lease_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The lease identifier assigned by Vault, if any.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_vault.generic.Secret">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.generic.</code><code class="sig-name descname">Secret</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">data_json=None</em>, <em class="sig-param">disable_read=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.generic.Secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Secret resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] data_json: String containing a JSON-encoded object that will be</p>
<blockquote>
<div><p>written as the secret data at the given path.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>disable_read</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – True/false. Set this to true if your vault
authentication is not able to read the data. Setting this to <code class="docutils literal notranslate"><span class="pre">true</span></code> will
break drift detection. Defaults to false.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full logical path at which to write the given data.
To write data into the “generic” secret backend mounted in Vault by default,
this should be prefixed with <code class="docutils literal notranslate"><span class="pre">secret/</span></code>. Writing to other backends with this
resource is possible; consult each backend’s documentation to see which
endpoints support the <code class="docutils literal notranslate"><span class="pre">PUT</span></code> and <code class="docutils literal notranslate"><span class="pre">DELETE</span></code> methods.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_vault.generic.Secret.data">
<code class="sig-name descname">data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.generic.Secret.data" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping whose keys are the top-level data keys returned from
Vault and whose values are the corresponding values. This map can only
represent string data, so any non-string values returned from Vault are
serialized as JSON.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.generic.Secret.data_json">
<code class="sig-name descname">data_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.generic.Secret.data_json" title="Permalink to this definition">¶</a></dt>
<dd><p>String containing a JSON-encoded object that will be
written as the secret data at the given path.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.generic.Secret.disable_read">
<code class="sig-name descname">disable_read</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.generic.Secret.disable_read" title="Permalink to this definition">¶</a></dt>
<dd><p>True/false. Set this to true if your vault
authentication is not able to read the data. Setting this to <code class="docutils literal notranslate"><span class="pre">true</span></code> will
break drift detection. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.generic.Secret.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.generic.Secret.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The full logical path at which to write the given data.
To write data into the “generic” secret backend mounted in Vault by default,
this should be prefixed with <code class="docutils literal notranslate"><span class="pre">secret/</span></code>. Writing to other backends with this
resource is possible; consult each backend’s documentation to see which
endpoints support the <code class="docutils literal notranslate"><span class="pre">PUT</span></code> and <code class="docutils literal notranslate"><span class="pre">DELETE</span></code> methods.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.generic.Secret.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">data=None</em>, <em class="sig-param">data_json=None</em>, <em class="sig-param">disable_read=None</em>, <em class="sig-param">path=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.generic.Secret.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Secret resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping whose keys are the top-level data keys returned from
Vault and whose values are the corresponding values. This map can only
represent string data, so any non-string values returned from Vault are
serialized as JSON.</p></li>
<li><p><strong>data_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String containing a JSON-encoded object that will be
written as the secret data at the given path.</p></li>
<li><p><strong>disable_read</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – True/false. Set this to true if your vault
authentication is not able to read the data. Setting this to <code class="docutils literal notranslate"><span class="pre">true</span></code> will
break drift detection. Defaults to false.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full logical path at which to write the given data.
To write data into the “generic” secret backend mounted in Vault by default,
this should be prefixed with <code class="docutils literal notranslate"><span class="pre">secret/</span></code>. Writing to other backends with this
resource is possible; consult each backend’s documentation to see which
endpoints support the <code class="docutils literal notranslate"><span class="pre">PUT</span></code> and <code class="docutils literal notranslate"><span class="pre">DELETE</span></code> methods.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.generic.Secret.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.generic.Secret.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.generic.Secret.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.generic.Secret.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_vault.generic.get_secret">
<code class="sig-prename descclassname">pulumi_vault.generic.</code><code class="sig-name descname">get_secret</code><span class="sig-paren">(</span><em class="sig-param">path=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.generic.get_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>path</strong> (<em>str</em>) – The full logical path from which to request data.
To read data from the “generic” secret backend mounted in Vault by
default, this should be prefixed with <code class="docutils literal notranslate"><span class="pre">secret/</span></code>. Reading from other backends
with this data source is possible; consult each backend’s documentation
to see which endpoints support the <code class="docutils literal notranslate"><span class="pre">GET</span></code> method.</p>
</dd>
</dl>
</dd></dl>

</div>
