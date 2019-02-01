<div class="section" id="module-pulumi_azure.apimanagement">
<span id="apimanagement"></span><h1>apimanagement<a class="headerlink" href="#module-pulumi_azure.apimanagement" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.apimanagement.API">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">API</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>additional_location=None</em>, <em>certificates=None</em>, <em>hostname_configuration=None</em>, <em>identity=None</em>, <em>location=None</em>, <em>name=None</em>, <em>notification_sender_email=None</em>, <em>publisher_email=None</em>, <em>publisher_name=None</em>, <em>resource_group_name=None</em>, <em>security=None</em>, <em>sku=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.API" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>additional_location</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – One or more <cite>additional_location</cite> blocks as defined below.</li>
<li><strong>certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more (up to 10) <cite>certificate</cite> blocks as defined below.</li>
<li><strong>hostname_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>hostname_configuration</cite> block as defined below.</li>
<li><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <cite>identity</cite> block is documented below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where the API Management Service exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>notification_sender_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address from which the notification will be sent.</li>
<li><strong>publisher_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email of publisher/company.</li>
<li><strong>publisher_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of publisher/company.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.</li>
<li><strong>security</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>security</cite> block as defined below.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>sku</cite> block as documented below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags assigned to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.additional_location">
<code class="descname">additional_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.additional_location" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>additional_location</cite> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.certificates">
<code class="descname">certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more (up to 10) <cite>certificate</cite> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.gateway_regional_url">
<code class="descname">gateway_regional_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.gateway_regional_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the Regional Gateway for the API Management Service in the specified region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.gateway_url">
<code class="descname">gateway_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.gateway_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the Gateway for the API Management Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.hostname_configuration">
<code class="descname">hostname_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.hostname_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>hostname_configuration</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.identity">
<code class="descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>An <cite>identity</cite> block is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.management_api_url">
<code class="descname">management_api_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.management_api_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for the Management API associated with this API Management service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.notification_sender_email">
<code class="descname">notification_sender_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.notification_sender_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email address from which the notification will be sent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.portal_url">
<code class="descname">portal_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.portal_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for the Publisher Portal associated with this API Management service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.public_ip_addresses">
<code class="descname">public_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.public_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.publisher_email">
<code class="descname">publisher_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.publisher_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email of publisher/company.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.publisher_name">
<code class="descname">publisher_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.publisher_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of publisher/company.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.scm_url">
<code class="descname">scm_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.scm_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for the SCM (Source Code Management) Endpoint associated with this API Management service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.security">
<code class="descname">security</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.security" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>security</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>sku</cite> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.API.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.API.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.API.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.API.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.GetAPIResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">GetAPIResult</code><span class="sig-paren">(</span><em>additional_locations=None</em>, <em>gateway_regional_url=None</em>, <em>gateway_url=None</em>, <em>hostname_configurations=None</em>, <em>location=None</em>, <em>management_api_url=None</em>, <em>notification_sender_email=None</em>, <em>portal_url=None</em>, <em>public_ip_addresses=None</em>, <em>publisher_email=None</em>, <em>publisher_name=None</em>, <em>scm_url=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GetAPIResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAPI.</p>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetAPIResult.additional_locations">
<code class="descname">additional_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetAPIResult.additional_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>additional_location</cite> blocks as defined below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetAPIResult.gateway_regional_url">
<code class="descname">gateway_regional_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetAPIResult.gateway_regional_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Gateway URL of the API Management service in the Region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetAPIResult.gateway_url">
<code class="descname">gateway_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetAPIResult.gateway_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for the API Management Service’s Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetAPIResult.hostname_configurations">
<code class="descname">hostname_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetAPIResult.hostname_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>hostname_configuration</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetAPIResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetAPIResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location name of the additional region among Azure Data center regions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetAPIResult.management_api_url">
<code class="descname">management_api_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetAPIResult.management_api_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL for the Management API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetAPIResult.notification_sender_email">
<code class="descname">notification_sender_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetAPIResult.notification_sender_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address from which the notification will be sent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetAPIResult.portal_url">
<code class="descname">portal_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetAPIResult.portal_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the Publisher Portal.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetAPIResult.public_ip_addresses">
<code class="descname">public_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetAPIResult.public_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>Public Static Load Balanced IP addresses of the API Management service in the additional location. Available only for Basic, Standard and Premium SKU.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetAPIResult.publisher_email">
<code class="descname">publisher_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetAPIResult.publisher_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email of Publisher/Company of the API Management Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetAPIResult.publisher_name">
<code class="descname">publisher_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetAPIResult.publisher_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Publisher/Company of the API Management Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetAPIResult.scm_url">
<code class="descname">scm_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetAPIResult.scm_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The SCM (Source Code Management) endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetAPIResult.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetAPIResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>sku</cite> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetAPIResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetAPIResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetAPIResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetAPIResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_azure.apimanagement.get_api">
<code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">get_api</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.get_api" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing API Management Service.</p>
</dd></dl>

</div>
