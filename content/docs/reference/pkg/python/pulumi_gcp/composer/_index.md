---
title: Module composer
title_tag: Module composer | Package pulumi_gcp | Python SDK
linktitle: composer
notitle: true
---

<div class="section" id="composer">
<h1>composer<a class="headerlink" href="#composer" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.composer"></span><dl class="py class">
<dt id="pulumi_gcp.composer.AwaitableGetImageVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.composer.</code><code class="sig-name descname">AwaitableGetImageVersionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_versions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.composer.AwaitableGetImageVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.composer.Environment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.composer.</code><code class="sig-name descname">Environment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.composer.Environment" title="Permalink to this definition">¶</a></dt>
<dd><p>An environment for running orchestration tasks.</p>
<p>Environments run Apache Airflow software on Google infrastructure.</p>
<p>To get more information about Environments, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/composer/docs/reference/rest/">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/composer/docs">Official Documentation</a></p></li>
<li><p><a class="reference external" href="https://cloud.google.com/composer/docs/how-to/managing/configuring-shared-vpc">Configuring Shared VPC for Composer Environments</a></p></li>
</ul>
</li>
<li><p><a class="reference external" href="http://airflow.apache.org/">Apache Airflow Documentation</a></p></li>
</ul>
<blockquote>
<div><dl class="simple">
<dt><strong>Warning:</strong> We <strong>STRONGLY</strong> recommend  you read the <a class="reference external" href="https://cloud.google.com/composer/docs/how-to">GCP guides</a></dt><dd><p>as the Environment resource requires a long deployment process and involves several layers of GCP infrastructure, 
including a Kubernetes Engine cluster, Cloud Storage, and Compute networking resources. Due to limitations of the API,
This provider will not be able to automatically find or manage many of these underlying resources. In particular:</p>
</dd>
</dl>
<ul class="simple">
<li><p>It can take up to one hour to create or update an environment resource. In addition, GCP may only detect some 
errors in configuration when they are used (e.g. ~40-50 minutes into the creation process), and is prone to limited
error reporting. If you encounter confusing or uninformative errors, please verify your configuration is valid 
against GCP Cloud Composer before filing bugs against this provider.</p></li>
<li><p><strong>Environments create Google Cloud Storage buckets that do not get cleaned up automatically</strong> on environment 
deletion. <a class="reference external" href="https://cloud.google.com/composer/docs/concepts/cloud-storage">More about Composer’s use of Cloud Storage</a>.</p></li>
</ul>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration parameters for this environment  Structure is documented below.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – User-defined labels for this environment. The labels map can contain
no more than 64 entries. Entries of the labels map are UTF8 strings
that comply with the following restrictions:
Label keys must be between 1 and 63 characters long and must conform
to the following regular expression: <code class="docutils literal notranslate"><span class="pre">a-z?</span></code>.
Label values must be between 0 and 63 characters long and must
conform to the regular expression <code class="docutils literal notranslate"><span class="pre">(a-z?)?</span></code>.
No more than 64 labels can be associated with a given environment.
Both keys and values must be &lt;= 128 bytes in size.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the environment</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location or Compute Engine region for the environment.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>config</strong> object supports the following:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">airflowUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dagGcsPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gkeCluster</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The configuration used for the Kubernetes Engine cluster.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The disk size in GB used for node VMs. Minimum size is 20GB.
If unspecified, defaults to 100GB. Cannot be updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_allocation_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration for controlling how IPs are allocated in the GKE cluster.
Structure is documented below.
Cannot be updated.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address range used to allocate IP addresses to pods in the cluster.
Set to blank to have GKE choose a range with the default size.
Set to /netmask (e.g. /14) to have GKE choose a range with a specific netmask.
Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks
(e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.
Specify either <code class="docutils literal notranslate"><span class="pre">cluster_secondary_range_name</span></code> or <code class="docutils literal notranslate"><span class="pre">cluster_ipv4_cidr_block</span></code> but not both.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the cluster’s secondary range used to allocate IP addresses to pods.
Specify either <code class="docutils literal notranslate"><span class="pre">cluster_secondary_range_name</span></code> or <code class="docutils literal notranslate"><span class="pre">cluster_ipv4_cidr_block</span></code> but not both.
This field is applicable only when <code class="docutils literal notranslate"><span class="pre">use_ip_aliases</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address range used to allocate IP addresses in this cluster.
Set to blank to have GKE choose a range with the default size.
Set to /netmask (e.g. /14) to have GKE choose a range with a specific netmask.
Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks
(e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.
Specify either <code class="docutils literal notranslate"><span class="pre">services_secondary_range_name</span></code> or <code class="docutils literal notranslate"><span class="pre">services_ipv4_cidr_block</span></code> but not both.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the services’ secondary range used to allocate IP addresses to the cluster.
Specify either <code class="docutils literal notranslate"><span class="pre">services_secondary_range_name</span></code> or <code class="docutils literal notranslate"><span class="pre">services_ipv4_cidr_block</span></code> but not both.
This field is applicable only when <code class="docutils literal notranslate"><span class="pre">use_ip_aliases</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useIpAliases</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether or not to enable Alias IPs in the GKE cluster. If true, a VPC-native cluster is created.
Defaults to true if the <code class="docutils literal notranslate"><span class="pre">ip_allocation_block</span></code> is present in config.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Compute Engine machine type used for cluster instances,
specified as a name or relative resource name. For example:
“projects/{project}/zones/{zone}/machineTypes/{machineType}”. Must belong to the enclosing environment’s project and
region/zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Compute Engine network to be used for machine
communications, specified as a self-link, relative resource name
(e.g. “projects/{project}/global/networks/{network}”), by name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of Google API scopes to be made available on all node
VMs. Cannot be updated. If empty, defaults to
<code class="docutils literal notranslate"><span class="pre">[&quot;https://www.googleapis.com/auth/cloud-platform&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Google Cloud Platform Service Account to be used by the
node VMs. If a service account is not specified, the “default”
Compute Engine service account is used. Cannot be updated. If given,
note that the service account must have <code class="docutils literal notranslate"><span class="pre">roles/composer.worker</span></code>
for any GCP resources created under the Cloud Composer Environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Compute Engine subnetwork to be used for machine
communications, , specified as a self-link, relative resource name (e.g.
“projects/{project}/regions/{region}/subnetworks/{subnetwork}”), or by name. If subnetwork is provided,
network must also be provided and the subnetwork must belong to the enclosing environment’s project and region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of instance tags applied to all node VMs. Tags are
used to identify valid sources or targets for network
firewalls. Each tag within the list must comply with RFC1035.
Cannot be updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Compute Engine zone in which to deploy the VMs running the
Apache Airflow software, specified as the zone name or
relative resource name (e.g. “projects/{project}/zones/{zone}”). Must belong to the enclosing environment’s project
and region.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of nodes in the Kubernetes Engine cluster that
will be used to run this environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateEnvironmentConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The configuration used for the Private IP Cloud Composer environment. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enablePrivateEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - -
If true, access to the public endpoint of the GKE cluster is denied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP range in CIDR notation to use for the hosted master network. This range is used
for assigning internal IP addresses to the cluster master or set of masters and to the
internal load balancer virtual IP. This range must not overlap with any other ranges
in use within the cluster’s network.
If left blank, the default value of ‘172.16.0.0/28’ is used.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">softwareConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The configuration settings for software inside the environment.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">airflowConfigOverrides</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - -
(Optional) Apache Airflow configuration properties to override. Property keys contain the section and property names,
separated by a hyphen, for example “core-dags_are_paused_at_creation”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">env_variables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Additional environment variables to provide to the Apache Airflow scheduler, worker, and webserver processes.
Environment variable names must match the regular expression <code class="docutils literal notranslate"><span class="pre">[a-zA-Z_][a-zA-Z0-9_]*</span></code>.
They cannot specify Apache Airflow software configuration overrides (they cannot match the regular expression
<code class="docutils literal notranslate"><span class="pre">AIRFLOW__[A-Z0-9_]+__[A-Z0-9_]+</span></code>), and they cannot match any of the following reserved names:
.. code-block:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">AIRFLOW_HOME</span>
<span class="n">C_FORCE_ROOT</span>
<span class="n">CONTAINER_NAME</span>
<span class="n">DAGS_FOLDER</span>
<span class="n">GCP_PROJECT</span>
<span class="n">GCS_BUCKET</span>
<span class="n">GKE_CLUSTER_NAME</span>
<span class="n">SQL_DATABASE</span>
<span class="n">SQL_INSTANCE</span>
<span class="n">SQL_PASSWORD</span>
<span class="n">SQL_PROJECT</span>
<span class="n">SQL_REGION</span>
<span class="n">SQL_USER</span>
</pre></div>
</div>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The version of the software running in the environment. This encapsulates both the version of Cloud Composer
functionality and the version of Apache Airflow. It must match the regular expression
<code class="docutils literal notranslate"><span class="pre">composer-[0-9]+\.[0-9]+(\.[0-9]+)?-airflow-[0-9]+\.[0-9]+(\.[0-9]+.*)?</span></code>.
The Cloud Composer portion of the version is a semantic version.
The portion of the image version following ‘airflow-‘ is an official Apache Airflow repository release name.
See <a class="reference external" href="https://cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments#softwareconfig">documentation</a>
for allowed release names.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pypiPackages</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Custom Python Package Index (PyPI) packages to be installed
in the environment. Keys refer to the lowercase package name (e.g. “numpy”). Values are the lowercase extras and
version specifier (e.g. “==1.12.0”, “[devel,gcp_api]”, “[devel]&gt;=1.8.2, &lt;1.9.2”). To specify a package without
pinning it to a version specifier, use the empty string as the value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pythonVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The major version of Python used to run the Apache Airflow scheduler, worker, and webserver processes.
Can be set to ‘2’ or ‘3’. If not specified, the default is ‘2’. Cannot be updated.</p></li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.composer.Environment.config">
<code class="sig-name descname">config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.composer.Environment.config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration parameters for this environment  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">airflowUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dagGcsPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gkeCluster</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_config</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The configuration used for the Kubernetes Engine cluster.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The disk size in GB used for node VMs. Minimum size is 20GB.
If unspecified, defaults to 100GB. Cannot be updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_allocation_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration for controlling how IPs are allocated in the GKE cluster.
Structure is documented below.
Cannot be updated.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IP address range used to allocate IP addresses to pods in the cluster.
Set to blank to have GKE choose a range with the default size.
Set to /netmask (e.g. /14) to have GKE choose a range with a specific netmask.
Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks
(e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.
Specify either <code class="docutils literal notranslate"><span class="pre">cluster_secondary_range_name</span></code> or <code class="docutils literal notranslate"><span class="pre">cluster_ipv4_cidr_block</span></code> but not both.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the cluster’s secondary range used to allocate IP addresses to pods.
Specify either <code class="docutils literal notranslate"><span class="pre">cluster_secondary_range_name</span></code> or <code class="docutils literal notranslate"><span class="pre">cluster_ipv4_cidr_block</span></code> but not both.
This field is applicable only when <code class="docutils literal notranslate"><span class="pre">use_ip_aliases</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IP address range used to allocate IP addresses in this cluster.
Set to blank to have GKE choose a range with the default size.
Set to /netmask (e.g. /14) to have GKE choose a range with a specific netmask.
Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks
(e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.
Specify either <code class="docutils literal notranslate"><span class="pre">services_secondary_range_name</span></code> or <code class="docutils literal notranslate"><span class="pre">services_ipv4_cidr_block</span></code> but not both.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the services’ secondary range used to allocate IP addresses to the cluster.
Specify either <code class="docutils literal notranslate"><span class="pre">services_secondary_range_name</span></code> or <code class="docutils literal notranslate"><span class="pre">services_ipv4_cidr_block</span></code> but not both.
This field is applicable only when <code class="docutils literal notranslate"><span class="pre">use_ip_aliases</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useIpAliases</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether or not to enable Alias IPs in the GKE cluster. If true, a VPC-native cluster is created.
Defaults to true if the <code class="docutils literal notranslate"><span class="pre">ip_allocation_block</span></code> is present in config.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Compute Engine machine type used for cluster instances,
specified as a name or relative resource name. For example:
“projects/{project}/zones/{zone}/machineTypes/{machineType}”. Must belong to the enclosing environment’s project and
region/zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Compute Engine network to be used for machine
communications, specified as a self-link, relative resource name
(e.g. “projects/{project}/global/networks/{network}”), by name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The set of Google API scopes to be made available on all node
VMs. Cannot be updated. If empty, defaults to
<code class="docutils literal notranslate"><span class="pre">[&quot;https://www.googleapis.com/auth/cloud-platform&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Google Cloud Platform Service Account to be used by the
node VMs. If a service account is not specified, the “default”
Compute Engine service account is used. Cannot be updated. If given,
note that the service account must have <code class="docutils literal notranslate"><span class="pre">roles/composer.worker</span></code>
for any GCP resources created under the Cloud Composer Environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Compute Engine subnetwork to be used for machine
communications, , specified as a self-link, relative resource name (e.g.
“projects/{project}/regions/{region}/subnetworks/{subnetwork}”), or by name. If subnetwork is provided,
network must also be provided and the subnetwork must belong to the enclosing environment’s project and region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The list of instance tags applied to all node VMs. Tags are
used to identify valid sources or targets for network
firewalls. Each tag within the list must comply with RFC1035.
Cannot be updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Compute Engine zone in which to deploy the VMs running the
Apache Airflow software, specified as the zone name or
relative resource name (e.g. “projects/{project}/zones/{zone}”). Must belong to the enclosing environment’s project
and region.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of nodes in the Kubernetes Engine cluster that
will be used to run this environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateEnvironmentConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The configuration used for the Private IP Cloud Composer environment. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enablePrivateEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - -
If true, access to the public endpoint of the GKE cluster is denied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IP range in CIDR notation to use for the hosted master network. This range is used
for assigning internal IP addresses to the cluster master or set of masters and to the
internal load balancer virtual IP. This range must not overlap with any other ranges
in use within the cluster’s network.
If left blank, the default value of ‘172.16.0.0/28’ is used.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">softwareConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The configuration settings for software inside the environment.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">airflowConfigOverrides</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - -
(Optional) Apache Airflow configuration properties to override. Property keys contain the section and property names,
separated by a hyphen, for example “core-dags_are_paused_at_creation”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">env_variables</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Additional environment variables to provide to the Apache Airflow scheduler, worker, and webserver processes.
Environment variable names must match the regular expression <code class="docutils literal notranslate"><span class="pre">[a-zA-Z_][a-zA-Z0-9_]*</span></code>.
They cannot specify Apache Airflow software configuration overrides (they cannot match the regular expression
<code class="docutils literal notranslate"><span class="pre">AIRFLOW__[A-Z0-9_]+__[A-Z0-9_]+</span></code>), and they cannot match any of the following reserved names:
.. code-block:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">AIRFLOW_HOME</span>
<span class="n">C_FORCE_ROOT</span>
<span class="n">CONTAINER_NAME</span>
<span class="n">DAGS_FOLDER</span>
<span class="n">GCP_PROJECT</span>
<span class="n">GCS_BUCKET</span>
<span class="n">GKE_CLUSTER_NAME</span>
<span class="n">SQL_DATABASE</span>
<span class="n">SQL_INSTANCE</span>
<span class="n">SQL_PASSWORD</span>
<span class="n">SQL_PROJECT</span>
<span class="n">SQL_REGION</span>
<span class="n">SQL_USER</span>
</pre></div>
</div>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
The version of the software running in the environment. This encapsulates both the version of Cloud Composer
functionality and the version of Apache Airflow. It must match the regular expression
<code class="docutils literal notranslate"><span class="pre">composer-[0-9]+\.[0-9]+(\.[0-9]+)?-airflow-[0-9]+\.[0-9]+(\.[0-9]+.*)?</span></code>.
The Cloud Composer portion of the version is a semantic version.
The portion of the image version following ‘airflow-‘ is an official Apache Airflow repository release name.
See <a class="reference external" href="https://cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments#softwareconfig">documentation</a>
for allowed release names.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pypiPackages</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Custom Python Package Index (PyPI) packages to be installed
in the environment. Keys refer to the lowercase package name (e.g. “numpy”). Values are the lowercase extras and
version specifier (e.g. “==1.12.0”, “[devel,gcp_api]”, “[devel]&gt;=1.8.2, &lt;1.9.2”). To specify a package without
pinning it to a version specifier, use the empty string as the value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pythonVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
The major version of Python used to run the Apache Airflow scheduler, worker, and webserver processes.
Can be set to ‘2’ or ‘3’. If not specified, the default is ‘2’. Cannot be updated.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.composer.Environment.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.composer.Environment.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined labels for this environment. The labels map can contain
no more than 64 entries. Entries of the labels map are UTF8 strings
that comply with the following restrictions:
Label keys must be between 1 and 63 characters long and must conform
to the following regular expression: <code class="docutils literal notranslate"><span class="pre">a-z?</span></code>.
Label values must be between 0 and 63 characters long and must
conform to the regular expression <code class="docutils literal notranslate"><span class="pre">(a-z?)?</span></code>.
No more than 64 labels can be associated with a given environment.
Both keys and values must be &lt;= 128 bytes in size.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.composer.Environment.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.composer.Environment.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the environment</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.composer.Environment.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.composer.Environment.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.composer.Environment.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.composer.Environment.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The location or Compute Engine region for the environment.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.composer.Environment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.composer.Environment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Environment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration parameters for this environment  Structure is documented below.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – User-defined labels for this environment. The labels map can contain
no more than 64 entries. Entries of the labels map are UTF8 strings
that comply with the following restrictions:
Label keys must be between 1 and 63 characters long and must conform
to the following regular expression: <code class="docutils literal notranslate"><span class="pre">a-z?</span></code>.
Label values must be between 0 and 63 characters long and must
conform to the regular expression <code class="docutils literal notranslate"><span class="pre">(a-z?)?</span></code>.
No more than 64 labels can be associated with a given environment.
Both keys and values must be &lt;= 128 bytes in size.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the environment</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location or Compute Engine region for the environment.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>config</strong> object supports the following:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">airflowUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dagGcsPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gkeCluster</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The configuration used for the Kubernetes Engine cluster.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The disk size in GB used for node VMs. Minimum size is 20GB.
If unspecified, defaults to 100GB. Cannot be updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_allocation_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration for controlling how IPs are allocated in the GKE cluster.
Structure is documented below.
Cannot be updated.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address range used to allocate IP addresses to pods in the cluster.
Set to blank to have GKE choose a range with the default size.
Set to /netmask (e.g. /14) to have GKE choose a range with a specific netmask.
Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks
(e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.
Specify either <code class="docutils literal notranslate"><span class="pre">cluster_secondary_range_name</span></code> or <code class="docutils literal notranslate"><span class="pre">cluster_ipv4_cidr_block</span></code> but not both.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the cluster’s secondary range used to allocate IP addresses to pods.
Specify either <code class="docutils literal notranslate"><span class="pre">cluster_secondary_range_name</span></code> or <code class="docutils literal notranslate"><span class="pre">cluster_ipv4_cidr_block</span></code> but not both.
This field is applicable only when <code class="docutils literal notranslate"><span class="pre">use_ip_aliases</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address range used to allocate IP addresses in this cluster.
Set to blank to have GKE choose a range with the default size.
Set to /netmask (e.g. /14) to have GKE choose a range with a specific netmask.
Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks
(e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.
Specify either <code class="docutils literal notranslate"><span class="pre">services_secondary_range_name</span></code> or <code class="docutils literal notranslate"><span class="pre">services_ipv4_cidr_block</span></code> but not both.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the services’ secondary range used to allocate IP addresses to the cluster.
Specify either <code class="docutils literal notranslate"><span class="pre">services_secondary_range_name</span></code> or <code class="docutils literal notranslate"><span class="pre">services_ipv4_cidr_block</span></code> but not both.
This field is applicable only when <code class="docutils literal notranslate"><span class="pre">use_ip_aliases</span></code> is true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useIpAliases</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether or not to enable Alias IPs in the GKE cluster. If true, a VPC-native cluster is created.
Defaults to true if the <code class="docutils literal notranslate"><span class="pre">ip_allocation_block</span></code> is present in config.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Compute Engine machine type used for cluster instances,
specified as a name or relative resource name. For example:
“projects/{project}/zones/{zone}/machineTypes/{machineType}”. Must belong to the enclosing environment’s project and
region/zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Compute Engine network to be used for machine
communications, specified as a self-link, relative resource name
(e.g. “projects/{project}/global/networks/{network}”), by name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of Google API scopes to be made available on all node
VMs. Cannot be updated. If empty, defaults to
<code class="docutils literal notranslate"><span class="pre">[&quot;https://www.googleapis.com/auth/cloud-platform&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Google Cloud Platform Service Account to be used by the
node VMs. If a service account is not specified, the “default”
Compute Engine service account is used. Cannot be updated. If given,
note that the service account must have <code class="docutils literal notranslate"><span class="pre">roles/composer.worker</span></code>
for any GCP resources created under the Cloud Composer Environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Compute Engine subnetwork to be used for machine
communications, , specified as a self-link, relative resource name (e.g.
“projects/{project}/regions/{region}/subnetworks/{subnetwork}”), or by name. If subnetwork is provided,
network must also be provided and the subnetwork must belong to the enclosing environment’s project and region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of instance tags applied to all node VMs. Tags are
used to identify valid sources or targets for network
firewalls. Each tag within the list must comply with RFC1035.
Cannot be updated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Compute Engine zone in which to deploy the VMs running the
Apache Airflow software, specified as the zone name or
relative resource name (e.g. “projects/{project}/zones/{zone}”). Must belong to the enclosing environment’s project
and region.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of nodes in the Kubernetes Engine cluster that
will be used to run this environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateEnvironmentConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The configuration used for the Private IP Cloud Composer environment. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enablePrivateEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - -
If true, access to the public endpoint of the GKE cluster is denied.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP range in CIDR notation to use for the hosted master network. This range is used
for assigning internal IP addresses to the cluster master or set of masters and to the
internal load balancer virtual IP. This range must not overlap with any other ranges
in use within the cluster’s network.
If left blank, the default value of ‘172.16.0.0/28’ is used.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">softwareConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The configuration settings for software inside the environment.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">airflowConfigOverrides</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - -
(Optional) Apache Airflow configuration properties to override. Property keys contain the section and property names,
separated by a hyphen, for example “core-dags_are_paused_at_creation”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">env_variables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Additional environment variables to provide to the Apache Airflow scheduler, worker, and webserver processes.
Environment variable names must match the regular expression <code class="docutils literal notranslate"><span class="pre">[a-zA-Z_][a-zA-Z0-9_]*</span></code>.
They cannot specify Apache Airflow software configuration overrides (they cannot match the regular expression
<code class="docutils literal notranslate"><span class="pre">AIRFLOW__[A-Z0-9_]+__[A-Z0-9_]+</span></code>), and they cannot match any of the following reserved names:
.. code-block:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">AIRFLOW_HOME</span>
<span class="n">C_FORCE_ROOT</span>
<span class="n">CONTAINER_NAME</span>
<span class="n">DAGS_FOLDER</span>
<span class="n">GCP_PROJECT</span>
<span class="n">GCS_BUCKET</span>
<span class="n">GKE_CLUSTER_NAME</span>
<span class="n">SQL_DATABASE</span>
<span class="n">SQL_INSTANCE</span>
<span class="n">SQL_PASSWORD</span>
<span class="n">SQL_PROJECT</span>
<span class="n">SQL_REGION</span>
<span class="n">SQL_USER</span>
</pre></div>
</div>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The version of the software running in the environment. This encapsulates both the version of Cloud Composer
functionality and the version of Apache Airflow. It must match the regular expression
<code class="docutils literal notranslate"><span class="pre">composer-[0-9]+\.[0-9]+(\.[0-9]+)?-airflow-[0-9]+\.[0-9]+(\.[0-9]+.*)?</span></code>.
The Cloud Composer portion of the version is a semantic version.
The portion of the image version following ‘airflow-‘ is an official Apache Airflow repository release name.
See <a class="reference external" href="https://cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments#softwareconfig">documentation</a>
for allowed release names.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pypiPackages</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Custom Python Package Index (PyPI) packages to be installed
in the environment. Keys refer to the lowercase package name (e.g. “numpy”). Values are the lowercase extras and
version specifier (e.g. “==1.12.0”, “[devel,gcp_api]”, “[devel]&gt;=1.8.2, &lt;1.9.2”). To specify a package without
pinning it to a version specifier, use the empty string as the value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pythonVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The major version of Python used to run the Apache Airflow scheduler, worker, and webserver processes.
Can be set to ‘2’ or ‘3’. If not specified, the default is ‘2’. Cannot be updated.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.composer.Environment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.composer.Environment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_gcp.composer.Environment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.composer.Environment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_gcp.composer.GetImageVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.composer.</code><code class="sig-name descname">GetImageVersionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_versions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.composer.GetImageVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getImageVersions.</p>
<dl class="py attribute">
<dt id="pulumi_gcp.composer.GetImageVersionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.composer.GetImageVersionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.composer.GetImageVersionsResult.image_versions">
<code class="sig-name descname">image_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.composer.GetImageVersionsResult.image_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of composer image versions available in the given project and location. Each <code class="docutils literal notranslate"><span class="pre">image_version</span></code> contains:</p>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt id="pulumi_gcp.composer.get_image_versions">
<code class="sig-prename descclassname">pulumi_gcp.composer.</code><code class="sig-name descname">get_image_versions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.composer.get_image_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to available Cloud Composer versions in a region for a given project.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project</strong> (<em>str</em>) – The ID of the project to list versions in.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The location to list versions in.
If it is not provider, the provider region is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
