<div class="section" id="module-pulumi_gcp.compute">
<span id="compute"></span><h1>compute<a class="headerlink" href="#module-pulumi_gcp.compute" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.compute.Address">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">Address</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>address=None</em>, <em>address_type=None</em>, <em>description=None</em>, <em>labels=None</em>, <em>name=None</em>, <em>network_tier=None</em>, <em>project=None</em>, <em>region=None</em>, <em>subnetwork=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Address" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents an Address resource.</p>
<p>Each virtual machine instance has an ephemeral internal IP address and,
optionally, an external IP address. To communicate between instances on
the same network, you can use an instance’s internal IP address. To
communicate with the Internet and instances outside of the same network,
you must specify the instance’s external IP address.</p>
<p>Internal IP addresses are ephemeral and only belong to an instance for
the lifetime of the instance; if the instance is deleted and recreated,
the instance is assigned a new internal IP address, either by Compute
Engine or by you. External IP addresses can be either ephemeral or
static.</p>
<p>To get more information about Address, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/beta/addresses">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/instances-and-network">Reserving a Static External IP Address</a></li>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/ip-addresses/reserve-static-internal-ip-address">Reserving a Static Internal IP Address</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=address_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP of the created resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] address_type
:param pulumi.Input[str] description
:param pulumi.Input[dict] labels
:param pulumi.Input[str] name
:param pulumi.Input[str] network_tier
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[str] region
:param pulumi.Input[str] subnetwork</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Address.address">
<code class="descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Address.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Address.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Address.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Address.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Address.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Address.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Address.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Address.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Address.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.AttachedDisk">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">AttachedDisk</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>device_name=None</em>, <em>disk=None</em>, <em>instance=None</em>, <em>mode=None</em>, <em>project=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AttachedDisk" title="Permalink to this definition">¶</a></dt>
<dd><p>Persistent disks can be attached to a compute instance using <cite>the ``attached_disk`</cite>
section within the compute instance configuration &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/google/r/compute_instance.html#attached_disk">https://www.terraform.io/docs/providers/google/r/compute_instance.html#attached_disk</a>&gt;`_.
However there may be situations where managing the attached disks via the compute
instance config isn’t preferable or possible, such as attaching dynamic
numbers of disks using the <code class="docutils literal notranslate"><span class="pre">count</span></code> variable.</p>
<p>To get more information about attaching disks, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/instances/attachDisk">API documentation</a></li>
<li><a class="reference external" href="https://www.terraform.io/docs/providers/google/r/compute_disk.html">Resource: google_compute_disk</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/disks/add-persistent-disk">Adding a persistent disk</a></li>
</ul>
</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] device_name
:param pulumi.Input[str] disk
:param pulumi.Input[str] instance
:param pulumi.Input[str] mode
:param pulumi.Input[str] project
:param pulumi.Input[str] zone</p>
<dl class="method">
<dt id="pulumi_gcp.compute.AttachedDisk.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AttachedDisk.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.AttachedDisk.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.AttachedDisk.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Autoscalar">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">Autoscalar</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>autoscaling_policy=None</em>, <em>description=None</em>, <em>name=None</em>, <em>project=None</em>, <em>target=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Autoscalar" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents an Autoscaler resource.</p>
<p>Autoscalers allow you to automatically scale virtual machine instances in
managed instance groups according to an autoscaling policy that you
define.</p>
<p>To get more information about Autoscaler, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/autoscalers">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/autoscaler/">Autoscaling Groups of Instances</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=autoscaler_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[dict] autoscaling_policy
:param pulumi.Input[str] description
:param pulumi.Input[str] name
:param pulumi.Input[str] project
:param pulumi.Input[str] target
:param pulumi.Input[str] zone</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Autoscalar.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Autoscalar.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Autoscalar.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Autoscalar.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Autoscalar.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Autoscalar.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.BackendBucket">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">BackendBucket</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket_name=None</em>, <em>description=None</em>, <em>enable_cdn=None</em>, <em>name=None</em>, <em>project=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendBucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Backend buckets allow you to use Google Cloud Storage buckets with HTTP(S)
load balancing.</p>
<p>An HTTP(S) load balancer can direct traffic to specified URLs to a
backend bucket rather than a backend service. It can send requests for
static content to a Cloud Storage bucket and requests for dynamic content
a virtual machine instance.</p>
<p>To get more information about BackendBucket, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/backendBuckets">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/http/backend-bucket">Using a Cloud Storage bucket as a load balancer backend</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=backend_bucket_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] bucket_name
:param pulumi.Input[str] description
:param pulumi.Input[bool] enable_cdn
:param pulumi.Input[str] name
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendBucket.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendBucket.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendBucket.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendBucket.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.BackendBucket.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendBucket.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.BackendBucket.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendBucket.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.BackendService">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">BackendService</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>backends=None</em>, <em>cdn_policy=None</em>, <em>connection_draining_timeout_sec=None</em>, <em>custom_request_headers=None</em>, <em>description=None</em>, <em>enable_cdn=None</em>, <em>health_checks=None</em>, <em>iap=None</em>, <em>name=None</em>, <em>port_name=None</em>, <em>project=None</em>, <em>protocol=None</em>, <em>security_policy=None</em>, <em>session_affinity=None</em>, <em>timeout_sec=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendService" title="Permalink to this definition">¶</a></dt>
<dd><p>A Backend Service defines a group of virtual machines that will serve traffic for load balancing. For more information
see <a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/http/backend-service">the official documentation</a>
and the <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/backendServices">API</a>.</p>
<p>For internal load balancing, use a <a class="reference external" href="https://www.terraform.io/docs/providers/google/r/compute_region_backend_service.html">google_compute_region_backend_service</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>backends</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of backends that serve this BackendService. Structure is documented below.</li>
<li><strong>cdn_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Cloud CDN configuration for this BackendService. Structure is documented below.</li>
<li><strong>connection_draining_timeout_sec</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Time for which instance will be drained (not accept new connections,
but still work to finish started ones). Defaults to <code class="docutils literal notranslate"><span class="pre">300</span></code>.</li>
<li><strong>custom_request_headers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Headers that the
HTTP/S load balancer should add to proxied requests. See <a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/http/backend-service#user-defined-request-headers">guide</a> for details.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta fields.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The textual description for the backend service.</li>
<li><strong>enable_cdn</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to enable the Cloud CDN on the backend service.</li>
<li><strong>health_checks</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a list of HTTP/HTTPS health checks
for checking the health of the backend service. Currently at most one health
check can be specified, and a health check is required.</li>
<li><strong>iap</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specification for the Identity-Aware proxy. Disabled if not specified. Structure is documented below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the backend service.</li>
<li><strong>port_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a service that has been added to an
instance group in this backend. See <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/#specifying_service_endpoints">related docs</a> for details. Defaults to http.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol for incoming requests. Defaults to
<code class="docutils literal notranslate"><span class="pre">HTTP</span></code>.</li>
<li><strong>security_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name or URI of a
<a class="reference external" href="https://cloud.google.com/armor/docs/security-policy-concepts">security policy</a> to add to the backend service.</li>
<li><strong>session_affinity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How to distribute load. Options are <code class="docutils literal notranslate"><span class="pre">NONE</span></code> (no
affinity), <code class="docutils literal notranslate"><span class="pre">CLIENT_IP</span></code> (hash of the source/dest addresses / ports), and
<code class="docutils literal notranslate"><span class="pre">GENERATED_COOKIE</span></code> (distribute load using a generated session cookie).</li>
<li><strong>timeout_sec</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of secs to wait for a backend to respond
to a request before considering the request failed. Defaults to <code class="docutils literal notranslate"><span class="pre">30</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.backends">
<code class="descname">backends</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.backends" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of backends that serve this BackendService. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.cdn_policy">
<code class="descname">cdn_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.cdn_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud CDN configuration for this BackendService. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.connection_draining_timeout_sec">
<code class="descname">connection_draining_timeout_sec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.connection_draining_timeout_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>Time for which instance will be drained (not accept new connections,
but still work to finish started ones). Defaults to <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.custom_request_headers">
<code class="descname">custom_request_headers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.custom_request_headers" title="Permalink to this definition">¶</a></dt>
<dd><p>Headers that the
HTTP/S load balancer should add to proxied requests. See <a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/http/backend-service#user-defined-request-headers">guide</a> for details.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The textual description for the backend service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.enable_cdn">
<code class="descname">enable_cdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.enable_cdn" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to enable the Cloud CDN on the backend service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the backend service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.health_checks">
<code class="descname">health_checks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.health_checks" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a list of HTTP/HTTPS health checks
for checking the health of the backend service. Currently at most one health
check can be specified, and a health check is required.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.iap">
<code class="descname">iap</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.iap" title="Permalink to this definition">¶</a></dt>
<dd><p>Specification for the Identity-Aware proxy. Disabled if not specified. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the backend service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.port_name">
<code class="descname">port_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.port_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a service that has been added to an
instance group in this backend. See <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/#specifying_service_endpoints">related docs</a> for details. Defaults to http.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.protocol">
<code class="descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol for incoming requests. Defaults to
<code class="docutils literal notranslate"><span class="pre">HTTP</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.security_policy">
<code class="descname">security_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.security_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Name or URI of a
<a class="reference external" href="https://cloud.google.com/armor/docs/security-policy-concepts">security policy</a> to add to the backend service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.session_affinity">
<code class="descname">session_affinity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.session_affinity" title="Permalink to this definition">¶</a></dt>
<dd><p>How to distribute load. Options are <code class="docutils literal notranslate"><span class="pre">NONE</span></code> (no
affinity), <code class="docutils literal notranslate"><span class="pre">CLIENT_IP</span></code> (hash of the source/dest addresses / ports), and
<code class="docutils literal notranslate"><span class="pre">GENERATED_COOKIE</span></code> (distribute load using a generated session cookie).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.BackendService.timeout_sec">
<code class="descname">timeout_sec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.BackendService.timeout_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of secs to wait for a backend to respond
to a request before considering the request failed. Defaults to <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.BackendService.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.BackendService.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.BackendService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Disk">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">Disk</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>disk_encryption_key=None</em>, <em>disk_encryption_key_raw=None</em>, <em>image=None</em>, <em>labels=None</em>, <em>name=None</em>, <em>project=None</em>, <em>size=None</em>, <em>snapshot=None</em>, <em>source_image_encryption_key=None</em>, <em>source_snapshot_encryption_key=None</em>, <em>type=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Disk" title="Permalink to this definition">¶</a></dt>
<dd><p>Persistent disks are durable storage devices that function similarly to
the physical disks in a desktop or a server. Compute Engine manages the
hardware behind these devices to ensure data redundancy and optimize
performance for you. Persistent disks are available as either standard
hard disk drives (HDD) or solid-state drives (SSD).</p>
<p>Persistent disks are located independently from your virtual machine
instances, so you can detach or move persistent disks to keep your data
even after you delete your instances. Persistent disk performance scales
automatically with size, so you can resize your existing persistent disks
or add more persistent disks to an instance to meet your performance and
storage space requirements.</p>
<p>Add a persistent disk to your instance when you need reliable and
affordable storage with consistent performance characteristics.</p>
<p>To get more information about Disk, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/disks">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/disks/add-persistent-disk">Adding a persistent disk</a></li>
</ul>
</li>
</ul>
<blockquote>
<div><strong>Warning:</strong> All arguments including the disk encryption key will be stored in the raw
state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=disk_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] description
:param pulumi.Input[dict] disk_encryption_key
:param pulumi.Input[str] disk_encryption_key_raw
:param pulumi.Input[str] image
:param pulumi.Input[dict] labels
:param pulumi.Input[str] name
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[int] size
:param pulumi.Input[str] snapshot
:param pulumi.Input[dict] source_image_encryption_key
:param pulumi.Input[dict] source_snapshot_encryption_key
:param pulumi.Input[str] type
:param pulumi.Input[str] zone</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Disk.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Disk.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Disk.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Disk.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Disk.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Disk.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Disk.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Disk.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Firewall">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">Firewall</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allows=None</em>, <em>denies=None</em>, <em>description=None</em>, <em>destination_ranges=None</em>, <em>direction=None</em>, <em>disabled=None</em>, <em>enable_logging=None</em>, <em>name=None</em>, <em>network=None</em>, <em>priority=None</em>, <em>project=None</em>, <em>source_ranges=None</em>, <em>source_service_accounts=None</em>, <em>source_tags=None</em>, <em>target_service_accounts=None</em>, <em>target_tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Firewall" title="Permalink to this definition">¶</a></dt>
<dd><p>Each network has its own firewall controlling access to and from the
instances.</p>
<p>All traffic to instances, even from other instances, is blocked by the
firewall unless firewall rules are created to allow it.</p>
<p>The default network has automatically created firewall rules that are
shown in default firewall rules. No manually created network has
automatically created firewall rules except for a default “allow” rule for
outgoing traffic and a default “deny” for incoming traffic. For all
networks except the default network, you must create any firewall rules
you need.</p>
<p>To get more information about Firewall, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/firewalls">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/vpc/docs/firewalls">Official Documentation</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=firewall_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] allows
:param pulumi.Input[list] denies
:param pulumi.Input[str] description
:param pulumi.Input[list] destination_ranges
:param pulumi.Input[str] direction
:param pulumi.Input[bool] disabled
:param pulumi.Input[bool] enable_logging
:param pulumi.Input[str] name
:param pulumi.Input[str] network
:param pulumi.Input[int] priority
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[list] source_ranges
:param pulumi.Input[str] source_service_accounts
:param pulumi.Input[list] source_tags
:param pulumi.Input[str] target_service_accounts
:param pulumi.Input[list] target_tags</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Firewall.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Firewall.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Firewall.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Firewall.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Firewall.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Firewall.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Firewall.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Firewall.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ForwardingRule">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">ForwardingRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>backend_service=None</em>, <em>description=None</em>, <em>ip_address=None</em>, <em>ip_protocol=None</em>, <em>ip_version=None</em>, <em>labels=None</em>, <em>load_balancing_scheme=None</em>, <em>name=None</em>, <em>network=None</em>, <em>network_tier=None</em>, <em>port_range=None</em>, <em>ports=None</em>, <em>project=None</em>, <em>region=None</em>, <em>service_label=None</em>, <em>subnetwork=None</em>, <em>target=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ForwardingRule" title="Permalink to this definition">¶</a></dt>
<dd><p>A ForwardingRule resource. A ForwardingRule resource specifies which pool
of target virtual machines to forward a packet to if it matches the given
[IPAddress, IPProtocol, portRange] tuple.</p>
<p>To get more information about ForwardingRule, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/forwardingRule">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/network/forwarding-rules">Official Documentation</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=forwarding_rule_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] backend_service
:param pulumi.Input[str] description
:param pulumi.Input[str] ip_address
:param pulumi.Input[str] ip_protocol
:param pulumi.Input[str] ip_version
:param pulumi.Input[dict] labels
:param pulumi.Input[str] load_balancing_scheme
:param pulumi.Input[str] name
:param pulumi.Input[str] network
:param pulumi.Input[str] network_tier
:param pulumi.Input[str] port_range
:param pulumi.Input[list] ports
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[str] region
:param pulumi.Input[str] service_label
:param pulumi.Input[str] subnetwork
:param pulumi.Input[str] target</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.ForwardingRule.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ForwardingRule.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.ForwardingRule.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ForwardingRule.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.ForwardingRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ForwardingRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ForwardingRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ForwardingRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.GetAddressResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GetAddressResult</code><span class="sig-paren">(</span><em>address=None</em>, <em>project=None</em>, <em>region=None</em>, <em>self_link=None</em>, <em>status=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetAddressResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAddress.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetAddressResult.address">
<code class="descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetAddressResult.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetAddressResult.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetAddressResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetAddressResult.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetAddressResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates if the address is used. Possible values are: RESERVED or IN_USE.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetAddressResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetAddressResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetBackendServiceResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GetBackendServiceResult</code><span class="sig-paren">(</span><em>backends=None</em>, <em>cdn_policies=None</em>, <em>connection_draining_timeout_sec=None</em>, <em>custom_request_headers=None</em>, <em>description=None</em>, <em>enable_cdn=None</em>, <em>fingerprint=None</em>, <em>health_checks=None</em>, <em>iaps=None</em>, <em>port_name=None</em>, <em>protocol=None</em>, <em>region=None</em>, <em>security_policy=None</em>, <em>self_link=None</em>, <em>session_affinity=None</em>, <em>timeout_sec=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBackendService.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.backends">
<code class="descname">backends</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.backends" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of backends that serve this Backend Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.connection_draining_timeout_sec">
<code class="descname">connection_draining_timeout_sec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.connection_draining_timeout_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>Time for which instance will be drained (not accept new connections, but still work to finish started ones).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Textual description for the Backend Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.enable_cdn">
<code class="descname">enable_cdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.enable_cdn" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not Cloud CDN is enabled on the Backend Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the Backend Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.health_checks">
<code class="descname">health_checks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.health_checks" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of HTTP/HTTPS health checks used by the Backend Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.port_name">
<code class="descname">port_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.port_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a service that has been added to an instance group in this backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.protocol">
<code class="descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol for incoming requests.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the Backend Service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.session_affinity">
<code class="descname">session_affinity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.session_affinity" title="Permalink to this definition">¶</a></dt>
<dd><p>The Backend Service session stickyness configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.timeout_sec">
<code class="descname">timeout_sec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.timeout_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of seconds to wait for a backend to respond to a request before considering the request failed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetBackendServiceResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetBackendServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetDefaultServiceAccountResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GetDefaultServiceAccountResult</code><span class="sig-paren">(</span><em>email=None</em>, <em>project=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetDefaultServiceAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDefaultServiceAccount.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetDefaultServiceAccountResult.email">
<code class="descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetDefaultServiceAccountResult.email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email address of the default service account used by VMs running in this project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetDefaultServiceAccountResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetDefaultServiceAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GetForwardingRuleResult</code><span class="sig-paren">(</span><em>backend_service=None</em>, <em>description=None</em>, <em>ip_address=None</em>, <em>ip_protocol=None</em>, <em>load_balancing_scheme=None</em>, <em>network=None</em>, <em>port_range=None</em>, <em>ports=None</em>, <em>project=None</em>, <em>region=None</em>, <em>self_link=None</em>, <em>subnetwork=None</em>, <em>target=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getForwardingRule.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.backend_service">
<code class="descname">backend_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.backend_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Backend service, if this forwarding rule has one.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of this forwarding rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.ip_address">
<code class="descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address of this forwarding rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.ip_protocol">
<code class="descname">ip_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.ip_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>IP protocol of this forwarding rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.load_balancing_scheme">
<code class="descname">load_balancing_scheme</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.load_balancing_scheme" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of load balancing of this forwarding rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.network">
<code class="descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Network of this forwarding rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.port_range">
<code class="descname">port_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.port_range" title="Permalink to this definition">¶</a></dt>
<dd><p>Port range, if this forwarding rule has one.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.ports">
<code class="descname">ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.ports" title="Permalink to this definition">¶</a></dt>
<dd><p>List of ports to use for internal load balancing, if this forwarding rule has any.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Region of this forwarding rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.subnetwork">
<code class="descname">subnetwork</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>Subnetwork of this forwarding rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.target">
<code class="descname">target</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.target" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of the target pool, if this forwarding rule has one.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetForwardingRuleResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetForwardingRuleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetGlobalAddressResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GetGlobalAddressResult</code><span class="sig-paren">(</span><em>address=None</em>, <em>project=None</em>, <em>self_link=None</em>, <em>status=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetGlobalAddressResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGlobalAddress.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetGlobalAddressResult.address">
<code class="descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetGlobalAddressResult.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetGlobalAddressResult.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetGlobalAddressResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetGlobalAddressResult.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetGlobalAddressResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates if the address is used. Possible values are: RESERVED or IN_USE.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetGlobalAddressResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetGlobalAddressResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetImageResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GetImageResult</code><span class="sig-paren">(</span><em>archive_size_bytes=None</em>, <em>creation_timestamp=None</em>, <em>description=None</em>, <em>disk_size_gb=None</em>, <em>family=None</em>, <em>image_encryption_key_sha256=None</em>, <em>image_id=None</em>, <em>label_fingerprint=None</em>, <em>labels=None</em>, <em>licenses=None</em>, <em>name=None</em>, <em>project=None</em>, <em>self_link=None</em>, <em>source_disk=None</em>, <em>source_disk_encryption_key_sha256=None</em>, <em>source_disk_id=None</em>, <em>source_image_id=None</em>, <em>status=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getImage.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.archive_size_bytes">
<code class="descname">archive_size_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.archive_size_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the image tar.gz archive stored in Google Cloud Storage in bytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.creation_timestamp">
<code class="descname">creation_timestamp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.creation_timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation timestamp in RFC3339 text format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional description of this image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.disk_size_gb">
<code class="descname">disk_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the image when restored onto a persistent disk in gigabytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.family">
<code class="descname">family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The family name of the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.image_encryption_key_sha256">
<code class="descname">image_encryption_key_sha256</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.image_encryption_key_sha256" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://tools.ietf.org/html/rfc4648#section-4">RFC 4648 base64</a>
encoded SHA-256 hash of the <a class="reference external" href="https://cloud.google.com/compute/docs/disks/customer-supplied-encryption">customer-supplied encryption key</a>
that protects this image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.image_id">
<code class="descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.label_fingerprint">
<code class="descname">label_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.label_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>A fingerprint for the labels being applied to this image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.labels">
<code class="descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of labels applied to this image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.licenses">
<code class="descname">licenses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.licenses" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of applicable license URI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.source_disk">
<code class="descname">source_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.source_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the source disk used to create this image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.source_disk_encryption_key_sha256">
<code class="descname">source_disk_encryption_key_sha256</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.source_disk_encryption_key_sha256" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://tools.ietf.org/html/rfc4648#section-4">RFC 4648 base64</a>
encoded SHA-256 hash of the <a class="reference external" href="https://cloud.google.com/compute/docs/disks/customer-supplied-encryption">customer-supplied encryption key</a>
that protects this image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.source_disk_id">
<code class="descname">source_disk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.source_disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID value of the disk used to create this image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.source_image_id">
<code class="descname">source_image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.source_image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID value of the image used to create this image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the image. Possible values are <strong>FAILED</strong>, <strong>PENDING</strong>, or <strong>READY</strong>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetImageResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetInstanceGroupResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GetInstanceGroupResult</code><span class="sig-paren">(</span><em>description=None</em>, <em>instances=None</em>, <em>named_ports=None</em>, <em>network=None</em>, <em>project=None</em>, <em>self_link=None</em>, <em>size=None</em>, <em>zone=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstanceGroup.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceGroupResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceGroupResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Textual description of the instance group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceGroupResult.instances">
<code class="descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceGroupResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>List of instances in the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceGroupResult.named_ports">
<code class="descname">named_ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceGroupResult.named_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>List of named ports in the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceGroupResult.network">
<code class="descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceGroupResult.network" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the network the instance group is in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceGroupResult.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceGroupResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceGroupResult.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceGroupResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of instances in the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceGroupResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetInstanceResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GetInstanceResult</code><span class="sig-paren">(</span><em>allow_stopping_for_update=None</em>, <em>attached_disks=None</em>, <em>boot_disks=None</em>, <em>can_ip_forward=None</em>, <em>cpu_platform=None</em>, <em>create_timeout=None</em>, <em>deletion_protection=None</em>, <em>description=None</em>, <em>disks=None</em>, <em>guest_accelerators=None</em>, <em>instance_id=None</em>, <em>label_fingerprint=None</em>, <em>labels=None</em>, <em>machine_type=None</em>, <em>metadata=None</em>, <em>metadata_fingerprint=None</em>, <em>metadata_startup_script=None</em>, <em>min_cpu_platform=None</em>, <em>networks=None</em>, <em>network_interfaces=None</em>, <em>schedulings=None</em>, <em>scratch_disks=None</em>, <em>self_link=None</em>, <em>service_accounts=None</em>, <em>tags=None</em>, <em>tags_fingerprint=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstance.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.attached_disks">
<code class="descname">attached_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.attached_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>List of disks attached to the instance. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.boot_disks">
<code class="descname">boot_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.boot_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>The boot disk for the instance. Sructure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.can_ip_forward">
<code class="descname">can_ip_forward</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.can_ip_forward" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether sending and receiving of packets with non-matching source or destination IPs is allowed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.cpu_platform">
<code class="descname">cpu_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.cpu_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The CPU platform used by this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.deletion_protection">
<code class="descname">deletion_protection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.deletion_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether deletion protection is enabled on this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A brief description of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.guest_accelerators">
<code class="descname">guest_accelerators</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.guest_accelerators" title="Permalink to this definition">¶</a></dt>
<dd><p>List of the type and count of accelerator cards attached to the instance. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.instance_id">
<code class="descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The server-assigned unique identifier of this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.label_fingerprint">
<code class="descname">label_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.label_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique fingerprint of the labels.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.labels">
<code class="descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of key/value label pairs assigned to the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.machine_type">
<code class="descname">machine_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.machine_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The machine type to create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata key/value pairs made available within the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.metadata_fingerprint">
<code class="descname">metadata_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.metadata_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique fingerprint of the metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.min_cpu_platform">
<code class="descname">min_cpu_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.min_cpu_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum CPU platform specified for the VM instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.networks">
<code class="descname">networks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.networks" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or self_link of the network attached to this interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.network_interfaces">
<code class="descname">network_interfaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.network_interfaces" title="Permalink to this definition">¶</a></dt>
<dd><p>The networks attached to the instance. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.schedulings">
<code class="descname">schedulings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.schedulings" title="Permalink to this definition">¶</a></dt>
<dd><p>The scheduling strategy being used by the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.scratch_disks">
<code class="descname">scratch_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.scratch_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>The scratch disks attached to the instance. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.service_accounts">
<code class="descname">service_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.service_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>The service account to attach to the instance. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of tags attached to the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.tags_fingerprint">
<code class="descname">tags_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.tags_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique fingerprint of the tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetInstanceResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetInstanceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetLBIPRangesResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GetLBIPRangesResult</code><span class="sig-paren">(</span><em>http_ssl_tcp_internals=None</em>, <em>networks=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetLBIPRangesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLBIPRanges.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetLBIPRangesResult.http_ssl_tcp_internals">
<code class="descname">http_ssl_tcp_internals</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetLBIPRangesResult.http_ssl_tcp_internals" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP ranges used for health checks when <strong>HTTP(S), SSL proxy, TCP proxy, and Internal load balancing</strong> is used</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetLBIPRangesResult.networks">
<code class="descname">networks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetLBIPRangesResult.networks" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP ranges used for health checks when <strong>Network load balancing</strong> is used</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetLBIPRangesResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetLBIPRangesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetNetblockIPRangesResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GetNetblockIPRangesResult</code><span class="sig-paren">(</span><em>cidr_blocks=None</em>, <em>cidr_blocks_ipv4s=None</em>, <em>cidr_blocks_ipv6s=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetNetblockIPRangesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetblockIPRanges.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetblockIPRangesResult.cidr_blocks">
<code class="descname">cidr_blocks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetblockIPRangesResult.cidr_blocks" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve list of all CIDR blocks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetblockIPRangesResult.cidr_blocks_ipv4s">
<code class="descname">cidr_blocks_ipv4s</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetblockIPRangesResult.cidr_blocks_ipv4s" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve list of the IP4 CIDR blocks</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetblockIPRangesResult.cidr_blocks_ipv6s">
<code class="descname">cidr_blocks_ipv6s</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetblockIPRangesResult.cidr_blocks_ipv6s" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve list of the IP6 CIDR blocks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetblockIPRangesResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetblockIPRangesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetNetworkResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GetNetworkResult</code><span class="sig-paren">(</span><em>description=None</em>, <em>gateway_ipv4=None</em>, <em>self_link=None</em>, <em>subnetworks_self_links=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetwork.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetworkResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetworkResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of this network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetworkResult.gateway_ipv4">
<code class="descname">gateway_ipv4</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetworkResult.gateway_ipv4" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetworkResult.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetworkResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetworkResult.subnetworks_self_links">
<code class="descname">subnetworks_self_links</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetworkResult.subnetworks_self_links" title="Permalink to this definition">¶</a></dt>
<dd><p>the list of subnetworks which belong to the network</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetNetworkResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetNetworkResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetRegionInstanceGroupResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GetRegionInstanceGroupResult</code><span class="sig-paren">(</span><em>instances=None</em>, <em>name=None</em>, <em>project=None</em>, <em>region=None</em>, <em>self_link=None</em>, <em>size=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetRegionInstanceGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegionInstanceGroup.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetRegionInstanceGroupResult.instances">
<code class="descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetRegionInstanceGroupResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>List of instances in the group, as a list of resources, each containing:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetRegionInstanceGroupResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetRegionInstanceGroupResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>String port name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetRegionInstanceGroupResult.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetRegionInstanceGroupResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of instances in the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetRegionInstanceGroupResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetRegionInstanceGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetRegionsResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GetRegionsResult</code><span class="sig-paren">(</span><em>names=None</em>, <em>project=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetRegionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegions.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetRegionsResult.names">
<code class="descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetRegionsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of regions available in the given project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetRegionsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetRegionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GetSSLPolicyResult</code><span class="sig-paren">(</span><em>creation_timestamp=None</em>, <em>custom_features=None</em>, <em>description=None</em>, <em>enabled_features=None</em>, <em>fingerprint=None</em>, <em>min_tls_version=None</em>, <em>profile=None</em>, <em>self_link=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSSLPolicy.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult.custom_features">
<code class="descname">custom_features</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult.custom_features" title="Permalink to this definition">¶</a></dt>
<dd><p>If the <code class="docutils literal notranslate"><span class="pre">profile</span></code> is <code class="docutils literal notranslate"><span class="pre">CUSTOM</span></code>, these are the custom encryption
ciphers supported by the profile. If the <code class="docutils literal notranslate"><span class="pre">profile</span></code> is <em>not</em> <code class="docutils literal notranslate"><span class="pre">CUSTOM</span></code>, this
attribute will be empty.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of this SSL Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult.enabled_features">
<code class="descname">enabled_features</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult.enabled_features" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of enabled encryption ciphers as a result of the policy config</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>Fingerprint of this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult.min_tls_version">
<code class="descname">min_tls_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult.min_tls_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum supported TLS version of this policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult.profile">
<code class="descname">profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult.profile" title="Permalink to this definition">¶</a></dt>
<dd><p>The Google-curated or custom profile used by this policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSSLPolicyResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSSLPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetSubnetworkResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GetSubnetworkResult</code><span class="sig-paren">(</span><em>description=None</em>, <em>gateway_address=None</em>, <em>ip_cidr_range=None</em>, <em>network=None</em>, <em>private_ip_google_access=None</em>, <em>project=None</em>, <em>region=None</em>, <em>secondary_ip_ranges=None</em>, <em>self_link=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetSubnetworkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSubnetwork.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSubnetworkResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSubnetworkResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of this subnetwork.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSubnetworkResult.gateway_address">
<code class="descname">gateway_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSubnetworkResult.gateway_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSubnetworkResult.ip_cidr_range">
<code class="descname">ip_cidr_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSubnetworkResult.ip_cidr_range" title="Permalink to this definition">¶</a></dt>
<dd><p>The range of IP addresses belonging to this subnetwork
secondary range.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSubnetworkResult.network">
<code class="descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSubnetworkResult.network" title="Permalink to this definition">¶</a></dt>
<dd><p>The network name or resource link to the parent
network of this subnetwork.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSubnetworkResult.private_ip_google_access">
<code class="descname">private_ip_google_access</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSubnetworkResult.private_ip_google_access" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the VMs in this subnet
can access Google services without assigned external IP
addresses.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSubnetworkResult.secondary_ip_ranges">
<code class="descname">secondary_ip_ranges</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSubnetworkResult.secondary_ip_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of configurations for secondary IP ranges for
VM instances contained in this subnetwork. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSubnetworkResult.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSubnetworkResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetSubnetworkResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetSubnetworkResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetVPNGatewayResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GetVPNGatewayResult</code><span class="sig-paren">(</span><em>description=None</em>, <em>network=None</em>, <em>project=None</em>, <em>region=None</em>, <em>self_link=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetVPNGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVPNGateway.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetVPNGatewayResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetVPNGatewayResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of this VPN gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetVPNGatewayResult.network">
<code class="descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetVPNGatewayResult.network" title="Permalink to this definition">¶</a></dt>
<dd><p>The network of this VPN gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetVPNGatewayResult.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetVPNGatewayResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Region of this VPN gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetVPNGatewayResult.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetVPNGatewayResult.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetVPNGatewayResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetVPNGatewayResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GetZonesResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GetZonesResult</code><span class="sig-paren">(</span><em>names=None</em>, <em>project=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZones.</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GetZonesResult.names">
<code class="descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetZonesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of zones available in the given region</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GetZonesResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GetZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.compute.GlobalAddress">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GlobalAddress</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>address_type=None</em>, <em>description=None</em>, <em>ip_version=None</em>, <em>labels=None</em>, <em>name=None</em>, <em>network=None</em>, <em>prefix_length=None</em>, <em>project=None</em>, <em>purpose=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GlobalAddress" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a Global Address resource. Global addresses are used for
HTTP(S) load balancing.</p>
<p>To get more information about GlobalAddress, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/globalAddresses">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address">Reserving a Static External IP Address</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=global_address_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] address_type
:param pulumi.Input[str] description
:param pulumi.Input[str] ip_version
:param pulumi.Input[dict] labels
:param pulumi.Input[str] name
:param pulumi.Input[str] network
:param pulumi.Input[int] prefix_length
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[str] purpose</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GlobalAddress.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GlobalAddress.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GlobalAddress.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GlobalAddress.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.GlobalAddress.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GlobalAddress.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.GlobalAddress.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GlobalAddress.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.GlobalForwardingRule">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">GlobalForwardingRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>ip_address=None</em>, <em>ip_protocol=None</em>, <em>ip_version=None</em>, <em>labels=None</em>, <em>name=None</em>, <em>port_range=None</em>, <em>project=None</em>, <em>target=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Global Forwarding Rule within GCE. This binds an ip and port to a target HTTP(s) proxy. For more
information see <a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/http/global-forwarding-rules">the official
documentation</a> and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/globalForwardingRules">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Textual description field.</li>
<li><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The static IP. (if not set, an ephemeral IP is
used). This should be the literal IP address to be used, not the <code class="docutils literal notranslate"><span class="pre">self_link</span></code>
to a <code class="docutils literal notranslate"><span class="pre">google_compute_global_address</span></code> resource. (If using a <code class="docutils literal notranslate"><span class="pre">google_compute_global_address</span></code>
resource, use the <code class="docutils literal notranslate"><span class="pre">address</span></code> property instead of the <code class="docutils literal notranslate"><span class="pre">self_link</span></code> property.)</li>
<li><strong>ip_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP protocol to route, one of “TCP” “UDP” “AH”
“ESP” or “SCTP”. (default “TCP”).</li>
<li><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP Version that will be used by this resource’s address. One of <code class="docutils literal notranslate"><span class="pre">&quot;IPV4&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;IPV6&quot;</span></code>.
You cannot provide this and <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>.</li>
<li><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>A set of key/value label pairs to assign to the resource. This property is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta fields.</p>
</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.</li>
<li><strong>port_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A range e.g. “1024-2048” or a single port “1024”
(defaults to all ports!).
Some types of forwarding targets have constraints on the acceptable ports:</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of target HTTP or HTTPS proxy.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.GlobalForwardingRule.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Textual description field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GlobalForwardingRule.ip_address">
<code class="descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The static IP. (if not set, an ephemeral IP is
used). This should be the literal IP address to be used, not the <code class="docutils literal notranslate"><span class="pre">self_link</span></code>
to a <code class="docutils literal notranslate"><span class="pre">google_compute_global_address</span></code> resource. (If using a <code class="docutils literal notranslate"><span class="pre">google_compute_global_address</span></code>
resource, use the <code class="docutils literal notranslate"><span class="pre">address</span></code> property instead of the <code class="docutils literal notranslate"><span class="pre">self_link</span></code> property.)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GlobalForwardingRule.ip_protocol">
<code class="descname">ip_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.ip_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP protocol to route, one of “TCP” “UDP” “AH”
“ESP” or “SCTP”. (default “TCP”).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GlobalForwardingRule.ip_version">
<code class="descname">ip_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP Version that will be used by this resource’s address. One of <code class="docutils literal notranslate"><span class="pre">&quot;IPV4&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;IPV6&quot;</span></code>.
You cannot provide this and <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GlobalForwardingRule.label_fingerprint">
<code class="descname">label_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.label_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The current label fingerprint. This property is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GlobalForwardingRule.labels">
<code class="descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of key/value label pairs to assign to the resource. This property is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GlobalForwardingRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GlobalForwardingRule.port_range">
<code class="descname">port_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.port_range" title="Permalink to this definition">¶</a></dt>
<dd><p>A range e.g. “1024-2048” or a single port “1024”
(defaults to all ports!).
Some types of forwarding targets have constraints on the acceptable ports:</p>
<ul class="simple">
<li>Target HTTP proxy: 80, 8080</li>
<li>Target HTTPS proxy: 443</li>
<li>Target TCP proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222</li>
<li>Target SSL proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222</li>
<li>Target VPN gateway: 500, 4500</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GlobalForwardingRule.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GlobalForwardingRule.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.GlobalForwardingRule.target">
<code class="descname">target</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.target" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of target HTTP or HTTPS proxy.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.GlobalForwardingRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.GlobalForwardingRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.GlobalForwardingRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.HealthCheck">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">HealthCheck</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>check_interval_sec=None</em>, <em>description=None</em>, <em>healthy_threshold=None</em>, <em>http_health_check=None</em>, <em>https_health_check=None</em>, <em>name=None</em>, <em>project=None</em>, <em>ssl_health_check=None</em>, <em>tcp_health_check=None</em>, <em>timeout_sec=None</em>, <em>unhealthy_threshold=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HealthCheck" title="Permalink to this definition">¶</a></dt>
<dd><p>Health Checks determine whether instances are responsive and able to do work.
They are an important part of a comprehensive load balancing configuration,
as they enable monitoring instances behind load balancers.</p>
<p>Health Checks poll instances at a specified interval. Instances that
do not respond successfully to some number of probes in a row are marked
as unhealthy. No new connections are sent to unhealthy instances,
though existing connections will continue. The health check will
continue to poll unhealthy instances. If an instance later responds
successfully to some number of consecutive probes, it is marked
healthy again and can receive new connections.</p>
<p>To get more information about HealthCheck, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/latest/healthChecks">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/load-balancing/docs/health-checks">Official Documentation</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=health_check_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[int] check_interval_sec
:param pulumi.Input[str] description
:param pulumi.Input[int] healthy_threshold
:param pulumi.Input[dict] http_health_check
:param pulumi.Input[dict] https_health_check
:param pulumi.Input[str] name
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[dict] ssl_health_check
:param pulumi.Input[dict] tcp_health_check
:param pulumi.Input[int] timeout_sec
:param pulumi.Input[int] unhealthy_threshold</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.HealthCheck.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.HealthCheck.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.HealthCheck.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.HealthCheck.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.HealthCheck.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HealthCheck.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.HealthCheck.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HealthCheck.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.HttpHealthCheck">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">HttpHealthCheck</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>check_interval_sec=None</em>, <em>description=None</em>, <em>healthy_threshold=None</em>, <em>host=None</em>, <em>name=None</em>, <em>port=None</em>, <em>project=None</em>, <em>request_path=None</em>, <em>timeout_sec=None</em>, <em>unhealthy_threshold=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HttpHealthCheck" title="Permalink to this definition">¶</a></dt>
<dd><p>An HttpHealthCheck resource. This resource defines a template for how
individual VMs should be checked for health, via HTTP.</p>
<blockquote>
<div><strong>Note:</strong> google_compute_http_health_check is a legacy health check.
The newer <a class="reference external" href="https://www.terraform.io/docs/providers/google/r/compute_health_check.html">google_compute_health_check</a>
should be preferred for all uses except
<a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/network/">Network Load Balancers</a>
which still require the legacy version.</div></blockquote>
<p>To get more information about HttpHealthCheck, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/httpHealthChecks">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/health-checks#legacy_health_checks">Adding Health Checks</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=http_health_check_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[int] check_interval_sec
:param pulumi.Input[str] description
:param pulumi.Input[int] healthy_threshold
:param pulumi.Input[str] host
:param pulumi.Input[str] name
:param pulumi.Input[int] port
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[str] request_path
:param pulumi.Input[int] timeout_sec
:param pulumi.Input[int] unhealthy_threshold</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.HttpHealthCheck.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.HttpHealthCheck.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.HttpHealthCheck.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.HttpHealthCheck.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.HttpHealthCheck.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HttpHealthCheck.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.HttpHealthCheck.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HttpHealthCheck.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.HttpsHealthCheck">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">HttpsHealthCheck</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>check_interval_sec=None</em>, <em>description=None</em>, <em>healthy_threshold=None</em>, <em>host=None</em>, <em>name=None</em>, <em>port=None</em>, <em>project=None</em>, <em>request_path=None</em>, <em>timeout_sec=None</em>, <em>unhealthy_threshold=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HttpsHealthCheck" title="Permalink to this definition">¶</a></dt>
<dd><p>An HttpsHealthCheck resource. This resource defines a template for how
individual VMs should be checked for health, via HTTPS.</p>
<blockquote>
<div><strong>Note:</strong> google_compute_https_health_check is a legacy health check.
The newer <a class="reference external" href="https://www.terraform.io/docs/providers/google/r/compute_health_check.html">google_compute_health_check</a>
should be preferred for all uses except
<a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/network/">Network Load Balancers</a>
which still require the legacy version.</div></blockquote>
<p>To get more information about HttpsHealthCheck, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/httpsHealthChecks">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/health-checks#legacy_health_checks">Adding Health Checks</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=https_health_check_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[int] check_interval_sec
:param pulumi.Input[str] description
:param pulumi.Input[int] healthy_threshold
:param pulumi.Input[str] host
:param pulumi.Input[str] name
:param pulumi.Input[int] port
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[str] request_path
:param pulumi.Input[int] timeout_sec
:param pulumi.Input[int] unhealthy_threshold</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.HttpsHealthCheck.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.HttpsHealthCheck.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.HttpsHealthCheck.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.HttpsHealthCheck.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.HttpsHealthCheck.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HttpsHealthCheck.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.HttpsHealthCheck.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.HttpsHealthCheck.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Image">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">Image</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>create_timeout=None</em>, <em>description=None</em>, <em>family=None</em>, <em>labels=None</em>, <em>licenses=None</em>, <em>name=None</em>, <em>project=None</em>, <em>raw_disk=None</em>, <em>source_disk=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Image" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a bootable VM image resource for Google Compute Engine from an existing
tarball. For more information see <a class="reference external" href="https://cloud.google.com/compute/docs/images">the official documentation</a> and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/images">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>create_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Configurable timeout in minutes for creating images. Default is 4 minutes.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the image to be created</li>
<li><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the image family to which this image belongs.</li>
<li><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of key/value label pairs to assign to the image.</li>
<li><strong>licenses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of license URIs to apply to this image. Changing this
forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>raw_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The raw disk that will be used as the source of the image.
Changing this forces a new resource to be created. Structure is documented
below.</li>
<li><strong>source_disk</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of a disk that will be used as the source of the
image. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Image.create_timeout">
<code class="descname">create_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Image.create_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Configurable timeout in minutes for creating images. Default is 4 minutes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Image.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Image.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the image to be created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Image.family">
<code class="descname">family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Image.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the image family to which this image belongs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Image.label_fingerprint">
<code class="descname">label_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Image.label_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the assigned labels.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Image.labels">
<code class="descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Image.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of key/value label pairs to assign to the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Image.licenses">
<code class="descname">licenses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Image.licenses" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of license URIs to apply to this image. Changing this
forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Image.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Image.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Image.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Image.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Image.raw_disk">
<code class="descname">raw_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Image.raw_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>The raw disk that will be used as the source of the image.
Changing this forces a new resource to be created. Structure is documented
below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Image.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Image.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Image.source_disk">
<code class="descname">source_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Image.source_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of a disk that will be used as the source of the
image. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Image.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Image.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Image.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Image.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Instance">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">Instance</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allow_stopping_for_update=None</em>, <em>attached_disks=None</em>, <em>boot_disk=None</em>, <em>can_ip_forward=None</em>, <em>create_timeout=None</em>, <em>deletion_protection=None</em>, <em>description=None</em>, <em>guest_accelerators=None</em>, <em>labels=None</em>, <em>machine_type=None</em>, <em>metadata=None</em>, <em>metadata_startup_script=None</em>, <em>min_cpu_platform=None</em>, <em>name=None</em>, <em>network_interfaces=None</em>, <em>project=None</em>, <em>scheduling=None</em>, <em>scratch_disks=None</em>, <em>service_account=None</em>, <em>tags=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a VM instance resource within GCE. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/instances">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instances">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allow_stopping_for_update</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, allows Terraform to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.</li>
<li><strong>attached_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of disks to attach to the instance. Structure is documented below.</li>
<li><strong>boot_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The boot disk for the instance.
Structure is documented below.</li>
<li><strong>can_ip_forward</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.</li>
<li><strong>create_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Configurable timeout in minutes for creating instances. Default is 4 minutes.
Changing this forces a new resource to be created.</li>
<li><strong>deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable deletion protection on this instance. Defaults to false.
<strong>Note:</strong> you must disable deletion protection before removing the resource (e.g., via <code class="docutils literal notranslate"><span class="pre">terraform</span> <span class="pre">destroy</span></code>), or the instance cannot be deleted and the Terraform run will not complete successfully.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A brief description of this resource.</li>
<li><strong>guest_accelerators</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the type and count of accelerator cards attached to the instance. Structure documented below.
<strong>Note:</strong> GPU accelerators can only be used with <code class="docutils literal notranslate"><span class="pre">on_host_maintenance</span></code> option set to TERMINATE.</li>
<li><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of key/value label pairs to assign to the instance.</li>
<li><strong>machine_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The machine type to create.</li>
<li><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata key/value pairs to make available from
within the instance.</li>
<li><strong>metadata_startup_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.</li>
<li><strong>min_cpu_platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
<code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code> or <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Skylake</span></code>. See the complete list <a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">here</a>.
<strong>Note</strong>: <code class="docutils literal notranslate"><span class="pre">allow_stopping_for_update</span></code> must be set to true in order to update this field.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</li>
<li><strong>network_interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>scheduling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The scheduling strategy to use. More details about
this configuration option are detailed below.</li>
<li><strong>scratch_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.</li>
<li><strong>service_account</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Service account to attach to the instance.
Structure is documented below.
<strong>Note</strong>: <code class="docutils literal notranslate"><span class="pre">allow_stopping_for_update</span></code> must be set to true in order to update this field.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tags to attach to the instance.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone that the machine should be created in.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.allow_stopping_for_update">
<code class="descname">allow_stopping_for_update</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.allow_stopping_for_update" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, allows Terraform to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.attached_disks">
<code class="descname">attached_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.attached_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>List of disks to attach to the instance. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.boot_disk">
<code class="descname">boot_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.boot_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>The boot disk for the instance.
Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.can_ip_forward">
<code class="descname">can_ip_forward</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.can_ip_forward" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.cpu_platform">
<code class="descname">cpu_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.cpu_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The CPU platform used by this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.create_timeout">
<code class="descname">create_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.create_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Configurable timeout in minutes for creating instances. Default is 4 minutes.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.deletion_protection">
<code class="descname">deletion_protection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.deletion_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable deletion protection on this instance. Defaults to false.
<strong>Note:</strong> you must disable deletion protection before removing the resource (e.g., via <code class="docutils literal notranslate"><span class="pre">terraform</span> <span class="pre">destroy</span></code>), or the instance cannot be deleted and the Terraform run will not complete successfully.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A brief description of this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.guest_accelerators">
<code class="descname">guest_accelerators</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.guest_accelerators" title="Permalink to this definition">¶</a></dt>
<dd><p>List of the type and count of accelerator cards attached to the instance. Structure documented below.
<strong>Note:</strong> GPU accelerators can only be used with <code class="docutils literal notranslate"><span class="pre">on_host_maintenance</span></code> option set to TERMINATE.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.instance_id">
<code class="descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The server-assigned unique identifier of this instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.label_fingerprint">
<code class="descname">label_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.label_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique fingerprint of the labels.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.labels">
<code class="descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of key/value label pairs to assign to the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.machine_type">
<code class="descname">machine_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.machine_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The machine type to create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata key/value pairs to make available from
within the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.metadata_fingerprint">
<code class="descname">metadata_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.metadata_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique fingerprint of the metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.metadata_startup_script">
<code class="descname">metadata_startup_script</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.metadata_startup_script" title="Permalink to this definition">¶</a></dt>
<dd><p>An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.min_cpu_platform">
<code class="descname">min_cpu_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.min_cpu_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
<code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code> or <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Skylake</span></code>. See the complete list <a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">here</a>.
<strong>Note</strong>: <code class="docutils literal notranslate"><span class="pre">allow_stopping_for_update</span></code> must be set to true in order to update this field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.network_interfaces">
<code class="descname">network_interfaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.network_interfaces" title="Permalink to this definition">¶</a></dt>
<dd><p>Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.scheduling">
<code class="descname">scheduling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.scheduling" title="Permalink to this definition">¶</a></dt>
<dd><p>The scheduling strategy to use. More details about
this configuration option are detailed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.scratch_disks">
<code class="descname">scratch_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.scratch_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.service_account">
<code class="descname">service_account</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.service_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Service account to attach to the instance.
Structure is documented below.
<strong>Note</strong>: <code class="docutils literal notranslate"><span class="pre">allow_stopping_for_update</span></code> must be set to true in order to update this field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to attach to the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.tags_fingerprint">
<code class="descname">tags_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.tags_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique fingerprint of the tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Instance.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Instance.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone that the machine should be created in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Instance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Instance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceFromTemplate">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">InstanceFromTemplate</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allow_stopping_for_update=None</em>, <em>attached_disks=None</em>, <em>boot_disk=None</em>, <em>can_ip_forward=None</em>, <em>deletion_protection=None</em>, <em>description=None</em>, <em>guest_accelerators=None</em>, <em>labels=None</em>, <em>machine_type=None</em>, <em>metadata=None</em>, <em>metadata_startup_script=None</em>, <em>min_cpu_platform=None</em>, <em>name=None</em>, <em>network_interfaces=None</em>, <em>project=None</em>, <em>scheduling=None</em>, <em>scratch_disks=None</em>, <em>service_account=None</em>, <em>source_instance_template=None</em>, <em>tags=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceFromTemplate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a VM instance resource within GCE. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/instances">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instances">API</a>.</p>
<p>This resource is specifically to create a compute instance from a given
<code class="docutils literal notranslate"><span class="pre">source_instance_template</span></code>. To create an instance without a template, use the
<code class="docutils literal notranslate"><span class="pre">google_compute_instance</span></code> resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[bool] allow_stopping_for_update
:param pulumi.Input[list] attached_disks
:param pulumi.Input[dict] boot_disk
:param pulumi.Input[bool] can_ip_forward
:param pulumi.Input[bool] deletion_protection
:param pulumi.Input[str] description
:param pulumi.Input[list] guest_accelerators
:param pulumi.Input[dict] labels
:param pulumi.Input[str] machine_type
:param pulumi.Input[dict] metadata
:param pulumi.Input[str] metadata_startup_script
:param pulumi.Input[str] min_cpu_platform
:param pulumi.Input[str] name: A unique name for the resource, required by GCE.</p>
<blockquote>
<div>Changing this forces a new resource to be created.</div></blockquote>
<p>:param pulumi.Input[list] network_interfaces
:param pulumi.Input[str] project
:param pulumi.Input[dict] scheduling
:param pulumi.Input[list] scratch_disks
:param pulumi.Input[dict] service_account
:param pulumi.Input[str] source_instance_template: Name or self link of an instance</p>
<blockquote>
<div>template to create the instance based on.</div></blockquote>
<p>:param pulumi.Input[list] tags
:param pulumi.Input[str] zone: The zone that the machine should be created in. If not</p>
<blockquote>
<div>set, the provider zone is used.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceFromTemplate.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceFromTemplate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceFromTemplate.source_instance_template">
<code class="descname">source_instance_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceFromTemplate.source_instance_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Name or self link of an instance
template to create the instance based on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceFromTemplate.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceFromTemplate.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone that the machine should be created in. If not
set, the provider zone is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceFromTemplate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceFromTemplate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceFromTemplate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceFromTemplate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceGroup">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">InstanceGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>instances=None</em>, <em>name=None</em>, <em>named_ports=None</em>, <em>network=None</em>, <em>project=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a group of dissimilar Compute Engine virtual machine instances.
For more information, see <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/#unmanaged_instance_groups">the official documentation</a>
and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instanceGroups">API</a></p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional textual description of the instance
group.</li>
<li><strong>instances</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of instances in the group. They should be given
as self_link URLs. When adding instances they must all be in the same
network and zone as the instance group.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance group. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</li>
<li><strong>named_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The named port configuration. See the section below
for details on configuration.</li>
<li><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the network the instance group is in. If
this is different from the network where the instances are in, the creation
fails. Defaults to the network where the instances are in (if neither
<code class="docutils literal notranslate"><span class="pre">network</span></code> nor <code class="docutils literal notranslate"><span class="pre">instances</span></code> is specified, this field will be blank).</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone that this instance group should be created in.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional textual description of the instance
group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.instances">
<code class="descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>List of instances in the group. They should be given
as self_link URLs. When adding instances they must all be in the same
network and zone as the instance group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance group. Must be 1-63
characters long and comply with
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a>. Supported characters
include lowercase letters, numbers, and hyphens.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.named_ports">
<code class="descname">named_ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.named_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>The named port configuration. See the section below
for details on configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.network">
<code class="descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.network" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the network the instance group is in. If
this is different from the network where the instances are in, the creation
fails. Defaults to the network where the instances are in (if neither
<code class="docutils literal notranslate"><span class="pre">network</span></code> nor <code class="docutils literal notranslate"><span class="pre">instances</span></code> is specified, this field will be blank).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of instances in the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroup.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone that this instance group should be created in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceGroupManager">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">InstanceGroupManager</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>auto_healing_policies=None</em>, <em>base_instance_name=None</em>, <em>description=None</em>, <em>instance_template=None</em>, <em>name=None</em>, <em>named_ports=None</em>, <em>project=None</em>, <em>rolling_update_policy=None</em>, <em>target_pools=None</em>, <em>target_size=None</em>, <em>update_strategy=None</em>, <em>versions=None</em>, <em>wait_for_instances=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager" title="Permalink to this definition">¶</a></dt>
<dd><p>The Google Compute Engine Instance Group Manager API creates and manages pools
of homogeneous Compute Engine virtual machine instances from a common instance
template. For more information, see <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/manager">the official documentation</a>
and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instanceGroupManagers">API</a></p>
<blockquote>
<div><strong>Note:</strong> Use <a class="reference external" href="https://www.terraform.io/docs/providers/google/r/compute_region_instance_group_manager.html">google_compute_region_instance_group_manager</a> to create a regional (multi-zone) instance group manager.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>auto_healing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>The autohealing policies for this managed instance
group. You can specify only one value. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups">official documentation</a>.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta fields.</p>
</li>
<li><strong>base_instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The base instance name to use for
instances in this group. The value must be a valid
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a> name. Supported characters
are lowercase letters, numbers, and hyphens (-). Instances are named by
appending a hyphen and a random four-character string to the base instance
name.</p>
</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional textual description of the instance
group manager.</li>
<li><strong>instance_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li>The full URL to an instance template from which all new instances of this version will be created.</li>
</ul>
</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li>Version name.</li>
</ul>
</li>
<li><strong>named_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The named port configuration. See the section below
for details on configuration.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>rolling_update_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>The update policy for this managed instance group. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups">official documentation</a> and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagers/patch">API</a>
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta fields.</p>
</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>target_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The full URL of all target pools to which new
instances in the group are added. Updating the target pools attribute does
not affect existing instances.</li>
<li><strong>target_size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – <ul>
<li>The number of instances calculated as a fixed number or a percentage depending on the settings. Structure is documented below.</li>
</ul>
</li>
<li><strong>update_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If the <code class="docutils literal notranslate"><span class="pre">instance_template</span></code>
resource is modified, a value of <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> will prevent any of the managed
instances from being restarted by Terraform. A value of <code class="docutils literal notranslate"><span class="pre">&quot;REPLACE&quot;</span></code> will
restart all of the instances at once. <code class="docutils literal notranslate"><span class="pre">&quot;ROLLING_UPDATE&quot;</span></code> is supported as a beta feature.
A value of <code class="docutils literal notranslate"><span class="pre">&quot;ROLLING_UPDATE&quot;</span></code> requires <code class="docutils literal notranslate"><span class="pre">rolling_update_policy</span></code> block to be set</li>
<li><strong>versions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Application versions managed by this instance group. Each
version deals with a specific instance template, allowing canary release scenarios.
Conflicts with <code class="docutils literal notranslate"><span class="pre">instance_template</span></code>. Structure is documented below. Beware that
exactly one version must not specify a target size. It means that versions with
a target size will respect the setting, and the one without target size will
be applied to all remaining Instances (top level target_size - each version target_size).
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta fields.</p>
</li>
<li><strong>wait_for_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, Terraform will
continue trying until it times out.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone that instances in this group should be created
in.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.auto_healing_policies">
<code class="descname">auto_healing_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.auto_healing_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>The autohealing policies for this managed instance
group. You can specify only one value. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups">official documentation</a>.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.base_instance_name">
<code class="descname">base_instance_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.base_instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The base instance name to use for
instances in this group. The value must be a valid
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a> name. Supported characters
are lowercase letters, numbers, and hyphens (-). Instances are named by
appending a hyphen and a random four-character string to the base instance
name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.description" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional textual description of the instance
group manager.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the instance group manager.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.instance_group">
<code class="descname">instance_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.instance_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The full URL of the instance group created by the manager.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.instance_template">
<code class="descname">instance_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.instance_template" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li>The full URL to an instance template from which all new instances of this version will be created.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.name" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li>Version name.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.named_ports">
<code class="descname">named_ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.named_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>The named port configuration. See the section below
for details on configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.rolling_update_policy">
<code class="descname">rolling_update_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.rolling_update_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The update policy for this managed instance group. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups">official documentation</a> and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagers/patch">API</a>
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.target_pools">
<code class="descname">target_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.target_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>The full URL of all target pools to which new
instances in the group are added. Updating the target pools attribute does
not affect existing instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.target_size">
<code class="descname">target_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.target_size" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li>The number of instances calculated as a fixed number or a percentage depending on the settings. Structure is documented below.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.update_strategy">
<code class="descname">update_strategy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.update_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>If the <code class="docutils literal notranslate"><span class="pre">instance_template</span></code>
resource is modified, a value of <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> will prevent any of the managed
instances from being restarted by Terraform. A value of <code class="docutils literal notranslate"><span class="pre">&quot;REPLACE&quot;</span></code> will
restart all of the instances at once. <code class="docutils literal notranslate"><span class="pre">&quot;ROLLING_UPDATE&quot;</span></code> is supported as a beta feature.
A value of <code class="docutils literal notranslate"><span class="pre">&quot;ROLLING_UPDATE&quot;</span></code> requires <code class="docutils literal notranslate"><span class="pre">rolling_update_policy</span></code> block to be set</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.versions">
<code class="descname">versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.versions" title="Permalink to this definition">¶</a></dt>
<dd><p>Application versions managed by this instance group. Each
version deals with a specific instance template, allowing canary release scenarios.
Conflicts with <code class="docutils literal notranslate"><span class="pre">instance_template</span></code>. Structure is documented below. Beware that
exactly one version must not specify a target size. It means that versions with
a target size will respect the setting, and the one without target size will
be applied to all remaining Instances (top level target_size - each version target_size).
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.wait_for_instances">
<code class="descname">wait_for_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.wait_for_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, Terraform will
continue trying until it times out.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceGroupManager.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone that instances in this group should be created
in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceGroupManager.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceGroupManager.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceGroupManager.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceTemplate">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">InstanceTemplate</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>can_ip_forward=None</em>, <em>description=None</em>, <em>disks=None</em>, <em>guest_accelerators=None</em>, <em>instance_description=None</em>, <em>labels=None</em>, <em>machine_type=None</em>, <em>metadata=None</em>, <em>metadata_startup_script=None</em>, <em>min_cpu_platform=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>network_interfaces=None</em>, <em>project=None</em>, <em>region=None</em>, <em>schedulings=None</em>, <em>service_account=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a VM instance template resource within GCE. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/instance-templates">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instanceTemplates">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>can_ip_forward</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A brief description of this resource.</li>
<li><strong>disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.</li>
<li><strong>guest_accelerators</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the type and count of accelerator cards attached to the instance. Structure documented below.</li>
<li><strong>instance_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A brief description to use for instances
created from this template.</li>
<li><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of key/value label pairs to assign to instances
created from this template,</li>
<li><strong>machine_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The machine type to create.</li>
<li><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata key/value pairs to make available from
within instances created from this template.</li>
<li><strong>metadata_startup_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An alternative to using the
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.</li>
<li><strong>min_cpu_platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
<code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code> or <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Skylake</span></code>. See the complete list <a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">here</a>.</p>
</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance template. If you leave
this blank, Terraform will auto-generate a unique name.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>network_interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom <code class="docutils literal notranslate"><span class="pre">subnetwork</span></code>
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.</li>
<li><strong>schedulings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The scheduling strategy to use. More details about
this configuration option are detailed below.</li>
<li><strong>service_account</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Service account to attach to the instance. Structure is documented below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Tags to attach to the instance.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.can_ip_forward">
<code class="descname">can_ip_forward</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.can_ip_forward" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A brief description of this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.disks">
<code class="descname">disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.disks" title="Permalink to this definition">¶</a></dt>
<dd><p>Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.guest_accelerators">
<code class="descname">guest_accelerators</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.guest_accelerators" title="Permalink to this definition">¶</a></dt>
<dd><p>List of the type and count of accelerator cards attached to the instance. Structure documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.instance_description">
<code class="descname">instance_description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.instance_description" title="Permalink to this definition">¶</a></dt>
<dd><p>A brief description to use for instances
created from this template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.labels">
<code class="descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of key/value label pairs to assign to instances
created from this template,</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.machine_type">
<code class="descname">machine_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.machine_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The machine type to create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata key/value pairs to make available from
within instances created from this template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.metadata_fingerprint">
<code class="descname">metadata_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.metadata_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique fingerprint of the metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.metadata_startup_script">
<code class="descname">metadata_startup_script</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.metadata_startup_script" title="Permalink to this definition">¶</a></dt>
<dd><p>An alternative to using the
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.min_cpu_platform">
<code class="descname">min_cpu_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.min_cpu_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
<code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code> or <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Skylake</span></code>. See the complete list <a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">here</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance template. If you leave
this blank, Terraform will auto-generate a unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.network_interfaces">
<code class="descname">network_interfaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.network_interfaces" title="Permalink to this definition">¶</a></dt>
<dd><p>Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.region" title="Permalink to this definition">¶</a></dt>
<dd><p>An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom <code class="docutils literal notranslate"><span class="pre">subnetwork</span></code>
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.schedulings">
<code class="descname">schedulings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.schedulings" title="Permalink to this definition">¶</a></dt>
<dd><p>The scheduling strategy to use. More details about
this configuration option are detailed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.service_account">
<code class="descname">service_account</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.service_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Service account to attach to the instance. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags to attach to the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InstanceTemplate.tags_fingerprint">
<code class="descname">tags_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.tags_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique fingerprint of the tags.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InstanceTemplate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InstanceTemplate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InstanceTemplate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InterconnectAttachment">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">InterconnectAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>interconnect=None</em>, <em>name=None</em>, <em>project=None</em>, <em>region=None</em>, <em>router=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InterconnectAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents an InterconnectAttachment (VLAN attachment) resource. For more
information, see Creating VLAN Attachments.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] description
:param pulumi.Input[str] interconnect
:param pulumi.Input[str] name
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[str] region
:param pulumi.Input[str] router</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.InterconnectAttachment.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InterconnectAttachment.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.InterconnectAttachment.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.InterconnectAttachment.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.InterconnectAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InterconnectAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.InterconnectAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.InterconnectAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Network">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">Network</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>auto_create_subnetworks=None</em>, <em>description=None</em>, <em>ipv4_range=None</em>, <em>name=None</em>, <em>project=None</em>, <em>routing_mode=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Network" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a network within GCE. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/vpc">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/networks">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>auto_create_subnetworks</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true, this network will be
created in auto subnet mode, and Google will create a subnet for each region
automatically. If set to false, a custom subnetted network will be created that
can support <code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork</span></code> resources. Defaults to true.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A brief description of this resource.</li>
<li><strong>ipv4_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set to a CIDR block, uses the legacy VPC API with the
specified range. This API is deprecated. If set, <code class="docutils literal notranslate"><span class="pre">auto_create_subnetworks</span></code> must be
explicitly set to false.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>routing_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the network-wide routing mode for Cloud Routers
to use. Accepted values are <code class="docutils literal notranslate"><span class="pre">&quot;GLOBAL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;REGIONAL&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;REGIONAL&quot;</span></code>.
Refer to the <a class="reference external" href="https://cloud.google.com/router/docs/concepts/overview#dynamic-routing-mode">Cloud Router documentation</a>
for more details.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Network.auto_create_subnetworks">
<code class="descname">auto_create_subnetworks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Network.auto_create_subnetworks" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to true, this network will be
created in auto subnet mode, and Google will create a subnet for each region
automatically. If set to false, a custom subnetted network will be created that
can support <code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork</span></code> resources. Defaults to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Network.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Network.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A brief description of this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Network.gateway_ipv4">
<code class="descname">gateway_ipv4</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Network.gateway_ipv4" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 address of the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Network.ipv4_range">
<code class="descname">ipv4_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Network.ipv4_range" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to a CIDR block, uses the legacy VPC API with the
specified range. This API is deprecated. If set, <code class="docutils literal notranslate"><span class="pre">auto_create_subnetworks</span></code> must be
explicitly set to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Network.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Network.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Network.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Network.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Network.routing_mode">
<code class="descname">routing_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Network.routing_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the network-wide routing mode for Cloud Routers
to use. Accepted values are <code class="docutils literal notranslate"><span class="pre">&quot;GLOBAL&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;REGIONAL&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;REGIONAL&quot;</span></code>.
Refer to the <a class="reference external" href="https://cloud.google.com/router/docs/concepts/overview#dynamic-routing-mode">Cloud Router documentation</a>
for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Network.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Network.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Network.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Network.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Network.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Network.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.NetworkPeering">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">NetworkPeering</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>auto_create_routes=None</em>, <em>name=None</em>, <em>network=None</em>, <em>peer_network=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a network peering within GCE. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/vpc/vpc-peering">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/networks">API</a>.</p>
<blockquote>
<div><p><strong>Note:</strong> Both network must create a peering with each other for the peering to be functional.</p>
<p><strong>Note:</strong> Subnets IP ranges across peered VPC networks cannot overlap.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>auto_create_routes</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the routes between the two networks will
be created and managed automatically. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the peering.</li>
<li><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource link of the network to add a peering to.</li>
<li><strong>peer_network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource link of the peer network.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.NetworkPeering.auto_create_routes">
<code class="descname">auto_create_routes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering.auto_create_routes" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the routes between the two networks will
be created and managed automatically. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.NetworkPeering.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the peering.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.NetworkPeering.network">
<code class="descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource link of the network to add a peering to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.NetworkPeering.peer_network">
<code class="descname">peer_network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering.peer_network" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource link of the peer network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.NetworkPeering.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering.state" title="Permalink to this definition">¶</a></dt>
<dd><p>State for the peering.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.NetworkPeering.state_details">
<code class="descname">state_details</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering.state_details" title="Permalink to this definition">¶</a></dt>
<dd><p>Details about the current state of the peering.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.NetworkPeering.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.NetworkPeering.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.NetworkPeering.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ProjectMetadata">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">ProjectMetadata</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>metadata=None</em>, <em>project=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages metadata common to all instances for a project in GCE. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/storing-retrieving-metadata">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/projects/setCommonInstanceMetadata">API</a>.</p>
<blockquote>
<div><strong>Note:</strong>  If you want to manage only single key/value pairs within the project metadata
rather than the entire set, then use
google_compute_project_metadata_item.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A series of key value pairs. Changing this resource
updates the GCE state.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.ProjectMetadata.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadata.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of key value pairs. Changing this resource
updates the GCE state.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.ProjectMetadata.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadata.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.ProjectMetadata.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadata.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ProjectMetadata.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadata.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ProjectMetadataItem">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">ProjectMetadataItem</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>key=None</em>, <em>project=None</em>, <em>value=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadataItem" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a single key/value pair on metadata common to all instances for
a project in GCE. Using <code class="docutils literal notranslate"><span class="pre">google_compute_project_metadata_item</span></code> lets you
manage a single key/value setting in Terraform rather than the entire
project metadata map.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metadata key to set.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to set for the given metadata key.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.ProjectMetadataItem.key">
<code class="descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadataItem.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The metadata key to set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.ProjectMetadataItem.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadataItem.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.ProjectMetadataItem.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadataItem.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value to set for the given metadata key.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.ProjectMetadataItem.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadataItem.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.ProjectMetadataItem.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.ProjectMetadataItem.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RegionAutoscaler">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">RegionAutoscaler</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>autoscaling_policy=None</em>, <em>description=None</em>, <em>name=None</em>, <em>project=None</em>, <em>region=None</em>, <em>target=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionAutoscaler" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents an Autoscaler resource.</p>
<p>Autoscalers allow you to automatically scale virtual machine instances in
managed instance groups according to an autoscaling policy that you
define.</p>
<p>To get more information about RegionAutoscaler, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/autoscaler/">Autoscaling Groups of Instances</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=region_autoscaler_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[dict] autoscaling_policy
:param pulumi.Input[str] description
:param pulumi.Input[str] name
:param pulumi.Input[str] project
:param pulumi.Input[str] region
:param pulumi.Input[str] target</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionAutoscaler.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionAutoscaler.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RegionAutoscaler.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionAutoscaler.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RegionAutoscaler.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionAutoscaler.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RegionBackendService">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">RegionBackendService</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>backends=None</em>, <em>connection_draining_timeout_sec=None</em>, <em>description=None</em>, <em>health_checks=None</em>, <em>name=None</em>, <em>project=None</em>, <em>protocol=None</em>, <em>region=None</em>, <em>session_affinity=None</em>, <em>timeout_sec=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService" title="Permalink to this definition">¶</a></dt>
<dd><p>A Region Backend Service defines a regionally-scoped group of virtual machines that will serve traffic for load balancing.
For more information see <a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/internal/">the official documentation</a>
and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/regionBackendServices">API</a>.</p>
<blockquote>
<div><dl class="docutils">
<dt><strong>Note</strong>\ <span class="classifier-delimiter">:</span> <span class="classifier">Region backend services can only be used when using internal load balancing. For external load balancing, use</span></dt>
<dd><code class="docutils literal notranslate"><span class="pre">google_compute_backend_service</span></code> instead.</dd>
</dl>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>backends</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of backends that serve this BackendService.
Structure is documented below.</li>
<li><strong>connection_draining_timeout_sec</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Time for which instance will be drained
(not accept new connections, but still work to finish started ones). Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The textual description for the backend service.</li>
<li><strong>health_checks</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a list of health checks
for checking the health of the backend service. Currently at most
one health check can be specified, and a health check is required.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the backend service.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol for incoming requests. Defaults to
<code class="docutils literal notranslate"><span class="pre">TCP</span></code>.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Region in which the created address should reside.
If it is not provided, the provider region is used.</li>
<li><strong>session_affinity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How to distribute load. Options are <code class="docutils literal notranslate"><span class="pre">NONE</span></code> (no
affinity), <code class="docutils literal notranslate"><span class="pre">CLIENT_IP</span></code>, <code class="docutils literal notranslate"><span class="pre">CLIENT_IP_PROTO</span></code>, or <code class="docutils literal notranslate"><span class="pre">CLIENT_IP_PORT_PROTO</span></code>.
Defaults to <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</li>
<li><strong>timeout_sec</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of secs to wait for a backend to respond
to a request before considering the request failed. Defaults to <code class="docutils literal notranslate"><span class="pre">30</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionBackendService.backends">
<code class="descname">backends</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.backends" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of backends that serve this BackendService.
Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionBackendService.connection_draining_timeout_sec">
<code class="descname">connection_draining_timeout_sec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.connection_draining_timeout_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>Time for which instance will be drained
(not accept new connections, but still work to finish started ones). Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionBackendService.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The textual description for the backend service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionBackendService.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the backend service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionBackendService.health_checks">
<code class="descname">health_checks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.health_checks" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a list of health checks
for checking the health of the backend service. Currently at most
one health check can be specified, and a health check is required.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionBackendService.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the backend service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionBackendService.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionBackendService.protocol">
<code class="descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol for incoming requests. Defaults to
<code class="docutils literal notranslate"><span class="pre">TCP</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionBackendService.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The Region in which the created address should reside.
If it is not provided, the provider region is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionBackendService.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionBackendService.session_affinity">
<code class="descname">session_affinity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.session_affinity" title="Permalink to this definition">¶</a></dt>
<dd><p>How to distribute load. Options are <code class="docutils literal notranslate"><span class="pre">NONE</span></code> (no
affinity), <code class="docutils literal notranslate"><span class="pre">CLIENT_IP</span></code>, <code class="docutils literal notranslate"><span class="pre">CLIENT_IP_PROTO</span></code>, or <code class="docutils literal notranslate"><span class="pre">CLIENT_IP_PORT_PROTO</span></code>.
Defaults to <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionBackendService.timeout_sec">
<code class="descname">timeout_sec</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.timeout_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of secs to wait for a backend to respond
to a request before considering the request failed. Defaults to <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RegionBackendService.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RegionBackendService.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionBackendService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RegionDisk">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">RegionDisk</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>disk_encryption_key=None</em>, <em>labels=None</em>, <em>name=None</em>, <em>project=None</em>, <em>region=None</em>, <em>replica_zones=None</em>, <em>size=None</em>, <em>snapshot=None</em>, <em>source_snapshot_encryption_key=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionDisk" title="Permalink to this definition">¶</a></dt>
<dd><p>Persistent disks are durable storage devices that function similarly to
the physical disks in a desktop or a server. Compute Engine manages the
hardware behind these devices to ensure data redundancy and optimize
performance for you. Persistent disks are available as either standard
hard disk drives (HDD) or solid-state drives (SSD).</p>
<p>Persistent disks are located independently from your virtual machine
instances, so you can detach or move persistent disks to keep your data
even after you delete your instances. Persistent disk performance scales
automatically with size, so you can resize your existing persistent disks
or add more persistent disks to an instance to meet your performance and
storage space requirements.</p>
<p>Add a persistent disk to your instance when you need reliable and
affordable storage with consistent performance characteristics.</p>
<p>To get more information about RegionDisk, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/regionDisks">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/disks/regional-persistent-disk">Adding or Resizing Regional Persistent Disks</a></li>
</ul>
</li>
</ul>
<blockquote>
<div><strong>Warning:</strong> All arguments including the disk encryption key will be stored in the raw
state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=region_disk_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] description
:param pulumi.Input[dict] disk_encryption_key
:param pulumi.Input[dict] labels
:param pulumi.Input[str] name
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[str] region
:param pulumi.Input[list] replica_zones
:param pulumi.Input[int] size
:param pulumi.Input[str] snapshot
:param pulumi.Input[dict] source_snapshot_encryption_key
:param pulumi.Input[str] type</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionDisk.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionDisk.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionDisk.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionDisk.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RegionDisk.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionDisk.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RegionDisk.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionDisk.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">RegionInstanceGroupManager</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>auto_healing_policies=None</em>, <em>base_instance_name=None</em>, <em>description=None</em>, <em>distribution_policy_zones=None</em>, <em>instance_template=None</em>, <em>name=None</em>, <em>named_ports=None</em>, <em>project=None</em>, <em>region=None</em>, <em>rolling_update_policy=None</em>, <em>target_pools=None</em>, <em>target_size=None</em>, <em>update_strategy=None</em>, <em>versions=None</em>, <em>wait_for_instances=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager" title="Permalink to this definition">¶</a></dt>
<dd><p>The Google Compute Engine Regional Instance Group Manager API creates and manages pools
of homogeneous Compute Engine virtual machine instances from a common instance
template. For more information, see <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups">the official documentation</a>
and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/regionInstanceGroupManagers">API</a></p>
<blockquote>
<div><strong>Note:</strong> Use <a class="reference external" href="https://www.terraform.io/docs/providers/google/r/compute_instance_group_manager.html">google_compute_instance_group_manager</a> to create a single-zone instance group manager.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>auto_healing_policies</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>The autohealing policies for this managed instance
group. You can specify only one value. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups">official documentation</a>.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta fields.</p>
</li>
<li><strong>base_instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The base instance name to use for
instances in this group. The value must be a valid
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a> name. Supported characters
are lowercase letters, numbers, and hyphens (-). Instances are named by
appending a hyphen and a random four-character string to the base instance
name.</p>
</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional textual description of the instance
group manager.</li>
<li><strong>distribution_policy_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>The distribution policy for this managed instance
group. You can specify one or more values. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selectingzones">official documentation</a>.</p>
</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>instance_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li>The full URL to an instance template from which all new instances of this version will be created.</li>
</ul>
</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li>Version name.</li>
</ul>
</li>
<li><strong>named_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The named port configuration. See the section below
for details on configuration.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where the managed instance group resides.</li>
<li><strong>rolling_update_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>The update policy for this managed instance group. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups">official documentation</a> and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patch">API</a>
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta fields.</p>
</li>
<li><strong>target_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The full URL of all target pools to which new
instances in the group are added. Updating the target pools attribute does
not affect existing instances.</li>
<li><strong>target_size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – <ul>
<li>The number of instances calculated as a fixed number or a percentage depending on the settings. Structure is documented below.</li>
</ul>
</li>
<li><strong>update_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If the <code class="docutils literal notranslate"><span class="pre">instance_template</span></code>
resource is modified, a value of <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> will prevent any of the managed
instances from being restarted by Terraform. A value of <code class="docutils literal notranslate"><span class="pre">&quot;ROLLING_UPDATE&quot;</span></code>
is supported as a beta feature. A value of <code class="docutils literal notranslate"><span class="pre">&quot;ROLLING_UPDATE&quot;</span></code> requires
<code class="docutils literal notranslate"><span class="pre">rolling_update_policy</span></code> block to be set. This field is deprecated as in
<code class="docutils literal notranslate"><span class="pre">2.0.0</span></code> it has no functionality anymore. It will be removed then. This field
is only present in the <code class="docutils literal notranslate"><span class="pre">google</span></code> provider.</li>
<li><strong>versions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Application versions managed by this instance group. Each
version deals with a specific instance template, allowing canary release scenarios.
Conflicts with <code class="docutils literal notranslate"><span class="pre">instance_template</span></code>. Structure is documented below. Beware that
exactly one version must not specify a target size. It means that versions with
a target size will respect the setting, and the one without target size will
be applied to all remaining Instances (top level target_size - each version target_size).
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta fields.</p>
</li>
<li><strong>wait_for_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, Terraform will
continue trying until it times out.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.auto_healing_policies">
<code class="descname">auto_healing_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.auto_healing_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>The autohealing policies for this managed instance
group. You can specify only one value. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups">official documentation</a>.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.base_instance_name">
<code class="descname">base_instance_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.base_instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The base instance name to use for
instances in this group. The value must be a valid
<a class="reference external" href="https://www.ietf.org/rfc/rfc1035.txt">RFC1035</a> name. Supported characters
are lowercase letters, numbers, and hyphens (-). Instances are named by
appending a hyphen and a random four-character string to the base instance
name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.description" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional textual description of the instance
group manager.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.distribution_policy_zones">
<code class="descname">distribution_policy_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.distribution_policy_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>The distribution policy for this managed instance
group. You can specify one or more values. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selectingzones">official documentation</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the instance group manager.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.instance_group">
<code class="descname">instance_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.instance_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The full URL of the instance group created by the manager.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.instance_template">
<code class="descname">instance_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.instance_template" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li>The full URL to an instance template from which all new instances of this version will be created.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.name" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li>Version name.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.named_ports">
<code class="descname">named_ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.named_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>The named port configuration. See the section below
for details on configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where the managed instance group resides.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.rolling_update_policy">
<code class="descname">rolling_update_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.rolling_update_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The update policy for this managed instance group. Structure is documented below. For more information, see the <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups">official documentation</a> and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patch">API</a>
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.target_pools">
<code class="descname">target_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.target_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>The full URL of all target pools to which new
instances in the group are added. Updating the target pools attribute does
not affect existing instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.target_size">
<code class="descname">target_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.target_size" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li>The number of instances calculated as a fixed number or a percentage depending on the settings. Structure is documented below.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.update_strategy">
<code class="descname">update_strategy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.update_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>If the <code class="docutils literal notranslate"><span class="pre">instance_template</span></code>
resource is modified, a value of <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code> will prevent any of the managed
instances from being restarted by Terraform. A value of <code class="docutils literal notranslate"><span class="pre">&quot;ROLLING_UPDATE&quot;</span></code>
is supported as a beta feature. A value of <code class="docutils literal notranslate"><span class="pre">&quot;ROLLING_UPDATE&quot;</span></code> requires
<code class="docutils literal notranslate"><span class="pre">rolling_update_policy</span></code> block to be set. This field is deprecated as in
<code class="docutils literal notranslate"><span class="pre">2.0.0</span></code> it has no functionality anymore. It will be removed then. This field
is only present in the <code class="docutils literal notranslate"><span class="pre">google</span></code> provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.versions">
<code class="descname">versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.versions" title="Permalink to this definition">¶</a></dt>
<dd><p>Application versions managed by this instance group. Each
version deals with a specific instance template, allowing canary release scenarios.
Conflicts with <code class="docutils literal notranslate"><span class="pre">instance_template</span></code>. Structure is documented below. Beware that
exactly one version must not specify a target size. It means that versions with
a target size will respect the setting, and the one without target size will
be applied to all remaining Instances (top level target_size - each version target_size).
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.wait_for_instances">
<code class="descname">wait_for_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.wait_for_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, Terraform will
continue trying until it times out.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RegionInstanceGroupManager.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RegionInstanceGroupManager.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Route">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">Route</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>dest_range=None</em>, <em>name=None</em>, <em>network=None</em>, <em>next_hop_gateway=None</em>, <em>next_hop_instance=None</em>, <em>next_hop_instance_zone=None</em>, <em>next_hop_ip=None</em>, <em>next_hop_vpn_tunnel=None</em>, <em>priority=None</em>, <em>project=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Route" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a Route resource.</p>
<p>A route is a rule that specifies how certain packets should be handled by
the virtual network. Routes are associated with virtual machines by tag,
and the set of routes for a particular virtual machine is called its
routing table. For each packet leaving a virtual machine, the system
searches that virtual machine’s routing table for a single best matching
route.</p>
<p>Routes match packets by destination IP address, preferring smaller or more
specific ranges over larger ones. If there is a tie, the system selects
the route with the smallest priority value. If there is still a tie, it
uses the layer three and four packet headers to select just one of the
remaining matching routes. The packet is then forwarded as specified by
the next_hop field of the winning route – either to another virtual
machine destination, a virtual machine gateway or a Compute
Engine-operated gateway. Packets that do not match any route in the
sending virtual machine’s routing table will be dropped.</p>
<p>A Route resource must have exactly one specification of either
nextHopGateway, nextHopInstance, nextHopIp, or nextHopVpnTunnel.</p>
<p>To get more information about Route, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/routes">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/vpc/docs/using-routes">Using Routes</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=route_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] description
:param pulumi.Input[str] dest_range
:param pulumi.Input[str] name
:param pulumi.Input[str] network
:param pulumi.Input[str] next_hop_gateway
:param pulumi.Input[str] next_hop_instance
:param pulumi.Input[str] next_hop_instance_zone: (Optional when <code class="docutils literal notranslate"><span class="pre">next_hop_instance</span></code> is</p>
<blockquote>
<div>specified)  The zone of the instance specified in
<code class="docutils literal notranslate"><span class="pre">next_hop_instance</span></code>.  Omit if <code class="docutils literal notranslate"><span class="pre">next_hop_instance</span></code> is specified as
a URL.</div></blockquote>
<p>:param pulumi.Input[str] next_hop_ip
:param pulumi.Input[str] next_hop_vpn_tunnel
:param pulumi.Input[int] priority
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[list] tags</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Route.next_hop_instance_zone">
<code class="descname">next_hop_instance_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Route.next_hop_instance_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional when <code class="docutils literal notranslate"><span class="pre">next_hop_instance</span></code> is
specified)  The zone of the instance specified in
<code class="docutils literal notranslate"><span class="pre">next_hop_instance</span></code>.  Omit if <code class="docutils literal notranslate"><span class="pre">next_hop_instance</span></code> is specified as
a URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Route.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Route.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Route.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Route.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Route.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Route.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Route.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Route.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Router">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">Router</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bgp=None</em>, <em>description=None</em>, <em>name=None</em>, <em>network=None</em>, <em>project=None</em>, <em>region=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Router" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a Router resource.</p>
<p>To get more information about Router, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/routers">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/router/docs/">Google Cloud Router</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=router_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[dict] bgp
:param pulumi.Input[str] description
:param pulumi.Input[str] name
:param pulumi.Input[str] network
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[str] region</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Router.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Router.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Router.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Router.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Router.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Router.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Router.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Router.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RouterInterface">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">RouterInterface</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>ip_range=None</em>, <em>name=None</em>, <em>project=None</em>, <em>region=None</em>, <em>router=None</em>, <em>vpn_tunnel=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Cloud Router interface. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/cloudrouter">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/routers">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>ip_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address and range of the interface. The IP range must be
in the RFC3927 link-local IP space. Changing this forces a new interface to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the interface, required by GCE. Changing
this forces a new interface to be created.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which this interface’s router belongs. If it
is not provided, the provider project is used. Changing this forces a new interface to be created.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region this interface’s router sits in. If not specified,
the project region will be used. Changing this forces a new interface to be
created.</li>
<li><strong>router</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the router this interface will be attached to.
Changing this forces a new interface to be created.</li>
<li><strong>vpn_tunnel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or resource link to the VPN tunnel this
interface will be linked to. Changing this forces a new interface to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterInterface.ip_range">
<code class="descname">ip_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.ip_range" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address and range of the interface. The IP range must be
in the RFC3927 link-local IP space. Changing this forces a new interface to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterInterface.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the interface, required by GCE. Changing
this forces a new interface to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterInterface.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which this interface’s router belongs. If it
is not provided, the provider project is used. Changing this forces a new interface to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterInterface.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region this interface’s router sits in. If not specified,
the project region will be used. Changing this forces a new interface to be
created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterInterface.router">
<code class="descname">router</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.router" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the router this interface will be attached to.
Changing this forces a new interface to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterInterface.vpn_tunnel">
<code class="descname">vpn_tunnel</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.vpn_tunnel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or resource link to the VPN tunnel this
interface will be linked to. Changing this forces a new interface to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RouterInterface.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RouterInterface.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterInterface.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RouterNat">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">RouterNat</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>icmp_idle_timeout_sec=None</em>, <em>min_ports_per_vm=None</em>, <em>name=None</em>, <em>nat_ip_allocate_option=None</em>, <em>nat_ips=None</em>, <em>project=None</em>, <em>region=None</em>, <em>router=None</em>, <em>source_subnetwork_ip_ranges_to_nat=None</em>, <em>subnetworks=None</em>, <em>tcp_established_idle_timeout_sec=None</em>, <em>tcp_transitory_idle_timeout_sec=None</em>, <em>udp_idle_timeout_sec=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterNat" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a RouterNat resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[int] icmp_idle_timeout_sec
:param pulumi.Input[int] min_ports_per_vm
:param pulumi.Input[str] name
:param pulumi.Input[str] nat_ip_allocate_option
:param pulumi.Input[list] nat_ips
:param pulumi.Input[str] project
:param pulumi.Input[str] region
:param pulumi.Input[str] router
:param pulumi.Input[str] source_subnetwork_ip_ranges_to_nat
:param pulumi.Input[list] subnetworks
:param pulumi.Input[int] tcp_established_idle_timeout_sec
:param pulumi.Input[int] tcp_transitory_idle_timeout_sec
:param pulumi.Input[int] udp_idle_timeout_sec</p>
<dl class="method">
<dt id="pulumi_gcp.compute.RouterNat.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RouterNat.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterNat.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RouterPeer">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">RouterPeer</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>advertised_route_priority=None</em>, <em>interface=None</em>, <em>name=None</em>, <em>peer_asn=None</em>, <em>peer_ip_address=None</em>, <em>project=None</em>, <em>region=None</em>, <em>router=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Cloud Router BGP peer. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/cloudrouter">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/routers">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>advertised_route_priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The priority of routes advertised to this BGP peer.
Changing this forces a new peer to be created.</li>
<li><strong>interface</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the interface the BGP peer is associated with.
Changing this forces a new peer to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for BGP peer, required by GCE. Changing
this forces a new peer to be created.</li>
<li><strong>peer_asn</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Peer BGP Autonomous System Number (ASN).
Changing this forces a new peer to be created.</li>
<li><strong>peer_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address of the BGP interface outside Google Cloud.
Changing this forces a new peer to be created.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which this peer’s router belongs. If it
is not provided, the provider project is used. Changing this forces a new peer to be created.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region this peer’s router sits in. If not specified,
the project region will be used. Changing this forces a new peer to be
created.</li>
<li><strong>router</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the router in which this BGP peer will be configured.
Changing this forces a new peer to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.advertised_route_priority">
<code class="descname">advertised_route_priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.advertised_route_priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of routes advertised to this BGP peer.
Changing this forces a new peer to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.interface">
<code class="descname">interface</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.interface" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the interface the BGP peer is associated with.
Changing this forces a new peer to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.ip_address">
<code class="descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address of the interface inside Google Cloud Platform.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for BGP peer, required by GCE. Changing
this forces a new peer to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.peer_asn">
<code class="descname">peer_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.peer_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>Peer BGP Autonomous System Number (ASN).
Changing this forces a new peer to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.peer_ip_address">
<code class="descname">peer_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.peer_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address of the BGP interface outside Google Cloud.
Changing this forces a new peer to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which this peer’s router belongs. If it
is not provided, the provider project is used. Changing this forces a new peer to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region this peer’s router sits in. If not specified,
the project region will be used. Changing this forces a new peer to be
created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.RouterPeer.router">
<code class="descname">router</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.router" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the router in which this BGP peer will be configured.
Changing this forces a new peer to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.RouterPeer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.RouterPeer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.RouterPeer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SSLCertificate">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">SSLCertificate</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>certificate=None</em>, <em>description=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>private_key=None</em>, <em>project=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SSLCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>An SslCertificate resource, used for HTTPS load balancing. This resource
provides a mechanism to upload an SSL key and certificate to
the load balancer to serve secure connections from the user.</p>
<p>To get more information about SslCertificate, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/sslCertificates">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/load-balancing/docs/ssl-certificates">Official Documentation</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=ssl_certificate_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] certificate
:param pulumi.Input[str] description
:param pulumi.Input[str] name
:param pulumi.Input[str] name_prefix: Creates a unique name beginning with the</p>
<blockquote>
<div>specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</div></blockquote>
<p>:param pulumi.Input[str] private_key
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.SSLCertificate.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SSLCertificate.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the
specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SSLCertificate.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SSLCertificate.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SSLCertificate.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SSLCertificate.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SSLCertificate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SSLCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SSLCertificate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SSLCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SSLPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">SSLPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>custom_features=None</em>, <em>description=None</em>, <em>min_tls_version=None</em>, <em>name=None</em>, <em>profile=None</em>, <em>project=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SSLPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a SSL policy. SSL policies give you the ability to control the
features of SSL that your SSL proxy or HTTPS load balancer negotiates.</p>
<p>To get more information about SslPolicy, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/sslPolicies">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/ssl-policies">Using SSL Policies</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=ssl_policy_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] custom_features
:param pulumi.Input[str] description
:param pulumi.Input[str] min_tls_version
:param pulumi.Input[str] name
:param pulumi.Input[str] profile
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.compute.SSLPolicy.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SSLPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SSLPolicy.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SSLPolicy.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SSLPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SSLPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SSLPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SSLPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SecurityPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">SecurityPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>project=None</em>, <em>rules=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>A Security Policy defines an IP blacklist or whitelist that protects load balanced Google Cloud services by denying or permitting traffic from specified IP ranges. For more information
see the <a class="reference external" href="https://cloud.google.com/armor/docs/configure-security-policies">official documentation</a>
and the <a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/securityPolicies">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional description of this security policy. Max size is 2048.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the security policy.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The set of rules that belong to this policy. There must always be a default
rule (rule with priority 2147483647 and match “*”). If no rules are provided when creating a
security policy, a default rule with action “allow” will be added. Structure is documented below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.SecurityPolicy.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional description of this security policy. Max size is 2048.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SecurityPolicy.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>Fingerprint of this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SecurityPolicy.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the security policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SecurityPolicy.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SecurityPolicy.rules">
<code class="descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of rules that belong to this policy. There must always be a default
rule (rule with priority 2147483647 and match “*”). If no rules are provided when creating a
security policy, a default rule with action “allow” will be added. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SecurityPolicy.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SecurityPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SecurityPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SecurityPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SharedVPCHostProject">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">SharedVPCHostProject</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>project=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCHostProject" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables the Google Compute Engine
<a class="reference external" href="https://cloud.google.com/compute/docs/shared-vpc">Shared VPC</a>
feature for a project, assigning it as a Shared VPC host project.</p>
<p>For more information, see,
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/projects">the Project API documentation</a>,
where the Shared VPC feature is referred to by its former name “XPN”.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project that will serve as a Shared VPC host project</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.SharedVPCHostProject.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCHostProject.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project that will serve as a Shared VPC host project</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SharedVPCHostProject.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCHostProject.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SharedVPCHostProject.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCHostProject.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SharedVPCServiceProject">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">SharedVPCServiceProject</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>host_project=None</em>, <em>service_project=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCServiceProject" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables the Google Compute Engine
<a class="reference external" href="https://cloud.google.com/compute/docs/shared-vpc">Shared VPC</a>
feature for a project, assigning it as a Shared VPC service project associated
with a given host project.</p>
<p>For more information, see,
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/projects">the Project API documentation</a>,
where the Shared VPC feature is referred to by its former name “XPN”.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>host_project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a host project to associate.</li>
<li><strong>service_project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project that will serve as a Shared VPC service project.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.SharedVPCServiceProject.host_project">
<code class="descname">host_project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCServiceProject.host_project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a host project to associate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SharedVPCServiceProject.service_project">
<code class="descname">service_project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCServiceProject.service_project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project that will serve as a Shared VPC service project.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SharedVPCServiceProject.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCServiceProject.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SharedVPCServiceProject.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SharedVPCServiceProject.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Snapshot">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">Snapshot</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>labels=None</em>, <em>name=None</em>, <em>project=None</em>, <em>snapshot_encryption_key=None</em>, <em>snapshot_encryption_key_raw=None</em>, <em>source_disk=None</em>, <em>source_disk_encryption_key=None</em>, <em>source_disk_encryption_key_raw=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a Persistent Disk Snapshot resource.</p>
<p>Use snapshots to back up data from your persistent disks. Snapshots are
different from public images and custom images, which are used primarily
to create instances or configure instance templates. Snapshots are useful
for periodic backup of the data on your persistent disks. You can create
snapshots from persistent disks even while they are attached to running
instances.</p>
<p>Snapshots are incremental, so you can create regular snapshots on a
persistent disk faster and at a much lower cost than if you regularly
created a full image of the disk.</p>
<p>To get more information about Snapshot, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/snapshots">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/disks/create-snapshots">Official Documentation</a></li>
</ul>
</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] description
:param pulumi.Input[dict] labels
:param pulumi.Input[str] name
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[dict] snapshot_encryption_key
:param pulumi.Input[str] snapshot_encryption_key_raw
:param pulumi.Input[str] source_disk
:param pulumi.Input[dict] source_disk_encryption_key
:param pulumi.Input[str] source_disk_encryption_key_raw
:param pulumi.Input[str] zone</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Snapshot.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Snapshot.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Snapshot.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Snapshot.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Snapshot.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Snapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Snapshot.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Snapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Subnetwork">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">Subnetwork</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>enable_flow_logs=None</em>, <em>ip_cidr_range=None</em>, <em>name=None</em>, <em>network=None</em>, <em>private_ip_google_access=None</em>, <em>project=None</em>, <em>region=None</em>, <em>secondary_ip_ranges=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>A VPC network is a virtual version of the traditional physical networks
that exist within and between physical data centers. A VPC network
provides connectivity for your Compute Engine virtual machine (VM)
instances, Container Engine containers, App Engine Flex services, and
other network-related resources.</p>
<p>Each GCP project contains one or more VPC networks. Each VPC network is a
global entity spanning all GCP regions. This global VPC network allows VM
instances and other resources to communicate with each other via internal,
private IP addresses.</p>
<p>Each VPC network is subdivided into subnets, and each subnet is contained
within a single region. You can have more than one subnet in a region for
a given VPC network. Each subnet has a contiguous private RFC1918 IP
space. You create instances, containers, and the like in these subnets.
When you create an instance, you must create it in a subnet, and the
instance draws its internal IP address from that subnet.</p>
<p>Virtual machine (VM) instances in a VPC network can communicate with
instances in all other subnets of the same VPC network, regardless of
region, using their RFC1918 private IP addresses. You can isolate portions
of the network, even entire subnets, using firewall rules.</p>
<p>To get more information about Subnetwork, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/beta/subnetworks">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/vpc/docs/configure-private-google-access">Private Google Access</a></li>
<li><a class="reference external" href="https://cloud.google.com/vpc/docs/using-vpc">Cloud Networking</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=subnetwork_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] description
:param pulumi.Input[bool] enable_flow_logs
:param pulumi.Input[str] ip_cidr_range
:param pulumi.Input[str] name
:param pulumi.Input[str] network
:param pulumi.Input[bool] private_ip_google_access
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[str] region
:param pulumi.Input[list] secondary_ip_ranges</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.Subnetwork.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Subnetwork.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.Subnetwork.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.Subnetwork.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.Subnetwork.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Subnetwork.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.Subnetwork.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.Subnetwork.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SubnetworkIAMBinding">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">SubnetworkIAMBinding</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>members=None</em>, <em>project=None</em>, <em>region=None</em>, <em>role=None</em>, <em>subnetwork=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><strong>Warning:</strong> These resources are in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta resources.</div></blockquote>
<p>Three different resources help you manage your IAM policy for GCE subnetwork. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_policy</span></code>: Authoritative. Sets the IAM policy for the subnetwork and replaces any existing policy already attached.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the subnetwork are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the subnetwork are preserved.</li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_policy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_binding</span></code> and <code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_member</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] members
:param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it</p>
<blockquote>
<div>is not provided, the provider project is used.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region of the subnetwork. If
unspecified, this defaults to the region configured in the provider.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</li>
<li><strong>subnetwork</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnetwork.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMBinding.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the subnetwork’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMBinding.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMBinding.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMBinding.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region of the subnetwork. If
unspecified, this defaults to the region configured in the provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMBinding.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMBinding.subnetwork">
<code class="descname">subnetwork</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMBinding.subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the subnetwork.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SubnetworkIAMBinding.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SubnetworkIAMBinding.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SubnetworkIAMMember">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">SubnetworkIAMMember</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>member=None</em>, <em>project=None</em>, <em>region=None</em>, <em>role=None</em>, <em>subnetwork=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMMember" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><strong>Warning:</strong> These resources are in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta resources.</div></blockquote>
<p>Three different resources help you manage your IAM policy for GCE subnetwork. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_policy</span></code>: Authoritative. Sets the IAM policy for the subnetwork and replaces any existing policy already attached.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the subnetwork are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the subnetwork are preserved.</li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_policy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_binding</span></code> and <code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_member</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] member
:param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it</p>
<blockquote>
<div>is not provided, the provider project is used.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region of the subnetwork. If
unspecified, this defaults to the region configured in the provider.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</li>
<li><strong>subnetwork</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnetwork.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMMember.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the subnetwork’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMMember.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMMember.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMMember.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region of the subnetwork. If
unspecified, this defaults to the region configured in the provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMMember.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMMember.subnetwork">
<code class="descname">subnetwork</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMMember.subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the subnetwork.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SubnetworkIAMMember.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SubnetworkIAMMember.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SubnetworkIAMPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">SubnetworkIAMPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>policy_data=None</em>, <em>project=None</em>, <em>region=None</em>, <em>subnetwork=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><strong>Warning:</strong> These resources are in beta, and should be used with the terraform-provider-google-beta provider.
See <a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">Provider Versions</a> for more details on beta resources.</div></blockquote>
<p>Three different resources help you manage your IAM policy for GCE subnetwork. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_policy</span></code>: Authoritative. Sets the IAM policy for the subnetwork and replaces any existing policy already attached.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the subnetwork are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the subnetwork are preserved.</li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_policy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_binding</span></code> and <code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_member</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_compute_subnetwork_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data source.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region of the subnetwork. If
unspecified, this defaults to the region configured in the provider.</li>
<li><strong>subnetwork</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnetwork.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMPolicy.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the subnetwork’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMPolicy.policy_data">
<code class="descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMPolicy.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMPolicy.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMPolicy.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region of the subnetwork. If
unspecified, this defaults to the region configured in the provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.SubnetworkIAMPolicy.subnetwork">
<code class="descname">subnetwork</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMPolicy.subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the subnetwork.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.SubnetworkIAMPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.SubnetworkIAMPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.SubnetworkIAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetHttpProxy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">TargetHttpProxy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>project=None</em>, <em>url_map=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpProxy" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a TargetHttpProxy resource, which is used by one or more global
forwarding rule to route incoming HTTP requests to a URL map.</p>
<p>To get more information about TargetHttpProxy, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/targetHttpProxies">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/http/target-proxies">Official Documentation</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=target_http_proxy_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] description
:param pulumi.Input[str] name
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[str] url_map</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetHttpProxy.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpProxy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetHttpProxy.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpProxy.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.TargetHttpProxy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpProxy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetHttpProxy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpProxy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetHttpsProxy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">TargetHttpsProxy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>project=None</em>, <em>quic_override=None</em>, <em>ssl_certificates=None</em>, <em>ssl_policy=None</em>, <em>url_map=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpsProxy" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a TargetHttpsProxy resource, which is used by one or more
global forwarding rule to route incoming HTTPS requests to a URL map.</p>
<p>To get more information about TargetHttpsProxy, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/targetHttpsProxies">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/http/target-proxies">Official Documentation</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=target_https_proxy_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] description
:param pulumi.Input[str] name
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[str] quic_override
:param pulumi.Input[list] ssl_certificates
:param pulumi.Input[str] ssl_policy
:param pulumi.Input[str] url_map</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetHttpsProxy.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpsProxy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetHttpsProxy.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpsProxy.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.TargetHttpsProxy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpsProxy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetHttpsProxy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetHttpsProxy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetPool">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">TargetPool</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>backup_pool=None</em>, <em>description=None</em>, <em>failover_ratio=None</em>, <em>health_checks=None</em>, <em>instances=None</em>, <em>name=None</em>, <em>project=None</em>, <em>region=None</em>, <em>session_affinity=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Target Pool within GCE. This is a collection of instances used as
target of a network load balancer (Forwarding Rule). For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/network/target-pools">the official
documentation</a>
and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/targetPools">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>backup_pool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL to the backup target pool. Must also set
failover_ratio.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Textual description field.</li>
<li><strong>failover_ratio</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Ratio (0 to 1) of failed nodes before using the
backup pool (which must also be set).</li>
<li><strong>health_checks</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – List of zero or one health check name or self_link. Only
legacy <code class="docutils literal notranslate"><span class="pre">google_compute_http_health_check</span></code> is supported.</li>
<li><strong>instances</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of instances in the pool. They can be given as
URLs, or in the form of “zone/name”. Note that the instances need not exist
at the time of target pool creation, so there is no need to use the
Terraform interpolators to create a dependency on the instances from the
target pool.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Where the target pool resides. Defaults to project
region.</li>
<li><strong>session_affinity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How to distribute load. Options are “NONE” (no
affinity). “CLIENT_IP” (hash of the source/dest addresses / ports), and
“CLIENT_IP_PROTO” also includes the protocol (default “NONE”).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.backup_pool">
<code class="descname">backup_pool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.backup_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>URL to the backup target pool. Must also set
failover_ratio.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Textual description field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.failover_ratio">
<code class="descname">failover_ratio</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.failover_ratio" title="Permalink to this definition">¶</a></dt>
<dd><p>Ratio (0 to 1) of failed nodes before using the
backup pool (which must also be set).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.health_checks">
<code class="descname">health_checks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.health_checks" title="Permalink to this definition">¶</a></dt>
<dd><p>List of zero or one health check name or self_link. Only
legacy <code class="docutils literal notranslate"><span class="pre">google_compute_http_health_check</span></code> is supported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.instances">
<code class="descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>List of instances in the pool. They can be given as
URLs, or in the form of “zone/name”. Note that the instances need not exist
at the time of target pool creation, so there is no need to use the
Terraform interpolators to create a dependency on the instances from the
target pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Where the target pool resides. Defaults to project
region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetPool.session_affinity">
<code class="descname">session_affinity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.session_affinity" title="Permalink to this definition">¶</a></dt>
<dd><p>How to distribute load. Options are “NONE” (no
affinity). “CLIENT_IP” (hash of the source/dest addresses / ports), and
“CLIENT_IP_PROTO” also includes the protocol (default “NONE”).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.TargetPool.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetPool.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetSSLProxy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">TargetSSLProxy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>backend_service=None</em>, <em>description=None</em>, <em>name=None</em>, <em>project=None</em>, <em>proxy_header=None</em>, <em>ssl_certificates=None</em>, <em>ssl_policy=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetSSLProxy" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a TargetSslProxy resource, which is used by one or more
global forwarding rule to route incoming SSL requests to a backend
service.</p>
<p>To get more information about TargetSslProxy, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/targetSslProxies">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/tcp-ssl/">Setting Up SSL proxy for Google Cloud Load Balancing</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=target_ssl_proxy_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] backend_service
:param pulumi.Input[str] description
:param pulumi.Input[str] name
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[str] proxy_header
:param pulumi.Input[str] ssl_certificates
:param pulumi.Input[str] ssl_policy</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetSSLProxy.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetSSLProxy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetSSLProxy.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetSSLProxy.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.TargetSSLProxy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetSSLProxy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetSSLProxy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetSSLProxy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetTCPProxy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">TargetTCPProxy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>backend_service=None</em>, <em>description=None</em>, <em>name=None</em>, <em>project=None</em>, <em>proxy_header=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetTCPProxy" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a TargetTcpProxy resource, which is used by one or more
global forwarding rule to route incoming TCP requests to a Backend
service.</p>
<p>To get more information about TargetTcpProxy, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/targetTcpProxies">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/tcp-ssl/tcp-proxy">Setting Up TCP proxy for Google Cloud Load Balancing</a></li>
</ul>
</li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=target_tcp_proxy_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] backend_service
:param pulumi.Input[str] description
:param pulumi.Input[str] name
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[str] proxy_header</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetTCPProxy.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetTCPProxy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.TargetTCPProxy.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.TargetTCPProxy.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.TargetTCPProxy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetTCPProxy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.TargetTCPProxy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.TargetTCPProxy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.URLMap">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">URLMap</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>default_service=None</em>, <em>description=None</em>, <em>host_rules=None</em>, <em>name=None</em>, <em>path_matchers=None</em>, <em>project=None</em>, <em>tests=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.URLMap" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a URL Map resource within GCE. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/http/url-map">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/urlMaps">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>default_service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The backend service or backend bucket to use when none of the given rules match.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A brief description of this resource.</li>
<li><strong>host_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of host rules. Multiple blocks of this type are permitted. Structure is documented below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</li>
<li><strong>path_matchers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of paths to match. Structure is documented below.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>tests</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The test to perform.  Multiple blocks of this type are permitted. Structure is documented below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.compute.URLMap.default_service">
<code class="descname">default_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.URLMap.default_service" title="Permalink to this definition">¶</a></dt>
<dd><p>The backend service or backend bucket to use when none of the given rules match.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.URLMap.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.URLMap.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A brief description of this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.URLMap.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.URLMap.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique fingerprint for this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.URLMap.host_rules">
<code class="descname">host_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.URLMap.host_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of host rules. Multiple blocks of this type are permitted. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.URLMap.map_id">
<code class="descname">map_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.URLMap.map_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCE assigned ID of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.URLMap.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.URLMap.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.URLMap.path_matchers">
<code class="descname">path_matchers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.URLMap.path_matchers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of paths to match. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.URLMap.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.URLMap.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.URLMap.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.URLMap.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.URLMap.tests">
<code class="descname">tests</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.URLMap.tests" title="Permalink to this definition">¶</a></dt>
<dd><p>The test to perform.  Multiple blocks of this type are permitted. Structure is documented below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.URLMap.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.URLMap.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.URLMap.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.URLMap.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.VPNGateway">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">VPNGateway</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>name=None</em>, <em>network=None</em>, <em>project=None</em>, <em>region=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.VPNGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a VPN gateway running in GCP. This virtual device is managed
by Google, but used only by you.</p>
<p>To get more information about VpnGateway, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways">API documentation</a></li>
</ul>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=target_vpn_gateway_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] description
:param pulumi.Input[str] name
:param pulumi.Input[str] network
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[str] region</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.VPNGateway.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.VPNGateway.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.VPNGateway.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.VPNGateway.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.VPNGateway.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.VPNGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.VPNGateway.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.VPNGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.VPNTunnel">
<em class="property">class </em><code class="descclassname">pulumi_gcp.compute.</code><code class="descname">VPNTunnel</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>ike_version=None</em>, <em>labels=None</em>, <em>local_traffic_selectors=None</em>, <em>name=None</em>, <em>peer_ip=None</em>, <em>project=None</em>, <em>region=None</em>, <em>remote_traffic_selectors=None</em>, <em>router=None</em>, <em>shared_secret=None</em>, <em>target_vpn_gateway=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.VPNTunnel" title="Permalink to this definition">¶</a></dt>
<dd><p>VPN tunnel resource.</p>
<p>To get more information about VpnTunnel, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/vpn/docs/concepts/overview">Cloud VPN Overview</a></li>
<li><a class="reference external" href="https://cloud.google.com/vpn/docs/concepts/choosing-networks-routing">Networks and Tunnel Routing</a></li>
</ul>
</li>
</ul>
<blockquote>
<div><strong>Warning:</strong> All arguments including the shared secret will be stored in the raw
state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=vpn_tunnel_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] description
:param pulumi.Input[int] ike_version
:param pulumi.Input[dict] labels
:param pulumi.Input[list] local_traffic_selectors
:param pulumi.Input[str] name
:param pulumi.Input[str] peer_ip
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<p>:param pulumi.Input[str] region
:param pulumi.Input[list] remote_traffic_selectors
:param pulumi.Input[str] router
:param pulumi.Input[str] shared_secret
:param pulumi.Input[str] target_vpn_gateway</p>
<dl class="attribute">
<dt id="pulumi_gcp.compute.VPNTunnel.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.VPNTunnel.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.compute.VPNTunnel.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.compute.VPNTunnel.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.compute.VPNTunnel.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.VPNTunnel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.VPNTunnel.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.VPNTunnel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.compute.get_address">
<code class="descclassname">pulumi_gcp.compute.</code><code class="descname">get_address</code><span class="sig-paren">(</span><em>name=None</em>, <em>project=None</em>, <em>region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the IP address from a static address. For more information see
the official <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/addresses/get">API</a> documentation.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_backend_service">
<code class="descclassname">pulumi_gcp.compute.</code><code class="descname">get_backend_service</code><span class="sig-paren">(</span><em>name=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_backend_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Provide acces to a Backend Service’s attribute. For more information
see <a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/http/backend-service">the official documentation</a>
and the <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/backendServices">API</a>.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_default_service_account">
<code class="descclassname">pulumi_gcp.compute.</code><code class="descname">get_default_service_account</code><span class="sig-paren">(</span><em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_default_service_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve default service account for this project</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_forwarding_rule">
<code class="descclassname">pulumi_gcp.compute.</code><code class="descname">get_forwarding_rule</code><span class="sig-paren">(</span><em>name=None</em>, <em>project=None</em>, <em>region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_forwarding_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Get a forwarding rule within GCE from its name.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_global_address">
<code class="descclassname">pulumi_gcp.compute.</code><code class="descname">get_global_address</code><span class="sig-paren">(</span><em>name=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_global_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the IP address from a static address reserved for a Global Forwarding Rule which are only used for HTTP load balancing. For more information see
the official <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/globalAddresses">API</a> documentation.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_image">
<code class="descclassname">pulumi_gcp.compute.</code><code class="descname">get_image</code><span class="sig-paren">(</span><em>family=None</em>, <em>name=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information about a Google Compute Image. Check that your service account has the <code class="docutils literal notranslate"><span class="pre">compute.imageUser</span></code> role if you want to share <a class="reference external" href="https://cloud.google.com/compute/docs/images/sharing-images-across-projects">custom images</a> from another project. If you want to use [public images][pubimg], do not forget to specify the dedicated project. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/images">the official documentation</a> and its <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/images">API</a>.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_instance">
<code class="descclassname">pulumi_gcp.compute.</code><code class="descname">get_instance</code><span class="sig-paren">(</span><em>name=None</em>, <em>project=None</em>, <em>zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information about a VM instance resource within GCE. For more information see
<a class="reference external" href="https://cloud.google.com/compute/docs/instances">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instances">API</a>.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_instance_group">
<code class="descclassname">pulumi_gcp.compute.</code><code class="descname">get_instance_group</code><span class="sig-paren">(</span><em>name=None</em>, <em>project=None</em>, <em>self_link=None</em>, <em>zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_instance_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Get a Compute Instance Group within GCE.
For more information, see <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/#unmanaged_instance_groups">the official documentation</a>
and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instanceGroups">API</a></p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_lbip_ranges">
<code class="descclassname">pulumi_gcp.compute.</code><code class="descname">get_lbip_ranges</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_lbip_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access IP ranges in your firewall rules.</p>
<p><a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/health-checks#health_check_source_ips_and_firewall_rules">https://cloud.google.com/compute/docs/load-balancing/health-checks#health_check_source_ips_and_firewall_rules</a></p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_netblock_ip_ranges">
<code class="descclassname">pulumi_gcp.compute.</code><code class="descname">get_netblock_ip_ranges</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_netblock_ip_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the IP ranges from the sender policy framework (SPF) record of _cloud-netblocks.googleusercontent</p>
<p><a class="reference external" href="https://cloud.google.com/compute/docs/faq#where_can_i_find_product_name_short_ip_ranges">https://cloud.google.com/compute/docs/faq#where_can_i_find_product_name_short_ip_ranges</a></p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_network">
<code class="descclassname">pulumi_gcp.compute.</code><code class="descname">get_network</code><span class="sig-paren">(</span><em>name=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_network" title="Permalink to this definition">¶</a></dt>
<dd><p>Get a network within GCE from its name.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_region_instance_group">
<code class="descclassname">pulumi_gcp.compute.</code><code class="descname">get_region_instance_group</code><span class="sig-paren">(</span><em>name=None</em>, <em>project=None</em>, <em>region=None</em>, <em>self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_region_instance_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Get a Compute Region Instance Group within GCE.
For more information, see <a class="reference external" href="https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups">the official documentation</a> and <a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/regionInstanceGroups">API</a>.</p>
<p>The most common use of this datasource will be to fetch information about the instances inside regional managed instance groups, for instance:</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_regions">
<code class="descclassname">pulumi_gcp.compute.</code><code class="descname">get_regions</code><span class="sig-paren">(</span><em>project=None</em>, <em>status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to available Google Compute regions for a given project.
See more about <a class="reference external" href="https://cloud.google.com/compute/docs/regions-zones/">regions and regions</a> in the upstream docs.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_ssl_policy">
<code class="descclassname">pulumi_gcp.compute.</code><code class="descname">get_ssl_policy</code><span class="sig-paren">(</span><em>name=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_ssl_policy" title="Permalink to this definition">¶</a></dt>
<dd><dl class="docutils">
<dt>Gets an SSL Policy within GCE from its name, for use with Target HTTPS and Target SSL Proxies.</dt>
<dd>For more information see <a class="reference external" href="https://cloud.google.com/compute/docs/load-balancing/ssl-policies">the official documentation</a>.</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_subnetwork">
<code class="descclassname">pulumi_gcp.compute.</code><code class="descname">get_subnetwork</code><span class="sig-paren">(</span><em>name=None</em>, <em>project=None</em>, <em>region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>Get a subnetwork within GCE from its name and region.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_vpn_gateway">
<code class="descclassname">pulumi_gcp.compute.</code><code class="descname">get_vpn_gateway</code><span class="sig-paren">(</span><em>name=None</em>, <em>project=None</em>, <em>region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_vpn_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Get a VPN gateway within GCE from its name.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.compute.get_zones">
<code class="descclassname">pulumi_gcp.compute.</code><code class="descname">get_zones</code><span class="sig-paren">(</span><em>project=None</em>, <em>region=None</em>, <em>status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.compute.get_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to available Google Compute zones in a region for a given project.
See more about <a class="reference external" href="https://cloud.google.com/compute/docs/regions-zones/regions-zones">regions and zones</a> in the upstream docs.</p>
</dd></dl>

</div>
