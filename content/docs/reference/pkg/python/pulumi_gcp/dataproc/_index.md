---
title: Module dataproc
title_tag: Module dataproc | Package pulumi_gcp | Python SDK
linktitle: dataproc
notitle: true
---

<div class="section" id="dataproc">
<h1>dataproc<a class="headerlink" href="#dataproc" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.dataproc"></span><dl class="class">
<dt id="pulumi_gcp.dataproc.AutoscalingPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dataproc.</code><code class="sig-name descname">AutoscalingPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">basic_algorithm=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">policy_id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">secondary_worker_config=None</em>, <em class="sig-param">worker_config=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.AutoscalingPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes an autoscaling policy for Dataproc cluster autoscaler.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>basic_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Basic algorithm for autoscaling.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the autoscaling poicy should reside. The default value is ‘global’.</p></li>
<li><p><strong>policy*id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The policy id. The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (<a href="#id3"><span class="problematic" id="id4">*</span></a>), and hyphens (-). Cannot
begin or end with underscore or hyphen. Must consist of between 3 and 50 characters.</p>
</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>secondary_worker_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes how the autoscaler will operate for secondary workers.</p></li>
<li><p><strong>worker_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes how the autoscaler will operate for primary workers.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>basic_algorithm</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cooldownPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">yarnConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">gracefulDecommissionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleDownFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleDownMinWorkerFraction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleUpFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleUpMinWorkerFraction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>secondary_worker_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">max_instances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>worker_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">max_instances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.dataproc.AutoscalingPolicy.basic_algorithm">
<code class="sig-name descname">basic_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.AutoscalingPolicy.basic_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Basic algorithm for autoscaling.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cooldownPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">yarnConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">gracefulDecommissionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleDownFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleDownMinWorkerFraction</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleUpFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleUpMinWorkerFraction</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.AutoscalingPolicy.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.AutoscalingPolicy.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the autoscaling poicy should reside. The default value is ‘global’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.AutoscalingPolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.AutoscalingPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The “resource name” of the autoscaling policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.AutoscalingPolicy.policy_id">
<code class="sig-name descname">policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.AutoscalingPolicy.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy id. The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). Cannot
begin or end with underscore or hyphen. Must consist of between 3 and 50 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.AutoscalingPolicy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.AutoscalingPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.AutoscalingPolicy.secondary_worker_config">
<code class="sig-name descname">secondary_worker_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.AutoscalingPolicy.secondary_worker_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes how the autoscaler will operate for secondary workers.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">max_instances</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.AutoscalingPolicy.worker_config">
<code class="sig-name descname">worker_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.AutoscalingPolicy.worker_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes how the autoscaler will operate for primary workers.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">max_instances</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.AutoscalingPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">basic_algorithm=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy_id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">secondary_worker_config=None</em>, <em class="sig-param">worker_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.AutoscalingPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AutoscalingPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>basic_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Basic algorithm for autoscaling.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the autoscaling poicy should reside. The default value is ‘global’.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The “resource name” of the autoscaling policy.</p></li>
<li><p><strong>policy*id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The policy id. The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (<a href="#id7"><span class="problematic" id="id8">*</span></a>), and hyphens (-). Cannot
begin or end with underscore or hyphen. Must consist of between 3 and 50 characters.</p>
</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>secondary_worker_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes how the autoscaler will operate for secondary workers.</p></li>
<li><p><strong>worker_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes how the autoscaler will operate for primary workers.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>basic_algorithm</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cooldownPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">yarnConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">gracefulDecommissionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleDownFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleDownMinWorkerFraction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleUpFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleUpMinWorkerFraction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>secondary_worker_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">max_instances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>worker_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">max_instances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.AutoscalingPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.AutoscalingPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.AutoscalingPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.AutoscalingPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dataproc.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_config=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Cloud Dataproc cluster resource within GCP. For more information see
<a class="reference external" href="https://cloud.google.com/dataproc/">the official dataproc documentation</a>.</p>
<p>!&gt; <strong>Warning:</strong> Due to limitations of the API, all arguments except
<code class="docutils literal notranslate"><span class="pre">labels</span></code>,<code class="docutils literal notranslate"><span class="pre">cluster_config.worker_config.num_instances</span></code> and <code class="docutils literal notranslate"><span class="pre">cluster_config.preemptible_worker_config.num_instances</span></code> are non-updatable. Changing others will cause recreation of the
whole cluster!</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Allows you to configure various aspects of the cluster.
Structure defined below.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including <code class="docutils literal notranslate"><span class="pre">goog-dataproc-cluster-name</span></code>
which is the name of the cluster.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the cluster, unique within the project and
zone.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the <code class="docutils literal notranslate"><span class="pre">cluster</span></code> will exist. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the cluster and associated nodes will be created in.
Defaults to <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cluster_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscalingConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The autoscaling policy config associated with the cluster.
Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">policyUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The autoscaling policy used by the cluster.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Customer managed encryption keys settings for the cluster.
Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud KMS key name to use for PD disk encryption for
all instances in the cluster.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">gceClusterConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Common config settings for resources of Google Compute Engine cluster
instances, applicable to all instances in the cluster. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">internalIpOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - By default, clusters are not restricted to internal IP addresses, 
and will have ephemeral external IP addresses assigned to each instance. If set to true, all
instances in the cluster will only have internal IP addresses. Note: Private Google Access
(also known as <code class="docutils literal notranslate"><span class="pre">privateIpGoogleAccess</span></code>) must be enabled on the subnetwork that the cluster
will be launched in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of the Compute Engine metadata entries to add to all instances
(see <a class="reference external" href="https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata">Project and instance metadata</a>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name or self_link of the Google Compute Engine
network to the cluster will be part of. Conflicts with <code class="docutils literal notranslate"><span class="pre">subnetwork</span></code>.
If neither is specified, this defaults to the “default” network.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service account to be used by the Node VMs.
If not specified, the “default” service account is used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccountScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of Google API scopes
to be made available on all of the node VMs under the <code class="docutils literal notranslate"><span class="pre">service_account</span></code>
specified. These can be   either FQDNs, or scope aliases. The following scopes
must be set if any other scopes are set. They’re necessary to ensure the
correct functioning ofthe cluster, and are set automatically by the API:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name or self_link of the Google Compute Engine
subnetwork the cluster will be part of. Conflicts with <code class="docutils literal notranslate"><span class="pre">network</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of instance tags applied to instances in the cluster.
Tags are used to identify valid sources or targets for network firewalls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The GCP zone where your data is stored and used (i.e. where
the master and the worker nodes will be created in). If <code class="docutils literal notranslate"><span class="pre">region</span></code> is set to ‘global’ (default)
then <code class="docutils literal notranslate"><span class="pre">zone</span></code> is mandatory, otherwise GCP is able to make use of <a class="reference external" href="https://cloud.google.com/dataproc/docs/concepts/auto-zone">Auto Zone Placement</a>
to determine this automatically for you.
Note: This setting additionally determines and restricts
which computing resources are available for use with other configs such as
<code class="docutils literal notranslate"><span class="pre">cluster_config.master_config.machine_type</span></code> and <code class="docutils literal notranslate"><span class="pre">cluster_config.worker_config.machine_type</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initializationActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Commands to execute on each node after config is completed.
You can specify multiple versions of these. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">script</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout_sec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum duration (in seconds) which <code class="docutils literal notranslate"><span class="pre">script</span></code> is
allowed to take to execute its action. GCP will default to a predetermined
computed value if not set (currently 300).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifecycleConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoDeleteTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time when cluster will be auto-deleted.
A timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds.
Example: “2014-10-02T15:01:23.045123456Z”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idleDeleteTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The duration to keep the cluster alive while idling
(no jobs running). After this TTL, the cluster will be deleted. Valid range: [10m, 14d].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idleStartTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Google Compute Engine config settings for the master instances
in a cluster.. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The Compute Engine accelerator configuration for these instances. Can be specified multiple times.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">acceleratorCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of the accelerator cards of this type exposed to this instance. Often restricted to one of <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code>, or <code class="docutils literal notranslate"><span class="pre">8</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">accelerator_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The short name of the accelerator type to expose to this instance. For example, <code class="docutils literal notranslate"><span class="pre">nvidia-tesla-k80</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Disk Config</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskSizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The disk type of the primary disk attached to each preemptible worker node.
One of <code class="docutils literal notranslate"><span class="pre">&quot;pd-ssd&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numLocalSsds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI for the image to use for this worker.  See <a class="reference external" href="https://cloud.google.com/dataproc/docs/guides/dataproc-images">the guide</a>
for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a Google Compute Engine machine type
to create for the worker nodes. If not specified, GCP will default to a predetermined
computed value (currently <code class="docutils literal notranslate"><span class="pre">n1-standard-4</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a minimum generation of CPU family
for the master. If not specified, GCP will default to a predetermined computed value
for each zone. See <a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">the guide</a>
for details about which CPU families are available (and defaulted) for each zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptibleWorkerConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Google Compute Engine config settings for the additional (aka
preemptible) instances in a cluster. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">diskConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Disk Config</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskSizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The disk type of the primary disk attached to each preemptible worker node.
One of <code class="docutils literal notranslate"><span class="pre">&quot;pd-ssd&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numLocalSsds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Security related configuration. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kerberosConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Kerberos Configuration</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustAdminServer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The admin server (IP or hostname) for the
remote trusted realm in a cross realm trust relationship.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustKdc</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The KDC (IP or hostname) for the
remote trusted realm in a cross realm trust relationship.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustRealm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The remote realm the Dataproc on-cluster KDC will
trust, should the user enable cross realm trust.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustSharedPasswordUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage URI of a KMS
encrypted file containing the shared password between the on-cluster Kerberos realm
and the remote trusted realm, in a cross realm trust relationship.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableKerberos</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Flag to indicate whether to Kerberize the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kdcDbKeyUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage URI of a KMS encrypted file containing
the master key of the KDC database.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyPasswordUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage URI of a KMS encrypted file containing
the password to the user provided key. For the self-signed certificate, this password
is generated by Dataproc.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keystorePasswordUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage URI of a KMS encrypted file containing
the password to the user provided keystore. For the self-signed certificated, the password
is generated by Dataproc.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keystoreUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage URI of the keystore file used for SSL encryption.
If not provided, Dataproc will provide a self-signed certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeyUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI of the KMS key used to encrypt various sensitive files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">realm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the on-cluster Kerberos realm. If not specified, the
uppercased domain of hostnames will be the realm.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootPrincipalPasswordUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage URI of a KMS encrypted file
containing the root principal password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tgtLifetimeHours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The lifetime of the ticket granting ticket, in hours.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">truststorePasswordUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage URI of a KMS encrypted file
containing the password to the user provided truststore. For the self-signed
certificate, this password is generated by Dataproc.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">truststoreUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage URI of the truststore file used for
SSL encryption. If not provided, Dataproc will provide a self-signed certificate.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">softwareConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The config settings for software inside the cluster.
Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">imageVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Dataproc image version to use
for the cluster - this controls the sets of software versions
installed onto the nodes when you create clusters. If not specified, defaults to the
latest version. For a list of valid versions see
<a class="reference external" href="https://cloud.google.com/dataproc/docs/concepts/dataproc-versions">Cloud Dataproc versions</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">optionalComponents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of optional components to activate on the cluster. 
Accepted values are:</p>
<ul>
<li><p>ANACONDA</p></li>
<li><p>DRUID</p></li>
<li><p>HIVE_WEBHCAT</p></li>
<li><p>JUPYTER</p></li>
<li><p>KERBEROS</p></li>
<li><p>PRESTO</p></li>
<li><p>ZEPPELIN</p></li>
<li><p>ZOOKEEPER</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A list of override and additional properties (key/value pairs)
used to modify various aspects of the common configuration files used when creating
a cluster. For a list of valid properties please see
<a class="reference external" href="https://cloud.google.com/dataproc/docs/concepts/cluster-properties">Cluster properties</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">stagingBucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage staging bucket used to stage files,
such as Hadoop jars, between client machines and the cluster.
Note: If you don’t explicitly specify a <code class="docutils literal notranslate"><span class="pre">staging_bucket</span></code>
then GCP will auto create / assign one for you. However, you are not guaranteed
an auto generated bucket which is solely dedicated to your cluster; it may be shared
with other clusters in the same region/zone also choosing to use the auto generation
option.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">worker_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Google Compute Engine config settings for the worker instances
in a cluster.. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The Compute Engine accelerator configuration for these instances. Can be specified multiple times.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">acceleratorCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of the accelerator cards of this type exposed to this instance. Often restricted to one of <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code>, or <code class="docutils literal notranslate"><span class="pre">8</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">accelerator_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The short name of the accelerator type to expose to this instance. For example, <code class="docutils literal notranslate"><span class="pre">nvidia-tesla-k80</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Disk Config</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskSizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The disk type of the primary disk attached to each preemptible worker node.
One of <code class="docutils literal notranslate"><span class="pre">&quot;pd-ssd&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numLocalSsds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI for the image to use for this worker.  See <a class="reference external" href="https://cloud.google.com/dataproc/docs/guides/dataproc-images">the guide</a>
for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a Google Compute Engine machine type
to create for the worker nodes. If not specified, GCP will default to a predetermined
computed value (currently <code class="docutils literal notranslate"><span class="pre">n1-standard-4</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a minimum generation of CPU family
for the master. If not specified, GCP will default to a predetermined computed value
for each zone. See <a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">the guide</a>
for details about which CPU families are available (and defaulted) for each zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Cluster.cluster_config">
<code class="sig-name descname">cluster_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Cluster.cluster_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to configure various aspects of the cluster.
Structure defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscalingConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The autoscaling policy config associated with the cluster.
Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">policyUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The autoscaling policy used by the cluster.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Customer managed encryption keys settings for the cluster.
Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Cloud KMS key name to use for PD disk encryption for
all instances in the cluster.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">gceClusterConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Common config settings for resources of Google Compute Engine cluster
instances, applicable to all instances in the cluster. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">internalIpOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - By default, clusters are not restricted to internal IP addresses, 
and will have ephemeral external IP addresses assigned to each instance. If set to true, all
instances in the cluster will only have internal IP addresses. Note: Private Google Access
(also known as <code class="docutils literal notranslate"><span class="pre">privateIpGoogleAccess</span></code>) must be enabled on the subnetwork that the cluster
will be launched in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A map of the Compute Engine metadata entries to add to all instances
(see <a class="reference external" href="https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata">Project and instance metadata</a>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name or self_link of the Google Compute Engine
network to the cluster will be part of. Conflicts with <code class="docutils literal notranslate"><span class="pre">subnetwork</span></code>.
If neither is specified, this defaults to the “default” network.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The service account to be used by the Node VMs.
If not specified, the “default” service account is used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccountScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The set of Google API scopes
to be made available on all of the node VMs under the <code class="docutils literal notranslate"><span class="pre">service_account</span></code>
specified. These can be       either FQDNs, or scope aliases. The following scopes
must be set if any other scopes are set. They’re necessary to ensure the
correct functioning ofthe cluster, and are set automatically by the API:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name or self_link of the Google Compute Engine
subnetwork the cluster will be part of. Conflicts with <code class="docutils literal notranslate"><span class="pre">network</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The list of instance tags applied to instances in the cluster.
Tags are used to identify valid sources or targets for network firewalls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The GCP zone where your data is stored and used (i.e. where
the master and the worker nodes will be created in). If <code class="docutils literal notranslate"><span class="pre">region</span></code> is set to ‘global’ (default)
then <code class="docutils literal notranslate"><span class="pre">zone</span></code> is mandatory, otherwise GCP is able to make use of <a class="reference external" href="https://cloud.google.com/dataproc/docs/concepts/auto-zone">Auto Zone Placement</a>
to determine this automatically for you.
Note: This setting additionally determines and restricts
which computing resources are available for use with other configs such as
<code class="docutils literal notranslate"><span class="pre">cluster_config.master_config.machine_type</span></code> and <code class="docutils literal notranslate"><span class="pre">cluster_config.worker_config.machine_type</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initializationActions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Commands to execute on each node after config is completed.
You can specify multiple versions of these. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">script</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout_sec</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum duration (in seconds) which <code class="docutils literal notranslate"><span class="pre">script</span></code> is
allowed to take to execute its action. GCP will default to a predetermined
computed value if not set (currently 300).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifecycleConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoDeleteTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The time when cluster will be auto-deleted.
A timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds.
Example: “2014-10-02T15:01:23.045123456Z”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idleDeleteTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The duration to keep the cluster alive while idling
(no jobs running). After this TTL, the cluster will be deleted. Valid range: [10m, 14d].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idleStartTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Google Compute Engine config settings for the master instances
in a cluster.. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The Compute Engine accelerator configuration for these instances. Can be specified multiple times.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">acceleratorCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of the accelerator cards of this type exposed to this instance. Often restricted to one of <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code>, or <code class="docutils literal notranslate"><span class="pre">8</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">accelerator_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The short name of the accelerator type to expose to this instance. For example, <code class="docutils literal notranslate"><span class="pre">nvidia-tesla-k80</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Disk Config</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskSizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The disk type of the primary disk attached to each preemptible worker node.
One of <code class="docutils literal notranslate"><span class="pre">&quot;pd-ssd&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numLocalSsds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URI for the image to use for this worker.  See <a class="reference external" href="https://cloud.google.com/dataproc/docs/guides/dataproc-images">the guide</a>
for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceNames</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of a Google Compute Engine machine type
to create for the worker nodes. If not specified, GCP will default to a predetermined
computed value (currently <code class="docutils literal notranslate"><span class="pre">n1-standard-4</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of a minimum generation of CPU family
for the master. If not specified, GCP will default to a predetermined computed value
for each zone. See <a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">the guide</a>
for details about which CPU families are available (and defaulted) for each zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptibleWorkerConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Google Compute Engine config settings for the additional (aka
preemptible) instances in a cluster. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">diskConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Disk Config</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskSizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The disk type of the primary disk attached to each preemptible worker node.
One of <code class="docutils literal notranslate"><span class="pre">&quot;pd-ssd&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numLocalSsds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceNames</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Security related configuration. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kerberosConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Kerberos Configuration</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustAdminServer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The admin server (IP or hostname) for the
remote trusted realm in a cross realm trust relationship.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustKdc</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The KDC (IP or hostname) for the
remote trusted realm in a cross realm trust relationship.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustRealm</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The remote realm the Dataproc on-cluster KDC will
trust, should the user enable cross realm trust.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustSharedPasswordUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Cloud Storage URI of a KMS
encrypted file containing the shared password between the on-cluster Kerberos realm
and the remote trusted realm, in a cross realm trust relationship.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableKerberos</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Flag to indicate whether to Kerberize the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kdcDbKeyUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Cloud Storage URI of a KMS encrypted file containing
the master key of the KDC database.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyPasswordUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Cloud Storage URI of a KMS encrypted file containing
the password to the user provided key. For the self-signed certificate, this password
is generated by Dataproc.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keystorePasswordUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Cloud Storage URI of a KMS encrypted file containing
the password to the user provided keystore. For the self-signed certificated, the password
is generated by Dataproc.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keystoreUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Cloud Storage URI of the keystore file used for SSL encryption.
If not provided, Dataproc will provide a self-signed certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeyUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URI of the KMS key used to encrypt various sensitive files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">realm</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the on-cluster Kerberos realm. If not specified, the
uppercased domain of hostnames will be the realm.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootPrincipalPasswordUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Cloud Storage URI of a KMS encrypted file
containing the root principal password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tgtLifetimeHours</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The lifetime of the ticket granting ticket, in hours.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">truststorePasswordUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Cloud Storage URI of a KMS encrypted file
containing the password to the user provided truststore. For the self-signed
certificate, this password is generated by Dataproc.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">truststoreUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Cloud Storage URI of the truststore file used for
SSL encryption. If not provided, Dataproc will provide a self-signed certificate.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">softwareConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The config settings for software inside the cluster.
Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">imageVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Cloud Dataproc image version to use
for the cluster - this controls the sets of software versions
installed onto the nodes when you create clusters. If not specified, defaults to the
latest version. For a list of valid versions see
<a class="reference external" href="https://cloud.google.com/dataproc/docs/concepts/dataproc-versions">Cloud Dataproc versions</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">optionalComponents</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The set of optional components to activate on the cluster. 
Accepted values are:</p>
<ul>
<li><p>ANACONDA</p></li>
<li><p>DRUID</p></li>
<li><p>HIVE_WEBHCAT</p></li>
<li><p>JUPYTER</p></li>
<li><p>KERBEROS</p></li>
<li><p>PRESTO</p></li>
<li><p>ZEPPELIN</p></li>
<li><p>ZOOKEEPER</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A list of override and additional properties (key/value pairs)
used to modify various aspects of the common configuration files used when creating
a cluster. For a list of valid properties please see
<a class="reference external" href="https://cloud.google.com/dataproc/docs/concepts/cluster-properties">Cluster properties</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">stagingBucket</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Cloud Storage staging bucket used to stage files,
such as Hadoop jars, between client machines and the cluster.
Note: If you don’t explicitly specify a <code class="docutils literal notranslate"><span class="pre">staging_bucket</span></code>
then GCP will auto create / assign one for you. However, you are not guaranteed
an auto generated bucket which is solely dedicated to your cluster; it may be shared
with other clusters in the same region/zone also choosing to use the auto generation
option.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">worker_config</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Google Compute Engine config settings for the worker instances
in a cluster.. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The Compute Engine accelerator configuration for these instances. Can be specified multiple times.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">acceleratorCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of the accelerator cards of this type exposed to this instance. Often restricted to one of <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code>, or <code class="docutils literal notranslate"><span class="pre">8</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">accelerator_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The short name of the accelerator type to expose to this instance. For example, <code class="docutils literal notranslate"><span class="pre">nvidia-tesla-k80</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Disk Config</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskSizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The disk type of the primary disk attached to each preemptible worker node.
One of <code class="docutils literal notranslate"><span class="pre">&quot;pd-ssd&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numLocalSsds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URI for the image to use for this worker.  See <a class="reference external" href="https://cloud.google.com/dataproc/docs/guides/dataproc-images">the guide</a>
for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceNames</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of a Google Compute Engine machine type
to create for the worker nodes. If not specified, GCP will default to a predetermined
computed value (currently <code class="docutils literal notranslate"><span class="pre">n1-standard-4</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of a minimum generation of CPU family
for the master. If not specified, GCP will default to a predetermined computed value
for each zone. See <a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">the guide</a>
for details about which CPU families are available (and defaulted) for each zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Cluster.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Cluster.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including <code class="docutils literal notranslate"><span class="pre">goog-dataproc-cluster-name</span></code>
which is the name of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Cluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the cluster, unique within the project and
zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Cluster.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Cluster.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the <code class="docutils literal notranslate"><span class="pre">cluster</span></code> will exist. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Cluster.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Cluster.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which the cluster and associated nodes will be created in.
Defaults to <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_config=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Allows you to configure various aspects of the cluster.
Structure defined below.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including <code class="docutils literal notranslate"><span class="pre">goog-dataproc-cluster-name</span></code>
which is the name of the cluster.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the cluster, unique within the project and
zone.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the <code class="docutils literal notranslate"><span class="pre">cluster</span></code> will exist. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the cluster and associated nodes will be created in.
Defaults to <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cluster_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscalingConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The autoscaling policy config associated with the cluster.
Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">policyUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The autoscaling policy used by the cluster.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Customer managed encryption keys settings for the cluster.
Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud KMS key name to use for PD disk encryption for
all instances in the cluster.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">gceClusterConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Common config settings for resources of Google Compute Engine cluster
instances, applicable to all instances in the cluster. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">internalIpOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - By default, clusters are not restricted to internal IP addresses, 
and will have ephemeral external IP addresses assigned to each instance. If set to true, all
instances in the cluster will only have internal IP addresses. Note: Private Google Access
(also known as <code class="docutils literal notranslate"><span class="pre">privateIpGoogleAccess</span></code>) must be enabled on the subnetwork that the cluster
will be launched in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of the Compute Engine metadata entries to add to all instances
(see <a class="reference external" href="https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata">Project and instance metadata</a>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name or self_link of the Google Compute Engine
network to the cluster will be part of. Conflicts with <code class="docutils literal notranslate"><span class="pre">subnetwork</span></code>.
If neither is specified, this defaults to the “default” network.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service account to be used by the Node VMs.
If not specified, the “default” service account is used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccountScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of Google API scopes
to be made available on all of the node VMs under the <code class="docutils literal notranslate"><span class="pre">service_account</span></code>
specified. These can be   either FQDNs, or scope aliases. The following scopes
must be set if any other scopes are set. They’re necessary to ensure the
correct functioning ofthe cluster, and are set automatically by the API:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name or self_link of the Google Compute Engine
subnetwork the cluster will be part of. Conflicts with <code class="docutils literal notranslate"><span class="pre">network</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of instance tags applied to instances in the cluster.
Tags are used to identify valid sources or targets for network firewalls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The GCP zone where your data is stored and used (i.e. where
the master and the worker nodes will be created in). If <code class="docutils literal notranslate"><span class="pre">region</span></code> is set to ‘global’ (default)
then <code class="docutils literal notranslate"><span class="pre">zone</span></code> is mandatory, otherwise GCP is able to make use of <a class="reference external" href="https://cloud.google.com/dataproc/docs/concepts/auto-zone">Auto Zone Placement</a>
to determine this automatically for you.
Note: This setting additionally determines and restricts
which computing resources are available for use with other configs such as
<code class="docutils literal notranslate"><span class="pre">cluster_config.master_config.machine_type</span></code> and <code class="docutils literal notranslate"><span class="pre">cluster_config.worker_config.machine_type</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initializationActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Commands to execute on each node after config is completed.
You can specify multiple versions of these. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">script</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout_sec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum duration (in seconds) which <code class="docutils literal notranslate"><span class="pre">script</span></code> is
allowed to take to execute its action. GCP will default to a predetermined
computed value if not set (currently 300).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifecycleConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoDeleteTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time when cluster will be auto-deleted.
A timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds.
Example: “2014-10-02T15:01:23.045123456Z”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idleDeleteTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The duration to keep the cluster alive while idling
(no jobs running). After this TTL, the cluster will be deleted. Valid range: [10m, 14d].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idleStartTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Google Compute Engine config settings for the master instances
in a cluster.. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The Compute Engine accelerator configuration for these instances. Can be specified multiple times.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">acceleratorCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of the accelerator cards of this type exposed to this instance. Often restricted to one of <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code>, or <code class="docutils literal notranslate"><span class="pre">8</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">accelerator_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The short name of the accelerator type to expose to this instance. For example, <code class="docutils literal notranslate"><span class="pre">nvidia-tesla-k80</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Disk Config</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskSizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The disk type of the primary disk attached to each preemptible worker node.
One of <code class="docutils literal notranslate"><span class="pre">&quot;pd-ssd&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numLocalSsds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI for the image to use for this worker.  See <a class="reference external" href="https://cloud.google.com/dataproc/docs/guides/dataproc-images">the guide</a>
for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a Google Compute Engine machine type
to create for the worker nodes. If not specified, GCP will default to a predetermined
computed value (currently <code class="docutils literal notranslate"><span class="pre">n1-standard-4</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a minimum generation of CPU family
for the master. If not specified, GCP will default to a predetermined computed value
for each zone. See <a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">the guide</a>
for details about which CPU families are available (and defaulted) for each zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptibleWorkerConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Google Compute Engine config settings for the additional (aka
preemptible) instances in a cluster. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">diskConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Disk Config</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskSizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The disk type of the primary disk attached to each preemptible worker node.
One of <code class="docutils literal notranslate"><span class="pre">&quot;pd-ssd&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numLocalSsds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Security related configuration. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kerberosConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Kerberos Configuration</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustAdminServer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The admin server (IP or hostname) for the
remote trusted realm in a cross realm trust relationship.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustKdc</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The KDC (IP or hostname) for the
remote trusted realm in a cross realm trust relationship.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustRealm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The remote realm the Dataproc on-cluster KDC will
trust, should the user enable cross realm trust.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustSharedPasswordUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage URI of a KMS
encrypted file containing the shared password between the on-cluster Kerberos realm
and the remote trusted realm, in a cross realm trust relationship.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableKerberos</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Flag to indicate whether to Kerberize the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kdcDbKeyUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage URI of a KMS encrypted file containing
the master key of the KDC database.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyPasswordUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage URI of a KMS encrypted file containing
the password to the user provided key. For the self-signed certificate, this password
is generated by Dataproc.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keystorePasswordUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage URI of a KMS encrypted file containing
the password to the user provided keystore. For the self-signed certificated, the password
is generated by Dataproc.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keystoreUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage URI of the keystore file used for SSL encryption.
If not provided, Dataproc will provide a self-signed certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kmsKeyUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI of the KMS key used to encrypt various sensitive files.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">realm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the on-cluster Kerberos realm. If not specified, the
uppercased domain of hostnames will be the realm.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootPrincipalPasswordUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage URI of a KMS encrypted file
containing the root principal password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tgtLifetimeHours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The lifetime of the ticket granting ticket, in hours.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">truststorePasswordUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage URI of a KMS encrypted file
containing the password to the user provided truststore. For the self-signed
certificate, this password is generated by Dataproc.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">truststoreUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage URI of the truststore file used for
SSL encryption. If not provided, Dataproc will provide a self-signed certificate.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">softwareConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The config settings for software inside the cluster.
Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">imageVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Dataproc image version to use
for the cluster - this controls the sets of software versions
installed onto the nodes when you create clusters. If not specified, defaults to the
latest version. For a list of valid versions see
<a class="reference external" href="https://cloud.google.com/dataproc/docs/concepts/dataproc-versions">Cloud Dataproc versions</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">optionalComponents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of optional components to activate on the cluster. 
Accepted values are:</p>
<ul>
<li><p>ANACONDA</p></li>
<li><p>DRUID</p></li>
<li><p>HIVE_WEBHCAT</p></li>
<li><p>JUPYTER</p></li>
<li><p>KERBEROS</p></li>
<li><p>PRESTO</p></li>
<li><p>ZEPPELIN</p></li>
<li><p>ZOOKEEPER</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrideProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A list of override and additional properties (key/value pairs)
used to modify various aspects of the common configuration files used when creating
a cluster. For a list of valid properties please see
<a class="reference external" href="https://cloud.google.com/dataproc/docs/concepts/cluster-properties">Cluster properties</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">stagingBucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Cloud Storage staging bucket used to stage files,
such as Hadoop jars, between client machines and the cluster.
Note: If you don’t explicitly specify a <code class="docutils literal notranslate"><span class="pre">staging_bucket</span></code>
then GCP will auto create / assign one for you. However, you are not guaranteed
an auto generated bucket which is solely dedicated to your cluster; it may be shared
with other clusters in the same region/zone also choosing to use the auto generation
option.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">worker_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Google Compute Engine config settings for the worker instances
in a cluster.. Structure defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The Compute Engine accelerator configuration for these instances. Can be specified multiple times.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">acceleratorCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of the accelerator cards of this type exposed to this instance. Often restricted to one of <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">4</span></code>, or <code class="docutils literal notranslate"><span class="pre">8</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">accelerator_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The short name of the accelerator type to expose to this instance. For example, <code class="docutils literal notranslate"><span class="pre">nvidia-tesla-k80</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Disk Config</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskSizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The disk type of the primary disk attached to each preemptible worker node.
One of <code class="docutils literal notranslate"><span class="pre">&quot;pd-ssd&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;pd-standard&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numLocalSsds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI for the image to use for this worker.  See <a class="reference external" href="https://cloud.google.com/dataproc/docs/guides/dataproc-images">the guide</a>
for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a Google Compute Engine machine type
to create for the worker nodes. If not specified, GCP will default to a predetermined
computed value (currently <code class="docutils literal notranslate"><span class="pre">n1-standard-4</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a minimum generation of CPU family
for the master. If not specified, GCP will default to a predetermined computed value
for each zone. See <a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">the guide</a>
for details about which CPU families are available (and defaulted) for each zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.ClusterIAMBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dataproc.</code><code class="sig-name descname">ClusterIAMBinding</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage IAM policies on dataproc clusters. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMPolicy</span></code>: Authoritative. Sets the IAM policy for the cluster and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the cluster are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the cluster are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMMember</span></code> or they will fight over what your policy should be. In addition, be careful not to accidentally unset ownership of the cluster as <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMPolicy</span></code> replaces the entire policy.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or relative resource id of the cluster to manage IAM policies for.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the cluster belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the cluster belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.dataproc.ClusterIAMBinding.cluster">
<code class="sig-name descname">cluster</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMBinding.cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or relative resource id of the cluster to manage IAM policies for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.ClusterIAMBinding.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the clusters’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.ClusterIAMBinding.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the cluster belongs. If it
is not provided, the provider will use a default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.ClusterIAMBinding.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMBinding.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which the cluster belongs. If it
is not provided, the provider will use a default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.ClusterIAMBinding.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.ClusterIAMBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClusterIAMBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or relative resource id of the cluster to manage IAM policies for.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the clusters’s IAM policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the cluster belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the cluster belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.ClusterIAMBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.ClusterIAMBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.ClusterIAMMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dataproc.</code><code class="sig-name descname">ClusterIAMMember</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage IAM policies on dataproc clusters. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMPolicy</span></code>: Authoritative. Sets the IAM policy for the cluster and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the cluster are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the cluster are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMMember</span></code> or they will fight over what your policy should be. In addition, be careful not to accidentally unset ownership of the cluster as <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMPolicy</span></code> replaces the entire policy.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or relative resource id of the cluster to manage IAM policies for.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the cluster belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the cluster belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.dataproc.ClusterIAMMember.cluster">
<code class="sig-name descname">cluster</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMMember.cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or relative resource id of the cluster to manage IAM policies for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.ClusterIAMMember.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the clusters’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.ClusterIAMMember.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the cluster belongs. If it
is not provided, the provider will use a default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.ClusterIAMMember.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMMember.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which the cluster belongs. If it
is not provided, the provider will use a default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.ClusterIAMMember.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.ClusterIAMMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClusterIAMMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or relative resource id of the cluster to manage IAM policies for.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the clusters’s IAM policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the cluster belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the cluster belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.ClusterIAMMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.ClusterIAMMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.ClusterIAMPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dataproc.</code><code class="sig-name descname">ClusterIAMPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage IAM policies on dataproc clusters. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMPolicy</span></code>: Authoritative. Sets the IAM policy for the cluster and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the cluster are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the cluster are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMMember</span></code> or they will fight over what your policy should be. In addition, be careful not to accidentally unset ownership of the cluster as <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMPolicy</span></code> replaces the entire policy.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">dataproc.ClusterIAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or relative resource id of the cluster to manage IAM policies for.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the cluster belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the cluster belongs. If it
is not provided, the provider will use a default.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.dataproc.ClusterIAMPolicy.cluster">
<code class="sig-name descname">cluster</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMPolicy.cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or relative resource id of the cluster to manage IAM policies for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.ClusterIAMPolicy.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the clusters’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.ClusterIAMPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.ClusterIAMPolicy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the cluster belongs. If it
is not provided, the provider will use a default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.ClusterIAMPolicy.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMPolicy.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which the cluster belongs. If it
is not provided, the provider will use a default.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.ClusterIAMPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClusterIAMPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or relative resource id of the cluster to manage IAM policies for.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the clusters’s IAM policy.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the cluster belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the cluster belongs. If it
is not provided, the provider will use a default.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.ClusterIAMPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.ClusterIAMPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.ClusterIAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.Job">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dataproc.</code><code class="sig-name descname">Job</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">force_delete=None</em>, <em class="sig-param">hadoop_config=None</em>, <em class="sig-param">hive_config=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">pig_config=None</em>, <em class="sig-param">placement=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">pyspark_config=None</em>, <em class="sig-param">reference=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">scheduling=None</em>, <em class="sig-param">spark_config=None</em>, <em class="sig-param">sparksql_config=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.Job" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a job resource within a Dataproc cluster within GCE. For more information see
<a class="reference external" href="https://cloud.google.com/dataproc/">the official dataproc documentation</a>.</p>
<p>!&gt; <strong>Note:</strong> This resource does not support ‘update’ and changing any attributes will cause the resource to be recreated.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The list of labels (key/value pairs) to add to the job.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the <code class="docutils literal notranslate"><span class="pre">cluster</span></code> can be found and jobs
subsequently run against. If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p></li>
<li><p><strong>scheduling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Optional. Job scheduling configuration.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>hadoop_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">archiveUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jarFileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of jar files to be added to the Spark CLASSPATH.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">driverLogLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mainClass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mainJarFileUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HCFS URI of the jar file containing the main class. Examples: ‘gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar’ ‘hdfs:/tmp/test-samples/custom-wordcount.jar’ ‘file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar’. Conflicts with <code class="docutils literal notranslate"><span class="pre">main_class</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of property names to values, used to configure Spark SQL’s SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.</p></li>
</ul>
<p>The <strong>hive_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">continueOnFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jarFileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of jar files to be added to the Spark CLASSPATH.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of property names to values, used to configure Spark SQL’s SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryFileUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HCFS URI of the script that contains SQL queries.
Conflicts with <code class="docutils literal notranslate"><span class="pre">query_list</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryLists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scriptVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Mapping of query variable names to values (equivalent to the Spark SQL command: <code class="docutils literal notranslate"><span class="pre">SET</span> <span class="pre">name=&quot;value&quot;;</span></code>).</p></li>
</ul>
<p>The <strong>pig_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">continueOnFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jarFileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of jar files to be added to the Spark CLASSPATH.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">driverLogLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of property names to values, used to configure Spark SQL’s SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryFileUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HCFS URI of the script that contains SQL queries.
Conflicts with <code class="docutils literal notranslate"><span class="pre">query_list</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryLists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scriptVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Mapping of query variable names to values (equivalent to the Spark SQL command: <code class="docutils literal notranslate"><span class="pre">SET</span> <span class="pre">name=&quot;value&quot;;</span></code>).</p></li>
</ul>
<p>The <strong>placement</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clusterName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterUuid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>pyspark_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">archiveUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jarFileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of jar files to be added to the Spark CLASSPATH.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">driverLogLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mainPythonFileUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of property names to values, used to configure Spark SQL’s SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pythonFileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS file URIs of Python files to pass to the PySpark framework. Supported file types: .py, .egg, and .zip.</p></li>
</ul>
<p>The <strong>reference</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">job_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scheduling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxFailuresPerHour</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>spark_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">archiveUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jarFileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of jar files to be added to the Spark CLASSPATH.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">driverLogLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mainClass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mainJarFileUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HCFS URI of the jar file containing the main class. Examples: ‘gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar’ ‘hdfs:/tmp/test-samples/custom-wordcount.jar’ ‘file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar’. Conflicts with <code class="docutils literal notranslate"><span class="pre">main_class</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of property names to values, used to configure Spark SQL’s SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.</p></li>
</ul>
<p>The <strong>sparksql_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">jarFileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of jar files to be added to the Spark CLASSPATH.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">driverLogLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of property names to values, used to configure Spark SQL’s SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryFileUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HCFS URI of the script that contains SQL queries.
Conflicts with <code class="docutils literal notranslate"><span class="pre">query_list</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryLists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scriptVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Mapping of query variable names to values (equivalent to the Spark SQL command: <code class="docutils literal notranslate"><span class="pre">SET</span> <span class="pre">name=&quot;value&quot;;</span></code>).</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Job.driver_controls_files_uri">
<code class="sig-name descname">driver_controls_files_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Job.driver_controls_files_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Job.driver_output_resource_uri">
<code class="sig-name descname">driver_output_resource_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Job.driver_output_resource_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>A URI pointing to the location of the stdout of the job’s driver program.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Job.force_delete">
<code class="sig-name descname">force_delete</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Job.force_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Job.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Job.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of labels (key/value pairs) to add to the job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Job.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Job.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the <code class="docutils literal notranslate"><span class="pre">cluster</span></code> can be found and jobs
subsequently run against. If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Job.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Job.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Job.scheduling">
<code class="sig-name descname">scheduling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Job.scheduling" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional. Job scheduling configuration.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxFailuresPerHour</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.Job.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">driver_controls_files_uri=None</em>, <em class="sig-param">driver_output_resource_uri=None</em>, <em class="sig-param">force_delete=None</em>, <em class="sig-param">hadoop_config=None</em>, <em class="sig-param">hive_config=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">pig_config=None</em>, <em class="sig-param">placement=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">pyspark_config=None</em>, <em class="sig-param">reference=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">scheduling=None</em>, <em class="sig-param">spark_config=None</em>, <em class="sig-param">sparksql_config=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.Job.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Job resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>driver_controls_files_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri.</p></li>
<li><p><strong>driver_output_resource_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A URI pointing to the location of the stdout of the job’s driver program.</p></li>
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The list of labels (key/value pairs) to add to the job.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the <code class="docutils literal notranslate"><span class="pre">cluster</span></code> can be found and jobs
subsequently run against. If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p></li>
<li><p><strong>scheduling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Optional. Job scheduling configuration.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>hadoop_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">archiveUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jarFileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of jar files to be added to the Spark CLASSPATH.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">driverLogLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mainClass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mainJarFileUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HCFS URI of the jar file containing the main class. Examples: ‘gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar’ ‘hdfs:/tmp/test-samples/custom-wordcount.jar’ ‘file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar’. Conflicts with <code class="docutils literal notranslate"><span class="pre">main_class</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of property names to values, used to configure Spark SQL’s SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.</p></li>
</ul>
<p>The <strong>hive_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">continueOnFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jarFileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of jar files to be added to the Spark CLASSPATH.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of property names to values, used to configure Spark SQL’s SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryFileUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HCFS URI of the script that contains SQL queries.
Conflicts with <code class="docutils literal notranslate"><span class="pre">query_list</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryLists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scriptVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Mapping of query variable names to values (equivalent to the Spark SQL command: <code class="docutils literal notranslate"><span class="pre">SET</span> <span class="pre">name=&quot;value&quot;;</span></code>).</p></li>
</ul>
<p>The <strong>pig_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">continueOnFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jarFileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of jar files to be added to the Spark CLASSPATH.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">driverLogLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of property names to values, used to configure Spark SQL’s SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryFileUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HCFS URI of the script that contains SQL queries.
Conflicts with <code class="docutils literal notranslate"><span class="pre">query_list</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryLists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scriptVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Mapping of query variable names to values (equivalent to the Spark SQL command: <code class="docutils literal notranslate"><span class="pre">SET</span> <span class="pre">name=&quot;value&quot;;</span></code>).</p></li>
</ul>
<p>The <strong>placement</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clusterName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterUuid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>pyspark_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">archiveUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jarFileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of jar files to be added to the Spark CLASSPATH.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">driverLogLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mainPythonFileUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of property names to values, used to configure Spark SQL’s SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pythonFileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS file URIs of Python files to pass to the PySpark framework. Supported file types: .py, .egg, and .zip.</p></li>
</ul>
<p>The <strong>reference</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">job_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scheduling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxFailuresPerHour</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>spark_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">archiveUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jarFileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of jar files to be added to the Spark CLASSPATH.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">driverLogLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mainClass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mainJarFileUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HCFS URI of the jar file containing the main class. Examples: ‘gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar’ ‘hdfs:/tmp/test-samples/custom-wordcount.jar’ ‘file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar’. Conflicts with <code class="docutils literal notranslate"><span class="pre">main_class</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of property names to values, used to configure Spark SQL’s SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.</p></li>
</ul>
<p>The <strong>sparksql_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">jarFileUris</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HCFS URIs of jar files to be added to the Spark CLASSPATH.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">driverLogLevels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of property names to values, used to configure Spark SQL’s SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryFileUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HCFS URI of the script that contains SQL queries.
Conflicts with <code class="docutils literal notranslate"><span class="pre">query_list</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryLists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scriptVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Mapping of query variable names to values (equivalent to the Spark SQL command: <code class="docutils literal notranslate"><span class="pre">SET</span> <span class="pre">name=&quot;value&quot;;</span></code>).</p></li>
</ul>
<p>The <strong>status</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">details</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stateStartTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">substate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.Job.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.Job.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.Job.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.Job.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.JobIAMBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dataproc.</code><code class="sig-name descname">JobIAMBinding</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">job_id=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage IAM policies on dataproc jobs. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMPolicy</span></code>: Authoritative. Sets the IAM policy for the job and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the job are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the job are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMMember</span></code> or they will fight over what your policy should be. In addition, be careful not to accidentally unset ownership of the job as <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMPolicy</span></code> replaces the entire policy.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the job belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the job belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.dataproc.JobIAMBinding.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the jobs’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.JobIAMBinding.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the job belongs. If it
is not provided, the provider will use a default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.JobIAMBinding.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMBinding.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which the job belongs. If it
is not provided, the provider will use a default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.JobIAMBinding.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.JobIAMBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">job_id=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing JobIAMBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the jobs’s IAM policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the job belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the job belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.JobIAMBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.JobIAMBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.JobIAMMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dataproc.</code><code class="sig-name descname">JobIAMMember</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">job_id=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage IAM policies on dataproc jobs. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMPolicy</span></code>: Authoritative. Sets the IAM policy for the job and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the job are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the job are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMMember</span></code> or they will fight over what your policy should be. In addition, be careful not to accidentally unset ownership of the job as <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMPolicy</span></code> replaces the entire policy.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the job belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the job belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.dataproc.JobIAMMember.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the jobs’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.JobIAMMember.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the job belongs. If it
is not provided, the provider will use a default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.JobIAMMember.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMMember.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which the job belongs. If it
is not provided, the provider will use a default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.JobIAMMember.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.JobIAMMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">job_id=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing JobIAMMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the jobs’s IAM policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the job belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the job belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.JobIAMMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.JobIAMMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.JobIAMPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dataproc.</code><code class="sig-name descname">JobIAMPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">job_id=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage IAM policies on dataproc jobs. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMPolicy</span></code>: Authoritative. Sets the IAM policy for the job and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the job are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the job are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMMember</span></code> or they will fight over what your policy should be. In addition, be careful not to accidentally unset ownership of the job as <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMPolicy</span></code> replaces the entire policy.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">dataproc.JobIAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the job belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the job belongs. If it
is not provided, the provider will use a default.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.dataproc.JobIAMPolicy.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the jobs’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.JobIAMPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.JobIAMPolicy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the job belongs. If it
is not provided, the provider will use a default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.JobIAMPolicy.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMPolicy.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which the job belongs. If it
is not provided, the provider will use a default.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.JobIAMPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">job_id=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing JobIAMPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the jobs’s IAM policy.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the job belongs. If it
is not provided, the provider will use a default.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the job belongs. If it
is not provided, the provider will use a default.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.JobIAMPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.JobIAMPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.JobIAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
