---
title: Module apimanagement
title_tag: Module apimanagement | Package pulumi_azure | Python SDK
linktitle: apimanagement
notitle: true
---

<div class="section" id="apimanagement">
<h1>apimanagement<a class="headerlink" href="#apimanagement" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.apimanagement"></span><dl class="class">
<dt id="pulumi_azure.apimanagement.Api">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">Api</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">import_=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">protocols=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">revision=None</em>, <em class="sig-param">service_url=None</em>, <em class="sig-param">soap_pass_through=None</em>, <em class="sig-param">subscription_key_parameter_names=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">version_set_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Api" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API within an API Management Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this API should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the API Management API, which may include HTML formatting tags.</p></li>
<li><p><strong>display*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The display name of the API.</p>
</p></li>
</ul>
</dd>
</dl>
<p>:param pulumi.Input[dict] import*: A <code class="docutils literal notranslate"><span class="pre">import</span></code> block as documented below.
:param pulumi.Input[str] name: The name of the API Management API. Changing this forces a new resource to be created.
:param pulumi.Input[str] path: The Path for this API Management API, which is a relative URL which uniquely identifies this API and all of it’s resource paths within the API Management Service.
:param pulumi.Input[list] protocols: A list of protocols the operations in this API can be invoked. Possible values are <code class="docutils literal notranslate"><span class="pre">http</span></code> and <code class="docutils literal notranslate"><span class="pre">https</span></code>.
:param pulumi.Input[str] resource_group_name: The Name of the Resource Group where the API Management API exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] revision: The Revision which used for this API.
:param pulumi.Input[str] service_url: Absolute URL of the backend service implementing this API.
:param pulumi.Input[bool] soap_pass_through: Should this API expose a SOAP frontend, rather than a HTTP frontend? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[dict] subscription_key_parameter_names: A <code class="docutils literal notranslate"><span class="pre">subscription_key_parameter_names</span></code> block as documented below.
:param pulumi.Input[str] version: The Version number of this API, if this API is versioned.
:param pulumi.Input[str] version_set_id: The ID of the Version Set which this API is associated with.</p>
<p>The <strong>import_</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The format of the content from which the API Definition should be imported. Possible values are: <code class="docutils literal notranslate"><span class="pre">swagger-json</span></code>, <code class="docutils literal notranslate"><span class="pre">swagger-link-json</span></code>, <code class="docutils literal notranslate"><span class="pre">wadl-link-json</span></code>, <code class="docutils literal notranslate"><span class="pre">wadl-xml</span></code>, <code class="docutils literal notranslate"><span class="pre">wsdl</span></code> and <code class="docutils literal notranslate"><span class="pre">wsdl-link</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Content from which the API Definition should be imported. When a <code class="docutils literal notranslate"><span class="pre">content_format</span></code> of <code class="docutils literal notranslate"><span class="pre">*-link-*</span></code> is specified this must be a URL, otherwise this must be defined inline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wsdlSelector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">wsdl_selector</span></code> block as defined below, which allows you to limit the import of a WSDL to only a subset of the document. This can only be specified when <code class="docutils literal notranslate"><span class="pre">content_format</span></code> is <code class="docutils literal notranslate"><span class="pre">wsdl</span></code> or <code class="docutils literal notranslate"><span class="pre">wsdl-link</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">endpointName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of endpoint (port) to import from WSDL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of service to import from WSDL.</p></li>
</ul>
</li>
</ul>
<p>The <strong>subscription_key_parameter_names</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">header</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the HTTP Header which should be used for the Subscription Key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the QueryString parameter which should be used for the Subscription Key.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Service where this API should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the API Management API, which may include HTML formatting tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.import_">
<code class="sig-name descname">import_</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.import_" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">import</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The format of the content from which the API Definition should be imported. Possible values are: <code class="docutils literal notranslate"><span class="pre">swagger-json</span></code>, <code class="docutils literal notranslate"><span class="pre">swagger-link-json</span></code>, <code class="docutils literal notranslate"><span class="pre">wadl-link-json</span></code>, <code class="docutils literal notranslate"><span class="pre">wadl-xml</span></code>, <code class="docutils literal notranslate"><span class="pre">wsdl</span></code> and <code class="docutils literal notranslate"><span class="pre">wsdl-link</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Content from which the API Definition should be imported. When a <code class="docutils literal notranslate"><span class="pre">content_format</span></code> of <code class="docutils literal notranslate"><span class="pre">*-link-*</span></code> is specified this must be a URL, otherwise this must be defined inline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wsdlSelector</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">wsdl_selector</span></code> block as defined below, which allows you to limit the import of a WSDL to only a subset of the document. This can only be specified when <code class="docutils literal notranslate"><span class="pre">content_format</span></code> is <code class="docutils literal notranslate"><span class="pre">wsdl</span></code> or <code class="docutils literal notranslate"><span class="pre">wsdl-link</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">endpointName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of endpoint (port) to import from WSDL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of service to import from WSDL.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.is_current">
<code class="sig-name descname">is_current</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.is_current" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this the current API Revision?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.is_online">
<code class="sig-name descname">is_online</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.is_online" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this API Revision online/accessible via the Gateway?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management API. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The Path for this API Management API, which is a relative URL which uniquely identifies this API and all of it’s resource paths within the API Management Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.protocols">
<code class="sig-name descname">protocols</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.protocols" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of protocols the operations in this API can be invoked. Possible values are <code class="docutils literal notranslate"><span class="pre">http</span></code> and <code class="docutils literal notranslate"><span class="pre">https</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Resource Group where the API Management API exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.revision">
<code class="sig-name descname">revision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.revision" title="Permalink to this definition">¶</a></dt>
<dd><p>The Revision which used for this API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.service_url">
<code class="sig-name descname">service_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.service_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Absolute URL of the backend service implementing this API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.soap_pass_through">
<code class="sig-name descname">soap_pass_through</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.soap_pass_through" title="Permalink to this definition">¶</a></dt>
<dd><p>Should this API expose a SOAP frontend, rather than a HTTP frontend? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.subscription_key_parameter_names">
<code class="sig-name descname">subscription_key_parameter_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.subscription_key_parameter_names" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">subscription_key_parameter_names</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">header</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the HTTP Header which should be used for the Subscription Key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the QueryString parameter which should be used for the Subscription Key.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The Version number of this API, if this API is versioned.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Api.version_set_id">
<code class="sig-name descname">version_set_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Api.version_set_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Version Set which this API is associated with.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Api.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">import_=None</em>, <em class="sig-param">is_current=None</em>, <em class="sig-param">is_online=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">protocols=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">revision=None</em>, <em class="sig-param">service_url=None</em>, <em class="sig-param">soap_pass_through=None</em>, <em class="sig-param">subscription_key_parameter_names=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">version_set_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Api.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Api resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this API should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the API Management API, which may include HTML formatting tags.</p></li>
<li><p><strong>display*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The display name of the API.</p>
</p></li>
</ul>
</dd>
</dl>
<p>:param pulumi.Input[dict] import*: A <code class="docutils literal notranslate"><span class="pre">import</span></code> block as documented below.
:param pulumi.Input[bool] is_current: Is this the current API Revision?
:param pulumi.Input[bool] is_online: Is this API Revision online/accessible via the Gateway?
:param pulumi.Input[str] name: The name of the API Management API. Changing this forces a new resource to be created.
:param pulumi.Input[str] path: The Path for this API Management API, which is a relative URL which uniquely identifies this API and all of it’s resource paths within the API Management Service.
:param pulumi.Input[list] protocols: A list of protocols the operations in this API can be invoked. Possible values are <code class="docutils literal notranslate"><span class="pre">http</span></code> and <code class="docutils literal notranslate"><span class="pre">https</span></code>.
:param pulumi.Input[str] resource_group_name: The Name of the Resource Group where the API Management API exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] revision: The Revision which used for this API.
:param pulumi.Input[str] service_url: Absolute URL of the backend service implementing this API.
:param pulumi.Input[bool] soap_pass_through: Should this API expose a SOAP frontend, rather than a HTTP frontend? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[dict] subscription_key_parameter_names: A <code class="docutils literal notranslate"><span class="pre">subscription_key_parameter_names</span></code> block as documented below.
:param pulumi.Input[str] version: The Version number of this API, if this API is versioned.
:param pulumi.Input[str] version_set_id: The ID of the Version Set which this API is associated with.</p>
<p>The <strong>import_</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The format of the content from which the API Definition should be imported. Possible values are: <code class="docutils literal notranslate"><span class="pre">swagger-json</span></code>, <code class="docutils literal notranslate"><span class="pre">swagger-link-json</span></code>, <code class="docutils literal notranslate"><span class="pre">wadl-link-json</span></code>, <code class="docutils literal notranslate"><span class="pre">wadl-xml</span></code>, <code class="docutils literal notranslate"><span class="pre">wsdl</span></code> and <code class="docutils literal notranslate"><span class="pre">wsdl-link</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Content from which the API Definition should be imported. When a <code class="docutils literal notranslate"><span class="pre">content_format</span></code> of <code class="docutils literal notranslate"><span class="pre">*-link-*</span></code> is specified this must be a URL, otherwise this must be defined inline.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wsdlSelector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">wsdl_selector</span></code> block as defined below, which allows you to limit the import of a WSDL to only a subset of the document. This can only be specified when <code class="docutils literal notranslate"><span class="pre">content_format</span></code> is <code class="docutils literal notranslate"><span class="pre">wsdl</span></code> or <code class="docutils literal notranslate"><span class="pre">wsdl-link</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">endpointName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of endpoint (port) to import from WSDL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of service to import from WSDL.</p></li>
</ul>
</li>
</ul>
<p>The <strong>subscription_key_parameter_names</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">header</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the HTTP Header which should be used for the Subscription Key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the QueryString parameter which should be used for the Subscription Key.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Api.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Api.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Api.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Api.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiOperation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">ApiOperation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">api_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">method=None</em>, <em class="sig-param">operation_id=None</em>, <em class="sig-param">request=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">responses=None</em>, <em class="sig-param">template_parameters=None</em>, <em class="sig-param">url_template=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Operation within an API Management Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>api_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API within the API Management Service where this API Operation should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this API Operation, which may include HTML formatting tags.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Display Name for this API Management Operation.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP Method used for this API Management Operation, like <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code> or <code class="docutils literal notranslate"><span class="pre">POST</span></code> - but not limited to these values.</p></li>
<li><p><strong>operation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique identifier for this API Operation. Changing this forces a new resource to be created.</p></li>
<li><p><strong>request</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">request</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>responses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">response</span></code> blocks as defined below.</p></li>
<li><p><strong>template_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">template_parameter</span></code> blocks as defined below.</p></li>
<li><p><strong>url_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The relative URL Template identifying the target resource for this operation, which may include parameters.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>request</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of the HTTP Request, which may include HTML tags.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">header</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value for this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Header Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of this Header, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more acceptable values for this Header.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">query_parameter</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value for this Query Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of this Query Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of this Query Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Query Parameter Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of this Query Parameter, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more acceptable values for this Query Parameter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">representations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">representation</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Content Type of this representation, such as <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">form_parameter</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value for this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Form Parameter Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of this Form Parameter, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more acceptable values for this Form Parameter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sample</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An example of this representation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schema_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of an API Management Schema which represents this Response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">typeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type Name defined by the Schema.</p></li>
</ul>
</li>
</ul>
<p>The <strong>responses</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of the HTTP Response, which may include HTML tags.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">header</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value for this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Header Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of this Header, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more acceptable values for this Header.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">representations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">representation</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Content Type of this representation, such as <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">form_parameter</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value for this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Form Parameter Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of this Form Parameter, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more acceptable values for this Form Parameter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sample</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An example of this representation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schema_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of an API Management Schema which represents this Response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">typeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type Name defined by the Schema.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTP Status Code.</p></li>
</ul>
<p>The <strong>template_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value for this Template Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of this Template Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of this Template Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Template Parameter Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of this Template Parameter, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more acceptable values for this Template Parameter.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.api_name">
<code class="sig-name descname">api_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.api_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API within the API Management Service where this API Operation should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for this API Operation, which may include HTML formatting tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Display Name for this API Management Operation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.method">
<code class="sig-name descname">method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.method" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP Method used for this API Management Operation, like <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code> or <code class="docutils literal notranslate"><span class="pre">POST</span></code> - but not limited to these values.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.operation_id">
<code class="sig-name descname">operation_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.operation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique identifier for this API Operation. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.request">
<code class="sig-name descname">request</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.request" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">request</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A description of the HTTP Request, which may include HTML tags.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">header</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The default value for this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A description of this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name of this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this Header Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of this Header, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more acceptable values for this Header.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">query_parameter</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The default value for this Query Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A description of this Query Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name of this Query Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this Query Parameter Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of this Query Parameter, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more acceptable values for this Query Parameter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">representations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">representation</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Content Type of this representation, such as <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">form_parameter</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The default value for this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A description of this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name of this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this Form Parameter Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of this Form Parameter, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more acceptable values for this Form Parameter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sample</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An example of this representation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schema_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of an API Management Schema which represents this Response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">typeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type Name defined by the Schema.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.responses">
<code class="sig-name descname">responses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.responses" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">response</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A description of the HTTP Response, which may include HTML tags.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">header</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The default value for this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A description of this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name of this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this Header Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of this Header, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more acceptable values for this Header.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">representations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">representation</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Content Type of this representation, such as <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">form_parameter</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The default value for this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A description of this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name of this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this Form Parameter Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of this Form Parameter, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more acceptable values for this Form Parameter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sample</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An example of this representation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schema_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of an API Management Schema which represents this Response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">typeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type Name defined by the Schema.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCode</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The HTTP Status Code.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.template_parameters">
<code class="sig-name descname">template_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.template_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">template_parameter</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The default value for this Template Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A description of this Template Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name of this Template Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this Template Parameter Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of this Template Parameter, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more acceptable values for this Template Parameter.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperation.url_template">
<code class="sig-name descname">url_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.url_template" title="Permalink to this definition">¶</a></dt>
<dd><p>The relative URL Template identifying the target resource for this operation, which may include parameters.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ApiOperation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">api_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">method=None</em>, <em class="sig-param">operation_id=None</em>, <em class="sig-param">request=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">responses=None</em>, <em class="sig-param">template_parameters=None</em>, <em class="sig-param">url_template=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApiOperation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>api_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API within the API Management Service where this API Operation should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this API Operation, which may include HTML formatting tags.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Display Name for this API Management Operation.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP Method used for this API Management Operation, like <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code> or <code class="docutils literal notranslate"><span class="pre">POST</span></code> - but not limited to these values.</p></li>
<li><p><strong>operation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique identifier for this API Operation. Changing this forces a new resource to be created.</p></li>
<li><p><strong>request</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">request</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>responses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">response</span></code> blocks as defined below.</p></li>
<li><p><strong>template_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">template_parameter</span></code> blocks as defined below.</p></li>
<li><p><strong>url_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The relative URL Template identifying the target resource for this operation, which may include parameters.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>request</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of the HTTP Request, which may include HTML tags.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">header</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value for this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Header Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of this Header, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more acceptable values for this Header.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">query_parameter</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value for this Query Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of this Query Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of this Query Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Query Parameter Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of this Query Parameter, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more acceptable values for this Query Parameter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">representations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">representation</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Content Type of this representation, such as <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">form_parameter</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value for this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Form Parameter Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of this Form Parameter, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more acceptable values for this Form Parameter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sample</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An example of this representation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schema_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of an API Management Schema which represents this Response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">typeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type Name defined by the Schema.</p></li>
</ul>
</li>
</ul>
<p>The <strong>responses</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of the HTTP Response, which may include HTML tags.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">header</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value for this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of this Header.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Header Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of this Header, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more acceptable values for this Header.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">representations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">representation</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">content_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Content Type of this representation, such as <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formParameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">form_parameter</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value for this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of this Form Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Form Parameter Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of this Form Parameter, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more acceptable values for this Form Parameter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sample</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An example of this representation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schema_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of an API Management Schema which represents this Response.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">typeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type Name defined by the Schema.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTP Status Code.</p></li>
</ul>
<p>The <strong>template_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value for this Template Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description of this Template Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of this Template Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">required</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this Template Parameter Required?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of this Template Parameter, such as a <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more acceptable values for this Template Parameter.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ApiOperation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiOperation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiOperationPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">ApiOperationPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">api_name=None</em>, <em class="sig-param">operation_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">xml_content=None</em>, <em class="sig-param">xml_link=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperationPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management API Operation Policy</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>api_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management API Operation within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>xml_content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The XML Content for this Policy.</p></li>
<li><p><strong>xml_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A link to a Policy XML Document, which must be publicly available.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperationPolicy.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperationPolicy.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperationPolicy.api_name">
<code class="sig-name descname">api_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperationPolicy.api_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the API Management API Operation within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperationPolicy.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperationPolicy.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperationPolicy.xml_content">
<code class="sig-name descname">xml_content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperationPolicy.xml_content" title="Permalink to this definition">¶</a></dt>
<dd><p>The XML Content for this Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiOperationPolicy.xml_link">
<code class="sig-name descname">xml_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperationPolicy.xml_link" title="Permalink to this definition">¶</a></dt>
<dd><p>A link to a Policy XML Document, which must be publicly available.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ApiOperationPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">api_name=None</em>, <em class="sig-param">operation_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">xml_content=None</em>, <em class="sig-param">xml_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperationPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApiOperationPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>api_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management API Operation within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>xml_content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The XML Content for this Policy.</p></li>
<li><p><strong>xml_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A link to a Policy XML Document, which must be publicly available.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ApiOperationPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperationPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiOperationPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiOperationPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">ApiPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">api_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">xml_content=None</em>, <em class="sig-param">xml_link=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management API Policy</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>api_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management API within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>xml_content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The XML Content for this Policy as a string.</p></li>
<li><p><strong>xml_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A link to a Policy XML Document, which must be publicly available.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiPolicy.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiPolicy.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiPolicy.api_name">
<code class="sig-name descname">api_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiPolicy.api_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the API Management API within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiPolicy.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiPolicy.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiPolicy.xml_content">
<code class="sig-name descname">xml_content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiPolicy.xml_content" title="Permalink to this definition">¶</a></dt>
<dd><p>The XML Content for this Policy as a string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiPolicy.xml_link">
<code class="sig-name descname">xml_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiPolicy.xml_link" title="Permalink to this definition">¶</a></dt>
<dd><p>A link to a Policy XML Document, which must be publicly available.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ApiPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">api_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">xml_content=None</em>, <em class="sig-param">xml_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApiPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>api_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management API within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>xml_content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The XML Content for this Policy as a string.</p></li>
<li><p><strong>xml_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A link to a Policy XML Document, which must be publicly available.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ApiPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiSchema">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">ApiSchema</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">api_name=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">schema_id=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Schema within an API Management Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>api_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API within the API Management Service where this API Schema should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content type of the API Schema.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>schema_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique identifier for this API Schema. Changing this forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JSON escaped string defining the document representing the Schema.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiSchema.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiSchema.api_name">
<code class="sig-name descname">api_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema.api_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API within the API Management Service where this API Schema should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiSchema.content_type">
<code class="sig-name descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The content type of the API Schema.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiSchema.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiSchema.schema_id">
<code class="sig-name descname">schema_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema.schema_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique identifier for this API Schema. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiSchema.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The JSON escaped string defining the document representing the Schema.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ApiSchema.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">api_name=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">schema_id=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApiSchema resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where the API exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>api_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API within the API Management Service where this API Schema should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content type of the API Schema.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>schema_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique identifier for this API Schema. Changing this forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JSON escaped string defining the document representing the Schema.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ApiSchema.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiSchema.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiSchema.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiVersionSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">ApiVersionSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">version_header_name=None</em>, <em class="sig-param">version_query_name=None</em>, <em class="sig-param">versioning_scheme=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Version Set within an API Management Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which the API Version Set should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of API Version Set.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of this API Version Set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Version Set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the parent API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>version_header_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Header which should be read from Inbound Requests which defines the API Version.</p></li>
<li><p><strong>version_query_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Query String which should be read from Inbound Requests which defines the API Version.</p></li>
<li><p><strong>versioning_scheme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies where in an Inbound HTTP Request that the API Version should be read from. Possible values are <code class="docutils literal notranslate"><span class="pre">Header</span></code>, <code class="docutils literal notranslate"><span class="pre">Query</span></code> and <code class="docutils literal notranslate"><span class="pre">Segment</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service in which the API Version Set should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of API Version Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of this API Version Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Version Set. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the parent API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.version_header_name">
<code class="sig-name descname">version_header_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.version_header_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Header which should be read from Inbound Requests which defines the API Version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.version_query_name">
<code class="sig-name descname">version_query_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.version_query_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Query String which should be read from Inbound Requests which defines the API Version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.versioning_scheme">
<code class="sig-name descname">versioning_scheme</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.versioning_scheme" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies where in an Inbound HTTP Request that the API Version should be read from. Possible values are <code class="docutils literal notranslate"><span class="pre">Header</span></code>, <code class="docutils literal notranslate"><span class="pre">Query</span></code> and <code class="docutils literal notranslate"><span class="pre">Segment</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">version_header_name=None</em>, <em class="sig-param">version_query_name=None</em>, <em class="sig-param">versioning_scheme=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApiVersionSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which the API Version Set should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of API Version Set.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of this API Version Set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Version Set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the parent API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>version_header_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Header which should be read from Inbound Requests which defines the API Version.</p></li>
<li><p><strong>version_query_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Query String which should be read from Inbound Requests which defines the API Version.</p></li>
<li><p><strong>versioning_scheme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies where in an Inbound HTTP Request that the API Version should be read from. Possible values are <code class="docutils literal notranslate"><span class="pre">Header</span></code>, <code class="docutils literal notranslate"><span class="pre">Query</span></code> and <code class="docutils literal notranslate"><span class="pre">Segment</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ApiVersionSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ApiVersionSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ApiVersionSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.AuthorizationServer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">AuthorizationServer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">authorization_endpoint=None</em>, <em class="sig-param">authorization_methods=None</em>, <em class="sig-param">bearer_token_sending_methods=None</em>, <em class="sig-param">client_authentication_methods=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_registration_endpoint=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">default_scope=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">grant_types=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">resource_owner_password=None</em>, <em class="sig-param">resource_owner_username=None</em>, <em class="sig-param">support_state=None</em>, <em class="sig-param">token_body_parameters=None</em>, <em class="sig-param">token_endpoint=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Authorization Server within an API Management Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which this Authorization Server should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>authorization_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OAUTH Authorization Endpoint.</p></li>
<li><p><strong>authorization_methods</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The HTTP Verbs supported by the Authorization Endpoint. Possible values are <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code> and <code class="docutils literal notranslate"><span class="pre">TRACE</span></code>.</p></li>
<li><p><strong>bearer_token_sending_methods</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The mechanism by which Access Tokens are passed to the API. Possible values are <code class="docutils literal notranslate"><span class="pre">authorizationHeader</span></code> and <code class="docutils literal notranslate"><span class="pre">query</span></code>.</p></li>
<li><p><strong>client_authentication_methods</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The Authentication Methods supported by the Token endpoint of this Authorization Server.. Possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Body</span></code>.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Client/App ID registered with this Authorization Server.</p></li>
<li><p><strong>client_registration_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of page where Client/App Registration is performed for this Authorization Server.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Client/App Secret registered with this Authorization Server.</p></li>
<li><p><strong>default_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Default Scope used when requesting an Access Token, specified as a string containing space-delimited values.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the Authorization Server, which may contain HTML formatting tags.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user-friendly name of this Authorization Server.</p></li>
<li><p><strong>grant_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Form of Authorization Grants required when requesting an Access Token. Possible values are <code class="docutils literal notranslate"><span class="pre">authorizationCode</span></code>, <code class="docutils literal notranslate"><span class="pre">clientCredentials</span></code>, <code class="docutils literal notranslate"><span class="pre">implicit</span></code> and <code class="docutils literal notranslate"><span class="pre">resourceOwnerPassword</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this Authorization Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_owner_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password associated with the Resource Owner.</p></li>
<li><p><strong>resource_owner_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username associated with the Resource Owner.</p></li>
<li><p><strong>support_state</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Server support State? If this is set to <code class="docutils literal notranslate"><span class="pre">true</span></code> the client may use the state parameter to raise protocol security.</p></li>
<li><p><strong>token_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OAUTH Token Endpoint.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>token_body_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of the Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Value of the Parameter.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service in which this Authorization Server should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.authorization_endpoint">
<code class="sig-name descname">authorization_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.authorization_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The OAUTH Authorization Endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.authorization_methods">
<code class="sig-name descname">authorization_methods</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.authorization_methods" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP Verbs supported by the Authorization Endpoint. Possible values are <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code> and <code class="docutils literal notranslate"><span class="pre">TRACE</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.bearer_token_sending_methods">
<code class="sig-name descname">bearer_token_sending_methods</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.bearer_token_sending_methods" title="Permalink to this definition">¶</a></dt>
<dd><p>The mechanism by which Access Tokens are passed to the API. Possible values are <code class="docutils literal notranslate"><span class="pre">authorizationHeader</span></code> and <code class="docutils literal notranslate"><span class="pre">query</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.client_authentication_methods">
<code class="sig-name descname">client_authentication_methods</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.client_authentication_methods" title="Permalink to this definition">¶</a></dt>
<dd><p>The Authentication Methods supported by the Token endpoint of this Authorization Server.. Possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Body</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Client/App ID registered with this Authorization Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.client_registration_endpoint">
<code class="sig-name descname">client_registration_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.client_registration_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of page where Client/App Registration is performed for this Authorization Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The Client/App Secret registered with this Authorization Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.default_scope">
<code class="sig-name descname">default_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.default_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The Default Scope used when requesting an Access Token, specified as a string containing space-delimited values.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the Authorization Server, which may contain HTML formatting tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The user-friendly name of this Authorization Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.grant_types">
<code class="sig-name descname">grant_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.grant_types" title="Permalink to this definition">¶</a></dt>
<dd><p>Form of Authorization Grants required when requesting an Access Token. Possible values are <code class="docutils literal notranslate"><span class="pre">authorizationCode</span></code>, <code class="docutils literal notranslate"><span class="pre">clientCredentials</span></code>, <code class="docutils literal notranslate"><span class="pre">implicit</span></code> and <code class="docutils literal notranslate"><span class="pre">resourceOwnerPassword</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this Authorization Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.resource_owner_password">
<code class="sig-name descname">resource_owner_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.resource_owner_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password associated with the Resource Owner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.resource_owner_username">
<code class="sig-name descname">resource_owner_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.resource_owner_username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username associated with the Resource Owner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.support_state">
<code class="sig-name descname">support_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.support_state" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Server support State? If this is set to <code class="docutils literal notranslate"><span class="pre">true</span></code> the client may use the state parameter to raise protocol security.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.token_endpoint">
<code class="sig-name descname">token_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.token_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The OAUTH Token Endpoint.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">authorization_endpoint=None</em>, <em class="sig-param">authorization_methods=None</em>, <em class="sig-param">bearer_token_sending_methods=None</em>, <em class="sig-param">client_authentication_methods=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_registration_endpoint=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">default_scope=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">grant_types=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">resource_owner_password=None</em>, <em class="sig-param">resource_owner_username=None</em>, <em class="sig-param">support_state=None</em>, <em class="sig-param">token_body_parameters=None</em>, <em class="sig-param">token_endpoint=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthorizationServer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which this Authorization Server should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>authorization_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OAUTH Authorization Endpoint.</p></li>
<li><p><strong>authorization_methods</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The HTTP Verbs supported by the Authorization Endpoint. Possible values are <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code> and <code class="docutils literal notranslate"><span class="pre">TRACE</span></code>.</p></li>
<li><p><strong>bearer_token_sending_methods</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The mechanism by which Access Tokens are passed to the API. Possible values are <code class="docutils literal notranslate"><span class="pre">authorizationHeader</span></code> and <code class="docutils literal notranslate"><span class="pre">query</span></code>.</p></li>
<li><p><strong>client_authentication_methods</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The Authentication Methods supported by the Token endpoint of this Authorization Server.. Possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Body</span></code>.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Client/App ID registered with this Authorization Server.</p></li>
<li><p><strong>client_registration_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of page where Client/App Registration is performed for this Authorization Server.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Client/App Secret registered with this Authorization Server.</p></li>
<li><p><strong>default_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Default Scope used when requesting an Access Token, specified as a string containing space-delimited values.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the Authorization Server, which may contain HTML formatting tags.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user-friendly name of this Authorization Server.</p></li>
<li><p><strong>grant_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Form of Authorization Grants required when requesting an Access Token. Possible values are <code class="docutils literal notranslate"><span class="pre">authorizationCode</span></code>, <code class="docutils literal notranslate"><span class="pre">clientCredentials</span></code>, <code class="docutils literal notranslate"><span class="pre">implicit</span></code> and <code class="docutils literal notranslate"><span class="pre">resourceOwnerPassword</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this Authorization Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_owner_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password associated with the Resource Owner.</p></li>
<li><p><strong>resource_owner_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username associated with the Resource Owner.</p></li>
<li><p><strong>support_state</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Server support State? If this is set to <code class="docutils literal notranslate"><span class="pre">true</span></code> the client may use the state parameter to raise protocol security.</p></li>
<li><p><strong>token_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OAUTH Token Endpoint.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>token_body_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of the Parameter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Value of the Parameter.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.AuthorizationServer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.AuthorizationServer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.AuthorizationServer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.AwaitableGetApiResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">AwaitableGetApiResult</code><span class="sig-paren">(</span><em class="sig-param">api_management_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">is_current=None</em>, <em class="sig-param">is_online=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">protocols=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">revision=None</em>, <em class="sig-param">service_url=None</em>, <em class="sig-param">soap_pass_through=None</em>, <em class="sig-param">subscription_key_parameter_names=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">version_set_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.AwaitableGetApiResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.AwaitableGetApiVersionSetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">AwaitableGetApiVersionSetResult</code><span class="sig-paren">(</span><em class="sig-param">api_management_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">version_header_name=None</em>, <em class="sig-param">version_query_name=None</em>, <em class="sig-param">versioning_scheme=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.AwaitableGetApiVersionSetResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.AwaitableGetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">AwaitableGetGroupResult</code><span class="sig-paren">(</span><em class="sig-param">api_management_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">external_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.AwaitableGetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.AwaitableGetProductResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">AwaitableGetProductResult</code><span class="sig-paren">(</span><em class="sig-param">api_management_name=None</em>, <em class="sig-param">approval_required=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">product_id=None</em>, <em class="sig-param">published=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">subscription_required=None</em>, <em class="sig-param">subscriptions_limit=None</em>, <em class="sig-param">terms=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.AwaitableGetProductResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.AwaitableGetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">AwaitableGetServiceResult</code><span class="sig-paren">(</span><em class="sig-param">additional_locations=None</em>, <em class="sig-param">gateway_regional_url=None</em>, <em class="sig-param">gateway_url=None</em>, <em class="sig-param">hostname_configurations=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">management_api_url=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notification_sender_email=None</em>, <em class="sig-param">portal_url=None</em>, <em class="sig-param">public_ip_addresses=None</em>, <em class="sig-param">publisher_email=None</em>, <em class="sig-param">publisher_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">scm_url=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.AwaitableGetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.AwaitableGetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">AwaitableGetUserResult</code><span class="sig-paren">(</span><em class="sig-param">api_management_name=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">first_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">last_name=None</em>, <em class="sig-param">note=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">user_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.AwaitableGetUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.Backend">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">Backend</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">credentials=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">proxy=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">service_fabric_cluster=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">tls=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Backend" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a backend within an API Management Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">credentials</span></code> block as documented below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the backend.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management backend. Changing this forces a new resource to be created.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol used by the backend host. Possible values are <code class="docutils literal notranslate"><span class="pre">http</span></code> or <code class="docutils literal notranslate"><span class="pre">soap</span></code>.</p></li>
<li><p><strong>proxy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">proxy</span></code> block as documented below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.</p></li>
<li><p><strong>service_fabric_cluster</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">service_fabric_cluster</span></code> block as documented below.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the backend.</p></li>
<li><p><strong>tls</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">tls</span></code> block as documented below.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the backend host.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authorization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">authorization</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authentication Parameter value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authentication Scheme name.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of client certificate thumbprints to present to the backend host. The certificates must exist within the API Management Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">header</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of header parameters to pass to the backend host. The keys are the header names and the values are a comma separated string of header values. This is converted to a list before being passed to the API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of query parameters to pass to the backend host. The keys are the query names and the values are a comma separated string of query values. This is converted to a list before being passed to the API.</p></li>
</ul>
<p>The <strong>proxy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password to connect to the proxy server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL of the proxy server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username to connect to the proxy server.</p></li>
</ul>
<p>The <strong>service_fabric_cluster</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificateThumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate thumbprint for the management endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managementEndpoints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of cluster management endpoints.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPartitionResolutionRetries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of retries when attempting resolve the partition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverCertificateThumbprints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of thumbprints of the server certificates of the Service Fabric cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverX509Names</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">server_x509_name</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">issuerCertificateThumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The thumbprint for the issuer of the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the API Management backend. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>tls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">validateCertificateChain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Flag indicating whether SSL certificate chain validation should be done when using self-signed certificates for the backend host.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">validateCertificateName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Flag indicating whether SSL certificate name validation should be done when using self-signed certificates for the backend host.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Backend.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Backend.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Backend.credentials">
<code class="sig-name descname">credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Backend.credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">credentials</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authorization</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - An <code class="docutils literal notranslate"><span class="pre">authorization</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The authentication Parameter value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The authentication Scheme name.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of client certificate thumbprints to present to the backend host. The certificates must exist within the API Management Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">header</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A mapping of header parameters to pass to the backend host. The keys are the header names and the values are a comma separated string of header values. This is converted to a list before being passed to the API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A mapping of query parameters to pass to the backend host. The keys are the query names and the values are a comma separated string of query values. This is converted to a list before being passed to the API.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Backend.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Backend.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Backend.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Backend.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management backend. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Backend.protocol">
<code class="sig-name descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Backend.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol used by the backend host. Possible values are <code class="docutils literal notranslate"><span class="pre">http</span></code> or <code class="docutils literal notranslate"><span class="pre">soap</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Backend.proxy">
<code class="sig-name descname">proxy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Backend.proxy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">proxy</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password to connect to the proxy server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL of the proxy server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username to connect to the proxy server.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Backend.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Backend.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Backend.resource_id">
<code class="sig-name descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Backend.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Backend.service_fabric_cluster">
<code class="sig-name descname">service_fabric_cluster</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Backend.service_fabric_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">service_fabric_cluster</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificateThumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client certificate thumbprint for the management endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managementEndpoints</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of cluster management endpoints.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPartitionResolutionRetries</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of retries when attempting resolve the partition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverCertificateThumbprints</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of thumbprints of the server certificates of the Service Fabric cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverX509Names</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">server_x509_name</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">issuerCertificateThumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The thumbprint for the issuer of the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the API Management backend. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Backend.title">
<code class="sig-name descname">title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Backend.title" title="Permalink to this definition">¶</a></dt>
<dd><p>The title of the backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Backend.tls">
<code class="sig-name descname">tls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Backend.tls" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">tls</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">validateCertificateChain</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Flag indicating whether SSL certificate chain validation should be done when using self-signed certificates for the backend host.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">validateCertificateName</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Flag indicating whether SSL certificate name validation should be done when using self-signed certificates for the backend host.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Backend.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Backend.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the backend host.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Backend.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">credentials=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">proxy=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">service_fabric_cluster=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">tls=None</em>, <em class="sig-param">url=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Backend.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Backend resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this backend should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">credentials</span></code> block as documented below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the backend.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management backend. Changing this forces a new resource to be created.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol used by the backend host. Possible values are <code class="docutils literal notranslate"><span class="pre">http</span></code> or <code class="docutils literal notranslate"><span class="pre">soap</span></code>.</p></li>
<li><p><strong>proxy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">proxy</span></code> block as documented below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The management URI of the backend host in an external system. This URI can be the ARM Resource ID of Logic Apps, Function Apps or API Apps, or the management endpoint of a Service Fabric cluster.</p></li>
<li><p><strong>service_fabric_cluster</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">service_fabric_cluster</span></code> block as documented below.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the backend.</p></li>
<li><p><strong>tls</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">tls</span></code> block as documented below.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the backend host.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authorization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">authorization</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">parameter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authentication Parameter value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authentication Scheme name.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of client certificate thumbprints to present to the backend host. The certificates must exist within the API Management Service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">header</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of header parameters to pass to the backend host. The keys are the header names and the values are a comma separated string of header values. This is converted to a list before being passed to the API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of query parameters to pass to the backend host. The keys are the query names and the values are a comma separated string of query values. This is converted to a list before being passed to the API.</p></li>
</ul>
<p>The <strong>proxy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password to connect to the proxy server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL of the proxy server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username to connect to the proxy server.</p></li>
</ul>
<p>The <strong>service_fabric_cluster</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificateThumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client certificate thumbprint for the management endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managementEndpoints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of cluster management endpoints.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPartitionResolutionRetries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of retries when attempting resolve the partition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverCertificateThumbprints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of thumbprints of the server certificates of the Service Fabric cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverX509Names</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">server_x509_name</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">issuerCertificateThumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The thumbprint for the issuer of the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the API Management backend. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>tls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">validateCertificateChain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Flag indicating whether SSL certificate chain validation should be done when using self-signed certificates for the backend host.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">validateCertificateName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Flag indicating whether SSL certificate name validation should be done when using self-signed certificates for the backend host.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Backend.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Backend.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Backend.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Backend.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Certificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">Certificate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">data=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Certificate within an API Management Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this Service should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base-64 encoded certificate data, which must be a PFX file. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Certificate. Changing this forces a new resource to be created.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password used for this certificate. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Certificate.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Service where this Service should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Certificate.data">
<code class="sig-name descname">data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.data" title="Permalink to this definition">¶</a></dt>
<dd><p>The base-64 encoded certificate data, which must be a PFX file. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Certificate.expiration">
<code class="sig-name descname">expiration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>The Expiration Date of this Certificate, formatted as an RFC3339 string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Certificate.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Certificate. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Certificate.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password used for this certificate. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Certificate.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Certificate.subject">
<code class="sig-name descname">subject</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.subject" title="Permalink to this definition">¶</a></dt>
<dd><p>The Subject of this Certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Certificate.thumbprint">
<code class="sig-name descname">thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Thumbprint of this Certificate.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Certificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">data=None</em>, <em class="sig-param">expiration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">subject=None</em>, <em class="sig-param">thumbprint=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Certificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this Service should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base-64 encoded certificate data, which must be a PFX file. Changing this forces a new resource to be created.</p></li>
<li><p><strong>expiration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Expiration Date of this Certificate, formatted as an RFC3339 string.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Certificate. Changing this forces a new resource to be created.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password used for this certificate. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subject</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Subject of this Certificate.</p></li>
<li><p><strong>thumbprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Thumbprint of this Certificate.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Certificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Certificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Certificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Diagnostic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">Diagnostic</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">identifier=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Diagnostic" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Service Diagnostic.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this Diagnostic should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether a Diagnostic should receive data or not.</p></li>
<li><p><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The diagnostic identifier for the API Management Service. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">applicationinsights</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Diagnostic.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Diagnostic.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Service where this Diagnostic should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Diagnostic.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Diagnostic.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether a Diagnostic should receive data or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Diagnostic.identifier">
<code class="sig-name descname">identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Diagnostic.identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The diagnostic identifier for the API Management Service. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">applicationinsights</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Diagnostic.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Diagnostic.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Diagnostic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">identifier=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Diagnostic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Diagnostic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this Diagnostic should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether a Diagnostic should receive data or not.</p></li>
<li><p><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The diagnostic identifier for the API Management Service. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">applicationinsights</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Diagnostic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Diagnostic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Diagnostic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Diagnostic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.GetApiResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">GetApiResult</code><span class="sig-paren">(</span><em class="sig-param">api_management_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">is_current=None</em>, <em class="sig-param">is_online=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">protocols=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">revision=None</em>, <em class="sig-param">service_url=None</em>, <em class="sig-param">soap_pass_through=None</em>, <em class="sig-param">subscription_key_parameter_names=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">version_set_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApi.</p>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the API Management API, which may include HTML formatting tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.is_current">
<code class="sig-name descname">is_current</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.is_current" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this the current API Revision?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.is_online">
<code class="sig-name descname">is_online</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.is_online" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this API Revision online/accessible via the Gateway?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The Path for this API Management API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.protocols">
<code class="sig-name descname">protocols</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.protocols" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of protocols the operations in this API can be invoked.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.service_url">
<code class="sig-name descname">service_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.service_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Absolute URL of the backend service implementing this API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.soap_pass_through">
<code class="sig-name descname">soap_pass_through</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.soap_pass_through" title="Permalink to this definition">¶</a></dt>
<dd><p>Should this API expose a SOAP frontend, rather than a HTTP frontend?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.subscription_key_parameter_names">
<code class="sig-name descname">subscription_key_parameter_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.subscription_key_parameter_names" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">subscription_key_parameter_names</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The Version number of this API, if this API is versioned.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiResult.version_set_id">
<code class="sig-name descname">version_set_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiResult.version_set_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Version Set which this API is associated with.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.GetApiVersionSetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">GetApiVersionSetResult</code><span class="sig-paren">(</span><em class="sig-param">api_management_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">version_header_name=None</em>, <em class="sig-param">version_query_name=None</em>, <em class="sig-param">versioning_scheme=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiVersionSetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApiVersionSet.</p>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiVersionSetResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiVersionSetResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of API Version Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiVersionSetResult.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiVersionSetResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of this API Version Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiVersionSetResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiVersionSetResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiVersionSetResult.version_header_name">
<code class="sig-name descname">version_header_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiVersionSetResult.version_header_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Header which should be read from Inbound Requests which defines the API Version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetApiVersionSetResult.version_query_name">
<code class="sig-name descname">version_query_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetApiVersionSetResult.version_query_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Query String which should be read from Inbound Requests which defines the API Version.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.GetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">GetGroupResult</code><span class="sig-paren">(</span><em class="sig-param">api_management_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">external_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetGroupResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this API Management Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetGroupResult.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of this API Management Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetGroupResult.external_id">
<code class="sig-name descname">external_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the external Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetGroupResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of this API Management Group, such as <code class="docutils literal notranslate"><span class="pre">custom</span></code> or <code class="docutils literal notranslate"><span class="pre">external</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.GetProductResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">GetProductResult</code><span class="sig-paren">(</span><em class="sig-param">api_management_name=None</em>, <em class="sig-param">approval_required=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">product_id=None</em>, <em class="sig-param">published=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">subscription_required=None</em>, <em class="sig-param">subscriptions_limit=None</em>, <em class="sig-param">terms=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProduct.</p>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.approval_required">
<code class="sig-name descname">approval_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.approval_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Do subscribers need to be approved prior to being able to use the Product?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this Product, which may include HTML formatting tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Display Name for this API Management Product.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.published">
<code class="sig-name descname">published</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.published" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Product Published?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.subscription_required">
<code class="sig-name descname">subscription_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.subscription_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Is a Subscription required to access API’s included in this Product?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.subscriptions_limit">
<code class="sig-name descname">subscriptions_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.subscriptions_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of subscriptions a user can have to this Product at the same time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.terms">
<code class="sig-name descname">terms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.terms" title="Permalink to this definition">¶</a></dt>
<dd><p>Any Terms and Conditions for this Product, which must be accepted by Developers before they can begin the Subscription process.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.GetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">GetServiceResult</code><span class="sig-paren">(</span><em class="sig-param">additional_locations=None</em>, <em class="sig-param">gateway_regional_url=None</em>, <em class="sig-param">gateway_url=None</em>, <em class="sig-param">hostname_configurations=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">management_api_url=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notification_sender_email=None</em>, <em class="sig-param">portal_url=None</em>, <em class="sig-param">public_ip_addresses=None</em>, <em class="sig-param">publisher_email=None</em>, <em class="sig-param">publisher_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">scm_url=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getService.</p>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.additional_locations">
<code class="sig-name descname">additional_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.additional_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">additional_location</span></code> blocks as defined below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.gateway_regional_url">
<code class="sig-name descname">gateway_regional_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.gateway_regional_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Gateway URL of the API Management service in the Region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.gateway_url">
<code class="sig-name descname">gateway_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.gateway_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for the API Management Service’s Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.hostname_configurations">
<code class="sig-name descname">hostname_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.hostname_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">hostname_configuration</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location name of the additional region among Azure Data center regions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.management_api_url">
<code class="sig-name descname">management_api_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.management_api_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for the Management API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the plan’s pricing tier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.notification_sender_email">
<code class="sig-name descname">notification_sender_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.notification_sender_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address from which the notification will be sent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.portal_url">
<code class="sig-name descname">portal_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.portal_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the Publisher Portal.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.public_ip_addresses">
<code class="sig-name descname">public_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.public_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.publisher_email">
<code class="sig-name descname">publisher_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.publisher_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email of Publisher/Company of the API Management Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.publisher_name">
<code class="sig-name descname">publisher_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.publisher_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Publisher/Company of the API Management Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.scm_url">
<code class="sig-name descname">scm_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.scm_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The SCM (Source Code Management) endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetServiceResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetServiceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.GetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">GetUserResult</code><span class="sig-paren">(</span><em class="sig-param">api_management_name=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">first_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">last_name=None</em>, <em class="sig-param">note=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">user_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.email">
<code class="sig-name descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The Email Address used for this User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.first_name">
<code class="sig-name descname">first_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.first_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The First Name for the User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.last_name">
<code class="sig-name descname">last_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.last_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Last Name for the User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.note">
<code class="sig-name descname">note</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.note" title="Permalink to this definition">¶</a></dt>
<dd><p>Any notes about this User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The current state of this User, for example <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">blocked</span></code> or <code class="docutils literal notranslate"><span class="pre">pending</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">external_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Group.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which the API Management Group should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this API Management Group.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of this API Management Group.</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the external Group. For example, an Azure Active Directory group <code class="docutils literal notranslate"><span class="pre">aad://&lt;tenant&gt;.onmicrosoft.com/groups/&lt;group</span> <span class="pre">object</span> <span class="pre">id&gt;</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Group should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of this API Management Group. Possible values are <code class="docutils literal notranslate"><span class="pre">custom</span></code> and <code class="docutils literal notranslate"><span class="pre">external</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">custom</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service in which the API Management Group should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this API Management Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of this API Management Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.external_id">
<code class="sig-name descname">external_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the external Group. For example, an Azure Active Directory group <code class="docutils literal notranslate"><span class="pre">aad://&lt;tenant&gt;.onmicrosoft.com/groups/&lt;group</span> <span class="pre">object</span> <span class="pre">id&gt;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Group should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of this API Management Group. Possible values are <code class="docutils literal notranslate"><span class="pre">custom</span></code> and <code class="docutils literal notranslate"><span class="pre">external</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">custom</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">external_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which the API Management Group should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this API Management Group.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of this API Management Group.</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the external Group. For example, an Azure Active Directory group <code class="docutils literal notranslate"><span class="pre">aad://&lt;tenant&gt;.onmicrosoft.com/groups/&lt;group</span> <span class="pre">object</span> <span class="pre">id&gt;</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Group should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of this API Management Group. Possible values are <code class="docutils literal notranslate"><span class="pre">custom</span></code> and <code class="docutils literal notranslate"><span class="pre">external</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">custom</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.GroupUser">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">GroupUser</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">group_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">user_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management User Assignment to a Group.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management User which should be assigned to this API Management Group. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GroupUser.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GroupUser.group_name">
<code class="sig-name descname">group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GroupUser.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GroupUser.user_id">
<code class="sig-name descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the API Management User which should be assigned to this API Management Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.GroupUser.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">group_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">user_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupUser resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management User which should be assigned to this API Management Group. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.GroupUser.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.GroupUser.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.IdentityProviderAad">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">IdentityProviderAad</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allowed_tenants=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderAad" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management AAD Identity Provider.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_tenants</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed AAD Tenants.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this AAD Identity Provider should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Id of the Application in the AAD Identity Provider.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret of the Application in the AAD Identity Provider.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderAad.allowed_tenants">
<code class="sig-name descname">allowed_tenants</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderAad.allowed_tenants" title="Permalink to this definition">¶</a></dt>
<dd><p>List of allowed AAD Tenants.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderAad.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderAad.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Service where this AAD Identity Provider should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderAad.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderAad.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Client Id of the Application in the AAD Identity Provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderAad.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderAad.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Client secret of the Application in the AAD Identity Provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderAad.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderAad.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.IdentityProviderAad.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allowed_tenants=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderAad.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IdentityProviderAad resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_tenants</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed AAD Tenants.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this AAD Identity Provider should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Id of the Application in the AAD Identity Provider.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret of the Application in the AAD Identity Provider.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.IdentityProviderAad.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderAad.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.IdentityProviderAad.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderAad.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.IdentityProviderFacebook">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">IdentityProviderFacebook</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">app_secret=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderFacebook" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Facebook Identity Provider.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this Facebook Identity Provider should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – App ID for Facebook.</p></li>
<li><p><strong>app_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – App Secret for Facebook.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderFacebook.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderFacebook.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Service where this Facebook Identity Provider should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderFacebook.app_id">
<code class="sig-name descname">app_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderFacebook.app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>App ID for Facebook.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderFacebook.app_secret">
<code class="sig-name descname">app_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderFacebook.app_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>App Secret for Facebook.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderFacebook.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderFacebook.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.IdentityProviderFacebook.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">app_secret=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderFacebook.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IdentityProviderFacebook resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this Facebook Identity Provider should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – App ID for Facebook.</p></li>
<li><p><strong>app_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – App Secret for Facebook.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.IdentityProviderFacebook.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderFacebook.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.IdentityProviderFacebook.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderFacebook.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.IdentityProviderGoogle">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">IdentityProviderGoogle</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderGoogle" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Google Identity Provider.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this Google Identity Provider should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Id for Google Sign-in.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret for Google Sign-in.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderGoogle.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderGoogle.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Service where this Google Identity Provider should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderGoogle.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderGoogle.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Client Id for Google Sign-in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderGoogle.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderGoogle.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Client secret for Google Sign-in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderGoogle.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderGoogle.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.IdentityProviderGoogle.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderGoogle.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IdentityProviderGoogle resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this Google Identity Provider should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Id for Google Sign-in.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret for Google Sign-in.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.IdentityProviderGoogle.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderGoogle.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.IdentityProviderGoogle.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderGoogle.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.IdentityProviderMicrosoft">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">IdentityProviderMicrosoft</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderMicrosoft" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Microsoft Identity Provider.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this Microsoft Identity Provider should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Id of the Azure AD Application.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret of the Azure AD Application.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderMicrosoft.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderMicrosoft.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Service where this Microsoft Identity Provider should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderMicrosoft.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderMicrosoft.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Client Id of the Azure AD Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderMicrosoft.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderMicrosoft.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Client secret of the Azure AD Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderMicrosoft.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderMicrosoft.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.IdentityProviderMicrosoft.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderMicrosoft.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IdentityProviderMicrosoft resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this Microsoft Identity Provider should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client Id of the Azure AD Application.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret of the Azure AD Application.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.IdentityProviderMicrosoft.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderMicrosoft.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.IdentityProviderMicrosoft.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderMicrosoft.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.IdentityProviderTwitter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">IdentityProviderTwitter</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_key=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">api_secret_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderTwitter" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Twitter Identity Provider.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – App Consumer API key for Twitter.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this Twitter Identity Provider should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>api_secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – App Consumer API secret key for Twitter.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderTwitter.api_key">
<code class="sig-name descname">api_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderTwitter.api_key" title="Permalink to this definition">¶</a></dt>
<dd><p>App Consumer API key for Twitter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderTwitter.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderTwitter.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Service where this Twitter Identity Provider should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderTwitter.api_secret_key">
<code class="sig-name descname">api_secret_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderTwitter.api_secret_key" title="Permalink to this definition">¶</a></dt>
<dd><p>App Consumer API secret key for Twitter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.IdentityProviderTwitter.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderTwitter.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.IdentityProviderTwitter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_key=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">api_secret_key=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderTwitter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IdentityProviderTwitter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – App Consumer API key for Twitter.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Service where this Twitter Identity Provider should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>api_secret_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – App Consumer API secret key for Twitter.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.IdentityProviderTwitter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderTwitter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.IdentityProviderTwitter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.IdentityProviderTwitter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Logger">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">Logger</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">application_insights=None</em>, <em class="sig-param">buffered=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">eventhub=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Logger" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Logger within an API Management Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>application_insights</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">application_insights</span></code> block as documented below.</p></li>
<li><p><strong>buffered</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether records should be buffered in the Logger prior to publishing. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this Logger.</p></li>
<li><p><strong>eventhub</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">eventhub</span></code> block as documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this Logger, which must be unique within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>application_insights</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instrumentation_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The instrumentation key used to push data to Application Insights.</p></li>
</ul>
<p>The <strong>eventhub</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connection_string</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The connection string of an EventHub Namespace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an EventHub.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Logger.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Logger.application_insights">
<code class="sig-name descname">application_insights</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.application_insights" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">application_insights</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instrumentation_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The instrumentation key used to push data to Application Insights.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Logger.buffered">
<code class="sig-name descname">buffered</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.buffered" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether records should be buffered in the Logger prior to publishing. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Logger.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of this Logger.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Logger.eventhub">
<code class="sig-name descname">eventhub</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.eventhub" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">eventhub</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connection_string</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The connection string of an EventHub Namespace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of an EventHub.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Logger.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this Logger, which must be unique within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Logger.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Logger.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">application_insights=None</em>, <em class="sig-param">buffered=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">eventhub=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Logger resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>application_insights</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">application_insights</span></code> block as documented below.</p></li>
<li><p><strong>buffered</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether records should be buffered in the Logger prior to publishing. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this Logger.</p></li>
<li><p><strong>eventhub</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">eventhub</span></code> block as documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this Logger, which must be unique within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>application_insights</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instrumentation_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The instrumentation key used to push data to Application Insights.</p></li>
</ul>
<p>The <strong>eventhub</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connection_string</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The connection string of an EventHub Namespace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of an EventHub.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Logger.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Logger.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Logger.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">OpenIdConnectProvider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">metadata_endpoint=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an OpenID Connect Provider within a API Management Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which this OpenID Connect Provider should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Client ID used for the Client Application.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Client Secret used for the Client Application.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this OpenID Connect Provider.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-friendly name for this OpenID Connect Provider.</p></li>
<li><p><strong>metadata_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the Metadata endpoint.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the Name of the OpenID Connect Provider which should be created within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service in which this OpenID Connect Provider should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Client ID used for the Client Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The Client Secret used for the Client Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of this OpenID Connect Provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A user-friendly name for this OpenID Connect Provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.metadata_endpoint">
<code class="sig-name descname">metadata_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.metadata_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the Metadata endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.name" title="Permalink to this definition">¶</a></dt>
<dd><p>the Name of the OpenID Connect Provider which should be created within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">metadata_endpoint=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OpenIdConnectProvider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which this OpenID Connect Provider should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Client ID used for the Client Application.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Client Secret used for the Client Application.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this OpenID Connect Provider.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-friendly name for this OpenID Connect Provider.</p></li>
<li><p><strong>metadata_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the Metadata endpoint.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the Name of the OpenID Connect Provider which should be created within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.OpenIdConnectProvider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.OpenIdConnectProvider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Product">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">Product</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">approval_required=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">product_id=None</em>, <em class="sig-param">published=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">subscription_required=None</em>, <em class="sig-param">subscriptions_limit=None</em>, <em class="sig-param">terms=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Product" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Product.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>approval_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do subscribers need to be approved prior to being able to use the Product?</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this Product, which may include HTML formatting tags.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Display Name for this API Management Product.</p></li>
<li><p><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identifier for this Product, which must be unique within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>published</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Product Published?</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subscription_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is a Subscription required to access API’s included in this Product?</p></li>
<li><p><strong>subscriptions_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of subscriptions a user can have to this Product at the same time.</p></li>
<li><p><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Terms and Conditions for this Product, which must be accepted by Developers before they can begin the Subscription process.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.approval_required">
<code class="sig-name descname">approval_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.approval_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Do subscribers need to be approved prior to being able to use the Product?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of this Product, which may include HTML formatting tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Display Name for this API Management Product.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.product_id">
<code class="sig-name descname">product_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.product_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Identifier for this Product, which must be unique within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.published">
<code class="sig-name descname">published</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.published" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Product Published?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.subscription_required">
<code class="sig-name descname">subscription_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.subscription_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Is a Subscription required to access API’s included in this Product?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.subscriptions_limit">
<code class="sig-name descname">subscriptions_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.subscriptions_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of subscriptions a user can have to this Product at the same time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.terms">
<code class="sig-name descname">terms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.terms" title="Permalink to this definition">¶</a></dt>
<dd><p>The Terms and Conditions for this Product, which must be accepted by Developers before they can begin the Subscription process.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Product.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">approval_required=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">product_id=None</em>, <em class="sig-param">published=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">subscription_required=None</em>, <em class="sig-param">subscriptions_limit=None</em>, <em class="sig-param">terms=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Product.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Product resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>approval_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do subscribers need to be approved prior to being able to use the Product?</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this Product, which may include HTML formatting tags.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Display Name for this API Management Product.</p></li>
<li><p><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identifier for this Product, which must be unique within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>published</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Product Published?</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subscription_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is a Subscription required to access API’s included in this Product?</p></li>
<li><p><strong>subscriptions_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of subscriptions a user can have to this Product at the same time.</p></li>
<li><p><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Terms and Conditions for this Product, which must be accepted by Developers before they can begin the Subscription process.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Product.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Product.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Product.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Product.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ProductApi">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">ProductApi</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">api_name=None</em>, <em class="sig-param">product_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductApi" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management API Assignment to a Product.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>api_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management API within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management Product within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductApi.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductApi.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductApi.api_name">
<code class="sig-name descname">api_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductApi.api_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management API within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductApi.product_id">
<code class="sig-name descname">product_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductApi.product_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the API Management Product within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductApi.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductApi.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ProductApi.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">api_name=None</em>, <em class="sig-param">product_id=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductApi.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProductApi resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>api_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management API within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management Product within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ProductApi.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductApi.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ProductApi.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductApi.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ProductGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">ProductGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">group_name=None</em>, <em class="sig-param">product_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Product Assignment to a Group.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management Product within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductGroup.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductGroup.group_name">
<code class="sig-name descname">group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductGroup.product_id">
<code class="sig-name descname">product_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.product_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the API Management Product within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductGroup.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ProductGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">group_name=None</em>, <em class="sig-param">product_id=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProductGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management Product within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ProductGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ProductGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ProductPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">ProductPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">product_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">xml_content=None</em>, <em class="sig-param">xml_link=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Product Policy</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management Product within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>xml_content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The XML Content for this Policy.</p></li>
<li><p><strong>xml_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A link to a Policy XML Document, which must be publicly available.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductPolicy.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductPolicy.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductPolicy.product_id">
<code class="sig-name descname">product_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductPolicy.product_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the API Management Product within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductPolicy.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductPolicy.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductPolicy.xml_content">
<code class="sig-name descname">xml_content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductPolicy.xml_content" title="Permalink to this definition">¶</a></dt>
<dd><p>The XML Content for this Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductPolicy.xml_link">
<code class="sig-name descname">xml_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductPolicy.xml_link" title="Permalink to this definition">¶</a></dt>
<dd><p>A link to a Policy XML Document, which must be publicly available.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ProductPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">product_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">xml_content=None</em>, <em class="sig-param">xml_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProductPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management Product within the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>xml_content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The XML Content for this Policy.</p></li>
<li><p><strong>xml_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A link to a Policy XML Document, which must be publicly available.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ProductPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ProductPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Property">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">Property</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secret=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Property" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Property.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which the API Management Property should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of this API Management Property.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Property. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Property should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secret</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the API Management Property is secret. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags to be applied to the API Management Property.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of this API Management Property.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service in which the API Management Property should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of this API Management Property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Property. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Property should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.secret">
<code class="sig-name descname">secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the API Management Property is secret. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to be applied to the API Management Property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of this API Management Property.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Property.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secret=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Property.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Property resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which the API Management Property should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of this API Management Property.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Property. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Property should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secret</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the API Management Property is secret. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags to be applied to the API Management Property.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of this API Management Property.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Property.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Property.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Property.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Property.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Service">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">Service</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_locations=None</em>, <em class="sig-param">certificates=None</em>, <em class="sig-param">hostname_configuration=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notification_sender_email=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">protocols=None</em>, <em class="sig-param">publisher_email=None</em>, <em class="sig-param">publisher_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">security=None</em>, <em class="sig-param">sign_in=None</em>, <em class="sig-param">sign_up=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">additional_location</span></code> blocks as defined below.</p></li>
<li><p><strong>certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more (up to 10) <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined below.</p></li>
<li><p><strong>hostname_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">hostname_configuration</span></code> block as defined below.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block is documented below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>notification_sender_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address from which the notification will be sent.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">policy</span></code> block as defined below.</p></li>
<li><p><strong>protocols</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">protocols</span></code> block as defined below.</p></li>
<li><p><strong>publisher_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email of publisher/company.</p></li>
<li><p><strong>publisher_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of publisher/company.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>security</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">security</span></code> block as defined below.</p></li>
<li><p><strong>sign_in</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sign_in</span></code> block as defined below.</p></li>
<li><p><strong>sign_up</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sign_up</span></code> block as defined below.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">sku_name</span></code> is a string consisting of two parts separated by an underscore(_). The fist part is the <code class="docutils literal notranslate"><span class="pre">name</span></code>, valid values include: <code class="docutils literal notranslate"><span class="pre">Developer</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. The second part is the <code class="docutils literal notranslate"><span class="pre">capacity</span></code> (e.g. the number of deployed units of the <code class="docutils literal notranslate"><span class="pre">sku</span></code>), which must be a positive <code class="docutils literal notranslate"><span class="pre">integer</span></code> (e.g. <code class="docutils literal notranslate"><span class="pre">Developer_1</span></code>).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags assigned to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>additional_locations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">gateway_regional_url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL of the Regional Gateway for the API Management Service in the specified region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure Region in which the API Management Service should be expanded to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_ip_addresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.</p></li>
</ul>
<p>The <strong>certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificatePassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encodedCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Base64 Encoded PFX Certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Certificate Store where this certificate should be stored. Possible values are <code class="docutils literal notranslate"><span class="pre">CertificateAuthority</span></code> and <code class="docutils literal notranslate"><span class="pre">Root</span></code>.</p></li>
</ul>
<p>The <strong>hostname_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">managements</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">management</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Base64 Encoded Certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificatePassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password associated with the certificate provided above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Hostname to use for the Management API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault Secret containing the SSL Certificate, which must be should be of the type <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negotiateClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Client Certificate Negotiation be enabled for this Hostname? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">portals</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">portal</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One or more (up to 10) <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificatePassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Hostname to use for the Management API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault Secret containing the SSL Certificate, which must be should be of the type <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negotiateClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Client Certificate Negotiation be enabled for this Hostname? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">proxies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">proxy</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Base64 Encoded Certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificatePassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password associated with the certificate provided above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultSslBinding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the certificate associated with this Hostname the Default SSL Certificate? This is used when an SNI header isn’t specified by a client. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Hostname to use for the Management API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault Secret containing the SSL Certificate, which must be should be of the type <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negotiateClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Client Certificate Negotiation be enabled for this Hostname? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">scms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">scm</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One or more (up to 10) <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificatePassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Hostname to use for the Management API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault Secret containing the SSL Certificate, which must be should be of the type <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negotiateClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Client Certificate Negotiation be enabled for this Hostname? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Principal ID associated with this Managed Service Identity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Tenant ID associated with this Managed Service Identity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of Managed Service Identity that should be configured on this API Management Service. At this time the only supported value is<code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
<p>The <strong>policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">xml_content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The XML Content for this Policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xml_link</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A link to an API Management Policy XML Document, which must be publicly available.</p></li>
</ul>
<p>The <strong>protocols</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enable_http2</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should HTTP/2 be supported by the API Management Service? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>security</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enableBackendSsl30</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should SSL 3.0 be enabled on the backend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableBackendTls10</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should TLS 1.0 be enabled on the backend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableBackendTls11</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should TLS 1.1 be enabled on the backend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableFrontendSsl30</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should SSL 3.0 be enabled on the frontend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableFrontendTls10</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should TLS 1.0 be enabled on the frontend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableFrontendTls11</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should TLS 1.1 be enabled on the frontend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableTripleDesCiphers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the <code class="docutils literal notranslate"><span class="pre">TLS_RSA_WITH_3DES_EDE_CBC_SHA</span></code> cipher be enabled for alL TLS versions (1.0, 1.1 and 1.2)? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>sign_in</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should anonymous users be redirected to the sign in page?</p></li>
</ul>
<p>The <strong>sign_up</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Can users sign up on the development portal?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">termsOfService</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">terms_of_service</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consentRequired</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the user be asked for consent during sign up?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Terms of Service be displayed during sign up?.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">text</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Terms of Service which users are required to agree to in order to sign up.</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.additional_locations">
<code class="sig-name descname">additional_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.additional_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">additional_location</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">gateway_regional_url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL of the Regional Gateway for the API Management Service in the specified region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Azure Region in which the API Management Service should be expanded to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_ip_addresses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.certificates">
<code class="sig-name descname">certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more (up to 10) <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificatePassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password for the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encodedCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Base64 Encoded PFX Certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Certificate Store where this certificate should be stored. Possible values are <code class="docutils literal notranslate"><span class="pre">CertificateAuthority</span></code> and <code class="docutils literal notranslate"><span class="pre">Root</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.gateway_regional_url">
<code class="sig-name descname">gateway_regional_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.gateway_regional_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the Regional Gateway for the API Management Service in the specified region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.gateway_url">
<code class="sig-name descname">gateway_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.gateway_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the Gateway for the API Management Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.hostname_configuration">
<code class="sig-name descname">hostname_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.hostname_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">hostname_configuration</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">managements</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">management</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Base64 Encoded Certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificatePassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password associated with the certificate provided above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Hostname to use for the Management API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Key Vault Secret containing the SSL Certificate, which must be should be of the type <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negotiateClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should Client Certificate Negotiation be enabled for this Hostname? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">portals</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">portal</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - One or more (up to 10) <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificatePassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password for the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Hostname to use for the Management API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Key Vault Secret containing the SSL Certificate, which must be should be of the type <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negotiateClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should Client Certificate Negotiation be enabled for this Hostname? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">proxies</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">proxy</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Base64 Encoded Certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificatePassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password associated with the certificate provided above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultSslBinding</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the certificate associated with this Hostname the Default SSL Certificate? This is used when an SNI header isn’t specified by a client. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Hostname to use for the Management API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Key Vault Secret containing the SSL Certificate, which must be should be of the type <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negotiateClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should Client Certificate Negotiation be enabled for this Hostname? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">scms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">scm</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - One or more (up to 10) <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificatePassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password for the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Hostname to use for the Management API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Key Vault Secret containing the SSL Certificate, which must be should be of the type <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negotiateClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should Client Certificate Negotiation be enabled for this Hostname? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Principal ID associated with this Managed Service Identity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Tenant ID associated with this Managed Service Identity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the type of Managed Service Identity that should be configured on this API Management Service. At this time the only supported value is<code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.management_api_url">
<code class="sig-name descname">management_api_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.management_api_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for the Management API associated with this API Management service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.notification_sender_email">
<code class="sig-name descname">notification_sender_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.notification_sender_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email address from which the notification will be sent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.policy">
<code class="sig-name descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">policy</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">xml_content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The XML Content for this Policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xml_link</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A link to an API Management Policy XML Document, which must be publicly available.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.portal_url">
<code class="sig-name descname">portal_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.portal_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for the Publisher Portal associated with this API Management service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.protocols">
<code class="sig-name descname">protocols</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.protocols" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">protocols</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enable_http2</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should HTTP/2 be supported by the API Management Service? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.public_ip_addresses">
<code class="sig-name descname">public_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.public_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.publisher_email">
<code class="sig-name descname">publisher_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.publisher_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email of publisher/company.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.publisher_name">
<code class="sig-name descname">publisher_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.publisher_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of publisher/company.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.scm_url">
<code class="sig-name descname">scm_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.scm_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for the SCM (Source Code Management) Endpoint associated with this API Management service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.security">
<code class="sig-name descname">security</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.security" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">security</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enableBackendSsl30</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should SSL 3.0 be enabled on the backend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableBackendTls10</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should TLS 1.0 be enabled on the backend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableBackendTls11</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should TLS 1.1 be enabled on the backend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableFrontendSsl30</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should SSL 3.0 be enabled on the frontend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableFrontendTls10</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should TLS 1.0 be enabled on the frontend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableFrontendTls11</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should TLS 1.1 be enabled on the frontend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableTripleDesCiphers</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the <code class="docutils literal notranslate"><span class="pre">TLS_RSA_WITH_3DES_EDE_CBC_SHA</span></code> cipher be enabled for alL TLS versions (1.0, 1.1 and 1.2)? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.sign_in">
<code class="sig-name descname">sign_in</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.sign_in" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sign_in</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should anonymous users be redirected to the sign in page?</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.sign_up">
<code class="sig-name descname">sign_up</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.sign_up" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sign_up</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Can users sign up on the development portal?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">termsOfService</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">terms_of_service</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consentRequired</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the user be asked for consent during sign up?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should Terms of Service be displayed during sign up?.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">text</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Terms of Service which users are required to agree to in order to sign up.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">sku_name</span></code> is a string consisting of two parts separated by an underscore(_). The fist part is the <code class="docutils literal notranslate"><span class="pre">name</span></code>, valid values include: <code class="docutils literal notranslate"><span class="pre">Developer</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. The second part is the <code class="docutils literal notranslate"><span class="pre">capacity</span></code> (e.g. the number of deployed units of the <code class="docutils literal notranslate"><span class="pre">sku</span></code>), which must be a positive <code class="docutils literal notranslate"><span class="pre">integer</span></code> (e.g. <code class="docutils literal notranslate"><span class="pre">Developer_1</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Service.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Service.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Service.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_locations=None</em>, <em class="sig-param">certificates=None</em>, <em class="sig-param">gateway_regional_url=None</em>, <em class="sig-param">gateway_url=None</em>, <em class="sig-param">hostname_configuration=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">management_api_url=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notification_sender_email=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">portal_url=None</em>, <em class="sig-param">protocols=None</em>, <em class="sig-param">public_ip_addresses=None</em>, <em class="sig-param">publisher_email=None</em>, <em class="sig-param">publisher_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">scm_url=None</em>, <em class="sig-param">security=None</em>, <em class="sig-param">sign_in=None</em>, <em class="sig-param">sign_up=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Service.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Service resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">additional_location</span></code> blocks as defined below.</p></li>
<li><p><strong>certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more (up to 10) <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined below.</p></li>
<li><p><strong>gateway_regional_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the Regional Gateway for the API Management Service in the specified region.</p></li>
<li><p><strong>gateway_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the Gateway for the API Management Service.</p></li>
<li><p><strong>hostname_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">hostname_configuration</span></code> block as defined below.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block is documented below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>management_api_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL for the Management API associated with this API Management service.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>notification_sender_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address from which the notification will be sent.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">policy</span></code> block as defined below.</p></li>
<li><p><strong>portal_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL for the Publisher Portal associated with this API Management service.</p></li>
<li><p><strong>protocols</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">protocols</span></code> block as defined below.</p></li>
<li><p><strong>public_ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.</p></li>
<li><p><strong>publisher_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email of publisher/company.</p></li>
<li><p><strong>publisher_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of publisher/company.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>scm_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL for the SCM (Source Code Management) Endpoint associated with this API Management service.</p></li>
<li><p><strong>security</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">security</span></code> block as defined below.</p></li>
<li><p><strong>sign_in</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sign_in</span></code> block as defined below.</p></li>
<li><p><strong>sign_up</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sign_up</span></code> block as defined below.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">sku_name</span></code> is a string consisting of two parts separated by an underscore(_). The fist part is the <code class="docutils literal notranslate"><span class="pre">name</span></code>, valid values include: <code class="docutils literal notranslate"><span class="pre">Developer</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. The second part is the <code class="docutils literal notranslate"><span class="pre">capacity</span></code> (e.g. the number of deployed units of the <code class="docutils literal notranslate"><span class="pre">sku</span></code>), which must be a positive <code class="docutils literal notranslate"><span class="pre">integer</span></code> (e.g. <code class="docutils literal notranslate"><span class="pre">Developer_1</span></code>).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags assigned to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>additional_locations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">gateway_regional_url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL of the Regional Gateway for the API Management Service in the specified region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure Region in which the API Management Service should be expanded to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_ip_addresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.</p></li>
</ul>
<p>The <strong>certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificatePassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encodedCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Base64 Encoded PFX Certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Certificate Store where this certificate should be stored. Possible values are <code class="docutils literal notranslate"><span class="pre">CertificateAuthority</span></code> and <code class="docutils literal notranslate"><span class="pre">Root</span></code>.</p></li>
</ul>
<p>The <strong>hostname_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">managements</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">management</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Base64 Encoded Certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificatePassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password associated with the certificate provided above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Hostname to use for the Management API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault Secret containing the SSL Certificate, which must be should be of the type <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negotiateClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Client Certificate Negotiation be enabled for this Hostname? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">portals</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">portal</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One or more (up to 10) <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificatePassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Hostname to use for the Management API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault Secret containing the SSL Certificate, which must be should be of the type <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negotiateClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Client Certificate Negotiation be enabled for this Hostname? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">proxies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">proxy</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Base64 Encoded Certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificatePassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password associated with the certificate provided above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultSslBinding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the certificate associated with this Hostname the Default SSL Certificate? This is used when an SNI header isn’t specified by a client. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Hostname to use for the Management API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault Secret containing the SSL Certificate, which must be should be of the type <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negotiateClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Client Certificate Negotiation be enabled for this Hostname? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">scms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">scm</span></code> blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One or more (up to 10) <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificatePassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password for the certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Hostname to use for the Management API.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault Secret containing the SSL Certificate, which must be should be of the type <code class="docutils literal notranslate"><span class="pre">application/x-pkcs12</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negotiateClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Client Certificate Negotiation be enabled for this Hostname? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Principal ID associated with this Managed Service Identity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Tenant ID associated with this Managed Service Identity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of Managed Service Identity that should be configured on this API Management Service. At this time the only supported value is<code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
<p>The <strong>policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">xml_content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The XML Content for this Policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xml_link</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A link to an API Management Policy XML Document, which must be publicly available.</p></li>
</ul>
<p>The <strong>protocols</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enable_http2</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should HTTP/2 be supported by the API Management Service? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>security</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enableBackendSsl30</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should SSL 3.0 be enabled on the backend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableBackendTls10</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should TLS 1.0 be enabled on the backend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableBackendTls11</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should TLS 1.1 be enabled on the backend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableFrontendSsl30</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should SSL 3.0 be enabled on the frontend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableFrontendTls10</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should TLS 1.0 be enabled on the frontend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableFrontendTls11</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should TLS 1.1 be enabled on the frontend of the gateway? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableTripleDesCiphers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the <code class="docutils literal notranslate"><span class="pre">TLS_RSA_WITH_3DES_EDE_CBC_SHA</span></code> cipher be enabled for alL TLS versions (1.0, 1.1 and 1.2)? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>sign_in</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should anonymous users be redirected to the sign in page?</p></li>
</ul>
<p>The <strong>sign_up</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Can users sign up on the development portal?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">termsOfService</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">terms_of_service</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consentRequired</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the user be asked for consent during sign up?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Terms of Service be displayed during sign up?.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">text</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Terms of Service which users are required to agree to in order to sign up.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Service.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Service.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Subscription">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">Subscription</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">product_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">subscription_id=None</em>, <em class="sig-param">user_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Subscription within a API Management Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service where this Subscription should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of this Subscription.</p></li>
<li><p><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Product which should be assigned to this Subscription. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of this Subscription. Possible values are <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">cancelled</span></code>, <code class="docutils literal notranslate"><span class="pre">expired</span></code>, <code class="docutils literal notranslate"><span class="pre">rejected</span></code>, <code class="docutils literal notranslate"><span class="pre">submitted</span></code> and <code class="docutils literal notranslate"><span class="pre">suspended</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">submitted</span></code>.</p></li>
<li><p><strong>subscription_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An Identifier which should used as the ID of this Subscription. If not specified a new Subscription ID will be generated. Changing this forces a new resource to be created.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the User which should be assigned to this Subscription. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Subscription.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service where this Subscription should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Subscription.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of this Subscription.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Subscription.product_id">
<code class="sig-name descname">product_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.product_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Product which should be assigned to this Subscription. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Subscription.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Subscription.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of this Subscription. Possible values are <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">cancelled</span></code>, <code class="docutils literal notranslate"><span class="pre">expired</span></code>, <code class="docutils literal notranslate"><span class="pre">rejected</span></code>, <code class="docutils literal notranslate"><span class="pre">submitted</span></code> and <code class="docutils literal notranslate"><span class="pre">suspended</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">submitted</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Subscription.subscription_id">
<code class="sig-name descname">subscription_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.subscription_id" title="Permalink to this definition">¶</a></dt>
<dd><p>An Identifier which should used as the ID of this Subscription. If not specified a new Subscription ID will be generated. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Subscription.user_id">
<code class="sig-name descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the User which should be assigned to this Subscription. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Subscription.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">product_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">subscription_id=None</em>, <em class="sig-param">user_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Subscription resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service where this Subscription should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of this Subscription.</p></li>
<li><p><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Product which should be assigned to this Subscription. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of this Subscription. Possible values are <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">cancelled</span></code>, <code class="docutils literal notranslate"><span class="pre">expired</span></code>, <code class="docutils literal notranslate"><span class="pre">rejected</span></code>, <code class="docutils literal notranslate"><span class="pre">submitted</span></code> and <code class="docutils literal notranslate"><span class="pre">suspended</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">submitted</span></code>.</p></li>
<li><p><strong>subscription_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An Identifier which should used as the ID of this Subscription. If not specified a new Subscription ID will be generated. Changing this forces a new resource to be created.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the User which should be assigned to this Subscription. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Subscription.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Subscription.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Subscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">confirmation=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">first_name=None</em>, <em class="sig-param">last_name=None</em>, <em class="sig-param">note=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">user_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management User.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which the User should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>confirmation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kind of confirmation email which will be sent to this user. Possible values are <code class="docutils literal notranslate"><span class="pre">invite</span></code> and <code class="docutils literal notranslate"><span class="pre">signup</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address associated with this user.</p></li>
<li><p><strong>first_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The first name for this user.</p></li>
<li><p><strong>last_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The last name for this user.</p></li>
<li><p><strong>note</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note about this user.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password associated with this user.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of this user. Possible values are <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">blocked</span></code> and <code class="docutils literal notranslate"><span class="pre">pending</span></code>.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identifier for this User, which must be unique within the API Management Service. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.api_management_name">
<code class="sig-name descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service in which the User should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.confirmation">
<code class="sig-name descname">confirmation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.confirmation" title="Permalink to this definition">¶</a></dt>
<dd><p>The kind of confirmation email which will be sent to this user. Possible values are <code class="docutils literal notranslate"><span class="pre">invite</span></code> and <code class="docutils literal notranslate"><span class="pre">signup</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.email">
<code class="sig-name descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address associated with this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.first_name">
<code class="sig-name descname">first_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.first_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The first name for this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.last_name">
<code class="sig-name descname">last_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.last_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The last name for this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.note">
<code class="sig-name descname">note</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.note" title="Permalink to this definition">¶</a></dt>
<dd><p>A note about this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password associated with this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of this user. Possible values are <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">blocked</span></code> and <code class="docutils literal notranslate"><span class="pre">pending</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.user_id">
<code class="sig-name descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Identifier for this User, which must be unique within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_management_name=None</em>, <em class="sig-param">confirmation=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">first_name=None</em>, <em class="sig-param">last_name=None</em>, <em class="sig-param">note=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">user_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which the User should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>confirmation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kind of confirmation email which will be sent to this user. Possible values are <code class="docutils literal notranslate"><span class="pre">invite</span></code> and <code class="docutils literal notranslate"><span class="pre">signup</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address associated with this user.</p></li>
<li><p><strong>first_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The first name for this user.</p></li>
<li><p><strong>last_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The last name for this user.</p></li>
<li><p><strong>note</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note about this user.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password associated with this user.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of this user. Possible values are <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">blocked</span></code> and <code class="docutils literal notranslate"><span class="pre">pending</span></code>.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identifier for this User, which must be unique within the API Management Service. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.get_api">
<code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">get_api</code><span class="sig-paren">(</span><em class="sig-param">api_management_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">revision=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.get_api" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing API Management API.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>api_management_name</strong> (<em>str</em>) – The name of the API Management Service in which the API Management API exists.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the API Management API.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group in which the API Management Service exists.</p></li>
<li><p><strong>revision</strong> (<em>str</em>) – The Revision of the API Management API.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.apimanagement.get_api_version_set">
<code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">get_api_version_set</code><span class="sig-paren">(</span><em class="sig-param">api_management_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.get_api_version_set" title="Permalink to this definition">¶</a></dt>
<dd><p>Uses this data source to access information about an API Version Set within an API Management Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>api_management_name</strong> (<em>str</em>) – The name of the API Management Service where the API Version Set exists.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the API Version Set.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group in which the parent API Management Service exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.apimanagement.get_group">
<code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">get_group</code><span class="sig-paren">(</span><em class="sig-param">api_management_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing API Management Group.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>api_management_name</strong> (<em>str</em>) – The Name of the API Management Service in which this Group exists.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The Name of the API Management Group.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group in which the API Management Service exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.apimanagement.get_product">
<code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">get_product</code><span class="sig-paren">(</span><em class="sig-param">api_management_name=None</em>, <em class="sig-param">product_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.get_product" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing API Management Product.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>api_management_name</strong> (<em>str</em>) – The Name of the API Management Service in which this Product exists.</p></li>
<li><p><strong>product_id</strong> (<em>str</em>) – The Identifier for the API Management Product.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group in which the API Management Service exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.apimanagement.get_service">
<code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">get_service</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.get_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing API Management Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the API Management service.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group in which the API Management Service exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.apimanagement.get_user">
<code class="sig-prename descclassname">pulumi_azure.apimanagement.</code><code class="sig-name descname">get_user</code><span class="sig-paren">(</span><em class="sig-param">api_management_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">user_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing API Management User.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>api_management_name</strong> (<em>str</em>) – The Name of the API Management Service in which this User exists.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group in which the API Management Service exists.</p></li>
<li><p><strong>user_id</strong> (<em>str</em>) – The Identifier for the User.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
