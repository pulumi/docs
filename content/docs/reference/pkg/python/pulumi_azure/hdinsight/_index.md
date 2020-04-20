---
title: Module hdinsight
title_tag: Module hdinsight | Package pulumi_azure | Python SDK
linktitle: hdinsight
notitle: true
---

<div class="section" id="hdinsight">
<h1>hdinsight<a class="headerlink" href="#hdinsight" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.hdinsight"></span><dl class="class">
<dt id="pulumi_azure.hdinsight.AwaitableGetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.hdinsight.</code><code class="sig-name descname">AwaitableGetClusterResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_version=None</em>, <em class="sig-param">component_versions=None</em>, <em class="sig-param">edge_ssh_endpoint=None</em>, <em class="sig-param">gateways=None</em>, <em class="sig-param">https_endpoint=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">kind=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">ssh_endpoint=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.AwaitableGetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.hdinsight.GetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.hdinsight.</code><code class="sig-name descname">GetClusterResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_version=None</em>, <em class="sig-param">component_versions=None</em>, <em class="sig-param">edge_ssh_endpoint=None</em>, <em class="sig-param">gateways=None</em>, <em class="sig-param">https_endpoint=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">kind=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">ssh_endpoint=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.cluster_version">
<code class="sig-name descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of HDInsights which is used on this HDInsight Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.component_versions">
<code class="sig-name descname">component_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.component_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of versions of software used on this HDInsights Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.edge_ssh_endpoint">
<code class="sig-name descname">edge_ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.edge_ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Endpoint of the Edge Node for this HDInsight Cluster, if an Edge Node exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.gateways">
<code class="sig-name descname">gateways</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.gateways" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.https_endpoint">
<code class="sig-name descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Endpoint for this HDInsight Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The kind of HDInsight Cluster this is, such as a Spark or Storm cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which this HDInsight Cluster exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.ssh_endpoint">
<code class="sig-name descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Endpoint for this HDInsight Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags assigned to the HDInsight Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.GetClusterResult.tier">
<code class="sig-name descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.GetClusterResult.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU / Tier of this HDInsight Cluster.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.hdinsight.HBaseCluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.hdinsight.</code><code class="sig-name descname">HBaseCluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_version=None</em>, <em class="sig-param">component_version=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">storage_account_gen2=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HDInsight HBase Cluster.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight HBase Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight HBase Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight HBase Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p></li>
<li><p><strong>storage_account_gen2</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_account_gen2</span></code> block as defined below.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight HBase Cluster.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight HBase Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>component_version</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hbase</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of HBase which should be used for this HDInsight HBase Cluster. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>gateway</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_account_gen2</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filesystemId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedIdentityResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Account. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.cluster_version">
<code class="sig-name descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.component_version">
<code class="sig-name descname">component_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.component_version" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hbase</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of HBase which should be used for this HDInsight HBase Cluster. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.gateway">
<code class="sig-name descname">gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.https_endpoint">
<code class="sig-name descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Connectivity Endpoint for this HDInsight HBase Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region which this HDInsight HBase Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name for this HDInsight HBase Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which this HDInsight HBase Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.ssh_endpoint">
<code class="sig-name descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for this HDInsight HBase Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.storage_account_gen2">
<code class="sig-name descname">storage_account_gen2</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.storage_account_gen2" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_account_gen2</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filesystemId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedIdentityResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Storage Account. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.storage_accounts">
<code class="sig-name descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Tags which should be assigned to this HDInsight HBase Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HBaseCluster.tier">
<code class="sig-name descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Tier which should be used for this HDInsight HBase Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.HBaseCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_version=None</em>, <em class="sig-param">component_version=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">https_endpoint=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">ssh_endpoint=None</em>, <em class="sig-param">storage_account_gen2=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HBaseCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p></li>
<li><p><strong>https_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTPS Connectivity Endpoint for this HDInsight HBase Cluster.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight HBase Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight HBase Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight HBase Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p></li>
<li><p><strong>ssh_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSH Connectivity Endpoint for this HDInsight HBase Cluster.</p></li>
<li><p><strong>storage_account_gen2</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_account_gen2</span></code> block as defined below.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight HBase Cluster.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight HBase Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>component_version</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hbase</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of HBase which should be used for this HDInsight HBase Cluster. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>gateway</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_account_gen2</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filesystemId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedIdentityResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Account. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.HBaseCluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.HBaseCluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.HBaseCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.HadoopCluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.hdinsight.</code><code class="sig-name descname">HadoopCluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_version=None</em>, <em class="sig-param">component_version=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">storage_account_gen2=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HDInsight Hadoop Cluster.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight Hadoop Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight Hadoop Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight Hadoop Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p></li>
<li><p><strong>storage_account_gen2</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_account_gen2</span></code> block as defined below.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight Hadoop Cluster.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight Hadoop Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>component_version</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hadoop</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of Hadoop which should be used for this HDInsight Hadoop Cluster. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>gateway</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">edgeNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">edge_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">installScriptActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">install_script_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the install script action. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI pointing to the script to run during the installation of the edge node. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Edge Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_account_gen2</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filesystemId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedIdentityResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Account. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.cluster_version">
<code class="sig-name descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.component_version">
<code class="sig-name descname">component_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.component_version" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hadoop</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of Hadoop which should be used for this HDInsight Hadoop Cluster. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.gateway">
<code class="sig-name descname">gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.https_endpoint">
<code class="sig-name descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Connectivity Endpoint for this HDInsight Hadoop Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region which this HDInsight Hadoop Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name for this HDInsight Hadoop Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which this HDInsight Hadoop Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">edgeNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">edge_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">installScriptActions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">install_script_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the install script action. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URI pointing to the script to run during the installation of the edge node. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Edge Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.ssh_endpoint">
<code class="sig-name descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for this HDInsight Hadoop Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.storage_account_gen2">
<code class="sig-name descname">storage_account_gen2</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.storage_account_gen2" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_account_gen2</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filesystemId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedIdentityResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Storage Account. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.storage_accounts">
<code class="sig-name descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Tags which should be assigned to this HDInsight Hadoop Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.HadoopCluster.tier">
<code class="sig-name descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Tier which should be used for this HDInsight Hadoop Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.HadoopCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_version=None</em>, <em class="sig-param">component_version=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">https_endpoint=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">ssh_endpoint=None</em>, <em class="sig-param">storage_account_gen2=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HadoopCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p></li>
<li><p><strong>https_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTPS Connectivity Endpoint for this HDInsight Hadoop Cluster.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight Hadoop Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight Hadoop Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight Hadoop Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p></li>
<li><p><strong>ssh_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSH Connectivity Endpoint for this HDInsight Hadoop Cluster.</p></li>
<li><p><strong>storage_account_gen2</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_account_gen2</span></code> block as defined below.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight Hadoop Cluster.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight Hadoop Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>component_version</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hadoop</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of Hadoop which should be used for this HDInsight Hadoop Cluster. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>gateway</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">edgeNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">edge_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">installScriptActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">install_script_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the install script action. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI pointing to the script to run during the installation of the edge node. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Edge Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_account_gen2</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filesystemId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedIdentityResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Account. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.HadoopCluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.HadoopCluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.HadoopCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.hdinsight.</code><code class="sig-name descname">InteractiveQueryCluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_version=None</em>, <em class="sig-param">component_version=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">storage_account_gen2=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HDInsight Interactive Query Cluster.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p></li>
<li><p><strong>storage_account_gen2</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_account_gen2</span></code> block as defined below.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>component_version</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">interactiveHive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>gateway</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_account_gen2</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filesystemId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedIdentityResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Account. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.cluster_version">
<code class="sig-name descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.component_version">
<code class="sig-name descname">component_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.component_version" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">interactiveHive</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.gateway">
<code class="sig-name descname">gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.https_endpoint">
<code class="sig-name descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Connectivity Endpoint for this HDInsight Interactive Query Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.ssh_endpoint">
<code class="sig-name descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for this HDInsight Interactive Query Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.storage_account_gen2">
<code class="sig-name descname">storage_account_gen2</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.storage_account_gen2" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_account_gen2</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filesystemId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedIdentityResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Storage Account. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.storage_accounts">
<code class="sig-name descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.tier">
<code class="sig-name descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_version=None</em>, <em class="sig-param">component_version=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">https_endpoint=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">ssh_endpoint=None</em>, <em class="sig-param">storage_account_gen2=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InteractiveQueryCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p></li>
<li><p><strong>https_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTPS Connectivity Endpoint for this HDInsight Interactive Query Cluster.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p></li>
<li><p><strong>ssh_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSH Connectivity Endpoint for this HDInsight Interactive Query Cluster.</p></li>
<li><p><strong>storage_account_gen2</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_account_gen2</span></code> block as defined below.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>component_version</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">interactiveHive</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>gateway</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_account_gen2</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filesystemId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedIdentityResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Account. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.InteractiveQueryCluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.InteractiveQueryCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.KafkaCluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.hdinsight.</code><code class="sig-name descname">KafkaCluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_version=None</em>, <em class="sig-param">component_version=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">storage_account_gen2=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HDInsight Kafka Cluster.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight Kafka Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight Kafka Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight Kafka Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p></li>
<li><p><strong>storage_account_gen2</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_account_gen2</span></code> block as defined below.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight Kafka Cluster.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight Kafka Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>component_version</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kafka</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of Kafka which should be used for this HDInsight Kafka Cluster. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>gateway</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisksPerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of Data Disks which should be assigned to each Worker Node, which can be between 1 and 8. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_account_gen2</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filesystemId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedIdentityResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Account. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.cluster_version">
<code class="sig-name descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.component_version">
<code class="sig-name descname">component_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.component_version" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kafka</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of Kafka which should be used for this HDInsight Kafka Cluster. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.gateway">
<code class="sig-name descname">gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.https_endpoint">
<code class="sig-name descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Connectivity Endpoint for this HDInsight Kafka Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region which this HDInsight Kafka Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name for this HDInsight Kafka Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which this HDInsight Kafka Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisksPerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of Data Disks which should be assigned to each Worker Node, which can be between 1 and 8. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.ssh_endpoint">
<code class="sig-name descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for this HDInsight Kafka Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.storage_account_gen2">
<code class="sig-name descname">storage_account_gen2</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.storage_account_gen2" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_account_gen2</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filesystemId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedIdentityResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Storage Account. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.storage_accounts">
<code class="sig-name descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Tags which should be assigned to this HDInsight Kafka Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.KafkaCluster.tier">
<code class="sig-name descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Tier which should be used for this HDInsight Kafka Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.KafkaCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_version=None</em>, <em class="sig-param">component_version=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">https_endpoint=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">ssh_endpoint=None</em>, <em class="sig-param">storage_account_gen2=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KafkaCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p></li>
<li><p><strong>https_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTPS Connectivity Endpoint for this HDInsight Kafka Cluster.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight Kafka Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight Kafka Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight Kafka Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p></li>
<li><p><strong>ssh_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSH Connectivity Endpoint for this HDInsight Kafka Cluster.</p></li>
<li><p><strong>storage_account_gen2</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_account_gen2</span></code> block as defined below.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight Kafka Cluster.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight Kafka Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>component_version</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kafka</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of Kafka which should be used for this HDInsight Kafka Cluster. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>gateway</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numberOfDisksPerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of Data Disks which should be assigned to each Worker Node, which can be between 1 and 8. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_account_gen2</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filesystemId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedIdentityResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Account. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.KafkaCluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.KafkaCluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.KafkaCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.MLServicesCluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.hdinsight.</code><code class="sig-name descname">MLServicesCluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_version=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">rstudio=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HDInsight ML Services Cluster.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight ML Services Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p></li>
<li><p><strong>rstudio</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should R Studio community edition for ML Services be installed? Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight ML Services Cluster.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight ML Services Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>gateway</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">edgeNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">edge_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Edge Node should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Edge Node should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Edge Node. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight ML Services Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.cluster_version">
<code class="sig-name descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.edge_ssh_endpoint">
<code class="sig-name descname">edge_ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.edge_ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for the Edge Node of the HDInsight ML Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.gateway">
<code class="sig-name descname">gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.https_endpoint">
<code class="sig-name descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Connectivity Endpoint for this HDInsight ML Services Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name for this HDInsight ML Services Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">edgeNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">edge_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Edge Node should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Edge Node should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Edge Node. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.rstudio">
<code class="sig-name descname">rstudio</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.rstudio" title="Permalink to this definition">¶</a></dt>
<dd><p>Should R Studio community edition for ML Services be installed? Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.ssh_endpoint">
<code class="sig-name descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for this HDInsight ML Services Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.storage_accounts">
<code class="sig-name descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this the Default Storage Account for the HDInsight ML Services Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Tags which should be assigned to this HDInsight ML Services Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.tier">
<code class="sig-name descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Tier which should be used for this HDInsight ML Services Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_version=None</em>, <em class="sig-param">edge_ssh_endpoint=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">https_endpoint=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">rstudio=None</em>, <em class="sig-param">ssh_endpoint=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MLServicesCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>edge_ssh_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSH Connectivity Endpoint for the Edge Node of the HDInsight ML Cluster.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p></li>
<li><p><strong>https_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTPS Connectivity Endpoint for this HDInsight ML Services Cluster.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight ML Services Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight ML Services Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p></li>
<li><p><strong>rstudio</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should R Studio community edition for ML Services be installed? Changing this forces a new resource to be created.</p></li>
<li><p><strong>ssh_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSH Connectivity Endpoint for this HDInsight ML Services Cluster.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight ML Services Cluster.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight ML Services Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>gateway</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">edgeNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">edge_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Edge Node should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Edge Node should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Edge Node. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight ML Services Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.MLServicesCluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.MLServicesCluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.MLServicesCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.RServerCluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.hdinsight.</code><code class="sig-name descname">RServerCluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_version=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">rstudio=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HDInsight RServer Cluster.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight RServer Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight RServer Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight RServer Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p></li>
<li><p><strong>rstudio</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should R Studio community edition for RServer be installed? Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight RServer Cluster.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight RServer Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>gateway</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">edgeNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">edge_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Edge Node should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Edge Node should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Edge Node. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight RServer Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.cluster_version">
<code class="sig-name descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.edge_ssh_endpoint">
<code class="sig-name descname">edge_ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.edge_ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for the Edge Node of the HDInsight RServer Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.gateway">
<code class="sig-name descname">gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.https_endpoint">
<code class="sig-name descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Connectivity Endpoint for this HDInsight RServer Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region which this HDInsight RServer Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name for this HDInsight RServer Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which this HDInsight RServer Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">edgeNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">edge_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Edge Node should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Edge Node should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Edge Node. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.rstudio">
<code class="sig-name descname">rstudio</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.rstudio" title="Permalink to this definition">¶</a></dt>
<dd><p>Should R Studio community edition for RServer be installed? Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.ssh_endpoint">
<code class="sig-name descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for this HDInsight RServer Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.storage_accounts">
<code class="sig-name descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this the Default Storage Account for the HDInsight RServer Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Tags which should be assigned to this HDInsight RServer Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.RServerCluster.tier">
<code class="sig-name descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Tier which should be used for this HDInsight RServer Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.RServerCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_version=None</em>, <em class="sig-param">edge_ssh_endpoint=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">https_endpoint=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">rstudio=None</em>, <em class="sig-param">ssh_endpoint=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RServerCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>edge_ssh_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSH Connectivity Endpoint for the Edge Node of the HDInsight RServer Cluster.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p></li>
<li><p><strong>https_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTPS Connectivity Endpoint for this HDInsight RServer Cluster.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight RServer Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight RServer Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight RServer Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p></li>
<li><p><strong>rstudio</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should R Studio community edition for RServer be installed? Changing this forces a new resource to be created.</p></li>
<li><p><strong>ssh_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSH Connectivity Endpoint for this HDInsight RServer Cluster.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight RServer Cluster.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight RServer Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>gateway</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">edgeNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">edge_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Edge Node should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Edge Node. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Edge Node should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Edge Node. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight RServer Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.RServerCluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.RServerCluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.RServerCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.SparkCluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.hdinsight.</code><code class="sig-name descname">SparkCluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_version=None</em>, <em class="sig-param">component_version=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">storage_account_gen2=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HDInsight Spark Cluster.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight Spark Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p></li>
<li><p><strong>storage_account_gen2</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_account_gen2</span></code> block as defined below.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight Spark Cluster.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight Spark Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>component_version</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">spark</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of Spark which should be used for this HDInsight Spark Cluster. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>gateway</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_account_gen2</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filesystemId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedIdentityResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Account. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.cluster_version">
<code class="sig-name descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.component_version">
<code class="sig-name descname">component_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.component_version" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">spark</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of Spark which should be used for this HDInsight Spark Cluster. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.gateway">
<code class="sig-name descname">gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.https_endpoint">
<code class="sig-name descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Connectivity Endpoint for this HDInsight Spark Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name for this HDInsight Spark Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.ssh_endpoint">
<code class="sig-name descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for this HDInsight Spark Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.storage_account_gen2">
<code class="sig-name descname">storage_account_gen2</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.storage_account_gen2" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_account_gen2</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filesystemId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedIdentityResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Storage Account. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.storage_accounts">
<code class="sig-name descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Tags which should be assigned to this HDInsight Spark Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.SparkCluster.tier">
<code class="sig-name descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Tier which should be used for this HDInsight Spark Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.SparkCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_version=None</em>, <em class="sig-param">component_version=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">https_endpoint=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">ssh_endpoint=None</em>, <em class="sig-param">storage_account_gen2=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SparkCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p></li>
<li><p><strong>https_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTPS Connectivity Endpoint for this HDInsight Spark Cluster.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight Spark Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p></li>
<li><p><strong>ssh_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSH Connectivity Endpoint for this HDInsight Spark Cluster.</p></li>
<li><p><strong>storage_account_gen2</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_account_gen2</span></code> block as defined below.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight Spark Cluster.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight Spark Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>component_version</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">spark</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of Spark which should be used for this HDInsight Spark Cluster. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>gateway</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_account_gen2</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filesystemId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedIdentityResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Account. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.SparkCluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.SparkCluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.SparkCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.StormCluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.hdinsight.</code><code class="sig-name descname">StormCluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_version=None</em>, <em class="sig-param">component_version=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HDInsight Storm Cluster.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight Storm Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight Storm Cluster.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight Storm Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>component_version</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of Storm which should be used for this HDInsight Storm Cluster. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>gateway</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Storm Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.cluster_version">
<code class="sig-name descname">cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.component_version">
<code class="sig-name descname">component_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.component_version" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storm</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of Storm which should be used for this HDInsight Storm Cluster. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.gateway">
<code class="sig-name descname">gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.https_endpoint">
<code class="sig-name descname">https_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.https_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTPS Connectivity Endpoint for this HDInsight Storm Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name for this HDInsight Storm Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.ssh_endpoint">
<code class="sig-name descname">ssh_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.ssh_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Connectivity Endpoint for this HDInsight Storm Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.storage_accounts">
<code class="sig-name descname">storage_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.storage_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this the Default Storage Account for the HDInsight Storm Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Tags which should be assigned to this HDInsight Storm Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hdinsight.StormCluster.tier">
<code class="sig-name descname">tier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.tier" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Tier which should be used for this HDInsight Storm Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.StormCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_version=None</em>, <em class="sig-param">component_version=None</em>, <em class="sig-param">gateway=None</em>, <em class="sig-param">https_endpoint=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">ssh_endpoint=None</em>, <em class="sig-param">storage_accounts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tier=None</em>, <em class="sig-param">tls_min_version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing StormCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>component_version</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">component_version</span></code> block as defined below.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gateway</span></code> block as defined below.</p></li>
<li><p><strong>https_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTPS Connectivity Endpoint for this HDInsight Storm Cluster.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name for this HDInsight Storm Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">roles</span></code> block as defined below.</p></li>
<li><p><strong>ssh_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSH Connectivity Endpoint for this HDInsight Storm Cluster.</p></li>
<li><p><strong>storage_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_account</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Tags which should be assigned to this HDInsight Storm Cluster.</p></li>
<li><p><strong>tier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Tier which should be used for this HDInsight Storm Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>component_version</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of Storm which should be used for this HDInsight Storm Cluster. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>gateway</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Ambari portal enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username used for the Ambari Portal. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">head_node</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workerNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">worker_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetInstanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of instances which should be run for the Worker Nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zookeeperNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">zookeeper_node</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_accounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Default Storage Account for the HDInsight Storm Cluster? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_container_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Storage Container. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hdinsight.StormCluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.StormCluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.StormCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hdinsight.get_cluster">
<code class="sig-prename descclassname">pulumi_azure.hdinsight.</code><code class="sig-name descname">get_cluster</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hdinsight.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing HDInsight Cluster.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of this HDInsight Cluster.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the Resource Group in which this HDInsight Cluster exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
