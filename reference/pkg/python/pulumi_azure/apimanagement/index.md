<div class="section" id="module-pulumi_azure.apimanagement">
<span id="apimanagement"></span><h1>apimanagement<a class="headerlink" href="#module-pulumi_azure.apimanagement" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.apimanagement.API">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">API</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>additional_location=None</em>, <em>certificates=None</em>, <em>hostname_configuration=None</em>, <em>identity=None</em>, <em>location=None</em>, <em>name=None</em>, <em>notification_sender_email=None</em>, <em>publisher_email=None</em>, <em>publisher_name=None</em>, <em>resource_group_name=None</em>, <em>security=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.API" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>additional_location</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">additional_location</span></code> blocks as defined below.</li>
<li><strong>certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more (up to 10) <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined below.</li>
<li><strong>hostname_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">hostname_configuration</span></code> block as defined below.</li>
<li><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block is documented below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where the API Management Service exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>notification_sender_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address from which the notification will be sent.</li>
<li><strong>publisher_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email of publisher/company.</li>
<li><strong>publisher_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of publisher/company.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.</li>
<li><strong>security</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">security</span></code> block as defined below.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as documented below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags assigned to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.additional_location">
<code class="descname">additional_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.additional_location" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">additional_location</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.certificates">
<code class="descname">certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more (up to 10) <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined below.</p>
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
<dd><p>A <code class="docutils literal notranslate"><span class="pre">hostname_configuration</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.identity">
<code class="descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block is documented below.</p>
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
<dd><p>A <code class="docutils literal notranslate"><span class="pre">security</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.API.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.API.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as documented below.</p>
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
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">additional_location</span></code> blocks as defined below</p>
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
<dd><p>A <code class="docutils literal notranslate"><span class="pre">hostname_configuration</span></code> block as defined below.</p>
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
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as documented below.</p>
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

