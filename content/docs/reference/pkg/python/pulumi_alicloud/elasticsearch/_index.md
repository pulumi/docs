---
title: Module elasticsearch
title_tag: Module elasticsearch | Package pulumi_alicloud | Python SDK
linktitle: elasticsearch
notitle: true
---

<div class="section" id="elasticsearch">
<h1>elasticsearch<a class="headerlink" href="#elasticsearch" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.elasticsearch"></span><dl class="class">
<dt id="pulumi_alicloud.elasticsearch.AwaitableGetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.elasticsearch.</code><code class="sig-name descname">AwaitableGetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param">description_regex=None</em>, <em class="sig-param">descriptions=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.elasticsearch.AwaitableGetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.elasticsearch.GetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.elasticsearch.</code><code class="sig-name descname">GetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param">description_regex=None</em>, <em class="sig-param">descriptions=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.elasticsearch.GetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstances.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.GetInstancesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.GetInstancesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.elasticsearch.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.elasticsearch.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">data_node_amount=None</em>, <em class="sig-param">data_node_disk_size=None</em>, <em class="sig-param">data_node_disk_type=None</em>, <em class="sig-param">data_node_spec=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">instance_charge_type=None</em>, <em class="sig-param">kibana_whitelists=None</em>, <em class="sig-param">kms_encrypted_password=None</em>, <em class="sig-param">kms_encryption_context=None</em>, <em class="sig-param">master_node_spec=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">private_whitelists=None</em>, <em class="sig-param">public_whitelists=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">zone_count=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Elasticsearch instance resource. It contains data nodes, dedicated master node(optional) and etc. It can be associated with private IP whitelists and kibana IP whitelist.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Only one operation is supported in a request. So if <code class="docutils literal notranslate"><span class="pre">data_node_spec</span></code> and <code class="docutils literal notranslate"><span class="pre">data_node_disk_size</span></code> are both changed, system will respond error.</p>
<p><strong>NOTE:</strong> At present, <code class="docutils literal notranslate"><span class="pre">version</span></code> can not be modified once instance has been created.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data_node_amount</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Elasticsearch cluster’s data node quantity, between 2 and 50.</p></li>
<li><p><strong>data_node_disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The single data node storage space.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `cloud_ssd`: An SSD disk, supports a maximum of 2048 GiB (2 TB).
- `cloud_efficiency` An ultra disk, supports a maximum of 5120 GiB (5 TB). If the data to be stored is larger than 2048 GiB, an ultra disk can only support the following data sizes (GiB): [`2560`, `3072`, `3584`, `4096`, `4608`, `5120`].
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>data_node_disk_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data node disk type. Supported values: cloud_ssd, cloud_efficiency.</p></li>
<li><p><strong>data_node_spec</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data node specifications of the Elasticsearch instance.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of instance. It a string of 0 to 30 characters.</p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. From version 1.69.0, the Elasticsearch cluster allows you to update your instance_charge_ype from <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code> to <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, the following attributes are required: <code class="docutils literal notranslate"><span class="pre">period</span></code>. But, updating from <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code> to <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> is not supported.</p></li>
<li><p><strong>kibana_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set the Kibana’s IP whitelist in internet network.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to a instance. If the <code class="docutils literal notranslate"><span class="pre">password</span></code> is filled in, this field will be ignored, but you have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating instance with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p></li>
<li><p><strong>master_node*spec</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The dedicated master node spec. If specified, dedicated master node will be created.</p>
</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of the instance. The password can be 8 to 30 characters in length and must contain three of the following conditions: uppercase letters, lowercase letters, numbers, and special characters (<cite>!&#64;#$%^&amp;*()*+-=`</cite>).</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy Elasticsearch instance (in month). It is valid when instance_charge_type is``PrePaid<code class="docutils literal notranslate"><span class="pre">.</span> <span class="pre">Valid</span> <span class="pre">values:</span> <span class="pre">[1~9],</span> <span class="pre">12,</span> <span class="pre">24,</span> <span class="pre">36.</span> <span class="pre">Default</span> <span class="pre">to</span> <span class="pre">1.</span> <span class="pre">From</span> <span class="pre">version</span> <span class="pre">1.69.2,</span> <span class="pre">when</span> <span class="pre">to</span> <span class="pre">modify</span> <span class="pre">this</span> <span class="pre">value,</span> <span class="pre">the</span> <span class="pre">resource</span> <span class="pre">can</span> <span class="pre">renewal</span> <span class="pre">a</span></code>PrePaid<a href="#id3"><span class="problematic" id="id4">``</span></a>instance.</p></li>
<li><p><strong>private_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set the instance’s IP whitelist in VPC network.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Elasticsearch version. Supported values:<code class="docutils literal notranslate"><span class="pre">\</span> <span class="pre">5.5.3_with_X-Pack\</span> <span class="pre">``,</span></code>6.3_with_X-Pack<code class="docutils literal notranslate"><span class="pre">and</span></code>6.7_with_X-Pack<a href="#id5"><span class="problematic" id="id6">``</span></a>.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of VSwitch.</p></li>
<li><p><strong>zone_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Multi-AZ supported for Elasticsearch, between 1 and 3. The``data_node_amount<code class="docutils literal notranslate"><span class="pre">value</span> <span class="pre">must</span> <span class="pre">be</span> <span class="pre">an</span> <span class="pre">integral</span> <span class="pre">multiple</span> <span class="pre">of</span> <span class="pre">the</span></code>zone_count` value.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/elasticsearch_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/elasticsearch_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.data_node_amount">
<code class="sig-name descname">data_node_amount</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.data_node_amount" title="Permalink to this definition">¶</a></dt>
<dd><p>The Elasticsearch cluster’s data node quantity, between 2 and 50.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.data_node_disk_size">
<code class="sig-name descname">data_node_disk_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.data_node_disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The single data node storage space.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>: An SSD disk, supports a maximum of 2048 GiB (2 TB).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code> An ultra disk, supports a maximum of 5120 GiB (5 TB). If the data to be stored is larger than 2048 GiB, an ultra disk can only support the following data sizes (GiB): [<code class="docutils literal notranslate"><span class="pre">2560</span></code>, <code class="docutils literal notranslate"><span class="pre">3072</span></code>, <code class="docutils literal notranslate"><span class="pre">3584</span></code>, <code class="docutils literal notranslate"><span class="pre">4096</span></code>, <code class="docutils literal notranslate"><span class="pre">4608</span></code>, <code class="docutils literal notranslate"><span class="pre">5120</span></code>].</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.data_node_disk_type">
<code class="sig-name descname">data_node_disk_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.data_node_disk_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The data node disk type. Supported values: cloud_ssd, cloud_efficiency.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.data_node_spec">
<code class="sig-name descname">data_node_spec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.data_node_spec" title="Permalink to this definition">¶</a></dt>
<dd><p>The data node specifications of the Elasticsearch instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of instance. It a string of 0 to 30 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.domain">
<code class="sig-name descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance connection domain (only VPC network access supported).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.instance_charge_type">
<code class="sig-name descname">instance_charge_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.instance_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. From version 1.69.0, the Elasticsearch cluster allows you to update your instance_charge_ype from <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code> to <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, the following attributes are required: <code class="docutils literal notranslate"><span class="pre">period</span></code>. But, updating from <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code> to <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> is not supported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.kibana_domain">
<code class="sig-name descname">kibana_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.kibana_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Kibana console domain (Internet access supported).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.kibana_port">
<code class="sig-name descname">kibana_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.kibana_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Kibana console port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.kibana_whitelists">
<code class="sig-name descname">kibana_whitelists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.kibana_whitelists" title="Permalink to this definition">¶</a></dt>
<dd><p>Set the Kibana’s IP whitelist in internet network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.kms_encrypted_password">
<code class="sig-name descname">kms_encrypted_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.kms_encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encrypts password used to a instance. If the <code class="docutils literal notranslate"><span class="pre">password</span></code> is filled in, this field will be ignored, but you have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.kms_encryption_context">
<code class="sig-name descname">kms_encryption_context</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.kms_encryption_context" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating instance with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.master_node_spec">
<code class="sig-name descname">master_node_spec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.master_node_spec" title="Permalink to this definition">¶</a></dt>
<dd><p>The dedicated master node spec. If specified, dedicated master node will be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password of the instance. The password can be 8 to 30 characters in length and must contain three of the following conditions: uppercase letters, lowercase letters, numbers, and special characters (<code class="docutils literal notranslate"><span class="pre">!&#64;#$%^&amp;*()_+-=</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration that you will buy Elasticsearch instance (in month). It is valid when instance_charge_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid values: [1~9], 12, 24, 36. Default to 1. From version 1.69.2, when to modify this value, the resource can renewal a <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance connection port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.private_whitelists">
<code class="sig-name descname">private_whitelists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.private_whitelists" title="Permalink to this definition">¶</a></dt>
<dd><p>Set the instance’s IP whitelist in VPC network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The Elasticsearch instance status. Includes <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">activating</span></code>, <code class="docutils literal notranslate"><span class="pre">inactive</span></code>. Some operations are denied when status is not <code class="docutils literal notranslate"><span class="pre">active</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Elasticsearch version. Supported values: <code class="docutils literal notranslate"><span class="pre">5.5.3_with_X-Pack</span></code>, <code class="docutils literal notranslate"><span class="pre">6.3_with_X-Pack</span></code> and <code class="docutils literal notranslate"><span class="pre">6.7_with_X-Pack</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of VSwitch.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.elasticsearch.Instance.zone_count">
<code class="sig-name descname">zone_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.zone_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The Multi-AZ supported for Elasticsearch, between 1 and 3. The <code class="docutils literal notranslate"><span class="pre">data_node_amount</span></code> value must be an integral multiple of the <code class="docutils literal notranslate"><span class="pre">zone_count</span></code> value.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.elasticsearch.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">data_node_amount=None</em>, <em class="sig-param">data_node_disk_size=None</em>, <em class="sig-param">data_node_disk_type=None</em>, <em class="sig-param">data_node_spec=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">instance_charge_type=None</em>, <em class="sig-param">kibana_domain=None</em>, <em class="sig-param">kibana_port=None</em>, <em class="sig-param">kibana_whitelists=None</em>, <em class="sig-param">kms_encrypted_password=None</em>, <em class="sig-param">kms_encryption_context=None</em>, <em class="sig-param">master_node_spec=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">private_whitelists=None</em>, <em class="sig-param">public_whitelists=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">zone_count=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data_node_amount</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Elasticsearch cluster’s data node quantity, between 2 and 50.</p></li>
<li><p><strong>data_node_disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The single data node storage space.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `cloud_ssd`: An SSD disk, supports a maximum of 2048 GiB (2 TB).
- `cloud_efficiency` An ultra disk, supports a maximum of 5120 GiB (5 TB). If the data to be stored is larger than 2048 GiB, an ultra disk can only support the following data sizes (GiB): [`2560`, `3072`, `3584`, `4096`, `4608`, `5120`].
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>data_node_disk_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data node disk type. Supported values: cloud_ssd, cloud_efficiency.</p></li>
<li><p><strong>data_node_spec</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data node specifications of the Elasticsearch instance.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of instance. It a string of 0 to 30 characters.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance connection domain (only VPC network access supported).</p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. From version 1.69.0, the Elasticsearch cluster allows you to update your instance_charge_ype from <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code> to <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, the following attributes are required: <code class="docutils literal notranslate"><span class="pre">period</span></code>. But, updating from <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code> to <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> is not supported.</p></li>
<li><p><strong>kibana_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kibana console domain (Internet access supported).</p></li>
<li><p><strong>kibana_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Kibana console port.</p></li>
<li><p><strong>kibana_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set the Kibana’s IP whitelist in internet network.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to a instance. If the <code class="docutils literal notranslate"><span class="pre">password</span></code> is filled in, this field will be ignored, but you have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating instance with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</p></li>
<li><p><strong>master_node*spec</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The dedicated master node spec. If specified, dedicated master node will be created.</p>
</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of the instance. The password can be 8 to 30 characters in length and must contain three of the following conditions: uppercase letters, lowercase letters, numbers, and special characters (<cite>!&#64;#$%^&amp;*()*+-=`</cite>).</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy Elasticsearch instance (in month). It is valid when instance_charge_type is``PrePaid<code class="docutils literal notranslate"><span class="pre">.</span> <span class="pre">Valid</span> <span class="pre">values:</span> <span class="pre">[1~9],</span> <span class="pre">12,</span> <span class="pre">24,</span> <span class="pre">36.</span> <span class="pre">Default</span> <span class="pre">to</span> <span class="pre">1.</span> <span class="pre">From</span> <span class="pre">version</span> <span class="pre">1.69.2,</span> <span class="pre">when</span> <span class="pre">to</span> <span class="pre">modify</span> <span class="pre">this</span> <span class="pre">value,</span> <span class="pre">the</span> <span class="pre">resource</span> <span class="pre">can</span> <span class="pre">renewal</span> <span class="pre">a</span></code>PrePaid<a href="#id11"><span class="problematic" id="id12">``</span></a>instance.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance connection port.</p></li>
<li><p><strong>private_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set the instance’s IP whitelist in VPC network.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Elasticsearch instance status. Includes``active<code class="docutils literal notranslate"><span class="pre">,</span></code>activating<code class="docutils literal notranslate"><span class="pre">,</span></code>inactive<code class="docutils literal notranslate"><span class="pre">.</span> <span class="pre">Some</span> <span class="pre">operations</span> <span class="pre">are</span> <span class="pre">denied</span> <span class="pre">when</span> <span class="pre">status</span> <span class="pre">is</span> <span class="pre">not</span></code>active<a href="#id13"><span class="problematic" id="id14">``</span></a>.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Elasticsearch version. Supported values:<code class="docutils literal notranslate"><span class="pre">\</span> <span class="pre">5.5.3_with_X-Pack\</span> <span class="pre">``,</span></code>6.3_with_X-Pack<code class="docutils literal notranslate"><span class="pre">and</span></code>6.7_with_X-Pack<a href="#id15"><span class="problematic" id="id16">``</span></a>.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of VSwitch.</p></li>
<li><p><strong>zone_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Multi-AZ supported for Elasticsearch, between 1 and 3. The``data_node_amount<code class="docutils literal notranslate"><span class="pre">value</span> <span class="pre">must</span> <span class="pre">be</span> <span class="pre">an</span> <span class="pre">integral</span> <span class="pre">multiple</span> <span class="pre">of</span> <span class="pre">the</span></code>zone_count` value.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/elasticsearch_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/elasticsearch_instance.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.elasticsearch.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.elasticsearch.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.elasticsearch.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.elasticsearch.get_instances">
<code class="sig-prename descclassname">pulumi_alicloud.elasticsearch.</code><code class="sig-name descname">get_instances</code><span class="sig-paren">(</span><em class="sig-param">description_regex=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.elasticsearch.get_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

</div>
