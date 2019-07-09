---
---

<div class="section" id="module-pulumi_azure.hdinsight">
<span id="hdinsight"></span><h1>hdinsight<a class="headerlink" href="#module-pulumi_azure.hdinsight" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.hdinsight.GetClusterResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.hdinsight.</code><code class="descname">GetClusterResult</code><span class="sig-paren">(</span><em>cluster_version=None</em>, <em>component_versions=None</em>, <em>edge_ssh_endpoint=None</em>, <em>gateways=None</em>, <em>https_endpoint=None</em>, <em>kind=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>ssh_endpoint=None</em>, <em>tags=None</em>, <em>tier=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.cluster_version">
<code class="descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of HDInsights which is used on this HDInsight Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.component_versions">
<code class="descname">component_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.component_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of versions of software used on this HDInsights Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.edge_ssh_endpoint">
<code class="descname">edge_ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.edge_ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Endpoint of the Edge Node for this HDInsight Cluster, if an Edge Node exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.gateways">
<code class="descname">gateways</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.gateways" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.https_endpoint">
<code class="descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Endpoint for this HDInsight Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.kind">
<code class="descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The kind of HDInsight Cluster this is, such as a Spark or Storm cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which this HDInsight Cluster exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.ssh_endpoint">
<code class="descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Endpoint for this HDInsight Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags assigned to the HDInsight Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.tier">
<code class="descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU / Tier of this HDInsight Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.hdinsight.HBaseCluster">
<em class="property">class </em><code class="descclassname">pulumi_azure.hdinsight.</code><code class="descname">HBaseCluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cluster_version=None</em>, <em>component_version=None</em>, <em>gateway=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>roles=None</em>, <em>storage_accounts=None</em>, <em>tags=None</em>, <em>tier=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HDInsight HBase Cluster.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</li>
<li><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</li>
<li><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight HBase Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight HBase Cluster. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight HBase Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</li>
<li><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight HBase Cluster.</li>
<li><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight HBase Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_hbase_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_hbase_cluster.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.cluster_version">
<code class="descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.component_version">
<code class="descname">component_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.component_version" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.gateway">
<code class="descname">gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.https_endpoint">
<code class="descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Connectivity Endpoint for this HDInsight HBase Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region which this HDInsight HBase Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name for this HDInsight HBase Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which this HDInsight HBase Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.roles">
<code class="descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.ssh_endpoint">
<code class="descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for this HDInsight HBase Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.storage_accounts">
<code class="descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Tags which should be assigned to this HDInsight HBase Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.tier">
<code class="descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Tier which should be used for this HDInsight HBase Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.HBaseCluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.HBaseCluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.HadoopCluster">
<em class="property">class </em><code class="descclassname">pulumi_azure.hdinsight.</code><code class="descname">HadoopCluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cluster_version=None</em>, <em>component_version=None</em>, <em>gateway=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>roles=None</em>, <em>storage_accounts=None</em>, <em>tags=None</em>, <em>tier=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HDInsight Hadoop Cluster.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</li>
<li><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</li>
<li><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight Hadoop Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight Hadoop Cluster. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight Hadoop Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</li>
<li><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight Hadoop Cluster.</li>
<li><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight Hadoop Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_hadoop_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_hadoop_cluster.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.cluster_version">
<code class="descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.component_version">
<code class="descname">component_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.component_version" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.gateway">
<code class="descname">gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.https_endpoint">
<code class="descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Connectivity Endpoint for this HDInsight Hadoop Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region which this HDInsight Hadoop Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name for this HDInsight Hadoop Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which this HDInsight Hadoop Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.roles">
<code class="descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.ssh_endpoint">
<code class="descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for this HDInsight Hadoop Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.storage_accounts">
<code class="descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Tags which should be assigned to this HDInsight Hadoop Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.tier">
<code class="descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Tier which should be used for this HDInsight Hadoop Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.HadoopCluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.HadoopCluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster">
<em class="property">class </em><code class="descclassname">pulumi_azure.hdinsight.</code><code class="descname">InteractiveQueryCluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cluster_version=None</em>, <em>component_version=None</em>, <em>gateway=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>roles=None</em>, <em>storage_accounts=None</em>, <em>tags=None</em>, <em>tier=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HDInsight Interactive Query Cluster.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</li>
<li><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</li>
<li><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</li>
<li><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.</li>
<li><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_interactive_query_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_interactive_query_cluster.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.cluster_version">
<code class="descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.component_version">
<code class="descname">component_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.component_version" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.gateway">
<code class="descname">gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.https_endpoint">
<code class="descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Connectivity Endpoint for this HDInsight Interactive Query Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.roles">
<code class="descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.ssh_endpoint">
<code class="descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for this HDInsight Interactive Query Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.storage_accounts">
<code class="descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.tier">
<code class="descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.KafkaCluster">
<em class="property">class </em><code class="descclassname">pulumi_azure.hdinsight.</code><code class="descname">KafkaCluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cluster_version=None</em>, <em>component_version=None</em>, <em>gateway=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>roles=None</em>, <em>storage_accounts=None</em>, <em>tags=None</em>, <em>tier=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HDInsight Kafka Cluster.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</li>
<li><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</li>
<li><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight Kafka Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight Kafka Cluster. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight Kafka Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</li>
<li><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight Kafka Cluster.</li>
<li><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight Kafka Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_kafka_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_kafka_cluster.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.cluster_version">
<code class="descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.component_version">
<code class="descname">component_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.component_version" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.gateway">
<code class="descname">gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.https_endpoint">
<code class="descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Connectivity Endpoint for this HDInsight Kafka Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region which this HDInsight Kafka Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name for this HDInsight Kafka Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which this HDInsight Kafka Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.roles">
<code class="descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.ssh_endpoint">
<code class="descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for this HDInsight Kafka Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.storage_accounts">
<code class="descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Tags which should be assigned to this HDInsight Kafka Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.tier">
<code class="descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Tier which should be used for this HDInsight Kafka Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.KafkaCluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.KafkaCluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.MLServicesCluster">
<em class="property">class </em><code class="descclassname">pulumi_azure.hdinsight.</code><code class="descname">MLServicesCluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cluster_version=None</em>, <em>gateway=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>roles=None</em>, <em>rstudio=None</em>, <em>storage_accounts=None</em>, <em>tags=None</em>, <em>tier=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HDInsight ML Services Cluster.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</li>
<li><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight ML Services Cluster. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</li>
<li><strong>rstudio</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should R Studio community edition for ML Services be installed? Changing this forces a new resource to be created.</li>
<li><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight ML Services Cluster.</li>
<li><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight ML Services Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_ml_services_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_ml_services_cluster.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.cluster_version">
<code class="descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.edge_ssh_endpoint">
<code class="descname">edge_ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.edge_ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for the Edge Node of the HDInsight ML Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.gateway">
<code class="descname">gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.https_endpoint">
<code class="descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Connectivity Endpoint for this HDInsight ML Services Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name for this HDInsight ML Services Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.roles">
<code class="descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.rstudio">
<code class="descname">rstudio</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.rstudio" title="Permalink to this definition">¶</a></dt>
<dd><p>Should R Studio community edition for ML Services be installed? Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.ssh_endpoint">
<code class="descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for this HDInsight ML Services Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.storage_accounts">
<code class="descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Tags which should be assigned to this HDInsight ML Services Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.tier">
<code class="descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Tier which should be used for this HDInsight ML Services Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.MLServicesCluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.RServerCluster">
<em class="property">class </em><code class="descclassname">pulumi_azure.hdinsight.</code><code class="descname">RServerCluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cluster_version=None</em>, <em>gateway=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>roles=None</em>, <em>rstudio=None</em>, <em>storage_accounts=None</em>, <em>tags=None</em>, <em>tier=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HDInsight RServer Cluster.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</li>
<li><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight RServer Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight RServer Cluster. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight RServer Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</li>
<li><strong>rstudio</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should R Studio community edition for RServer be installed? Changing this forces a new resource to be created.</li>
<li><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight RServer Cluster.</li>
<li><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight RServer Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_rserver_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_rserver_cluster.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.cluster_version">
<code class="descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.edge_ssh_endpoint">
<code class="descname">edge_ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.edge_ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for the Edge Node of the HDInsight RServer Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.gateway">
<code class="descname">gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.https_endpoint">
<code class="descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Connectivity Endpoint for this HDInsight RServer Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region which this HDInsight RServer Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name for this HDInsight RServer Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which this HDInsight RServer Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.roles">
<code class="descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.rstudio">
<code class="descname">rstudio</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.rstudio" title="Permalink to this definition">¶</a></dt>
<dd><p>Should R Studio community edition for RServer be installed? Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.ssh_endpoint">
<code class="descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for this HDInsight RServer Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.storage_accounts">
<code class="descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Tags which should be assigned to this HDInsight RServer Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.tier">
<code class="descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Tier which should be used for this HDInsight RServer Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.RServerCluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.RServerCluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.SparkCluster">
<em class="property">class </em><code class="descclassname">pulumi_azure.hdinsight.</code><code class="descname">SparkCluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cluster_version=None</em>, <em>component_version=None</em>, <em>gateway=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>roles=None</em>, <em>storage_accounts=None</em>, <em>tags=None</em>, <em>tier=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HDInsight Spark Cluster.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</li>
<li><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</li>
<li><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight Spark Cluster. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</li>
<li><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight Spark Cluster.</li>
<li><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight Spark Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_spark_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_spark_cluster.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.cluster_version">
<code class="descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.component_version">
<code class="descname">component_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.component_version" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.gateway">
<code class="descname">gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.https_endpoint">
<code class="descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Connectivity Endpoint for this HDInsight Spark Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name for this HDInsight Spark Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.roles">
<code class="descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.ssh_endpoint">
<code class="descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for this HDInsight Spark Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.storage_accounts">
<code class="descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Tags which should be assigned to this HDInsight Spark Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.tier">
<code class="descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Tier which should be used for this HDInsight Spark Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.SparkCluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.SparkCluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.StormCluster">
<em class="property">class </em><code class="descclassname">pulumi_azure.hdinsight.</code><code class="descname">StormCluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cluster_version=None</em>, <em>component_version=None</em>, <em>gateway=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>roles=None</em>, <em>storage_accounts=None</em>, <em>tags=None</em>, <em>tier=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HDInsight Storm Cluster.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</li>
<li><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</li>
<li><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight Storm Cluster. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</li>
<li><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight Storm Cluster.</li>
<li><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight Storm Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_storm_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_storm_cluster.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.cluster_version">
<code class="descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.component_version">
<code class="descname">component_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.component_version" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.gateway">
<code class="descname">gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.https_endpoint">
<code class="descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Connectivity Endpoint for this HDInsight Storm Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name for this HDInsight Storm Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.roles">
<code class="descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.ssh_endpoint">
<code class="descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for this HDInsight Storm Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.storage_accounts">
<code class="descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Tags which should be assigned to this HDInsight Storm Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.tier">
<code class="descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Tier which should be used for this HDInsight Storm Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.StormCluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.StormCluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.get_cluster">
<code class="descclassname">pulumi_azure.hdinsight.</code><code class="descname">get_cluster</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing HDInsight Cluster.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/hdinsight_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/hdinsight_cluster.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
