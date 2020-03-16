---
title: Module iot
title_tag: Module iot | Package pulumi_azure | Python SDK
linktitle: iot
notitle: true
---

<div class="section" id="iot">
<h1>iot<a class="headerlink" href="#iot" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.iot"></span><dl class="class">
<dt id="pulumi_azure.iot.AwaitableGetDpsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">AwaitableGetDpsResult</code><span class="sig-paren">(</span><em class="sig-param">allocation_policy=None</em>, <em class="sig-param">device_provisioning_host_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">id_scope=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_operations_host_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.AwaitableGetDpsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.iot.AwaitableGetDpsSharedAccessPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">AwaitableGetDpsSharedAccessPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">iothub_dps_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.AwaitableGetDpsSharedAccessPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.iot.AwaitableGetSharedAccessPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">AwaitableGetSharedAccessPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.AwaitableGetSharedAccessPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.iot.ConsumerGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">ConsumerGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">eventhub_endpoint_name=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.ConsumerGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Consumer Group within an IotHub</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_consumer_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_consumer_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eventhub_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Event Hub-compatible endpoint in the IoT hub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>iothub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoT Hub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this Consumer Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group that contains the IoT hub. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.iot.ConsumerGroup.eventhub_endpoint_name">
<code class="sig-name descname">eventhub_endpoint_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.ConsumerGroup.eventhub_endpoint_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Event Hub-compatible endpoint in the IoT hub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.ConsumerGroup.iothub_name">
<code class="sig-name descname">iothub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.ConsumerGroup.iothub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IoT Hub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.ConsumerGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.ConsumerGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this Consumer Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.ConsumerGroup.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.ConsumerGroup.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group that contains the IoT hub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.ConsumerGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">eventhub_endpoint_name=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.ConsumerGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ConsumerGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eventhub_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Event Hub-compatible endpoint in the IoT hub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>iothub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoT Hub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this Consumer Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group that contains the IoT hub. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.ConsumerGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.ConsumerGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.ConsumerGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.ConsumerGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.DpsSharedAccessPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">DpsSharedAccessPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enrollment_read=None</em>, <em class="sig-param">enrollment_write=None</em>, <em class="sig-param">iothub_dps_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">registration_read=None</em>, <em class="sig-param">registration_write=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_config=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.DpsSharedAccessPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IotHub Device Provisioning Service Shared Access Policy</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_dps_shared_access_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_dps_shared_access_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enrollment_read</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">EnrollmentRead</span></code> permission to this Shared Access Account. It allows read access to enrollment data.</p></li>
<li><p><strong>enrollment_write</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">EnrollmentWrite</span></code> permission to this Shared Access Account. It allows write access to enrollment data.</p></li>
<li><p><strong>iothub_dps_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoT Hub Device Provisioning service to which this Shared Access Policy belongs. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the IotHub Shared Access Policy resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>registration_read</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">RegistrationStatusRead</span></code> permission to this Shared Access Account. It allows read access to device registrations.</p></li>
<li><p><strong>registration_write</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">RegistrationStatusWrite</span></code> permission to this Shared Access Account. It allows write access to device registrations.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the IotHub Shared Access Policy resource has to be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_config</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">ServiceConfig</span></code> permission to this Shared Access Account. It allows configuration of the Device Provisioning Service.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.iot.DpsSharedAccessPolicy.enrollment_read">
<code class="sig-name descname">enrollment_read</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.DpsSharedAccessPolicy.enrollment_read" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds <code class="docutils literal notranslate"><span class="pre">EnrollmentRead</span></code> permission to this Shared Access Account. It allows read access to enrollment data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.DpsSharedAccessPolicy.enrollment_write">
<code class="sig-name descname">enrollment_write</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.DpsSharedAccessPolicy.enrollment_write" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds <code class="docutils literal notranslate"><span class="pre">EnrollmentWrite</span></code> permission to this Shared Access Account. It allows write access to enrollment data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.DpsSharedAccessPolicy.iothub_dps_name">
<code class="sig-name descname">iothub_dps_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.DpsSharedAccessPolicy.iothub_dps_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IoT Hub Device Provisioning service to which this Shared Access Policy belongs. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.DpsSharedAccessPolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.DpsSharedAccessPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the IotHub Shared Access Policy resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.DpsSharedAccessPolicy.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.DpsSharedAccessPolicy.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string of the Shared Access Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.DpsSharedAccessPolicy.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.DpsSharedAccessPolicy.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary key used to create the authentication token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.DpsSharedAccessPolicy.registration_read">
<code class="sig-name descname">registration_read</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.DpsSharedAccessPolicy.registration_read" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds <code class="docutils literal notranslate"><span class="pre">RegistrationStatusRead</span></code> permission to this Shared Access Account. It allows read access to device registrations.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.DpsSharedAccessPolicy.registration_write">
<code class="sig-name descname">registration_write</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.DpsSharedAccessPolicy.registration_write" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds <code class="docutils literal notranslate"><span class="pre">RegistrationStatusWrite</span></code> permission to this Shared Access Account. It allows write access to device registrations.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.DpsSharedAccessPolicy.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.DpsSharedAccessPolicy.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group under which the IotHub Shared Access Policy resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.DpsSharedAccessPolicy.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.DpsSharedAccessPolicy.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string of the Shared Access Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.DpsSharedAccessPolicy.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.DpsSharedAccessPolicy.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary key used to create the authentication token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.DpsSharedAccessPolicy.service_config">
<code class="sig-name descname">service_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.DpsSharedAccessPolicy.service_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds <code class="docutils literal notranslate"><span class="pre">ServiceConfig</span></code> permission to this Shared Access Account. It allows configuration of the Device Provisioning Service.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.DpsSharedAccessPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enrollment_read=None</em>, <em class="sig-param">enrollment_write=None</em>, <em class="sig-param">iothub_dps_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">registration_read=None</em>, <em class="sig-param">registration_write=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">service_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.DpsSharedAccessPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DpsSharedAccessPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enrollment_read</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">EnrollmentRead</span></code> permission to this Shared Access Account. It allows read access to enrollment data.</p></li>
<li><p><strong>enrollment_write</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">EnrollmentWrite</span></code> permission to this Shared Access Account. It allows write access to enrollment data.</p></li>
<li><p><strong>iothub_dps_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoT Hub Device Provisioning service to which this Shared Access Policy belongs. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the IotHub Shared Access Policy resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary connection string of the Shared Access Policy.</p></li>
<li><p><strong>primary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary key used to create the authentication token.</p></li>
<li><p><strong>registration_read</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">RegistrationStatusRead</span></code> permission to this Shared Access Account. It allows read access to device registrations.</p></li>
<li><p><strong>registration_write</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">RegistrationStatusWrite</span></code> permission to this Shared Access Account. It allows write access to device registrations.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the IotHub Shared Access Policy resource has to be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secondary connection string of the Shared Access Policy.</p></li>
<li><p><strong>secondary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secondary key used to create the authentication token.</p></li>
<li><p><strong>service_config</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">ServiceConfig</span></code> permission to this Shared Access Account. It allows configuration of the Device Provisioning Service.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.DpsSharedAccessPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.DpsSharedAccessPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.DpsSharedAccessPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.DpsSharedAccessPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.EndpointEventhub">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">EndpointEventhub</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.EndpointEventhub" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IotHub EventHub Endpoint</p>
<blockquote>
<div><p><strong>NOTE:</strong> Endpoints can be defined either directly on the <code class="docutils literal notranslate"><span class="pre">iot.IoTHub</span></code> resource, or using the <code class="docutils literal notranslate"><span class="pre">azurerm_iothub_endpoint_*</span></code> resources - but the two ways of defining the endpoints cannot be used together. If both are used against the same IoTHub, spurious changes will occur. Also, defining a <code class="docutils literal notranslate"><span class="pre">azurerm_iothub_endpoint_*</span></code> resource and another endpoint of a different type directly on the <code class="docutils literal notranslate"><span class="pre">iot.IoTHub</span></code> resource is not supported.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_endpoint_eventhub.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_endpoint_eventhub.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string for the endpoint.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  <code class="docutils literal notranslate"><span class="pre">events</span></code>, <code class="docutils literal notranslate"><span class="pre">operationsMonitoringEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">fileNotifications</span></code> and <code class="docutils literal notranslate"><span class="pre">$default</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.iot.EndpointEventhub.connection_string">
<code class="sig-name descname">connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.EndpointEventhub.connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string for the endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.EndpointEventhub.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.EndpointEventhub.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  <code class="docutils literal notranslate"><span class="pre">events</span></code>, <code class="docutils literal notranslate"><span class="pre">operationsMonitoringEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">fileNotifications</span></code> and <code class="docutils literal notranslate"><span class="pre">$default</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.EndpointEventhub.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.EndpointEventhub.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EndpointEventhub resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string for the endpoint.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  <code class="docutils literal notranslate"><span class="pre">events</span></code>, <code class="docutils literal notranslate"><span class="pre">operationsMonitoringEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">fileNotifications</span></code> and <code class="docutils literal notranslate"><span class="pre">$default</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.EndpointEventhub.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.EndpointEventhub.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.EndpointEventhub.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.EndpointEventhub.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.EndpointServicebusQueue">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">EndpointServicebusQueue</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.EndpointServicebusQueue" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IotHub ServiceBus Queue Endpoint</p>
<blockquote>
<div><p><strong>NOTE:</strong> Endpoints can be defined either directly on the <code class="docutils literal notranslate"><span class="pre">iot.IoTHub</span></code> resource, or using the <code class="docutils literal notranslate"><span class="pre">azurerm_iothub_endpoint_*</span></code> resources - but the two ways of defining the endpoints cannot be used together. If both are used against the same IoTHub, spurious changes will occur. Also, defining a <code class="docutils literal notranslate"><span class="pre">azurerm_iothub_endpoint_*</span></code> resource and another endpoint of a different type directly on the <code class="docutils literal notranslate"><span class="pre">iot.IoTHub</span></code> resource is not supported.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_endpoint_servicebus_queue.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_endpoint_servicebus_queue.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string for the endpoint.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  <code class="docutils literal notranslate"><span class="pre">events</span></code>, <code class="docutils literal notranslate"><span class="pre">operationsMonitoringEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">fileNotifications</span></code> and <code class="docutils literal notranslate"><span class="pre">$default</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.iot.EndpointServicebusQueue.connection_string">
<code class="sig-name descname">connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.EndpointServicebusQueue.connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string for the endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.EndpointServicebusQueue.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.EndpointServicebusQueue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  <code class="docutils literal notranslate"><span class="pre">events</span></code>, <code class="docutils literal notranslate"><span class="pre">operationsMonitoringEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">fileNotifications</span></code> and <code class="docutils literal notranslate"><span class="pre">$default</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.EndpointServicebusQueue.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.EndpointServicebusQueue.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EndpointServicebusQueue resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string for the endpoint.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  <code class="docutils literal notranslate"><span class="pre">events</span></code>, <code class="docutils literal notranslate"><span class="pre">operationsMonitoringEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">fileNotifications</span></code> and <code class="docutils literal notranslate"><span class="pre">$default</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.EndpointServicebusQueue.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.EndpointServicebusQueue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.EndpointServicebusQueue.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.EndpointServicebusQueue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.EndpointServicebusTopic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">EndpointServicebusTopic</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.EndpointServicebusTopic" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IotHub ServiceBus Topic Endpoint</p>
<blockquote>
<div><p><strong>NOTE:</strong> Endpoints can be defined either directly on the <code class="docutils literal notranslate"><span class="pre">iot.IoTHub</span></code> resource, or using the <code class="docutils literal notranslate"><span class="pre">azurerm_iothub_endpoint_*</span></code> resources - but the two ways of defining the endpoints cannot be used together. If both are used against the same IoTHub, spurious changes will occur. Also, defining a <code class="docutils literal notranslate"><span class="pre">azurerm_iothub_endpoint_*</span></code> resource and another endpoint of a different type directly on the <code class="docutils literal notranslate"><span class="pre">iot.IoTHub</span></code> resource is not supported.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_endpoint_servicebus_topic.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_endpoint_servicebus_topic.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string for the endpoint.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  <code class="docutils literal notranslate"><span class="pre">events</span></code>, <code class="docutils literal notranslate"><span class="pre">operationsMonitoringEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">fileNotifications</span></code> and <code class="docutils literal notranslate"><span class="pre">$default</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.iot.EndpointServicebusTopic.connection_string">
<code class="sig-name descname">connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.EndpointServicebusTopic.connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string for the endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.EndpointServicebusTopic.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.EndpointServicebusTopic.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  <code class="docutils literal notranslate"><span class="pre">events</span></code>, <code class="docutils literal notranslate"><span class="pre">operationsMonitoringEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">fileNotifications</span></code> and <code class="docutils literal notranslate"><span class="pre">$default</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.EndpointServicebusTopic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.EndpointServicebusTopic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EndpointServicebusTopic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string for the endpoint.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  <code class="docutils literal notranslate"><span class="pre">events</span></code>, <code class="docutils literal notranslate"><span class="pre">operationsMonitoringEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">fileNotifications</span></code> and <code class="docutils literal notranslate"><span class="pre">$default</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.EndpointServicebusTopic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.EndpointServicebusTopic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.EndpointServicebusTopic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.EndpointServicebusTopic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.EndpointStorageContainer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">EndpointStorageContainer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">batch_frequency_in_seconds=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">container_name=None</em>, <em class="sig-param">encoding=None</em>, <em class="sig-param">file_name_format=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">max_chunk_size_in_bytes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.EndpointStorageContainer" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IotHub Storage Container Endpoint</p>
<blockquote>
<div><p><strong>NOTE:</strong> Endpoints can be defined either directly on the <code class="docutils literal notranslate"><span class="pre">iot.IoTHub</span></code> resource, or using the <code class="docutils literal notranslate"><span class="pre">azurerm_iothub_endpoint_*</span></code> resources - but the two ways of defining the endpoints cannot be used together. If both are used against the same IoTHub, spurious changes will occur. Also, defining a <code class="docutils literal notranslate"><span class="pre">azurerm_iothub_endpoint_*</span></code> resource and another endpoint of a different type directly on the <code class="docutils literal notranslate"><span class="pre">iot.IoTHub</span></code> resource is not supported.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_endpoint_storage_container.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_endpoint_storage_container.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>batch_frequency_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time interval at which blobs are written to storage. Value should be between 60 and 720 seconds. Default value is 300 seconds.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string for the endpoint.</p></li>
<li><p><strong>container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of storage container in the storage account.
*</p></li>
<li><p><strong>encoding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Encoding that is used to serialize messages to blobs. Supported values are ‘avro’ and ‘avrodeflate’. Default value is ‘avro’.</p></li>
<li><p><strong>file_name_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – File name format for the blob. Default format is <code class="docutils literal notranslate"><span class="pre">{iothub}/{partition}/{YYYY}/{MM}/{DD}/{HH}/{mm}</span></code>. All parameters are mandatory but can be reordered.</p></li>
<li><p><strong>iothub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoTHub to which this Storage Container Endpoint belongs. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_chunk_size_in_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum number of bytes for each blob written to storage. Value should be between 10485760(10MB) and 524288000(500MB). Default value is 314572800(300MB).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  <code class="docutils literal notranslate"><span class="pre">events</span></code>, <code class="docutils literal notranslate"><span class="pre">operationsMonitoringEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">fileNotifications</span></code> and <code class="docutils literal notranslate"><span class="pre">$default</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the IotHub Storage Container Endpoint resource has to be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.iot.EndpointStorageContainer.batch_frequency_in_seconds">
<code class="sig-name descname">batch_frequency_in_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.EndpointStorageContainer.batch_frequency_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Time interval at which blobs are written to storage. Value should be between 60 and 720 seconds. Default value is 300 seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.EndpointStorageContainer.connection_string">
<code class="sig-name descname">connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.EndpointStorageContainer.connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection string for the endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.EndpointStorageContainer.container_name">
<code class="sig-name descname">container_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.EndpointStorageContainer.container_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of storage container in the storage account.
*</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.EndpointStorageContainer.encoding">
<code class="sig-name descname">encoding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.EndpointStorageContainer.encoding" title="Permalink to this definition">¶</a></dt>
<dd><p>Encoding that is used to serialize messages to blobs. Supported values are ‘avro’ and ‘avrodeflate’. Default value is ‘avro’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.EndpointStorageContainer.file_name_format">
<code class="sig-name descname">file_name_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.EndpointStorageContainer.file_name_format" title="Permalink to this definition">¶</a></dt>
<dd><p>File name format for the blob. Default format is <code class="docutils literal notranslate"><span class="pre">{iothub}/{partition}/{YYYY}/{MM}/{DD}/{HH}/{mm}</span></code>. All parameters are mandatory but can be reordered.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.EndpointStorageContainer.iothub_name">
<code class="sig-name descname">iothub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.EndpointStorageContainer.iothub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IoTHub to which this Storage Container Endpoint belongs. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.EndpointStorageContainer.max_chunk_size_in_bytes">
<code class="sig-name descname">max_chunk_size_in_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.EndpointStorageContainer.max_chunk_size_in_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum number of bytes for each blob written to storage. Value should be between 10485760(10MB) and 524288000(500MB). Default value is 314572800(300MB).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.EndpointStorageContainer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.EndpointStorageContainer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  <code class="docutils literal notranslate"><span class="pre">events</span></code>, <code class="docutils literal notranslate"><span class="pre">operationsMonitoringEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">fileNotifications</span></code> and <code class="docutils literal notranslate"><span class="pre">$default</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.EndpointStorageContainer.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.EndpointStorageContainer.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group under which the IotHub Storage Container Endpoint resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.EndpointStorageContainer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">batch_frequency_in_seconds=None</em>, <em class="sig-param">connection_string=None</em>, <em class="sig-param">container_name=None</em>, <em class="sig-param">encoding=None</em>, <em class="sig-param">file_name_format=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">max_chunk_size_in_bytes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.EndpointStorageContainer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EndpointStorageContainer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>batch_frequency_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time interval at which blobs are written to storage. Value should be between 60 and 720 seconds. Default value is 300 seconds.</p></li>
<li><p><strong>connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection string for the endpoint.</p></li>
<li><p><strong>container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of storage container in the storage account.
*</p></li>
<li><p><strong>encoding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Encoding that is used to serialize messages to blobs. Supported values are ‘avro’ and ‘avrodeflate’. Default value is ‘avro’.</p></li>
<li><p><strong>file_name_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – File name format for the blob. Default format is <code class="docutils literal notranslate"><span class="pre">{iothub}/{partition}/{YYYY}/{MM}/{DD}/{HH}/{mm}</span></code>. All parameters are mandatory but can be reordered.</p></li>
<li><p><strong>iothub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoTHub to which this Storage Container Endpoint belongs. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_chunk_size_in_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum number of bytes for each blob written to storage. Value should be between 10485760(10MB) and 524288000(500MB). Default value is 314572800(300MB).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  <code class="docutils literal notranslate"><span class="pre">events</span></code>, <code class="docutils literal notranslate"><span class="pre">operationsMonitoringEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">fileNotifications</span></code> and <code class="docutils literal notranslate"><span class="pre">$default</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the IotHub Storage Container Endpoint resource has to be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.EndpointStorageContainer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.EndpointStorageContainer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.EndpointStorageContainer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.EndpointStorageContainer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.FallbackRoute">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">FallbackRoute</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">endpoint_names=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.FallbackRoute" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IotHub Fallback Route</p>
<blockquote>
<div><p><strong>Note:</strong> Fallback route can be defined either directly on the <code class="docutils literal notranslate"><span class="pre">iot.IoTHub</span></code> resource, or using the <code class="docutils literal notranslate"><span class="pre">iot.FallbackRoute</span></code> resource - but the two cannot be used together. If both are used against the same IoTHub, spurious changes will occur.</p>
<p><strong>Note:</strong> Since this resource is provisioned by default, the Azure Provider will not check for the presence of an existing resource prior to attempting to create it.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_fallback_route.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_fallback_route.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to <code class="docutils literal notranslate"><span class="pre">true</span></code> by default. For grammar, see: <a class="reference external" href="https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language">https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language</a>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Used to specify whether the fallback route is enabled.</p></li>
<li><p><strong>endpoint_names</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoints to which messages that satisfy the condition are routed. Currently only 1 endpoint is allowed.</p></li>
<li><p><strong>iothub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoTHub to which this Fallback Route belongs. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the IotHub Storage Container Endpoint resource has to be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.iot.FallbackRoute.condition">
<code class="sig-name descname">condition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.FallbackRoute.condition" title="Permalink to this definition">¶</a></dt>
<dd><p>The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to <code class="docutils literal notranslate"><span class="pre">true</span></code> by default. For grammar, see: <a class="reference external" href="https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language">https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.FallbackRoute.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.FallbackRoute.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to specify whether the fallback route is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.FallbackRoute.endpoint_names">
<code class="sig-name descname">endpoint_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.FallbackRoute.endpoint_names" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoints to which messages that satisfy the condition are routed. Currently only 1 endpoint is allowed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.FallbackRoute.iothub_name">
<code class="sig-name descname">iothub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.FallbackRoute.iothub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IoTHub to which this Fallback Route belongs. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.FallbackRoute.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.FallbackRoute.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group under which the IotHub Storage Container Endpoint resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.FallbackRoute.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">endpoint_names=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.FallbackRoute.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FallbackRoute resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to <code class="docutils literal notranslate"><span class="pre">true</span></code> by default. For grammar, see: <a class="reference external" href="https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language">https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language</a>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Used to specify whether the fallback route is enabled.</p></li>
<li><p><strong>endpoint_names</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoints to which messages that satisfy the condition are routed. Currently only 1 endpoint is allowed.</p></li>
<li><p><strong>iothub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoTHub to which this Fallback Route belongs. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the IotHub Storage Container Endpoint resource has to be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.FallbackRoute.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.FallbackRoute.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.FallbackRoute.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.FallbackRoute.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.GetDpsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">GetDpsResult</code><span class="sig-paren">(</span><em class="sig-param">allocation_policy=None</em>, <em class="sig-param">device_provisioning_host_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">id_scope=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_operations_host_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.GetDpsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDps.</p>
<dl class="attribute">
<dt id="pulumi_azure.iot.GetDpsResult.allocation_policy">
<code class="sig-name descname">allocation_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.GetDpsResult.allocation_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The allocation policy of the IoT Device Provisioning Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.GetDpsResult.device_provisioning_host_name">
<code class="sig-name descname">device_provisioning_host_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.GetDpsResult.device_provisioning_host_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The device endpoint of the IoT Device Provisioning Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.GetDpsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.GetDpsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.GetDpsResult.id_scope">
<code class="sig-name descname">id_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.GetDpsResult.id_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the IoT Device Provisioning Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.GetDpsResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.GetDpsResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the IoT Device Provisioning Service exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.GetDpsResult.service_operations_host_name">
<code class="sig-name descname">service_operations_host_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.GetDpsResult.service_operations_host_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The service endpoint of the IoT Device Provisioning Service.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.iot.GetDpsSharedAccessPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">GetDpsSharedAccessPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">iothub_dps_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.GetDpsSharedAccessPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDpsSharedAccessPolicy.</p>
<dl class="attribute">
<dt id="pulumi_azure.iot.GetDpsSharedAccessPolicyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.GetDpsSharedAccessPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.GetDpsSharedAccessPolicyResult.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.GetDpsSharedAccessPolicyResult.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string of the Shared Access Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.GetDpsSharedAccessPolicyResult.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.GetDpsSharedAccessPolicyResult.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary key used to create the authentication token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.GetDpsSharedAccessPolicyResult.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.GetDpsSharedAccessPolicyResult.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string of the Shared Access Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.GetDpsSharedAccessPolicyResult.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.GetDpsSharedAccessPolicyResult.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary key used to create the authentication token.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.iot.GetSharedAccessPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">GetSharedAccessPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.GetSharedAccessPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSharedAccessPolicy.</p>
<dl class="attribute">
<dt id="pulumi_azure.iot.GetSharedAccessPolicyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.GetSharedAccessPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.GetSharedAccessPolicyResult.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.GetSharedAccessPolicyResult.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string of the Shared Access Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.GetSharedAccessPolicyResult.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.GetSharedAccessPolicyResult.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary key used to create the authentication token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.GetSharedAccessPolicyResult.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.GetSharedAccessPolicyResult.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string of the Shared Access Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.GetSharedAccessPolicyResult.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.GetSharedAccessPolicyResult.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary key used to create the authentication token.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.iot.IoTHub">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">IoTHub</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">endpoints=None</em>, <em class="sig-param">event_hub_partition_count=None</em>, <em class="sig-param">event_hub_retention_in_days=None</em>, <em class="sig-param">fallback_route=None</em>, <em class="sig-param">file_upload=None</em>, <em class="sig-param">ip_filter_rules=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">routes=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.IoTHub" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IotHub</p>
<blockquote>
<div><p><strong>NOTE:</strong> Endpoints can be defined either directly on the <code class="docutils literal notranslate"><span class="pre">iot.IoTHub</span></code> resource, or using the <code class="docutils literal notranslate"><span class="pre">azurerm_iothub_endpoint_*</span></code> resources - but the two ways of defining the endpoints cannot be used together. If both are used against the same IoTHub, spurious changes will occur. Also, defining a <code class="docutils literal notranslate"><span class="pre">azurerm_iothub_endpoint_*</span></code> resource and another endpoint of a different type directly on the <code class="docutils literal notranslate"><span class="pre">iot.IoTHub</span></code> resource is not supported.</p>
<p><strong>NOTE:</strong> Routes can be defined either directly on the <code class="docutils literal notranslate"><span class="pre">iot.IoTHub</span></code> resource, or using the <code class="docutils literal notranslate"><span class="pre">iot.Route</span></code> resource - but the two cannot be used together. If both are used against the same IoTHub, spurious changes will occur.</p>
<p><strong>NOTE:</strong> Fallback route can be defined either directly on the <code class="docutils literal notranslate"><span class="pre">iot.IoTHub</span></code> resource, or using the <code class="docutils literal notranslate"><span class="pre">iot.FallbackRoute</span></code> resource - but the two cannot be used together. If both are used against the same IoTHub, spurious changes will occur.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">endpoint</span></code> block as defined below.</p></li>
<li><p><strong>event_hub_partition_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of device-to-cloud partitions used by backing event hubs. Must be between <code class="docutils literal notranslate"><span class="pre">2</span></code> and <code class="docutils literal notranslate"><span class="pre">128</span></code>.</p></li>
<li><p><strong>event_hub_retention_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The event hub retention to use in days. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">7</span></code>.</p></li>
<li><p><strong>fallback_route</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">fallback_route</span></code> block as defined below. If the fallback route is enabled, messages that don’t match any of the supplied routes are automatically sent to this route. Defaults to messages/events.</p></li>
<li><p><strong>file_upload</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">file_upload</span></code> block as defined below.</p></li>
<li><p><strong>ip_filter_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">ip_filter_rule</span></code> blocks as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>routes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">route</span></code> block as defined below.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>endpoints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">batch_frequency_in_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_string</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">container_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">file_name_format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_chunk_size_in_bytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>fallback_route</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">condition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint_names</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>file_upload</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connection_string</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">container_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lock_duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_delivery_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notifications</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ip_filter_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipMask</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>routes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">condition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint_names</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.endpoints">
<code class="sig-name descname">endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">endpoint</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">batch_frequency_in_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_string</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">container_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">file_name_format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_chunk_size_in_bytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.event_hub_events_endpoint">
<code class="sig-name descname">event_hub_events_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.event_hub_events_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The EventHub compatible endpoint for events data</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.event_hub_events_path">
<code class="sig-name descname">event_hub_events_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.event_hub_events_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The EventHub compatible path for events data</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.event_hub_operations_endpoint">
<code class="sig-name descname">event_hub_operations_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.event_hub_operations_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The EventHub compatible endpoint for operational data</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.event_hub_operations_path">
<code class="sig-name descname">event_hub_operations_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.event_hub_operations_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The EventHub compatible path for operational data</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.event_hub_partition_count">
<code class="sig-name descname">event_hub_partition_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.event_hub_partition_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of device-to-cloud partitions used by backing event hubs. Must be between <code class="docutils literal notranslate"><span class="pre">2</span></code> and <code class="docutils literal notranslate"><span class="pre">128</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.event_hub_retention_in_days">
<code class="sig-name descname">event_hub_retention_in_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.event_hub_retention_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>The event hub retention to use in days. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">7</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.fallback_route">
<code class="sig-name descname">fallback_route</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.fallback_route" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">fallback_route</span></code> block as defined below. If the fallback route is enabled, messages that don’t match any of the supplied routes are automatically sent to this route. Defaults to messages/events.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">condition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint_names</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.file_upload">
<code class="sig-name descname">file_upload</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.file_upload" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">file_upload</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connection_string</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">container_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lock_duration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_delivery_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notifications</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.hostname">
<code class="sig-name descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname of the IotHub Resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.ip_filter_rules">
<code class="sig-name descname">ip_filter_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.ip_filter_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">ip_filter_rule</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipMask</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.routes">
<code class="sig-name descname">routes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.routes" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">route</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">condition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint_names</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.shared_access_policies">
<code class="sig-name descname">shared_access_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.shared_access_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">shared_access_policy</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the shared access policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The permissions assigned to the shared access policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The primary key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secondary_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The secondary key.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.IoTHub.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">endpoints=None</em>, <em class="sig-param">event_hub_events_endpoint=None</em>, <em class="sig-param">event_hub_events_path=None</em>, <em class="sig-param">event_hub_operations_endpoint=None</em>, <em class="sig-param">event_hub_operations_path=None</em>, <em class="sig-param">event_hub_partition_count=None</em>, <em class="sig-param">event_hub_retention_in_days=None</em>, <em class="sig-param">fallback_route=None</em>, <em class="sig-param">file_upload=None</em>, <em class="sig-param">hostname=None</em>, <em class="sig-param">ip_filter_rules=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">routes=None</em>, <em class="sig-param">shared_access_policies=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.IoTHub.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IoTHub resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">endpoint</span></code> block as defined below.</p></li>
<li><p><strong>event_hub_events_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EventHub compatible endpoint for events data</p></li>
<li><p><strong>event_hub_events_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EventHub compatible path for events data</p></li>
<li><p><strong>event_hub_operations_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EventHub compatible endpoint for operational data</p></li>
<li><p><strong>event_hub_operations_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EventHub compatible path for operational data</p></li>
<li><p><strong>event_hub_partition_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of device-to-cloud partitions used by backing event hubs. Must be between <code class="docutils literal notranslate"><span class="pre">2</span></code> and <code class="docutils literal notranslate"><span class="pre">128</span></code>.</p></li>
<li><p><strong>event_hub_retention_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The event hub retention to use in days. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">7</span></code>.</p></li>
<li><p><strong>fallback_route</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">fallback_route</span></code> block as defined below. If the fallback route is enabled, messages that don’t match any of the supplied routes are automatically sent to this route. Defaults to messages/events.</p></li>
<li><p><strong>file_upload</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">file_upload</span></code> block as defined below.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname of the IotHub Resource.</p></li>
<li><p><strong>ip_filter_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">ip_filter_rule</span></code> blocks as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>routes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">route</span></code> block as defined below.</p></li>
<li><p><strong>shared_access_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">shared_access_policy</span></code> blocks as defined below.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>endpoints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">batch_frequency_in_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_string</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">container_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encoding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">file_name_format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_chunk_size_in_bytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>fallback_route</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">condition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint_names</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>file_upload</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connection_string</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">container_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lock_duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_delivery_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notifications</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ip_filter_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipMask</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>routes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">condition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint_names</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>shared_access_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the shared access policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The permissions assigned to the shared access policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The primary key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secondary_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secondary key.</p></li>
</ul>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.IoTHub.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.IoTHub.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.IoTHub.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.IoTHub.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.IotHubCertificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">IotHubCertificate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">certificate_content=None</em>, <em class="sig-param">iot_dps_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.IotHubCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IotHub Device Provisioning Service Certificate.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_dps_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_dps_certificate.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate_content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base-64 representation of the X509 leaf certificate .cer file or just a .pem file content.</p></li>
<li><p><strong>iot_dps_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoT Device Provisioning Service that this certificate will be attached to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Iot Device Provisioning Service Certificate resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the Iot Device Provisioning Service Certificate resource has to be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.iot.IotHubCertificate.certificate_content">
<code class="sig-name descname">certificate_content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IotHubCertificate.certificate_content" title="Permalink to this definition">¶</a></dt>
<dd><p>The Base-64 representation of the X509 leaf certificate .cer file or just a .pem file content.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IotHubCertificate.iot_dps_name">
<code class="sig-name descname">iot_dps_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IotHubCertificate.iot_dps_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IoT Device Provisioning Service that this certificate will be attached to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IotHubCertificate.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IotHubCertificate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Iot Device Provisioning Service Certificate resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IotHubCertificate.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IotHubCertificate.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group under which the Iot Device Provisioning Service Certificate resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.IotHubCertificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">certificate_content=None</em>, <em class="sig-param">iot_dps_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.IotHubCertificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IotHubCertificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate_content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base-64 representation of the X509 leaf certificate .cer file or just a .pem file content.</p></li>
<li><p><strong>iot_dps_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoT Device Provisioning Service that this certificate will be attached to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Iot Device Provisioning Service Certificate resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the Iot Device Provisioning Service Certificate resource has to be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.IotHubCertificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.IotHubCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.IotHubCertificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.IotHubCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.IotHubDps">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">IotHubDps</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">linked_hubs=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.IotHubDps" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IotHub Device Provisioning Service.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_dps.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_dps.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>linked_hubs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">linked_hub</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Iot Device Provisioning Service resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the Iot Device Provisioning Service resource has to be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>linked_hubs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allocationWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">applyAllocationPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_string</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Iot Device Provisioning Service resource. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.iot.IotHubDps.allocation_policy">
<code class="sig-name descname">allocation_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IotHubDps.allocation_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The allocation policy of the IoT Device Provisioning Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IotHubDps.device_provisioning_host_name">
<code class="sig-name descname">device_provisioning_host_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IotHubDps.device_provisioning_host_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The device endpoint of the IoT Device Provisioning Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IotHubDps.id_scope">
<code class="sig-name descname">id_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IotHubDps.id_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the IoT Device Provisioning Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IotHubDps.linked_hubs">
<code class="sig-name descname">linked_hubs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IotHubDps.linked_hubs" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">linked_hub</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allocationWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">applyAllocationPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_string</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IotHubDps.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IotHubDps.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IotHubDps.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IotHubDps.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Iot Device Provisioning Service resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IotHubDps.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IotHubDps.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group under which the Iot Device Provisioning Service resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IotHubDps.service_operations_host_name">
<code class="sig-name descname">service_operations_host_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IotHubDps.service_operations_host_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The service endpoint of the IoT Device Provisioning Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IotHubDps.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IotHubDps.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Iot Device Provisioning Service resource. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IotHubDps.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IotHubDps.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.IotHubDps.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allocation_policy=None</em>, <em class="sig-param">device_provisioning_host_name=None</em>, <em class="sig-param">id_scope=None</em>, <em class="sig-param">linked_hubs=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_operations_host_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.IotHubDps.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IotHubDps resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocation_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The allocation policy of the IoT Device Provisioning Service.</p></li>
<li><p><strong>device_provisioning_host_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The device endpoint of the IoT Device Provisioning Service.</p></li>
<li><p><strong>id_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the IoT Device Provisioning Service.</p></li>
<li><p><strong>linked_hubs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">linked_hub</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Iot Device Provisioning Service resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the Iot Device Provisioning Service resource has to be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_operations_host_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service endpoint of the IoT Device Provisioning Service.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>linked_hubs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allocationWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">applyAllocationPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_string</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Iot Device Provisioning Service resource. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.IotHubDps.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.IotHubDps.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.IotHubDps.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.IotHubDps.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.Route">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">Route</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">endpoint_names=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.Route" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IotHub Route</p>
<blockquote>
<div><p><strong>NOTE:</strong> Routes can be defined either directly on the <code class="docutils literal notranslate"><span class="pre">iot.IoTHub</span></code> resource, or using the <code class="docutils literal notranslate"><span class="pre">iot.Route</span></code> resourcs - but the two cannot be used together. If both are used against the same IoTHub, spurious changes will occur.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_route.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_route.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to <code class="docutils literal notranslate"><span class="pre">true</span></code> by default. For grammar, see: <a class="reference external" href="https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language">https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language</a>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether a route is enabled.</p></li>
<li><p><strong>endpoint_names</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The list of endpoints to which messages that satisfy the condition are routed. Currently only one endpoint is allowed.</p></li>
<li><p><strong>iothub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoTHub to which this Route belongs. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the route.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the IotHub Route resource has to be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source that the routing rule is to be applied to. Possible values include: <code class="docutils literal notranslate"><span class="pre">DeviceJobLifecycleEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">DeviceLifecycleEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">DeviceMessages</span></code>, <code class="docutils literal notranslate"><span class="pre">Invalid</span></code>, <code class="docutils literal notranslate"><span class="pre">TwinChangeEvents</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.iot.Route.condition">
<code class="sig-name descname">condition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.Route.condition" title="Permalink to this definition">¶</a></dt>
<dd><p>The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to <code class="docutils literal notranslate"><span class="pre">true</span></code> by default. For grammar, see: <a class="reference external" href="https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language">https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.Route.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.Route.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether a route is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.Route.endpoint_names">
<code class="sig-name descname">endpoint_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.Route.endpoint_names" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of endpoints to which messages that satisfy the condition are routed. Currently only one endpoint is allowed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.Route.iothub_name">
<code class="sig-name descname">iothub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.Route.iothub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IoTHub to which this Route belongs. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.Route.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.Route.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the route.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.Route.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.Route.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group under which the IotHub Route resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.Route.source">
<code class="sig-name descname">source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.Route.source" title="Permalink to this definition">¶</a></dt>
<dd><p>The source that the routing rule is to be applied to. Possible values include: <code class="docutils literal notranslate"><span class="pre">DeviceJobLifecycleEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">DeviceLifecycleEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">DeviceMessages</span></code>, <code class="docutils literal notranslate"><span class="pre">Invalid</span></code>, <code class="docutils literal notranslate"><span class="pre">TwinChangeEvents</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.Route.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">endpoint_names=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.Route.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Route resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The condition that is evaluated to apply the routing rule. If no condition is provided, it evaluates to <code class="docutils literal notranslate"><span class="pre">true</span></code> by default. For grammar, see: <a class="reference external" href="https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language">https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-query-language</a>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether a route is enabled.</p></li>
<li><p><strong>endpoint_names</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The list of endpoints to which messages that satisfy the condition are routed. Currently only one endpoint is allowed.</p></li>
<li><p><strong>iothub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoTHub to which this Route belongs. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the route.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the IotHub Route resource has to be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source that the routing rule is to be applied to. Possible values include: <code class="docutils literal notranslate"><span class="pre">DeviceJobLifecycleEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">DeviceLifecycleEvents</span></code>, <code class="docutils literal notranslate"><span class="pre">DeviceMessages</span></code>, <code class="docutils literal notranslate"><span class="pre">Invalid</span></code>, <code class="docutils literal notranslate"><span class="pre">TwinChangeEvents</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.Route.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.Route.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.Route.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.Route.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.SharedAccessPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">SharedAccessPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">device_connect=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">registry_read=None</em>, <em class="sig-param">registry_write=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_connect=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IotHub Shared Access Policy</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_shared_access_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_shared_access_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>device_connect</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">DeviceConnect</span></code> permission to this Shared Access Account. It allows sending and receiving on the device-side endpoints.</p></li>
<li><p><strong>iothub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoTHub to which this Shared Access Policy belongs. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the IotHub Shared Access Policy resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>registry_read</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">RegistryRead</span></code> permission to this Shared Access Account. It allows read access to the identity registry.</p></li>
<li><p><strong>registry_write</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">RegistryWrite</span></code> permission to this Shared Access Account. It allows write access to the identity registry.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the IotHub Shared Access Policy resource has to be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_connect</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">ServiceConnect</span></code> permission to this Shared Access Account. It allows sending and receiving on the cloud-side endpoints.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.device_connect">
<code class="sig-name descname">device_connect</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.device_connect" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds <code class="docutils literal notranslate"><span class="pre">DeviceConnect</span></code> permission to this Shared Access Account. It allows sending and receiving on the device-side endpoints.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.iothub_name">
<code class="sig-name descname">iothub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.iothub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IoTHub to which this Shared Access Policy belongs. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the IotHub Shared Access Policy resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.primary_connection_string">
<code class="sig-name descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string of the Shared Access Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary key used to create the authentication token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.registry_read">
<code class="sig-name descname">registry_read</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.registry_read" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds <code class="docutils literal notranslate"><span class="pre">RegistryRead</span></code> permission to this Shared Access Account. It allows read access to the identity registry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.registry_write">
<code class="sig-name descname">registry_write</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.registry_write" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds <code class="docutils literal notranslate"><span class="pre">RegistryWrite</span></code> permission to this Shared Access Account. It allows write access to the identity registry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group under which the IotHub Shared Access Policy resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.secondary_connection_string">
<code class="sig-name descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string of the Shared Access Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary key used to create the authentication token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.service_connect">
<code class="sig-name descname">service_connect</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.service_connect" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds <code class="docutils literal notranslate"><span class="pre">ServiceConnect</span></code> permission to this Shared Access Account. It allows sending and receiving on the cloud-side endpoints.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.SharedAccessPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">device_connect=None</em>, <em class="sig-param">iothub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">primary_connection_string=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">registry_read=None</em>, <em class="sig-param">registry_write=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_connection_string=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">service_connect=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SharedAccessPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>device_connect</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">DeviceConnect</span></code> permission to this Shared Access Account. It allows sending and receiving on the device-side endpoints.</p></li>
<li><p><strong>iothub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoTHub to which this Shared Access Policy belongs. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the IotHub Shared Access Policy resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary connection string of the Shared Access Policy.</p></li>
<li><p><strong>primary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The primary key used to create the authentication token.</p></li>
<li><p><strong>registry_read</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">RegistryRead</span></code> permission to this Shared Access Account. It allows read access to the identity registry.</p></li>
<li><p><strong>registry_write</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">RegistryWrite</span></code> permission to this Shared Access Account. It allows write access to the identity registry.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the IotHub Shared Access Policy resource has to be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_connection_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secondary connection string of the Shared Access Policy.</p></li>
<li><p><strong>secondary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secondary key used to create the authentication token.</p></li>
<li><p><strong>service_connect</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">ServiceConnect</span></code> permission to this Shared Access Account. It allows sending and receiving on the cloud-side endpoints.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.SharedAccessPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.SharedAccessPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.get_dps">
<code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">get_dps</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.get_dps" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing IotHub Device Provisioning Service.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/iothub_dps.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/iothub_dps.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Iot Device Provisioning Service resource.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group under which the Iot Device Provisioning Service is located in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.iot.get_dps_shared_access_policy">
<code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">get_dps_shared_access_policy</code><span class="sig-paren">(</span><em class="sig-param">iothub_dps_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.get_dps_shared_access_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing IotHub Device Provisioning Service Shared Access Policy</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/iothub_dps_shared_access_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/iothub_dps_shared_access_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>iothub_dps_name</strong> (<em>str</em>) – Specifies the name of the IoT Hub Device Provisioning service to which the Shared Access Policy belongs.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the IotHub Shared Access Policy.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group under which the IotHub Shared Access Policy resource exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.iot.get_shared_access_policy">
<code class="sig-prename descclassname">pulumi_azure.iot.</code><code class="sig-name descname">get_shared_access_policy</code><span class="sig-paren">(</span><em class="sig-param">iothub_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.get_shared_access_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing IotHub Shared Access Policy</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/iothub_shared_access_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/iothub_shared_access_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>iothub_name</strong> (<em>str</em>) – The name of the IoTHub to which this Shared Access Policy belongs.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the IotHub Shared Access Policy resource.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group under which the IotHub Shared Access Policy resource has to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