<dl class="class">
<dt id="pulumi_azure.apimanagement.GetGroupResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">GetGroupResult</code><span class="sig-paren">(</span><em>description=None</em>, <em>display_name=None</em>, <em>external_id=None</em>, <em>type=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetGroupResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this API Management Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetGroupResult.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of this API Management Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetGroupResult.external_id">
<code class="descname">external_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the external Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetGroupResult.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of this API Management Group, such as <code class="docutils literal notranslate"><span class="pre">custom</span></code> or <code class="docutils literal notranslate"><span class="pre">external</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetGroupResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.GetProductResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">GetProductResult</code><span class="sig-paren">(</span><em>approval_required=None</em>, <em>description=None</em>, <em>display_name=None</em>, <em>published=None</em>, <em>subscription_required=None</em>, <em>subscriptions_limit=None</em>, <em>terms=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProduct.</p>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.approval_required">
<code class="descname">approval_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.approval_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Do subscribers need to be approved prior to being able to use the Product?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this Product, which may include HTML formatting tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Display Name for this API Management Product.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.published">
<code class="descname">published</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.published" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Product Published?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.subscription_required">
<code class="descname">subscription_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.subscription_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Is a Subscription required to access API’s included in this Product?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.subscriptions_limit">
<code class="descname">subscriptions_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.subscriptions_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of subscriptions a user can have to this Product at the same time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.terms">
<code class="descname">terms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.terms" title="Permalink to this definition">¶</a></dt>
<dd><p>Any Terms and Conditions for this Product, which must be accepted by Developers before they can begin the Subscription process.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetProductResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetProductResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.GetUserResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">GetUserResult</code><span class="sig-paren">(</span><em>email=None</em>, <em>first_name=None</em>, <em>last_name=None</em>, <em>note=None</em>, <em>state=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.email">
<code class="descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The Email Address used for this User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.first_name">
<code class="descname">first_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.first_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The First Name for the User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.last_name">
<code class="descname">last_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.last_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Last Name for the User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.note">
<code class="descname">note</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.note" title="Permalink to this definition">¶</a></dt>
<dd><p>Any notes about this User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The current state of this User, for example <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">blocked</span></code> or <code class="docutils literal notranslate"><span class="pre">pending</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GetUserResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.apimanagement.Group">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">Group</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>description=None</em>, <em>display_name=None</em>, <em>external_id=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Group.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which the API Management Group should exist. Changing this forces a new resource to be created.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this API Management Group.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of this API Management Group.</li>
<li><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the external Group. For example, an Azure Active Directory group <code class="docutils literal notranslate"><span class="pre">aad://&lt;tenant&gt;.onmicrosoft.com/groups/&lt;group</span> <span class="pre">object</span> <span class="pre">id&gt;</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Group. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Group should exist. Changing this forces a new resource to be created.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of this API Management Group. Possible values are <code class="docutils literal notranslate"><span class="pre">custom</span></code> and <code class="docutils literal notranslate"><span class="pre">external</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">custom</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service in which the API Management Group should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this API Management Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of this API Management Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.external_id">
<code class="descname">external_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the external Group. For example, an Azure Active Directory group <code class="docutils literal notranslate"><span class="pre">aad://&lt;tenant&gt;.onmicrosoft.com/groups/&lt;group</span> <span class="pre">object</span> <span class="pre">id&gt;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Group should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Group.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Group.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of this API Management Group. Possible values are <code class="docutils literal notranslate"><span class="pre">custom</span></code> and <code class="docutils literal notranslate"><span class="pre">external</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">custom</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Group.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Group.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.GroupUser">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">GroupUser</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>group_name=None</em>, <em>resource_group_name=None</em>, <em>user_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management User Assignment to a Group.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</li>
<li><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the API Management User which should be assigned to this API Management Group. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GroupUser.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GroupUser.group_name">
<code class="descname">group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GroupUser.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.GroupUser.user_id">
<code class="descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the API Management User which should be assigned to this API Management Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.GroupUser.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.GroupUser.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.GroupUser.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Product">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">Product</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>approval_required=None</em>, <em>description=None</em>, <em>display_name=None</em>, <em>product_id=None</em>, <em>published=None</em>, <em>resource_group_name=None</em>, <em>subscription_required=None</em>, <em>subscriptions_limit=None</em>, <em>terms=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Product" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Product.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>approval_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do subscribers need to be approved prior to being able to use the Product?</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this Product, which may include HTML formatting tags.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Display Name for this API Management Product.</li>
<li><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identifier for this Product, which must be unique within the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>published</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is this Product Published?</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.</li>
<li><strong>subscription_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is a Subscription required to access API’s included in this Product?</li>
<li><strong>subscriptions_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of subscriptions a user can have to this Product at the same time.</li>
<li><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Terms and Conditions for this Product, which must be accepted by Developers before they can begin the Subscription process.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.approval_required">
<code class="descname">approval_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.approval_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Do subscribers need to be approved prior to being able to use the Product?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of this Product, which may include HTML formatting tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Display Name for this API Management Product.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.product_id">
<code class="descname">product_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.product_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Identifier for this Product, which must be unique within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.published">
<code class="descname">published</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.published" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Product Published?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service should be exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.subscription_required">
<code class="descname">subscription_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.subscription_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Is a Subscription required to access API’s included in this Product?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.subscriptions_limit">
<code class="descname">subscriptions_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.subscriptions_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of subscriptions a user can have to this Product at the same time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Product.terms">
<code class="descname">terms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Product.terms" title="Permalink to this definition">¶</a></dt>
<dd><p>The Terms and Conditions for this Product, which must be accepted by Developers before they can begin the Subscription process.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Product.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Product.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Product.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Product.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ProductGroup">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">ProductGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>group_name=None</em>, <em>product_id=None</em>, <em>resource_group_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Product Assignment to a Group.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductGroup.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductGroup.group_name">
<code class="descname">group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the API Management Group within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.ProductGroup.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.ProductGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.ProductGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.ProductGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Property">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">Property</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>display_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>secret=None</em>, <em>tags=None</em>, <em>value=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Property" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management Property.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which the API Management Property should exist. Changing this forces a new resource to be created.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of this API Management Property.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Property. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Property should exist. Changing this forces a new resource to be created.</li>
<li><strong>secret</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the API Management Property is secret. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags to be applied to the API Management Property.</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of this API Management Property.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service in which the API Management Property should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of this API Management Property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Property. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Property should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.secret">
<code class="descname">secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the API Management Property is secret. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to be applied to the API Management Property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.Property.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.Property.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of this API Management Property.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.Property.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Property.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.Property.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.Property.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.User">
<em class="property">class </em><code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">User</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_management_name=None</em>, <em>confirmation=None</em>, <em>email=None</em>, <em>first_name=None</em>, <em>last_name=None</em>, <em>note=None</em>, <em>password=None</em>, <em>resource_group_name=None</em>, <em>state=None</em>, <em>user_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Management User.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_management_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API Management Service in which the User should be created. Changing this forces a new resource to be created.</li>
<li><strong>confirmation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kind of confirmation email which will be sent to this user. Possible values are <code class="docutils literal notranslate"><span class="pre">invite</span></code> and <code class="docutils literal notranslate"><span class="pre">signup</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address associated with this user.</li>
<li><strong>first_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The first name for this user.</li>
<li><strong>last_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The last name for this user.</li>
<li><strong>note</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note about this user.</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password associated with this user.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</li>
<li><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of this user. Possible values are <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">blocked</span></code> and <code class="docutils literal notranslate"><span class="pre">pending</span></code>.</li>
<li><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Identifier for this User, which must be unique within the API Management Service. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.api_management_name">
<code class="descname">api_management_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.api_management_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API Management Service in which the User should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.confirmation">
<code class="descname">confirmation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.confirmation" title="Permalink to this definition">¶</a></dt>
<dd><p>The kind of confirmation email which will be sent to this user. Possible values are <code class="docutils literal notranslate"><span class="pre">invite</span></code> and <code class="docutils literal notranslate"><span class="pre">signup</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.email">
<code class="descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address associated with this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.first_name">
<code class="descname">first_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.first_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The first name for this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.last_name">
<code class="descname">last_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.last_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The last name for this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.note">
<code class="descname">note</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.note" title="Permalink to this definition">¶</a></dt>
<dd><p>A note about this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password associated with this user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of this user. Possible values are <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">blocked</span></code> and <code class="docutils literal notranslate"><span class="pre">pending</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.apimanagement.User.user_id">
<code class="descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.apimanagement.User.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Identifier for this User, which must be unique within the API Management Service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.apimanagement.User.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.User.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.apimanagement.get_api">
<code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">get_api</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.get_api" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing API Management Service.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.apimanagement.get_group">
<code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">get_group</code><span class="sig-paren">(</span><em>api_management_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing API Management Group.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.apimanagement.get_product">
<code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">get_product</code><span class="sig-paren">(</span><em>api_management_name=None</em>, <em>product_id=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.get_product" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing API Management Product.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.apimanagement.get_user">
<code class="descclassname">pulumi_azure.apimanagement.</code><code class="descname">get_user</code><span class="sig-paren">(</span><em>api_management_name=None</em>, <em>resource_group_name=None</em>, <em>user_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.apimanagement.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing API Management User.</p>
</dd></dl>

</div>
